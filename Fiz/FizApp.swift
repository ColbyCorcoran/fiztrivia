//
//  FizApp.swift
//  Fiz
//
//  Created by Colby Corcoran on 8/12/25.
//

import SwiftUI
import SwiftData
import TipKit

@main
struct FizApp: App {
    @Environment(\.scenePhase) private var scenePhase
    @StateObject private var onboardingManager = OnboardingManager.shared
    @StateObject private var whatsNewManager = WhatsNewManager.shared

    var sharedModelContainer: ModelContainer = {
        let schema = Schema([
            LeaderboardEntry.self,
            QuestionHistoryEntry.self,
        ])
        let modelConfiguration = ModelConfiguration(schema: schema, isStoredInMemoryOnly: false)

        do {
            return try ModelContainer(for: schema, configurations: [modelConfiguration])
        } catch {
            fatalError("Could not create ModelContainer: \(error)")
        }
    }()

    init() {
        // Validate UserDefaults keys on app launch (debug builds only)
        UserDefaultsKeys.validateUniqueKeys()

        // Configure TipKit — tips show at most once per day, stored in app's default location
        try? Tips.configure([
            .displayFrequency(.immediate),
            .datastoreLocation(.applicationDefault)
        ])
    }

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(sharedModelContainer)
        .onChange(of: scenePhase) { oldPhase, newPhase in
            switch newPhase {
            case .active:
                // Track analytics
                AnalyticsManager.shared.trackAppOpened()

                // Increment launch count only on genuine foreground transitions
                // (background → active), not on every activation (e.g. dismissing Control Center)
                if oldPhase == .background {
                    onboardingManager.incrementLaunchCount()
                }
            case .background:
                AnalyticsManager.shared.trackAppBackgrounded()
            case .inactive:
                break
            @unknown default:
                break
            }
        }
    }
}
