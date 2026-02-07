import Foundation
import SwiftData
import UIKit

// MARK: - Notification Names

extension Notification.Name {
    /// Posted when expansion packs are installed or uninstalled
    static let expansionPacksChanged = Notification.Name("expansionPacksChanged")
}

// MARK: - Models

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

    static let animation = EntertainmentSubcategory(name: "Animation", icon: "film.stack.fill", color: "#F7B500")
    static let sciFiFantasy = EntertainmentSubcategory(name: "Sci-Fi/Fantasy", icon: "sparkles", color: "#FF7F0F")
    static let actionAdventure = EntertainmentSubcategory(name: "Action/Adventure", icon: "figure.run", color: "#8E44AD")
    static let dramaComedy = EntertainmentSubcategory(name: "Drama/Comedy", icon: "theatermasks.fill", color: "#3498DB")

    static let all: [EntertainmentSubcategory] = [animation, sciFiFantasy, actionAdventure, dramaComedy]
}

// MARK: - Sports Subcategories
struct SportsSubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let teamSports = SportsSubcategory(name: "Team Sports", icon: "figure.basketball", color: "#F7B500")
    static let individualSports = SportsSubcategory(name: "Individual Sports", icon: "figure.tennis", color: "#FF7F0F")
    static let internationalCompetition = SportsSubcategory(name: "International Competition", icon: "medal.fill", color: "#8E44AD")
    static let extremeActionSports = SportsSubcategory(name: "Extreme & Action Sports", icon: "figure.snowboarding", color: "#3498DB")
    static let sportsHistoryRecords = SportsSubcategory(name: "Sports History & Records", icon: "trophy.fill", color: "#1ABC9C")
    static let athletesBiography = SportsSubcategory(name: "Athletes & Biography", icon: "person.2.fill", color: "#2ECC71")

    static let all: [SportsSubcategory] = [teamSports, individualSports, internationalCompetition, extremeActionSports, sportsHistoryRecords, athletesBiography]
}

// MARK: - Bible Subcategories
struct BibleSubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let bibleTrivia = BibleSubcategory(name: "Bible Trivia", icon: "text.book.closed.fill", color: "#F7B500")
    static let biblicalHistory = BibleSubcategory(name: "Biblical History", icon: "clock.arrow.circlepath", color: "#FF7F0F")
    static let biblicalTheology = BibleSubcategory(name: "Biblical Theology", icon: "text.magnifyingglass", color: "#8E44AD")
    static let bibleLanguages = BibleSubcategory(name: "Bible Languages", icon: "pencil.and.scribble", color: "#3498DB")

    static let all: [BibleSubcategory] = [bibleTrivia, biblicalHistory, biblicalTheology, bibleLanguages]
}

// MARK: - History Subcategories
struct HistorySubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let modernHistory = HistorySubcategory(name: "Modern History", icon: "building.fill", color: "#F7B500")
    static let ancientHistory = HistorySubcategory(name: "Ancient History", icon: "building.columns.fill", color: "#FF7F0F")
    static let medievalHistory = HistorySubcategory(name: "Medieval History", icon: "shield.lefthalf.filled", color: "#8E44AD")
    static let churchHistory = HistorySubcategory(name: "Church History", icon: "text.book.closed.fill", color: "#3498DB")

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
    static let astronomy = ScienceSubcategory(name: "Astronomy", icon: "moon.stars.fill", color: "#3498DB")

    static let all: [ScienceSubcategory] = [biology, chemistry, physics, astronomy]
}

// MARK: - Nature Subcategories
struct NatureSubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let trees = NatureSubcategory(name: "Trees", icon: "tree.fill", color: "#F7B500")
    static let weather = NatureSubcategory(name: "Weather", icon: "cloud.sun.fill", color: "#FF7F0F")
    static let plantsFlowers = NatureSubcategory(name: "Plants & Flowers", icon: "leaf.fill", color: "#8E44AD")
    static let animalsWildlife = NatureSubcategory(name: "Animals & Wildlife", icon: "pawprint.fill", color: "#3498DB")
    static let oceansMarineLife = NatureSubcategory(name: "Oceans & Marine Life", icon: "water.waves", color: "#1ABC9C")

    static let all: [NatureSubcategory] = [trees, weather, plantsFlowers, animalsWildlife, oceansMarineLife]
}

// MARK: - Food Subcategories
struct FoodSubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let ingredients = FoodSubcategory(name: "Ingredients", icon: "carrot.fill", color: "#F7B500")
    static let bakingDesserts = FoodSubcategory(name: "Baking & Desserts", icon: "birthday.cake.fill", color: "#FF7F0F")
    static let cooking = FoodSubcategory(name: "Cooking", icon: "cooktop.fill", color: "#8E44AD")
    static let foodHistory = FoodSubcategory(name: "Food History", icon: "clock.arrow.circlepath", color: "#3498DB")
    static let dishesCuisines = FoodSubcategory(name: "Dishes & Cuisines", icon: "fork.knife", color: "#1ABC9C")
    static let beverages = FoodSubcategory(name: "Beverages", icon: "cup.and.saucer.fill", color: "#2ECC71")

    static let all: [FoodSubcategory] = [ingredients, bakingDesserts, cooking, foodHistory, dishesCuisines, beverages]
}

// MARK: - Literature Subcategories
struct LiteratureSubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let fantasyLiterature = LiteratureSubcategory(name: "Fantasy Literature", icon: "wand.and.stars", color: "#F7B500")
    static let classicLiterature = LiteratureSubcategory(name: "Classic Literature", icon: "book.closed.fill", color: "#FF7F0F")
    static let modernFiction = LiteratureSubcategory(name: "Modern Fiction", icon: "book.pages.fill", color: "#8E44AD")
    static let poetry = LiteratureSubcategory(name: "Poetry", icon: "text.alignleft", color: "#3498DB")
    static let childrensBooks = LiteratureSubcategory(name: "Children's Books", icon: "figure.and.child.holdinghands", color: "#1ABC9C")
    static let authorsBiography = LiteratureSubcategory(name: "Authors & Biography", icon: "person.text.rectangle.fill", color: "#2ECC71")

    static let all: [LiteratureSubcategory] = [fantasyLiterature, classicLiterature, modernFiction, poetry, childrensBooks, authorsBiography]
}

// MARK: - Music Subcategories
struct MusicSubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let historyEras = MusicSubcategory(name: "History & Eras", icon: "clock.arrow.circlepath", color: "#F7B500")
    static let musiciansBands = MusicSubcategory(name: "Musicians & Bands", icon: "guitars.fill", color: "#FF7F0F")
    static let awardsRecords = MusicSubcategory(name: "Awards & Records", icon: "trophy.fill", color: "#8E44AD")
    static let instrumentsTheory = MusicSubcategory(name: "Instruments & Theory", icon: "music.quarternote.3", color: "#3498DB")
    static let filmTV = MusicSubcategory(name: "Film & TV", icon: "music.note.tv.fill", color: "#1ABC9C")

    static let all: [MusicSubcategory] = [historyEras, musiciansBands, awardsRecords, instrumentsTheory, filmTV]
}

