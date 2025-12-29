import SwiftUI

struct HapticsSettingsView: View {
    @StateObject private var hapticSettingsManager = HapticSettingsManager.shared

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
        }
        .scrollContentBackground(.hidden)
        .background(backgroundGradient)
        .navigationTitle("Haptics")
        .navigationBarTitleDisplayMode(.large)
    }
}

#Preview {
    NavigationStack {
        HapticsSettingsView()
    }
}
