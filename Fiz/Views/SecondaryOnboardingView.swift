import SwiftUI

struct SecondaryOnboardingView: View {
    @Environment(\.dismiss) private var dismiss
    @StateObject private var onboardingManager = OnboardingManager.shared
    @State private var currentPage = 0
    @State private var showDontShowAgainConfirmation = false

    private let features: [OnboardingFeature] = [
        .difficulty,
        .categorySelection,
        .phobiaFilters,
        .gameModes
    ]

    private var isLastPage: Bool {
        currentPage == features.count - 1
    }

    var body: some View {
        ZStack {
            // Background gradient
            LinearGradient(
                gradient: Gradient(colors: [Color.fizBackground, Color.fizBackgroundSecondary]),
                startPoint: .topLeading,
                endPoint: .bottomTrailing
            )
            .ignoresSafeArea()

            VStack(spacing: 0) {
                // Header
                HStack {
                    Button(action: {
                        showDontShowAgainConfirmation = true
                    }) {
                        Text("Don't show again")
                            .font(.subheadline)
                            .foregroundColor(.secondary)
                    }

                    Spacer()

                    Button(action: skipOnboarding) {
                        Text("Skip")
                            .font(.headline)
                            .foregroundColor(.fizOrange)
                    }
                }
                .padding(.horizontal, 20)
                .padding(.top, 20)
                .padding(.bottom, 10)

                // Title
                Text("What's New in Fiz")
                    .font(.largeTitle.bold())
                    .foregroundColor(.primary)
                    .padding(.top, 10)
                    .padding(.bottom, 20)

                // Feature cards carousel
                TabView(selection: $currentPage) {
                    ForEach(Array(features.enumerated()), id: \.offset) { index, feature in
                        FeatureCardView(feature: feature)
                            .tag(index)
                    }
                }
                .tabViewStyle(.page(indexDisplayMode: .never))
                .frame(maxWidth: .infinity, maxHeight: .infinity)

                // Page indicators
                HStack(spacing: 8) {
                    ForEach(0..<features.count, id: \.self) { index in
                        Circle()
                            .fill(currentPage == index ? Color.fizOrange : Color.gray.opacity(0.3))
                            .frame(width: 8, height: 8)
                            .animation(.easeInOut, value: currentPage)
                    }
                }
                .padding(.vertical, 20)

                // Navigation button
                Button(action: nextOrDone) {
                    Text(isLastPage ? "Get Started" : "Next")
                        .font(.headline)
                        .foregroundColor(.white)
                        .frame(maxWidth: .infinity)
                        .frame(height: 50)
                        .background(Color.fizOrange)
                        .cornerRadius(12)
                }
                .padding(.horizontal, 20)
                .padding(.bottom, 40)
            }
        }
        .alert("Skip Feature Tour?", isPresented: $showDontShowAgainConfirmation) {
            Button("Cancel", role: .cancel) { }
            Button("Don't Show Again", role: .destructive) {
                onboardingManager.dismissSecondaryOnboardingPermanently()
                AnalyticsManager.shared.trackSecondaryOnboardingDismissed(atPage: currentPage)
                dismiss()
            }
        } message: {
            Text("You can always revisit this tour from Settings > Feature Tour.")
        }
    }

    private func nextOrDone() {
        HapticManager.shared.buttonTapEffect()

        if isLastPage {
            // Track completion
            AnalyticsManager.shared.trackSecondaryOnboardingCompleted()
            onboardingManager.markSecondaryOnboardingAsShown()
            dismiss()
        } else {
            // Track page view
            AnalyticsManager.shared.trackSecondaryOnboardingPageViewed(page: currentPage + 1)
            withAnimation {
                currentPage += 1
            }
        }
    }

    private func skipOnboarding() {
        HapticManager.shared.buttonTapEffect()
        AnalyticsManager.shared.trackSecondaryOnboardingSkipped(atPage: currentPage)
        onboardingManager.markSecondaryOnboardingAsShown()
        dismiss()
    }
}

// MARK: - Feature Card View
struct FeatureCardView: View {
    let feature: OnboardingFeature

    var body: some View {
        VStack(spacing: 20) {
            Spacer()

            // Icon
            Image(systemName: feature.icon)
                .font(.system(size: 80))
                .foregroundColor(feature.color)
                .padding(.bottom, 10)

            // Title
            Text(feature.title)
                .font(.title.bold())
                .foregroundColor(.primary)
                .multilineTextAlignment(.center)
                .padding(.horizontal, 30)

            // Description
            Text(feature.description)
                .font(.body)
                .foregroundColor(.secondary)
                .multilineTextAlignment(.center)
                .padding(.horizontal, 40)
                .fixedSize(horizontal: false, vertical: true)

            Spacer()
        }
        .padding()
    }
}

// MARK: - Onboarding Feature Model
enum OnboardingFeature {
    case difficulty
    case categorySelection
    case phobiaFilters
    case gameModes

    var icon: String {
        switch self {
        case .difficulty:
            return "speedometer"
        case .categorySelection:
            return "chart.pie.fill"
        case .phobiaFilters:
            return "eye.slash.fill"
        case .gameModes:
            return "gamecontroller.fill"
        }
    }

    var color: Color {
        switch self {
        case .difficulty, .categorySelection, .gameModes:
            return .fizOrange
        case .phobiaFilters:
            return .fizTeal
        }
    }

    var title: String {
        switch self {
        case .difficulty:
            return "Find Your Perfect Challenge"
        case .categorySelection:
            return "Choose Your Categories"
        case .phobiaFilters:
            return "Stay Comfortable"
        case .gameModes:
            return "Practice Makes Perfect"
        }
    }

    var description: String {
        switch self {
        case .difficulty:
            return "Select Casual for easy questions, Normal for a mix, or Difficult for the ultimate trivia challenge."
        case .categorySelection:
            return "Pick 2-12 categories for your wheel and save your favorites as your personal default."
        case .phobiaFilters:
            return "Exclude topics that make you uncomfortable. Your wellbeing matters to us."
        case .gameModes:
            return "Use Single Category Mode to focus on one topic and master it question by question."
        }
    }
}

#Preview {
    SecondaryOnboardingView()
        .modelContainer(for: LeaderboardEntry.self, inMemory: true)
}
