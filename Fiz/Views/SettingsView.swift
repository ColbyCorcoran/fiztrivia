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
                                Text("Username, App Icon, and more")
                                    .font(.caption)
                                    .foregroundColor(.secondary)
                            }
                        }
                    }
                }
                Section {
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

                Section {
                    NavigationLink(destination: QuestionHistoryView()) {
                        HStack {
                            Image(systemName: "clock.arrow.circlepath")
                                .font(.title2)
                                .foregroundColor(Color.fizBrown)
                                .frame(width: 32)
                            VStack(alignment: .leading, spacing: 2) {
                                Text("Question History")
                                    .font(.body)
                                Text("Review answered questions")
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
                        Text(appVersion)
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

    private var appVersion: String {
        if let version = Bundle.main.infoDictionary?["CFBundleShortVersionString"] as? String {
            if let build = Bundle.main.infoDictionary?["CFBundleVersion"] as? String {
                return "\(version) (\(build))"
            }
            return version
        }
        return "Unknown"
    }
}

#Preview {
    SettingsView(gameViewModel: GameViewModel())
        .modelContainer(for: LeaderboardEntry.self, inMemory: true)
}
