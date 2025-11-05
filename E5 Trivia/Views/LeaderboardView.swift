import SwiftUI
import SwiftData

struct LeaderboardView: View {
    @Bindable var gameViewModel: GameViewModel
    @StateObject private var userManager = UserManager.shared
    @Environment(\.modelContext) private var modelContext
    @Query(sort: [
        SortDescriptor(\LeaderboardEntry.streak, order: .reverse),
        SortDescriptor(\LeaderboardEntry.date, order: .reverse)
    ]) 
    private var leaderboardEntries: [LeaderboardEntry]
    
    private var recentEntries: [LeaderboardEntry] {
        Array(leaderboardEntries.prefix(15))
    }
    
    var body: some View {
        ZStack {
            LinearGradient(
                colors: [Color(hex: "#f3eddf"), Color(hex: "#e8dcc8")],
                startPoint: .topLeading,
                endPoint: .bottomTrailing
            )
            .ignoresSafeArea()
            
            VStack(spacing: 0) {
                // Top toolbar
                HStack {
                    Button("Done") {
                        gameViewModel.continueGame()
                    }
                    .font(.headline)
                    .foregroundColor(.primary)
                    
                    Spacer()
                }
                .padding(.horizontal, 20)
                .padding(.top, 10)
                .frame(height: 50)
                
                VStack(spacing: 15) {
                // Header with Fiz
                HStack(spacing: 16) {
                    Image("fiz-leaderboard")
                        .resizable()
                        .scaledToFit()
                        .frame(width: 120, height: 120)

                    VStack(alignment: .leading, spacing: 4) {
                        Text("Top Answer")
                            .font(.title)
                            .fontWeight(.bold)
                            .foregroundColor(.primary)
                        Text("Streaks")
                            .font(.title)
                            .fontWeight(.bold)
                            .foregroundColor(.primary)
                    }
                    .frame(maxWidth: .infinity, alignment: .leading)
                }
                .frame(maxWidth: .infinity)
                .padding(.horizontal, 20)
                
                // Leaderboard list - fixed height container
                ZStack {
                    if recentEntries.isEmpty {
                        VStack(spacing: 20) {
                            Text("No streaks yet!")
                                .font(.title2)
                                .foregroundColor(.secondary)
                            
                            Text("Start playing to see your best streaks here")
                                .font(.body)
                                .foregroundColor(.secondary)
                                .multilineTextAlignment(.center)
                        }
                        .frame(maxHeight: .infinity)
                    } else {
                        ScrollView {
                            LazyVStack(spacing: 12) {
                                ForEach(Array(recentEntries.enumerated()), id: \.element.id) { index, entry in
                                    LeaderboardRow(
                                        rank: index + 1,
                                        entry: entry,
                                        isTopThree: index < 3
                                    )
                                }
                            }
                            .padding(.horizontal)
                            .padding(.top, 8)
                        }
                    }
                }
                .frame(height: 450)
                
                Spacer(minLength: 20)
                
                // Current streak display
                HStack(spacing: 8) {
                    Text("\(userManager.displayName)'s Current Streak:")
                        .font(.subheadline)
                        .foregroundColor(Color(hex: "#533214"))

                    Text("\(gameViewModel.gameSession.currentStreak)")
                        .font(.title2)
                        .fontWeight(.bold)
                        .foregroundColor(Color(hex: "#39766d"))
                }
                .padding(.horizontal, 16)
                .padding(.vertical, 12)
                .background(Color(hex: "#39766d").opacity(0.2))
                .cornerRadius(12)
                .shadow(color: Color(hex: "#533214").opacity(0.15), radius: 3, x: 0, y: 1)
                
                Spacer(minLength: 20)
                }
                .padding()
            }
        }
    }
}

struct LeaderboardRow: View {
    let rank: Int
    let entry: LeaderboardEntry
    let isTopThree: Bool

    private var rankIcon: String {
        switch rank {
        case 1: return "🥇"
        case 2: return "🥈"
        case 3: return "🥉"
        default: return "#\(rank)"
        }
    }

    private var backgroundColor: Color {
        switch rank {
        case 1: return Color(hex: "#f3d29d").opacity(0.6)
        case 2: return Color(hex: "#b1aea5").opacity(0.4)
        case 3: return Color(hex: "#d48c20").opacity(0.4)
        default: return Color(hex: "#e8dcc8").opacity(0.5)
        }
    }

    private var streakIcon: String {
        switch entry.streak {
        case 1...2: return "⭐"
        case 3...4: return "🌟"
        case 5...9: return "🔥"
        case 10...14: return "🔥🔥"
        default: return "💯" // 15+
        }
    }
    
    var body: some View {
        HStack(spacing: 15) {
            // Rank
            Text(rankIcon)
                .font(isTopThree ? .title2 : .headline)
                .frame(width: 40)
            
            // Streak
            VStack(alignment: .leading, spacing: 2) {
                Text("\(entry.streak) correct answer\(entry.streak == 1 ? "" : "s")")
                    .font(.headline)
                    .fontWeight(.semibold)
                    .foregroundColor(.primary)
                
                Text(entry.date, format: .dateTime.month().day().year())
                    .font(.caption)
                    .foregroundColor(.secondary)
            }
            
            Spacer()

            // Dynamic streak icon based on achievement level
            Text(streakIcon)
                .font(.title3)
        }
        .padding()
        .background(backgroundColor)
        .cornerRadius(12)
        .shadow(color: Color(hex: "#533214").opacity(0.1), radius: 2, x: 0, y: 1)
    }
}

#Preview {
    LeaderboardView(gameViewModel: GameViewModel())
        .modelContainer(for: LeaderboardEntry.self, inMemory: true)
}
