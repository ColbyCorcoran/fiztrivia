import SwiftUI

struct HapticsSettingsView: View {
    @StateObject private var hapticSettingsManager = HapticSettingsManager.shared
    @StateObject private var swipeNavigationManager = SwipeNavigationManager.shared

    private var backgroundGradient: some View {
        Color(.systemGroupedBackground)
            .ignoresSafeArea()
    }

    var body: some View {
        Form {
            Section(footer: Text("Haptic feedback provides tactile responses when you interact with the app.")) {
                Toggle("Haptic Feedback", isOn: Binding(
                    get: { hapticSettingsManager.isHapticEnabled },
                    set: { hapticSettingsManager.setHapticEnabled($0) }
                ))
                .accessibilityHint("Enable or disable haptic feedback")
            }

            Section(footer: Text("Swipe left/right on the main screen to navigate between Leaderboard, Main Wheel, and Settings. Swipe gestures only work when no question is active.")) {
                Toggle("Swipe Navigation", isOn: Binding(
                    get: { swipeNavigationManager.isSwipeNavigationEnabled },
                    set: { swipeNavigationManager.setSwipeNavigationEnabled($0) }
                ))
                .accessibilityHint("Enable or disable swipe navigation between screens")
            }
        }
        .scrollContentBackground(.hidden)
        .background(backgroundGradient)
        .navigationTitle("Interaction")
        .navigationBarTitleDisplayMode(.large)
    }
}

#Preview {
    NavigationStack {
        HapticsSettingsView()
    }
}
