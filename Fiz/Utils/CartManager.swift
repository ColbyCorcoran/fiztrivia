//
//  CartManager.swift
//  Fiz
//
//  Shopping cart management for expansion pack purchases
//

import Foundation
import Combine

class CartManager: ObservableObject {
    static let shared = CartManager()

    @Published private(set) var cartItems: Set<String> = [] // Pack IDs in cart

    private init() {
        // Load cart from UserDefaults
        if let savedCart = UserDefaults.standard.array(forKey: "cart_items") as? [String] {
            cartItems = Set(savedCart)
        }
    }

    // MARK: - Cart Operations

    func addToCart(packId: String) {
        cartItems.insert(packId)
        saveCart()
        print("✅ Added \(packId) to cart. Total items: \(cartItems.count)")
    }

    func removeFromCart(packId: String) {
        cartItems.remove(packId)
        saveCart()
        print("❌ Removed \(packId) from cart. Total items: \(cartItems.count)")
    }

    func isInCart(packId: String) -> Bool {
        return cartItems.contains(packId)
    }

    func clearCart() {
        cartItems.removeAll()
        saveCart()
        print("🗑️ Cart cleared")
    }

    var itemCount: Int {
        return cartItems.count
    }

    // MARK: - Price Calculations

    func calculateSubtotal(for packs: [ExpansionPack]) -> Double {
        let cartPacks = packs.filter { cartItems.contains($0.packId) }
        return cartPacks.reduce(0) { $0 + $1.price }
    }

    func calculateTotal(subtotal: Double, discount: Double) -> Double {
        return max(0, subtotal - discount)
    }

    // MARK: - Persistence

    private func saveCart() {
        UserDefaults.standard.set(Array(cartItems), forKey: "cart_items")
    }
}
