import SwiftUI
import SwiftData

struct GameModesSettingsView: View {
    @Bindable var gameViewModel: GameViewModel
    @StateObject private var gameModeManager = GameModeManager.shared
    @StateObject private var answeredQuestionsManager = AnsweredQuestionsManager.shared
    @StateObject private var difficultyManager = DifficultyManager.shared
    @Environment(\.modelContext) private var modelContext
    @Environment(\.sizeCategory) private var sizeCategory
    @Environment(\.dismiss) private var dismiss

    @State private var showingStreakAlert = false
    @State private var showingIncompleteSelectionAlert = false
    @State private var pendingMode: GameMode?
    @State private var previousMode: GameMode = .multiCategory
    @State private var pendingCategory: TriviaCategory?
    @State private var previousCategory: TriviaCategory?
    @State private var localSelectedMode: GameMode = .multiCategory
    @State private var localSelectedCategory: TriviaCategory? = nil
    @State private var localSelectedTopic: String? = nil
    @State private var isInitialLoad = true
    @State private var isApplyingChanges = false

    // Category selection state
    @StateObject private var categoryManager = CategorySelectionManager.shared
    @State private var showMaxReachedAlert = false
    @State private var showMinimumAlert = false
    @State private var showActiveCategoryAlert = false
    @State private var confirmationMessage: String? = nil

    // Reset functionality state
    @State private var showingTopicResetAlert = false
    @State private var topicToReset: String? = nil
    @State private var topicResetCount: Int = 0
    @State private var topicResetName: String = ""

    private var backgroundGradient: some View {
        Color(.systemGroupedBackground)
            .ignoresSafeArea()
    }

    // Check if current selection is complete and valid
    private var isSelectionComplete: Bool {
        switch localSelectedMode {
        case .multiCategory:
            return true
        case .singleCategory:
            return localSelectedCategory != nil
        case .singleTopic:
            return localSelectedTopic != nil
        // Future modes:
        // case .seasonal:
        //     return true
        }
    }

    // MARK: - View Sections

    @ViewBuilder
    private var gameModeSelectionSection: some View {
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
    }

    @ViewBuilder
    private var multiCategorySettingsSection: some View {
        if localSelectedMode == .multiCategory {
            // Category count display
            Section {
                HStack {
                    Text("Selected Categories")
                        .font(.headline)
                    Spacer()
                    Text("\(categoryManager.selectedCategories.count)/\(CategorySelectionManager.maximumCategories)")
                        .font(.headline)
                        .foregroundColor(categoryManager.selectedCategories.count >= CategorySelectionManager.maximumCategories ? .orange : .secondary)
                }
                .padding(.vertical, 4)
            }

            categoryToggleSection

            categoryActionButtonsSection
        }
    }

    @ViewBuilder
    private var categoryToggleSection: some View {
        Section(footer: Text("Select \(CategorySelectionManager.minimumCategories)-\(CategorySelectionManager.maximumCategories) categories to appear on the wheel. Deselected categories will be hidden.")) {
            ForEach(TriviaCategory.allCases, id: \.self) { category in
                CategorySelectionRow(
                    category: category,
                    isSelected: categoryManager.isSelected(category),
                    canToggle: categoryManager.canToggle(category),
                    onToggle: { handleCategoryToggle(category) }
                )
            }
        }
    }

    @ViewBuilder
    private var categoryActionButtonsSection: some View {
        Section {
            // Save current selection as user's custom default
            Button(action: {
                categoryManager.saveCurrentAsDefault()
                HapticManager.shared.buttonTapEffect()
                showConfirmation("Selection saved as your new default ✓")
            }) {
                HStack {
                    Image(systemName: "bookmark.fill")
                    Text("Save selection as my default")
                }
                .foregroundColor(.fizOrange)
            }

            // Reset to user's custom default (only shown if they have one saved)
            if categoryManager.hasCustomDefault() {
                Button(action: {
                    categoryManager.resetToMyDefault()
                    HapticManager.shared.buttonTapEffect()
                    AnalyticsManager.shared.trackCategorySelectionReset()
                    showConfirmation("Reset to your saved default ✓")
                }) {
                    HStack {
                        Image(systemName: "arrow.counterclockwise")
                        Text("Reset to my default")
                    }
                    .foregroundColor(.fizOrange)
                }
            }

            // Reset to factory default (all 12 categories)
            Button(action: {
                categoryManager.resetToFactoryDefault()
                HapticManager.shared.buttonTapEffect()
                AnalyticsManager.shared.trackCategorySelectionReset()
                showConfirmation("Reset to original default ✓")
            }) {
                HStack {
                    Image(systemName: "arrow.uturn.backward")
                    Text("Reset to original default")
                }
                .foregroundColor(.fizOrange)
            }
        }
    }

