//
//  UserDefaultsKeys.swift
//  Fiz
//
//  Created by Claude Code on Code Review
//

import Foundation

/// Centralized UserDefaults keys to prevent typos and key collisions
/// All UserDefaults keys used throughout the app are defined here
enum UserDefaultsKeys {

    // MARK: - User Management
    enum User {
        static let username = "user_name"
        static let hasCompletedOnboarding = "has_completed_onboarding"
    }

    // MARK: - Game State
    enum Game {
        static let currentStreak = "current_streak"
        static let selectedDifficulty = "selected_difficulty_mode"
        static let answeredQuestions = "answered_questions"
    }

    // MARK: - Game Modes
    enum GameMode {
        static let selectedMode = "selected_game_mode"
        static let selectedCategory = "game_mode_selected_category"
        static let selectedTopic = "game_mode_selected_topic"
        // Future: static let seasonalTheme = "game_mode_seasonal_theme"
    }

    // MARK: - Category Selection
    enum Categories {
        static let selectedCategories = "selected_categories"
        static let customDefaultCategories = "custom_default_categories"
    }

    // MARK: - Expansion Packs & Store
    enum Store {
        static let purchasedPacks = "purchased_expansion_packs"
        static let installedPacks = "installed_expansion_packs"
    }

    // MARK: - Settings & Preferences
    enum Settings {
        static let hapticEnabled = "haptic_feedback_enabled"
        static let swipeNavigationEnabled = "swipe_navigation_enabled"
        static let correctPopupDuration = "correct_popup_duration"
        static let incorrectPopupDuration = "incorrect_popup_duration"
    }

    // MARK: - Personalization
    enum Personalization {
        static let selectedAppIcon = "selected_app_icon"
    }

    // MARK: - Phobia Filters
    enum Phobia {
        static let phobias = "user_phobias"
    }

    // MARK: - Analytics
    enum Analytics {
        static let enabled = "analytics_enabled"
        static let consentShown = "analytics_consent_shown"
    }

    // MARK: - Onboarding
    enum Onboarding {
        static let launchCount = "app_launch_count"
        static let firstLaunchDate = "first_launch_date"
        static let hasSeenSecondaryOnboarding = "has_seen_secondary_onboarding"
        static let onboardingDismissedPermanently = "onboarding_dismissed_permanently"
    }

    // MARK: - What's New
    enum WhatsNew {
        static let lastSeenVersion = "last_seen_app_version"
    }

    // MARK: - Developer Tools
    enum Developer {
        static let bypassEnabled = "developer_bypass_enabled"
    }

    // MARK: - Validation

    /// Validates that all keys are unique (run in debug builds)
    static func validateUniqueKeys() {
        let allKeys = [
            User.username, User.hasCompletedOnboarding,
            Game.currentStreak, Game.selectedDifficulty, Game.answeredQuestions,
            GameMode.selectedMode, GameMode.selectedCategory, GameMode.selectedTopic,
            Categories.selectedCategories, Categories.customDefaultCategories,
            Store.purchasedPacks, Store.installedPacks,
            Settings.hapticEnabled, Settings.swipeNavigationEnabled,
            Settings.correctPopupDuration, Settings.incorrectPopupDuration,
            Personalization.selectedAppIcon,
            Phobia.phobias,
            Analytics.enabled, Analytics.consentShown,
            Onboarding.launchCount, Onboarding.firstLaunchDate,
            Onboarding.hasSeenSecondaryOnboarding, Onboarding.onboardingDismissedPermanently,
            WhatsNew.lastSeenVersion,
            Developer.bypassEnabled
        ]

        let uniqueKeys = Set(allKeys)
        assert(allKeys.count == uniqueKeys.count, "⚠️ Duplicate UserDefaults keys detected!")

        #if DEBUG
        if allKeys.count != uniqueKeys.count {
            print("⚠️ CRITICAL: Duplicate UserDefaults keys found!")
            let duplicates = allKeys.filter { key in
                allKeys.filter({ $0 == key }).count > 1
            }
            print("Duplicates: \(Set(duplicates))")
        } else {
            print("✅ All UserDefaults keys are unique (\(allKeys.count) keys)")
        }
        #endif
    }
}
