import SwiftUI
import SwiftData

struct QuestionHistoryView: View {
    @Environment(\.modelContext) private var modelContext
    @Query(sort: [SortDescriptor(\QuestionHistoryEntry.timestamp, order: .reverse)]) private var historyEntries: [QuestionHistoryEntry]

    var body: some View {
        Group {
            if historyEntries.isEmpty {
                emptyStateView
            } else {
                List {
                    ForEach(historyEntries) { entry in
                        QuestionHistoryRow(entry: entry)
                    }
                    .onDelete(perform: deleteEntries)
                }
                .listStyle(.insetGrouped)
            }
        }
        .navigationTitle("Question History")
        .navigationBarTitleDisplayMode(.large)
        .toolbar {
            if !historyEntries.isEmpty {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button(role: .destructive) {
                        clearAllHistory()
                    } label: {
                        Text("Clear All")
                    }
                }
            }
        }
    }

    private var emptyStateView: some View {
        VStack(spacing: 20) {
            Spacer()

            Image(systemName: "clock.arrow.circlepath")
                .font(.system(size: 60))
                .foregroundColor(.secondary)

            Text("No Questions Answered Yet")
                .font(.title2)
                .fontWeight(.semibold)
                .foregroundColor(.primary)

            Text("Your answered questions will appear here.\nUse this to review correct answers.")
                .font(.body)
                .foregroundColor(.secondary)
                .multilineTextAlignment(.center)
                .padding(.horizontal, 40)

            Spacer()
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .background(
            LinearGradient(
                colors: [Color.fizBackground, Color.fizBackgroundSecondary],
                startPoint: .topLeading,
                endPoint: .bottomTrailing
            )
            .ignoresSafeArea()
        )
    }

    private func deleteEntries(at offsets: IndexSet) {
        for index in offsets {
            modelContext.delete(historyEntries[index])
        }

        do {
            try modelContext.save()
        } catch {
            print("Failed to delete history entries: \(error)")
        }
    }

    private func clearAllHistory() {
        for entry in historyEntries {
            modelContext.delete(entry)
        }

        do {
            try modelContext.save()
        } catch {
            print("Failed to clear history: \(error)")
        }
    }
}

struct QuestionHistoryRow: View {
    let entry: QuestionHistoryEntry

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            // Top row: Result icon and timestamp
            HStack {
                // Checkmark or X
                Image(systemName: entry.wasCorrect ? "checkmark.circle.fill" : "xmark.circle.fill")
                    .font(.title2)
                    .foregroundColor(entry.wasCorrect ? Color.fizTeal : .red)

                Spacer()

                // Timestamp
                Text(timeAgoString(from: entry.timestamp))
                    .font(.caption)
                    .foregroundColor(.secondary)
            }

            // Question text
            Text(entry.questionText)
                .font(.body)
                .fontWeight(.medium)
                .foregroundColor(.primary)
                .fixedSize(horizontal: false, vertical: true)

            // Category and subcategory
            HStack(spacing: 6) {
                Text(entry.category)
                    .font(.caption)
                    .foregroundColor(.secondary)

                if let subcategory = entry.subcategory {
                    Text("•")
                        .font(.caption)
                        .foregroundColor(.secondary)

                    Text(subcategory)
                        .font(.caption)
                        .foregroundColor(.secondary)
                }
            }

            // Correct answer (always shown)
            VStack(alignment: .leading, spacing: 4) {
                Text("Correct Answer:")
                    .font(.caption)
                    .foregroundColor(.secondary)

                Text(entry.correctAnswer)
                    .font(.subheadline)
                    .fontWeight(.semibold)
                    .foregroundColor(Color.fizTeal)
                    .padding(.horizontal, 12)
                    .padding(.vertical, 8)
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .background(Color.fizTeal.opacity(0.15))
                    .cornerRadius(8)
            }

            // User's answer (only if incorrect)
            if !entry.wasCorrect {
                VStack(alignment: .leading, spacing: 4) {
                    Text("Your Answer:")
                        .font(.caption)
                        .foregroundColor(.secondary)

                    Text(entry.userAnswer)
                        .font(.subheadline)
                        .fontWeight(.medium)
                        .foregroundColor(.red)
                        .padding(.horizontal, 12)
                        .padding(.vertical, 8)
                        .frame(maxWidth: .infinity, alignment: .leading)
                        .background(Color.red.opacity(0.1))
                        .cornerRadius(8)
                }
            }
        }
        .padding(.vertical, 8)
    }

    private func timeAgoString(from date: Date) -> String {
        let now = Date()
        let interval = now.timeIntervalSince(date)

        if interval < 60 {
            return "Just now"
        } else if interval < 3600 {
            let minutes = Int(interval / 60)
            return "\(minutes)m ago"
        } else if interval < 86400 {
            let hours = Int(interval / 3600)
            return "\(hours)h ago"
        } else {
            let days = Int(interval / 86400)
            return "\(days)d ago"
        }
    }
}

#Preview {
    NavigationStack {
        QuestionHistoryView()
    }
    .modelContainer(for: QuestionHistoryEntry.self, inMemory: true)
}
