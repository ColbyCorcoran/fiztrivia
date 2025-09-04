import Foundation
import SwiftData

struct TriviaQuestion: Codable, Identifiable {
    let id: String
    let category: String
    let subcategory: String?
    let question: String
    let options: [String]
    let correctAnswer: String
    let difficulty: String
    
    init(id: String? = nil, category: String, subcategory: String?, question: String, options: [String], correctAnswer: String, difficulty: String) {
        self.id = id ?? UUID().uuidString
        self.category = category
        self.subcategory = subcategory
        self.question = question
        self.options = options
        self.correctAnswer = correctAnswer
        self.difficulty = difficulty
    }
    
    private enum CodingKeys: String, CodingKey {
        case id, category, subcategory, question, options
        case correctAnswer = "correct_answer"
        case difficulty
    }
}

enum TriviaCategory: String, CaseIterable {
    case entertainment = "Entertainment"
    case sports = "Sports"
    case bible = "Bible"
    case history = "History"
    case science = "Science"
    case earth = "Earth"
    case food = "Food"
    
    var icon: String {
        switch self {
        case .entertainment: return "movieclapper.fill"
        case .sports: return "tennisball.fill"
        case .bible: return "text.book.closed.fill"
        case .history: return "building.columns.fill"
        case .science: return "atom"
        case .earth: return "globe.europe.africa.fill"
        case .food: return "fork.knife.circle.fill"
        }
    }
    
    var color: String {
        switch self {
        case .entertainment: return "#F7B500"
        case .sports: return "#FF7F0F"
        case .bible: return "#8E44AD"
        case .history: return "#3498DB"
        case .science: return "#1ABC9C"
        case .earth: return "#2ECC71"
        case .food: return "#E91E63"
        }
    }
}

@Model
final class LeaderboardEntry {
    var streak: Int
    var date: Date
    var id: UUID
    
    init(streak: Int, date: Date) {
        self.streak = streak
        self.date = date
        self.id = UUID()
    }
}

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

// MARK: - User Management
class UserManager: ObservableObject {
    private static let usernameKey = "user_name"
    private static let hasCompletedOnboardingKey = "has_completed_onboarding"
    
    @Published var username: String = ""
    @Published var hasCompletedOnboarding: Bool = false
    
    static let shared = UserManager()
    
    private init() {
        loadUserData()
    }
    
    private func loadUserData() {
        username = UserDefaults.standard.string(forKey: Self.usernameKey) ?? ""
        hasCompletedOnboarding = UserDefaults.standard.bool(forKey: Self.hasCompletedOnboardingKey)
    }
    
    func saveUsername(_ name: String) {
        username = name.trimmingCharacters(in: .whitespacesAndNewlines)
        UserDefaults.standard.set(username, forKey: Self.usernameKey)
        
        if !hasCompletedOnboarding {
            hasCompletedOnboarding = true
            UserDefaults.standard.set(true, forKey: Self.hasCompletedOnboardingKey)
        }
    }
    
    func updateUsername(_ name: String) {
        saveUsername(name)
    }
    
    var displayName: String {
        return username.isEmpty ? "Player" : username
    }
    
    var personalizedTagline: String {
        return username.isEmpty ? "Trivia, just for you" : "Trivia, just for \(username)"
    }
    
    func personalizedCongratulatoryMessage() -> String {
        let messages = [
            "Excellent, \(displayName)!",
            "Well done, \(displayName)!",
            "Correct, \(displayName)!",
            "Nice work, \(displayName)!",
            "Outstanding, \(displayName)!",
            "Perfect, \(displayName)!",
            "Great job, \(displayName)!",
            "Fantastic, \(displayName)!"
        ]
        return messages.randomElement() ?? "Great, \(displayName)!"
    }
    
    func personalizedEncouragingMessage() -> String {
        let messages = [
            "Good try, \(displayName)!",
            "You'll get it next time, \(displayName)!",
            "Close, \(displayName)!",
            "Keep going, \(displayName)!",
            "Nice attempt, \(displayName)!",
            "Don't give up, \(displayName)!"
        ]
        return messages.randomElement() ?? "Try again, \(displayName)!"
    }
}

