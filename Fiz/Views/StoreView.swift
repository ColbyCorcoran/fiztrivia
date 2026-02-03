//
//  StoreView.swift
//  Fiz
//
//  Redesigned for scalability on 2/3/26.
//

import SwiftUI
import StoreKit

struct StoreView: View {
    @Environment(\.dismiss) var dismiss
    @StateObject private var storeManager = StoreManager.shared
    @StateObject private var expansionManager = ExpansionPackManager.shared
    @StateObject private var cartManager = CartManager.shared
    @State private var showingRestoreAlert = false
    @State private var showingCart = false

    // Search & Filter State
    @State private var searchText: String = ""
    @State private var selectedTopicFilter: TopicFilter = .all
    @State private var selectedCountFilter: QuestionCountFilter = .all
    @State private var expandedPackIds: Set<String> = []

    // Keyboard Management
    @FocusState private var searchFieldFocus: Bool
    @State private var searchDebounceTask: Task<Void, Never>?

    // Computed Properties
    private var filteredPacks: [ExpansionPack] {
        var packs = expansionManager.availablePacks

        // Topic filter
        if selectedTopicFilter != .all {
            packs = packs.filter { selectedTopicFilter.matches(packId: $0.packId) }
        }

        // Question count filter
        if selectedCountFilter != .all {
            packs = packs.filter { selectedCountFilter.matches(questionCount: $0.questionCount) }
        }

        // Search filter (name, ID, description, subtopics, topic categories, contextual keywords)
        if !searchText.isEmpty {
            let query = searchText.lowercased()
            packs = packs.filter { pack in
                // Direct text matches
                let directMatch = pack.packName.lowercased().contains(query) ||
                    pack.packId.lowercased().contains(query) ||
                    pack.packDescription.lowercased().contains(query) ||
                    pack.subtopics.contains { $0.lowercased().contains(query) }

                // Topic category matches (e.g., searching "fantasy" finds Harry Potter and Pokémon)
                let categoryMatch = TopicFilter.allCases.contains { filter in
                    filter != .all &&
                    filter.rawValue.lowercased().contains(query) &&
                    filter.matches(packId: pack.packId)
                }

                // Contextual keyword matches (e.g., searching "baseball" finds Sports pack)
                let keywordMatch = TopicFilter.contextualKeywords(for: pack.packId)
                    .contains { $0.lowercased().contains(query) }

                return directMatch || categoryMatch || keywordMatch
            }
        }

        return packs
    }

    private var hasActiveFilters: Bool {
        selectedTopicFilter != .all || selectedCountFilter != .all || !searchText.isEmpty
    }

    private var activeFilterCount: Int {
        var count = 0
        if selectedTopicFilter != .all { count += 1 }
        if selectedCountFilter != .all { count += 1 }
        if !searchText.isEmpty { count += 1 }
        return count
    }

