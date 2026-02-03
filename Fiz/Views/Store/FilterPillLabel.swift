//
//  FilterPillLabel.swift
//  Fiz
//
//  Created by Claude on 2/3/26.
//

import SwiftUI

struct FilterPillLabel: View {
    let icon: String
    let text: String
    let isActive: Bool
    var color: Color = .fizOrange

    var body: some View {
        HStack(spacing: 6) {
            Image(systemName: icon)
                .font(.caption)
            Text(text)
                .font(.subheadline)
                .fontWeight(.medium)
        }
        .padding(.horizontal, 14)
        .padding(.vertical, 8)
        .background(
            RoundedRectangle(cornerRadius: 20)
                .fill(isActive ? color.opacity(0.2) : Color(.tertiarySystemFill))
        )
        .foregroundColor(isActive ? color : .primary.opacity(0.7))
        .overlay(
            RoundedRectangle(cornerRadius: 20)
                .strokeBorder(isActive ? color : Color.clear, lineWidth: 1.5)
        )
        .padding(2)
    }
}
