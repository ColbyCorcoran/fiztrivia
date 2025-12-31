//
//  StoreManager.swift
//  Fiz
//
//  Created by Claude Code on 12/31/24.
//

import Foundation
import StoreKit

@MainActor
class StoreManager: ObservableObject {
    static let shared = StoreManager()

    @Published private(set) var products: [Product] = []
    @Published private(set) var purchasedProductIDs: Set<String> = []
    @Published private(set) var isLoading = false
    @Published var errorMessage: String?

    private var updateListenerTask: Task<Void, Error>?

    private let productIDs = [
        "com.fiz.pack.harry_potter",
        "com.fiz.pack.pokemon",
        "com.fiz.pack.80s_trivia",
        "com.fiz.pack.disney",
        "com.fiz.pack.the_office"
    ]

    private init() {
        // Start listening for transaction updates
        updateListenerTask = listenForTransactions()

        Task {
            await loadProducts()
            await updatePurchasedProducts()
        }
    }

    deinit {
        updateListenerTask?.cancel()
    }

    // MARK: - Load Products

    func loadProducts() async {
        isLoading = true
        defer { isLoading = false }

        do {
            let storeProducts = try await Product.products(for: productIDs)
            products = storeProducts.sorted { $0.price < $1.price }
            print("Loaded \(products.count) products from the App Store")
        } catch {
            errorMessage = "Failed to load products: \(error.localizedDescription)"
            print("Error loading products: \(error)")
        }
    }

    // MARK: - Purchase Product

    func purchase(_ product: Product) async -> Bool {
        do {
            let result = try await product.purchase()

            switch result {
            case .success(let verification):
                // Verify the transaction
                let transaction = try checkVerified(verification)

                // Update purchased products
                await updatePurchasedProducts()

                // Update ExpansionPackManager
                ExpansionPackManager.shared.unlockPack(packId: product.id)

                // Finish the transaction
                await transaction.finish()

                // Track analytics
                AnalyticsManager.shared.trackExpansionPackPurchased(packId: product.id)

                return true

            case .userCancelled:
                print("User cancelled purchase")
                return false

            case .pending:
                print("Purchase is pending approval")
                errorMessage = "Purchase is pending approval"
                return false

            @unknown default:
                print("Unknown purchase result")
                return false
            }
        } catch {
            errorMessage = "Purchase failed: \(error.localizedDescription)"
            print("Error during purchase: \(error)")
            return false
        }
    }

    // MARK: - Restore Purchases

    func restorePurchases() async -> Bool {
        do {
            try await AppStore.sync()
            await updatePurchasedProducts()
            print("✅ Purchases restored successfully")
            return true
        } catch {
            errorMessage = "Failed to restore purchases: \(error.localizedDescription)"
            print("❌ Error restoring purchases: \(error)")
            return false
        }
    }

    // MARK: - Update Purchased Products

    func updatePurchasedProducts() async {
        var purchased: Set<String> = []

        for await result in Transaction.currentEntitlements {
            do {
                let transaction = try checkVerified(result)

                // Check if this transaction is for one of our products
                if productIDs.contains(transaction.productID) {
                    purchased.insert(transaction.productID)
                }
            } catch {
                print("Error verifying transaction: \(error)")
            }
        }

        purchasedProductIDs = purchased

        // Sync with ExpansionPackManager
        for productID in purchased {
            ExpansionPackManager.shared.unlockPack(packId: productID)
        }
    }

    // MARK: - Transaction Listener

    private func listenForTransactions() -> Task<Void, Error> {
        return Task {
            // Iterate through any transactions that don't come from a direct call to purchase()
            for await result in Transaction.updates {
                do {
                    let transaction = try checkVerified(result)

                    // Deliver products to the user
                    await updatePurchasedProducts()

                    // Always finish a transaction
                    await transaction.finish()
                } catch {
                    print("Transaction verification failed: \(error)")
                }
            }
        }
    }

    // MARK: - Verification

    private func checkVerified<T>(_ result: VerificationResult<T>) throws -> T {
        switch result {
        case .unverified:
            throw StoreError.failedVerification
        case .verified(let safe):
            return safe
        }
    }

    // MARK: - Helper Methods

    func isPurchased(_ productID: String) -> Bool {
        return purchasedProductIDs.contains(productID)
    }

    func product(for packId: String) -> Product? {
        return products.first { $0.id == packId }
    }
}

// MARK: - Store Errors

enum StoreError: Error {
    case failedVerification
}
