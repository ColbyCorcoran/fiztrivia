//
//  TriviaCategory.swift
//  Fiz
//
//  Extracted from TriviaModels.swift during code review refactor
//

import Foundation

enum TriviaCategory: String, CaseIterable {
    case entertainment = "Entertainment"
    case sports = "Sports"
    case music = "Music"
    case technology = "Technology"
    case art = "Art"
    case geography = "Geography"
    case science = "Science"
    case literature = "Literature"
    case nature = "Nature"
    case history = "History"
    case bible = "Bible"
    case food = "Food"

    var icon: String {
        switch self {
        case .entertainment: return "movieclapper.fill"
        case .sports: return "tennisball.fill"
        case .music: return "music.note"
        case .technology: return "laptopcomputer"
        case .art: return "paintpalette.fill"
        case .geography: return "map.fill"
        case .science: return "atom"
        case .literature: return "book.fill"
        case .nature: return "leaf.fill"
        case .history: return "building.columns.fill"
        case .bible: return "text.book.closed.fill"
        case .food: return "fork.knife.circle.fill"
        }
    }

    var color: String {
        switch self {
        case .entertainment: return "#F7B500"  // Gold (LOCKED)
        case .sports:        return "#FF7F0F"  // Orange (LOCKED)
        case .music:         return "#2ECC71"  // Green
        case .technology:    return "#3498DB"  // Blue
        case .art:           return "#8E44AD"  // Purple
        case .geography:     return "#E91E63"  // Red
        case .science:       return "#F7B500"  // Gold
        case .literature:    return "#FF7F0F"  // Orange
        case .nature:        return "#2ECC71"  // Green (LOCKED)
        case .history:       return "#3498DB"  // Blue (LOCKED)
        case .bible:         return "#8E44AD"  // Purple (LOCKED)
        case .food:          return "#E91E63"  // Red (LOCKED)
        }
    }

    // Helper to identify locked categories (never change color)
    var isColorLocked: Bool {
        switch self {
        case .entertainment, .sports, .bible, .history, .nature, .food:
            return true
        case .literature, .music, .technology, .art, .geography, .science:
            return false
        }
    }

    var subcategories: [String] {
        // This will be populated dynamically from the question database
        return []
    }
}
