import SwiftUI

struct SettingsView: View {
    @Bindable var gameViewModel: GameViewModel
    @StateObject private var userManager = UserManager.shared
    @StateObject private var difficultyManager = DifficultyManager.shared
    @StateObject private var answeredQuestionsManager = AnsweredQuestionsManager.shared
    @State private var soundEnabled = true
    @State private var hapticEnabled = true
    @State private var editedUsername: String = ""
    @State private var isEditingUsername = false
    @State private var showingResetAlert = false
    
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
}

#Preview {
    SettingsView(gameViewModel: GameViewModel())
}
