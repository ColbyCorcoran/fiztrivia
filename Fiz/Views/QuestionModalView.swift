import SwiftUI

// MARK: - Question Modal View
// Presents trivia questions in a scrollable modal for users with large Dynamic Type sizes.
// This ensures all content remains readable and accessible even with maximum text sizes.
// Modal cannot be dismissed manually - users must answer the question first.
struct QuestionModalView: View {
    @Binding var isPresented: Bool
    let question: TriviaQuestion?
    let selectedCategory: TriviaCategory?
    let answerResult: AnswerState
    let showingResult: Bool
    let onAnswerSelected: (String) -> Void
    let onDismiss: () -> Void

    // MARK: - Background Gradient
    private var backgroundGradient: some View {
        LinearGradient(
            colors: [Color.fizBackground, Color.fizBackgroundSecondary],
            startPoint: .topLeading,
            endPoint: .bottomTrailing
        )
        .ignoresSafeArea()
    }

    var body: some View {
        ZStack {
            // Background gradient matching app design
            backgroundGradient

            // Content
            ScrollView {
                if showingResult {
                    // Show result after answer selected
                    ResultContentView(
                        answerResult: answerResult,
                        currentQuestion: question,
                        showingResult: showingResult
                    )
                    .padding(.top, 8)
                } else if let question = question {
                    // Show question
                    QuestionContentView(
                        question: question,
                        selectedCategory: selectedCategory,
                        onAnswerSelected: onAnswerSelected
                    )
                    .padding(.top, 8)
                }
            }
        }
    }
}

// MARK: - Preview
#Preview("Question State") {
    QuestionModalView(
        isPresented: .constant(true),
        question: TriviaQuestion(
            id: "test_001",
            category: "Science",
            subcategory: "Physics",
            question: "What is the Heisenberg Uncertainty Principle?",
            options: [
                "You cannot simultaneously know a particle's exact position and momentum",
                "Light behaves as both a wave and particle",
                "Energy cannot be created or destroyed",
                "Objects in motion stay in motion"
            ],
            correctAnswer: "You cannot simultaneously know a particle's exact position and momentum",
            difficulty: "hard"
        ),
        selectedCategory: .science,
        answerResult: .unanswered,
        showingResult: false,
        onAnswerSelected: { answer in
            print("Selected: \(answer)")
        },
        onDismiss: {
            print("Modal dismissed")
        }
    )
}

#Preview("Result State - Correct") {
    QuestionModalView(
        isPresented: .constant(true),
        question: TriviaQuestion(
            id: "test_001",
            category: "Science",
            subcategory: "Physics",
            question: "What is the Heisenberg Uncertainty Principle?",
            options: [
                "You cannot simultaneously know a particle's exact position and momentum",
                "Light behaves as both a wave and particle",
                "Energy cannot be created or destroyed",
                "Objects in motion stay in motion"
            ],
            correctAnswer: "You cannot simultaneously know a particle's exact position and momentum",
            difficulty: "hard"
        ),
        selectedCategory: .science,
        answerResult: .correct,
        showingResult: true,
        onAnswerSelected: { answer in
            print("Selected: \(answer)")
        },
        onDismiss: {
            print("Modal dismissed")
        }
    )
}
