//
//  PopupDurationManager.swift
//  Fiz
//
//  Extracted from TriviaModels.swift
//

import Foundation

/// Manages customizable popup durations for correct/incorrect answer feedback
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
