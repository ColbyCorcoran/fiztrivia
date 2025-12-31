import SwiftUI

struct WhatsNewView: View {
    @Environment(\.dismiss) private var dismiss
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
                // Header
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
                .padding(.bottom, 10)

                // Scrollable updates list
                ScrollView {
                    VStack(spacing: 40) {
                        ForEach(Array(updates.enumerated()), id: \.element.id) { index, update in
                            WhatsNewUpdateSection(
                                update: update,
                                isLatest: index == 0
                            )
                        }
                    }
                    .padding(.horizontal, 30)
                    .padding(.top, 10)
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
                .padding(.vertical, 30)
            }
        }
    }
}

// MARK: - Update Section
struct WhatsNewUpdateSection: View {
    let update: WhatsNewUpdate
    let isLatest: Bool

    var body: some View {
        VStack(spacing: 15) {
            // Icon (only for latest update)
            if isLatest {
                Image(systemName: "sparkles")
                    .font(.system(size: 60))
                    .foregroundColor(.fizOrange)
                    .padding(.bottom, 10)
            }

            // Version badge
            HStack(spacing: 6) {
                Image(systemName: "tag.fill")
                    .font(.caption)
                Text("Version \(update.version)")
                    .font(.subheadline.bold())
            }
            .foregroundColor(isLatest ? .fizOrange : .secondary)
            .padding(.horizontal, 12)
            .padding(.vertical, 6)
            .background(isLatest ? Color.fizOrange.opacity(0.15) : Color.secondary.opacity(0.1))
            .cornerRadius(20)

            // Title
            Text(update.title)
                .font(isLatest ? .title.bold() : .title2.bold())
                .foregroundColor(.primary)
                .multilineTextAlignment(.center)
                .padding(.horizontal, 10)

            // Features
            VStack(spacing: 15) {
                ForEach(update.features) { feature in
                    WhatsNewFeatureRow(
                        feature: feature,
                        compact: !isLatest
                    )
                }
            }
            .padding(.top, 5)

            // Divider (except for last update)
            if !isLatest {
                Divider()
                    .padding(.top, 15)
            }
        }
    }
}

struct WhatsNewFeatureRow: View {
    let feature: WhatsNewFeature
    var compact: Bool = false

    var body: some View {
        HStack(alignment: .top, spacing: compact ? 12 : 15) {
            // Icon
            Image(systemName: feature.icon)
                .font(compact ? .body : .title2)
                .foregroundColor(.fizOrange)
                .frame(width: compact ? 32 : 40, height: compact ? 32 : 40)
                .background(Color.fizOrange.opacity(0.1))
                .clipShape(RoundedRectangle(cornerRadius: compact ? 8 : 10))

            VStack(alignment: .leading, spacing: 4) {
                Text(feature.title)
                    .font(compact ? .subheadline.bold() : .headline)
                    .foregroundColor(.primary)

                Text(feature.description)
                    .font(compact ? .caption : .body)
                    .foregroundColor(.secondary)
                    .fixedSize(horizontal: false, vertical: true)
            }

            Spacer()
        }
    }
}

#Preview {
    WhatsNewView(updates: [
        WhatsNewUpdate(
            version: "1.3.0",
            title: "Major Update!",
            features: [
                WhatsNewFeature(icon: "purchased.circle.fill", title: "Expansion Packs", description: "Purchase themed question packs to expand your trivia library"),
                WhatsNewFeature(icon: "star.fill", title: "Premium Categories", description: "Access exclusive categories")
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
