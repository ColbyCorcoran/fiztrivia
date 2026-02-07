//
//  LeaderboardEntry.swift
//  Fiz
//
//  Extracted from TriviaModels.swift during code review refactor
//

import Foundation
import SwiftData

@Model
final class LeaderboardEntry {
    var streak: Int
    var date: Date
    var id: UUID
    var gameMode: String = "Multi-Category" // "Multi-Category", "Single Category", or "Single Topic"
    var categoryName: String? = nil // Category name if in Single Category/Topic mode

    init(streak: Int, date: Date, gameMode: String = "Multi-Category", categoryName: String? = nil) {
        self.streak = streak
        self.date = date
        self.id = UUID()
        self.gameMode = gameMode
        self.categoryName = categoryName
    }
}