// MARK: - Technology Subcategories
struct TechnologySubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let videoGames = TechnologySubcategory(name: "Video Games", icon: "gamecontroller.fill", color: "#F7B500")
    static let computersSoftware = TechnologySubcategory(name: "Computers & Software", icon: "desktopcomputer", color: "#FF7F0F")
    static let internetSocialMedia = TechnologySubcategory(name: "Internet & Social Media", icon: "network", color: "#8E44AD")
    static let techCompanies = TechnologySubcategory(name: "Tech Companies", icon: "building.2.fill", color: "#3498DB")
    static let inventions = TechnologySubcategory(name: "Inventions", icon: "lightbulb.fill", color: "#1ABC9C")

    static let all: [TechnologySubcategory] = [videoGames, computersSoftware, internetSocialMedia, techCompanies, inventions]
}

// MARK: - Art Subcategories
struct ArtSubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let famousPainters = ArtSubcategory(name: "Famous Painters", icon: "paintbrush.fill", color: "#F7B500")
    static let artHistoryMovements = ArtSubcategory(name: "Art History & Movements", icon: "clock.arrow.circlepath", color: "#FF7F0F")
    static let sculpture = ArtSubcategory(name: "Sculpture", icon: "person.bust.fill", color: "#8E44AD")
    static let architecture = ArtSubcategory(name: "Architecture", icon: "building.fill", color: "#3498DB")
    static let photography = ArtSubcategory(name: "Photography", icon: "camera.fill", color: "#1ABC9C")

    static let all: [ArtSubcategory] = [famousPainters, artHistoryMovements, sculpture, architecture, photography]
}

// MARK: - Geography Subcategories
struct GeographySubcategory: TriviaSubcategory {
    let name: String
    let icon: String
    let color: String

    static let usGeography = GeographySubcategory(name: "U.S. Geography", icon: "mappin", color: "#F7B500")
    static let worldGeography = GeographySubcategory(name: "World Geography", icon: "globe", color: "#FF7F0F")
    static let flags = GeographySubcategory(name: "Flags", icon: "flag.2.crossed.fill", color: "#8E44AD")
    static let landmarksMonuments = GeographySubcategory(name: "Landmarks & Monuments", icon: "building.2.fill", color: "#3498DB")
    static let mapsBorders = GeographySubcategory(name: "Maps & Borders", icon: "map.fill", color: "#1ABC9C")

