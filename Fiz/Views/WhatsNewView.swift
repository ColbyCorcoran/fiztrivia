import SwiftUI

struct WhatsNewView: View {
    @Environment(\.dismiss) private var dismiss
    @StateObject private var whatsNewManager = WhatsNewManager.shared
    let update: WhatsNewUpdate

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
                        AnalyticsManager.shared.trackWhatsNewDismissed(version: update.version)
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

                // Icon
                Image(systemName: "sparkles")
                    .font(.system(size: 60))
                    .foregroundColor(.fizOrange)
                    .padding(.bottom, 20)

                // Title
                Text(update.title)
                    .font(.largeTitle.bold())
                    .foregroundColor(.primary)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal, 30)
                    .padding(.bottom, 10)

                // Version
                Text("Version \(update.version)")
                    .font(.subheadline)
                    .foregroundColor(.secondary)
                    .padding(.bottom, 30)

                // Features list
                ScrollView {
                    VStack(spacing: 20) {
                        ForEach(update.features) { feature in
                            WhatsNewFeatureRow(feature: feature)
                        }
                    }
                    .padding(.horizontal, 30)
                }

                // Continue button
                Button(action: {
                    whatsNewManager.markCurrentVersionAsSeen()
                    AnalyticsManager.shared.trackWhatsNewCompleted(version: update.version)
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

struct WhatsNewFeatureRow: View {
    let feature: WhatsNewFeature

    var body: some View {
        HStack(alignment: .top, spacing: 15) {
            // Icon
            Image(systemName: feature.icon)
                .font(.title2)
                .foregroundColor(.fizOrange)
                .frame(width: 40, height: 40)
                .background(Color.fizOrange.opacity(0.1))
                .clipShape(RoundedRectangle(cornerRadius: 10))

            VStack(alignment: .leading, spacing: 4) {
                Text(feature.title)
                    .font(.headline)
                    .foregroundColor(.primary)

                Text(feature.description)
                    .font(.body)
                    .foregroundColor(.secondary)
                    .fixedSize(horizontal: false, vertical: true)
            }

            Spacer()
        }
    }
}

#Preview {
    WhatsNewView(update: WhatsNewUpdate(
        version: "1.1.0",
        title: "Question Expansions!",
        features: [
            WhatsNewFeature(icon: "purchased.circle.fill", title: "Expansion Packs", description: "Purchase themed question packs to expand your trivia library"),
            WhatsNewFeature(icon: "star.fill", title: "Premium Categories", description: "Access exclusive categories like Movies, TV Shows, and more"),
            WhatsNewFeature(icon: "sparkles", title: "Special Events", description: "Limited-time themed packs for holidays and special occasions")
        ]
    ))
}
