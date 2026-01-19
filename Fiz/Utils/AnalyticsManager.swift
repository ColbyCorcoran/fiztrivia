import Foundation
import PostHog

// MARK: - Analytics Manager
class AnalyticsManager: ObservableObject {
    private static let analyticsEnabledKey = "analytics_enabled"
    private static let hasShownConsentKey = "analytics_consent_shown"

    @Published var isAnalyticsEnabled: Bool = true
    @Published var hasShownConsent: Bool = false

    static let shared = AnalyticsManager()

    private init() {
        loadSettings()
        configurePostHog()
    }

    private func loadSettings() {
        hasShownConsent = UserDefaults.standard.bool(forKey: Self.hasShownConsentKey)

        // Opt-in by default - if key doesn't exist (first launch), enable analytics
        if let savedValue = UserDefaults.standard.object(forKey: Self.analyticsEnabledKey) as? Bool {
            isAnalyticsEnabled = savedValue
        } else {
            isAnalyticsEnabled = true  // Default to enabled for new users
        }
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

        // Apply user's analytics preference
        if !isAnalyticsEnabled {
            PostHogSDK.shared.optOut()
        } else {
            PostHogSDK.shared.optIn()
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

    // MARK: - What's New Events

    func trackWhatsNewViewed(version: String) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("whats_new_viewed", properties: [
            "version": version
        ])
    }

    func trackWhatsNewCompleted(version: String) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("whats_new_completed", properties: [
            "version": version
        ])
    }

    func trackWhatsNewDismissed(version: String) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("whats_new_dismissed", properties: [
            "version": version
        ])
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

    func trackGameModeChanged(newMode: String, previousMode: String?) {
        guard isAnalyticsEnabled else { return }
        var properties: [String: Any] = ["new_mode": newMode]
        if let previousMode = previousMode {
            properties["previous_mode"] = previousMode
        }
        PostHogSDK.shared.capture("game_mode_changed", properties: properties)
    }

    func trackStreakSaveDecision(action: String, streakValue: Int) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("streak_save_decision", properties: [
            "action": action,
            "streak_value": streakValue
        ])
    }

    // MARK: - Gameplay Events

    func trackQuestionAnswered(isCorrect: Bool, category: String, difficulty: String, gameMode: String) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("question_answered", properties: [
            "is_correct": isCorrect,
            "category": category,
            "difficulty": difficulty,
            "game_mode": gameMode
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

    // MARK: - Expansion Pack Events

    func trackStoreViewed() {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("store_viewed")
    }

    func trackStoreDismissed(hadItemsInCart: Bool, cartItemCount: Int) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("store_dismissed", properties: [
            "had_items_in_cart": hadItemsInCart,
            "cart_item_count": cartItemCount
        ])
    }

    func trackExpansionPackViewed(packId: String, packName: String) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("expansion_pack_viewed", properties: [
            "pack_id": packId,
            "pack_name": packName
        ])
    }

    func trackExpansionPackPurchased(packId: String) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("expansion_pack_purchased", properties: [
            "pack_id": packId
        ])
    }

    func trackExpansionPackInstalled(packId: String) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("expansion_pack_installed", properties: [
            "pack_id": packId
        ])
    }

    func trackExpansionPackUninstalled(packId: String) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("expansion_pack_uninstalled", properties: [
            "pack_id": packId
        ])
    }

    func trackPurchasesRestored(packsRestored: Int) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("purchases_restored", properties: [
            "packs_restored": packsRestored
        ])
    }

    // MARK: - Cart Events

    func trackCartViewed(itemCount: Int) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("cart_viewed", properties: [
            "item_count": itemCount
        ])
    }

    func trackPackAddedToCart(packId: String, packName: String) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("pack_added_to_cart", properties: [
            "pack_id": packId,
            "pack_name": packName
        ])
    }

    func trackPackRemovedFromCart(packId: String, packName: String, totalItemsRemaining: Int) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("pack_removed_from_cart", properties: [
            "pack_id": packId,
            "pack_name": packName,
            "total_items_remaining": totalItemsRemaining
        ])
    }

    func trackCartCleared(itemsCleared: Int) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("cart_cleared", properties: [
            "items_cleared": itemsCleared
        ])
    }

    func trackCheckoutInitiated(itemCount: Int, subtotal: Double, hasDiscount: Bool) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("checkout_initiated", properties: [
            "item_count": itemCount,
            "subtotal": subtotal,
            "has_discount": hasDiscount
        ])
    }

    func trackCheckoutCompleted(itemCount: Int, total: Double, hadDiscount: Bool) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("checkout_completed", properties: [
            "item_count": itemCount,
            "total": total,
            "had_discount": hadDiscount
        ])
    }

    func trackCheckoutFailed(itemCount: Int, failureReason: String) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("checkout_failed", properties: [
            "item_count": itemCount,
            "failure_reason": failureReason
        ])
    }

    func trackDiscountCodeApplied(codeType: String, discountAmount: Double) {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("discount_code_applied", properties: [
            "code_type": codeType,
            "discount_amount": discountAmount
        ])
    }

    func trackDiscountCodeRemoved() {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("discount_code_removed")
    }

    func trackDiscountCodeInvalid() {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("discount_code_invalid")
    }

    // MARK: - Support & Legal Tracking

    func trackFeatureRequestsOpened() {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("feature_requests_opened")
    }

    func trackTermsOfServiceViewed() {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("terms_of_service_viewed")
    }

    func trackContactSupportOpened() {
        guard isAnalyticsEnabled else { return }
        PostHogSDK.shared.capture("contact_support_opened")
    }
}
