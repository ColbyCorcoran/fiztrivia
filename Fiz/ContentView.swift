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
                LeaderboardView(gameViewModel: gameViewModel, onDrag: handleDrag)
                    .offset(x: calculateLeaderboardOffset(screenWidth: geometry.size.width) + dragOffset)
                    .opacity(calculateOpacity(for: .leaderboard))
                    .zIndex(gameViewModel.gameState == .leaderboard ? 1 : 0)

                // Main wheel (center page)
                CategoryWheelView(gameViewModel: gameViewModel, onDrag: handleDrag)
                    .offset(x: calculateMainOffset(screenWidth: geometry.size.width) + dragOffset)
                    .opacity(calculateOpacity(for: .selectingCategory))
                    .zIndex(gameViewModel.gameState == .selectingCategory ? 1 : 0)

                // Settings (right page)
                SettingsView(gameViewModel: gameViewModel, onDrag: handleDrag)
                    .offset(x: calculateSettingsOffset(screenWidth: geometry.size.width) + dragOffset)
                    .opacity(calculateOpacity(for: .settings))
                    .zIndex(gameViewModel.gameState == .settings ? 1 : 0)
            }
        }
        .animation(.spring(response: 0.3, dampingFraction: 0.86), value: gameViewModel.gameState)
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
        let isActive = gameViewModel.gameState == state

        if isDragging && !isActive {
            // Incoming view fades in gradually during drag (0.3 → 1.0)
            // This provides visual feedback without flickering the active view
            let normalizedOffset = min(abs(dragOffset) / 100.0, 1.0)  // 0.0 to 1.0
            return 0.3 + (0.7 * normalizedOffset)  // Fade from 0.3 to 1.0
        }

        return isActive ? 1.0 : 0.3
    }

    private func handleDrag(translation: CGFloat, velocity: CGFloat, isEnded: Bool) {
        guard swipeNavigationManager.isSwipeNavigationEnabled else { return }

        if isEnded {
            // DIAGNOSTIC: Log gesture completion
            print("🔵 GESTURE END - translation: \(translation), velocity: \(velocity), dragOffset: \(dragOffset), state: \(gameViewModel.gameState)")

            // Calculate navigation decision
            let threshold: CGFloat = 100
            let velocityThreshold: CGFloat = 800  // Increased from 500 for more deliberate fast swipes

            var shouldNavigate = false
            var navigationDirection: SwipeDirection?

            // Check if at navigation boundary (rubber banding edge)
            let atBoundary = isAtNavigationBoundary(translation: translation)

            // Decision tree:
            if atBoundary {
                // At edge boundary - don't navigate, just snap back
                print("🔴 AT BOUNDARY - no navigation (translation: \(translation))")
            } else if abs(velocity) > velocityThreshold {
                // 1. Very fast swipe - always honor velocity direction
                shouldNavigate = true
                navigationDirection = velocity > 0 ? .right : .left
                print("🟢 FAST SWIPE - velocity \(velocity) → \(navigationDirection?.description ?? "nil")")
            } else if abs(translation) > threshold {
                // 2. Slow drag past threshold
                // Check if velocity opposes translation (user trying to cancel)
                let translationDirection = translation > 0 ? 1 : -1
                let velocityDirection = velocity > 0 ? 1 : -1

                // If velocity is significant AND opposite to translation, user is canceling
                if abs(velocity) > 200 && (translationDirection != velocityDirection) {
                    // Cancellation: user crossed threshold but is now reversing with significant speed
                    print("🔴 CANCELLED - reversal detected (translation: \(translation), velocity: \(velocity))")
                } else {
                    // Normal slow drag - use translation direction
                    shouldNavigate = true
                    navigationDirection = translation > 0 ? .right : .left
                    print("🟢 SLOW DRAG - translation \(translation) → \(navigationDirection?.description ?? "nil")")
                }
            } else {
                print("🟡 SNAP BACK - translation \(translation) below threshold")
            }

            // Determine target state
            var targetState = gameViewModel.gameState
            if shouldNavigate, let direction = navigationDirection {
                targetState = navigationTarget(from: gameViewModel.gameState, direction: direction)
            }

            // Batch ALL updates in single animated transaction
            withAnimation(.spring(response: 0.3, dampingFraction: 0.86)) {  // Slightly slower for Apple feel
                isDragging = false
                dragOffset = 0
                gameViewModel.gameState = targetState
            }
        } else {
            // Gesture in progress - direct updates for instant feedback
            isDragging = true
            let newOffset = applyRubberBanding(translation: translation)

            // Reduce jitter: increased threshold to 3pt (from 1pt)
            if abs(newOffset - dragOffset) > 3 {
                dragOffset = newOffset
            }
        }
    }

    // Helper to check if user is trying to navigate beyond boundaries
    private func isAtNavigationBoundary(translation: CGFloat) -> Bool {
        let tryingToGoLeftFromLeaderboard = gameViewModel.gameState == .leaderboard && translation > 0
        let tryingToGoRightFromSettings = gameViewModel.gameState == .settings && translation < 0
        return tryingToGoLeftFromLeaderboard || tryingToGoRightFromSettings
    }

    // Helper to determine navigation target
    private func navigationTarget(from state: GameState, direction: SwipeDirection) -> GameState {
        switch (state, direction) {
        case (.selectingCategory, .right):
            return .leaderboard
        case (.selectingCategory, .left):
            return .settings
        case (.leaderboard, .left):
            return .selectingCategory
        case (.settings, .right):
            return .selectingCategory
        default:
            return state
        }
    }

    private func applyRubberBanding(translation: CGFloat) -> CGFloat {
        // Check if we're trying to drag BEYOND the navigation boundaries
        // Left edge: at Leaderboard and swiping right (trying to go further left beyond edge)
        let atLeftEdge = gameViewModel.gameState == .leaderboard && translation > 0
        // Right edge: at Settings and swiping left (trying to go further right beyond edge)
        let atRightEdge = gameViewModel.gameState == .settings && translation < 0

        if atLeftEdge || atRightEdge {
            // Apply rubber banding resistance (logarithmic)
            let resistance: CGFloat = 0.3
            return translation * resistance
        }

        return translation
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
