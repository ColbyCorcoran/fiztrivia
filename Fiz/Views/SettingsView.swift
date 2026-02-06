import SwiftUI

struct SettingsView: View {
    @Bindable var gameViewModel: GameViewModel
    var onSwipe: ((SwipeDirection) -> Void)? = nil
    var onDrag: ((CGFloat, CGFloat, Bool) -> Void)? = nil
    @StateObject private var swipeNavigationManager = SwipeNavigationManager.shared
    @StateObject private var gameModeManager = GameModeManager.shared
    @StateObject private var onboardingManager = OnboardingManager.shared
    @Environment(\.sizeCategory) private var sizeCategory
    @Environment(\.openURL) private var openURL

    @State private var swipeTranslation: CGFloat = 0
    @State private var showingStore = false

    // Developer bypass state
    @StateObject private var developerBypassManager = DeveloperBypassManager.shared
    @State private var versionTapCount: Int = 0
    @State private var lastTapTime: Date = Date()
    @State private var showingCodePrompt: Bool = false
    @State private var codeInput: String = ""
    @State private var showingErrorAlert: Bool = false
    @State private var showingDeactivateAlert: Bool = false

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

                    // Store - Expansion Packs
                    Button(action: {
                        HapticManager.shared.buttonTapEffect()
                        showingStore = true
                    }) {
                        SettingsRow(
                            icon: "rectangle.stack.badge.plus",
                            iconColor: .fizOrange,
                            title: "Expansion Packs"
                        )
                    }
                    .buttonStyle(.plain)

                    // Game Settings Section
                    Section("Game Settings") {
                        NavigationLink(destination: DifficultySettingsView()) {
                            SettingsRow(
                                icon: "speedometer",
                                iconColor: .fizOrange,
                                title: "Game Difficulty"
                                // subtitle: "Casual, Normal, or Difficult"
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

                    // Support & Legal Section
                    Section("Support & Legal") {
                        // Developer Bypass Deactivation (only visible when active)
                        if developerBypassManager.isBypassActive {
                            Button(action: {
                                showingDeactivateAlert = true
                            }) {
                                SettingsRow(
                                    icon: "key.slash",
                                    iconColor: .red,
                                    title: "Developer Access Active"
                                )
                            }
                            .buttonStyle(.plain)
                        }

                        // Feature Requests & Bug Reports
                        Button(action: {
                            AnalyticsManager.shared.trackFeatureRequestsOpened()
                            HapticManager.shared.buttonTapEffect()
                            if let url = URL(string: "https://fiztrivia.userjot.com/board/feature-requests-bug-reports") {
                                openURL(url)
                            }
                        }) {
                            SettingsRow(
                                icon: "ellipsis.message",
                                iconColor: .fizBrown,
                                title: "Feature Requests & Bug Reports"
                            )
                        }
                        .buttonStyle(.plain)

                        // Terms of Service & Privacy Policy
                        Button(action: {
                            AnalyticsManager.shared.trackTermsOfServiceViewed()
                            HapticManager.shared.buttonTapEffect()
                            if let url = URL(string: "https://github.com/ColbyCorcoran/fiztrivia/tree/main/Terms%20%26%20Privacy") {
                                UIApplication.shared.open(url)
                            }
                        }) {
                            SettingsRow(
                                icon: "doc.text",
                                iconColor: .fizBrown,
                                title: "Terms of Service & Privacy Policy"
                            )
                        }
                        .buttonStyle(.plain)

                        // Contact Support
                        Button(action: {
                            AnalyticsManager.shared.trackContactSupportOpened()
                            HapticManager.shared.buttonTapEffect()
                            if let url = URL(string: "mailto:woodsy.relics.6n@icloud.com?subject=Fiz%20Trivia%20Support") {
                                openURL(url)
                            }
                        }) {
                            SettingsRow(
                                icon: "envelope",
                                iconColor: .fizBrown,
                                title: "Contact Support"
                            )
                        }
                        .buttonStyle(.plain)

                        // Feature Tour (moved from top)
                        Button(action: {
                            onboardingManager.forceShowSecondaryOnboarding()
                            AnalyticsManager.shared.trackFeatureTourManuallyOpened()
                            HapticManager.shared.buttonTapEffect()
                        }) {
                            SettingsRow(
                                icon: "lightbulb",
                                iconColor: .fizBrown,
                                title: "Feature Tour"
                            )
                        }
                        .buttonStyle(.plain)

                        // Version footer at bottom
                        Text("Version \(appVersion)")
                            .font(.caption)
                            .foregroundColor(.secondary)
                            .frame(maxWidth: .infinity)
                            .listRowBackground(Color.clear)
                            .listRowSeparator(.hidden)
                            .padding(.top, 8)
                            .onTapGesture {
                                let now = Date()
                                // Reset count if more than 2 seconds since last tap
                                if now.timeIntervalSince(lastTapTime) > 2.0 {
                                    versionTapCount = 1
                                } else {
                                    versionTapCount += 1
                                }
                                lastTapTime = now

                                // Trigger on 5th tap
                                if versionTapCount >= 5 {
                                    versionTapCount = 0 // Reset
                                    showingCodePrompt = true
                                    HapticManager.shared.lightImpact()
                                }
                            }
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
                .sheet(isPresented: $showingStore) {
                    StoreView()
                        .presentationDragIndicator(.visible)
                }
                .alert("Enter Access Code", isPresented: $showingCodePrompt) {
                    TextField("Code", text: $codeInput)
                        .textInputAutocapitalization(.characters)
                        .autocorrectionDisabled()

                    Button("Cancel", role: .cancel) {
                        codeInput = ""
                    }

                    Button("Submit") {
                        validateAndActivateBypass()
                    }
                } message: {
                    Text("Enter the developer access code")
                }
                .alert("Invalid Code", isPresented: $showingErrorAlert) {
                    Button("OK", role: .cancel) { }
                } message: {
                    Text("The code you entered is not valid.")
                }
                .alert("Deactivate Developer Access?", isPresented: $showingDeactivateAlert) {
                    Button("Cancel", role: .cancel) { }
                    Button("Deactivate", role: .destructive) {
                        developerBypassManager.deactivateBypass()
                        HapticManager.shared.lightImpact()
                    }
                } message: {
                    Text("All expansion packs will return to their normal purchase state. Any packs you've actually purchased will remain available.")
                }
            }
        }

    private var settingsSwipeGesture: some Gesture {
        DragGesture(minimumDistance: 10)
            .onChanged { value in
                guard swipeNavigationManager.isSwipeNavigationEnabled else { return }

                let distance = value.translation.width
                let velocity = (value.predictedEndTranslation.width - distance) / 0.016

                // Real-time drag tracking
                onDrag?(distance, velocity, false)
            }
            .onEnded { value in
                guard swipeNavigationManager.isSwipeNavigationEnabled else { return }

                let distance = value.translation.width
                let velocity = (value.predictedEndTranslation.width - distance) / 0.016

                // Signal end of drag
                onDrag?(distance, velocity, true)
                HapticManager.shared.lightImpact()
            }
    }

    private func validateAndActivateBypass() {
        let trimmedCode = codeInput.trimmingCharacters(in: .whitespacesAndNewlines)

        if trimmedCode == "FAMILY" || trimmedCode == "DEVELOPER" {
            developerBypassManager.activateBypass()
            HapticManager.shared.correctAnswerEffect()
            codeInput = ""
        } else {
            codeInput = ""
            showingErrorAlert = true
            HapticManager.shared.lightImpact()
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
