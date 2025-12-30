import SwiftUI
import SwiftData

struct GameModesSettingsView: View {
    @Bindable var gameViewModel: GameViewModel
    @StateObject private var gameModeManager = GameModeManager.shared
    @Environment(\.modelContext) private var modelContext
    @Environment(\.sizeCategory) private var sizeCategory
    @Environment(\.dismiss) private var dismiss

    @State private var showingStreakAlert = false
    @State private var showingIncompleteSelectionAlert = false
    @State private var pendingMode: GameMode?
    @State private var previousMode: GameMode = .regular
    @State private var pendingCategory: TriviaCategory?
    @State private var previousCategory: TriviaCategory?
    @State private var localSelectedMode: GameMode = .regular
    @State private var localSelectedCategory: TriviaCategory? = nil
    @State private var isInitialLoad = true
    @State private var isApplyingChanges = false

    private var backgroundGradient: some View {
        Color(.systemGroupedBackground)
            .ignoresSafeArea()
    }

    // Check if current selection is complete and valid
    private var isSelectionComplete: Bool {
        switch localSelectedMode {
        case .regular:
            return true
        case .singleCategory:
            return localSelectedCategory != nil
        // Future modes:
        // case .singleTopic:
        //     return localSelectedTopic != nil
        // case .seasonal:
        //     return true
        }
    }

