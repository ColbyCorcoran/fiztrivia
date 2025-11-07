import SwiftUI

// MARK: - Liquid Glass Button Styles (iOS 26+)
// iOS 26 introduces native .buttonStyle(.glass) and .buttonStyle(.glassProminent)
// This file provides wrappers and fallbacks for older iOS versions

// MARK: - Glass Button Style with Fallback
struct GlassButtonStyleWrapper: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        if #available(iOS 26.0, *) {
            // iOS 26+: Use native glass button style
            configuration.label
                .buttonStyle(.glass)
        } else {
            // Fallback: Custom glass-like effect for iOS 17-25
            configuration.label
                .padding(.horizontal, 12)
                .padding(.vertical, 12)
                .background(
                    ZStack {
                        Color.primary.opacity(0.05)
                        if !configuration.isPressed {
                            Color.white.opacity(0.1)
                                .blur(radius: 8)
                        }
                    }
                )
                .cornerRadius(10)
                .overlay(
                    RoundedRectangle(cornerRadius: 10)
                        .stroke(Color.primary.opacity(0.15), lineWidth: 0.5)
                )
                .scaleEffect(configuration.isPressed ? 0.95 : 1.0)
                .animation(.easeInOut(duration: 0.1), value: configuration.isPressed)
        }
    }
}

// MARK: - Prominent Glass Button Style with Fallback
struct GlassProminentButtonStyleWrapper: ButtonStyle {
    var color: Color = Color.fizOrange

    func makeBody(configuration: Configuration) -> some View {
        if #available(iOS 26.0, *) {
            // iOS 26+: Use native glass prominent button style
            configuration.label
                .buttonStyle(.glassProminent)
                .tint(color)
        } else {
            // Fallback: Enhanced glass-like effect for iOS 17-25
            configuration.label
                .fontWeight(.semibold)
                .padding(.horizontal, 20)
                .padding(.vertical, 14)
                .background(
                    ZStack {
                        color.opacity(0.3)
                        if !configuration.isPressed {
                            LinearGradient(
                                colors: [color.opacity(0.4), color.opacity(0.2)],
                                startPoint: .topLeading,
                                endPoint: .bottomTrailing
                            )
                            .blur(radius: 8)
                        }
                    }
                )
                .foregroundStyle(.white)
                .cornerRadius(14)
                .overlay(
                    RoundedRectangle(cornerRadius: 14)
                        .stroke(
                            LinearGradient(
                                colors: [.white.opacity(0.5), .white.opacity(0.1)],
                                startPoint: .topLeading,
                                endPoint: .bottomTrailing
                            ),
                            lineWidth: 1.5
                        )
                )
                .shadow(color: color.opacity(0.3), radius: 10, x: 0, y: 5)
                .scaleEffect(configuration.isPressed ? 0.95 : 1.0)
                .animation(.easeInOut(duration: 0.1), value: configuration.isPressed)
        }
    }
}

// MARK: - Liquid Glass Button Style (for answer buttons)
struct LiquidGlassButtonStyle: ButtonStyle {
    var color: Color = Color.fizTeal

    func makeBody(configuration: Configuration) -> some View {
        if #available(iOS 26.0, *) {
            // iOS 26+: Use native glass with custom tint
            configuration.label
                .buttonStyle(.glass)
                .tint(color)
        } else if #available(iOS 17.0, *) {
            // iOS 17-25: Custom translucent glass effect
            configuration.label
                .padding(.horizontal, 16)
                .padding(.vertical, 12)
                .background(
                    ZStack {
                        color.opacity(0.2)
                        if !configuration.isPressed {
                            color.opacity(0.1)
                                .blur(radius: 10)
                        }
                    }
                )
                .foregroundStyle(color)
                .cornerRadius(12)
                .overlay(
                    RoundedRectangle(cornerRadius: 12)
                        .stroke(color.opacity(0.3), lineWidth: 1)
                )
                .scaleEffect(configuration.isPressed ? 0.95 : 1.0)
                .animation(.easeInOut(duration: 0.1), value: configuration.isPressed)
        } else {
            // Fallback for iOS < 17
            configuration.label
                .padding(.horizontal, 16)
                .padding(.vertical, 12)
                .background(color.opacity(0.15))
                .foregroundColor(color)
                .cornerRadius(12)
                .overlay(
                    RoundedRectangle(cornerRadius: 12)
                        .stroke(color.opacity(0.3), lineWidth: 1)
                )
                .scaleEffect(configuration.isPressed ? 0.95 : 1.0)
        }
    }
}

// MARK: - View Extensions
extension View {
    /// Applies glass button style with iOS 26+ support and fallback
    func glassButtonStyle() -> some View {
        self.buttonStyle(GlassButtonStyleWrapper())
    }

    /// Applies prominent glass button style with iOS 26+ support and fallback
    func glassProminentButtonStyle(color: Color = Color.fizOrange) -> some View {
        self.buttonStyle(GlassProminentButtonStyleWrapper(color: color))
    }

    /// Applies liquid glass button style (for answer buttons)
    func liquidGlassButtonStyle(color: Color = Color.fizTeal) -> some View {
        self.buttonStyle(LiquidGlassButtonStyle(color: color))
    }

    /// Legacy alias for compatibility
    func prominentLiquidGlassButtonStyle(color: Color = Color.fizOrange) -> some View {
        self.glassProminentButtonStyle(color: color)
    }
}
