//
//  StoreView.swift
//  Fiz
//
//  Created by Claude Code on 12/31/24.
//

import SwiftUI
import StoreKit

struct StoreView: View {
    @Environment(\.dismiss) var dismiss
    @StateObject private var storeManager = StoreManager.shared
    @StateObject private var expansionManager = ExpansionPackManager.shared
    @State private var showingRestoreAlert = false
    @State private var purchasingPackId: String?

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

                ScrollView {
                    VStack(spacing: 20) {
                        // Header
                        VStack(spacing: 8) {
                            Image(systemName: "bag")
                                .font(.system(size: 50))
                                .foregroundColor(.fizOrange)

                            Text("Expansion Packs")
                                .font(.largeTitle)
                                .fontWeight(.bold)
                                .foregroundColor(.fizBrown)

                            Text("Unlock new topics and questions")
                                .font(.subheadline)
                                .foregroundColor(.fizBrown.opacity(0.7))
                        }
                        .padding(.top, 20)

                        // Pack Cards
                        if storeManager.isLoading {
                            ProgressView("Loading packs...")
                                .padding(40)
                        } else if expansionManager.availablePacks.isEmpty {
                            Text("No expansion packs available")
                                .foregroundColor(.fizBrown.opacity(0.6))
                                .padding(40)
                        } else {
                            ForEach(expansionManager.availablePacks) { pack in
                                ExpansionPackCard(
                                    pack: pack,
                                    isPurchasing: purchasingPackId == pack.packId,
                                    onPurchase: {
                                        await purchasePack(pack)
                                    },
                                    onInstall: {
                                        installPack(pack)
                                    },
                                    onUninstall: {
                                        uninstallPack(pack)
                                    }
                                )
                            }
                        }

                        // Restore Purchases Button
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
                    .padding(.horizontal)
                }
            }
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
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
            .alert("Purchases Restored", isPresented: $showingRestoreAlert) {
                Button("OK", role: .cancel) { }
            } message: {
                Text("Your purchases have been restored successfully.")
            }
        }
        .onAppear {
            AnalyticsManager.shared.trackStoreViewed()
        }
    }

    private func purchasePack(_ pack: ExpansionPack) async {
        guard let product = storeManager.product(for: pack.packId) else { return }

        purchasingPackId = pack.packId
        let success = await storeManager.purchase(product)
        purchasingPackId = nil

        if success {
            // Auto-install after purchase
            expansionManager.installPack(packId: pack.packId)
            HapticManager.shared.correctAnswerEffect()
            AnalyticsManager.shared.trackExpansionPackInstalled(packId: pack.packId)
        }
    }

    private func installPack(_ pack: ExpansionPack) {
        expansionManager.installPack(packId: pack.packId)
        HapticManager.shared.mediumImpact()
        AnalyticsManager.shared.trackExpansionPackInstalled(packId: pack.packId)
    }

    private func uninstallPack(_ pack: ExpansionPack) {
        expansionManager.uninstallPack(packId: pack.packId)
        HapticManager.shared.lightImpact()
        AnalyticsManager.shared.trackExpansionPackUninstalled(packId: pack.packId)
    }
}

// MARK: - Expansion Pack Card

struct ExpansionPackCard: View {
    let pack: ExpansionPack
    let isPurchasing: Bool
    let onPurchase: () async -> Void
    let onInstall: () -> Void
    let onUninstall: () -> Void

    @StateObject private var storeManager = StoreManager.shared
    @StateObject private var expansionManager = ExpansionPackManager.shared

    private var isPurchased: Bool {
        expansionManager.isPurchased(packId: pack.packId)
    }

    private var isInstalled: Bool {
        expansionManager.isInstalled(packId: pack.packId)
    }

