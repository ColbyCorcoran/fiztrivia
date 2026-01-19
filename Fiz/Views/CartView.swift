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
    @StateObject private var discountManager = DiscountCodeManager.shared

    @State private var discountCodeInput = ""
    @State private var appliedDiscount: DiscountCode?
    @State private var showingInvalidCodeAlert = false
    @State private var isPurchasing = false
    @State private var showingSuccessAlert = false
    @State private var showingErrorAlert = false
    @State private var errorMessage = ""
    @State private var showingClearBagAlert = false

    private var cartPacks: [ExpansionPack] {
        expansionManager.availablePacks.filter { cartManager.isInCart(packId: $0.packId) }
    }

    private var subtotal: Double {
        cartManager.calculateSubtotal(for: expansionManager.availablePacks)
    }

    private var discount: Double {
        guard let code = appliedDiscount else { return 0 }
        return discountManager.calculateDiscount(code: code, subtotal: subtotal)
    }

    private var total: Double {
        cartManager.calculateTotal(subtotal: subtotal, discount: discount)
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

                            // Discount code section
                            discountCodeSection

                            // Price breakdown
                            priceBreakdownSection

                            // Purchase button
                            purchaseButton

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
            .alert("Invalid Code", isPresented: $showingInvalidCodeAlert) {
                Button("OK", role: .cancel) { }
            } message: {
                Text("The discount code '\(discountCodeInput)' is not valid.")
            }
            .alert("Purchase Complete!", isPresented: $showingSuccessAlert) {
                Button("OK") {
                    dismiss()
                }
            } message: {
                Text("Your expansion packs have been purchased and installed successfully!")
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
                    appliedDiscount = nil
                    discountCodeInput = ""
                    AnalyticsManager.shared.trackCartCleared(itemsCleared: itemsCleared)
                }
            } message: {
                Text("This will remove all \(cartPacks.count) item\(cartPacks.count == 1 ? "" : "s") from your shopping bag.")
            }
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

    private var discountCodeSection: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text("Discount Code")
                .font(.headline)
                .foregroundColor(.fizBrown)

            HStack(spacing: 12) {
                TextField("Enter code", text: $discountCodeInput)
                    .textFieldStyle(.roundedBorder)
                    .textInputAutocapitalization(.characters)
                    .autocorrectionDisabled()

                Button(action: applyDiscountCode) {
                    Text("Apply")
                        .font(.headline)
                        .foregroundColor(.white)
                        .padding(.horizontal, 20)
                        .padding(.vertical, 8)
                        .background(Color.fizOrange)
                        .cornerRadius(8)
                }
                .disabled(discountCodeInput.isEmpty)
            }

            if let discount = appliedDiscount {
                HStack {
                    Image(systemName: "checkmark.circle.fill")
                        .foregroundColor(.green)
                    Text("\(discountManager.getDiscountDescription(code: discount)) applied")
                        .font(.caption)
                        .foregroundColor(.green)

                    Spacer()

                    Button(action: removeDiscount) {
                        Text("Remove")
                            .font(.caption)
                            .foregroundColor(.red)
                    }
                }
                .padding(.top, 4)
            }
        }
        .padding()
        .background(Color(.secondarySystemBackground))
        .cornerRadius(12)
    }

    private var priceBreakdownSection: some View {
        VStack(spacing: 12) {
            // Subtotal
            HStack {
                Text("Subtotal")
                    .font(.body)
                    .foregroundColor(.fizBrown)
                Spacer()
                Text(String(format: "$%.2f", subtotal))
                    .font(.body)
                    .fontWeight(.semibold)
                    .foregroundColor(.fizBrown)
            }

            // Discount
            if discount > 0 {
                HStack {
                    Text("Discount")
                        .font(.body)
                        .foregroundColor(.green)
                    Spacer()
                    Text("-\(String(format: "$%.2f", discount))")
                        .font(.body)
                        .fontWeight(.semibold)
                        .foregroundColor(.green)
                }
            }

            Divider()

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

    private var purchaseButton: some View {
        Button(action: {
            Task {
                await purchaseAll()
            }
        }) {
            HStack {
                if isPurchasing {
                    ProgressView()
                        .progressViewStyle(CircularProgressViewStyle(tint: .white))
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

    private func applyDiscountCode() {
        HapticManager.shared.buttonTapEffect()

        if let code = discountManager.validateCode(discountCodeInput) {
            appliedDiscount = code
            let discountAmount = discountManager.calculateDiscount(code: code, subtotal: subtotal)
            AnalyticsManager.shared.trackDiscountCodeApplied(
                codeType: discountManager.getDiscountDescription(code: code),
                discountAmount: discountAmount
            )
            print("✅ Applied discount: \(code.description)")
        } else {
            AnalyticsManager.shared.trackDiscountCodeInvalid()
            showingInvalidCodeAlert = true
        }
    }

    private func removeDiscount() {
        HapticManager.shared.lightImpact()
        appliedDiscount = nil
        discountCodeInput = ""
        AnalyticsManager.shared.trackDiscountCodeRemoved()
    }

    private func purchaseAll() async {
        // Track checkout initiated
        AnalyticsManager.shared.trackCheckoutInitiated(
            itemCount: cartPacks.count,
            subtotal: subtotal,
            hasDiscount: appliedDiscount != nil
        )

        isPurchasing = true

        var successCount = 0
        var failedPacks: [String] = []

        // Purchase each pack sequentially
        for pack in cartPacks {
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
                hadDiscount: appliedDiscount != nil
            )

            cartManager.clearCart()
            appliedDiscount = nil
            discountCodeInput = ""
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
