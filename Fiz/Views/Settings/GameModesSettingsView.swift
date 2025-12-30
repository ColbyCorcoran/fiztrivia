import SwiftUI
import SwiftData

struct GameModesSettingsView: View {
    @Bindable var gameViewModel: GameViewModel
    @StateObject private var singleCategoryManager = SingleCategoryModeManager.shared
    @Environment(\.modelContext) private var modelContext
    @Environment(\.sizeCategory) private var sizeCategory

    private var backgroundGradient: some View {
        Color(.systemGroupedBackground)
            .ignoresSafeArea()
    }
    @State private var showingStreakAlert = false
    @State private var pendingModeChange: Bool? = nil
    @State private var previousModeValue: Bool? = nil
    @State private var pendingCategoryChange: TriviaCategory? = nil
    @State private var previousCategory: TriviaCategory? = nil
    @State private var localModeEnabled: Bool = false
    @State private var localSelectedCategory: TriviaCategory? = nil
    @State private var isInitialLoad: Bool = true
    @State private var isApplyingChanges: Bool = false

    var body: some View {
        Form {
            Section(footer: Text("Focus on questions from a single category. The wheel will show subcategories instead of all categories.")) {
                Toggle("Enable Single Category Mode", isOn: $localModeEnabled)
                    .onChange(of: localModeEnabled) { oldValue, newValue in
                        handleModeChange(from: oldValue, to: newValue)
                    }

                if localModeEnabled {
                    VStack(alignment: .leading, spacing: 8) {
                        HStack {
                            // Hide label at accessibility sizes to reduce cramping
                            if !sizeCategory.isAccessibilitySize {
                                Text("Selected Category")
                                Spacer()
                            }
                            Picker("", selection: $localSelectedCategory) {
                                Text("Select...").tag(nil as TriviaCategory?)
                                ForEach(CategorySelectionManager.shared.selectedCategories.sorted(by: { $0.rawValue < $1.rawValue }), id: \.self) { category in
                                    HStack {
                                        Image(systemName: category.icon)
                                        Text(category.rawValue)
                                    }
                                    .tag(category as TriviaCategory?)
                                }
                            }
                            .pickerStyle(MenuPickerStyle())
                            .onChange(of: localSelectedCategory) { oldValue, newValue in
                                handleCategoryChange(from: oldValue, to: newValue)
                            }
                        }

                        if let selectedCategory = localSelectedCategory {
                            Text("Wheel will show \(selectedCategory.rawValue) subcategories")
                                .font(.caption)
                                .foregroundColor(.secondary)
                        } else {
                            Text("Select a category to begin")
                                .font(.caption)
                                .foregroundColor(.orange)
                        }
                    }
                }
            }
        }
        .scrollContentBackground(.hidden)
        .background(backgroundGradient)
        .navigationTitle("Game Modes")
        .navigationBarTitleDisplayMode(.large)
        .alert("Save Current Streak?", isPresented: $showingStreakAlert) {
            Button("Cancel", role: .cancel) {
                handleAlertCancel()
            }
            Button("Discard & Continue") {
                applyPendingChanges(saveStreak: false)
            }
            Button("Save & Continue") {
                applyPendingChanges(saveStreak: true)
            }
        } message: {
            Text("You currently have a streak of \(gameViewModel.gameSession.currentStreak). Would you like to save it to the leaderboard before switching?")
        }
        .onAppear {
            isInitialLoad = true
            localModeEnabled = singleCategoryManager.isEnabled
            localSelectedCategory = singleCategoryManager.selectedCategory
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.1) {
                isInitialLoad = false
            }
        }
    }

    private func handleAlertCancel() {
        if let previousMode = previousModeValue {
            localModeEnabled = previousMode
            previousModeValue = nil
        }

        if let previousCat = previousCategory {
            localSelectedCategory = previousCat
            previousCategory = nil
        }

        pendingModeChange = nil
        pendingCategoryChange = nil
    }

    private func handleModeChange(from oldValue: Bool, to newValue: Bool) {
        guard !isInitialLoad && !isApplyingChanges else { return }

        if gameViewModel.gameSession.currentStreak > 0 {
            previousModeValue = oldValue
            pendingModeChange = newValue
            DispatchQueue.main.async {
                self.showingStreakAlert = true
            }
        } else {
            singleCategoryManager.setModeEnabled(newValue)
            if !newValue {
                singleCategoryManager.setSelectedCategory(nil)
                localSelectedCategory = nil
                AnalyticsManager.shared.trackSingleCategoryModeDisabled()
            }
        }
    }

    private func handleCategoryChange(from oldValue: TriviaCategory?, to newValue: TriviaCategory?) {
        guard !isInitialLoad && !isApplyingChanges else { return }

        if gameViewModel.gameSession.currentStreak > 0 && oldValue != nil && oldValue != newValue {
            previousCategory = oldValue
            pendingCategoryChange = newValue
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) {
                self.showingStreakAlert = true
            }
        } else {
            singleCategoryManager.setSelectedCategory(newValue)
            if let category = newValue {
                AnalyticsManager.shared.trackSingleCategoryModeEnabled(category: category.rawValue)
            }
        }
    }

    private func applyPendingChanges(saveStreak: Bool) {
        isApplyingChanges = true

        if saveStreak && gameViewModel.gameSession.currentStreak > 0 {
            // Capture CURRENT mode/category before applying changes
            let gameMode: String
            let categoryName: String?

            if singleCategoryManager.isEnabled {
                gameMode = "Single Category"
                categoryName = singleCategoryManager.selectedCategory?.rawValue
            } else {
                gameMode = "Regular"
                categoryName = nil
            }

            let entry = LeaderboardEntry(
                streak: gameViewModel.gameSession.currentStreak,
                date: Date(),
                gameMode: gameMode,
                categoryName: categoryName
            )
            modelContext.insert(entry)

            do {
                try modelContext.save()
                print("Saved streak to leaderboard: \(gameViewModel.gameSession.currentStreak) (\(gameMode)\(categoryName.map { " - \($0)" } ?? ""))")
            } catch {
                print("Failed to save streak: \(error)")
            }
        }

        gameViewModel.gameSession.currentStreak = 0
        StreakPersistenceManager.clearCurrentStreak()

        if let modeChange = pendingModeChange {
            singleCategoryManager.setModeEnabled(modeChange)
            if !modeChange {
                singleCategoryManager.setSelectedCategory(nil)
            }
            pendingModeChange = nil
        }

        if let categoryChange = pendingCategoryChange {
            singleCategoryManager.setSelectedCategory(categoryChange)
            pendingCategoryChange = nil
        }

        previousModeValue = nil
        previousCategory = nil

        HapticManager.shared.buttonTapEffect()

        DispatchQueue.main.asyncAfter(deadline: .now() + 0.1) {
            self.localModeEnabled = self.singleCategoryManager.isEnabled
            self.localSelectedCategory = self.singleCategoryManager.selectedCategory
            self.isApplyingChanges = false
        }
    }
}

#Preview {
    NavigationStack {
        GameModesSettingsView(gameViewModel: GameViewModel())
            .modelContainer(for: LeaderboardEntry.self, inMemory: true)
    }
}
