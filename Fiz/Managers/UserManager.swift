//
//  UserManager.swift
//  Fiz
//
//  Extracted from TriviaModels.swift on 2026-02-07
//  Manages user personalization including username and onboarding state
//

import Foundation
import Combine

// MARK: - User Management
class UserManager: ObservableObject {
    @Published var username: String = ""
    @Published var hasCompletedOnboarding: Bool = false

    static let shared = UserManager()

    private init() {
        loadUserData()
    }

    private func loadUserData() {
        username = UserDefaults.standard.string(forKey: UserDefaultsKeys.User.username) ?? ""
        hasCompletedOnboarding = UserDefaults.standard.bool(forKey: UserDefaultsKeys.User.hasCompletedOnboarding)
    }

    /// Sanitizes and saves the username with validation
    /// - Parameter name: Raw username input from user
    /// - Returns: True if username was saved, false if validation failed
    @discardableResult
    func saveUsername(_ name: String) -> Bool {
        let sanitized = sanitizeUsername(name)

        // Allow empty username (falls back to "Player")
        username = sanitized
        UserDefaults.standard.set(username, forKey: UserDefaultsKeys.User.username)

        if !hasCompletedOnboarding {
            hasCompletedOnboarding = true
            UserDefaults.standard.set(true, forKey: UserDefaultsKeys.User.hasCompletedOnboarding)
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
