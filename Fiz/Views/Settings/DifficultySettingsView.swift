import SwiftUI

struct DifficultySettingsView: View {
    @StateObject private var difficultyManager = DifficultyManager.shared

    private var backgroundGradient: some View {
        Color(.systemGroupedBackground)
            .ignoresSafeArea()
    }

    var body: some View {
        Form {
            Section(footer: Text("Choose the difficulty level that matches your trivia expertise.")) {
                VStack(alignment: .leading, spacing: 8) {
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

                    Text(difficultyManager.selectedDifficulty.description)
                        .font(.caption)
                        .foregroundColor(.secondary)
                }
            }
        }
        .scrollContentBackground(.hidden)
        .background(backgroundGradient)
        .navigationTitle("Difficulty")
        .navigationBarTitleDisplayMode(.large)
    }
}

#Preview {
    NavigationStack {
        DifficultySettingsView()
    }
}
