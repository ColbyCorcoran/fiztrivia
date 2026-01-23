//
//  CartView.swift
//  Fiz
//
//  Shopping cart for expansion pack purchases
//

import SwiftUI
import StoreKit

struct CartView: View {
    @Environment(\.dismiss) var dismiss
    @StateObject private var cartManager = CartManager.shared
    @StateObject private var expansionManager = ExpansionPackManager.shared
    @StateObject private var storeManager = StoreManager.shared

    @State private var isPurchasing = false
    @State private var showingSuccessAlert = false
    @State private var showingErrorAlert = false
    @State private var errorMessage = ""
    @State private var showingClearBagAlert = false
    @State private var showingCheckoutWarning = false
    @State private var purchaseProgress: Int = 0
    @State private var showingOfferCodeRedemption = false

    private var cartPacks: [ExpansionPack] {
        expansionManager.availablePacks.filter { cartManager.isInCart(packId: $0.packId) }
    }

    private var total: Double {
        cartManager.calculateSubtotal(for: expansionManager.availablePacks)
    }

    var body: some View {
        NavigationView {
            ZStack {
                // Background gradient
                LinearGradient(
                    gradient: Gradient(colors: [
                        Color.fizBackground,
                        Color.fizBackgroundSecondary
                    ]),
                    startPoint: .topLeading,
                    endPoint: .bottomTrailing
                )
                .ignoresSafeArea()

                if cartPacks.isEmpty {
                    emptyCartView
                } else {
                    ScrollView {
                        VStack(spacing: 20) {
                            // Cart items
                            ForEach(cartPacks) { pack in
                                CartItemRow(
                                    pack: pack,
                                    onRemove: {
                                        HapticManager.shared.lightImpact()
                                        cartManager.removeFromCart(packId: pack.packId)
                                        AnalyticsManager.shared.trackPackRemovedFromCart(
                                            packId: pack.packId,
                                            packName: pack.packName,
                                            totalItemsRemaining: cartManager.itemCount
                                        )
                                    }
                                )
                            }

                            // Offer code redemption button
                            offerCodeSection

                            // Price breakdown
                            priceBreakdownSection

                            // Purchase button
                            purchaseButton

                            // Legal links
                            legalLinksSection

                            Spacer(minLength: 20)
                        }
                        .padding()
                    }
                }
            }
            .navigationTitle("Shopping Bag")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                // Clear Bag button (leading)
                if !cartPacks.isEmpty {
                    ToolbarItem(placement: .navigationBarLeading) {
                        Button(action: {
                            showingClearBagAlert = true
                        }) {
                            Text("Clear Bag")
                                .font(.body)
                        }
                        .tint(.red)
                    }
                }

                // Done button (trailing)
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button(action: {
                        dismiss()
                    }) {
                        Image(systemName: "checkmark")
                            .font(.body.weight(.semibold))
                    }
                    .tint(.fizOrange)
                }
            }
            .presentationDragIndicator(.visible)
            .alert("Ready to Purchase?", isPresented: $showingCheckoutWarning) {
                Button("Cancel", role: .cancel) { }
                Button("Continue") {
                    Task {
                        await purchaseAll()
                    }
                }
            } message: {
                if cartPacks.count > 1 {
                    Text("You'll be prompted \(cartPacks.count) times by the App Store to complete your purchase (once for each pack). This is normal for multiple pack purchases.")
                } else {
                    Text("You'll be prompted once by the App Store to complete your purchase.")
                }
            }
            .alert("Purchase Complete!", isPresented: $showingSuccessAlert) {
                Button("OK") {
                    dismiss()
                }
            } message: {
                let packCount = purchaseProgress
                if packCount > 1 {
                    Text("All \(packCount) expansion packs have been purchased and installed! They're now part of the game and ready to play in Single Topic Mode.")
                } else {
                    Text("Your expansion pack has been purchased and installed! It's now part of the game and ready to play in Single Topic Mode.")
                }
            }
            .alert("Purchase Failed", isPresented: $showingErrorAlert) {
                Button("OK", role: .cancel) { }
            } message: {
                Text(errorMessage)
            }
            .alert("Clear Shopping Bag?", isPresented: $showingClearBagAlert) {
                Button("Cancel", role: .cancel) { }
                Button("Clear Bag", role: .destructive) {
                    HapticManager.shared.lightImpact()
                    let itemsCleared = cartPacks.count
                    cartManager.clearCart()
                    AnalyticsManager.shared.trackCartCleared(itemsCleared: itemsCleared)
                }
            } message: {
                Text("This will remove all \(cartPacks.count) item\(cartPacks.count == 1 ? "" : "s") from your shopping bag.")
            }
            .offerCodeRedemption(isPresented: $showingOfferCodeRedemption)
            .onAppear {
                AnalyticsManager.shared.trackCartViewed(itemCount: cartPacks.count)
            }
        }
    }

    // MARK: - Subviews

    private var emptyCartView: some View {
        VStack(spacing: 16) {
            Image(systemName: "bag")
                .font(.system(size: 60))
                .foregroundColor(.fizBrown.opacity(0.5))

            Text("Your bag is empty")
                .font(.title2)
                .fontWeight(.semibold)
                .foregroundColor(.fizBrown)

            Text("Add some expansion packs to get started!")
                .font(.body)
                .foregroundColor(.fizBrown.opacity(0.7))
                .multilineTextAlignment(.center)
        }
        .padding(40)
    }

    private var offerCodeSection: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text("Have an Offer Code?")
                .font(.headline)
                .foregroundColor(.fizBrown)

            Button(action: {
                showingOfferCodeRedemption = true
            }) {
                HStack {
                    Image(systemName: "tag.fill")
                    Text("Redeem Offer Code")
                        .font(.headline)
                }
                .frame(maxWidth: .infinity)
                .padding()
                .background(Color.fizOrange)
                .foregroundColor(.white)
                .cornerRadius(12)
            }
        }
        .padding()
        .background(Color(.secondarySystemBackground))
        .cornerRadius(12)
    }

    private var priceBreakdownSection: some View {
        VStack(spacing: 12) {
            // Total
            HStack {
                Text("Total")
                    .font(.title3)
                    .fontWeight(.bold)
                    .foregroundColor(.fizBrown)
                Spacer()
                Text(String(format: "$%.2f", total))
                    .font(.title3)
                    .fontWeight(.bold)
                    .foregroundColor(.fizOrange)
            }
        }
        .padding()
        .background(Color(.secondarySystemBackground))
        .cornerRadius(12)
    }

    private var legalLinksSection: some View {
        VStack(spacing: 8) {
            HStack(spacing: 16) {
                Link(destination: URL(string: "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/")!) {
                    Text("Terms of Service")
                        .font(.caption)
                        .foregroundColor(.fizOrange)
                }

                Text("•")
                    .font(.caption)
                    .foregroundColor(.secondary)

                Link(destination: URL(string: "https://www.apple.com/legal/privacy/")!) {
                    Text("Privacy Policy")
                        .font(.caption)
                        .foregroundColor(.fizOrange)
                }
            }
        }
        .frame(maxWidth: .infinity)
        .padding(.vertical, 8)
    }

    private var purchaseButton: some View {
        Button(action: {
            showingCheckoutWarning = true
        }) {
            HStack {
                if isPurchasing {
                    ProgressView()
                        .progressViewStyle(CircularProgressViewStyle(tint: .white))
                    if cartPacks.count > 1 {
                        Text("Purchasing \(purchaseProgress) of \(cartPacks.count)...")
                    } else {
                        Text("Purchasing...")
                    }
                } else {
                    Image(systemName: "cart.fill")
                    Text("Purchase All (\(cartPacks.count) \(cartPacks.count == 1 ? "item" : "items"))")
                }
            }
            .font(.headline)
            .frame(maxWidth: .infinity)
            .padding()
            .background(isPurchasing ? Color.gray : Color.fizOrange)
            .foregroundColor(.white)
            .cornerRadius(12)
        }
        .disabled(isPurchasing)
    }

    // MARK: - Actions

    private func purchaseAll() async {
        // Track checkout initiated
        AnalyticsManager.shared.trackCheckoutInitiated(
            itemCount: cartPacks.count,
            subtotal: total,
            hasDiscount: false
        )

        isPurchasing = true
        purchaseProgress = 0

        var successCount = 0
        var failedPacks: [String] = []

        // Purchase each pack sequentially
        for (index, pack) in cartPacks.enumerated() {
            purchaseProgress = index + 1

            guard let product = storeManager.product(for: pack.packId) else {
                failedPacks.append(pack.packName)
                continue
            }

            let success = await storeManager.purchase(product)
            if success {
                successCount += 1
                // Auto-install after purchase
                ExpansionPackManager.shared.installPack(packId: pack.packId)
            } else {
                failedPacks.append(pack.packName)
            }
        }

        isPurchasing = false

        if successCount == cartPacks.count {
            // All successful
            HapticManager.shared.correctAnswerEffect()

            // Track successful checkout
            AnalyticsManager.shared.trackCheckoutCompleted(
                itemCount: cartPacks.count,
                total: total,
                hadDiscount: false
            )

            cartManager.clearCart()
            showingSuccessAlert = true
        } else if successCount > 0 {
            // Partial success
            errorMessage = "Successfully purchased \(successCount) pack(s). Failed: \(failedPacks.joined(separator: ", "))"

            // Track partial failure
            AnalyticsManager.shared.trackCheckoutFailed(
                itemCount: cartPacks.count,
                failureReason: "partial_failure"
            )

            // Remove successful items from cart
            for pack in cartPacks {
                if expansionManager.isPurchased(packId: pack.packId) {
                    cartManager.removeFromCart(packId: pack.packId)
                }
            }
            showingErrorAlert = true
        } else {
            // All failed
            errorMessage = "Failed to purchase packs. Please try again."

            // Track complete failure
            AnalyticsManager.shared.trackCheckoutFailed(
                itemCount: cartPacks.count,
                failureReason: "all_failed"
            )

            showingErrorAlert = true
        }
    }
}