    private var product: Product? {
        storeManager.product(for: pack.packId)
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            // Debug logging
            let _ = print("📦 Pack: \(pack.packName), Subtopics: \(pack.subtopics)")

            // Header with icon and title
            HStack(spacing: 12) {
                Image(systemName: pack.icon)
                    .font(.system(size: 32))
                    .foregroundColor(.fizOrange)
                    .frame(width: 50, height: 50)

                VStack(alignment: .leading, spacing: 4) {
                    Text(pack.packName)
                        .font(.title2)
                        .fontWeight(.bold)
                        .foregroundColor(.fizBrown)

                    Text("\(pack.questionCount) questions")
                        .font(.subheadline)
                        .foregroundColor(.fizBrown.opacity(0.7))
                }

                Spacer()

                // Price or status badge
                if isPurchased {
                    if isInstalled {
                        StatusBadge(text: "Installed", color: .green)
                    } else {
                        StatusBadge(text: "Owned", color: .blue)
                    }
                } else if let product = product {
                    Text(product.displayPrice)
                        .font(.title3)
                        .fontWeight(.bold)
                        .foregroundColor(.fizOrange)
                }
            }

            // Description
            Text(pack.packDescription)
                .font(.body)
                .foregroundColor(.fizBrown.opacity(0.8))
                .fixedSize(horizontal: false, vertical: true)

            // Subtopics
            VStack(alignment: .leading, spacing: 8) {
                Text("Subtopics:")
                    .font(.caption)
                    .fontWeight(.semibold)
                    .foregroundColor(.fizBrown)

                // Debug: Show count
                if pack.subtopics.isEmpty {
                    Text("No subtopics available")
                        .font(.caption)
                        .foregroundColor(.red)
                } else {
                    // Simple wrapping layout with LazyVGrid
                    let columns = [
                        GridItem(.adaptive(minimum: 100, maximum: 160), spacing: 8)
                    ]

                    LazyVGrid(columns: columns, alignment: .leading, spacing: 8) {
                        ForEach(pack.subtopics, id: \.self) { subtopic in
                            Text(subtopic)
                                .font(.caption)
                                .fontWeight(.medium)
                                .foregroundColor(.fizBrown)
                                .multilineTextAlignment(.center)
                                .lineLimit(2)
                                .frame(maxWidth: .infinity, minHeight: 44, alignment: .center)
                                .padding(.horizontal, 12)
                                .padding(.vertical, 8)
                                .background(
                                    RoundedRectangle(cornerRadius: 8)
                                        .fill(Color.fizOrange.opacity(0.15))
                                )
                        }
                    }
                }
            }

            // Difficulty breakdown
            HStack(spacing: 16) {
                DifficultyPill(difficulty: "Easy", count: pack.difficulty.easy, color: .green)
                DifficultyPill(difficulty: "Medium", count: pack.difficulty.medium, color: .orange)
                DifficultyPill(difficulty: "Hard", count: pack.difficulty.hard, color: .red)
            }

            // Action Button
            if isPurchased {
                if isInstalled {
                    Button(action: onUninstall) {
                        Text("Uninstall")
                            .font(.headline)
                            .frame(maxWidth: .infinity)
                            .padding()
                            .background(Color.fizBrown.opacity(0.2))
                            .foregroundColor(.fizBrown)
                            .cornerRadius(12)
                    }
                } else {
                    Button(action: onInstall) {
                        HStack {
                            Image(systemName: "arrow.down.circle.fill")
                            Text("Install")
                        }
                        .font(.headline)
                        .frame(maxWidth: .infinity)
                        .padding()
                        .background(Color.fizOrange)
                        .foregroundColor(.white)
                        .cornerRadius(12)
                    }
                }
            } else {
                Button(action: {
                    Task {
                        await onPurchase()
                    }
                }) {
                    HStack {
                        if isPurchasing {
                            ProgressView()
                                .progressViewStyle(CircularProgressViewStyle(tint: .white))
                        } else {
                            Image(systemName: "cart.fill")
                            if let product = product {
                                Text("Purchase for \(product.displayPrice)")
                            } else {
                                Text("Purchase")
                            }
                        }
                    }
                    .font(.headline)
                    .frame(maxWidth: .infinity)
                    .padding()
                    .background(isPurchasing ? Color.gray : Color.fizOrange)
                    .foregroundColor(.white)
                    .cornerRadius(12)
                }
                .disabled(isPurchasing)

                // Free preview note
                Text("Includes \(pack.freePreviewCount) free preview questions")
                    .font(.caption)
                    .foregroundColor(.fizBrown.opacity(0.6))
                    .padding(.top, 4)
            }
        }
        .padding()
        .background(Color.white.opacity(0.8))
        .cornerRadius(16)
        .shadow(color: Color.black.opacity(0.1), radius: 8, x: 0, y: 4)
        .onAppear {
            AnalyticsManager.shared.trackExpansionPackViewed(packId: pack.packId, packName: pack.packName)
        }
    }
}

// MARK: - Helper Views

struct StatusBadge: View {
    let text: String
    let color: Color

    var body: some View {
        Text(text)
            .font(.caption)
            .fontWeight(.semibold)
            .padding(.horizontal, 10)
            .padding(.vertical, 5)
            .background(color.opacity(0.2))
            .foregroundColor(color)
            .cornerRadius(8)
    }
}

struct DifficultyPill: View {
    let difficulty: String
    let count: Int
    let color: Color

    var body: some View {
        HStack(spacing: 4) {
            Circle()
                .fill(color)
                .frame(width: 8, height: 8)
            Text("\(count)")
                .font(.caption)
                .fontWeight(.semibold)
            Text(difficulty)
                .font(.caption)
        }
        .foregroundColor(.fizBrown.opacity(0.7))
    }
}

// FlowLayout for wrapping subtopic tags
struct FlowLayout: Layout {
    var spacing: CGFloat = 8

    func sizeThatFits(proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) -> CGSize {
        let result = FlowResult(
            in: proposal.replacingUnspecifiedDimensions().width,
            subviews: subviews,
            spacing: spacing
        )
        return result.size
    }

    func placeSubviews(in bounds: CGRect, proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) {
        let result = FlowResult(
            in: bounds.width,
            subviews: subviews,
            spacing: spacing
        )
        for (index, subview) in subviews.enumerated() {
            subview.place(at: result.positions[index], proposal: .unspecified)
        }
    }

    struct FlowResult {
        var size: CGSize = .zero
        var positions: [CGPoint] = []

        init(in maxWidth: CGFloat, subviews: Subviews, spacing: CGFloat) {
            var x: CGFloat = 0
            var y: CGFloat = 0
            var lineHeight: CGFloat = 0

            for subview in subviews {
                let size = subview.sizeThatFits(.unspecified)

                if x + size.width > maxWidth && x > 0 {
                    x = 0
                    y += lineHeight + spacing
                    lineHeight = 0
                }

                positions.append(CGPoint(x: x, y: y))
                lineHeight = max(lineHeight, size.height)
                x += size.width + spacing
            }

            self.size = CGSize(width: maxWidth, height: y + lineHeight)
        }
    }
}

#Preview {
    StoreView()
}
