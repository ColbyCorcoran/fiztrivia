//
//  GameEnums.swift
//  Fiz
//
//  Extracted from TriviaModels.swift during code review refactor
//

import Foundation

enum GameState {
    case selectingCategory
    case leaderboard
    case settings
}

enum AnswerState {
    case unanswered
    case correct
    case incorrect
}

enum DifficultyMode: String, CaseIterable {
    case casual = "Casual"
    case normal = "Normal"
    case difficult = "Difficult"

    var description: String {
        switch self {
        case .casual: return "Only easy questions"
        case .normal: return "Mix of all difficulty levels"
        case .difficult: return "Medium and hard questions only"
        }
    }

    func shouldInclude(questionDifficulty: String) -> Bool {
        let difficulty = questionDifficulty.lowercased()
        switch self {
        case .casual: return difficulty == "easy"
        case .normal:
            return true
        case .difficult:
            return difficulty == "medium" || difficulty == "hard"
        }
    }
}

// MARK: - Game Mode Enum
enum GameMode: String, CaseIterable, Codable, Identifiable {
    case multiCategory = "Multi-Category"
    case singleCategory = "Single Category"
    case singleTopic = "Single Topic"

    // PLANNED: Seasonal Mode (Uncomment when implementing)
    // Seasonal mode provides holiday-themed trivia experiences for Christmas, Halloween, Easter, etc.
    // Features to implement:
    // - Special UI themes with seasonal graphics and colors
    // - Time-limited seasonal question packs (auto-enable/disable based on date)
    // - Festive animations and sound effects
    // - Seasonal leaderboards separate from regular gameplay
    // - Holiday-specific completion badges
    //
    // Implementation notes:
    // - Add seasonalTheme property to GameModeManager (key already reserved in UserDefaultsKeys)
    // - Create seasonal question JSON files: seasonal_christmas.json, seasonal_halloween.json, etc.
    // - Add date range logic to auto-activate (e.g., Dec 1-31 for Christmas)
    // - Update CategoryWheelView to apply seasonal theme colors and graphics
    // - Consider IAP for premium seasonal packs vs free base seasonal questions
    //
    // case seasonal = "Seasonal"

    var id: String { rawValue }

    var description: String {
        switch self {
        case .multiCategory:
            return "Mix of all selected categories"
        case .singleCategory:
            return "Focus on one category's subcategories"
        case .singleTopic:
            return "Focus on questions from a specific topic"
        // When implementing seasonal mode, uncomment:
        // case .seasonal:
        //     return "Special themed trivia experience for holidays and seasons"
        }
    }

    var icon: String {
        switch self {
        case .multiCategory:
            return "circle.grid.cross.left.filled"
        case .singleCategory:
            return "circle.grid.cross.up.filled"
        case .singleTopic:
            return "circle.grid.cross.right.filled"
        // When implementing seasonal mode, uncomment:
        // case .seasonal:
        //     return "sparkles" // Or "snowflake" for winter, "leaf.fill" for fall, etc.
        }
    }
}
