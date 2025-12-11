import SwiftUI

// MARK: - iOS 26 Liquid Glass Button Styles with iOS 18 Fallback
// iOS 26 introduces native .buttonStyle(.glass) and .buttonStyle(.glassProminent)
// For iOS 18 and below, we use traditional solid button styles

// MARK: - Toolbar Glass Button (Leaderboard, Settings, Done buttons)
extension View {
    func toolbarGlassButton() -> some View {
        if #available(iOS 26, *) {
            // iOS 26: Use native glass button style
            return AnyView(self.buttonStyle(.glass))
        } else {
            // iOS 18 and below: Use plain style (icon buttons)
            return AnyView(self.buttonStyle(.plain))
        }
    }
}

// MARK: - Answer Button Style (Question Options)
struct AnswerButtonStyle: ViewModifier {
    func body(content: Content) -> some View {
        if #available(iOS 26, *) {
            // iOS 26: Use native glass button style
            content
                .buttonStyle(.glass)
        } else {
            // iOS 18 and below: Traditional solid buttons
            content
                .buttonStyle(iOS18AnswerButtonStyle())
        }
    }
}

struct iOS18AnswerButtonStyle: ButtonStyle {
    @Environment(\.sizeCategory) var sizeCategory

    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .font(.body)
            .fontWeight(.medium)
            .foregroundColor(.primary)
            .multilineTextAlignment(.center)
            .lineLimit(nil)
            .fixedSize(horizontal: false, vertical: true)
            .frame(maxWidth: .infinity, minHeight: dynamicMinHeight)
            .padding(.horizontal, dynamicHorizontalPadding)
            .padding(.vertical, dynamicVerticalPadding)
            .background(Color.fizBackground)
            .cornerRadius(12)
            .shadow(color: Color.fizBrown.opacity(0.15), radius: 2, x: 0, y: 1)
            .scaleEffect(configuration.isPressed ? 0.95 : 1.0)
    }

    private var dynamicMinHeight: CGFloat {
        // Ensure minimum touch target of 44pt, but allow natural growth
        sizeCategory >= .accessibilityMedium ? 56 : 44
    }

    private var dynamicHorizontalPadding: CGFloat {
        sizeCategory >= .accessibilityMedium ? 8 : 12
    }

    private var dynamicVerticalPadding: CGFloat {
        sizeCategory >= .accessibilityMedium ? 8 : 10
    }
}

extension View {
    func answerButtonStyle() -> some View {
        self.modifier(AnswerButtonStyle())
    }
}

// MARK: - Prominent Action Button Style (Play Again, Ready to Start, etc.)
struct ProminentActionButtonStyle: ViewModifier {
    var color: Color

    func body(content: Content) -> some View {
        if #available(iOS 26, *) {
            // iOS 26: Use native glass prominent button style
            content
                .buttonStyle(.glassProminent)
                .tint(color)
        } else {
            // iOS 18 and below: Traditional solid prominent buttons
            content
                .buttonStyle(iOS18ProminentButtonStyle(color: color))
        }
    }
}

struct iOS18ProminentButtonStyle: ButtonStyle {
    var color: Color
    @Environment(\.sizeCategory) var sizeCategory

    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .font(.headline)
            .fontWeight(.semibold)
            .foregroundColor(.white)
            .frame(maxWidth: .infinity)
            .padding(.vertical, dynamicVerticalPadding)
            .background(color)
            .cornerRadius(12)
            .shadow(color: Color.fizBrown.opacity(0.3), radius: 4, x: 0, y: 2)
            .scaleEffect(configuration.isPressed ? 0.95 : 1.0)
    }

    private var dynamicVerticalPadding: CGFloat {
        sizeCategory >= .accessibilityMedium ? 12 : 16
    }
}

extension View {
    func prominentActionButton(color: Color = Color.fizOrange) -> some View {
        self.modifier(ProminentActionButtonStyle(color: color))
    }
}

// MARK: - Legacy Aliases for Compatibility
extension View {
    func glassButtonStyle() -> some View {
        self.toolbarGlassButton()
    }

    func liquidGlassButtonStyle(color: Color = Color.fizTeal) -> some View {
        self.answerButtonStyle()
    }

    func glassProminentButtonStyle(color: Color = Color.fizOrange) -> some View {
        self.prominentActionButton(color: color)
    }

    func prominentLiquidGlassButtonStyle(color: Color = Color.fizOrange) -> some View {
        self.prominentActionButton(color: color)
    }
}