    static let all: [GeographySubcategory] = [usGeography, worldGeography, flags, landmarksMonuments, mapsBorders]
}

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
    private static let UserDefaultsKeys.User.username = "user_name"
    private static let UserDefaultsKeys.User.hasCompletedOnboarding = "has_completed_onboarding"
    
    @Published var username: String = ""
    @Published var hasCompletedOnboarding: Bool = false
    
    static let shared = UserManager()
    
    private init() {
        loadUserData()
    }
    
    private func loadUserData() {
        username = UserDefaults.standard.string(forKey: Self.UserDefaultsKeys.User.username) ?? ""
        hasCompletedOnboarding = UserDefaults.standard.bool(forKey: Self.UserDefaultsKeys.User.hasCompletedOnboarding)
    }
    
    /// Sanitizes and saves the username with validation
    /// - Parameter name: Raw username input from user
    /// - Returns: True if username was saved, false if validation failed
    @discardableResult
    func saveUsername(_ name: String) -> Bool {
        let sanitized = sanitizeUsername(name)

        // Allow empty username (falls back to "Player")
        username = sanitized
        UserDefaults.standard.set(username, forKey: Self.UserDefaultsKeys.User.username)

        if !hasCompletedOnboarding {
            hasCompletedOnboarding = true
            UserDefaults.standard.set(true, forKey: Self.UserDefaultsKeys.User.hasCompletedOnboarding)
        }

        return true
    }

    func updateUsername(_ name: String) {
        saveUsername(name)
    }

    /// Sanitizes username input to prevent UI corruption and analytics issues
    /// - Allows: Letters, numbers, spaces, common punctuation (. , ' -)
    /// - Limits: 50 characters maximum
    /// - Trims: Leading/trailing whitespace
    private func sanitizeUsername(_ name: String) -> String {
        let trimmed = name.trimmingCharacters(in: .whitespacesAndNewlines)

        // Allow letters, numbers, spaces, and safe punctuation
        let allowedCharacters = CharacterSet.letters
            .union(.decimalDigits)
            .union(.whitespaces)
            .union(CharacterSet(charactersIn: ".,'- "))

        let sanitized = trimmed.unicodeScalars.filter { allowedCharacters.contains($0) }
        let result = String(String.UnicodeScalarView(sanitized))

        // Limit to 50 characters
        return String(result.prefix(50))
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

// MARK: - Phobia Data Model
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
    private static let UserDefaultsKeys.Game.selectedDifficulty = "selected_difficulty_mode"
    
    @Published var selectedDifficulty: DifficultyMode = .normal
    
    static let shared = DifficultyManager()
    
    private init() {
        loadSelectedDifficulty()
    }
    
    private func loadSelectedDifficulty() {
        if let saved = UserDefaults.standard.string(forKey: Self.UserDefaultsKeys.Game.selectedDifficulty),
           let difficulty = DifficultyMode(rawValue: saved) {
            selectedDifficulty = difficulty
        }
    }
    
    func setDifficulty(_ difficulty: DifficultyMode) {
        selectedDifficulty = difficulty
        UserDefaults.standard.set(difficulty.rawValue, forKey: Self.UserDefaultsKeys.Game.selectedDifficulty)
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

// MARK: - Game Mode Manager
class GameModeManager: ObservableObject {
    private static let selectedModeKey = "selected_game_mode"
    private static let selectedCategoryKey = "game_mode_selected_category"
    private static let selectedTopicKey = "game_mode_selected_topic"
    // Future keys ready:
    // private static let seasonalThemeKey = "game_mode_seasonal_theme"

    @Published var selectedMode: GameMode = .multiCategory

    // Mode-specific settings
    @Published var selectedCategory: TriviaCategory? = nil
    @Published var selectedTopic: String? = nil // Topic packId (e.g., "com.fiz.pack.harry_potter")
    // Future settings ready:
    // @Published var seasonalTheme: String? = nil

    static let shared = GameModeManager()

    private init() {
        migrateFromLegacyStorage()
        loadSettings()
        validateAndFixInvalidState()
    }

    // MARK: - Migration

    private func migrateFromLegacyStorage() {
        let legacyModeKey = "single_category_mode_enabled"
        let legacyCategoryKey = "single_category_mode_selected_category"

        if UserDefaults.standard.object(forKey: legacyModeKey) != nil {
            let wasEnabled = UserDefaults.standard.bool(forKey: legacyModeKey)

            if wasEnabled {
                // Migrate to new system
                UserDefaults.standard.set(GameMode.singleCategory.rawValue, forKey: UserDefaultsKeys.GameMode.selectedMode)

                // Migrate category selection
                if let categoryString = UserDefaults.standard.string(forKey: legacyCategoryKey) {
                    UserDefaults.standard.set(categoryString, forKey: UserDefaultsKeys.GameMode.selectedCategory)
                }
            } else {
                UserDefaults.standard.set(GameMode.multiCategory.rawValue, forKey: UserDefaultsKeys.GameMode.selectedMode)
            }

            // Clean up legacy keys
            UserDefaults.standard.removeObject(forKey: legacyModeKey)
            UserDefaults.standard.removeObject(forKey: legacyCategoryKey)

            print("Migrated from SingleCategoryModeManager to GameModeManager")
        }
    }

    // MARK: - Persistence

    private func loadSettings() {
        // Load selected mode
        if let modeString = UserDefaults.standard.string(forKey: UserDefaultsKeys.GameMode.selectedMode),
           let mode = GameMode(rawValue: modeString) {
            selectedMode = mode
        }

        // Load mode-specific settings
        if let categoryString = UserDefaults.standard.string(forKey: UserDefaultsKeys.GameMode.selectedCategory),
           let category = TriviaCategory(rawValue: categoryString) {
            selectedCategory = category
        }

        if let topicString = UserDefaults.standard.string(forKey: UserDefaultsKeys.GameMode.selectedTopic) {
            selectedTopic = topicString
        }
    }

    private func saveSettings() {
        UserDefaults.standard.set(selectedMode.rawValue, forKey: UserDefaultsKeys.GameMode.selectedMode)

        if let category = selectedCategory {
            UserDefaults.standard.set(category.rawValue, forKey: UserDefaultsKeys.GameMode.selectedCategory)
        } else {
            UserDefaults.standard.removeObject(forKey: UserDefaultsKeys.GameMode.selectedCategory)
        }

        if let topic = selectedTopic {
            UserDefaults.standard.set(topic, forKey: UserDefaultsKeys.GameMode.selectedTopic)
        } else {
            UserDefaults.standard.removeObject(forKey: UserDefaultsKeys.GameMode.selectedTopic)
        }
    }

    // MARK: - Validation

    private func validateAndFixInvalidState() {
        var isValid = true

        switch selectedMode {
        case .multiCategory:
            // Multi-Category mode is always valid
            isValid = true
        case .singleCategory:
            // Single Category requires a selected category
            if selectedCategory == nil {
                isValid = false
                print("⚠️ Invalid state detected: Single Category mode without category selection")
            }
        case .singleTopic:
            // Single Topic requires a selected topic
            guard let topicId = selectedTopic else {
                isValid = false
                print("⚠️ Invalid state detected: Single Topic mode without topic selection")
                break
            }

            // Verify the topic is still available (installed OR has previews)
            if !ExpansionPackManager.shared.isAvailableForSingleTopicMode(packId: topicId) {
                isValid = false
                print("⚠️ Invalid state detected: Selected topic is not available")
            }
        // Future modes:
        // case .seasonal:
        //     // Seasonal mode might always be valid
        //     isValid = true
        }

        // If invalid, reset to Multi-Category mode
        if !isValid {
            print("🔄 Resetting to Multi-Category mode due to invalid state")
            selectedMode = .multiCategory
            selectedCategory = nil
            selectedTopic = nil
            saveSettings()
        }
    }

    // MARK: - Public Methods

    func setMode(_ mode: GameMode) {
        selectedMode = mode

        // Clear settings for other modes when switching
        if mode != .singleCategory {
            selectedCategory = nil
        }
        if mode != .singleTopic {
            selectedTopic = nil
        }

        saveSettings()
    }

    func setSelectedCategory(_ category: TriviaCategory?) {
        selectedCategory = category
        saveSettings()
    }

    func setSelectedTopic(_ topicPackId: String?) {
        selectedTopic = topicPackId
        saveSettings()
    }

    // MARK: - Computed Properties for Compatibility

    // For backward compatibility with existing code
    var isMultiCategoryMode: Bool {
        return selectedMode == .multiCategory
    }

    var isSingleCategoryMode: Bool {
        return selectedMode == .singleCategory
    }

    var isSingleTopicMode: Bool {
        return selectedMode == .singleTopic
    }

    // MARK: - Wheel Segment Logic

    func getSubtopicsForSelectedTopic() -> [String] {
        guard selectedMode == .singleTopic,
              let topicPackId = selectedTopic else {
            return []
        }

        // Get the expansion pack for this topic
        if let pack = ExpansionPackManager.shared.availablePacks.first(where: { $0.packId == topicPackId }) {
            return pack.subtopics
        }

        return []
    }

    func getSubcategoriesForSelectedCategory(from questions: [TriviaQuestion],
                                            difficultyMode: DifficultyMode)
        -> [any TriviaSubcategory] {
        guard selectedMode == .singleCategory,
              let category = selectedCategory else {
            return []
        }

        // Get all unique subcategories from the question database for this category
        let subcategoryNames = Set(questions.filter { $0.category == category.rawValue }.compactMap { $0.subcategory })

        // Map to subcategory objects with icon and color
        var subcategories: [any TriviaSubcategory] = []

        switch category {
        case .entertainment:
            subcategories = EntertainmentSubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .literature:
            subcategories = LiteratureSubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .music:
            subcategories = MusicSubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .technology:
            subcategories = TechnologySubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .art:
            subcategories = ArtSubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .geography:
            subcategories = GeographySubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .sports:
            subcategories = SportsSubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .science:
            subcategories = ScienceSubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .nature:
            subcategories = NatureSubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .history:
            subcategories = HistorySubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .bible:
            subcategories = BibleSubcategory.all.filter { subcategoryNames.contains($0.name) }
        case .food:
            subcategories = FoodSubcategory.all.filter { subcategoryNames.contains($0.name) }
        }

        return subcategories
    }

    func hasQuestionsRemaining(for subcategory: String,
                              in questions: [TriviaQuestion],
                              difficultyMode: DifficultyMode,
                              answeredManager: AnsweredQuestionsManager) -> Bool {
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

// MARK: - Haptic Settings Manager
class HapticSettingsManager: ObservableObject {
    private static let hapticEnabledKey = "haptic_feedback_enabled"

    @Published var isHapticEnabled: Bool = true

    static let shared = HapticSettingsManager()

    private init() {
        loadSettings()
    }

    private func loadSettings() {
        // Default to true if no preference is saved
        if UserDefaults.standard.object(forKey: UserDefaultsKeys.Settings.hapticEnabled) != nil {
            isHapticEnabled = UserDefaults.standard.bool(forKey: UserDefaultsKeys.Settings.hapticEnabled)
        } else {
            isHapticEnabled = true
        }
    }

    func setHapticEnabled(_ enabled: Bool) {
        isHapticEnabled = enabled
        UserDefaults.standard.set(enabled, forKey: UserDefaultsKeys.Settings.hapticEnabled)
    }
}

// MARK: - Popup Duration Manager
class PopupDurationManager: ObservableObject {
    private static let correctPopupDurationKey = "correct_popup_duration"
    private static let incorrectPopupDurationKey = "incorrect_popup_duration"

    @Published var correctPopupDuration: Double = 1.5 // Default 1.5 seconds
    @Published var incorrectPopupDuration: Double = 3.0 // Default 3.0 seconds

    static let shared = PopupDurationManager()

    private init() {
        loadSettings()
    }

    private func loadSettings() {
        // Load correct popup duration (default 1.5)
        if UserDefaults.standard.object(forKey: UserDefaultsKeys.Settings.correctPopupDuration) != nil {
            correctPopupDuration = UserDefaults.standard.double(forKey: UserDefaultsKeys.Settings.correctPopupDuration)
        } else {
            correctPopupDuration = 1.5
        }

        // Load incorrect popup duration (default 3.0)
        if UserDefaults.standard.object(forKey: UserDefaultsKeys.Settings.incorrectPopupDuration) != nil {
            incorrectPopupDuration = UserDefaults.standard.double(forKey: UserDefaultsKeys.Settings.incorrectPopupDuration)
        } else {
            incorrectPopupDuration = 3.0
        }
    }

    func setCorrectPopupDuration(_ duration: Double) {
        correctPopupDuration = duration
        UserDefaults.standard.set(duration, forKey: UserDefaultsKeys.Settings.correctPopupDuration)
    }

    func setIncorrectPopupDuration(_ duration: Double) {
        incorrectPopupDuration = duration
        UserDefaults.standard.set(duration, forKey: UserDefaultsKeys.Settings.incorrectPopupDuration)
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
            // Image names from Assets.xcassets for preview (with cream background to match actual app icons)
            switch self {
            case .correct: return "AppIcon-Correct-Preview"
            case .regularPose: return "AppIcon-RegularPose-Preview"
            case .happySmirk: return "AppIcon-HappySmirk-Preview"
            case .incorrect: return "AppIcon-Incorrect-Preview"
            case .leaderboard: return "AppIcon-Leaderboard-Preview"
            case .newHighScore: return "AppIcon-NewHighScore-Preview"
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
        if let savedIconName = UserDefaults.standard.string(forKey: UserDefaultsKeys.Personalization.selectedAppIcon),
           let icon = AppIcon(rawValue: savedIconName) {
            selectedIcon = icon
        } else {
            // Default to Correct if no saved preference
            selectedIcon = .correct
        }
    }

    func setIcon(_ icon: AppIcon) {
        selectedIcon = icon
        UserDefaults.standard.set(icon.rawValue, forKey: UserDefaultsKeys.Personalization.selectedAppIcon)

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

// MARK: - Category Selection Manager
class CategorySelectionManager: ObservableObject {
    private static let selectedCategoriesKey = "selected_categories"
    private static let customDefaultCategoriesKey = "custom_default_categories"

    @Published var selectedCategories: Set<TriviaCategory> = []

    static let shared = CategorySelectionManager()
    static let minimumCategories = 2
    static let maximumCategories = 12

    private init() {
        loadSettings()
    }

    private func loadSettings() {
        if let data = UserDefaults.standard.data(forKey: UserDefaultsKeys.Categories.selectedCategories),
           let decodedStrings = try? JSONDecoder().decode(Set<String>.self, from: data) {
            selectedCategories = Set(decodedStrings.compactMap { TriviaCategory(rawValue: $0) })

            // Validate count - reset if invalid
            if selectedCategories.count < Self.minimumCategories || selectedCategories.isEmpty {
                setDefaultSelection()
            }
        } else {
            setDefaultSelection()
        }
    }

    private func saveSettings() {
        let categoryStrings = Set(selectedCategories.map { $0.rawValue })
        if let encoded = try? JSONEncoder().encode(categoryStrings) {
            UserDefaults.standard.set(encoded, forKey: UserDefaultsKeys.Categories.selectedCategories)
        }
    }

    func toggleCategory(_ category: TriviaCategory) -> Bool {
        if selectedCategories.contains(category) {
            // Deselecting - check minimum
            if selectedCategories.count > Self.minimumCategories {
                // Check if this is the active single-category mode category
                if GameModeManager.shared.isSingleCategoryMode &&
                   GameModeManager.shared.selectedCategory == category {
                    return false // Cannot deselect active category
                }

                selectedCategories.remove(category)
                saveSettings()
                return true
            } else {
                return false // Cannot go below minimum
            }
        } else {
            // Selecting - check maximum
            if selectedCategories.count < Self.maximumCategories {
                selectedCategories.insert(category)
                saveSettings()
                return true
            } else {
                return false // At maximum
            }
        }
    }

    func isSelected(_ category: TriviaCategory) -> Bool {
        return selectedCategories.contains(category)
    }

    func canToggle(_ category: TriviaCategory) -> Bool {
        if selectedCategories.contains(category) {
            return selectedCategories.count > Self.minimumCategories
        } else {
            return selectedCategories.count < Self.maximumCategories
        }
    }

    // MARK: - Factory Default
    private var factoryDefault: Set<TriviaCategory> {
        // Factory default: All 12 categories enabled
        return [
            .entertainment,
            .sports,
            .bible,
            .history,
            .science,
            .nature,
            .food,
            .music,
            .technology,
            .art,
            .geography,
            .literature
        ]
    }

    private func setDefaultSelection() {
        selectedCategories = factoryDefault
        saveSettings()
    }

    // MARK: - Custom Default Management

    /// Check if user has saved a custom default
    func hasCustomDefault() -> Bool {
        return UserDefaults.standard.data(forKey: UserDefaultsKeys.Categories.customDefaultCategories) != nil
    }

    /// Save current selection as user's custom default
    func saveCurrentAsDefault() {
        let categoryStrings = Set(selectedCategories.map { $0.rawValue })
        if let encoded = try? JSONEncoder().encode(categoryStrings) {
            UserDefaults.standard.set(encoded, forKey: UserDefaultsKeys.Categories.customDefaultCategories)
        }
    }

    /// Save current selection as default only if it differs from factory default
    /// Used for onboarding flow
    func saveCurrentAsDefaultIfDifferent() {
        if selectedCategories != factoryDefault {
            saveCurrentAsDefault()
        }
    }

    /// Reset to user's custom default (or factory default if no custom saved)
    func resetToMyDefault() {
        if let data = UserDefaults.standard.data(forKey: UserDefaultsKeys.Categories.customDefaultCategories),
           let decodedStrings = try? JSONDecoder().decode(Set<String>.self, from: data) {
            selectedCategories = Set(decodedStrings.compactMap { TriviaCategory(rawValue: $0) })

            // Validate count - fall back to factory if invalid
            if selectedCategories.count < Self.minimumCategories || selectedCategories.isEmpty {
                setDefaultSelection()
            } else {
                saveSettings()
            }
        } else {
            // No custom default - fall back to factory
            setDefaultSelection()
        }
    }

    /// Reset to factory default (all 12 categories)
    func resetToFactoryDefault() {
        setDefaultSelection()
    }

    /// Legacy method - now resets to user's custom default
    func resetToDefault() {
        resetToMyDefault()
    }
}

// MARK: - Swipe Navigation Manager
class SwipeNavigationManager: ObservableObject {
    private static let swipeNavigationEnabledKey = "swipe_navigation_enabled"

    @Published var isSwipeNavigationEnabled: Bool = true

    static let shared = SwipeNavigationManager()

    private init() {
        loadSettings()
    }

    private func loadSettings() {
        // Default to true (opt-out for accessibility)
        if UserDefaults.standard.object(forKey: UserDefaultsKeys.Settings.swipeNavigationEnabled) != nil {
            isSwipeNavigationEnabled = UserDefaults.standard.bool(forKey: UserDefaultsKeys.Settings.swipeNavigationEnabled)
        } else {
            isSwipeNavigationEnabled = true
        }
    }

    func setSwipeNavigationEnabled(_ enabled: Bool) {
        isSwipeNavigationEnabled = enabled
        UserDefaults.standard.set(enabled, forKey: UserDefaultsKeys.Settings.swipeNavigationEnabled)
    }
}

// MARK: - Phobia Exclusion Manager
class PhobiaExclusionManager: ObservableObject {
    private static let phobiasKey = "user_phobias"

    @Published var phobias: [Phobia] = []

    static let shared = PhobiaExclusionManager()

    // Predefined synonym dictionary for common phobias
    private let phobiaSynonyms: [String: [String]] = [
        "snake": ["snake", "serpent", "cobra", "python", "viper", "boa", "anaconda",
                  "reptile", "slither", "constrictor", "rattlesnake", "copperhead"],
        "spider": ["spider", "arachnid", "tarantula", "web", "eight-legged", "daddy long legs"],
        "height": ["height", "tall", "cliff", "skyscraper", "altitude", "elevation",
                   "mountain", "tower", "high-rise"],
        "blood": ["blood", "bleeding", "hemorrhage", "vampire", "transfusion"],
        "needle": ["needle", "injection", "syringe", "shot", "vaccine"],
        "dog": ["dog", "canine", "puppy", "hound", "retriever", "terrier"],
        "clown": ["clown", "jester", "circus"],
        "ocean": ["ocean", "sea", "deep water", "shark", "whale", "dolphin"],
        "flying": ["fly", "flight", "airplane", "aircraft", "aviation", "pilot"],
        "crowd": ["crowd", "crowded", "audience", "mass", "gathering"]
    ]

    private init() {
        loadPhobias()
    }

    // MARK: - Persistence

    private func loadPhobias() {
        if let data = UserDefaults.standard.data(forKey: UserDefaultsKeys.Phobia.phobias),
           let decoded = try? JSONDecoder().decode([Phobia].self, from: data) {
            phobias = decoded
        }
    }

    private func savePhobias() {
        if let encoded = try? JSONEncoder().encode(phobias) {
            UserDefaults.standard.set(encoded, forKey: UserDefaultsKeys.Phobia.phobias)
        }
    }

    // MARK: - Public Methods

    /// Adds a phobia filter with input validation
    /// - Parameters:
    ///   - term: User-entered phobia term
    ///   - questions: Question database to scan
    /// - Returns: Tuple of created phobia and count of excluded questions, or nil if validation failed
    func addPhobia(term: String, in questions: [TriviaQuestion]) -> (phobia: Phobia, excludedCount: Int)? {
        // INPUT VALIDATION: Sanitize and validate phobia term
        guard let sanitizedTerm = sanitizePhobiaTerm(term) else {
            print("⚠️ Invalid phobia term: '\(term)' - must be 2-30 characters, letters/numbers only")
            return nil
        }

        // Check for duplicates
        if phobias.contains(where: { $0.term == sanitizedTerm }) {
            print("⚠️ Phobia term already exists: '\(sanitizedTerm)'")
            return nil
        }

        let searchTerms = getSearchTerms(for: sanitizedTerm)
        let excludedIds = scanForMatches(searchTerms: searchTerms, in: questions)

        let phobia = Phobia(term: sanitizedTerm, excludedQuestionIds: excludedIds)
        phobias.append(phobia)
        savePhobias()

        return (phobia, excludedIds.count)
    }

    /// Sanitizes phobia term input to prevent malformed searches
    /// - Allows: Letters, numbers, spaces
    /// - Limits: 2-30 characters
    /// - Trims: Leading/trailing whitespace
    /// - Returns: Sanitized term or nil if invalid
    private func sanitizePhobiaTerm(_ term: String) -> String? {
        let trimmed = term.lowercased().trimmingCharacters(in: .whitespacesAndNewlines)

        // Allow only letters, numbers, and spaces
        let allowedCharacters = CharacterSet.letters
            .union(.decimalDigits)
            .union(.whitespaces)

        let sanitized = trimmed.unicodeScalars.filter { allowedCharacters.contains($0) }
        let result = String(String.UnicodeScalarView(sanitized))

        // Validate length (2-30 characters)
        guard result.count >= 2 && result.count <= 30 else {
            return nil
        }

        return result
    }

    func removePhobia(_ phobia: Phobia) {
        phobias.removeAll { $0.id == phobia.id }
        savePhobias()
    }

    func isQuestionExcluded(_ questionId: String) -> Bool {
        return phobias.contains { $0.excludedQuestionIds.contains(questionId) }
    }

    func getTotalExcludedCount() -> Int {
        let allExcluded = phobias.flatMap { $0.excludedQuestionIds }
        return Set(allExcluded).count // Remove duplicates
    }

    /// Rescans all existing phobias against the current question list.
    /// Call this whenever new questions are added (e.g., expansion pack installed).
    /// Returns total count of newly excluded questions across all phobias.
    @discardableResult
    func rescanAllPhobias(in questions: [TriviaQuestion]) -> Int {
        guard !phobias.isEmpty else { return 0 }

        var totalNewExclusions = 0
        var phobiasUpdated = false

        for i in 0..<phobias.count {
            let phobia = phobias[i]
            let searchTerms = getSearchTerms(for: phobia.term)
            let newExcludedIds = scanForMatches(searchTerms: searchTerms, in: questions)

            // Check if new questions were excluded
            let previousCount = phobia.excludedQuestionIds.count
            let newCount = newExcludedIds.count

            if previousCount != newCount {
                // Update the phobia's excluded question IDs
                phobias[i].excludedQuestionIds = newExcludedIds

                totalNewExclusions += (newCount - previousCount)
                phobiasUpdated = true

                print("Phobia '\(phobia.term)': \(previousCount) → \(newCount) excluded questions (+\(newCount - previousCount))")
            }
        }

        // Save if any phobias were updated
        if phobiasUpdated {
            savePhobias()
            print("✅ Rescanned \(phobias.count) phobia(s), found \(totalNewExclusions) new exclusions")
        }

        return totalNewExclusions
    }

    // MARK: - Private Helpers

    private func getSearchTerms(for term: String) -> [String] {
        // Check if term matches a common phobia in dictionary
        if let synonyms = phobiaSynonyms[term] {
            return synonyms
        }

        // Check if term is a substring of any dictionary key
        for (key, synonyms) in phobiaSynonyms {
            if term.contains(key) || key.contains(term) {
                return synonyms
            }
        }

        // Not a common phobia - use exact term only
        return [term]
    }

    private func scanForMatches(searchTerms: [String], in questions: [TriviaQuestion]) -> Set<String> {
        var matchedIds = Set<String>()

        for question in questions {
            // Collect all searchable text from question
            var searchableText = [question.question.lowercased()]
            searchableText.append(contentsOf: question.options.map { $0.lowercased() })
            searchableText.append(question.correctAnswer.lowercased())

            if let subcategory = question.subcategory {
                searchableText.append(subcategory.lowercased())
            }

            // Check if any search term matches any searchable text (substring)
            let matches = searchTerms.contains { searchTerm in
                searchableText.contains { text in
                    text.contains(searchTerm)
                }
            }

            if matches {
                matchedIds.insert(question.id)
            }
        }

        return matchedIds
    }
}

// MARK: - Onboarding Manager
class OnboardingManager: ObservableObject {
    private static let launchCountKey = "app_launch_count"
    private static let firstLaunchDateKey = "first_launch_date"
    private static let hasSeenSecondaryOnboardingKey = "has_seen_secondary_onboarding"
    private static let onboardingDismissedKey = "onboarding_dismissed_permanently"

    @Published var launchCount: Int = 0
    @Published var shouldShowSecondaryOnboarding: Bool = false

    static let shared = OnboardingManager()

    // Trigger thresholds
    static let launchThreshold = 15  // Show after 15 launches
    static let dayThreshold = 5      // OR after 5 days

    private init() {
        loadSettings()
    }

    private func loadSettings() {
        // Load launch count
        launchCount = UserDefaults.standard.integer(forKey: UserDefaultsKeys.Onboarding.launchCount)

        // Set first launch date if not set
        if UserDefaults.standard.object(forKey: UserDefaultsKeys.Onboarding.firstLaunchDate) == nil {
            UserDefaults.standard.set(Date(), forKey: UserDefaultsKeys.Onboarding.firstLaunchDate)
        }

        // Check if should show secondary onboarding
        updateSecondaryOnboardingStatus()
    }

    func incrementLaunchCount() {
        launchCount += 1
        UserDefaults.standard.set(launchCount, forKey: UserDefaultsKeys.Onboarding.launchCount)
        updateSecondaryOnboardingStatus()
    }

    private func updateSecondaryOnboardingStatus() {
        // Don't show if already seen (ONE TIME EVER)
        let hasSeenOnboarding = UserDefaults.standard.bool(forKey: UserDefaultsKeys.Onboarding.hasSeenSecondaryOnboarding)

        // Don't show if permanently dismissed
        let isPermanentlyDismissed = UserDefaults.standard.bool(forKey: UserDefaultsKeys.Onboarding.onboardingDismissedPermanently)

        if hasSeenOnboarding || isPermanentlyDismissed {
            shouldShowSecondaryOnboarding = false
            return
        }

        // Check launch threshold
        if launchCount >= Self.launchThreshold {
            shouldShowSecondaryOnboarding = true
            return
        }

        // Check day threshold
        if let firstLaunchDate = UserDefaults.standard.object(forKey: UserDefaultsKeys.Onboarding.firstLaunchDate) as? Date {
            let daysSinceFirstLaunch = Calendar.current.dateComponents([.day], from: firstLaunchDate, to: Date()).day ?? 0
            if daysSinceFirstLaunch >= Self.dayThreshold {
                shouldShowSecondaryOnboarding = true
                return
            }
        }

        shouldShowSecondaryOnboarding = false
    }

    func markSecondaryOnboardingAsShown() {
        UserDefaults.standard.set(true, forKey: UserDefaultsKeys.Onboarding.hasSeenSecondaryOnboarding)
        shouldShowSecondaryOnboarding = false
    }

    func dismissSecondaryOnboardingPermanently() {
        UserDefaults.standard.set(true, forKey: UserDefaultsKeys.Onboarding.onboardingDismissedPermanently)
        shouldShowSecondaryOnboarding = false
    }

    func forceShowSecondaryOnboarding() {
        // For testing or "Feature Tour" button
        shouldShowSecondaryOnboarding = true
    }

    func resetOnboardingForTesting() {
        // Debugging/testing method
        UserDefaults.standard.removeObject(forKey: UserDefaultsKeys.Onboarding.launchCount)
        UserDefaults.standard.removeObject(forKey: UserDefaultsKeys.Onboarding.firstLaunchDate)
        UserDefaults.standard.removeObject(forKey: UserDefaultsKeys.Onboarding.hasSeenSecondaryOnboarding)
        UserDefaults.standard.removeObject(forKey: UserDefaultsKeys.Onboarding.onboardingDismissedPermanently)
        launchCount = 0
        shouldShowSecondaryOnboarding = false
        loadSettings()
    }

    // Debug info
    func getDebugInfo() -> String {
        let firstLaunchDate = UserDefaults.standard.object(forKey: UserDefaultsKeys.Onboarding.firstLaunchDate) as? Date ?? Date()
        let daysSinceFirstLaunch = Calendar.current.dateComponents([.day], from: firstLaunchDate, to: Date()).day ?? 0
        let hasSeenOnboarding = UserDefaults.standard.bool(forKey: UserDefaultsKeys.Onboarding.hasSeenSecondaryOnboarding)
        let isDismissed = UserDefaults.standard.bool(forKey: UserDefaultsKeys.Onboarding.onboardingDismissedPermanently)

        return """
        Launch Count: \(launchCount)/\(Self.launchThreshold)
        Days Since Install: \(daysSinceFirstLaunch)/\(Self.dayThreshold)
        Has Seen Onboarding: \(hasSeenOnboarding)
        Is Dismissed: \(isDismissed)
        Should Show: \(shouldShowSecondaryOnboarding)
        """
    }
}

// MARK: - What's New Manager
class WhatsNewManager: ObservableObject {
    private static let lastSeenVersionKey = "last_seen_app_version"

    @Published var shouldShowWhatsNew: Bool = false
    @Published var updatesToShow: [WhatsNewUpdate] = []

    static let shared = WhatsNewManager()

    // Define updates here - add new ones at the TOP when you push updates
    // Updates are shown in order: newest first
    private let updates: [WhatsNewUpdate] = [
        // Example for when you add expansions:
        // WhatsNewUpdate(
        //     version: "1.3.0",
        //     title: "New Feature Name",
        //     features: [
        //         WhatsNewFeature(icon: "star.fill", title: "Feature Title", description: "Feature description")
        //     ]
        // ),
        // WhatsNewUpdate(
        //     version: "1.2.0",
        //     title: "Previous Update",
        //     features: [
        //         WhatsNewFeature(icon: "sparkles", title: "Old Feature", description: "This will show below v1.3")
        //     ]
        // ),
        // WhatsNewUpdate(
        //     version: "1.1.0",
        //     title: "Question Expansions!",
        //     features: [
        //         WhatsNewFeature(icon: "purchased.circle.fill", title: "Expansion Packs", description: "Purchase themed question packs to expand your trivia library"),
        //         WhatsNewFeature(icon: "star.fill", title: "Premium Categories", description: "Access exclusive categories like Movies, TV Shows, and more")
        //     ]
        // )
    ]

    private init() {
        checkForNewVersion()
    }

    private func checkForNewVersion() {
        guard let currentVersion = Bundle.main.infoDictionary?["CFBundleShortVersionString"] as? String else {
            return
        }

        let lastSeenVersion = UserDefaults.standard.string(forKey: UserDefaultsKeys.WhatsNew.lastSeenVersion)

        // First launch ever or version changed
        if lastSeenVersion != currentVersion {
            // Check if current version has an update defined
            if updates.contains(where: { $0.version == currentVersion }) {
                // Show all available updates (running changelog)
                updatesToShow = updates
                shouldShowWhatsNew = true
            } else {
                // No update defined for this version - just mark as seen
                markCurrentVersionAsSeen()
            }
        }
    }

    func markCurrentVersionAsSeen() {
        if let currentVersion = Bundle.main.infoDictionary?["CFBundleShortVersionString"] as? String {
            UserDefaults.standard.set(currentVersion, forKey: UserDefaultsKeys.WhatsNew.lastSeenVersion)
        }
        shouldShowWhatsNew = false
        updatesToShow = []
    }

    func forceShowWhatsNew() {
        // For testing - show all updates
        if !updates.isEmpty {
            updatesToShow = updates
            shouldShowWhatsNew = true
        }
    }

    func resetForTesting() {
        UserDefaults.standard.removeObject(forKey: UserDefaultsKeys.WhatsNew.lastSeenVersion)
        checkForNewVersion()
    }
}

// MARK: - What's New Models
struct WhatsNewUpdate: Identifiable {
    let id = UUID()
    let version: String
    let title: String
    let features: [WhatsNewFeature]
}

struct WhatsNewFeature: Identifiable {
    let id = UUID()
    let icon: String
    let title: String
    let description: String
}

// MARK: - Expansion Pack Models
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

// MARK: - Expansion Pack Manager
class ExpansionPackManager: ObservableObject {
    static let shared = ExpansionPackManager()

    private static let purchasedPacksKey = "purchased_expansion_packs"
    private static let installedPacksKey = "installed_expansion_packs"

    @Published var availablePacks: [ExpansionPack] = []
    @Published var purchasedPackIds: Set<String> = []
    @Published var installedPackIds: Set<String> = []

    private init() {
        loadPurchasedPacks()
        loadInstalledPacks()
        loadAvailablePacks()
    }

    // MARK: - Load Available Packs
    func loadAvailablePacks() {
        availablePacks = []

        // Scan Resources folder for expansion_*.json files (only published packs)
        // Draft packs should use draft_*.json naming convention
        guard let resourcePath = Bundle.main.resourcePath else {
            print("Could not find resource path")
            return
        }

        let fileManager = FileManager.default

        // Check both root and "Expansion Packs" subdirectory
        let pathsToCheck = [
            resourcePath,
            (resourcePath as NSString).appendingPathComponent("Expansion Packs")
        ]

        do {
            for basePath in pathsToCheck {
                guard fileManager.fileExists(atPath: basePath) else { continue }

                let resourceContents = try fileManager.contentsOfDirectory(atPath: basePath)
                let expansionFiles = resourceContents.filter { $0.hasPrefix("expansion_") && $0.hasSuffix(".json") }

                for fileName in expansionFiles {
                    let filePath = (basePath as NSString).appendingPathComponent(fileName)

                    if let data = try? Data(contentsOf: URL(fileURLWithPath: filePath)) {
                        let decoder = JSONDecoder()
                        decoder.dateDecodingStrategy = .iso8601
                        if let pack = try? decoder.decode(ExpansionPack.self, from: data) {
                            // Only add packs that are marked as published
                            if pack.isPublished {
                                availablePacks.append(pack)
                                print("Loaded expansion pack: \(pack.packName)")
                            } else {
                                print("Skipping unpublished pack: \(pack.packName)")
                            }
                        } else {
                            print("Failed to decode expansion pack: \(fileName)")
                        }
                    }
                }
            }

            print("Loaded \(availablePacks.count) published expansion packs")
        } catch {
            print("Error loading expansion packs: \(error)")
        }
    }

    // MARK: - Purchase Management
    func isPurchased(packId: String) -> Bool {
        // Check bypass first - if active, all packs appear purchased
        if DeveloperBypassManager.shared.isBypassActive {
            return true
        }
        return purchasedPackIds.contains(packId)
    }

    func unlockPack(packId: String) {
        purchasedPackIds.insert(packId)
        savePurchasedPacks()
    }

    private func savePurchasedPacks() {
        let array = Array(purchasedPackIds)
        UserDefaults.standard.set(array, forKey: UserDefaultsKeys.Store.purchasedPacks)
    }

    private func loadPurchasedPacks() {
        if let array = UserDefaults.standard.array(forKey: UserDefaultsKeys.Store.purchasedPacks) as? [String] {
            purchasedPackIds = Set(array)
        }
    }

    // MARK: - Install Management
    func isInstalled(packId: String) -> Bool {
        return installedPackIds.contains(packId)
    }

    func installPack(packId: String) {
        guard isPurchased(packId: packId) else {
            print("Cannot install pack that is not purchased: \(packId)")
            return
        }
        installedPackIds.insert(packId)
        saveInstalledPacks()

        // Notify that expansion packs changed (triggers question reload & phobia rescan)
        NotificationCenter.default.post(name: .expansionPacksChanged, object: nil)
    }

    func uninstallPack(packId: String) {
        installedPackIds.remove(packId)
        saveInstalledPacks()

        // Notify that expansion packs changed (triggers question reload & phobia rescan)
        NotificationCenter.default.post(name: .expansionPacksChanged, object: nil)
    }

    private func saveInstalledPacks() {
        let array = Array(installedPackIds)
        UserDefaults.standard.set(array, forKey: UserDefaultsKeys.Store.installedPacks)
    }

    private func loadInstalledPacks() {
        if let array = UserDefaults.standard.array(forKey: UserDefaultsKeys.Store.installedPacks) as? [String] {
            installedPackIds = Set(array)
        }
    }

    // MARK: - Question Access
    func getInstalledQuestions() -> [TriviaQuestion] {
        var allQuestions: [TriviaQuestion] = []
        for pack in availablePacks where installedPackIds.contains(pack.packId) {
            allQuestions.append(contentsOf: pack.allQuestions)
        }
        return allQuestions
    }

    func getFreePreviewQuestions() -> [TriviaQuestion] {
        var allQuestions: [TriviaQuestion] = []
        for pack in availablePacks {
            allQuestions.append(contentsOf: pack.freePreviewQuestions)
        }
        return allQuestions
    }

    func getPurchasedPacks(for category: TriviaCategory) -> [ExpansionPack] {
        return availablePacks.filter { pack in
            isPurchased(packId: pack.packId) &&
            pack.allQuestions.contains { $0.category == category.rawValue }
        }
    }

    // MARK: - Single Topic Mode Support

    /// Checks if a pack is available for Single Topic Mode (either installed OR has free previews)
    func isAvailableForSingleTopicMode(packId: String) -> Bool {
        guard let pack = availablePacks.first(where: { $0.packId == packId }) else {
            return false
        }
        // Available if installed OR has preview questions
        return isInstalled(packId: packId) || !pack.freePreviewQuestions.isEmpty
    }

    /// Returns all packs available for Single Topic Mode (installed packs + packs with previews)
    func getAvailableTopicsForSingleTopicMode() -> [ExpansionPack] {
        return availablePacks.filter { pack in
            isInstalled(packId: pack.packId) || !pack.freePreviewQuestions.isEmpty
        }
    }

    /// Returns questions for a specific topic based on install state
    /// - If installed: returns all questions (previews + paid)
    /// - If not installed: returns only free preview questions
    func getQuestionsForTopic(packId: String) -> [TriviaQuestion] {
        guard let pack = availablePacks.first(where: { $0.packId == packId }) else {
            return []
        }

        if isInstalled(packId: packId) {
            // User has full pack installed
            return pack.allQuestions
        } else {
            // User only has preview access
            return pack.freePreviewQuestions
        }
    }

    /// Checks if user only has preview access to a pack (not purchased/installed)
    func hasOnlyPreviews(packId: String) -> Bool {
        return !isInstalled(packId: packId) && isAvailableForSingleTopicMode(packId: packId)
    }

    // MARK: - Display Name Mapping

    /// Maps topic/pack IDs to user-friendly display names
    /// Includes existing packs, draft packs, and future pack IDs
    private let topicDisplayNames: [String: String] = [
        // Existing expansion packs
        "com.fiz.pack.harry_potter": "Harry Potter",
        "com.fiz.pack.pokemon": "Pocket Monsters",
        "com.fiz.pack.the_office": "Dunder Mifflinfinity",
        "com.fiz.pack.disney": "Disney",
        "com.fiz.pack.80s_trivia": "80s Trivia",

        // Draft expansion packs
        "com.fiz.pack.marvel": "Marvel",
        "com.fiz.pack.pixar": "Pixar",

        // Future expansion packs - Sports
        "com.fiz.pack.baseball": "Baseball",
        "com.fiz.pack.basketball": "Basketball",
        "com.fiz.pack.boxing": "Boxing",
        "com.fiz.pack.football": "Football",
        "com.fiz.pack.golf": "Golf",
        "com.fiz.pack.hockey": "Hockey",
        "com.fiz.pack.olympics": "Olympics",
        "com.fiz.pack.soccer": "Soccer",
        "com.fiz.pack.tennis": "Tennis",

        // Future expansion packs - Other
        "com.fiz.pack.dc": "DC",
        "com.fiz.pack.star_wars": "Star Wars",
    ]

    /// Returns the user-friendly display name for a topic/pack ID
    /// - Parameter topicId: The pack ID (e.g., "com.fiz.pack.harry_potter")
    /// - Returns: Display name (e.g., "Harry Potter")
    func getDisplayName(for topicId: String) -> String {
        // First check if it's a loaded expansion pack (most reliable)
        if let pack = availablePacks.first(where: { $0.packId == topicId }) {
            return pack.packName
        }

        // Then check pre-defined display names (includes draft and future packs)
        if let displayName = topicDisplayNames[topicId] {
            return displayName
        }

        // Fallback: format the pack ID nicely
        return formatPackId(topicId)
    }

    /// Formats a pack ID into a readable name as fallback
    /// - Parameter packId: Pack ID like "com.fiz.pack.star_wars"
    /// - Returns: Formatted name like "Star Wars"
    private func formatPackId(_ packId: String) -> String {
        // Strip "com.fiz.pack." prefix
        let name = packId.replacingOccurrences(of: "com.fiz.pack.", with: "")
        // Replace underscores with spaces and capitalize
        return name.replacingOccurrences(of: "_", with: " ")
            .split(separator: " ")
            .map { $0.capitalized }
            .joined(separator: " ")
    }

    // MARK: - Base Game Question Counting

    /// Counts how many base game questions (from questions.json) have a specific topic
    /// Used to calculate total free questions available (base + preview)
    func countBaseGameQuestions(for packId: String) -> Int {
        guard let url = Bundle.main.url(forResource: "questions", withExtension: "json") else {
            return 0
        }

        do {
            let data = try Data(contentsOf: url)
            let jsonObject = try JSONSerialization.jsonObject(with: data, options: [])

            guard let jsonDict = jsonObject as? [String: Any],
                  let categories = jsonDict["categories"] as? [String: [[String: Any]]] else {
                return 0
            }

            var count = 0
            for (_, categoryQuestions) in categories {
                for questionDict in categoryQuestions {
                    if let topic = questionDict["topic"] as? String, topic == packId {
                        count += 1
                    }
                }
            }

            return count
        } catch {
            print("Failed to count base game questions: \(error)")
            return 0
        }
    }

    // MARK: - Testing Helpers
    func resetForTesting() {
        UserDefaults.standard.removeObject(forKey: UserDefaultsKeys.Store.purchasedPacks)
        UserDefaults.standard.removeObject(forKey: UserDefaultsKeys.Store.installedPacks)
        purchasedPackIds = []
        installedPackIds = []
    }
}

// MARK: - Developer Bypass Manager
class DeveloperBypassManager: ObservableObject {
    static let shared = DeveloperBypassManager()

    private static let bypassEnabledKey = "developer_bypass_enabled"

    @Published var isBypassActive: Bool = false

    private init() {
        loadBypassState()
    }

    private func loadBypassState() {
        isBypassActive = UserDefaults.standard.bool(forKey: UserDefaultsKeys.Developer.bypassEnabled)
    }

    func activateBypass() {
        isBypassActive = true
        UserDefaults.standard.set(true, forKey: UserDefaultsKeys.Developer.bypassEnabled)
        print("Developer bypass activated")
    }

    func deactivateBypass() {
        isBypassActive = false
        UserDefaults.standard.set(false, forKey: UserDefaultsKeys.Developer.bypassEnabled)
        print("Developer bypass deactivated")
    }
}
