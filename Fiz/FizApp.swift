//
//  FizApp.swift
//  Fiz
//
//  Created by Colby Corcoran on 8/12/25.
//

import SwiftUI
import SwiftData

@main
struct FizApp: App {
    @Environment(\.scenePhase) private var scenePhase

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

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(sharedModelContainer)
        .onChange(of: scenePhase) { oldPhase, newPhase in
            switch newPhase {
            case .active:
                AnalyticsManager.shared.trackAppOpened()
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
