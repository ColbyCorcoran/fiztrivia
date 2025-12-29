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

// MARK: - Dynamic Type Helpers
extension ContentSizeCategory {
    /// Returns true if the user has enabled accessibility text sizes
    var isAccessibilitySize: Bool {
        self >= .accessibilityMedium
    }

    /// Returns true if questions should be displayed in a modal for better readability
    /// Threshold: .accessibilityMedium and above
    var shouldUseModalQuestions: Bool {
        self >= .accessibilityMedium
    }

    // MARK: - Dynamic Sizing Helpers

    /// Scaling factor for UI elements (1.0 → 2.5)
    var uiScaleFactor: CGFloat {
        switch self {
        case .extraSmall: return 0.9
        case .small: return 0.95
        case .medium: return 1.0
        case .large: return 1.1
        case .extraLarge: return 1.2
        case .extraExtraLarge: return 1.3
        case .extraExtraExtraLarge: return 1.5
        case .accessibilityMedium: return 1.6
        case .accessibilityLarge: return 1.8
        case .accessibilityExtraLarge: return 2.0
        case .accessibilityExtraExtraLarge: return 2.2
        case .accessibilityExtraExtraExtraLarge: return 2.5
        @unknown default: return 1.0
        }
    }

    /// Conservative scaling for structural elements (1.0 → 1.8)
    var conservativeScaleFactor: CGFloat {
        switch self {
        case .extraSmall, .small, .medium: return 1.0
        case .large: return 1.05
        case .extraLarge: return 1.1
        case .extraExtraLarge: return 1.15
        case .extraExtraExtraLarge: return 1.2
        case .accessibilityMedium: return 1.3
        case .accessibilityLarge: return 1.4
        case .accessibilityExtraLarge: return 1.5
        case .accessibilityExtraExtraLarge: return 1.6
        case .accessibilityExtraExtraExtraLarge: return 1.8
        @unknown default: return 1.0
        }
    }

    /// Adaptive minimumScaleFactor for text
    var textMinimumScaleFactor: CGFloat {
        if self >= .accessibilityMedium {
            return 0.9
        } else if self >= .extraLarge {
            return 0.8
        } else {
            return 0.7
        }
    }

    /// Use compact layouts at very large sizes
    var shouldUseCompactLayout: Bool {
        self >= .accessibilityLarge
    }

    /// Returns the preferred initial modal detent based on text size
    /// For very large accessibility sizes, start at .large for maximum space
    var preferredModalDetent: PresentationDetent {
        if self >= .accessibilityExtraLarge {
            return .large  // Extreme sizes need maximum space immediately
        } else {
            return .medium  // Normal and moderate accessibility sizes start compact
        }
    }
}

// MARK: - Adaptive Frame Modifier
struct AdaptiveFrame: ViewModifier {
    let baseWidth: CGFloat?
    let baseHeight: CGFloat?
    let scaleWithText: Bool
    @Environment(\.sizeCategory) private var sizeCategory

    func body(content: Content) -> some View {
        let scaleFactor = scaleWithText ? sizeCategory.uiScaleFactor : 1.0

        return content
            .frame(
                width: baseWidth.map { $0 * scaleFactor },
                height: baseHeight.map { $0 * scaleFactor }
            )
    }
}

extension View {
    func adaptiveFrame(width: CGFloat? = nil, height: CGFloat? = nil, scaleWithText: Bool = true) -> some View {
        self.modifier(AdaptiveFrame(baseWidth: width, baseHeight: height, scaleWithText: scaleWithText))
    }
}