// MARK: - Persistent Streak Manager
class StreakPersistenceManager {
    private static let streakKey = "current_streak"
    
    static func saveCurrentStreak(_ streak: Int) {
        UserDefaults.standard.set(streak, forKey: streakKey)
    }
    
    static func loadCurrentStreak() -> Int {
        return UserDefaults.standard.integer(forKey: streakKey)
    }
    
    static func clearCurrentStreak() {
        UserDefaults.standard.removeObject(forKey: streakKey)
    }
}

// MARK: - Difficulty Manager
class DifficultyManager: ObservableObject {
    private static let difficultyKey = "selected_difficulty_mode"
    
    @Published var selectedDifficulty: DifficultyMode = .normal
    
    static let shared = DifficultyManager()
    
    private init() {
        loadSelectedDifficulty()
    }
    
    private func loadSelectedDifficulty() {
        if let saved = UserDefaults.standard.string(forKey: Self.difficultyKey),
           let difficulty = DifficultyMode(rawValue: saved) {
            selectedDifficulty = difficulty
        }
    }
    
    func setDifficulty(_ difficulty: DifficultyMode) {
        selectedDifficulty = difficulty
        UserDefaults.standard.set(difficulty.rawValue, forKey: Self.difficultyKey)
    }
}

// MARK: - Answered Questions Manager
class AnsweredQuestionsManager: ObservableObject {
    private static let answeredQuestionsKey = "answered_questions"
    
    @Published var answeredQuestionIds: Set<String> = []
    
    static let shared = AnsweredQuestionsManager()
    
    private init() {
        loadAnsweredQuestions()
    }
    
    private func loadAnsweredQuestions() {
        if let data = UserDefaults.standard.data(forKey: Self.answeredQuestionsKey),
           let decoded = try? JSONDecoder().decode(Set<String>.self, from: data) {
            answeredQuestionIds = decoded
        }
    }
    
    private func saveAnsweredQuestions() {
        if let encoded = try? JSONEncoder().encode(answeredQuestionIds) {
            UserDefaults.standard.set(encoded, forKey: Self.answeredQuestionsKey)
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
    
    func getAnsweredCountForCategory(_ category: String, in questions: [TriviaQuestion], difficultyMode: DifficultyMode) -> Int {
        let categoryQuestions = questions.filter { question in
            question.category == category &&
            difficultyMode.shouldInclude(questionDifficulty: question.difficulty)
        }
        
        return categoryQuestions.filter { answeredQuestionIds.contains($0.id) }.count
    }
    
    func getTotalQuestionsForCategory(_ category: String, in questions: [TriviaQuestion], difficultyMode: DifficultyMode) -> Int {
        return questions.filter { question in
            question.category == category &&
            difficultyMode.shouldInclude(questionDifficulty: question.difficulty)
        }.count
    }
    
    func areAllQuestionsAnswered(in questions: [TriviaQuestion], difficultyMode: DifficultyMode) -> Bool {
        let availableQuestions = questions.filter { difficultyMode.shouldInclude(questionDifficulty: $0.difficulty) }
        return availableQuestions.allSatisfy { answeredQuestionIds.contains($0.id) }
    }
}

struct GameSession {
    private var _currentStreak: Int = 0
    
    var currentStreak: Int {
        get {
            return _currentStreak
        }
        set {
            _currentStreak = newValue
            // Automatically save to persistence whenever streak changes
            StreakPersistenceManager.saveCurrentStreak(newValue)
        }
    }
    
    var selectedCategory: TriviaCategory?
    var currentQuestion: TriviaQuestion?
    var answerState: AnswerState = .unanswered
    
    init() {
        // Load persistent streak on initialization
        _currentStreak = StreakPersistenceManager.loadCurrentStreak()
    }
}
