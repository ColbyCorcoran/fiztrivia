import Foundation
import SwiftData
import UIKit

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

    var subcategories: [String] {
        // This will be populated dynamically from the question database
        return []
    }
}

// MARK: - Subcategory Protocol
protocol TriviaSubcategory {
    var name: String { get }
    var icon: String { get }
    var color: String { get }
}

// MARK: - Entertainment Subcategories
struct EntertainmentSubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let comicBooks = EntertainmentSubcategory(name: "Comic Books", icon: "book.pages.fill", color: "#F7B500")
    static let harryPotter = EntertainmentSubcategory(name: "Harry Potter", icon: "wand.and.stars", color: "#FF7F0F")
    static let pokemon = EntertainmentSubcategory(name: "Pokémon", icon: "circle.circle.fill", color: "#8E44AD")
    static let starWars = EntertainmentSubcategory(name: "Star Wars", icon: "allergens.fill", color: "#3498DB")
    static let pixar = EntertainmentSubcategory(name: "Pixar", icon: "lamp.desk.fill", color: "#1ABC9C")
    static let filmScoreComposers = EntertainmentSubcategory(name: "Film Score Composers", icon: "music.note.list", color: "#2ECC71")
    static let theOffice = EntertainmentSubcategory(name: "The Office", icon: "building.2.fill", color: "#E91E63")

    static let all: [EntertainmentSubcategory] = [comicBooks, harryPotter, pokemon, starWars, pixar, filmScoreComposers, theOffice]
}

// MARK: - Sports Subcategories
struct SportsSubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let basketball = SportsSubcategory(name: "Basketball", icon: "basketball.fill", color: "#F7B500")
    static let tennis = SportsSubcategory(name: "Tennis", icon: "tennisball.fill", color: "#FF7F0F")
    static let golf = SportsSubcategory(name: "Golf", icon: "figure.golf", color: "#8E44AD")
    static let soccer = SportsSubcategory(name: "Soccer", icon: "soccerball", color: "#3498DB")
    static let olympics = SportsSubcategory(name: "Olympics", icon: "medal.fill", color: "#1ABC9C")
    static let hockey = SportsSubcategory(name: "Hockey", icon: "hockey.puck.fill", color: "#2ECC71")
    static let americanFootball = SportsSubcategory(name: "American Football", icon: "football.fill", color: "#E91E63")
    static let baseball = SportsSubcategory(name: "Baseball", icon: "baseball.fill", color: "#5C6BC0")

    static let all: [SportsSubcategory] = [basketball, tennis, golf, soccer, olympics, hockey, americanFootball, baseball]
}

// MARK: - Bible Subcategories
struct BibleSubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let oldTestament = BibleSubcategory(name: "Old Testament", icon: "scroll.fill", color: "#F7B500")
    static let newTestament = BibleSubcategory(name: "New Testament", icon: "flame.fill", color: "#FF7F0F")
    static let bibleTrivia = BibleSubcategory(name: "Bible Trivia", icon: "questionmark.circle.fill", color: "#8E44AD")
    static let biblicalHistory = BibleSubcategory(name: "Biblical History", icon: "building.columns.fill", color: "#3498DB")
    static let biblicalTheology = BibleSubcategory(name: "Biblical Theology", icon: "lightbulb.fill", color: "#1ABC9C")
    static let biblicalLanguages = BibleSubcategory(name: "Biblical Languages", icon: "textformat.abc", color: "#2ECC71")

    static let all: [BibleSubcategory] = [oldTestament, newTestament, bibleTrivia, biblicalHistory, biblicalTheology, biblicalLanguages]
}

// MARK: - History Subcategories
struct HistorySubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let modernHistory = HistorySubcategory(name: "Modern History", icon: "airplane.departure", color: "#F7B500")
    static let ancientHistory = HistorySubcategory(name: "Ancient History", icon: "building.columns.fill", color: "#FF7F0F")
    static let medievalHistory = HistorySubcategory(name: "Medieval History", icon: "shield.lefthalf.filled", color: "#8E44AD")
    static let churchHistory = HistorySubcategory(name: "Church History", icon: "building.fill", color: "#3498DB")

    static let all: [HistorySubcategory] = [modernHistory, ancientHistory, medievalHistory, churchHistory]
}

