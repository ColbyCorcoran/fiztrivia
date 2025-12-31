import Foundation
import SwiftUI
import SwiftData

@Observable
class GameViewModel {
    var gameState: GameState = .selectingCategory
    var gameSession = GameSession()
    var questions: [TriviaQuestion] = []
    var wheelRotation: Double = 0
    var isSpinning = false
    var showCompletionCelebration = false
    var showSingleCategoryCompletionAlert = false
    var showPreviewPackCompletionAlert = false
    var completedPreviewPackId: String?

    private var usedQuestions: Set<String> = []
    private let difficultyManager = DifficultyManager.shared
    private let answeredQuestionsManager = AnsweredQuestionsManager.shared
    private let gameModeManager = GameModeManager.shared
    private let phobiaManager = PhobiaExclusionManager.shared

    init() {
        loadQuestions()

        // Listen for expansion pack changes to reload questions and rescan phobia filters
        NotificationCenter.default.addObserver(
            forName: .expansionPacksChanged,
            object: nil,
            queue: .main
        ) { [weak self] _ in
            self?.loadQuestions()
        }
    }

    deinit {
        NotificationCenter.default.removeObserver(self)
    }
    
    func loadQuestions() {
        guard let url = Bundle.main.url(forResource: "questions", withExtension: "json") else {
            print("Failed to find questions.json file")
            return
        }

        do {
            let data = try Data(contentsOf: url)
            let jsonObject = try JSONSerialization.jsonObject(with: data, options: [])

            guard let jsonDict = jsonObject as? [String: Any],
                  let categories = jsonDict["categories"] as? [String: [[String: Any]]] else {
                print("Invalid JSON structure")
                return
            }

            var allQuestions: [TriviaQuestion] = []

            for (categoryName, categoryQuestions) in categories {
                for questionDict in categoryQuestions {
                    if let question = questionDict["question"] as? String,
                       let options = questionDict["options"] as? [String],
                       let correctAnswer = questionDict["correct_answer"] as? String {

                        let id = questionDict["id"] as? String
                        let subcategory = questionDict["subcategory"] as? String
                        let difficulty = questionDict["difficulty"] as? String ?? "Medium"
                        let topic = questionDict["topic"] as? String
                        let subtopic = questionDict["subtopic"] as? String

                        let triviaQuestion = TriviaQuestion(
                            id: id,
                            category: categoryName,
                            subcategory: subcategory,
                            topic: topic,
                            subtopic: subtopic,
                            question: question,
                            options: options,
                            correctAnswer: correctAnswer,
                            difficulty: difficulty
                        )
                        allQuestions.append(triviaQuestion)
                    }
                }
            }

            // Add expansion pack questions (free previews + installed packs)
            let expansionQuestions = ExpansionPackManager.shared.getFreePreviewQuestions() +
                                   ExpansionPackManager.shared.getInstalledQuestions()
            allQuestions.append(contentsOf: expansionQuestions)

            questions = allQuestions
            print("Successfully loaded \(questions.count) questions from database (including \(expansionQuestions.count) expansion questions)")

            // Rescan phobia filters to catch any new questions (e.g., from newly installed expansion packs)
            phobiaManager.rescanAllPhobias(in: allQuestions)

        } catch {
            print("Failed to parse JSON: \(error)")
            createSampleQuestions()
        }
    }
    
