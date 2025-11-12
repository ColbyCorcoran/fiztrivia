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
    
    // MARK: - Haptic Feedback
    func lightImpact() {
        impactLight.impactOccurred()
    }
    
    func mediumImpact() {
        impactMedium.impactOccurred()
    }
    
    func heavyImpact() {
        impactHeavy.impactOccurred()
    }
    
    func successFeedback() {
        notification.notificationOccurred(.success)
    }
    
    func errorFeedback() {
        notification.notificationOccurred(.error)
    }
    
    func warningFeedback() {
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