// MARK: - Cart Item Row

struct CartItemRow: View {
    let pack: ExpansionPack
    let onRemove: () -> Void

    @StateObject private var storeManager = StoreManager.shared

    private var product: Product? {
        storeManager.product(for: pack.packId)
    }

    var body: some View {
        HStack(spacing: 12) {
            Image(systemName: pack.icon)
                .font(.title2)
                .foregroundColor(.fizOrange)
                .frame(width: 40, height: 40)

            VStack(alignment: .leading, spacing: 4) {
                Text(pack.packName)
                    .font(.headline)
                    .foregroundColor(.fizBrown)

                Text("\(pack.questionCount) questions")
                    .font(.caption)
                    .foregroundColor(.fizBrown.opacity(0.7))
            }

            Spacer()

            VStack(alignment: .trailing, spacing: 4) {
                Text(product?.displayPrice ?? String(format: "$%.2f", pack.price))
                    .font(.headline)
                    .fontWeight(.bold)
                    .foregroundColor(.fizOrange)

                Button(action: onRemove) {
                    Text("Remove")
                        .font(.caption)
                        .foregroundColor(.red)
                }
            }
        }
        .padding()
        .background(Color(.secondarySystemBackground))
        .cornerRadius(12)
    }
}

#Preview {
    CartView()
}