    private func createSampleQuestions() {
        print("Creating sample questions as fallback")
        questions = [
            TriviaQuestion(
                id: "ent_sample_001",
                category: "Entertainment",
                subcategory: "Movies",
                question: "Who directed the movie 'Jaws'?",
                options: ["Steven Spielberg", "George Lucas", "Martin Scorsese", "Francis Ford Coppola"],
                correctAnswer: "Steven Spielberg",
                difficulty: "Medium"
            ),
            TriviaQuestion(
                id: "sci_sample_001",
                category: "Science",
                subcategory: "Physics",
                question: "What is the chemical symbol for gold?",
                options: ["Go", "Gd", "Au", "Ag"],
                correctAnswer: "Au",
                difficulty: "Easy"
            ),
            TriviaQuestion(
                id: "spt_sample_001",
                category: "Sports",
                subcategory: "Football",
                question: "How many players are on a football team on the field at once?",
                options: ["10", "11", "12", "13"],
                correctAnswer: "11",
                difficulty: "Easy"
            )
        ]
        print("Created \(questions.count) sample questions")
    }
    
    func startGame() {
        gameSession = GameSession()
        usedQuestions.removeAll()
        gameState = .selectingCategory
    }
    
    
    
    func loadRandomQuestion() {
        guard let category = gameSession.selectedCategory else { return }
        
        let categoryQuestions = questions.filter { question in
            question.category == category.rawValue &&
            !usedQuestions.contains(question.id) &&
            !answeredQuestionsManager.isQuestionAnswered(question.id) &&
            difficultyManager.selectedDifficulty.shouldInclude(questionDifficulty: question.difficulty) &&
            !phobiaManager.isQuestionExcluded(question.id)
        }
        
        guard let randomQuestion = categoryQuestions.randomElement() else {
            print("No more unanswered questions available for category: \(category.rawValue) with difficulty: \(difficultyManager.selectedDifficulty.rawValue)")
            return
        }
        
        gameSession.currentQuestion = randomQuestion
        gameSession.answerState = .unanswered
    }
    
    func selectAnswer(_ answer: String, modelContext: ModelContext? = nil) {
        guard let question = gameSession.currentQuestion else { return }
        
        usedQuestions.insert(question.id)
        answeredQuestionsManager.markQuestionAnswered(question.id)
        
        if answer == question.correctAnswer {
            gameSession.answerState = .correct
            gameSession.currentStreak += 1

            // Track streak milestones (10, 25, 50, 100)
            let milestones = [10, 25, 50, 100]
            if milestones.contains(gameSession.currentStreak) {
                AnalyticsManager.shared.trackStreakMilestoneReached(streakValue: gameSession.currentStreak)
            }

            HapticManager.shared.correctAnswerEffect()
        } else {
            gameSession.answerState = .incorrect
            // Save the current streak before resetting if it's > 0
            if gameSession.currentStreak > 0, let context = modelContext {
                // Determine game mode and category for this streak
                let gameMode: String
                let categoryName: String?

                if gameModeManager.isSingleCategoryMode {
                    gameMode = "Single Category"
                    categoryName = gameModeManager.selectedCategory?.rawValue
                } else {
                    gameMode = "Regular"
                    categoryName = nil
                }

                let entry = LeaderboardEntry(
                    streak: gameSession.currentStreak,
                    date: Date(),
                    gameMode: gameMode,
                    categoryName: categoryName
                )
                context.insert(entry)
                
                do {
                    try context.save()
                    print("Automatically saved streak to leaderboard: \(gameSession.currentStreak)")

                    // Track streak saved to leaderboard
                    AnalyticsManager.shared.trackStreakSavedToLeaderboard(
                        streakValue: gameSession.currentStreak,
                        gameMode: gameMode,
                        category: categoryName
                    )

                    // Clear the persistent streak since it's now saved to leaderboard
                    gameSession.currentStreak = 0
                    StreakPersistenceManager.clearCurrentStreak()

                } catch {
                    print("Failed to auto-save streak: \(error)")
                    // Still reset the streak even if save failed
                    gameSession.currentStreak = 0
                    StreakPersistenceManager.clearCurrentStreak()
                }
            } else {
                // No streak to save, just reset
                gameSession.currentStreak = 0
                StreakPersistenceManager.clearCurrentStreak()
            }
            HapticManager.shared.incorrectAnswerEffect()
        }
        
        // Check if all questions have been answered
        checkForCompletion()
    }
    
    
    func continueGame() {
        gameState = .selectingCategory
    }
    
