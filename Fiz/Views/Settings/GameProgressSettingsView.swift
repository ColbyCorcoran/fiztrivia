import SwiftUI

struct GameProgressSettingsView: View {
    @Bindable var gameViewModel: GameViewModel
    @State private var showingResetAlert = false

    private var backgroundGradient: some View {
        Color(.systemGroupedBackground)
            .ignoresSafeArea()
    }

    var body: some View {
        Form {
            Section(footer: Text("Track your progress through the question database.")) {
                HStack {
                    Text("Questions Answered")
                    Spacer()
                    Text("\(gameViewModel.getAnsweredQuestionsCount()) / \(gameViewModel.getTotalQuestionsCount())")
                        .foregroundColor(.secondary)
                }

                HStack {
                    Text("Completion")
                    Spacer()
                    let progress = Double(gameViewModel.getAnsweredQuestionsCount()) / Double(max(gameViewModel.getTotalQuestionsCount(), 1))
                    Text("\(Int(progress * 100))%")
                        .foregroundColor(.secondary)
                }
            }

            Section {
                Button(action: {
                    showingResetAlert = true
                }) {
                    HStack {
                        Image(systemName: "arrow.clockwise")
                        Text("Reset All Progress")
                    }
                    .foregroundColor(.red)
                }
                .alert("Reset Progress", isPresented: $showingResetAlert) {
                    Button("Cancel", role: .cancel) { }
                    Button("Reset", role: .destructive) {
                        gameViewModel.resetAllProgress()
                        HapticManager.shared.buttonTapEffect()
                    }
                } message: {
                    Text("This will reset all answered questions and allow you to play them again. This action cannot be undone.")
                }
            }
        }
        .scrollContentBackground(.hidden)
        .background(backgroundGradient)
        .navigationTitle("Game Progress")
        .navigationBarTitleDisplayMode(.large)
    }
}

#Preview {
    NavigationStack {
        GameProgressSettingsView(gameViewModel: GameViewModel())
    }
}
