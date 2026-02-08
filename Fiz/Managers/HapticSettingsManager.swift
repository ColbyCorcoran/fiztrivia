//
//  HapticSettingsManager.swift
//  Fiz
//
//  Extracted from TriviaModels.swift
//

import Foundation

/// Manages user preference for haptic feedback
class HapticSettingsManager: ObservableObject {
    private static let hapticEnabledKey = "haptic_feedback_enabled"

    @Published var isHapticEnabled: Bool = true

    static let shared = HapticSettingsManager()

    private init() {
        loadSettings()
    }

    private func loadSettings() {
        // Default to true if no preference is saved
        if UserDefaults.standard.object(forKey: UserDefaultsKeys.Settings.hapticEnabled) != nil {
            isHapticEnabled = UserDefaults.standard.bool(forKey: UserDefaultsKeys.Settings.hapticEnabled)
        } else {
            isHapticEnabled = true
        }
    }

    func setHapticEnabled(_ enabled: Bool) {
        isHapticEnabled = enabled
        UserDefaults.standard.set(enabled, forKey: UserDefaultsKeys.Settings.hapticEnabled)
    }
}
