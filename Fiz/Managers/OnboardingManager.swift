//
//  OnboardingManager.swift
//  Fiz
//
//  Extracted from TriviaModels.swift
//

import Foundation

/// Manages onboarding state, launch count, and secondary onboarding triggers
class OnboardingManager: ObservableObject {
    private static let launchCountKey = "app_launch_count"
    private static let firstLaunchDateKey = "first_launch_date"
    private static let hasSeenSecondaryOnboardingKey = "has_seen_secondary_onboarding"
    private static let onboardingDismissedKey = "onboarding_dismissed_permanently"

    @Published var launchCount: Int = 0
    @Published var shouldShowSecondaryOnboarding: Bool = false

    static let shared = OnboardingManager()

    // Trigger thresholds
    static let launchThreshold = 15  // Show after 15 launches
    static let dayThreshold = 5      // OR after 5 days

    private init() {
        loadSettings()
    }

    private func loadSettings() {
        // Load launch count
        launchCount = UserDefaults.standard.integer(forKey: UserDefaultsKeys.Onboarding.launchCount)

        // Set first launch date if not set
        if UserDefaults.standard.object(forKey: UserDefaultsKeys.Onboarding.firstLaunchDate) == nil {
            UserDefaults.standard.set(Date(), forKey: UserDefaultsKeys.Onboarding.firstLaunchDate)
        }

        // Check if should show secondary onboarding
        updateSecondaryOnboardingStatus()
    }

    func incrementLaunchCount() {
        launchCount += 1
        UserDefaults.standard.set(launchCount, forKey: UserDefaultsKeys.Onboarding.launchCount)
        updateSecondaryOnboardingStatus()
    }

    private func updateSecondaryOnboardingStatus() {
        // Don't show if already seen (ONE TIME EVER)
        let hasSeenOnboarding = UserDefaults.standard.bool(forKey: UserDefaultsKeys.Onboarding.hasSeenSecondaryOnboarding)

        // Don't show if permanently dismissed
        let isPermanentlyDismissed = UserDefaults.standard.bool(forKey: UserDefaultsKeys.Onboarding.onboardingDismissedPermanently)

        if hasSeenOnboarding || isPermanentlyDismissed {
            shouldShowSecondaryOnboarding = false
            return
        }

        // Check launch threshold
        if launchCount >= Self.launchThreshold {
            shouldShowSecondaryOnboarding = true
            return
        }

        // Check day threshold
        if let firstLaunchDate = UserDefaults.standard.object(forKey: UserDefaultsKeys.Onboarding.firstLaunchDate) as? Date {
            let daysSinceFirstLaunch = Calendar.current.dateComponents([.day], from: firstLaunchDate, to: Date()).day ?? 0
            if daysSinceFirstLaunch >= Self.dayThreshold {
                shouldShowSecondaryOnboarding = true
                return
            }
        }

        shouldShowSecondaryOnboarding = false
    }

    func markSecondaryOnboardingAsShown() {
        UserDefaults.standard.set(true, forKey: UserDefaultsKeys.Onboarding.hasSeenSecondaryOnboarding)
        shouldShowSecondaryOnboarding = false
    }

    func dismissSecondaryOnboardingPermanently() {
        UserDefaults.standard.set(true, forKey: UserDefaultsKeys.Onboarding.onboardingDismissedPermanently)
        shouldShowSecondaryOnboarding = false
    }

    func forceShowSecondaryOnboarding() {
        // For testing or "Feature Tour" button
        shouldShowSecondaryOnboarding = true
    }

    func resetOnboardingForTesting() {
        // Debugging/testing method
        UserDefaults.standard.removeObject(forKey: UserDefaultsKeys.Onboarding.launchCount)
        UserDefaults.standard.removeObject(forKey: UserDefaultsKeys.Onboarding.firstLaunchDate)
        UserDefaults.standard.removeObject(forKey: UserDefaultsKeys.Onboarding.hasSeenSecondaryOnboarding)
        UserDefaults.standard.removeObject(forKey: UserDefaultsKeys.Onboarding.onboardingDismissedPermanently)
        launchCount = 0
        shouldShowSecondaryOnboarding = false
        loadSettings()
    }

    // Debug info
    func getDebugInfo() -> String {
        let firstLaunchDate = UserDefaults.standard.object(forKey: UserDefaultsKeys.Onboarding.firstLaunchDate) as? Date ?? Date()
        let daysSinceFirstLaunch = Calendar.current.dateComponents([.day], from: firstLaunchDate, to: Date()).day ?? 0
        let hasSeenOnboarding = UserDefaults.standard.bool(forKey: UserDefaultsKeys.Onboarding.hasSeenSecondaryOnboarding)
        let isDismissed = UserDefaults.standard.bool(forKey: UserDefaultsKeys.Onboarding.onboardingDismissedPermanently)

        return """
        Launch Count: \(launchCount)/\(Self.launchThreshold)
        Days Since Install: \(daysSinceFirstLaunch)/\(Self.dayThreshold)
        Has Seen Onboarding: \(hasSeenOnboarding)
        Is Dismissed: \(isDismissed)
        Should Show: \(shouldShowSecondaryOnboarding)
        """
    }
}
