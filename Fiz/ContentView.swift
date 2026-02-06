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

    // Interactive gesture tracking
    @State private var dragOffset: CGFloat = 0
    @State private var isDragging: Bool = false

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
                LeaderboardView(gameViewModel: gameViewModel, onSwipe: handleSwipe, onDrag: handleDrag)
                    .offset(x: calculateLeaderboardOffset(screenWidth: geometry.size.width) + dragOffset)
                    .opacity(calculateOpacity(for: .leaderboard))
                    .zIndex(gameViewModel.gameState == .leaderboard ? 1 : 0)

                // Main wheel (center page)
                CategoryWheelView(gameViewModel: gameViewModel, onSwipe: handleSwipe, onDrag: handleDrag)
                    .offset(x: calculateMainOffset(screenWidth: geometry.size.width) + dragOffset)
                    .zIndex(gameViewModel.gameState == .selectingCategory ? 1 : 0)

                // Settings (right page)
                SettingsView(gameViewModel: gameViewModel, onSwipe: handleSwipe, onDrag: handleDrag)
                    .offset(x: calculateSettingsOffset(screenWidth: geometry.size.width) + dragOffset)
                    .opacity(calculateOpacity(for: .settings))
                    .zIndex(gameViewModel.gameState == .settings ? 1 : 0)
            }
        }
        .animation(isDragging ? nil : .spring(response: 0.25, dampingFraction: 0.85), value: gameViewModel.gameState)
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

    private func calculateOpacity(for state: GameState) -> Double {
        if isDragging {
            // During drag, gradually fade opacity based on drag distance
            let normalizedOffset = abs(dragOffset) / 100.0
            if gameViewModel.gameState == state {
                return max(0.3, 1.0 - normalizedOffset)
            } else {
                return min(1.0, 0.3 + normalizedOffset)
            }
        } else {
            return gameViewModel.gameState == state ? 1 : 0.3
        }
    }

    private func handleDrag(translation: CGFloat, velocity: CGFloat, isEnded: Bool) {
        guard swipeNavigationManager.isSwipeNavigationEnabled else { return }

        if isEnded {
            // Gesture ended - determine if we should navigate
            isDragging = false

            let threshold: CGFloat = 100 // Minimum drag distance
            let velocityThreshold: CGFloat = 500 // Fast swipe threshold

            // Determine if user intended to navigate
            let shouldNavigate = abs(translation) > threshold || abs(velocity) > velocityThreshold

            if shouldNavigate {
                if translation > 0 {
                    // Swiped right
                    handleSwipe(.right)
                } else {
                    // Swiped left
                    handleSwipe(.left)
                }
            }

            // Reset drag offset with animation
            withAnimation(.spring(response: 0.25, dampingFraction: 0.85)) {
                dragOffset = 0
            }
        } else {
            // Gesture in progress - update offset in real-time
            isDragging = true

            // Apply rubber banding at edges
            let rubberBandedOffset = applyRubberBanding(translation: translation)
            dragOffset = rubberBandedOffset
        }
    }

    private func applyRubberBanding(translation: CGFloat) -> CGFloat {
        // Check if we're at the edge of navigation
        let atLeftEdge = gameViewModel.gameState == .leaderboard && translation > 0
        let atRightEdge = gameViewModel.gameState == .settings && translation < 0

        if atLeftEdge || atRightEdge {
            // Apply rubber banding resistance (logarithmic)
            let resistance: CGFloat = 0.3
            return translation * resistance
        }

        return translation
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
