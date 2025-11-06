import SwiftUI

// MARK: - Accessibility Helpers
extension View {
    func triviaAccessibility(label: String, hint: String? = nil, traits: AccessibilityTraits = []) -> some View {
        self
            .accessibilityLabel(label)
            .accessibilityHint(hint ?? "")
            .accessibilityAddTraits(traits)
    }
    
    func wheelSegmentAccessibility(category: TriviaCategory, isSelected: Bool = false) -> some View {
        let label = "\(category.rawValue) category"
        let hint = isSelected ? "Currently selected category" : "Tap to select this category"
        
        return self
            .accessibilityLabel(label)
            .accessibilityHint(hint)
            .accessibilityAddTraits(.isButton)
            .accessibilityAddTraits(isSelected ? .isSelected : [])
    }
    
    func answerButtonAccessibility(answer: String, letter: String, isCorrect: Bool? = nil) -> some View {
        let label = "Answer \(letter): \(answer)"
        var hint = "Tap to select this answer"
        
        if let correct = isCorrect {
            hint = correct ? "This is the correct answer" : "This is an incorrect answer"
        }
        
        return self
            .accessibilityLabel(label)
            .accessibilityHint(hint)
            .accessibilityAddTraits(.isButton)
            .accessibilityAddTraits((isCorrect == true) ? .isSelected : [])
    }
}

// MARK: - Accessibility Settings
struct AccessibilitySettings {
    static let minimumTouchTargetSize: CGFloat = 44.0
    static let defaultAnimationDuration: Double = 0.3
    
    static var isVoiceOverRunning: Bool {
        UIAccessibility.isVoiceOverRunning
    }
    
    static var isReduceMotionEnabled: Bool {
        UIAccessibility.isReduceMotionEnabled
    }
    
    static var prefersCrossFadeTransitions: Bool {
        UIAccessibility.prefersCrossFadeTransitions
    }
    
    static func adjustedAnimationDuration(_ duration: Double) -> Double {
        return isReduceMotionEnabled ? 0 : duration
    }
}