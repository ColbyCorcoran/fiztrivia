import Foundation

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
