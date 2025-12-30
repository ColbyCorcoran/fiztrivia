import SwiftUI

struct SettingsView: View {
    @Bindable var gameViewModel: GameViewModel
    var onSwipe: ((SwipeDirection, CGFloat) -> Void)? = nil
    @StateObject private var swipeNavigationManager = SwipeNavigationManager.shared
    @StateObject private var gameModeManager = GameModeManager.shared
    @Environment(\.sizeCategory) private var sizeCategory

    @State private var swipeTranslation: CGFloat = 0

    private var backgroundGradient: some View {
        Color(.systemGroupedBackground)
            .ignoresSafeArea()
    }

    var body: some View {
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
                        NavigationLink(destination: AppIconSettingsView()) {
                            SettingsRow(
                                icon: "app.badge",
                                iconColor: .fizTeal,
                                title: "App Icon"
                                // subtitle: "Choose your favorite Fiz"
                            )
                        }
                        NavigationLink(destination: PhobiaSettingsView()) {
                            SettingsRow(
                                icon: "eye.slash",
                                iconColor: .fizTeal,
                                title: "Phobia Filters"
                                // subtitle: "Exclude topics you'd like to avoid"
                            )
                        }
                        NavigationLink(destination: HapticsSettingsView()) {
                            SettingsRow(
                                icon: "hand.tap.fill",
                                iconColor: .fizTeal,
                                title: "Interaction"
                                // subtitle: "Haptics and swipe navigation"
                            )
                        }
                        NavigationLink(destination: PopupDurationSettingsView()) {
                            SettingsRow(
                                icon: "timer",
                                iconColor: .fizTeal,
                                title: "Answer Popup Duration"
                                // subtitle: "Control result display timing"
                            )
                        }
                        NavigationLink(destination: AnalyticsSettingsView()) {
                            SettingsRow(
                                icon: "chart.bar.fill",
                                iconColor: .fizTeal,
                                title: "Analytics"
                                // subtitle: "Anonymous usage data sharing"
                            )
                        }
                    }

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
                        NavigationLink(destination: CategorySelectionSettingsView()) {
                            SettingsRow(
                                icon: "chart.pie",
                                iconColor: .fizOrange,
                                title: "Category Selection"
                            )
                        }
                        NavigationLink(destination: GameModesSettingsView(gameViewModel: gameViewModel)) {
                            SettingsRow(
                                icon: gameModeManager.selectedMode.icon,
                                iconColor: .fizOrange,
                                title: "Game Modes"
                                // subtitle: "Single category focus mode"
                            )
                        }
                        NavigationLink(destination: GameProgressSettingsView(gameViewModel: gameViewModel)) {
                            SettingsRow(
                                icon: "chart.line.uptrend.xyaxis",
                                iconColor: .fizOrange,
                                title: "Game Progress"
                                // subtitle: "Stats and reset options"
                            )
                        }
                    }

                    // Version footer at bottom of scroll
                    Section {
                        Text("Version \(appVersion)")
                            .font(.caption)
                            .foregroundColor(.secondary)
                            .frame(maxWidth: .infinity)
                            .listRowBackground(Color.clear)
                    }
                }
//                .scrollContentBackground(.hidden)
//                .background(backgroundGradient)
//                .listStyle(.insetGrouped)
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
                .gesture(settingsSwipeGesture)
            }
        }

    private var settingsSwipeGesture: some Gesture {
        DragGesture()
            .onChanged { value in
                guard swipeNavigationManager.isSwipeNavigationEnabled else { return }

                swipeTranslation = value.translation.width
                onSwipe?(.right, swipeTranslation)
            }
            .onEnded { value in
                guard swipeNavigationManager.isSwipeNavigationEnabled else {
                    swipeTranslation = 0
                    onSwipe?(.right, 0)
                    return
                }

                let distance = value.translation.width

                // Check threshold: 120pt minimum distance
                // From settings, only swipe right goes back to main
                if distance > 120 {
                    HapticManager.shared.lightImpact()
                    onSwipe?(.right, 0)
                } else {
                    // Didn't meet threshold - spring back
                    onSwipe?(.right, 0)
                }

                swipeTranslation = 0
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
