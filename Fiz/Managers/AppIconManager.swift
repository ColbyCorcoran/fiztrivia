//
//  AppIconManager.swift
//  Fiz
//
//  Extracted from TriviaModels.swift
//

import Foundation
import UIKit

/// Manages runtime app icon switching with 6 icon variants
class AppIconManager: ObservableObject {
    private static let selectedIconKey = "selected_app_icon"

    @Published var selectedIcon: AppIcon = .correct

    static let shared = AppIconManager()

    enum AppIcon: String, CaseIterable, Identifiable {
        case correct = "Correct"
        case regularPose = "Regular Pose"
        case happySmirk = "Happy Smirk"
        case incorrect = "Incorrect"
        case leaderboard = "Leaderboard"
        case newHighScore = "New High Score"

        var id: String { rawValue }

        var iconName: String? {
            // Return nil for the default icon (Correct - ships with the app)
            // For alternate icons, return the name that matches the bundle icon name
            switch self {
            case .correct: return nil  // Default - uses main AppIcon
            case .regularPose: return "AppIcon-RegularPose"
            case .happySmirk: return "AppIcon-HappySmirk"
            case .incorrect: return "AppIcon-Incorrect"
            case .leaderboard: return "AppIcon-Leaderboard"
            case .newHighScore: return "AppIcon-NewHighScore"
            }
        }

        var previewImageName: String {
            // Image names from Assets.xcassets for preview (with cream background to match actual app icons)
            switch self {
            case .correct: return "AppIcon-Correct-Preview"
            case .regularPose: return "AppIcon-RegularPose-Preview"
            case .happySmirk: return "AppIcon-HappySmirk-Preview"
            case .incorrect: return "AppIcon-Incorrect-Preview"
            case .leaderboard: return "AppIcon-Leaderboard-Preview"
            case .newHighScore: return "AppIcon-NewHighScore-Preview"
            }
        }

        var description: String {
            switch self {
            case .correct: return "Fiz celebrating (Default)"
            case .regularPose: return "Fiz in regular pose"
            case .happySmirk: return "Fiz with a happy smirk"
            case .incorrect: return "Fiz thinking"
            case .leaderboard: return "Fiz on the leaderboard"
            case .newHighScore: return "Fiz with new high score"
            }
        }
    }

    private init() {
        loadSelectedIcon()
    }

    private func loadSelectedIcon() {
        if let savedIconName = UserDefaults.standard.string(forKey: UserDefaultsKeys.Personalization.selectedAppIcon),
           let icon = AppIcon(rawValue: savedIconName) {
            selectedIcon = icon
        } else {
            // Default to Correct if no saved preference
            selectedIcon = .correct
        }
    }

    func setIcon(_ icon: AppIcon) {
        selectedIcon = icon
        UserDefaults.standard.set(icon.rawValue, forKey: UserDefaultsKeys.Personalization.selectedAppIcon)

        // Change the app icon using UIApplication
        if UIApplication.shared.supportsAlternateIcons {
            UIApplication.shared.setAlternateIconName(icon.iconName) { error in
                if let error = error {
                    print("Error setting alternate icon: \(error.localizedDescription)")
                } else {
                    print("Successfully changed app icon to: \(icon.rawValue)")
                }
            }
        }
    }
}
