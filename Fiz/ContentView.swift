//
//  ContentView.swift
//  Fiz
//
//  Created by Colby Corcoran on 8/12/25.
//

import SwiftUI
import SwiftData

struct ContentView: View {
    @State private var gameViewModel = GameViewModel()
    @StateObject private var userManager = UserManager.shared
    @StateObject private var swipeNavigationManager = SwipeNavigationManager.shared
    @StateObject private var onboardingManager = OnboardingManager.shared
    @StateObject private var whatsNewManager = WhatsNewManager.shared

    // Live drag offset for real-time page following during swipe
    @State private var liveDragOffset: CGFloat = 0

    var body: some View {
        Group {
            if !userManager.hasCompletedOnboarding {
                OnboardingView()
            } else {
                gameView
            }
        }
        // Cap Dynamic Type at accessibility3 — the inline expansion looks great here.
        // Users with larger device settings still get a well-laid-out accessible experience,
        // just capped so the layout stays intact. The modal fallback handles the one tier above.
        .dynamicTypeSize(...DynamicTypeSize.accessibility2)
        .animation(.easeInOut(duration: 0.3), value: userManager.hasCompletedOnboarding)
        .sheet(isPresented: $onboardingManager.shouldShowSecondaryOnboarding) {
            SecondaryOnboardingView()
                .interactiveDismissDisabled(false)
                .onAppear {
                    AnalyticsManager.shared.trackSecondaryOnboardingViewed()
                }
        }
        .sheet(isPresented: $whatsNewManager.shouldShowWhatsNew) {
            if !whatsNewManager.updatesToShow.isEmpty {
                WhatsNewView(updates: whatsNewManager.updatesToShow)
                    .interactiveDismissDisabled(false)
                    .onAppear {
                        let latestVersion = whatsNewManager.updatesToShow.first?.version ?? ""
                        AnalyticsManager.shared.trackWhatsNewViewed(version: latestVersion)
                    }
            }
        }
    }

    private var gameView: some View {
        GeometryReader { geometry in
            let screenWidth = geometry.size.width
            ZStack {
                // Leaderboard (left page)
                LeaderboardView(
                    gameViewModel: gameViewModel,
                    onSwipe: handleSwipe,
                    onDragChanged: handleDragChanged,
                    onDragEnded: handleDragEnded
                )
                .offset(x: calculateLeaderboardOffset(screenWidth: screenWidth))
                .zIndex(gameViewModel.gameState == .leaderboard ? 1 : 0)

                // Main wheel (center page)
                CategoryWheelView(
                    gameViewModel: gameViewModel,
                    onSwipe: handleSwipe,
                    onDragChanged: handleDragChanged,
                    onDragEnded: handleDragEnded
                )
                .offset(x: calculateMainOffset(screenWidth: screenWidth))
                .zIndex(gameViewModel.gameState == .selectingCategory ? 1 : 0)

                // Settings (right page)
                SettingsView(
                    gameViewModel: gameViewModel,
                    onSwipe: handleSwipe,
                    onDragChanged: handleDragChanged,
                    onDragEnded: handleDragEnded
                )
                .offset(x: calculateSettingsOffset(screenWidth: screenWidth))
                .zIndex(gameViewModel.gameState == .settings ? 1 : 0)
            }
            // No implicit animation here — snap/spring is applied explicitly via withAnimation
            // in handleDragEnded/handleSwipe so there's zero animation overhead during live drag
        }
    }

    private func calculateLeaderboardOffset(screenWidth: CGFloat) -> CGFloat {
        let baseOffset: CGFloat
        switch gameViewModel.gameState {
        case .leaderboard:
            baseOffset = 0
        case .selectingCategory:
            baseOffset = -screenWidth
        case .settings:
            baseOffset = -screenWidth * 2
        }
        return baseOffset + liveDragOffset
    }

    private func calculateMainOffset(screenWidth: CGFloat) -> CGFloat {
        let baseOffset: CGFloat
        switch gameViewModel.gameState {
        case .leaderboard:
            baseOffset = screenWidth
        case .selectingCategory:
            baseOffset = 0
        case .settings:
            baseOffset = -screenWidth
        }
        return baseOffset + liveDragOffset
    }

    private func calculateSettingsOffset(screenWidth: CGFloat) -> CGFloat {
        let baseOffset: CGFloat
        switch gameViewModel.gameState {
        case .leaderboard:
            baseOffset = screenWidth * 2
        case .selectingCategory:
            baseOffset = screenWidth
        case .settings:
            baseOffset = 0
        }
        return baseOffset + liveDragOffset
    }

    private func handleDragChanged(_ translation: CGFloat) {
        // Direct assignment — no animation, this must follow the finger in real time
        liveDragOffset = translation
    }

    private func handleDragEnded() {
        // Spring snap back to resting position after finger lifts
        withAnimation(.spring(response: 0.3, dampingFraction: 0.85)) {
            liveDragOffset = 0
        }
    }

    private func handleSwipe(_ direction: SwipeDirection) {
        guard swipeNavigationManager.isSwipeNavigationEnabled else { return }

        withAnimation(.spring(response: 0.3, dampingFraction: 0.85)) {
            switch (gameViewModel.gameState, direction) {
            case (.selectingCategory, .right):
                gameViewModel.gameState = .leaderboard
            case (.selectingCategory, .left):
                gameViewModel.gameState = .settings
            case (.leaderboard, .left):
                gameViewModel.gameState = .selectingCategory
            case (.settings, .right):
                gameViewModel.gameState = .selectingCategory
            default:
                break
            }
        }
    }
}

enum SwipeDirection {
    case left
    case right

    var description: String {
        switch self {
        case .left: return "LEFT"
        case .right: return "RIGHT"
        }
    }
}

#Preview {
    ContentView()
        .modelContainer(for: LeaderboardEntry.self, inMemory: true)
}
