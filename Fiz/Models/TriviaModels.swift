//
//  TriviaModels.swift
//  Fiz
//
//  Refactored on 2026-02-07 during code review
//  This file now serves as a central import point and contains only the NotificationCenter extension
//
//  All models, enums, protocols, and managers have been extracted to separate files:
//
//  Core Models (Models/Core/):
//  - TriviaQuestion.swift
//  - TriviaCategory.swift
//  - LeaderboardEntry.swift
//  - QuestionHistoryEntry.swift
//  - GameSession.swift
//  - Phobia.swift
//  - ExpansionPack.swift
//  - WhatsNewModels.swift
//
//  Enums (Models/Enums/):
//  - GameEnums.swift (GameState, AnswerState, DifficultyMode, GameMode)
//
//  Protocols (Protocols/):
//  - TriviaSubcategories.swift (TriviaSubcategory protocol + all 12 category subcategories)
//
//  Managers (Managers/):
//  - UserManager.swift
//  - StreakPersistenceManager.swift
//  - DifficultyManager.swift
//  - AnsweredQuestionsManager.swift
//  - GameModeManager.swift
//  - HapticSettingsManager.swift
//  - PopupDurationManager.swift
//  - AppIconManager.swift
//  - CategorySelectionManager.swift
//  - SwipeNavigationManager.swift
//  - PhobiaExclusionManager.swift
//  - OnboardingManager.swift
//  - WhatsNewManager.swift
//  - ExpansionPackManager.swift
//  - DeveloperBypassManager.swift
//

import Foundation

// MARK: - Notification Names

extension Notification.Name {
    /// Posted when expansion packs are installed or uninstalled
    static let expansionPacksChanged = Notification.Name("expansionPacksChanged")
}
