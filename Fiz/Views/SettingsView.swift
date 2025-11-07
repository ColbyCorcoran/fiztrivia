import SwiftUI

struct SettingsView: View {
    @Bindable var gameViewModel: GameViewModel
    @StateObject private var userManager = UserManager.shared
    @StateObject private var difficultyManager = DifficultyManager.shared
    @StateObject private var singleCategoryManager = SingleCategoryModeManager.shared
    @StateObject private var answeredQuestionsManager = AnsweredQuestionsManager.shared
    @StateObject private var appIconManager = AppIconManager.shared
    @Environment(\.modelContext) private var modelContext
    @State private var soundEnabled = true
    @State private var hapticEnabled = true
    @State private var editedUsername: String = ""
    @State private var isEditingUsername = false
    @State private var showingResetAlert = false
    @State private var showingStreakAlert = false
    @State private var pendingModeChange: Bool? = nil
    @State private var previousModeValue: Bool? = nil  // Store old mode for cancel
    @State private var pendingCategoryChange: TriviaCategory? = nil
    @State private var previousCategory: TriviaCategory? = nil  // Store old category for cancel

    // Local state for immediate UI updates
    @State private var localModeEnabled: Bool = false
    @State private var localSelectedCategory: TriviaCategory? = nil
    @State private var isInitialLoad: Bool = true  // Prevent onChange from firing on initial load
    @State private var isApplyingChanges: Bool = false  // Prevent onChange from firing while applying alert changes
    
