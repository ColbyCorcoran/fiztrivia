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
                            set: { newValue in
                                popupDurationManager.setCorrectPopupDuration(newValue)
                                let isCustom = abs(newValue - 1.5) > 0.01  // Default is 1.5s
                                AnalyticsManager.shared.trackPopupDurationChanged(popupType: "correct", duration: newValue, isCustom: isCustom)
                            }
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
                            set: { newValue in
                                popupDurationManager.setIncorrectPopupDuration(newValue)
                                let isCustom = abs(newValue - 3.0) > 0.01  // Default is 3.0s
                                AnalyticsManager.shared.trackPopupDurationChanged(popupType: "incorrect", duration: newValue, isCustom: isCustom)
                            }
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
