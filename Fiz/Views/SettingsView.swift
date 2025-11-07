import SwiftUI

struct SettingsView: View {
    @Bindable var gameViewModel: GameViewModel

    var body: some View {
        NavigationView {
            Form {
                Section {
                    NavigationLink(destination: PersonalizationSettingsView(gameViewModel: gameViewModel)) {
                        HStack {
                            Image(systemName: "person.crop.circle")
                                .font(.title2)
                                .foregroundColor(Color.fizTeal)
                                .frame(width: 32)
                            VStack(alignment: .leading, spacing: 2) {
                                Text("Personalization")
                                    .font(.body)
                                Text("Profile, App Icon, Haptics")
                                    .font(.caption)
                                    .foregroundColor(.secondary)
                            }
                        }
                    }

                    NavigationLink(destination: GameSettingsView(gameViewModel: gameViewModel)) {
                        HStack {
                            Image(systemName: "gamecontroller.fill")
                                .font(.title2)
                                .foregroundColor(Color.fizOrange)
                                .frame(width: 32)
                            VStack(alignment: .leading, spacing: 2) {
                                Text("Game Settings")
                                    .font(.body)
                                Text("Difficulty, Progress, Statistics")
                                    .font(.caption)
                                    .foregroundColor(.secondary)
                            }
                        }
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
                    .glassButtonStyle()
                }
            }
        }
    }
}

#Preview {
    SettingsView(gameViewModel: GameViewModel())
        .modelContainer(for: LeaderboardEntry.self, inMemory: true)
}
