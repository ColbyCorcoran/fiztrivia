//
//  ExpansionPack.swift
//  Fiz
//
//  Extracted from TriviaModels.swift during code review refactor
//

import Foundation

struct ExpansionPack: Codable, Identifiable {
    let id: String  // Same as packId
    let packId: String  // e.g., "com.fiz.pack.harry_potter"
    let packName: String  // "Harry Potter"
    let packDescription: String
    let subtopics: [String]  // ["Characters", "Spells", "Locations", "Books", "Movies", "Trivia"]
    let questionCount: Int
    let freePreviewCount: Int
    let difficulty: DifficultyBreakdown
    let price: Double
    let icon: String  // SF Symbol for pack (e.g., "wand.and.stars")
    let isPublished: Bool  // Whether pack should appear in UI (default: true for backward compatibility)
    let subtopicIcons: [String: String]?  // Optional mapping of subtopic name → SF Symbol icon
    let releaseDate: Date?  // ISO8601 date for "New" badge logic (nil for old packs)
    let freePreviewQuestions: [TriviaQuestion]
    let paidQuestions: [TriviaQuestion]

    var allQuestions: [TriviaQuestion] {
        return freePreviewQuestions + paidQuestions
    }

    /// Returns true if pack was released within the last 3 weeks
    var isNew: Bool {
        guard let releaseDate = releaseDate else { return false }
        let threeWeeksInSeconds: TimeInterval = 21 * 24 * 60 * 60  // 3 weeks
        return Date.now.timeIntervalSince(releaseDate) <= threeWeeksInSeconds
    }

    /// Get icon for a specific subtopic, falling back to pack icon if not specified
    func icon(for subtopic: String) -> String {
        return subtopicIcons?[subtopic] ?? icon
    }

    private enum CodingKeys: String, CodingKey {
        case packId, packName, packDescription, subtopics, questionCount, freePreviewCount, difficulty, price, icon, isPublished, subtopicIcons, releaseDate, freePreviewQuestions, paidQuestions
    }

    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        let packId = try container.decode(String.self, forKey: .packId)
        self.id = packId
        self.packId = packId
        self.packName = try container.decode(String.self, forKey: .packName)
        self.packDescription = try container.decode(String.self, forKey: .packDescription)
        self.subtopics = try container.decode([String].self, forKey: .subtopics)
        self.questionCount = try container.decode(Int.self, forKey: .questionCount)
        self.freePreviewCount = try container.decode(Int.self, forKey: .freePreviewCount)
        self.difficulty = try container.decode(DifficultyBreakdown.self, forKey: .difficulty)
        self.price = try container.decode(Double.self, forKey: .price)
        self.icon = try container.decode(String.self, forKey: .icon)
        // Default to true for backward compatibility with existing packs
        self.isPublished = try container.decodeIfPresent(Bool.self, forKey: .isPublished) ?? true
        // Optional subtopic icons (defaults to nil if not present)
        self.subtopicIcons = try container.decodeIfPresent([String: String].self, forKey: .subtopicIcons)
        // Optional release date for "New" badge logic (defaults to nil if not present)
        self.releaseDate = try container.decodeIfPresent(Date.self, forKey: .releaseDate)
        self.freePreviewQuestions = try container.decode([TriviaQuestion].self, forKey: .freePreviewQuestions)
        self.paidQuestions = try container.decode([TriviaQuestion].self, forKey: .paidQuestions)
    }
}

struct DifficultyBreakdown: Codable {
    let easy: Int
    let medium: Int
    let hard: Int
}
