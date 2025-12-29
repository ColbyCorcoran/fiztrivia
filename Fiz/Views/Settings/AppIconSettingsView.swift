import SwiftUI

struct AppIconSettingsView: View {
    @StateObject private var appIconManager = AppIconManager.shared
    @Environment(\.sizeCategory) private var sizeCategory

    // Adaptive grid columns based on accessibility size
    private var iconGridColumns: [GridItem] {
        if sizeCategory.isAccessibilitySize {
            return [GridItem(.flexible()), GridItem(.flexible())]  // 2 columns
        } else {
            return [GridItem(.flexible()), GridItem(.flexible()), GridItem(.flexible())]  // 3 columns
        }
    }

    // Adaptive icon size
    private var iconSize: CGFloat {
        sizeCategory.isAccessibilitySize ? 90 : 60
    }

    var body: some View {
        Form {
            Section(footer: Text("Choose your favorite Fiz to represent your app!")) {
                LazyVGrid(columns: iconGridColumns, spacing: sizeCategory.isAccessibilitySize ? 20 : 16) {
                    ForEach(AppIconManager.AppIcon.allCases) { icon in
                        Button(action: {
                            HapticManager.shared.buttonTapEffect()
                            appIconManager.setIcon(icon)
                        }) {
                            VStack(spacing: 8) {
                                Image(icon.previewImageName)
                                    .resizable()
                                    .scaledToFit()
                                    .frame(width: iconSize, height: iconSize)
                                    .clipShape(RoundedRectangle(cornerRadius: sizeCategory.isAccessibilitySize ? 18 : 12))
                                    .overlay(
                                        RoundedRectangle(cornerRadius: sizeCategory.isAccessibilitySize ? 18 : 12)
                                            .stroke(appIconManager.selectedIcon == icon ? Color.fizTeal : Color.clear, lineWidth: 3)
                                    )
                                    .shadow(color: Color.fizBrown.opacity(0.2), radius: 4, x: 0, y: 2)

                                Text(icon.rawValue)
                                    .font(.caption)
                                    .foregroundColor(.primary)
                                    .multilineTextAlignment(.center)
                                    .lineLimit(nil)
                                    .fixedSize(horizontal: false, vertical: true)
                            }
                            .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .top)
                        }
                        .buttonStyle(.plain)
                    }
                }
                .padding(.vertical, 8)
            }
        }
        .navigationTitle("App Icon")
        .navigationBarTitleDisplayMode(.large)
    }
}

#Preview {
    NavigationStack {
        AppIconSettingsView()
    }
}