    @ViewBuilder
    private var singleCategorySettingsSection: some View {
        if localSelectedMode == .singleCategory {
            Section(header: Text("Select Category"),
                    footer: Text("Choose which category to focus on. The wheel will show subcategories instead of all categories.")) {
                ForEach(TriviaCategory.allCases.filter { CategorySelectionManager.shared.selectedCategories.contains($0) }, id: \.self) { category in
                    SingleCategorySelectionRow(
                        category: category,
                        isSelected: localSelectedCategory == category,
                        onSelect: {
                            if localSelectedCategory != category {
                                handleCategoryChange(from: localSelectedCategory, to: category)
                            }
                        }
                    )
                }
            }

            if localSelectedCategory == nil {
                Section {
                    Text("Select a category above to begin")
                        .font(.caption)
                        .foregroundColor(.orange)
                        .frame(maxWidth: .infinity, alignment: .center)
                        .listRowBackground(Color.clear)
                }
            }
        }
    }

    @ViewBuilder
    private var singleTopicSettingsSection: some View {
        if localSelectedMode == .singleTopic {
            let availablePacks = ExpansionPackManager.shared.getAvailableTopicsForSingleTopicMode()
            let installedPacks = availablePacks.filter { ExpansionPackManager.shared.isInstalled(packId: $0.packId) }
            let previewPacks = availablePacks.filter { ExpansionPackManager.shared.hasOnlyPreviews(packId: $0.packId) }

            installedPacksSection(installedPacks)
            previewPacksSection(previewPacks)
            emptyTopicStateSection(availablePacks)
            topicSelectionPromptSection(availablePacks)
        }
    }

    @ViewBuilder
    private func installedPacksSection(_ installedPacks: [ExpansionPack]) -> some View {
        if !installedPacks.isEmpty {
            Section(header: Text("Purchased & Installed Packs")) {
                ForEach(installedPacks, id: \.packId) { pack in
                    TopicPackRow(
                        pack: pack,
                        isPreview: false,
                        gameViewModel: gameViewModel,
                        answeredQuestionsManager: answeredQuestionsManager,
                        difficultyManager: difficultyManager,
                        localSelectedTopic: localSelectedTopic,
                        onSelect: {
                            handleTopicSelection(pack.packId)
                        },
                        onReset: { packId, packName, count in
                            topicToReset = packId
                            topicResetName = packName
                            topicResetCount = count
                            showingTopicResetAlert = true
                        }
                    )
                }
            }
        }
    }

    @ViewBuilder
    private func previewPacksSection(_ previewPacks: [ExpansionPack]) -> some View {
        if !previewPacks.isEmpty {
            Section(header: Text("Free Previews"),
                    footer: Text("Try these topics before purchasing. Preview questions are included for free!")) {
                ForEach(previewPacks, id: \.packId) { pack in
                    TopicPackRow(
                        pack: pack,
                        isPreview: true,
                        gameViewModel: gameViewModel,
                        answeredQuestionsManager: answeredQuestionsManager,
                        difficultyManager: difficultyManager,
                        localSelectedTopic: localSelectedTopic,
                        onSelect: {
                            handleTopicSelection(pack.packId)
                        },
                        onReset: { packId, packName, count in
                            topicToReset = packId
                            topicResetName = packName
                            topicResetCount = count
                            showingTopicResetAlert = true
                        }
                    )
                }
            }
        }
    }