    var body: some View {
        NavigationView {
            Form {
                    Section("Profile") {
                        HStack {
                            Text("Username")
                            Spacer()

                            if isEditingUsername {
                                TextField("Enter username", text: $editedUsername)
                                    .textFieldStyle(RoundedBorderTextFieldStyle())
                                    .autocorrectionDisabled()
                                    .textInputAutocapitalization(.words)
                                    .frame(maxWidth: 150)
                                    .onSubmit {
                                        saveUsername()
                                    }

                                Button("Save") {
                                    saveUsername()
                                }
                                .font(.caption)
                                .foregroundColor(.blue)

                                Button("Cancel") {
                                    cancelEditing()
                                }
                                .font(.caption)
                                .foregroundColor(.secondary)

                            } else {
                                Button(userManager.displayName) {
                                    startEditing()
                                }
                                .foregroundColor(.blue)
                                .font(.body)
                            }
                        }
                    }

                    Section(header: Text("App Icon"),
                           footer: Text("Choose your favorite Fiz to represent your app!")) {
                        LazyVGrid(columns: [
                            GridItem(.flexible()),
                            GridItem(.flexible()),
                            GridItem(.flexible())
                        ], spacing: 16) {
                            ForEach(AppIconManager.AppIcon.allCases) { icon in
                                Button(action: {
                                    HapticManager.shared.buttonTapEffect()
                                    appIconManager.setIcon(icon)
                                }) {
                                    VStack(spacing: 8) {
                                        Image(icon.previewImageName)
                                            .resizable()
                                            .scaledToFit()
                                            .frame(width: 60, height: 60)
                                            .clipShape(RoundedRectangle(cornerRadius: 12))
                                            .overlay(
                                                RoundedRectangle(cornerRadius: 12)
                                                    .stroke(appIconManager.selectedIcon == icon ? Color.fizTeal : Color.clear, lineWidth: 3)
                                            )
                                            .shadow(color: Color.fizBrown.opacity(0.2), radius: 4, x: 0, y: 2)

                                        Text(icon.rawValue)
                                            .font(.caption)
                                            .foregroundColor(.primary)
                                            .multilineTextAlignment(.center)
                                            .lineLimit(2)
                                            .frame(height: 30)

                                        if appIconManager.selectedIcon == icon {
                                            Image(systemName: "checkmark.circle.fill")
                                                .foregroundColor(Color.fizTeal)
                                                .font(.caption)
                                        }
                                    }
                                    .frame(maxWidth: .infinity)
                                }
                                .buttonStyle(.plain)
                            }
                        }
                        .padding(.vertical, 8)
                    }
                    
                    Section("Audio & Haptics") {
                        Toggle("Sound Effects", isOn: $soundEnabled)
                            .accessibilityHint("Enable or disable sound effects")
                        
                        Toggle("Haptic Feedback", isOn: $hapticEnabled)
                            .accessibilityHint("Enable or disable haptic feedback")
                    }
                    
                    Section("Game Settings") {
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
                            }

                            Text(difficultyManager.selectedDifficulty.description)
                                .font(.caption)
                                .foregroundColor(.secondary)
                                .padding(.leading, 0)
                        }
                    }

                    Section(header: Text("Single Category Mode"),
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
                    
                    Section("About") {
                        HStack {
                            Text("Version")
                            Spacer()
                            Text("1.0")
                                .foregroundColor(.secondary)
                        }
                        
                        HStack {
                            Text("Categories")
                            Spacer()
                            Text("\(TriviaCategory.allCases.count)")
                                .foregroundColor(.secondary)
                        }
                    }
                }
                .navigationTitle("Settings")
                .navigationBarTitleDisplayMode(.large)
                .toolbar {
                    ToolbarItem(placement: .navigationBarTrailing) {
                        Button("Done") {
                            gameViewModel.continueGame()
                        }
                    }
                }
                .onAppear {
                    // Set initial load flag to prevent onChange from firing during setup
                    isInitialLoad = true

                    // Initialize local state from manager
                    localModeEnabled = singleCategoryManager.isEnabled
                    localSelectedCategory = singleCategoryManager.selectedCategory

                    // Set flag to false after a brief delay to allow onChange to settle
                    DispatchQueue.main.asyncAfter(deadline: .now() + 0.1) {
                        isInitialLoad = false
                    }
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
    }
    
    private func startEditing() {
        editedUsername = userManager.username
        isEditingUsername = true
    }
    
    private func saveUsername() {
        let trimmedName = editedUsername.trimmingCharacters(in: .whitespacesAndNewlines)
        if !trimmedName.isEmpty {
            userManager.updateUsername(trimmedName)
            HapticManager.shared.buttonTapEffect()
        }
        isEditingUsername = false
        editedUsername = ""
    }
    
    private func cancelEditing() {
        isEditingUsername = false
        editedUsername = ""
    }

    private func handleAlertCancel() {
        // Revert mode toggle to previous value if it was changed
        if let previousMode = previousModeValue {
            localModeEnabled = previousMode
            previousModeValue = nil
        }

        // Revert category picker to previous selection if it was changed
        if let previousCat = previousCategory {
            localSelectedCategory = previousCat
            previousCategory = nil
        }

        // Clear all pending changes
        pendingModeChange = nil
        pendingCategoryChange = nil
    }

    private func handleModeChange(from oldValue: Bool, to newValue: Bool) {
        // Skip if this is the initial load or we're applying changes from alert
        guard !isInitialLoad && !isApplyingChanges else { return }

        // Check if user has a streak
        if gameViewModel.gameSession.currentStreak > 0 {
            // Store old mode for potential revert (if user cancels)
            previousModeValue = oldValue
            // Store new mode as pending
            pendingModeChange = newValue
            // Let toggle UI update to new value immediately

            // Use DispatchQueue to ensure alert shows after any UI updates
            DispatchQueue.main.async {
                // Show alert immediately after current UI cycle
                self.showingStreakAlert = true
            }
        } else {
            // No streak, apply immediately
            singleCategoryManager.setModeEnabled(newValue)
            if !newValue {
                singleCategoryManager.setSelectedCategory(nil)
                localSelectedCategory = nil
            }
        }
    }

    private func handleCategoryChange(from oldValue: TriviaCategory?, to newValue: TriviaCategory?) {
        // Skip if this is the initial load or we're applying changes from alert
        guard !isInitialLoad && !isApplyingChanges else { return }

        // Only show alert if changing from one category to another (not initial selection)
        if gameViewModel.gameSession.currentStreak > 0 && oldValue != nil && oldValue != newValue {
            // Store old category for potential revert (if user cancels)
            previousCategory = oldValue
            // Store new category as pending
            pendingCategoryChange = newValue
            // Let picker UI update to new value immediately

            // Delay alert to allow picker to fully dismiss (increased to 0.5s for reliability)
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) {
                // Force state update to trigger alert reliably
                self.showingStreakAlert = true
            }
        } else {
            // No streak or initial selection, apply immediately
            singleCategoryManager.setSelectedCategory(newValue)
        }
    }

    private func applyPendingChanges(saveStreak: Bool) {
        // Set flag to prevent onChange from triggering during our updates
        isApplyingChanges = true

        // Save streak to leaderboard if requested
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

        // Reset streak
        gameViewModel.gameSession.currentStreak = 0
        StreakPersistenceManager.clearCurrentStreak()

        // Apply pending mode change
        if let modeChange = pendingModeChange {
            singleCategoryManager.setModeEnabled(modeChange)
            if !modeChange {
                singleCategoryManager.setSelectedCategory(nil)
            }
            pendingModeChange = nil
        }

        // Apply pending category change
        if let categoryChange = pendingCategoryChange {
            singleCategoryManager.setSelectedCategory(categoryChange)
            pendingCategoryChange = nil
        }

        // Clear previous value tracking
        previousModeValue = nil
        previousCategory = nil

        HapticManager.shared.buttonTapEffect()

        // Update local state AFTER manager updates with a slight delay to ensure they stick
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.1) {
            // Sync local state from manager (source of truth)
            self.localModeEnabled = self.singleCategoryManager.isEnabled
            self.localSelectedCategory = self.singleCategoryManager.selectedCategory

            // Reset flag to allow onChange to work normally
            self.isApplyingChanges = false
        }
    }
}

#Preview {
    SettingsView(gameViewModel: GameViewModel())
}
