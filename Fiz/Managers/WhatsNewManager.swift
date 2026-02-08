//
//  WhatsNewManager.swift
//  Fiz
//
//  Extracted from TriviaModels.swift
//

import Foundation

/// Manages "What's New" feature state and version-based update announcements
class WhatsNewManager: ObservableObject {
    private static let lastSeenVersionKey = "last_seen_app_version"

    @Published var shouldShowWhatsNew: Bool = false
    @Published var updatesToShow: [WhatsNewUpdate] = []

    static let shared = WhatsNewManager()

    // Define updates here - add new ones at the TOP when you push updates
    // Updates are shown in order: newest first
    private let updates: [WhatsNewUpdate] = [
        // Example for when you add expansions:
        // WhatsNewUpdate(
        //     version: "1.3.0",
        //     title: "New Feature Name",
        //     features: [
        //         WhatsNewFeature(icon: "star.fill", title: "Feature Title", description: "Feature description")
        //     ]
        // ),
        // WhatsNewUpdate(
        //     version: "1.2.0",
        //     title: "Previous Update",
        //     features: [
        //         WhatsNewFeature(icon: "sparkles", title: "Old Feature", description: "This will show below v1.3")
        //     ]
        // ),
        // WhatsNewUpdate(
        //     version: "1.1.0",
        //     title: "Question Expansions!",
        //     features: [
        //         WhatsNewFeature(icon: "purchased.circle.fill", title: "Expansion Packs", description: "Purchase themed question packs to expand your trivia library"),
        //         WhatsNewFeature(icon: "star.fill", title: "Premium Categories", description: "Access exclusive categories like Movies, TV Shows, and more")
        //     ]
        // )
    ]

    private init() {
        checkForNewVersion()
    }

    private func checkForNewVersion() {
        guard let currentVersion = Bundle.main.infoDictionary?["CFBundleShortVersionString"] as? String else {
            return
        }

        let lastSeenVersion = UserDefaults.standard.string(forKey: UserDefaultsKeys.WhatsNew.lastSeenVersion)

        // First launch ever or version changed
        if lastSeenVersion != currentVersion {
            // Check if current version has an update defined
            if updates.contains(where: { $0.version == currentVersion }) {
                // Show all available updates (running changelog)
                updatesToShow = updates
                shouldShowWhatsNew = true
            } else {
                // No update defined for this version - just mark as seen
                markCurrentVersionAsSeen()
            }
        }
    }

    func markCurrentVersionAsSeen() {
        if let currentVersion = Bundle.main.infoDictionary?["CFBundleShortVersionString"] as? String {
            UserDefaults.standard.set(currentVersion, forKey: UserDefaultsKeys.WhatsNew.lastSeenVersion)
        }
        shouldShowWhatsNew = false
        updatesToShow = []
    }

    func forceShowWhatsNew() {
        // For testing - show all updates
        if !updates.isEmpty {
            updatesToShow = updates
            shouldShowWhatsNew = true
        }
    }

    func resetForTesting() {
        UserDefaults.standard.removeObject(forKey: UserDefaultsKeys.WhatsNew.lastSeenVersion)
        checkForNewVersion()
    }
}
