//
//  StreakPersistenceManager.swift
//  Fiz
//
//  Extracted from TriviaModels.swift
//

import Foundation

/// Manages persistent storage of current streak across app sessions
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
