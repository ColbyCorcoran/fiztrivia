//
//  CategorySelectionManager.swift
//  Fiz
//
//  Extracted from TriviaModels.swift
//

import Foundation

/// Manages multi-category selection for Multi-Category game mode (2-12 categories)
class CategorySelectionManager: ObservableObject {
    private static let selectedCategoriesKey = "selected_categories"
    private static let customDefaultCategoriesKey = "custom_default_categories"

    @Published var selectedCategories: Set<TriviaCategory> = []

    static let shared = CategorySelectionManager()
    static let minimumCategories = 2
    static let maximumCategories = 12

    private init() {
        loadSettings()
    }

    private func loadSettings() {
        if let data = UserDefaults.standard.data(forKey: UserDefaultsKeys.Categories.selectedCategories),
           let decodedStrings = try? JSONDecoder().decode(Set<String>.self, from: data) {
            selectedCategories = Set(decodedStrings.compactMap { TriviaCategory(rawValue: $0) })

            // Validate count - reset if invalid
            if selectedCategories.count < Self.minimumCategories || selectedCategories.isEmpty {
                setDefaultSelection()
            }
        } else {
            setDefaultSelection()
        }
    }

    private func saveSettings() {
        let categoryStrings = Set(selectedCategories.map { $0.rawValue })
        if let encoded = try? JSONEncoder().encode(categoryStrings) {
            UserDefaults.standard.set(encoded, forKey: UserDefaultsKeys.Categories.selectedCategories)
        }
    }

    func toggleCategory(_ category: TriviaCategory) -> Bool {
        if selectedCategories.contains(category) {
            // Deselecting - check minimum
            if selectedCategories.count > Self.minimumCategories {
                // Check if this is the active single-category mode category
                if GameModeManager.shared.isSingleCategoryMode &&
                   GameModeManager.shared.selectedCategory == category {
                    return false // Cannot deselect active category
                }

                selectedCategories.remove(category)
                saveSettings()
                return true
            } else {
                return false // Cannot go below minimum
            }
        } else {
            // Selecting - check maximum
            if selectedCategories.count < Self.maximumCategories {
                selectedCategories.insert(category)
                saveSettings()
                return true
            } else {
                return false // At maximum
            }
        }
    }

    func isSelected(_ category: TriviaCategory) -> Bool {
        return selectedCategories.contains(category)
    }

    func canToggle(_ category: TriviaCategory) -> Bool {
        if selectedCategories.contains(category) {
            return selectedCategories.count > Self.minimumCategories
        } else {
            return selectedCategories.count < Self.maximumCategories
        }
    }

    // MARK: - Factory Default
    private var factoryDefault: Set<TriviaCategory> {
        // Factory default: All 12 categories enabled
        return [
            .entertainment,
            .sports,
            .bible,
            .history,
            .science,
            .nature,
            .food,
            .music,
            .technology,
            .art,
            .geography,
            .literature
        ]
    }

    private func setDefaultSelection() {
        selectedCategories = factoryDefault
        saveSettings()
    }

    // MARK: - Custom Default Management

    /// Check if user has saved a custom default
    func hasCustomDefault() -> Bool {
        return UserDefaults.standard.data(forKey: UserDefaultsKeys.Categories.customDefaultCategories) != nil
    }

    /// Save current selection as user's custom default
    func saveCurrentAsDefault() {
        let categoryStrings = Set(selectedCategories.map { $0.rawValue })
        if let encoded = try? JSONEncoder().encode(categoryStrings) {
            UserDefaults.standard.set(encoded, forKey: UserDefaultsKeys.Categories.customDefaultCategories)
        }
    }

    /// Save current selection as default only if it differs from factory default
    /// Used for onboarding flow
    func saveCurrentAsDefaultIfDifferent() {
        if selectedCategories != factoryDefault {
            saveCurrentAsDefault()
        }
    }

    /// Reset to user's custom default (or factory default if no custom saved)
    func resetToMyDefault() {
        if let data = UserDefaults.standard.data(forKey: UserDefaultsKeys.Categories.customDefaultCategories),
           let decodedStrings = try? JSONDecoder().decode(Set<String>.self, from: data) {
            selectedCategories = Set(decodedStrings.compactMap { TriviaCategory(rawValue: $0) })

            // Validate count - fall back to factory if invalid
            if selectedCategories.count < Self.minimumCategories || selectedCategories.isEmpty {
                setDefaultSelection()
            } else {
                saveSettings()
            }
        } else {
            // No custom default - fall back to factory
            setDefaultSelection()
        }
    }

    /// Reset to factory default (all 12 categories)
    func resetToFactoryDefault() {
        setDefaultSelection()
    }

    /// Legacy method - now resets to user's custom default
    func resetToDefault() {
        resetToMyDefault()
    }
}