    func showLeaderboard() {
        gameState = .leaderboard
    }
    
    func showSettings() {
        gameState = .settings
    }
    
    
    var randomCongratulatoryMessage: String {
        return UserManager.shared.personalizedCongratulatoryMessage()
    }
    
    var randomEncouragingMessage: String {
        return UserManager.shared.personalizedEncouragingMessage()
    }
    
    private func checkForCompletion() {
        // Check for preview pack completion in Single Topic Mode (highest priority)
        if gameModeManager.isSingleTopicMode,
           let selectedTopic = gameModeManager.selectedTopic,
           ExpansionPackManager.shared.hasOnlyPreviews(packId: selectedTopic) {

            // Count questions from this topic that match difficulty and aren't excluded by phobias
            let topicQuestions = questions.filter { question in
                question.topic == selectedTopic &&
                difficultyManager.selectedDifficulty.shouldInclude(questionDifficulty: question.difficulty) &&
                !phobiaManager.isQuestionExcluded(question.id)
            }

            // Check if all topic questions are answered
            let allAnswered = topicQuestions.allSatisfy { answeredQuestionsManager.isQuestionAnswered($0.id) }

            if allAnswered && !topicQuestions.isEmpty {
                print("🎉 Preview pack (\(selectedTopic)) completed! Showing upgrade prompt.")
                completedPreviewPackId = selectedTopic
                showPreviewPackCompletionAlert = true
                HapticManager.shared.correctAnswerEffect()
                return
            }
        }

        // Check for single category mode completion
        if gameModeManager.isSingleCategoryMode,
           let selectedCategory = gameModeManager.selectedCategory,
           answeredQuestionsManager.areAllCategoryQuestionsAnswered(selectedCategory.rawValue, in: questions, difficultyMode: difficultyManager.selectedDifficulty) {
            print("🎉 Single category (\(selectedCategory.rawValue)) completed! Showing alert.")
            showSingleCategoryCompletionAlert = true
            HapticManager.shared.correctAnswerEffect()
            return
        }

        // Check for overall completion (all questions in all categories)
        if answeredQuestionsManager.areAllQuestionsAnswered(in: questions, difficultyMode: difficultyManager.selectedDifficulty) {
            print("🎉 All questions completed! Showing celebration.")
            showCompletionCelebration = true
            HapticManager.shared.correctAnswerEffect()
        }
    }
    
    func resetAllProgress() {
        answeredQuestionsManager.resetAllAnswered()
        usedQuestions.removeAll()
        showCompletionCelebration = false
        gameSession.currentQuestion = nil
        gameSession.answerState = .unanswered
        print("All progress reset - ready to play again!")
    }
    
    func getTotalQuestionsCount() -> Int {
        return questions.filter {
            difficultyManager.selectedDifficulty.shouldInclude(questionDifficulty: $0.difficulty) &&
            !phobiaManager.isQuestionExcluded($0.id)
        }.count
    }

    func getAnsweredQuestionsCount() -> Int {
        let availableQuestions = questions.filter {
            difficultyManager.selectedDifficulty.shouldInclude(questionDifficulty: $0.difficulty) &&
            !phobiaManager.isQuestionExcluded($0.id)
        }
        return availableQuestions.filter { answeredQuestionsManager.isQuestionAnswered($0.id) }.count
    }
    
    func getCategoryProgress(_ category: TriviaCategory) -> (answered: Int, total: Int) {
        let answered = answeredQuestionsManager.getAnsweredCountForCategory(category.rawValue, in: questions, difficultyMode: difficultyManager.selectedDifficulty)
        let total = answeredQuestionsManager.getTotalQuestionsForCategory(category.rawValue, in: questions, difficultyMode: difficultyManager.selectedDifficulty)
        return (answered, total)
    }
}
