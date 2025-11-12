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
        let config = PostHogConfig(apiKey: "phc_pPTqusdmpJSoGYjymsgdz6BX6lcnUfuZzkKGw713JeZ")
        config.host = "https://us.posthog.com"

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
}
