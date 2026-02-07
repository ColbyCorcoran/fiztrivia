//
//  DeveloperBypassManager.swift
//  Fiz
//
//  Extracted from TriviaModels.swift
//

import Foundation

/// Developer bypass for testing IAP/expansion packs without actual purchases
class DeveloperBypassManager: ObservableObject {
    static let shared = DeveloperBypassManager()

    private static let bypassEnabledKey = "developer_bypass_enabled"

    @Published var isBypassActive: Bool = false

    private init() {
        loadBypassState()
    }

    private func loadBypassState() {
        isBypassActive = UserDefaults.standard.bool(forKey: UserDefaultsKeys.Developer.bypassEnabled)
    }

    func activateBypass() {
        isBypassActive = true
        UserDefaults.standard.set(true, forKey: UserDefaultsKeys.Developer.bypassEnabled)
        print("Developer bypass activated")
    }

    func deactivateBypass() {
        isBypassActive = false
        UserDefaults.standard.set(false, forKey: UserDefaultsKeys.Developer.bypassEnabled)
        print("Developer bypass deactivated")
    }
}
