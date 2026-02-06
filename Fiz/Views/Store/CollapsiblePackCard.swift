//
//  CollapsiblePackCard.swift
//  Fiz
//
//  Created by Claude on 2/3/26.
//

import SwiftUI

struct CollapsiblePackCard: View {
    let pack: ExpansionPack
    @Binding var isExpanded: Bool
    let onInstall: () -> Void
    let onUninstall: () -> Void

    @StateObject private var expansionManager = ExpansionPackManager.shared
    @StateObject private var cartManager = CartManager.shared
    @StateObject private var storeManager = StoreManager.shared

    private var isPurchased: Bool {
        expansionManager.isPurchased(packId: pack.packId)
    }

    private var isInstalled: Bool {
        expansionManager.isInstalled(packId: pack.packId)
    }

    private var isInCart: Bool {
        cartManager.isInCart(packId: pack.packId)
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            // COLLAPSED STATE (always visible)
            collapsedHeader
                .zIndex(1)

            // EXPANDED STATE (conditionally visible)
            if isExpanded {
                expandedContent
                    .zIndex(0)
            }
        }
        .background(Color(.secondarySystemBackground))
        .cornerRadius(16)
        .shadow(color: Color.black.opacity(0.1), radius: 8, x: 0, y: 4)
    }

    // MARK: - Collapsed Header
    private var collapsedHeader: some View {
        Button(action: {
            withAnimation(.spring(response: 0.45, dampingFraction: 0.82)) {
                isExpanded.toggle()
                HapticManager.shared.lightImpact()

                if isExpanded {
                    AnalyticsManager.shared.trackExpansionPackExpanded(
                        packId: pack.packId,
                        packName: pack.packName
                    )
                }
            }
        }) {
            HStack(spacing: 12) {
                // Icon
                Image(systemName: pack.icon)
                    .font(.system(size: 28))
                    .foregroundColor(.fizOrange)
                    .frame(width: 44, height: 44)

                // Name & Question Count
                VStack(alignment: .leading, spacing: 3) {
                    HStack(spacing: 6) {
                        Text(pack.packName)
                            .font(.headline)
                            .fontWeight(.semibold)
                            .foregroundColor(.fizBrown)
                            .lineLimit(isExpanded ? 2 : 1)

                        // NEW badge
                        if pack.isNew {
                            Text("NEW")
                                .font(.caption2)
                                .fontWeight(.bold)
                                .foregroundColor(.white)
                                .padding(.horizontal, 6)
                                .padding(.vertical, 2)
                                .background(Color.fizOrange)
                                .cornerRadius(4)
                        }
                    }

                    Text("\(pack.questionCount) questions")
                        .font(.subheadline)
                        .foregroundColor(.fizBrown.opacity(0.6))
                }

                Spacer()

                // Status/Price/Action
                HStack(spacing: 8) {
                    // Status badges
                    if isPurchased {
                        if isInstalled {
                            StatusBadge(text: "Installed", color: .green)
                        } else {
                            StatusBadge(text: "Owned", color: .blue)
                        }
                    } else {
                        Group {
                            if isInCart {
                                Image(systemName: "checkmark.circle.fill")
                                    .font(.title3)
                                    .foregroundColor(.fizTeal)
                            } else {
                                Text(storeManager.product(for: pack.packId)?.displayPrice ??
                                     String(format: "$%.2f", pack.price))
                                    .font(.title3)
                                    .fontWeight(.bold)
                                    .foregroundColor(.fizOrange)
                            }
                        }
                        .animation(.spring(response: 0.35, dampingFraction: 0.75), value: isInCart)
                    }

                    // Chevron
                    Image(systemName: isExpanded ? "chevron.up" : "chevron.down")
                        .font(.caption)
                        .foregroundColor(.fizBrown.opacity(0.5))
                }
            }
            .padding(.horizontal, 16)
            .padding(.vertical, 14)
        }
        .buttonStyle(.plain)
        .background(Color(.secondarySystemBackground))
    }

    // MARK: - Expanded Content
    private var expandedContent: some View {
        VStack(alignment: .leading, spacing: 12) {
            Divider()
                .padding(.horizontal, 16)

            // Description
            Text(pack.packDescription)
                .font(.body)
                .foregroundColor(.fizBrown.opacity(0.8))
                .fixedSize(horizontal: false, vertical: true)
                .padding(.horizontal, 16)

            // Subtopics Grid
            subtopicsSection
                .padding(.horizontal, 16)

            // Difficulty Breakdown
            HStack(spacing: 16) {
                DifficultyPill(difficulty: "Easy", count: pack.difficulty.easy, color: .green)
                DifficultyPill(difficulty: "Medium", count: pack.difficulty.medium, color: .orange)
                DifficultyPill(difficulty: "Hard", count: pack.difficulty.hard, color: .red)
            }
            .padding(.horizontal, 16)

            // Action Button
            actionButton
                .padding(.horizontal, 16)
                .padding(.bottom, 12)

            // Free preview note
            if !isPurchased {
                Text(freeQuestionText)
                    .font(.caption)
                    .foregroundColor(.fizBrown.opacity(0.6))
                    .padding(.horizontal, 16)
                    .padding(.bottom, 12)
            }
        }
        .transition(.opacity)
    }

    // MARK: - Subtopics Grid
    @ViewBuilder
    private var subtopicsSection: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text("Subtopics:")
                .font(.caption)
                .fontWeight(.semibold)
                .foregroundColor(.fizBrown)

            if !pack.subtopics.isEmpty {
                let columns = [GridItem(.adaptive(minimum: 100, maximum: 160), spacing: 8)]
                LazyVGrid(columns: columns, alignment: .leading, spacing: 8) {
                    ForEach(pack.subtopics, id: \.self) { subtopic in
                        Text(subtopic)
                            .font(.caption)
                            .fontWeight(.medium)
                            .foregroundColor(.fizBrown)
                            .multilineTextAlignment(.center)
                            .lineLimit(2)
                            .frame(maxWidth: .infinity, minHeight: 44, alignment: .center)
                            .padding(.horizontal, 12)
                            .padding(.vertical, 8)
                            .background(
                                RoundedRectangle(cornerRadius: 8)
                                    .fill(Color.fizOrange.opacity(0.15))
                            )
                    }
                }
            }
        }
    }

    // MARK: - Action Button
    @ViewBuilder
    private var actionButton: some View {
        if isPurchased {
            if isInstalled {
                Button(action: onUninstall) {
                    Text("Uninstall")
                        .font(.headline)
                        .frame(maxWidth: .infinity)
                        .padding()
                        .background(Color.fizBrown.opacity(0.2))
                        .foregroundColor(.fizBrown)
                        .cornerRadius(12)
                }
            } else {
                Button(action: onInstall) {
                    HStack {
                        Image(systemName: "arrow.down.circle.fill")
                        Text("Install")
                    }
                    .font(.headline)
                    .frame(maxWidth: .infinity)
                    .padding()
                    .background(Color.fizOrange)
                    .foregroundColor(.white)
                    .cornerRadius(12)
                }
            }
        } else {
            Button(action: {
                HapticManager.shared.buttonTapEffect()
                withAnimation(.spring(response: 0.35, dampingFraction: 0.75)) {
                    if isInCart {
                        cartManager.removeFromCart(packId: pack.packId)
                        AnalyticsManager.shared.trackPackRemovedFromCart(
                            packId: pack.packId,
                            packName: pack.packName,
                            totalItemsRemaining: cartManager.itemCount
                        )
                    } else {
                        cartManager.addToCart(packId: pack.packId)
                        AnalyticsManager.shared.trackPackAddedToCart(
                            packId: pack.packId,
                            packName: pack.packName
                        )
                    }
                }
            }) {
                HStack(spacing: 8) {
                    Image(systemName: isInCart ? "checkmark.circle.fill" : "bag.badge.plus")
                        .font(.headline)
                    Text(isInCart ? "Added to Bag" : "Add to Bag")
                        .font(.headline)
                }
                .frame(maxWidth: .infinity)
                .padding()
                .background(
                    RoundedRectangle(cornerRadius: 12)
                        .fill(isInCart ? Color.fizTeal : Color.fizOrange)
                )
                .foregroundColor(.white)
            }
            .buttonStyle(ScaleButtonStyle())
        }
    }

    // MARK: - Helpers
    private var freeQuestionText: String {
        let baseGameCount = expansionManager.countBaseGameQuestions(for: pack.packId)
        let totalFree = pack.freePreviewCount + baseGameCount

        let roundedCount: Int
        switch totalFree {
        case 0...9: roundedCount = totalFree
        case 10...24: roundedCount = 10
        case 25...39: roundedCount = 25
        case 40...49: roundedCount = 40
        case 50...59: roundedCount = 50
        case 60...74: roundedCount = 60
        case 75...99: roundedCount = 75
        default: roundedCount = 100
        }

        return "Try \(roundedCount)+ questions free"
    }
}

// MARK: - Supporting Views
private struct StatusBadge: View {
    let text: String
    let color: Color

    var body: some View {
        Text(text)
            .font(.caption)
            .fontWeight(.semibold)
            .foregroundColor(.white)
            .padding(.horizontal, 8)
            .padding(.vertical, 4)
            .background(color)
            .cornerRadius(6)
    }
}

private struct DifficultyPill: View {
    let difficulty: String
    let count: Int
    let color: Color

    var body: some View {
        HStack(spacing: 4) {
            Circle()
                .fill(color)
                .frame(width: 8, height: 8)
            Text("\(count)")
                .font(.caption)
                .fontWeight(.semibold)
            Text(difficulty)
                .font(.caption)
                .foregroundColor(.secondary)
        }
    }
}

// MARK: - Scale Button Style
private struct ScaleButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .scaleEffect(configuration.isPressed ? 0.97 : 1.0)
            .animation(.spring(response: 0.25, dampingFraction: 0.7), value: configuration.isPressed)
    }
}
