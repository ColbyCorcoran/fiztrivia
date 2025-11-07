import SwiftUI

// MARK: - Liquid Glass Button Style (iOS 17+)
struct LiquidGlassButtonStyle: ButtonStyle {
    var color: Color = Color.fizTeal

    func makeBody(configuration: Configuration) -> some View {
        if #available(iOS 17.0, *) {
            // Modern iOS 17+ style with translucent glass effect
            configuration.label
                .padding(.horizontal, 16)
                .padding(.vertical, 12)
                .background(
                    ZStack {
                        // Base translucent background
                        color.opacity(0.2)

                        // Glass blur effect
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
            // Fallback for older iOS versions
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

// MARK: - Prominent Liquid Glass Button Style (iOS 17+)
struct ProminentLiquidGlassButtonStyle: ButtonStyle {
    var color: Color = Color.fizOrange

    func makeBody(configuration: Configuration) -> some View {
        if #available(iOS 17.0, *) {
            // Modern iOS 17+ style with more prominent translucent glass effect
            configuration.label
                .fontWeight(.semibold)
                .padding(.horizontal, 20)
                .padding(.vertical, 14)
                .background(
                    ZStack {
                        // Base color background
                        color.opacity(0.3)

                        // Glass blur effect overlay
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
        } else {
            // Fallback for older iOS versions
            configuration.label
                .fontWeight(.semibold)
                .padding(.horizontal, 20)
                .padding(.vertical, 14)
                .background(color)
                .foregroundColor(.white)
                .cornerRadius(14)
                .shadow(color: color.opacity(0.3), radius: 10, x: 0, y: 5)
                .scaleEffect(configuration.isPressed ? 0.95 : 1.0)
        }
    }
}

// MARK: - View Extensions
extension View {
    func liquidGlassButtonStyle(color: Color = Color.fizTeal) -> some View {
        self.buttonStyle(LiquidGlassButtonStyle(color: color))
    }

    func prominentLiquidGlassButtonStyle(color: Color = Color.fizOrange) -> some View {
        self.buttonStyle(ProminentLiquidGlassButtonStyle(color: color))
    }
}
