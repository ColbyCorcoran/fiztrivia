import SwiftUI

// MARK: - Shared Question Content Component
// Displays trivia questions with category header, question text, and answer options.
// Used in both inline display and modal presentation for consistent rendering.
struct QuestionContentView: View {
    let question: TriviaQuestion
    let selectedCategory: TriviaCategory?
    let onAnswerSelected: (String) -> Void
    @Environment(\.sizeCategory) private var sizeCategory

    // Adaptive grid: single column at accessibility sizes, 2 columns otherwise
    private var answerColumns: [GridItem] {
        if sizeCategory.isAccessibilitySize {
            return [GridItem(.flexible())]  // 1 column
        } else {
            return [GridItem(.flexible(), spacing: 12), GridItem(.flexible(), spacing: 12)]  // 2 columns
        }
    }

    var body: some View {
        VStack(spacing: 16) {
            VStack(spacing: 8) {
                // Show category with subcategory underneath
                VStack(spacing: 2) {
                    // Main category
                    if let category = selectedCategory {
                        HStack(spacing: 6) {
                            Image(systemName: category.icon)
                                .font(.title2)
                            Text(category.rawValue)
                                .font(.body)
                                .fontWeight(.semibold)
                        }
                        .foregroundColor(.secondary)
                    }

                    // Subcategory (smaller, underneath)
                    if let subcategory = question.subcategory {
                        Text(subcategory)
                            .font(.caption)
                            .fontWeight(.medium)
                            .foregroundColor(.secondary.opacity(0.7))
                    }
                }

                Text(question.question)
                    .font(.title3)
                    .fontWeight(.medium)
                    .foregroundColor(.primary)
                    .multilineTextAlignment(.center)
                    .lineLimit(nil)
                    .minimumScaleFactor(0.9)
                    .fixedSize(horizontal: false, vertical: true)
            }

            LazyVGrid(columns: answerColumns, spacing: 12) {
                ForEach(Array(question.options.enumerated()), id: \.offset) { index, option in
                    Button(action: {
                        onAnswerSelected(option)
                    }) {
                        Text(option)
                            .font(.headline)
                            .fontWeight(.medium)
                            .foregroundColor(.primary)
                            .multilineTextAlignment(.center)
                            .lineLimit(nil)
                            .fixedSize(horizontal: false, vertical: true)
                            .frame(maxWidth: .infinity, minHeight: 56)
                            .padding(.horizontal, 16)
                            .padding(.vertical, 14)
                            .background(Color.fizBackground)
                            .cornerRadius(12)
                            .shadow(color: Color.fizBrown.opacity(0.15), radius: 2, x: 0, y: 1)
                    }
                    .buttonStyle(.plain)
                }
            }
        }
        .padding(20)
    }
}

// MARK: - Preview
#Preview {
    QuestionContentView(
        question: TriviaQuestion(
            id: "test_001",
            category: "Science",
            subcategory: "Physics",
            question: "What is the speed of light in a vacuum?",
            options: ["299,792,458 m/s", "300,000,000 m/s", "186,282 mi/s", "150,000,000 m/s"],
            correctAnswer: "299,792,458 m/s",
            difficulty: "medium"
        ),
        selectedCategory: .science,
        onAnswerSelected: { answer in
            print("Selected: \(answer)")
        }
    )
    .preferredColorScheme(.light)
}
