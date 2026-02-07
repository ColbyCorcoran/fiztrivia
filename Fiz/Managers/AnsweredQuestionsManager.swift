import Foundation
import Combine

// MARK: - Answered Questions Manager
class AnsweredQuestionsManager: ObservableObject {
    private static let answeredQuestionsKey = "answered_questions"

    @Published var answeredQuestionIds: Set<String> = []

    static let shared = AnsweredQuestionsManager()

    private init() {
        loadAnsweredQuestions()
    }

    private func loadAnsweredQuestions() {
        if let data = UserDefaults.standard.data(forKey: UserDefaultsKeys.Game.answeredQuestions),
           let decoded = try? JSONDecoder().decode(Set<String>.self, from: data) {
            answeredQuestionIds = decoded
        }
    }

    private func saveAnsweredQuestions() {
        if let encoded = try? JSONEncoder().encode(answeredQuestionIds) {
            UserDefaults.standard.set(encoded, forKey: UserDefaultsKeys.Game.answeredQuestions)
        }
    }

    func markQuestionAnswered(_ questionId: String) {
        answeredQuestionIds.insert(questionId)
        saveAnsweredQuestions()
    }

    func isQuestionAnswered(_ questionId: String) -> Bool {
        return answeredQuestionIds.contains(questionId)
    }

    func getAnsweredCount() -> Int {
        return answeredQuestionIds.count
    }

    func resetAllAnswered() {
        answeredQuestionIds.removeAll()
        saveAnsweredQuestions()
    }

    // MARK: - Topic Reset Methods

    // Reset answered questions for a specific topic
    func resetTopicProgress(_ topicId: String, in questions: [TriviaQuestion]) {
        let topicQuestionIds = questions
            .filter { $0.topic == topicId }
            .map { $0.id }

        answeredQuestionIds.subtract(topicQuestionIds)
        saveAnsweredQuestions()
    }

    // Get count of answered questions for a topic (for reset confirmation)
    func getResetCountForTopic(_ topicId: String, in questions: [TriviaQuestion]) -> Int {
        let topicQuestionIds = Set(questions.filter { $0.topic == topicId }.map { $0.id })
        return topicQuestionIds.intersection(answeredQuestionIds).count
    }

    func getAnsweredCountForCategory(_ category: String, in questions: [TriviaQuestion], difficultyMode: DifficultyMode) -> Int {
        let categoryQuestions = questions.filter { question in
            question.category == category &&
            difficultyMode.shouldInclude(questionDifficulty: question.difficulty) &&
            !PhobiaExclusionManager.shared.isQuestionExcluded(question.id)
        }

        return categoryQuestions.filter { answeredQuestionIds.contains($0.id) }.count
    }

    func getTotalQuestionsForCategory(_ category: String, in questions: [TriviaQuestion], difficultyMode: DifficultyMode) -> Int {
        return questions.filter { question in
            question.category == category &&
            difficultyMode.shouldInclude(questionDifficulty: question.difficulty) &&
            !PhobiaExclusionManager.shared.isQuestionExcluded(question.id)
        }.count
    }

    func areAllQuestionsAnswered(in questions: [TriviaQuestion], difficultyMode: DifficultyMode) -> Bool {
        let availableQuestions = questions.filter { difficultyMode.shouldInclude(questionDifficulty: $0.difficulty) }
        return availableQuestions.allSatisfy { answeredQuestionIds.contains($0.id) }
    }

    func areAllCategoryQuestionsAnswered(_ category: String, in questions: [TriviaQuestion], difficultyMode: DifficultyMode) -> Bool {
        let categoryQuestions = questions.filter { question in
            question.category == category &&
            difficultyMode.shouldInclude(questionDifficulty: question.difficulty) &&
            !PhobiaExclusionManager.shared.isQuestionExcluded(question.id)
        }

        if categoryQuestions.isEmpty {
            return true // Consider empty category as completed
        }

        return categoryQuestions.allSatisfy { answeredQuestionIds.contains($0.id) }
    }

    func getAnsweredCountForSubcategory(_ subcategory: String, in questions: [TriviaQuestion], difficultyMode: DifficultyMode) -> Int {
        let subcategoryQuestions = questions.filter { question in
            question.subcategory == subcategory &&
            difficultyMode.shouldInclude(questionDifficulty: question.difficulty) &&
            !PhobiaExclusionManager.shared.isQuestionExcluded(question.id)
        }

        return subcategoryQuestions.filter { answeredQuestionIds.contains($0.id) }.count
    }

    func getTotalQuestionsForSubcategory(_ subcategory: String, in questions: [TriviaQuestion], difficultyMode: DifficultyMode) -> Int {
        return questions.filter { question in
            question.subcategory == subcategory &&
            difficultyMode.shouldInclude(questionDifficulty: question.difficulty) &&
            !PhobiaExclusionManager.shared.isQuestionExcluded(question.id)
        }.count
    }

    func areAllSubcategoryQuestionsAnswered(_ subcategory: String, in questions: [TriviaQuestion], difficultyMode: DifficultyMode) -> Bool {
        let subcategoryQuestions = questions.filter { question in
            question.subcategory == subcategory &&
            difficultyMode.shouldInclude(questionDifficulty: question.difficulty) &&
            !PhobiaExclusionManager.shared.isQuestionExcluded(question.id)
        }

        if subcategoryQuestions.isEmpty {
            return true // Consider empty subcategory as completed
        }

        return subcategoryQuestions.allSatisfy { answeredQuestionIds.contains($0.id) }
    }

    // MARK: - Topic Completion Methods

    // Check if all questions for a topic are answered
    func areAllTopicQuestionsAnswered(_ topicId: String, in questions: [TriviaQuestion], difficultyMode: DifficultyMode) -> Bool {
        let topicQuestions = questions.filter { question in
            question.topic == topicId &&
            difficultyMode.shouldInclude(questionDifficulty: question.difficulty) &&
            !PhobiaExclusionManager.shared.isQuestionExcluded(question.id)
        }

        if topicQuestions.isEmpty {
            return true
        }

        return topicQuestions.allSatisfy { answeredQuestionIds.contains($0.id) }
    }

    // Get answered count for a topic
    func getAnsweredCountForTopic(_ topicId: String, in questions: [TriviaQuestion], difficultyMode: DifficultyMode) -> Int {
        let topicQuestions = questions.filter { question in
            question.topic == topicId &&
            difficultyMode.shouldInclude(questionDifficulty: question.difficulty) &&
            !PhobiaExclusionManager.shared.isQuestionExcluded(question.id)
        }

        return topicQuestions.filter { answeredQuestionIds.contains($0.id) }.count
    }

    // Get total questions for a topic
    func getTotalQuestionsForTopic(_ topicId: String, in questions: [TriviaQuestion], difficultyMode: DifficultyMode) -> Int {
        return questions.filter { question in
            question.topic == topicId &&
            difficultyMode.shouldInclude(questionDifficulty: question.difficulty) &&
            !PhobiaExclusionManager.shared.isQuestionExcluded(question.id)
        }.count
    }
}
