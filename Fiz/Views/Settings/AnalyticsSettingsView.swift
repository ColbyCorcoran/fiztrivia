import SwiftUI

struct AnalyticsSettingsView: View {
    @StateObject private var analyticsManager = AnalyticsManager.shared

    var body: some View {
        Form {
            Section(footer: Text("Help improve Fiz by sharing anonymous usage data. We only track which features you use - no personal information, location, or question answers are collected.")) {
                Toggle("Share Anonymous Analytics", isOn: Binding(
                    get: { analyticsManager.isAnalyticsEnabled },
                    set: { newValue in
                        analyticsManager.setAnalyticsEnabled(newValue)
                        if newValue {
                            // Track that analytics was enabled
                            analyticsManager.trackSettingChanged(setting: "analytics", value: "enabled")
                        }
                    }
                ))
                .accessibilityHint("Enable or disable anonymous analytics")
            }
        }
        .navigationTitle("Analytics")
        .navigationBarTitleDisplayMode(.large)
    }
}

#Preview {
    NavigationStack {
        AnalyticsSettingsView()
    }
}
