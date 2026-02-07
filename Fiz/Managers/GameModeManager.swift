import Foundation
import SwiftUI

// MARK: - Game Mode Manager
class GameModeManager: ObservableObject {
    private static let selectedModeKey = "selected_game_mode"
    private static let selectedCategoryKey = "game_mode_selected_category"
    private static let selectedTopicKey = "game_mode_selected_topic"
    // Future keys ready:
    // private static let seasonalThemeKey = "game_mode_seasonal_theme"

    @Published var selectedMode: GameMode = .multiCategory

    // Mode-specific settings
    @Published var selectedCategory: TriviaCategory? = nil
    @Published var selectedTopic: String? = nil // Topic packId (e.g., "com.fiz.pack.harry_potter")
    // Future settings ready:
    // @Published var seasonalTheme: String? = nil

    static let shared = GameModeManager()

    private init() {
        migrateFromLegacyStorage()
        loadSettings()
        validateAndFixInvalidState()
    }

    // MARK: - Migration

    private func migrateFromLegacyStorage() {
        let legacyModeKey = "single_category_mode_enabled"
        let legacyCategoryKey = "single_category_mode_selected_category"

        if UserDefaults.standard.object(forKey: legacyModeKey) != nil {
            let wasEnabled = UserDefaults.standard.bool(forKey: legacyModeKey)

            if wasEnabled {
                // Migrate to new system
                UserDefaults.standard.set(GameMode.singleCategory.rawValue, forKey: UserDefaultsKeys.GameMode.selectedMode)

                // Migrate category selection
                if let categoryString = UserDefaults.standard.string(forKey: legacyCategoryKey) {
                    UserDefaults.standard.set(categoryString, forKey: UserDefaultsKeys.GameMode.selectedCategory)
                }
            } else {
                UserDefaults.standard.set(GameMode.multiCategory.rawValue, forKey: UserDefaultsKeys.GameMode.selectedMode)
            }

            // Clean up legacy keys
            UserDefaults.standard.removeObject(forKey: legacyModeKey)
            UserDefaults.standard.removeObject(forKey: legacyCategoryKey)

            print("Migrated from SingleCategoryModeManager to GameModeManager")
        }
    }

    // MARK: - Persistence

    private func loadSettings() {
        // Load selected mode
        if let modeString = UserDefaults.standard.string(forKey: UserDefaultsKeys.GameMode.selectedMode),
           let mode = GameMode(rawValue: modeString) {
            selectedMode = mode
        }

        // Load mode-specific settings
        if let categoryString = UserDefaults.standard.string(forKey: UserDefaultsKeys.GameMode.selectedCategory),
           let category = TriviaCategory(rawValue: categoryString) {
            selectedCategory = category
        }

        if let topicString = UserDefaults.standard.string(forKey: UserDefaultsKeys.GameMode.selectedTopic) {
            selectedTopic = topicString
        }
    }

    private func saveSettings() {
        UserDefaults.standard.set(selectedMode.rawValue, forKey: UserDefaultsKeys.GameMode.selectedMode)

        if let category = selectedCategory {
            UserDefaults.standard.set(category.rawValue, forKey: UserDefaultsKeys.GameMode.selectedCategory)
        } else {
            UserDefaults.standard.removeObject(forKey: UserDefaultsKeys.GameMode.selectedCategory)
        }

        if let topic = selectedTopic {
            UserDefaults.standard.set(topic, forKey: UserDefaultsKeys.GameMode.selectedTopic)
        } else {
            UserDefaults.standard.removeObject(forKey: UserDefaultsKeys.GameMode.selectedTopic)
        }
    }

    // MARK: - Validation

