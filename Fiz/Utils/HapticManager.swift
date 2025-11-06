import UIKit
import AVFoundation

class HapticManager {
    static let shared = HapticManager()
    
    private let impactLight = UIImpactFeedbackGenerator(style: .light)
    private let impactMedium = UIImpactFeedbackGenerator(style: .medium)
    private let impactHeavy = UIImpactFeedbackGenerator(style: .heavy)
    private let notification = UINotificationFeedbackGenerator()
    
    private var audioPlayer: AVAudioPlayer?
    
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
    
    // MARK: - Sound Effects
    func playWheelSpin() {
        playSystemSound(soundID: 1103) // Swoosh sound
    }
    
    func playCorrectAnswer() {
        playSystemSound(soundID: 1054) // Success sound
    }
    
    func playIncorrectAnswer() {
        playSystemSound(soundID: 1053) // Error sound
    }
    
    func playButtonTap() {
        playSystemSound(soundID: 1104) // Click sound
    }
    
    private func playSystemSound(soundID: SystemSoundID) {
        AudioServicesPlaySystemSound(soundID)
    }
    
    // MARK: - Combined Effects
    func wheelSpinEffect() {
        mediumImpact()
        playWheelSpin()
    }
    
    func correctAnswerEffect() {
        successFeedback()
        playCorrectAnswer()
    }
    
    func incorrectAnswerEffect() {
        errorFeedback()
        playIncorrectAnswer()
    }
    
    func buttonTapEffect() {
        lightImpact()
        playButtonTap()
    }
}