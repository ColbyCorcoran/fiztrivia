import SwiftUI

/// A sheet wrapper around GameModesSettingsView with a checkmark dismiss button.
/// Presented from the tappable Mode badge on the wheel view.
struct GameModesQuickSheet: View {
    @Bindable var gameViewModel: GameViewModel
    @Environment(\.dismiss) private var dismiss
    @StateObject private var gameModeManager = GameModeManager.shared

    /// Mirrors GameModesSettingsView.isSelectionComplete — computed from manager state
    /// so we don't need to modify GameModesSettingsView.
    private var isSelectionComplete: Bool {
        switch gameModeManager.selectedMode {
        case .multiCategory:
            return true
        case .singleCategory:
            return gameModeManager.selectedCategory != nil
        case .singleTopic:
            return gameModeManager.selectedTopic != nil
        }
    }

    var body: some View {
        NavigationStack {
            GameModesSettingsView(gameViewModel: gameViewModel)
                .toolbar {
                    ToolbarItem(placement: .navigationBarTrailing) {
                        Button(action: {
                            HapticManager.shared.buttonTapEffect()
                            dismiss()
                        }) {
                            Image(systemName: "checkmark")
                                .font(.body.weight(.semibold))
                        }
                        .tint(.fizTeal)
                        .disabled(!isSelectionComplete)
                        .opacity(isSelectionComplete ? 1.0 : 0.4)
                    }
                }
        }
    }
}
