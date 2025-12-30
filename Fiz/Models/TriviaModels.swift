import Foundation
import SwiftData
import UIKit

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
    case literature = "Literature"
    case music = "Music"
    case technology = "Technology"
    case art = "Art"
    case geography = "Geography"
    case sports = "Sports"
    case science = "Science"
    case nature = "Nature"
    case history = "History"
    case bible = "Bible"
    case food = "Food"

    var icon: String {
        switch self {
        case .entertainment: return "movieclapper.fill"
        case .literature: return "book.fill"
        case .music: return "music.note"
        case .technology: return "laptopcomputer"
        case .art: return "paintpalette.fill"
        case .geography: return "map.fill"
        case .sports: return "tennisball.fill"
        case .science: return "atom"
        case .nature: return "leaf.fill"
        case .history: return "building.columns.fill"
        case .bible: return "text.book.closed.fill"
        case .food: return "fork.knife.circle.fill"
        }
    }

    var color: String {
        switch self {
        // SATURATED (Primary/Secondary Colors)
        case .sports: return "#E63946"             // Red - energy, competition
        case .entertainment: return "#FFD60A"      // Yellow - bright, fun
        case .science: return "#0077B6"            // Blue - logic, precision
        case .food: return "#FF6B35"               // Orange - appetite, warmth
        case .nature: return "#2D6A4F"             // Green - natural (unchanged)
        case .bible: return "#7209B7"              // Purple - royalty, spirituality

        // DESATURATED (Pastel Colors)
        case .art: return "#FF8FA3"                // Coral - creative, soft
        case .history: return "#C9ADA7"            // Gold - aged, classic
        case .technology: return "#90E0EF"         // Cyan - modern, digital
        case .geography: return "#A68A64"          // Tan - earth tones
        case .music: return "#52B788"              // Mint - calm, harmony
        case .literature: return "#B8A0D9"         // Lavender - refined, literary
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
    var gameMode: String = "Regular" // "Regular", "Single Category", or "Single Topic" (future)
    var categoryName: String? = nil // Category name if in Single Category/Topic mode

    init(streak: Int, date: Date, gameMode: String = "Regular", categoryName: String? = nil) {
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
    var id: UUID

    init(questionId: String, questionText: String, correctAnswer: String, userAnswer: String, wasCorrect: Bool, category: String, subcategory: String?) {
        self.questionId = questionId
        self.questionText = questionText
        self.correctAnswer = correctAnswer
        self.userAnswer = userAnswer
        self.wasCorrect = wasCorrect
        self.timestamp = Date()
        self.category = category
        self.subcategory = subcategory
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
        if UserDefaults.standard.object(forKey: Self.hapticEnabledKey) != nil {
            isHapticEnabled = UserDefaults.standard.bool(forKey: Self.hapticEnabledKey)
        } else {
            isHapticEnabled = true
        }
    }

    func setHapticEnabled(_ enabled: Bool) {
        isHapticEnabled = enabled
        UserDefaults.standard.set(enabled, forKey: Self.hapticEnabledKey)
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
        if UserDefaults.standard.object(forKey: Self.correctPopupDurationKey) != nil {
            correctPopupDuration = UserDefaults.standard.double(forKey: Self.correctPopupDurationKey)
        } else {
            correctPopupDuration = 1.5
        }

        // Load incorrect popup duration (default 3.0)
        if UserDefaults.standard.object(forKey: Self.incorrectPopupDurationKey) != nil {
            incorrectPopupDuration = UserDefaults.standard.double(forKey: Self.incorrectPopupDurationKey)
        } else {
            incorrectPopupDuration = 3.0
        }
    }

    func setCorrectPopupDuration(_ duration: Double) {
        correctPopupDuration = duration
        UserDefaults.standard.set(duration, forKey: Self.correctPopupDurationKey)
    }

    func setIncorrectPopupDuration(_ duration: Double) {
        incorrectPopupDuration = duration
        UserDefaults.standard.set(duration, forKey: Self.incorrectPopupDurationKey)
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

// MARK: - Category Selection Manager
class CategorySelectionManager: ObservableObject {
    private static let selectedCategoriesKey = "selected_categories"

    @Published var selectedCategories: Set<TriviaCategory> = []

    static let shared = CategorySelectionManager()
    static let minimumCategories = 2
    static let maximumCategories = 12

    private init() {
        loadSettings()
    }

    private func loadSettings() {
        if let data = UserDefaults.standard.data(forKey: Self.selectedCategoriesKey),
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
            UserDefaults.standard.set(encoded, forKey: Self.selectedCategoriesKey)
        }
    }

    func toggleCategory(_ category: TriviaCategory) -> Bool {
        if selectedCategories.contains(category) {
            // Deselecting - check minimum
            if selectedCategories.count > Self.minimumCategories {
                // Check if this is the active single-category mode category
                if SingleCategoryModeManager.shared.isEnabled &&
                   SingleCategoryModeManager.shared.selectedCategory == category {
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

    private func setDefaultSelection() {
        // Default: Core 7 reorganized categories + Geography + Art
        selectedCategories = [
            .entertainment,
            .sports,
            .bible,
            .history,
            .science,
            .nature,
            .food,
            .geography,
            .art
        ]
        saveSettings()
    }

    func resetToDefault() {
        setDefaultSelection()
    }
}

// MARK: - Swipe Navigation Manager
class SwipeNavigationManager: ObservableObject {
    private static let swipeNavigationEnabledKey = "swipe_navigation_enabled"

    @Published var isSwipeNavigationEnabled: Bool = false

    static let shared = SwipeNavigationManager()

    private init() {
        loadSettings()
    }

    private func loadSettings() {
        // Default to false (opt-in for accessibility)
        if UserDefaults.standard.object(forKey: Self.swipeNavigationEnabledKey) != nil {
            isSwipeNavigationEnabled = UserDefaults.standard.bool(forKey: Self.swipeNavigationEnabledKey)
        } else {
            isSwipeNavigationEnabled = false
        }
    }

    func setSwipeNavigationEnabled(_ enabled: Bool) {
        isSwipeNavigationEnabled = enabled
        UserDefaults.standard.set(enabled, forKey: Self.swipeNavigationEnabledKey)
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
        if let data = UserDefaults.standard.data(forKey: Self.phobiasKey),
           let decoded = try? JSONDecoder().decode([Phobia].self, from: data) {
            phobias = decoded
        }
    }

    private func savePhobias() {
        if let encoded = try? JSONEncoder().encode(phobias) {
            UserDefaults.standard.set(encoded, forKey: Self.phobiasKey)
        }
    }

    // MARK: - Public Methods

    func addPhobia(term: String, in questions: [TriviaQuestion]) -> (phobia: Phobia, excludedCount: Int) {
        let normalizedTerm = term.lowercased().trimmingCharacters(in: .whitespacesAndNewlines)
        let searchTerms = getSearchTerms(for: normalizedTerm)
        let excludedIds = scanForMatches(searchTerms: searchTerms, in: questions)

        let phobia = Phobia(term: normalizedTerm, excludedQuestionIds: excludedIds)
        phobias.append(phobia)
        savePhobias()

        return (phobia, excludedIds.count)
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
