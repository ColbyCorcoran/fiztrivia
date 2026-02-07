//
//  QuestionHistoryEntry.swift
//  Fiz
//
//  Extracted from TriviaModels.swift during code review refactor
//

import Foundation
import SwiftData

@Model
final class QuestionHistoryEntry {
    var questionId: String
    var questionText: String
    var correctAnswer: String
    var userAnswer: String
    var wasCorrect: Bool
    var timestamp: Date
    var category: String
    var subcategory: String?
    var topic: String?  // Pack ID for expansion pack questions
    var id: UUID

    init(questionId: String, questionText: String, correctAnswer: String, userAnswer: String, wasCorrect: Bool, category: String, subcategory: String?, topic: String? = nil) {
        self.questionId = questionId
        self.questionText = questionText
        self.correctAnswer = correctAnswer
        self.userAnswer = userAnswer
        self.wasCorrect = wasCorrect
        self.timestamp = Date()
        self.category = category
        self.subcategory = subcategory
        self.topic = topic
        self.id = UUID()
    }
}
