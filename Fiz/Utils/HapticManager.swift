import UIKit

class HapticManager {
    static let shared = HapticManager()

    private let impactLight = UIImpactFeedbackGenerator(style: .light)
    private let impactMedium = UIImpactFeedbackGenerator(style: .medium)
    private let impactHeavy = UIImpactFeedbackGenerator(style: .heavy)
    private let notification = UINotificationFeedbackGenerator()

    private init() {
        prepareHaptics()
    }

    private func prepareHaptics() {
        impactLight.prepare()
        impactMedium.prepare()
        impactHeavy.prepare()
        notification.prepare()
    }

    // Check if haptics are enabled before performing
    private var isHapticEnabled: Bool {
        return HapticSettingsManager.shared.isHapticEnabled
    }

    // MARK: - Haptic Feedback
    func lightImpact() {
        guard isHapticEnabled else { return }
        impactLight.impactOccurred()
    }

    func mediumImpact() {
        guard isHapticEnabled else { return }
        impactMedium.impactOccurred()
    }

    func heavyImpact() {
        guard isHapticEnabled else { return }
        impactHeavy.impactOccurred()
    }

    func successFeedback() {
        guard isHapticEnabled else { return }
        notification.notificationOccurred(.success)
    }

    func errorFeedback() {
        guard isHapticEnabled else { return }
        notification.notificationOccurred(.error)
    }

    func warningFeedback() {
        guard isHapticEnabled else { return }
        notification.notificationOccurred(.warning)
    }
    
    // MARK: - Combined Effects
    func wheelSpinEffect() {
        mediumImpact()
    }

    func correctAnswerEffect() {
        // Custom celebratory haptic pattern
        // Pattern: light -> medium -> light (creates a "bounce" celebration effect)
        lightImpact()

        DispatchQueue.main.asyncAfter(deadline: .now() + 0.06) {
            self.mediumImpact()
        }

        DispatchQueue.main.asyncAfter(deadline: .now() + 0.12) {
            self.lightImpact()
        }
    }

    func incorrectAnswerEffect() {
        errorFeedback()
    }

    func buttonTapEffect() {
        lightImpact()
    }
}