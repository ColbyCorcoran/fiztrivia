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
        .gameModes,
        .expansionPacks
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
//                    Button(action: {
//                        showDontShowAgainConfirmation = true
//                    }) {
//                        Text("Don't show again")
//                            .font(.subheadline)
//                            .foregroundColor(.secondary)
//                    }

                    Spacer()
                    
                    

                    Button(action: skipOnboarding) {
                        Image(systemName: "xmark")
                            .font(.title3.weight(.semibold))
                    }
                    .glassButtonStyle()
                    .tint(.fizOrange)
                }
                .padding(.horizontal, 20)
                .padding(.top, 20)
                .padding(.bottom, 10)

                // Title
                Text("Key Fiz Features")
                    .font(.largeTitle.bold())
                    .foregroundColor(.primary)
                    .padding(.top, 10)
                
                // Subtitle
                Text("Trivia, designed just for you")
                    .font(.subheadline)
                    .foregroundColor(.secondary)
                    .padding(.top, 10)

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
    case expansionPacks

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
        case .expansionPacks:
            return "rectangle.stack.badge.plus"
        }
    }

    var color: Color {
        switch self {
        case .difficulty, .categorySelection, .gameModes, .expansionPacks:
            return .fizOrange
        case .phobiaFilters:
            return .fizTeal
        }
    }

    var title: String {
        switch self {
        case .difficulty:
            return "Find Your Perfect Challenge with Game Difficulty"
        case .categorySelection:
            return "Pick What You Answer with Category Selection"
        case .phobiaFilters:
            return "Stay Comfortable with Phobia Filters"
        case .gameModes:
            return "Play Your Way with Game Modes"
        case .expansionPacks:
            return "Add More Questions with Expansion Packs"
        }
    }

    var description: String {
        switch self {
        case .difficulty:
            return "Choose between Casual, Normal, or Difficult for your perfect trivia challenge."
        case .categorySelection:
            return "Select 2-12 categories for your wheel to choose what questions you answer. Add or remove categories at any time, and save your favorites as your personal default for faster, easier access."
        case .phobiaFilters:
            return "Add Phobia Filters to exclude questions & topics that make you uncomfortable. Your wellbeing matters to us."
        case .gameModes:
            return "Use Single Category Mode or Single Topic Mode to focus in and master that chosen area, question by question."
        case .expansionPacks:
            return "Purchase Expansion Packs from our Store to add more questions from your favorite topics to your game. Each available Expansion Pack includes free preview questions for all players, whether you purchase it or not!"
        }
    }
}

#Preview {
    SecondaryOnboardingView()
        .modelContainer(for: LeaderboardEntry.self, inMemory: true)
}
