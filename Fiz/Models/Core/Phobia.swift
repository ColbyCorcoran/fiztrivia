//
//  Phobia.swift
//  Fiz
//
//  Extracted from TriviaModels.swift during code review refactor
//

import Foundation

struct Phobia: Codable, Identifiable, Equatable {
    let id: String
    let term: String                      // User-entered phobia term (e.g., "snakes")
    var excludedQuestionIds: Set<String>  // IDs of questions to exclude
    let dateAdded: Date

    init(term: String, excludedQuestionIds: Set<String> = []) {
        self.id = UUID().uuidString
        self.term = term
        self.excludedQuestionIds = excludedQuestionIds
        self.dateAdded = Date()
    }
}
