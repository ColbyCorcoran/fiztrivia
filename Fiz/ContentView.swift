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

    var body: some View {
        Group {
            if !userManager.hasCompletedOnboarding {
                OnboardingView()
            } else {
                gameView
            }
        }
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
            ZStack {
                // Leaderboard (left page)
                LeaderboardView(gameViewModel: gameViewModel, onSwipe: handleSwipe)
                    .offset(x: calculateLeaderboardOffset(screenWidth: geometry.size.width))
                    .opacity(gameViewModel.gameState == .leaderboard ? 1 : 0.3)
                    .zIndex(gameViewModel.gameState == .leaderboard ? 1 : 0)

                // Main wheel (center page)
                CategoryWheelView(gameViewModel: gameViewModel, onSwipe: handleSwipe)
                    .offset(x: calculateMainOffset(screenWidth: geometry.size.width))
                    .zIndex(gameViewModel.gameState == .selectingCategory ? 1 : 0)

                // Settings (right page)
                SettingsView(gameViewModel: gameViewModel, onSwipe: handleSwipe)
                    .offset(x: calculateSettingsOffset(screenWidth: geometry.size.width))
                    .opacity(gameViewModel.gameState == .settings ? 1 : 0.3)
                    .zIndex(gameViewModel.gameState == .settings ? 1 : 0)
            }
        }
        .animation(.easeInOut(duration: 0.3), value: gameViewModel.gameState)
    }

    private func calculateLeaderboardOffset(screenWidth: CGFloat) -> CGFloat {
        switch gameViewModel.gameState {
        case .leaderboard:
            return 0
        case .selectingCategory:
            return -screenWidth
        case .settings:
            return -screenWidth * 2
        }
    }

    private func calculateMainOffset(screenWidth: CGFloat) -> CGFloat {
        switch gameViewModel.gameState {
        case .leaderboard:
            return screenWidth
        case .selectingCategory:
            return 0
        case .settings:
            return -screenWidth
        }
    }

    private func calculateSettingsOffset(screenWidth: CGFloat) -> CGFloat {
        switch gameViewModel.gameState {
        case .leaderboard:
            return screenWidth * 2
        case .selectingCategory:
            return screenWidth
        case .settings:
            return 0
        }
    }

    private func handleSwipe(_ direction: SwipeDirection) {
        guard swipeNavigationManager.isSwipeNavigationEnabled else { return }

        // Instant state change - no preview, no lag
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

enum SwipeDirection {
    case left
    case right
}

#Preview {
    ContentView()
        .modelContainer(for: LeaderboardEntry.self, inMemory: true)
}
