import SwiftUI

struct PhobiaSettingsView: View {
    @StateObject private var phobiaManager = PhobiaExclusionManager.shared
    @State private var showingAddSheet = false
    @State private var newPhobiaTerm = ""
    @State private var showingConfirmation = false
    @State private var lastAddedPhobia: Phobia?
    @State private var lastExcludedCount = 0
    @State private var isScanning = false

    // Access GameViewModel to get questions for scanning
    private var gameViewModel = GameViewModel()

    private var backgroundGradient: some View {
        Color(.systemGroupedBackground)
            .ignoresSafeArea()
    }

    var body: some View {
        Form {
            if phobiaManager.phobias.isEmpty {
                Section {
                    VStack(spacing: 12) {
                        Image(systemName: "eye.slash")
                            .font(.system(size: 48))
                            .foregroundColor(.secondary)
                        Text("No Phobia Filters")
                            .font(.headline)
                        Text("Add phobias or topics you'd like to avoid in questions.")
                            .font(.caption)
                            .foregroundColor(.secondary)
                            .multilineTextAlignment(.center)
                    }
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, 32)
                }
            } else {
                Section(header: Text("Active Filters"),
                        footer: Text("Questions matching these terms are excluded from gameplay. Swipe to remove a filter.")) {
                    ForEach(phobiaManager.phobias) { phobia in
                        PhobiaRow(phobia: phobia)
                    }
                    .onDelete(perform: deletePhobia)
                }

                Section {
                    HStack {
                        Text("Total Questions Excluded")
                        Spacer()
                        Text("\(phobiaManager.getTotalExcludedCount())")
                            .foregroundColor(.secondary)
                    }
                }
            }

            Section {
                Button(action: {
                    showingAddSheet = true
                }) {
                    HStack {
                        Image(systemName: "plus.circle.fill")
                        Text("Add Phobia Filter")
                    }
                    .foregroundColor(.fizTeal)
                }
            }
        }
        .scrollContentBackground(.hidden)
        .background(backgroundGradient)
        .navigationTitle("Phobia Filters")
        .navigationBarTitleDisplayMode(.large)
        .sheet(isPresented: $showingAddSheet) {
            AddPhobiaSheet(
                phobiaTerm: $newPhobiaTerm,
                isPresented: $showingAddSheet,
                onAdd: addPhobia
            )
        }
        .alert("Filter Added", isPresented: $showingConfirmation) {
            Button("OK", role: .cancel) { }
        } message: {
            if let phobia = lastAddedPhobia {
                Text("Excluded \(lastExcludedCount) question\(lastExcludedCount == 1 ? "" : "s") related to '\(phobia.term)'.")
            }
        }
    }

    private func addPhobia() {
        guard !newPhobiaTerm.isEmpty else { return }

        isScanning = true

        // Scan database and add phobia
        let result = phobiaManager.addPhobia(term: newPhobiaTerm, in: gameViewModel.questions)

        lastAddedPhobia = result.phobia
        lastExcludedCount = result.excludedCount

        newPhobiaTerm = ""
        isScanning = false
        showingAddSheet = false
        showingConfirmation = true

        HapticManager.shared.buttonTapEffect()
        AnalyticsManager.shared.trackPhobiaFilterAdded(totalFilterCount: phobiaManager.phobias.count)
    }

    private func deletePhobia(at offsets: IndexSet) {
        for index in offsets {
            let phobia = phobiaManager.phobias[index]
            phobiaManager.removePhobia(phobia)
            AnalyticsManager.shared.trackPhobiaFilterRemoved(remainingFilterCount: phobiaManager.phobias.count)
        }
        HapticManager.shared.buttonTapEffect()
    }
}

// MARK: - Phobia Row with Blur Effect

struct PhobiaRow: View {
    let phobia: Phobia
    @State private var isRevealed = false

    var body: some View {
        VStack(alignment: .leading, spacing: 4) {
            HStack {
                // Blurred/Redacted phobia term with tap to reveal overlay
                ZStack(alignment: .leading) {
                    // The actual phobia term (blurred when not revealed)
                    Text(phobia.term.capitalized)
                        .font(.body)
                        .blur(radius: isRevealed ? 0 : 8)
                        .opacity(isRevealed ? 1 : 0.3)

                    // "Tap to reveal" message (shown when not revealed)
                    Text("Tap to reveal")
                        .font(.caption)
                        .foregroundColor(.secondary)
                        .opacity(isRevealed ? 0 : 1)
                }
                .frame(minWidth: 100, alignment: .leading)
                .onTapGesture {
                    withAnimation(.easeInOut(duration: 0.2)) {
                        isRevealed.toggle()
                    }
                    if isRevealed {
                        // Auto-hide after 3 seconds
                        DispatchQueue.main.asyncAfter(deadline: .now() + 3) {
                            withAnimation(.easeInOut(duration: 0.2)) {
                                isRevealed = false
                            }
                        }
                    }
                }

                Spacer()

                Text("\(phobia.excludedQuestionIds.count)")
                    .font(.caption)
                    .foregroundColor(.secondary)
            }

            Text("\(phobia.excludedQuestionIds.count) question\(phobia.excludedQuestionIds.count == 1 ? "" : "s") excluded")
                .font(.caption)
                .foregroundColor(.secondary)
        }
        .padding(.vertical, 4)
    }
}

// MARK: - Add Phobia Sheet

struct AddPhobiaSheet: View {
    @Binding var phobiaTerm: String
    @Binding var isPresented: Bool
    let onAdd: () -> Void
    @FocusState private var isTextFieldFocused: Bool

    var body: some View {
        NavigationStack {
            Form {
                Section(header: Text("Filter Term"),
                        footer: Text("Enter a word or topic you'd like to avoid in questions (e.g., 'snakes', 'spiders', 'heights').")) {
                    TextField("Enter term...", text: $phobiaTerm)
                        .textInputAutocapitalization(.never)
                        .autocorrectionDisabled()
                        .focused($isTextFieldFocused)
                }

                Section {
                    Text("The app will scan the question database and exclude any questions containing this term or related words.")
                        .font(.caption)
                        .foregroundColor(.secondary)
                }
            }
            .navigationTitle("Add Phobia Filter")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancel") {
                        isPresented = false
                    }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button("Add") {
                        onAdd()
                    }
                    .disabled(phobiaTerm.trimmingCharacters(in: .whitespaces).isEmpty)
                }
            }
            .onAppear {
                isTextFieldFocused = true
            }
        }
    }
}

#Preview {
    NavigationStack {
        PhobiaSettingsView()
    }
}
