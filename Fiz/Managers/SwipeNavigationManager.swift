//
//  SwipeNavigationManager.swift
//  Fiz
//
//  Extracted from TriviaModels.swift
//

import Foundation

/// Manages swipe gesture navigation toggle (opt-out for accessibility)
class SwipeNavigationManager: ObservableObject {
    private static let swipeNavigationEnabledKey = "swipe_navigation_enabled"

    @Published var isSwipeNavigationEnabled: Bool = true

    static let shared = SwipeNavigationManager()

    private init() {
        loadSettings()
    }

    private func loadSettings() {
        // Default to true (opt-out for accessibility)
        if UserDefaults.standard.object(forKey: UserDefaultsKeys.Settings.swipeNavigationEnabled) != nil {
            isSwipeNavigationEnabled = UserDefaults.standard.bool(forKey: UserDefaultsKeys.Settings.swipeNavigationEnabled)
        } else {
            isSwipeNavigationEnabled = true
        }
    }

    func setSwipeNavigationEnabled(_ enabled: Bool) {
        isSwipeNavigationEnabled = enabled
        UserDefaults.standard.set(enabled, forKey: UserDefaultsKeys.Settings.swipeNavigationEnabled)
    }
}
