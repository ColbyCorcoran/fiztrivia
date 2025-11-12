import SwiftUI
import SwiftData

struct GameSettingsView: View {
    @Bindable var gameViewModel: GameViewModel
    @StateObject private var difficultyManager = DifficultyManager.shared
    @StateObject private var singleCategoryManager = SingleCategoryModeManager.shared
    @StateObject private var answeredQuestionsManager = AnsweredQuestionsManager.shared
    @Environment(\.modelContext) private var modelContext
    @State private var showingResetAlert = false
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
            Section("Game Difficulty") {
                VStack(alignment: .leading, spacing: 8) {
                    HStack {
                        Text("Difficulty Mode")
                        Spacer()
                        Picker("", selection: $difficultyManager.selectedDifficulty) {
                            ForEach(DifficultyMode.allCases, id: \.self) { difficulty in
                                Text(difficulty.rawValue).tag(difficulty)
                            }
                        }
                        .pickerStyle(MenuPickerStyle())
                        .onChange(of: difficultyManager.selectedDifficulty) { _, newValue in
                            difficultyManager.setDifficulty(newValue)
                            AnalyticsManager.shared.trackSettingChanged(setting: "difficulty_mode", value: newValue.rawValue)
                        }
                    }

                    Text(difficultyManager.selectedDifficulty.description)
                        .font(.caption)
                        .foregroundColor(.secondary)
                        .padding(.leading, 0)
                }
            }

            Section(header: Text("Game Modes"),
                   footer: Text("Focus on questions from a single category. The wheel will show subcategories instead of all categories.")) {
                Toggle("Enable Single Category Mode", isOn: $localModeEnabled)
                    .onChange(of: localModeEnabled) { oldValue, newValue in
                        handleModeChange(from: oldValue, to: newValue)
                    }

                if localModeEnabled {
                    VStack(alignment: .leading, spacing: 8) {
                        HStack {
                            Text("Selected Category")
                            Spacer()
                            Picker("", selection: $localSelectedCategory) {
                                Text("Select...").tag(nil as TriviaCategory?)
                                ForEach(TriviaCategory.allCases, id: \.self) { category in
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

            Section("Game Progress") {
                HStack {
                    Text("Questions Answered")
                    Spacer()
                    Text("\(gameViewModel.getAnsweredQuestionsCount()) / \(gameViewModel.getTotalQuestionsCount())")
                        .foregroundColor(.secondary)
                }

                HStack {
                    Text("Completion")
                    Spacer()
                    let progress = Double(gameViewModel.getAnsweredQuestionsCount()) / Double(gameViewModel.getTotalQuestionsCount())
                    Text("\(Int(progress * 100))%")
                        .foregroundColor(.secondary)
                }

                Button(action: {
                    showingResetAlert = true
                }) {
                    HStack {
                        Image(systemName: "arrow.clockwise")
                        Text("Reset All Progress")
                    }
                    .foregroundColor(.red)
                }
                .alert("Reset Progress", isPresented: $showingResetAlert) {
                    Button("Cancel", role: .cancel) { }
                    Button("Reset", role: .destructive) {
                        gameViewModel.resetAllProgress()
                        HapticManager.shared.buttonTapEffect()
                    }
                } message: {
                    Text("This will reset all answered questions and allow you to play them again. This action cannot be undone.")
                }
            }

            Section("Game Statistics") {
                HStack {
                    Text("Current Streak")
                    Spacer()
                    Text("\(gameViewModel.gameSession.currentStreak)")
                        .foregroundColor(.secondary)
                }
            }
        }
        .navigationTitle("Game Settings")
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
            let entry = LeaderboardEntry(streak: gameViewModel.gameSession.currentStreak, date: Date())
            modelContext.insert(entry)

            do {
                try modelContext.save()
                print("Saved streak to leaderboard: \(gameViewModel.gameSession.currentStreak)")
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
        GameSettingsView(gameViewModel: GameViewModel())
            .modelContainer(for: LeaderboardEntry.self, inMemory: true)
    }
}
