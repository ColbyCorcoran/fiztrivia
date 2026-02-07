import Foundation
import SwiftUI

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