// MARK: - Science Subcategories
struct ScienceSubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let biology = ScienceSubcategory(name: "Biology", icon: "leaf.fill", color: "#F7B500")
    static let chemistry = ScienceSubcategory(name: "Chemistry", icon: "flask.fill", color: "#FF7F0F")
    static let physics = ScienceSubcategory(name: "Physics", icon: "atom", color: "#8E44AD")
    static let astronomy = ScienceSubcategory(name: "Astronomy", icon: "sparkles", color: "#3498DB")

    static let all: [ScienceSubcategory] = [biology, chemistry, physics, astronomy]
}

// MARK: - Earth Subcategories
struct EarthSubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let animals = EarthSubcategory(name: "Animals", icon: "pawprint.fill", color: "#F7B500")
    static let weather = EarthSubcategory(name: "Weather", icon: "cloud.sun.fill", color: "#FF7F0F")
    static let plants = EarthSubcategory(name: "Plants", icon: "leaf.fill", color: "#8E44AD")
    static let trees = EarthSubcategory(name: "Trees", icon: "tree.fill", color: "#3498DB")
    static let geography = EarthSubcategory(name: "Geography", icon: "map.fill", color: "#1ABC9C")

    static let all: [EarthSubcategory] = [animals, weather, plants, trees, geography]
}

// MARK: - Food Subcategories
struct FoodSubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let ingredients = FoodSubcategory(name: "Ingredients", icon: "carrot.fill", color: "#F7B500")
    static let famousChefs = FoodSubcategory(name: "Famous Chefs/Restaurants", icon: "person.3.fill", color: "#FF7F0F")
    static let dishes = FoodSubcategory(name: "Dishes", icon: "fork.knife", color: "#8E44AD")

    static let all: [FoodSubcategory] = [ingredients, famousChefs, dishes]
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

    func getAnsweredCountForSubcategory(_ subcategory: String, in questions: [TriviaQuestion], difficultyMode: DifficultyMode) -> Int {
        let subcategoryQuestions = questions.filter { question in
            question.subcategory == subcategory &&
            difficultyMode.shouldInclude(questionDifficulty: question.difficulty)
        }

        return subcategoryQuestions.filter { answeredQuestionIds.contains($0.id) }.count
    }

    func getTotalQuestionsForSubcategory(_ subcategory: String, in questions: [TriviaQuestion], difficultyMode: DifficultyMode) -> Int {
        return questions.filter { question in
            question.subcategory == subcategory &&
            difficultyMode.shouldInclude(questionDifficulty: question.difficulty)
        }.count
    }

    func areAllSubcategoryQuestionsAnswered(_ subcategory: String, in questions: [TriviaQuestion], difficultyMode: DifficultyMode) -> Bool {
        let subcategoryQuestions = questions.filter { question in
            question.subcategory == subcategory &&
            difficultyMode.shouldInclude(questionDifficulty: question.difficulty)
        }

        if subcategoryQuestions.isEmpty {
            return true // Consider empty subcategory as completed
        }

        return subcategoryQuestions.allSatisfy { answeredQuestionIds.contains($0.id) }
    }
}

// MARK: - Single Category Mode Manager
class SingleCategoryModeManager: ObservableObject {
    private static let modeEnabledKey = "single_category_mode_enabled"
    private static let selectedCategoryKey = "single_category_mode_selected_category"

    @Published var isEnabled: Bool = false
    @Published var selectedCategory: TriviaCategory?

    static let shared = SingleCategoryModeManager()

    private init() {
        loadSettings()
    }

    private func loadSettings() {
        isEnabled = UserDefaults.standard.bool(forKey: Self.modeEnabledKey)

        if let categoryString = UserDefaults.standard.string(forKey: Self.selectedCategoryKey),
           let category = TriviaCategory(rawValue: categoryString) {
            selectedCategory = category
        }
    }

    func setModeEnabled(_ enabled: Bool) {
        isEnabled = enabled
        UserDefaults.standard.set(enabled, forKey: Self.modeEnabledKey)
    }

    func setSelectedCategory(_ category: TriviaCategory?) {
        selectedCategory = category
        if let category = category {
            UserDefaults.standard.set(category.rawValue, forKey: Self.selectedCategoryKey)
        } else {
            UserDefaults.standard.removeObject(forKey: Self.selectedCategoryKey)
        }
    }