    var body: some View {
        NavigationView {
            ZStack {
                // Background gradient
                LinearGradient(
                    gradient: Gradient(colors: [
                        Color.fizBackground,
                        Color.fizBackgroundSecondary
                    ]),
                    startPoint: .topLeading,
                    endPoint: .bottomTrailing
                )
                .ignoresSafeArea()

                // Main Content
                ScrollView {
                    VStack(spacing: 16) {
                        // Header (condensed)
                        headerSection

                        // Filter Pills Row
                        filterPillsRow

                        // Active Filter Indicator
                        if hasActiveFilters {
                            activeFilterIndicator
                                .transition(.opacity.combined(with: .move(edge: .top)))
                        }

                        // Pack List or Empty State
                        if storeManager.isLoading {
                            ProgressView("Loading packs...")
                                .padding(40)
                        } else if filteredPacks.isEmpty {
                            emptyStateView
                        } else {
                            packListSection
                        }

                        // Restore Purchases Button
                        restorePurchasesButton

                        // Bottom padding for floating search bar
                        Color.clear.frame(height: 80)
                    }
                }
                .simultaneousGesture(
                    DragGesture().onChanged { _ in
                        if searchFieldFocus {
                            searchFieldFocus = false
                        }
                    }
                )

                // Floating Search Bar
                VStack {
                    Spacer()
                    bottomSearchBar
                }
            }
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                // Cart button with count
                ToolbarItem(placement: .navigationBarLeading) {
                    Button(action: {
                        HapticManager.shared.buttonTapEffect()
                        showingCart = true
                    }) {
                        HStack(spacing: 4) {
                            Image(systemName: "bag")
                                .font(.body.weight(.semibold))

                            if cartManager.itemCount > 0 {
                                Text("(\(cartManager.itemCount) \(cartManager.itemCount == 1 ? "Pack" : "Packs"))")
                                    .font(.caption)
                                    .fontWeight(.medium)
                            }
                        }
                    }
                    .tint(.fizOrange)
                }

                // Done button
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button(action: {
                        dismiss()
                    }) {
                        Image(systemName: "checkmark")
                            .font(.body.weight(.semibold))
                    }
                    .tint(.fizOrange)
                }
            }
            .sheet(isPresented: $showingCart) {
                CartView()
                    .presentationDragIndicator(.visible)
            }
            .alert("Purchases Restored", isPresented: $showingRestoreAlert) {
                Button("OK", role: .cancel) { }
            } message: {
                Text("Your purchases have been restored successfully.")
            }
        }
        .onAppear {
            AnalyticsManager.shared.trackStoreViewed()
        }
        .onDisappear {
            // Track store dismissal with cart context
            let hadItems = cartManager.itemCount > 0
            AnalyticsManager.shared.trackStoreDismissed(hadItemsInCart: hadItems, cartItemCount: cartManager.itemCount)
        }
    }

    // MARK: - Header Section
    private var headerSection: some View {
        VStack(spacing: 8) {
            Image(systemName: "rectangle.stack.badge.plus")
                .font(.system(size: 44))
                .foregroundColor(.fizOrange)

            Text("Expansion Packs")
                .font(.title2)
                .fontWeight(.bold)
                .foregroundColor(.fizBrown)

            Text("\(filteredPacks.count) pack\(filteredPacks.count == 1 ? "" : "s") available")
                .font(.subheadline)
                .foregroundColor(.fizBrown.opacity(0.7))
        }
        .padding(.top, 12)
        .padding(.bottom, 8)
    }

    // MARK: - Filter Pills Row
    private var filterPillsRow: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            HStack(spacing: 10) {
                // Topic Filter Menu
                Menu {
                    ForEach(TopicFilter.allCases) { filter in
                        Button(action: {
                            withAnimation(.easeInOut(duration: 0.3)) {
                                selectedTopicFilter = filter
                            }
                            HapticManager.shared.lightImpact()
                            AnalyticsManager.shared.trackStoreFilterUsed(
                                filterType: "topic",
                                filterValue: filter.rawValue
                            )
                        }) {
                            HStack {
                                Text(filter.rawValue)
                                if selectedTopicFilter == filter {
                                    Image(systemName: "checkmark")
                                }
                            }
                        }
                    }
                } label: {
                    FilterPillLabel(
                        icon: "tag.fill",
                        text: selectedTopicFilter.rawValue,
                        isActive: selectedTopicFilter != .all
                    )
                }
                .buttonStyle(.plain)

                // Question Count Filter Menu
                Menu {
                    ForEach(QuestionCountFilter.allCases) { filter in
                        Button(action: {
                            withAnimation(.easeInOut(duration: 0.3)) {
                                selectedCountFilter = filter
                            }
                            HapticManager.shared.lightImpact()
                            AnalyticsManager.shared.trackStoreFilterUsed(
                                filterType: "question_count",
                                filterValue: filter.rawValue
                            )
                        }) {
                            HStack {
                                Text(filter.rawValue)
                                if selectedCountFilter == filter {
                                    Image(systemName: "checkmark")
                                }
                            }
                        }
                    }
                } label: {
                    FilterPillLabel(
                        icon: "number",
                        text: selectedCountFilter.rawValue,
                        isActive: selectedCountFilter != .all
                    )
                }
                .buttonStyle(.plain)

                // Clear All Filters
                if hasActiveFilters {
                    Button(action: {
                        withAnimation(.easeInOut(duration: 0.3)) {
                            searchText = ""
                            selectedTopicFilter = .all
                            selectedCountFilter = .all
                        }
                        HapticManager.shared.lightImpact()
                        AnalyticsManager.shared.trackStoreFilterCleared()
                    }) {
                        FilterPillLabel(
                            icon: "xmark.circle.fill",
                            text: "Clear All",
                            isActive: false,
                            color: .red
                        )
                    }
                    .transition(.opacity)
                }
            }
            .padding(.horizontal)
            .padding(.vertical, 3)
        }
        .padding(.vertical, 6)
    }

    // MARK: - Active Filter Indicator
    private var activeFilterIndicator: some View {
        HStack {
            Image(systemName: "line.3.horizontal.decrease.circle")
                .font(.caption)
            Text("\(activeFilterCount) filter\(activeFilterCount == 1 ? "" : "s") active • \(filteredPacks.count) result\(filteredPacks.count == 1 ? "" : "s")")
                .font(.caption)
                .fontWeight(.medium)
        }
        .foregroundColor(.fizOrange)
        .padding(.horizontal)
        .padding(.bottom, 4)
    }

    // MARK: - Pack List Section
    private var packListSection: some View {
        LazyVStack(spacing: 12) {
            ForEach(filteredPacks) { pack in
                CollapsiblePackCard(
                    pack: pack,
                    isExpanded: Binding(
                        get: { expandedPackIds.contains(pack.packId) },
                        set: { isExpanded in
                            if isExpanded {
                                expandedPackIds.insert(pack.packId)
                            } else {
                                expandedPackIds.remove(pack.packId)
                            }
                        }
                    ),
                    onInstall: {
                        expansionManager.installPack(packId: pack.packId)
                        HapticManager.shared.correctAnswerEffect()
                        AnalyticsManager.shared.trackExpansionPackInstalled(
                            packId: pack.packId
                        )
                    },
                    onUninstall: {
                        expansionManager.uninstallPack(packId: pack.packId)
                        HapticManager.shared.lightImpact()
                        AnalyticsManager.shared.trackExpansionPackUninstalled(
                            packId: pack.packId
                        )
                    }
                )
                .transition(.opacity.combined(with: .scale(scale: 0.95)))
            }
        }
        .padding(.horizontal)
        .animation(.easeInOut(duration: 0.3), value: filteredPacks.map { $0.id })
    }

    // MARK: - Empty State View
    private var emptyStateView: some View {
        VStack(spacing: 16) {
            Image(systemName: "magnifyingglass")
                .font(.system(size: 50))
                .foregroundColor(.fizBrown.opacity(0.3))

            Text("No packs found")
                .font(.title3)
                .fontWeight(.semibold)
                .foregroundColor(.fizBrown)

            Text("Try adjusting your filters or search")
                .font(.subheadline)
                .foregroundColor(.fizBrown.opacity(0.6))
                .multilineTextAlignment(.center)

            if hasActiveFilters {
                Button(action: {
                    searchText = ""
                    selectedTopicFilter = .all
                    selectedCountFilter = .all
                    HapticManager.shared.lightImpact()
                }) {
                    Text("Clear All Filters")
                        .font(.headline)
                        .padding(.horizontal, 20)
                        .padding(.vertical, 12)
                        .background(Color.fizOrange)
                        .foregroundColor(.white)
                        .cornerRadius(12)
                }
                .padding(.top, 8)
            }
        }
        .padding(40)
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }

    // MARK: - Restore Purchases Button
    private var restorePurchasesButton: some View {
        Button(action: {
            Task {
                let success = await storeManager.restorePurchases()
                if success {
                    showingRestoreAlert = true
                }
            }
        }) {
            Text("Restore Purchases")
                .font(.footnote)
                .foregroundColor(.fizBrown.opacity(0.7))
        }
        .padding(.top, 10)
        .padding(.bottom, 30)
    }

    // MARK: - Bottom Search Bar
    private var bottomSearchBar: some View {
        HStack(spacing: 12) {
            Image(systemName: "magnifyingglass")
                .font(.body)

            TextField("Search", text: $searchText)
                .textFieldStyle(.plain)
                .font(.body)
                .autocorrectionDisabled()
                .textInputAutocapitalization(.never)
                .focused($searchFieldFocus)
                .onChange(of: searchText) { oldValue, newValue in
                    // Debounce search analytics
                    searchDebounceTask?.cancel()
                    searchDebounceTask = Task {
                        try? await Task.sleep(nanoseconds: 300_000_000)
                        if !newValue.isEmpty {
                            AnalyticsManager.shared.trackStoreSearchUsed(
                                resultCount: filteredPacks.count
                            )
                        }
                    }
                }

            if !searchText.isEmpty {
                Button(action: {
                    searchText = ""
                    searchFieldFocus = false
                    HapticManager.shared.lightImpact()
                }) {
                    Image(systemName: "xmark.circle.fill")
                        .font(.body)
                }
                .buttonStyle(.plain)
                .transition(.scale.combined(with: .opacity))
            }
        }
        .padding(.horizontal, 16)
        .padding(.vertical, 12)
        .glassSearchBarStyle()
        .padding(.horizontal, 16)
        .padding(.bottom, 12)
    }
}

#Preview {
    StoreView()
}

// MARK: - Glass Search Bar Style
extension View {
    @ViewBuilder
    func glassSearchBarStyle() -> some View {
        if #available(iOS 26, *) {
            self
                .background(.thinMaterial, in: RoundedRectangle(cornerRadius: 20, style: .continuous))
                .buttonBorderShape(.capsule)
                .controlSize(.regular)
        } else {
            // iOS 18 fallback
            self
                .background(
                    RoundedRectangle(cornerRadius: 20, style: .continuous)
                        .fill(Color(.secondarySystemBackground))
                )
        }
    }
}
