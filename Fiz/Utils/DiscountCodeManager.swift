//
//  DiscountCodeManager.swift
//  Fiz
//
//  Manages promotional discount codes for expansion packs
//

import Foundation
import Combine

enum DiscountType {
    case percentage(Int) // e.g., 100 = 100% off
    case dollarAmount(Double) // e.g., 5.00 = $5 off
}

struct DiscountCode {
    let code: String
    let type: DiscountType
    let description: String
}

class DiscountCodeManager: ObservableObject {
    static let shared = DiscountCodeManager()

    private init() {}

    // MARK: - Predefined Discount Codes

    private let availableCodes: [String: DiscountCode] = [
        // Developer testing codes
        "DEVELOPER": DiscountCode(
            code: "DEVELOPER",
            type: .percentage(100),
            description: "Developer: Free pack"
        ),
        "TESTING": DiscountCode(
            code: "TESTING",
            type: .percentage(100),
            description: "Testing: Free pack"
        ),

        // Loyalty/promotional codes
        "LOYAL10": DiscountCode(
            code: "LOYAL10",
            type: .percentage(10),
            description: "Loyalty: 10% off"
        ),
        "LOYAL25": DiscountCode(
            code: "LOYAL25",
            type: .percentage(25),
            description: "Loyalty: 25% off"
        ),
        "LOYAL50": DiscountCode(
            code: "LOYAL50",
            type: .percentage(50),
            description: "Loyalty: 50% off"
        ),
        "FREEPACK": DiscountCode(
            code: "FREEPACK",
            type: .percentage(100),
            description: "Promotional: Free pack"
        ),

        // Dollar amount discounts
        "SAVE1": DiscountCode(
            code: "SAVE1",
            type: .dollarAmount(1.00),
            description: "$1 off your order"
        ),
        "SAVE2": DiscountCode(
            code: "SAVE2",
            type: .dollarAmount(2.00),
            description: "$2 off your order"
        ),
        "SAVE5": DiscountCode(
            code: "SAVE5",
            type: .dollarAmount(5.00),
            description: "$5 off your order"
        )
    ]

    // MARK: - Code Validation

    func validateCode(_ code: String) -> DiscountCode? {
        let upperCode = code.uppercased().trimmingCharacters(in: .whitespacesAndNewlines)
        return availableCodes[upperCode]
    }

    func calculateDiscount(code: DiscountCode, subtotal: Double) -> Double {
        switch code.type {
        case .percentage(let percent):
            return subtotal * (Double(percent) / 100.0)
        case .dollarAmount(let amount):
            return min(amount, subtotal) // Can't discount more than subtotal
        }
    }

    // MARK: - Helper Methods

    func getDiscountDescription(code: DiscountCode) -> String {
        switch code.type {
        case .percentage(let percent):
            return "\(percent)% off"
        case .dollarAmount(let amount):
            return String(format: "$%.2f off", amount)
        }
    }
}
