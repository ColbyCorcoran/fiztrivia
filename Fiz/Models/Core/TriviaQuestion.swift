//
//  TriviaQuestion.swift
//  Fiz
//
//  Extracted from TriviaModels.swift during code review refactor
//

import Foundation

struct TriviaQuestion: Codable, Identifiable {
    let id: String
    let category: String
    let subcategory: String?
    let topic: String?
    let subtopic: String?
    let question: String
    let options: [String]
    let correctAnswer: String
    let difficulty: String

    init(id: String? = nil, category: String, subcategory: String?, topic: String? = nil, subtopic: String? = nil, question: String, options: [String], correctAnswer: String, difficulty: String) {
        self.id = id ?? UUID().uuidString
        self.category = category
        self.subcategory = subcategory
        self.topic = topic
        self.subtopic = subtopic
        self.question = question
        self.options = options
        self.correctAnswer = correctAnswer
        self.difficulty = difficulty
    }

    private enum CodingKeys: String, CodingKey {
        case id, category, subcategory, topic, subtopic, question, options
        case correctAnswer = "correct_answer"
        case difficulty
    }
}
