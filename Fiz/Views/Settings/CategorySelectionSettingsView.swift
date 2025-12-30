import SwiftUI

struct CategorySelectionSettingsView: View {
    @StateObject private var categoryManager = CategorySelectionManager.shared
    @State private var showMaxReachedAlert = false
    @State private var showMinimumAlert = false
    @State private var showActiveCategoryAlert = false
    @State private var confirmationMessage: String? = nil
    @Environment(\.sizeCategory) private var sizeCategory

    private var backgroundGradient: some View {
        Color(.systemGroupedBackground)
            .ignoresSafeArea()
    }

    var body: some View {
        ZStack {
            Form {
                Section {
                    HStack {
                        Text("Selected Categories")
                            .font(.headline)
                        Spacer()
                        Text("\(categoryManager.selectedCategories.count)/\(CategorySelectionManager.maximumCategories)")
                            .font(.headline)
                            .foregroundColor(categoryManager.selectedCategories.count >= CategorySelectionManager.maximumCategories ? .orange : .secondary)
                    }
                    .padding(.vertical, 4)
                }

                Section(footer: Text("Select \(CategorySelectionManager.minimumCategories)-\(CategorySelectionManager.maximumCategories) categories to appear on the wheel. Deselected categories will be hidden.")) {
                    ForEach(TriviaCategory.allCases, id: \.self) { category in
                        CategorySelectionRow(
                            category: category,
                            isSelected: categoryManager.isSelected(category),
                            canToggle: categoryManager.canToggle(category),
                            onToggle: {
                                let success = categoryManager.toggleCategory(category)
                                if !success {
                                    // Determine which alert to show
                                    if categoryManager.selectedCategories.contains(category) {
                                        // Trying to deselect but can't
                                        if GameModeManager.shared.isSingleCategoryMode &&
                                           GameModeManager.shared.selectedCategory == category {
                                            showActiveCategoryAlert = true
                                        } else {
                                            showMinimumAlert = true
                                        }
                                    } else {
                                        showMaxReachedAlert = true
                                    }
                                    HapticManager.shared.incorrectAnswerEffect()
                                } else {
                                    HapticManager.shared.buttonTapEffect()
                                }
                            }
                        )
                    }
                }

                Section {
                    // Save current selection as user's custom default
                    Button(action: {
                        categoryManager.saveCurrentAsDefault()
                        HapticManager.shared.buttonTapEffect()
                        showConfirmation("Selection saved as your new default ✓")
                    }) {
                        HStack {
                            Image(systemName: "bookmark.fill")
                            Text("Save selection as my default")
                        }
                        .foregroundColor(.fizOrange)
                    }

                    // Reset to user's custom default (only shown if they have one saved)
                    if categoryManager.hasCustomDefault() {
                        Button(action: {
                            categoryManager.resetToMyDefault()
                            HapticManager.shared.buttonTapEffect()
                            AnalyticsManager.shared.trackCategorySelectionReset()
                            showConfirmation("Reset to your saved default ✓")
                        }) {
                            HStack {
                                Image(systemName: "arrow.counterclockwise")
                                Text("Reset to my default")
                            }
                            .foregroundColor(.fizOrange)
                        }
                    }

                    // Reset to factory default (all 12 categories)
                    Button(action: {
                        categoryManager.resetToFactoryDefault()
                        HapticManager.shared.buttonTapEffect()
                        AnalyticsManager.shared.trackCategorySelectionReset()
                        showConfirmation("Reset to original default ✓")
                    }) {
                        HStack {
                            Image(systemName: "arrow.uturn.backward")
                            Text("Reset to original default")
                        }
                        .foregroundColor(.fizOrange)
                    }
                }
            }
            .scrollContentBackground(.hidden)
            .background(backgroundGradient)

            // Confirmation message overlay
            if let message = confirmationMessage {
                VStack {
                    Spacer()
                    Text(message)
                        .font(.body)
                        .foregroundColor(.white)
                        .padding(.horizontal, 20)
                        .padding(.vertical, 12)
                        .background(Color.fizOrange)
                        .cornerRadius(10)
                        .shadow(radius: 5)
                        .padding(.bottom, 80)
                }
                .transition(.move(edge: .bottom).combined(with: .opacity))
                .animation(.easeInOut(duration: 0.3), value: confirmationMessage)
            }
        }
        .navigationTitle("Category Selection")
        .navigationBarTitleDisplayMode(.large)
        .alert("Maximum Reached", isPresented: $showMaxReachedAlert) {
            Button("OK", role: .cancel) { }
        } message: {
            Text("You can select up to \(CategorySelectionManager.maximumCategories) categories. Deselect one to add another.")
        }
        .alert("Minimum Required", isPresented: $showMinimumAlert) {
            Button("OK", role: .cancel) { }
        } message: {
            Text("You must have at least \(CategorySelectionManager.minimumCategories) categories selected for gameplay.")
        }
        .alert("Cannot Deselect", isPresented: $showActiveCategoryAlert) {
            Button("OK", role: .cancel) { }
        } message: {
            Text("This category is currently active in Single Category Mode. Disable Single Category Mode first, or switch to a different category.")
        }
    }

    private func showConfirmation(_ message: String) {
        confirmationMessage = message

        // Auto-dismiss after 2 seconds
        DispatchQueue.main.asyncAfter(deadline: .now() + 2.0) {
            confirmationMessage = nil
        }
    }
}

struct CategorySelectionRow: View {
    let category: TriviaCategory
    let isSelected: Bool
    let canToggle: Bool
    let onToggle: () -> Void

    @Environment(\.sizeCategory) private var sizeCategory

    var body: some View {
        Button(action: onToggle) {
            HStack(spacing: 12) {
                Image(systemName: category.icon)
                    .font(.title2)
                    .foregroundColor(Color(hex: category.color))
                    .frame(width: 32)

                Text(category.rawValue)
                    .font(.body)
                    .foregroundColor(.primary)

                Spacer()

                if isSelected {
                    Image(systemName: "checkmark.circle.fill")
                        .font(.title3)
                        .foregroundColor(.fizOrange)
                } else {
                    Image(systemName: "circle")
                        .font(.title3)
                        .foregroundColor(.secondary.opacity(0.3))
                }
            }
            .contentShape(Rectangle())
            .opacity(canToggle || isSelected ? 1.0 : 0.5)
        }
        .buttonStyle(.plain)
    }
}

#Preview {
    NavigationStack {
        CategorySelectionSettingsView()
    }
}