    var body: some View {
        Form {
            // Game Mode Selection Section
            Section(header: Text("Select Game Mode"),
                    footer: Text("Choose how you want to play trivia. Switching modes will reset your current streak.")) {
                ForEach(GameMode.allCases) { mode in
                    GameModeRow(
                        mode: mode,
                        isSelected: localSelectedMode == mode,
                        onSelect: {
                            handleModeSelection(mode)
                        }
                    )
                }
            }

            // Conditional Settings Based on Selected Mode
            if localSelectedMode == .singleCategory {
                Section(header: Text("Category Settings"),
                        footer: Text("Select which category to focus on. The wheel will show subcategories instead of all categories.")) {
                    VStack(alignment: .leading, spacing: 8) {
                        HStack {
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

            // Future: Single Topic settings section would go here
            // if localSelectedMode == .singleTopic { ... }

            // Future: Seasonal settings section would go here
            // if localSelectedMode == .seasonal { ... }
        }
        .scrollContentBackground(.hidden)
        .background(backgroundGradient)
        .navigationTitle("Game Modes")
        .navigationBarTitleDisplayMode(.large)
        .navigationBarBackButtonHidden(!isSelectionComplete)
        .toolbar {
            if !isSelectionComplete {
                ToolbarItem(placement: .navigationBarLeading) {
                    Button(action: {
                        showingIncompleteSelectionAlert = true
                    }) {
                        Image(systemName: "chevron.left")
                            .font(.body.weight(.semibold))
                    }
                }
            }
        }
        .alert("Selection Required", isPresented: $showingIncompleteSelectionAlert) {
            Button("OK", role: .cancel) { }
        } message: {
            Text("Please select a category before leaving, or switch back to Regular mode.")
        }
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
            localSelectedMode = gameModeManager.selectedMode
            localSelectedCategory = gameModeManager.selectedCategory
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.1) {
                isInitialLoad = false
            }
        }
    }

    // MARK: - Event Handlers

    private func handleModeSelection(_ mode: GameMode) {
        guard !isInitialLoad && !isApplyingChanges else { return }
        guard mode != localSelectedMode else { return }

        if gameViewModel.gameSession.currentStreak > 0 {
            previousMode = localSelectedMode
            pendingMode = mode
            DispatchQueue.main.async {
                self.showingStreakAlert = true
            }
        } else {
            gameModeManager.setMode(mode)
            localSelectedMode = mode

            // Clear settings for other modes
            if mode != .singleCategory {
                gameModeManager.setSelectedCategory(nil)
                localSelectedCategory = nil
            }

            AnalyticsManager.shared.trackSettingChanged(setting: "game_mode", value: mode.rawValue)
        }
    }

    private func handleCategoryChange(from oldValue: TriviaCategory?, to newValue: TriviaCategory?) {
        guard !isInitialLoad && !isApplyingChanges else { return }

        if gameViewModel.gameSession.currentStreak > 0 && oldValue != nil && oldValue != newValue {
            previousCategory = oldValue
            pendingCategory = newValue
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) {
                self.showingStreakAlert = true
            }
        } else {
            gameModeManager.setSelectedCategory(newValue)
            if let category = newValue {
                AnalyticsManager.shared.trackSettingChanged(setting: "single_category_selected", value: category.rawValue)
            }
        }
    }

    private func handleAlertCancel() {
        if let pending = pendingMode {
            localSelectedMode = previousMode
            pendingMode = nil
        }

        if let previousCat = previousCategory {
            localSelectedCategory = previousCat
            previousCategory = nil
        }

        pendingCategory = nil

        // Track streak save decision: cancelled
        AnalyticsManager.shared.trackStreakSaveDecision(action: "cancelled", streakValue: gameViewModel.gameSession.currentStreak)
    }

    private func applyPendingChanges(saveStreak: Bool) {
        isApplyingChanges = true

        // Track streak save decision
        let action = saveStreak ? "saved" : "discarded"
        AnalyticsManager.shared.trackStreakSaveDecision(action: action, streakValue: gameViewModel.gameSession.currentStreak)

        if saveStreak && gameViewModel.gameSession.currentStreak > 0 {
            // Save streak with current mode info
            let gameMode = gameModeManager.selectedMode.rawValue
            let categoryName = gameModeManager.selectedCategory?.rawValue

            let entry = LeaderboardEntry(
                streak: gameViewModel.gameSession.currentStreak,
                date: Date(),
                gameMode: gameMode,
                categoryName: categoryName
            )
            modelContext.insert(entry)

            do {
                try modelContext.save()
                print("Saved streak: \(gameViewModel.gameSession.currentStreak) (\(gameMode)\(categoryName.map { " - \($0)" } ?? ""))")
            } catch {
                print("Failed to save streak: \(error)")
            }
        }

        // Reset streak
        gameViewModel.gameSession.currentStreak = 0
        StreakPersistenceManager.clearCurrentStreak()

        // Apply pending mode change
        if let newMode = pendingMode {
            gameModeManager.setMode(newMode)
            localSelectedMode = newMode

            if newMode != .singleCategory {
                gameModeManager.setSelectedCategory(nil)
                localSelectedCategory = nil
            }

            pendingMode = nil
        }

        // Apply pending category change
        if let newCategory = pendingCategory {
            gameModeManager.setSelectedCategory(newCategory)
            localSelectedCategory = newCategory
            pendingCategory = nil
        }

        previousMode = localSelectedMode
        previousCategory = nil

        HapticManager.shared.buttonTapEffect()

        DispatchQueue.main.asyncAfter(deadline: .now() + 0.1) {
            self.isApplyingChanges = false
        }
    }
}

// MARK: - Game Mode Row Component

struct GameModeRow: View {
    let mode: GameMode
    let isSelected: Bool
    let onSelect: () -> Void

    var body: some View {
        Button(action: onSelect) {
            HStack(spacing: 12) {
                Image(systemName: mode.icon)
                    .font(.title3)
                    .foregroundColor(.fizOrange)
                    .frame(width: 28)

                VStack(alignment: .leading, spacing: 2) {
                    Text(mode.rawValue)
                        .font(.body)
                        .foregroundColor(.primary)

                    Text(mode.description)
                        .font(.caption)
                        .foregroundColor(.secondary)
                }

                Spacer()

                if isSelected {
                    Image(systemName: "checkmark.circle.fill")
                        .font(.title3)
                        .foregroundColor(.fizOrange)
                } else {
                    Image(systemName: "circle")
                        .font(.title3)
                        .foregroundColor(.secondary.opacity(0.3))
                }
            }
            .contentShape(Rectangle())
        }
        .buttonStyle(.plain)
    }
}

#Preview {
    NavigationStack {
        GameModesSettingsView(gameViewModel: GameViewModel())
            .modelContainer(for: LeaderboardEntry.self, inMemory: true)
    }
}
