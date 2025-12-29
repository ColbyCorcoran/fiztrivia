import SwiftUI

struct PopupDurationSettingsView: View {
    @StateObject private var popupDurationManager = PopupDurationManager.shared

    private var backgroundGradient: some View {
        Color(.systemGroupedBackground)
            .ignoresSafeArea()
    }

    var body: some View {
        Form {
            Section(footer: Text("Control how long answer popups are displayed. Shorter durations allow for faster trivia gameplay. Use Question History to review answers later.")) {
                VStack(alignment: .leading, spacing: 12) {
                    Text("Correct Answer: \(String(format: "%.1f", popupDurationManager.correctPopupDuration))s")
                        .font(.subheadline)
                    Slider(
                        value: Binding(
                            get: { popupDurationManager.correctPopupDuration },
                            set: { popupDurationManager.setCorrectPopupDuration($0) }
                        ),
                        in: 0.5...5.0,
                        step: 0.5
                    )
                }

                VStack(alignment: .leading, spacing: 12) {
                    Text("Incorrect Answer: \(String(format: "%.1f", popupDurationManager.incorrectPopupDuration))s")
                        .font(.subheadline)
                    Slider(
                        value: Binding(
                            get: { popupDurationManager.incorrectPopupDuration },
                            set: { popupDurationManager.setIncorrectPopupDuration($0) }
                        ),
                        in: 0.5...5.0,
                        step: 0.5
                    )
                }
            }
        }
        .scrollContentBackground(.hidden)
        .background(backgroundGradient)
        .navigationTitle("Answer Popup Duration")
        .navigationBarTitleDisplayMode(.large)
    }
}

#Preview {
    NavigationStack {
        PopupDurationSettingsView()
    }
}
