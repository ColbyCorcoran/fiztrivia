import SwiftUI
import UIKit

// MARK: - UIColor Hex Extension
extension UIColor {
    convenience init(hex: String) {
        let hex = hex.trimmingCharacters(in: CharacterSet.alphanumerics.inverted)
        var int: UInt64 = 0
        Scanner(string: hex).scanHexInt64(&int)
        let a, r, g, b: UInt64
        switch hex.count {
        case 3: // RGB (12-bit)
            (a, r, g, b) = (255, (int >> 8) * 17, (int >> 4 & 0xF) * 17, (int & 0xF) * 17)
        case 6: // RGB (24-bit)
            (a, r, g, b) = (255, int >> 16, int >> 8 & 0xFF, int & 0xFF)
        case 8: // ARGB (32-bit)
            (a, r, g, b) = (int >> 24, int >> 16 & 0xFF, int >> 8 & 0xFF, int & 0xFF)
        default:
            (a, r, g, b) = (255, 1, 1, 0)
        }

        self.init(
            red: CGFloat(r) / 255,
            green: CGFloat(g) / 255,
            blue: CGFloat(b) / 255,
            alpha: CGFloat(a) / 255
        )
    }
}

// MARK: - Color Adaptive Extension
extension Color {
    /// Creates an adaptive color that responds to light/dark mode
    init(light: String, dark: String) {
        self.init(UIColor { traitCollection in
            traitCollection.userInterfaceStyle == .dark
                ? UIColor(hex: dark)
                : UIColor(hex: light)
        })
    }
}

// MARK: - Fiz Color Palette
extension Color {
    // MARK: - Primary Colors

    /// Background Color - Warm off-white background (light) / Deep warm brown-black (dark)
    static let fizBackground = Color(light: "#f3eddf", dark: "#1a1612")

    /// Fox Orange - Primary brand orange, slightly brighter in dark mode for visibility
    static let fizOrange = Color(light: "#dd7423", dark: "#ff9447")

    /// Fox Cream - Light cream accent, slightly desaturated in dark mode
    static let fizCream = Color(light: "#f4d29b", dark: "#d4b77b")

    /// Fox Brown (Shadow) - Deep brown for shadows (light) / Lighter brown for text (dark)
    static let fizBrown = Color(light: "#533214", dark: "#a88860")

    /// Teal Accent - Primary teal for streaks and highlights, lighter in dark mode
    static let fizTeal = Color(light: "#39766d", dark: "#52a393")

    /// Teal Shadow - Darker teal for depth, slightly lighter in dark mode
    static let fizTealShadow = Color(light: "#2e5147", dark: "#3d6b5e")

    // MARK: - Secondary Colors

    /// Secondary Gray - Silver/gray accent, medium gray in dark mode
    static let fizGray = Color(light: "#b1aea5", dark: "#8a8782")

    /// Dark Gold Star - Bronze/gold accent, brighter in dark mode
    static let fizDarkGold = Color(light: "#d48c20", dark: "#f0a840")

    /// Light Gold Star - Bright gold highlight, desaturated in dark mode
    static let fizLightGold = Color(light: "#f3d29d", dark: "#d4b77d")

    /// Secondary Background - Slightly darker warm background (light) / Slightly lighter than primary dark background
    static let fizBackgroundSecondary = Color(light: "#e8dcc8", dark: "#2a2420")
}
