//
//  WhatsNewManager.swift
//  Fiz
//
//  Extracted from TriviaModels.swift
//

import Foundation

/// Manages "What's New" feature state and version-based update announcements
class WhatsNewManager: ObservableObject {
    private static let lastSeenVersionKey = "last_seen_app_version"

    @Published var shouldShowWhatsNew: Bool = false
    @Published var updatesToShow: [WhatsNewUpdate] = []

    static let shared = WhatsNewManager()

    // Define updates here - add new ones at the TOP when you push updates
    // Updates are shown in order: newest first
    private let updates: [WhatsNewUpdate] = [
        WhatsNewUpdate(
            version: "1.2.5",
            title: "Smarter, Smoother, Better",
            features: [
                WhatsNewFeature(icon: "circle.grid.cross.left.filled", title: "Quick Mode Switch", description: "Tap the Mode badge on the wheel view to instantly switch game modes without diving into settings."),
                WhatsNewFeature(icon: "lightbulb.fill", title: "Helpful Tips", description: "First-time tips now appear on the wheel view and in settings to help you discover features you might have missed."),
                WhatsNewFeature(icon: "chart.line.uptrend.xyaxis", title: "Single Topic Progress", description: "Game Progress now tracks your completion when playing in Single Topic mode."),
                WhatsNewFeature(icon: "sparkles", title: "What's New Redesign", description: "This view got a cleaner look with version headers and a more readable layout.")
            ]
        ),
        WhatsNewUpdate(
            version: "1.2.4",
            title: "More New Packs!",
            features: [
                WhatsNewFeature(icon: "ring", title: "Lord of the Rings", description: "One pack to rule them all — 500 questions across Middle-earth."),
                WhatsNewFeature(icon: "flame.fill", title: "Survivor", description: "Outwit, Outplay, Outlast — 400 questions spanning all eras of the show."),
                WhatsNewFeature(icon: "cup.and.saucer.fill", title: "Friends", description: "Could this pack BE any better? 400 questions about Central Perk and beyond."),
                WhatsNewFeature(icon: "desktopcomputer", title: "Apple", description: "Think different — 300 questions about Apple's products, people, and history.")
            ]
        ),
        WhatsNewUpdate(
            version: "1.2.3",
            title: "New Expansion Packs",
            features: [
                WhatsNewFeature(icon: "crown.fill", title: "Narnia", description: "Step through the wardrobe — 400 questions from Aslan's world."),
                WhatsNewFeature(icon: "wrench.adjustable.fill", title: "Super Mario", description: "Let's-a go! 500 questions about the Mushroom Kingdom and beyond."),
                WhatsNewFeature(icon: "tv.fill", title: "90s Trivia", description: "All that and a bag of chips — 400 questions about the totally rad nineties.")
            ]
        ),
        WhatsNewUpdate(
            version: "1.2.2",
            title: "Smoother Navigation",
            features: [
                WhatsNewFeature(icon: "hand.draw", title: "Swipe to Navigate", description: "Swipe left or right anywhere to move between the wheel, leaderboard, and settings.")
            ]
        ),
        WhatsNewUpdate(
            version: "1.2.0",
            title: "Expansion Packs Are Here!",
            features: [
                WhatsNewFeature(icon: "bag.fill", title: "In-App Store", description: "Browse and purchase themed question packs directly inside Fiz."),
                WhatsNewFeature(icon: "wand.and.stars", title: "Harry Potter", description: "500 questions spanning all seven books and the wizarding world."),
                WhatsNewFeature(icon: "circle.circle.fill", title: "Pokémon", description: "Gotta answer 'em all — 500 questions across every generation."),
                WhatsNewFeature(icon: "headphones", title: "80s Trivia", description: "Totally tubular — 400 questions about the most radical decade."),
                WhatsNewFeature(icon: "sparkles", title: "Disney", description: "The most magical trivia on Earth — 500 questions across the Disney universe."),
                WhatsNewFeature(icon: "lamp.desk.fill", title: "Pixar", description: "From Toy Story to Elemental — 400 questions about Lamp Light Animation."),
                WhatsNewFeature(icon: "briefcase.fill", title: "The Office", description: "That's what she said — 300 questions about Dunder Mifflin and its finest employees."),
                WhatsNewFeature(icon: "scope", title: "Single Topic Mode", description: "Dive deep into one expansion pack topic and play all the way through.")
            ]
        ),
        WhatsNewUpdate(
            version: "1.1.0",
            title: "Personalization & Game Modes",
            features: [
                WhatsNewFeature(icon: "app.badge", title: "Custom App Icons", description: "Choose from 6 unique Fiz icons to make the app your own."),
                WhatsNewFeature(icon: "gamecontroller.fill", title: "Game Modes", description: "Mix categories in Multi-Category mode or drill down with Single Category focus."),
                WhatsNewFeature(icon: "eye.slash", title: "Phobia Filters", description: "Exclude topics you'd rather skip — spiders, heights, and more.")
            ]
        ),
        WhatsNewUpdate(
            version: "1.0.0",
            title: "Welcome to Fiz!",
            features: [
                WhatsNewFeature(icon: "arrow.2.circlepath", title: "Spin the Wheel", description: "Pull to spin and land on a category — trivia is just a flick away."),
                WhatsNewFeature(icon: "speedometer", title: "Difficulty Modes", description: "Play Casual, Normal, or Difficult — filter questions to match your comfort level."),
                WhatsNewFeature(icon: "trophy.fill", title: "Streaks & Leaderboard", description: "Build answer streaks and track your best scores across every category.")
            ]
        )
    ]

    var allUpdates: [WhatsNewUpdate] { updates }

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
