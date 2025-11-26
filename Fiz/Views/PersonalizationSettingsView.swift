import SwiftUI

struct PersonalizationSettingsView: View {
    @Bindable var gameViewModel: GameViewModel
    @StateObject private var userManager = UserManager.shared
    @StateObject private var appIconManager = AppIconManager.shared
    @StateObject private var hapticSettingsManager = HapticSettingsManager.shared
    @StateObject private var analyticsManager = AnalyticsManager.shared
    @State private var editedUsername: String = ""
    @State private var isEditingUsername = false

    var body: some View {
        Form {
            Section("Profile") {
                HStack {
                    Text("Username")
                    Spacer()

                    if isEditingUsername {
                        TextField("Enter username", text: $editedUsername)
                            .textFieldStyle(RoundedBorderTextFieldStyle())
                            .autocorrectionDisabled()
                            .textInputAutocapitalization(.words)
                            .frame(maxWidth: 150)
                            .onSubmit {
                                saveUsername()
                            }

                        Button("Save") {
                            saveUsername()
                        }
                        .font(.caption)
                        .foregroundColor(.blue)

                        Button("Cancel") {
                            cancelEditing()
                        }
                        .font(.caption)
                        .foregroundColor(.secondary)

                    } else {
                        Button(userManager.displayName) {
                            startEditing()
                        }
                        .foregroundColor(.blue)
                        .font(.body)
                    }
                }
            }

            Section(header: Text("App Icon"),
                   footer: Text("Choose your favorite Fiz to represent your app!")) {
                LazyVGrid(columns: [
                    GridItem(.flexible()),
                    GridItem(.flexible()),
                    GridItem(.flexible())
                ], spacing: 16) {
                    ForEach(AppIconManager.AppIcon.allCases) { icon in
                        Button(action: {
                            HapticManager.shared.buttonTapEffect()
                            appIconManager.setIcon(icon)
                        }) {
                            VStack(spacing: 8) {
                                Image(icon.previewImageName)
                                    .resizable()
                                    .scaledToFit()
                                    .frame(width: 60, height: 60)
                                    .clipShape(RoundedRectangle(cornerRadius: 12))
                                    .overlay(
                                        RoundedRectangle(cornerRadius: 12)
                                            .stroke(appIconManager.selectedIcon == icon ? Color.fizTeal : Color.clear, lineWidth: 3)
                                    )
                                    .shadow(color: Color.fizBrown.opacity(0.2), radius: 4, x: 0, y: 2)

                                Text(icon.rawValue)
                                    .font(.caption)
                                    .foregroundColor(.primary)
                                    .multilineTextAlignment(.center)
                                    .lineLimit(2)
                                    .frame(height: 30)
                            }
                            .frame(maxWidth: .infinity)
                        }
                        .buttonStyle(.plain)
                    }
                }
                .padding(.vertical, 8)
            }

            Section(header: Text("Haptics"),
                   footer: Text("Haptic feedback provides tactile responses when you interact with the app.")) {
                Toggle("Haptic Feedback", isOn: Binding(
                    get: { hapticSettingsManager.isHapticEnabled },
                    set: { hapticSettingsManager.setHapticEnabled($0) }
                ))
                    .accessibilityHint("Enable or disable haptic feedback")
            }

            Section(header: Text("Analytics"),
                   footer: Text("Help improve Fiz by sharing anonymous usage data. We only track which features you use - no personal information, location, or question answers are collected.")) {
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
        .navigationTitle("Personalization")
        .navigationBarTitleDisplayMode(.large)
    }

    private func startEditing() {
        editedUsername = userManager.username
        isEditingUsername = true
    }

    private func saveUsername() {
        let trimmedName = editedUsername.trimmingCharacters(in: .whitespacesAndNewlines)
        if !trimmedName.isEmpty {
            userManager.updateUsername(trimmedName)
            HapticManager.shared.buttonTapEffect()
        }
        isEditingUsername = false
        editedUsername = ""
    }

    private func cancelEditing() {
        isEditingUsername = false
        editedUsername = ""
    }
}

#Preview {
    NavigationStack {
        PersonalizationSettingsView(gameViewModel: GameViewModel())
    }
}
