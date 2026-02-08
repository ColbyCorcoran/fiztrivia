//
//  DifficultyManager.swift
//  Fiz
//
//  Extracted from TriviaModels.swift
//

import Foundation

// MARK: - Difficulty Manager
class DifficultyManager: ObservableObject {
    @Published var selectedDifficulty: DifficultyMode = .normal

    static let shared = DifficultyManager()

    private init() {
        loadSelectedDifficulty()
    }

    private func loadSelectedDifficulty() {
        if let saved = UserDefaults.standard.string(forKey: UserDefaultsKeys.Game.selectedDifficulty),
           let difficulty = DifficultyMode(rawValue: saved) {
            selectedDifficulty = difficulty
        }
    }

    func setDifficulty(_ difficulty: DifficultyMode) {
        selectedDifficulty = difficulty
        UserDefaults.standard.set(difficulty.rawValue, forKey: UserDefaultsKeys.Game.selectedDifficulty)
    }
}
