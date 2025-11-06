//
//  ContentView.swift
//  Fiz
//
//  Created by Colby Corcoran on 8/12/25.
//

import SwiftUI
import SwiftData

struct ContentView: View {
    @State private var gameViewModel = GameViewModel()
    @StateObject private var userManager = UserManager.shared
    
    var body: some View {
        Group {
            if !userManager.hasCompletedOnboarding {
                OnboardingView()
            } else {
                gameView
            }
        }
        .animation(.easeInOut(duration: 0.3), value: userManager.hasCompletedOnboarding)
    }
    
    private var gameView: some View {
        Group {
            switch gameViewModel.gameState {
            case .selectingCategory:
                CategoryWheelView(gameViewModel: gameViewModel)
                
            case .leaderboard:
                LeaderboardView(gameViewModel: gameViewModel)
                
            case .settings:
                SettingsView(gameViewModel: gameViewModel)
            }
        }
        .animation(.easeInOut(duration: 0.3), value: gameViewModel.gameState)
    }
}

#Preview {
    ContentView()
        .modelContainer(for: LeaderboardEntry.self, inMemory: true)
}
