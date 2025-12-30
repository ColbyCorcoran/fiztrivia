import SwiftUI
import SwiftData

struct LeaderboardView: View {
    @Bindable var gameViewModel: GameViewModel
    var onSwipe: ((SwipeDirection, CGFloat) -> Void)? = nil
    @StateObject private var userManager = UserManager.shared
    @StateObject private var swipeNavigationManager = SwipeNavigationManager.shared
    @Environment(\.modelContext) private var modelContext
    @Environment(\.sizeCategory) private var sizeCategory
    @Query(sort: [
        SortDescriptor(\LeaderboardEntry.streak, order: .reverse),
        SortDescriptor(\LeaderboardEntry.date, order: .reverse)
    ])
    private var leaderboardEntries: [LeaderboardEntry]

    @State private var swipeTranslation: CGFloat = 0
    
    private var recentEntries: [LeaderboardEntry] {
        Array(leaderboardEntries.prefix(15))
    }
    
    var body: some View {
        ZStack {
            LinearGradient(
                colors: [Color.fizBackground, Color.fizBackgroundSecondary],
                startPoint: .topLeading,
                endPoint: .bottomTrailing
            )
            .ignoresSafeArea()

            VStack(spacing: 0) {
                // Top toolbar - checkmark visible at ALL sizes
                HStack {
                    Button(action: {
                        gameViewModel.continueGame()
                    }) {
                        Image(systemName: "checkmark")
                            .font(.title3.weight(.semibold))
                    }
                    .glassButtonStyle()
                    .controlSize(.large)
                    .tint(.fizTeal)
                    .triviaAccessibility(
                        label: "Return to game",
                        hint: "Tap to continue playing",
                        traits: .isButton
                    )

                    Spacer()
                }
                .padding(.horizontal, 10)
//                .padding(.top, 10)
                .frame(height: 44)

                // FIXED Header with Fiz - outside ScrollView
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
                            .lineLimit(sizeCategory.isAccessibilitySize ? nil : 1)
                            .fixedSize(horizontal: false, vertical: sizeCategory.isAccessibilitySize)
                        Text("Streaks")
                            .font(.title)
                            .fontWeight(.bold)
                            .foregroundColor(.primary)
                            .lineLimit(sizeCategory.isAccessibilitySize ? nil : 1)
                            .fixedSize(horizontal: false, vertical: sizeCategory.isAccessibilitySize)
                    }
                    .frame(maxWidth: .infinity, alignment: .leading)
                }
                .frame(maxWidth: .infinity)
                .padding(.horizontal, 20)
                .padding(.bottom, 15)

                // Leaderboard list - flexible height, scrollable
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
                            .padding(.bottom, 16)
                        }
                    }
                }
                .frame(maxHeight: .infinity)

                // Current streak display - fixed at bottom
                VStack(spacing: 8) {
                    Text("\(userManager.displayName)'s Current Streak:")
                        .font(.subheadline)
                        .foregroundColor(Color.fizBrown)
                        .lineLimit(sizeCategory.isAccessibilitySize ? nil : 1)
                        .multilineTextAlignment(.center)
                        .fixedSize(horizontal: false, vertical: sizeCategory.isAccessibilitySize)

                    Text("\(gameViewModel.gameSession.currentStreak)")
                        .font(.title2)
                        .fontWeight(.bold)
                        .foregroundColor(Color.fizTeal)
                }
                .padding(.horizontal, 16)
                .padding(.vertical, 12)
                .background(Color.fizTeal.opacity(0.2))
                .cornerRadius(12)
                .shadow(color: Color.fizBrown.opacity(0.15), radius: 3, x: 0, y: 1)
                .padding(.horizontal, 20)
                .padding(.vertical, 20)
            }
        }
        .gesture(leaderboardSwipeGesture)
    }

    private var leaderboardSwipeGesture: some Gesture {
        DragGesture()
            .onChanged { value in
                guard swipeNavigationManager.isSwipeNavigationEnabled else { return }

                swipeTranslation = value.translation.width
                onSwipe?(.left, swipeTranslation)
            }
            .onEnded { value in
                guard swipeNavigationManager.isSwipeNavigationEnabled else {
                    swipeTranslation = 0
                    onSwipe?(.left, 0)
                    return
                }

                let distance = value.translation.width

                // Check threshold: 120pt minimum distance
                // From leaderboard, only swipe left goes back to main
                if distance < -120 {
                    HapticManager.shared.lightImpact()
                    onSwipe?(.left, 0)
                } else {
                    // Didn't meet threshold - spring back
                    onSwipe?(.left, 0)
                }

                swipeTranslation = 0
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
        case 1: return Color.fizLightGold.opacity(0.6)
        case 2: return Color.fizGray.opacity(0.4)
        case 3: return Color.fizDarkGold.opacity(0.4)
        default: return Color.fizBackgroundSecondary.opacity(0.5)
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
            VStack(alignment: .leading, spacing: 4) {
                Text("\(entry.streak) correct answer\(entry.streak == 1 ? "" : "s")")
                    .font(.headline)
                    .fontWeight(.semibold)
                    .foregroundColor(.primary)

                Text(entry.date, format: .dateTime.month().day().year())
                    .font(.caption)
                    .foregroundColor(.secondary)

                // Game mode badge
                if entry.gameMode != "Regular" {
                    HStack(spacing: 4) {
                        Image(systemName: "circle.grid.cross.left.filled")
                            .font(.system(size: 10))
                        if let category = entry.categoryName {
                            Text("\(entry.gameMode): \(category)")
                                .font(.caption2)
                        } else {
                            Text(entry.gameMode)
                                .font(.caption2)
                        }
                    }
                    .padding(.horizontal, 6)
                    .padding(.vertical, 4)
                    .background(Color.fizOrange.opacity(0.15))
                    .foregroundColor(Color.fizOrange)
                    .cornerRadius(8)
                }
            }

            Spacer()

            // Dynamic streak icon based on achievement level
            Text(streakIcon)
                .font(.title3)
        }
        .padding()
        .background(backgroundColor)
        .cornerRadius(12)
        .shadow(color: Color.fizBrown.opacity(0.1), radius: 2, x: 0, y: 1)
    }
}

#Preview("Light Mode") {
    LeaderboardView(gameViewModel: GameViewModel())
        .modelContainer(for: LeaderboardEntry.self, inMemory: true)
        .preferredColorScheme(.light)
}

#Preview("Dark Mode") {
    LeaderboardView(gameViewModel: GameViewModel())
        .modelContainer(for: LeaderboardEntry.self, inMemory: true)
        .preferredColorScheme(.dark)
}