    private func validateAndFixInvalidState() {
        var isValid = true

        switch selectedMode {
        case .multiCategory:
            // Multi-Category mode is always valid
            isValid = true
        case .singleCategory:
            // Single Category requires a selected category
            if selectedCategory == nil {
                isValid = false
                print("⚠️ Invalid state detected: Single Category mode without category selection")
            }
        case .singleTopic:
            // Single Topic requires a selected topic
            guard let topicId = selectedTopic else {
                isValid = false
                print("⚠️ Invalid state detected: Single Topic mode without topic selection")
                break
            }

            // Verify the topic is still available (installed OR has previews)
            if !ExpansionPackManager.shared.isAvailableForSingleTopicMode(packId: topicId) {
                isValid = false
                print("⚠️ Invalid state detected: Selected topic is not available")
            }
        // Future modes:
        // case .seasonal:
        //     // Seasonal mode might always be valid
        //     isValid = true
        }

        // If invalid, reset to Multi-Category mode
        if !isValid {
            print("🔄 Resetting to Multi-Category mode due to invalid state")
            selectedMode = .multiCategory
            selectedCategory = nil
            selectedTopic = nil
            saveSettings()
        }
    }

    // MARK: - Public Methods

    func setMode(_ mode: GameMode) {
        selectedMode = mode

        // Clear settings for other modes when switching
        if mode != .singleCategory {
            selectedCategory = nil
        }
        if mode != .singleTopic {
            selectedTopic = nil
        }

        saveSettings()
    }

    func setSelectedCategory(_ category: TriviaCategory?) {
        selectedCategory = category
        saveSettings()
    }

    func setSelectedTopic(_ topicPackId: String?) {
        selectedTopic = topicPackId
        saveSettings()
    }

    // MARK: - Computed Properties for Compatibility

    // For backward compatibility with existing code
    var isMultiCategoryMode: Bool {
        return selectedMode == .multiCategory
    }

    var isSingleCategoryMode: Bool {
        return selectedMode == .singleCategory
    }

    var isSingleTopicMode: Bool {
        return selectedMode == .singleTopic
    }

    // MARK: - Wheel Segment Logic

    func getSubtopicsForSelectedTopic() -> [String] {
        guard selectedMode == .singleTopic,
              let topicPackId = selectedTopic else {
            return []
        }

        // Get the expansion pack for this topic
        if let pack = ExpansionPackManager.shared.availablePacks.first(where: { $0.packId == topicPackId }) {
            return pack.subtopics
        }

        return []
    }

    func getSubcategoriesForSelectedCategory(from questions: [TriviaQuestion],
                                            difficultyMode: DifficultyMode)
        -> [any TriviaSubcategory] {
        guard selectedMode == .singleCategory,
              let category = selectedCategory else {
            return []
        }

        // Get all unique subcategories from the question database for this category
        let subcategoryNames = Set(questions.filter { $0.category == category.rawValue }.compactMap { $0.subcategory })

        // Map to subcategory objects with icon and color
        var subcategories: [any TriviaSubcategory] = []

        switch category {
        case .entertainment:
            subcategories = EntertainmentSubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .literature:
            subcategories = LiteratureSubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .music:
            subcategories = MusicSubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .technology:
            subcategories = TechnologySubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .art:
            subcategories = ArtSubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .geography:
            subcategories = GeographySubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .sports:
            subcategories = SportsSubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .science:
            subcategories = ScienceSubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .nature:
            subcategories = NatureSubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .history:
            subcategories = HistorySubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .bible:
            subcategories = BibleSubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .food:
            subcategories = FoodSubcategory.all.filter { subcategoryNames.contains($0.name) }
        }

        return subcategories
    }

    func hasQuestionsRemaining(for subcategory: String,
                              in questions: [TriviaQuestion],
                              difficultyMode: DifficultyMode,
                              answeredManager: AnsweredQuestionsManager) -> Bool {
        let subcategoryQuestions = questions.filter { question in
            question.subcategory == subcategory &&
            difficultyMode.shouldInclude(questionDifficulty: question.difficulty) &&
            !answeredManager.isQuestionAnswered(question.id)
        }

        return !subcategoryQuestions.isEmpty
    }
}
