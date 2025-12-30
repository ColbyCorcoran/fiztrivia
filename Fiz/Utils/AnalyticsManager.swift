import Foundation
import PostHog

// MARK: - Analytics Manager
class AnalyticsManager: ObservableObject {
    private static let analyticsEnabledKey = "analytics_enabled"
    private static let hasShownConsentKey = "analytics_consent_shown"

    @Published var isAnalyticsEnabled: Bool = false
    @Published var hasShownConsent: Bool = false

    static let shared = AnalyticsManager()

    private init() {
        loadSettings()
        configurePostHog()
    }

    private func loadSettings() {
        hasShownConsent = UserDefaults.standard.bool(forKey: Self.hasShownConsentKey)
        isAnalyticsEnabled = UserDefaults.standard.bool(forKey: Self.analyticsEnabledKey)
    }

    private func configurePostHog() {
        let config = PostHogConfig(
            apiKey: "phc_pPTqusdmpJSoGYjymsgdz6BX6lcnUfuZzkKGw713JeZ",
            host: "https://us.posthog.com"
        )

        // Privacy-focused configuration
        config.captureApplicationLifecycleEvents = false  // We'll track these manually
        config.captureScreenViews = false  // Don't auto-capture screens

        PostHogSDK.shared.setup(config)

        // Opt out by default until user enables
        if !isAnalyticsEnabled {
            PostHogSDK.shared.optOut()
        }
    }

    func setAnalyticsEnabled(_ enabled: Bool) {
        isAnalyticsEnabled = enabled
        UserDefaults.standard.set(enabled, forKey: Self.analyticsEnabledKey)

        if enabled {
            PostHogSDK.shared.optIn()
        } else {
            PostHogSDK.shared.optOut()
            PostHogSDK.shared.reset()  // Clear any stored data
        }
    }

    func markConsentShown() {
        hasShownConsent = true
        UserDefaults.standard.set(true, forKey: Self.hasShownConsentKey)
    }

    // MARK: - Event Tracking

    func trackAppOpened() {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("app_opened")
    }

    func trackAppBackgrounded() {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("app_backgrounded")
    }

    func trackSettingChanged(setting: String, value: String) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("setting_changed", properties: [
            "setting": setting,
            "value": value
        ])
    }

    func trackCategoryCompleted(category: String, difficultyMode: String, questionsAnswered: Int) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("category_completed", properties: [
            "category": category,
            "difficulty_mode": difficultyMode,
            "questions_answered": questionsAnswered
        ])
    }

    func trackSingleCategoryModeEnabled(category: String) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("single_category_mode_enabled", properties: [
            "category": category
        ])
    }

    func trackSingleCategoryModeDisabled() {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("single_category_mode_disabled")
    }

    // MARK: - Onboarding Events

    func trackOnboardingCompleted(hasUsername: Bool) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("onboarding_completed", properties: [
            "has_username": hasUsername
        ])
    }

    func trackOnboardingSkipped() {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("onboarding_skipped")
    }

    // MARK: - Secondary Onboarding Events

    func trackSecondaryOnboardingViewed() {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("secondary_onboarding_viewed")
    }

    func trackSecondaryOnboardingPageViewed(page: Int) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("secondary_onboarding_page_viewed", properties: [
            "page": page
        ])
    }

    func trackSecondaryOnboardingCompleted() {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("secondary_onboarding_completed")
    }

    func trackSecondaryOnboardingSkipped(atPage page: Int) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("secondary_onboarding_skipped", properties: [
            "page": page
        ])
    }

    func trackSecondaryOnboardingDismissed(atPage page: Int) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("secondary_onboarding_dismissed_permanently", properties: [
            "page": page
        ])
    }

    func trackFeatureTourManuallyOpened() {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("feature_tour_manually_opened")
    }

    // MARK: - Personalization Events

    func trackUsernameUpdated(hadPreviousUsername: Bool) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("username_updated", properties: [
            "had_previous_username": hadPreviousUsername
        ])
    }

    func trackAppIconChanged(iconName: String) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("app_icon_changed", properties: [
            "icon_name": iconName
        ])
    }

    // MARK: - Phobia Filter Events (Privacy-Safe - NO terms or exclusion counts)

    func trackPhobiaFilterAdded(totalFilterCount: Int) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("phobia_filter_added", properties: [
            "total_filter_count": totalFilterCount
        ])
    }

    func trackPhobiaFilterRemoved(remainingFilterCount: Int) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("phobia_filter_removed", properties: [
            "remaining_filter_count": remainingFilterCount
        ])
    }

    func trackPhobiaFiltersClearedAll(filterCountCleared: Int) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("phobia_filters_cleared_all", properties: [
            "filter_count_cleared": filterCountCleared
        ])
    }

    // MARK: - Interaction Settings Events

    func trackHapticFeedbackToggled(enabled: Bool) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("haptic_feedback_toggled", properties: [
            "enabled": enabled
        ])
    }

    func trackSwipeNavigationToggled(enabled: Bool) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("swipe_navigation_toggled", properties: [
            "enabled": enabled
        ])
    }

    func trackSwipeGestureUsageSummary(totalSwipes: Int, leftCount: Int, rightCount: Int) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("swipe_gesture_used", properties: [
            "total_swipes_since_enable": totalSwipes,
            "left_count": leftCount,
            "right_count": rightCount
        ])
    }

    // MARK: - Popup Duration Events

    func trackPopupDurationChanged(popupType: String, duration: Double, isCustom: Bool) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("popup_duration_changed", properties: [
            "popup_type": popupType,
            "duration": duration,
            "is_custom": isCustom
        ])
    }

    // MARK: - Analytics Consent Events

    func trackAnalyticsEnabled() {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("analytics_enabled")
    }

    func trackAnalyticsDisabled() {
        // Special case: track before disabling, then analytics will be disabled
        if isAnalyticsEnabled {
            PostHogSDK.shared.capture("analytics_disabled")
        }
    }

    // MARK: - Category Selection Events

    func trackCategorySelectionChanged(selectedCategories: [String], totalCount: Int) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("category_selection_changed", properties: [
            "selected_categories": selectedCategories,
            "total_count": totalCount
        ])
    }

    func trackCategorySelectionReset() {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("category_selection_reset")
    }

    // MARK: - Game Mode Events

    func trackStreakSaveDecision(action: String, streakValue: Int) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("streak_save_decision", properties: [
            "action": action,
            "streak_value": streakValue
        ])
    }

    // MARK: - Progress Events

    func trackProgressResetConfirmed(totalQuestionsCleared: Int) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("progress_reset_confirmed", properties: [
            "total_questions_cleared": totalQuestionsCleared
        ])
    }

    // MARK: - Milestone Events (Low Frequency)

    func trackStreakMilestoneReached(streakValue: Int) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("streak_milestone_reached", properties: [
            "streak_value": streakValue
        ])
    }

    func trackStreakSavedToLeaderboard(streakValue: Int, gameMode: String, category: String?) {
        guard isAnalyticsEnabled else { return }
        var properties: [String: Any] = [
            "streak_value": streakValue,
            "game_mode": gameMode
        ]
        if let category = category {
            properties["category"] = category
        }
        PostHogSDK.shared.capture("streak_saved_to_leaderboard", properties: properties)
    }
}