    @ViewBuilder
    private func emptyTopicStateSection(_ availablePacks: [ExpansionPack]) -> some View {
        if availablePacks.isEmpty {
            Section(header: Text("Topic Settings"),
                    footer: Text("No expansion packs available. Visit the Store to browse and purchase expansion packs!")) {
                Text("No topics available")
                    .font(.body)
                    .foregroundColor(.secondary)
            }
        }
    }

    @ViewBuilder
    private func topicSelectionPromptSection(_ availablePacks: [ExpansionPack]) -> some View {
        if localSelectedTopic == nil && !availablePacks.isEmpty {
            Section {
                Text("Select a topic above to begin")
                    .font(.caption)
                    .foregroundColor(.orange)
                    .frame(maxWidth: .infinity, alignment: .center)
                    .listRowBackground(Color.clear)
            }
        }
    }

    var body: some View {
        ZStack {
            Form {
                gameModeSelectionSection

                multiCategorySettingsSection

                singleCategorySettingsSection

                singleTopicSettingsSection
            }
            .scrollContentBackground(.hidden)
            .background(backgroundGradient)

            // Confirmation message overlay
            if let message = confirmationMessage {
                VStack {
                    Spacer()
                    Text(message)
                        .font(.body)
                        .foregroundColor(.white)
                        .padding(.horizontal, 20)
                        .padding(.vertical, 12)
                        .background(Color.fizOrange)
                        .cornerRadius(10)
                        .shadow(radius: 5)
                        .padding(.bottom, 80)
                }
                .transition(.move(edge: .bottom).combined(with: .opacity))
                .animation(.easeInOut(duration: 0.3), value: confirmationMessage)
            }
        }
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
            if localSelectedMode == .singleCategory {
                Text("Please select a category before leaving, or switch back to Multi-Category mode.")
            } else if localSelectedMode == .singleTopic {
                Text("Please select a topic before leaving, or switch back to Multi-Category mode.")
            } else {
                Text("Please complete your selection before leaving.")
            }
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
        .alert("Reset \(topicResetName)?", isPresented: $showingTopicResetAlert) {
            Button("Cancel", role: .cancel) {
                topicToReset = nil
                topicResetCount = 0
                topicResetName = ""
            }
            Button("Reset", role: .destructive) {
                if let packId = topicToReset {
                    answeredQuestionsManager.resetTopicProgress(packId, in: gameViewModel.questions)
                    HapticManager.shared.buttonTapEffect()

                    AnalyticsManager.shared.trackSettingChanged(
                        setting: "topic_progress_reset",
                        value: packId
                    )

                    // Clear if this was the selected topic
                    if localSelectedTopic == packId {
                        localSelectedTopic = nil
                        gameModeManager.setSelectedTopic(nil)
                    }
                }
                topicToReset = nil
                topicResetCount = 0
                topicResetName = ""
            }
        } message: {
            Text("This will reset \(topicResetCount) answered question\(topicResetCount == 1 ? "" : "s") for \(topicResetName). You'll be able to answer them again. This action cannot be undone.")
        }
        .alert("Maximum Reached", isPresented: $showMaxReachedAlert) {
            Button("OK", role: .cancel) { }
        } message: {
            Text("You can select up to \(CategorySelectionManager.maximumCategories) categories. Deselect one to add another.")
        }
        .alert("Minimum Required", isPresented: $showMinimumAlert) {
            Button("OK", role: .cancel) { }
        } message: {
            Text("You must have at least \(CategorySelectionManager.minimumCategories) categories selected for gameplay.")
        }
        .alert("Cannot Deselect", isPresented: $showActiveCategoryAlert) {
            Button("OK", role: .cancel) { }
        } message: {
            Text("This category is currently active in Single Category Mode. Disable Single Category Mode first, or switch to a different category.")
        }
        .onAppear {
            isInitialLoad = true
            localSelectedMode = gameModeManager.selectedMode
            localSelectedCategory = gameModeManager.selectedCategory
            localSelectedTopic = gameModeManager.selectedTopic
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.1) {
                isInitialLoad = false
            }
        }
    }

    // MARK: - Event Handlers

    private func handleCategoryToggle(_ category: TriviaCategory) {
        let success = categoryManager.toggleCategory(category)
        if !success {
            // Determine which alert to show
            if categoryManager.selectedCategories.contains(category) {
                // Trying to deselect but can't
                if GameModeManager.shared.isSingleCategoryMode &&
                   GameModeManager.shared.selectedCategory == category {
                    showActiveCategoryAlert = true
                } else {
                    showMinimumAlert = true
                }
            } else {
                showMaxReachedAlert = true
            }
            HapticManager.shared.incorrectAnswerEffect()
        } else {
            HapticManager.shared.buttonTapEffect()
        }
    }

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
            if mode != .singleTopic {
                gameModeManager.setSelectedTopic(nil)
                localSelectedTopic = nil
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
            localSelectedCategory = newValue
            gameModeManager.setSelectedCategory(newValue)
            if let category = newValue {
                AnalyticsManager.shared.trackSettingChanged(setting: "single_category_selected", value: category.rawValue)
            }
        }
    }

    private func handleTopicSelection(_ packId: String) {
        guard !isInitialLoad && !isApplyingChanges else { return }

        // Check if pack is completed
        let isCompleted = answeredQuestionsManager.areAllTopicQuestionsAnswered(
            packId,
            in: gameViewModel.questions,
            difficultyMode: difficultyManager.selectedDifficulty
        )

        if isCompleted {
            HapticManager.shared.warningFeedback()
            return
        }

        // If user taps already selected topic, do nothing
        if localSelectedTopic == packId {
            HapticManager.shared.buttonTapEffect()
            return
        }

        let oldValue = localSelectedTopic
        let newValue = packId

        if gameViewModel.gameSession.currentStreak > 0 && oldValue != nil {
            // Save old value temporarily
            localSelectedTopic = newValue // Update UI immediately
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.1) {
                self.showingStreakAlert = true
            }
        } else {
            localSelectedTopic = newValue
            gameModeManager.setSelectedTopic(newValue)
            AnalyticsManager.shared.trackSettingChanged(setting: "single_topic_selected", value: newValue)
            HapticManager.shared.buttonTapEffect()
        }
    }

    private func handleTopicChange(from oldValue: String?, to newValue: String?) {
        guard !isInitialLoad && !isApplyingChanges else { return }

        if gameViewModel.gameSession.currentStreak > 0 && oldValue != nil && oldValue != newValue {
            // For now, just show alert without tracking previous topic
            // Could add pendingTopic state if needed
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) {
                self.showingStreakAlert = true
            }
        } else {
            gameModeManager.setSelectedTopic(newValue)
            if let topicPackId = newValue {
                AnalyticsManager.shared.trackSettingChanged(setting: "single_topic_selected", value: topicPackId)
            }
        }
    }

    private func handleAlertCancel() {
        if pendingMode != nil {
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
            let gameMode: String
            let categoryName: String?

            if gameModeManager.isSingleCategoryMode {
                gameMode = "Single Category"
                categoryName = gameModeManager.selectedCategory?.rawValue
            } else if gameModeManager.isSingleTopicMode {
                gameMode = "Single Topic"
                // Get display name for the selected topic
                if let topicId = gameModeManager.selectedTopic {
                    categoryName = ExpansionPackManager.shared.getDisplayName(for: topicId)
                } else {
                    categoryName = nil
                }
            } else {
                gameMode = "Multi-Category"
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
            if newMode != .singleTopic {
                gameModeManager.setSelectedTopic(nil)
                localSelectedTopic = nil
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

    private func showConfirmation(_ message: String) {
        confirmationMessage = message

        // Auto-dismiss after 2 seconds
        DispatchQueue.main.asyncAfter(deadline: .now() + 2.0) {
            confirmationMessage = nil
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

// MARK: - Helper View for Topic Pack Rows
private struct TopicPackRow: View {
    let pack: ExpansionPack
    let isPreview: Bool
    let gameViewModel: GameViewModel
    let answeredQuestionsManager: AnsweredQuestionsManager
    let difficultyManager: DifficultyManager
    let localSelectedTopic: String?
    let onSelect: () -> Void
    let onReset: (String, String, Int) -> Void

    var body: some View {
        let isCompleted = answeredQuestionsManager.areAllTopicQuestionsAnswered(
            pack.packId,
            in: gameViewModel.questions,
            difficultyMode: difficultyManager.selectedDifficulty
        )
        let answeredCount = answeredQuestionsManager.getAnsweredCountForTopic(
            pack.packId,
            in: gameViewModel.questions,
            difficultyMode: difficultyManager.selectedDifficulty
        )
        let totalCount = answeredQuestionsManager.getTotalQuestionsForTopic(
            pack.packId,
            in: gameViewModel.questions,
            difficultyMode: difficultyManager.selectedDifficulty
        )

        // Show reset button if questions answered AND (pack is NOT currently selected OR is completed)
        // This ensures completed packs show reset even if they're still "selected" in state
        let showResetButton = answeredCount > 0 && (localSelectedTopic != pack.packId || isCompleted)

        // Main pack row - split into two parts so reset button stays fully visible
        HStack(spacing: 12) {
            // Left side: Main selection button with opacity applied
            Button(action: {
                if !isCompleted {
                    onSelect()
                } else {
                    HapticManager.shared.warningFeedback()
                }
            }) {
                HStack(spacing: 12) {
                    Image(systemName: pack.icon)
                        .font(.title3)
                        .foregroundColor(isCompleted ? .secondary : .fizOrange)
                        .frame(width: 28)

                    VStack(alignment: .leading, spacing: 2) {
                        Text(pack.packName)
                            .font(.body)
                            .foregroundColor(isCompleted ? .secondary : .primary)
                            .strikethrough(isCompleted)

                        // Always show "answered" at the end
                        Text("\(answeredCount)/\(totalCount) \(isPreview ? "preview " : "")questions answered")
                            .font(.caption)
                            .foregroundColor(.secondary)
                    }

                    Spacer(minLength: 0)

                    // Selection checkmark (only on selected, not on completed)
                    if localSelectedTopic == pack.packId && !isCompleted {
                        Image(systemName: "checkmark.circle.fill")
                            .font(.title3)
                            .foregroundColor(.fizOrange)
                    }
                }
                .contentShape(Rectangle())
                .opacity(isCompleted ? 0.6 : 1.0)
            }
            .buttonStyle(.plain)
            .disabled(isCompleted)

            // Right side: Reset button - stays fully opaque and clickable
            if showResetButton {
                Button(action: {
                    onReset(pack.packId, pack.packName, answeredCount)
                }) {
                    VStack(spacing: 2) {
                        Image(systemName: "arrow.counterclockwise")
                            .font(.caption)
                        Text("Reset")
                            .font(.caption2)
                    }
                    .foregroundColor(.orange)
                }
                .buttonStyle(.plain)
            }
        }
    }
}

// MARK: - Category Selection Row Component

struct CategorySelectionRow: View {
    let category: TriviaCategory
    let isSelected: Bool
    let canToggle: Bool
    let onToggle: () -> Void

    @Environment(\.sizeCategory) private var sizeCategory

    var body: some View {
        Button(action: onToggle) {
            HStack(spacing: 12) {
                Image(systemName: category.icon)
                    .font(.title2)
                    .foregroundColor(Color(hex: category.color))
                    .frame(width: 32)

                Text(category.rawValue)
                    .font(.body)
                    .foregroundColor(.primary)

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
            .opacity(canToggle || isSelected ? 1.0 : 0.5)
        }
        .buttonStyle(.plain)
    }
}

// MARK: - Single Category Selection Row Component

struct SingleCategorySelectionRow: View {
    let category: TriviaCategory
    let isSelected: Bool
    let onSelect: () -> Void

    var body: some View {
        Button(action: onSelect) {
            HStack(spacing: 12) {
                Image(systemName: category.icon)
                    .font(.title2)
                    .foregroundColor(Color(hex: category.color))
                    .frame(width: 32)

                VStack(alignment: .leading, spacing: 2) {
                    Text(category.rawValue)
                        .font(.body)
                        .foregroundColor(.primary)

                    Text("Wheel will show \(category.rawValue) subcategories")
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
