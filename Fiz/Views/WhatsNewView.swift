import SwiftUI

struct WhatsNewView: View {
    @Environment(\.dismiss) private var dismiss
    @Environment(\.sizeCategory) private var sizeCategory
    @StateObject private var whatsNewManager = WhatsNewManager.shared
    let updates: [WhatsNewUpdate]

    private var latestVersion: String {
        updates.first?.version ?? ""
    }

    var body: some View {
        ZStack {
            // Background gradient
            LinearGradient(
                gradient: Gradient(colors: [Color.fizBackground, Color.fizBackgroundSecondary]),
                startPoint: .topLeading,
                endPoint: .bottomTrailing
            )
            .ignoresSafeArea()

            VStack(spacing: 0) {
                // Header row with dismiss button
                HStack {
                    Spacer()
                    Button(action: {
                        whatsNewManager.markCurrentVersionAsSeen()
                        AnalyticsManager.shared.trackWhatsNewDismissed(version: latestVersion)
                        HapticManager.shared.buttonTapEffect()
                        dismiss()
                    }) {
                        Image(systemName: "xmark.circle.fill")
                            .font(.title2)
                            .foregroundColor(.secondary)
                    }
                }
                .padding(.horizontal, 20)
                .padding(.top, 20)
                .padding(.bottom, 8)

                // Scrollable content
                ScrollView {
                    VStack(alignment: .leading, spacing: 0) {
                        // "What's New" title block
                        VStack(alignment: .leading, spacing: 4) {
                            Text("What's New")
                                .font(.largeTitle.bold())
                                .foregroundColor(.primary)

                            Text("Version \(latestVersion)")
                                .font(.subheadline)
                                .foregroundColor(.secondary)
                        }
                        .frame(maxWidth: .infinity, alignment: .leading)
                        .padding(.horizontal, 24)
                        .padding(.bottom, 28)

                        // Feature sections
                        ForEach(Array(updates.enumerated()), id: \.element.id) { index, update in
                            WhatsNewUpdateSection(
                                update: update,
                                isLatest: index == 0,
                                showVersionHeader: index > 0
                            )
                        }
                    }
                    .padding(.top, 4)
                    .padding(.bottom, 20)
                }

                // Continue button
                Button(action: {
                    whatsNewManager.markCurrentVersionAsSeen()
                    AnalyticsManager.shared.trackWhatsNewCompleted(version: latestVersion)
                    HapticManager.shared.buttonTapEffect()
                    dismiss()
                }) {
                    Text("Continue")
                        .font(.headline)
                        .foregroundColor(.white)
                        .frame(maxWidth: .infinity)
                        .frame(height: 50)
                        .background(Color.fizOrange)
                        .cornerRadius(12)
                }
                .padding(.horizontal, 20)
                .padding(.vertical, 20)
            }
        }
    }
}

// MARK: - Update Section

struct WhatsNewUpdateSection: View {
    let update: WhatsNewUpdate
    let isLatest: Bool
    var showVersionHeader: Bool = false

    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            // Version header for older updates
            if showVersionHeader {
                HStack {
                    Text("Version \(update.version)")
                        .font(.footnote.weight(.semibold))
                        .foregroundColor(.secondary)
                        .textCase(.uppercase)
                    Rectangle()
                        .frame(height: 0.5)
                        .foregroundColor(Color.secondary.opacity(0.3))
                }
                .padding(.horizontal, 24)
                .padding(.top, 32)
                .padding(.bottom, 16)
            }

            // Feature rows
            VStack(spacing: 0) {
                ForEach(update.features) { feature in
                    WhatsNewFeatureRow(feature: feature, compact: !isLatest)
                }
            }
            .padding(.horizontal, 24)
        }
    }
}

// MARK: - Feature Row

struct WhatsNewFeatureRow: View {
    @Environment(\.sizeCategory) private var sizeCategory
    let feature: WhatsNewFeature
    var compact: Bool = false

    private var iconSize: CGFloat { compact ? 28 : 36 }
    private var iconFrameSize: CGFloat { compact ? 44 : 56 }
    private var iconCornerRadius: CGFloat { compact ? 10 : 13 }
    private var iconFont: Font { compact ? .body : .title2 }

    var body: some View {
        HStack(alignment: .top, spacing: 16) {
            // Icon — visible at non-accessibility sizes only
            if !sizeCategory.isAccessibilitySize {
                Image(systemName: feature.icon)
                    .font(iconFont)
                    .foregroundColor(.fizOrange)
                    .frame(width: iconFrameSize, height: iconFrameSize)
                    .background(Color.fizOrange.opacity(0.12))
                    .clipShape(RoundedRectangle(cornerRadius: iconCornerRadius))
            }

            VStack(alignment: .leading, spacing: 3) {
                Text(feature.title)
                    .font(compact ? .subheadline.bold() : .headline)
                    .foregroundColor(.primary)

                Text(feature.description)
                    .font(compact ? .footnote : .subheadline)
                    .foregroundColor(.secondary)
                    .fixedSize(horizontal: false, vertical: true)
            }
            .frame(maxWidth: .infinity, alignment: .leading)
        }
        .padding(.vertical, compact ? 10 : 14)
    }
}

#Preview {
    WhatsNewView(updates: [
        WhatsNewUpdate(
            version: "1.3.0",
            title: "Major Update!",
            features: [
                WhatsNewFeature(icon: "purchased.circle.fill", title: "Expansion Packs", description: "Purchase themed question packs to expand your trivia library"),
                WhatsNewFeature(icon: "gamecontroller.fill", title: "Game Modes", description: "Choose Multi-Category, Single Category, or Single Topic mode"),
                WhatsNewFeature(icon: "star.fill", title: "Streak Tracking", description: "Track your answer streaks across sessions")
            ]
        ),
        WhatsNewUpdate(
            version: "1.2.0",
            title: "Performance Improvements",
            features: [
                WhatsNewFeature(icon: "speedometer", title: "Faster Loading", description: "Questions load 2x faster"),
                WhatsNewFeature(icon: "paintbrush.fill", title: "UI Polish", description: "Refined animations and transitions")
            ]
        ),
        WhatsNewUpdate(
            version: "1.1.0",
            title: "Question Expansions!",
            features: [
                WhatsNewFeature(icon: "sparkles", title: "Special Events", description: "Limited-time themed packs for holidays")
            ]
        )
    ])
}
