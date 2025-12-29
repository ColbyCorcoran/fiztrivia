import SwiftUI

// MARK: - Shared Result Content Component
// Displays trivia answer results with Fiz mascot and personalized messaging.
// Used in both inline display and modal presentation for consistent feedback.
struct ResultContentView: View {
    let answerResult: AnswerState
    let currentQuestion: TriviaQuestion?
    let showingResult: Bool

    @StateObject private var userManager = UserManager.shared

    var body: some View {
        VStack(spacing: 20) {
            // Fiz mascot - celebrating or encouraging (TOP, larger)
            Image(answerResult == .correct ? "fiz-correct" : "fiz-incorrect")
                .resizable()
                .scaledToFit()
                .frame(width: 180, height: 180)
                .scaleEffect(showingResult ? 1.0 : 0.5)
                .animation(.spring(response: 0.6, dampingFraction: 0.6), value: showingResult)

            // For correct answers: simple centered text
            if answerResult == .correct {
                Text(userManager.personalizedCongratulatoryMessage())
                    .font(.title)
                    .fontWeight(.bold)
                    .foregroundColor(.primary)
                    .multilineTextAlignment(.center)
                    .lineLimit(nil)
                    .minimumScaleFactor(0.7)
                    .padding(.horizontal, 20)
            }

            // For incorrect answers: centered text with answer
            if answerResult == .incorrect {
                VStack(spacing: 12) {
                    Text(userManager.personalizedEncouragingMessage())
                        .font(.title)
                        .fontWeight(.bold)
                        .foregroundColor(.primary)
                        .multilineTextAlignment(.center)
                        .lineLimit(nil)
                        .minimumScaleFactor(0.7)
                        .padding(.horizontal, 20)

                    if let question = currentQuestion {
                        VStack(spacing: 8) {
                            Text("Correct Answer:")
                                .font(.callout)
                                .foregroundColor(.secondary)

                            Text(question.correctAnswer)
                                .font(.title3)
                                .fontWeight(.semibold)
                                .foregroundColor(Color.fizTeal)
                                .multilineTextAlignment(.center)
                                .lineLimit(nil)
                                .minimumScaleFactor(0.9)
                                .padding(.horizontal, 20)
                                .padding(.vertical, 12)
                                .background(Color.fizTeal.opacity(0.15))
                                .cornerRadius(10)
                        }
                        .padding(.horizontal, 16)
                    }
                }
            }
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .padding(.horizontal, 24)
    }
}

// MARK: - Preview
#Preview("Correct Answer") {
    ResultContentView(
        answerResult: .correct,
        currentQuestion: TriviaQuestion(
            id: "test_001",
            category: "Science",
            subcategory: "Physics",
            question: "What is the speed of light?",
            options: ["299,792,458 m/s", "300,000,000 m/s", "186,282 mi/s", "150,000,000 m/s"],
            correctAnswer: "299,792,458 m/s",
            difficulty: "medium"
        ),
        showingResult: true
    )
    .preferredColorScheme(.light)
}

#Preview("Incorrect Answer") {
    ResultContentView(
        answerResult: .incorrect,
        currentQuestion: TriviaQuestion(
            id: "test_001",
            category: "Science",
            subcategory: "Physics",
            question: "What is the speed of light?",
            options: ["299,792,458 m/s", "300,000,000 m/s", "186,282 mi/s", "150,000,000 m/s"],
            correctAnswer: "299,792,458 m/s",
            difficulty: "medium"
        ),
        showingResult: true
    )
    .preferredColorScheme(.light)
}
