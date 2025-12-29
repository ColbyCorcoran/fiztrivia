import SwiftUI

struct SettingsView: View {
    @Bindable var gameViewModel: GameViewModel
    @Environment(\.sizeCategory) private var sizeCategory
    
    private var backgroundGradient: some View {
        LinearGradient(
            colors: [Color.fizBackground, Color.fizBackgroundSecondary],
            startPoint: .topLeading,
            endPoint: .bottomTrailing
        )
        .ignoresSafeArea()
    }

    var body: some View {
        ZStack{
            backgroundGradient
            
            NavigationStack {
                Form {
                    // Question History - TOP (standalone, no section header)
                    NavigationLink(destination: QuestionHistoryView()) {
                        SettingsRow(
                            icon: "clock.arrow.circlepath",
                            iconColor: .fizBrown,
                            title: "Question History"
                            // subtitle: "Review answered questions"
                        )
                    }
                    .listRowBackground(
                        Rectangle().fill(.ultraThinMaterial)
                    )

                    // Personalization Section
                    Section("Personalization") {
                        NavigationLink(destination: UsernameSettingsView()) {
                            SettingsRow(
                                icon: "person.fill",
                                iconColor: .fizTeal,
                                title: "Username"
                                // subtitle: "Change your display name"
                            )
                        }
                        .listRowBackground(
                            Rectangle().fill(.ultraThinMaterial)
                        )
                        NavigationLink(destination: AppIconSettingsView()) {
                            SettingsRow(
                                icon: "app.badge",
                                iconColor: .fizTeal,
                                title: "App Icon"
                                // subtitle: "Choose your favorite Fiz"
                            )
                        }
                        .listRowBackground(
                            Rectangle().fill(.ultraThinMaterial)
                        )
                        NavigationLink(destination: HapticsSettingsView()) {
                            SettingsRow(
                                icon: "hand.tap.fill",
                                iconColor: .fizTeal,
                                title: "Haptics"
                                // subtitle: "Tactile feedback settings"
                            )
                        }
                        .listRowBackground(
                            Rectangle().fill(.ultraThinMaterial)
                        )
                        NavigationLink(destination: PopupDurationSettingsView()) {
                            SettingsRow(
                                icon: "timer",
                                iconColor: .fizTeal,
                                title: "Answer Popup Duration"
                                // subtitle: "Control result display timing"
                            )
                        }
                        .listRowBackground(
                            Rectangle().fill(.ultraThinMaterial)
                        )
                        NavigationLink(destination: AnalyticsSettingsView()) {
                            SettingsRow(
                                icon: "chart.bar.fill",
                                iconColor: .fizTeal,
                                title: "Analytics"
                                // subtitle: "Anonymous usage data sharing"
                            )
                        }
                        .listRowBackground(
                            Rectangle().fill(.ultraThinMaterial)
                        )
                    }
                    .listRowBackground(
                        Rectangle().fill(.ultraThinMaterial)
                    )

                    // Game Settings Section
                    Section("Game Settings") {
                        NavigationLink(destination: DifficultySettingsView()) {
                            SettingsRow(
                                icon: "speedometer",
                                iconColor: .fizOrange,
                                title: "Difficulty"
                                // subtitle: "Casual, Normal, or Difficult"
                            )
                        }
                        .listRowBackground(
                            Rectangle().fill(.ultraThinMaterial)
                        )
                        NavigationLink(destination: GameModesSettingsView(gameViewModel: gameViewModel)) {
                            SettingsRow(
                                icon: "square.grid.2x2",
                                iconColor: .fizOrange,
                                title: "Game Modes"
                                // subtitle: "Single category focus mode"
                            )
                        }
                        .listRowBackground(
                            Rectangle().fill(.ultraThinMaterial)
                        )
                        NavigationLink(destination: GameProgressSettingsView(gameViewModel: gameViewModel)) {
                            SettingsRow(
                                icon: "chart.line.uptrend.xyaxis",
                                iconColor: .fizOrange,
                                title: "Game Progress"
                                // subtitle: "Stats and reset options"
                            )
                        }
                        .listRowBackground(
                            Rectangle().fill(.ultraThinMaterial)
                        )
                    }
                    .listRowBackground(
                        Rectangle().fill(.ultraThinMaterial)
                    )

                    // Version footer at bottom of scroll
                    Section {
                        Text("Version \(appVersion)")
                            .font(.caption)
                            .foregroundColor(.secondary)
                            .frame(maxWidth: .infinity)
                            .listRowBackground(Color.clear)
                    }
                }
                .scrollContentBackground(.hidden)
                .listStyle(.insetGrouped)
                .navigationTitle("Settings")
                .navigationBarTitleDisplayMode(.large)
                .toolbar {
                    ToolbarItem(placement: .navigationBarTrailing) {
                        Button(action: {
                            gameViewModel.continueGame()
                        }) {
                            Image(systemName: "checkmark")
                                .font(.body.weight(.semibold))
                        }
                        .tint(.fizTeal)
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

// MARK: - Reusable Settings Row Component
struct SettingsRow: View {
    let icon: String
    let iconColor: Color
    let title: String
    // var subtitle: String? = nil  // Uncomment to enable subtitles
    @Environment(\.sizeCategory) private var sizeCategory

    var body: some View {
        HStack {
            // Hide icon at accessibility sizes to prevent overlap
            if !sizeCategory.isAccessibilitySize {
                Image(systemName: icon)
                    .font(.title3)
                    .foregroundColor(iconColor)
                    .frame(width: 28)
            }
            Text(title)
                .font(.body)
            // Uncomment below to enable subtitles:
            // VStack(alignment: .leading, spacing: 2) {
            //     Text(title)
            //         .font(.body)
            //     if let subtitle = subtitle {
            //         Text(subtitle)
            //             .font(.caption)
            //             .foregroundColor(.secondary)
            //     }
            // }
        }
    }
}

#Preview {
    SettingsView(gameViewModel: GameViewModel())
        .modelContainer(for: LeaderboardEntry.self, inMemory: true)
}