    func getSubcategoriesForSelectedCategory(from questions: [TriviaQuestion], difficultyMode: DifficultyMode) -> [any TriviaSubcategory] {
        guard let category = selectedCategory else { return [] }

        // Get all unique subcategories from the question database for this category
        let subcategoryNames = Set(questions.filter { $0.category == category.rawValue }.compactMap { $0.subcategory })

        // Map to subcategory objects with icon and color
        var subcategories: [any TriviaSubcategory] = []

        switch category {
        case .entertainment:
            subcategories = EntertainmentSubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .sports:
            subcategories = SportsSubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .bible:
            subcategories = BibleSubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .history:
            subcategories = HistorySubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .science:
            subcategories = ScienceSubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .earth:
            subcategories = EarthSubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .food:
            subcategories = FoodSubcategory.all.filter { subcategoryNames.contains($0.name) }
        }

        return subcategories
    }

    func hasQuestionsRemaining(for subcategory: String, in questions: [TriviaQuestion], difficultyMode: DifficultyMode, answeredManager: AnsweredQuestionsManager) -> Bool {
        let subcategoryQuestions = questions.filter { question in
            question.subcategory == subcategory &&
            difficultyMode.shouldInclude(questionDifficulty: question.difficulty) &&
            !answeredManager.isQuestionAnswered(question.id)
        }

        return !subcategoryQuestions.isEmpty
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

// MARK: - App Icon Manager
class AppIconManager: ObservableObject {
    private static let selectedIconKey = "selected_app_icon"

    @Published var selectedIcon: AppIcon = .correct

    static let shared = AppIconManager()

    enum AppIcon: String, CaseIterable, Identifiable {
        case correct = "Correct"
        case regularPose = "Regular Pose"
        case happySmirk = "Happy Smirk"
        case incorrect = "Incorrect"
        case leaderboard = "Leaderboard"
        case newHighScore = "New High Score"

        var id: String { rawValue }

        var iconName: String? {
            // Return nil for the default icon (Correct - ships with the app)
            // For alternate icons, return the name that matches the bundle icon name
            switch self {
            case .correct: return nil  // Default - uses main AppIcon
            case .regularPose: return "AppIcon-RegularPose"
            case .happySmirk: return "AppIcon-HappySmirk"
            case .incorrect: return "AppIcon-Incorrect"
            case .leaderboard: return "AppIcon-Leaderboard"
            case .newHighScore: return "AppIcon-NewHighScore"
            }
        }

        var previewImageName: String {
            // Image names from Assets.xcassets for preview
            switch self {
            case .correct: return "fiz-correct"
            case .regularPose: return "fiz-regular pose"
            case .happySmirk: return "fiz-happy smirk"
            case .incorrect: return "fiz-incorrect"
            case .leaderboard: return "fiz-leaderboard"
            case .newHighScore: return "fiz-new high score"
            }
        }

        var description: String {
            switch self {
            case .correct: return "Fiz celebrating (Default)"
            case .regularPose: return "Fiz in regular pose"
            case .happySmirk: return "Fiz with a happy smirk"
            case .incorrect: return "Fiz thinking"
            case .leaderboard: return "Fiz on the leaderboard"
            case .newHighScore: return "Fiz with new high score"
            }
        }
    }

    private init() {
        loadSelectedIcon()
    }

    private func loadSelectedIcon() {
        if let savedIconName = UserDefaults.standard.string(forKey: Self.selectedIconKey),
           let icon = AppIcon(rawValue: savedIconName) {
            selectedIcon = icon
        } else {
            // Default to Correct if no saved preference
            selectedIcon = .correct
        }
    }

    func setIcon(_ icon: AppIcon) {
        selectedIcon = icon
        UserDefaults.standard.set(icon.rawValue, forKey: Self.selectedIconKey)

        // Change the app icon using UIApplication
        if UIApplication.shared.supportsAlternateIcons {
            UIApplication.shared.setAlternateIconName(icon.iconName) { error in
                if let error = error {
                    print("Error setting alternate icon: \(error.localizedDescription)")
                } else {
                    print("Successfully changed app icon to: \(icon.rawValue)")
                }
            }
        }
    }
}
