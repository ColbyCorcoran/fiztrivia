import SwiftUI
import SwiftData

// MARK: - Wheel Segment Data
struct WheelSegmentData: Hashable {
    let name: String
    let icon: String
    let color: String
    let subcategory: String? // nil for main categories, set for subcategories

    static func == (lhs: WheelSegmentData, rhs: WheelSegmentData) -> Bool {
        return lhs.name == rhs.name && lhs.subcategory == rhs.subcategory
    }

    func hash(into hasher: inout Hasher) {
        hasher.combine(name)
        hasher.combine(subcategory)
    }
}

struct CategoryWheelView: View {
    @Bindable var gameViewModel: GameViewModel
    @StateObject private var userManager = UserManager.shared
    @StateObject private var difficultyManager = DifficultyManager.shared
    @StateObject private var singleCategoryManager = SingleCategoryModeManager.shared
    @StateObject private var answeredQuestionsManager = AnsweredQuestionsManager.shared
    @Environment(\.modelContext) private var modelContext
    @Query(sort: [SortDescriptor(\LeaderboardEntry.streak, order: .reverse)]) private var leaderboardEntries: [LeaderboardEntry]
    
    // New state management for inline questions/results
    @State private var showingQuestion = false
    @State private var showingResult = false
    @State private var navigationButtonsDisabled = false
    @State private var currentQuestion: TriviaQuestion?
    @State private var answerResult: AnswerState = .unanswered

    // Drag gesture state for pull-to-spin
    @State private var dragRotation: Double = 0
    @State private var isDragging = false

    // Toast notification for subcategory/category completion
    @State private var showingCompletionToast = false
    @State private var completedSubcategoryName = ""
    @State private var completedCategoryName = ""

    // New high score tracking
    @State private var achievedNewHighScore = false
    @State private var showingHighScoreToast = false
    @State private var newHighScoreValue = 0

    // Random Fiz selection for spin button
    @State private var currentSpinFizImage = "fiz-regular pose"

    // No questions available notification
    @State private var showingNoQuestionsToast = false
    @State private var noQuestionsMessage = ""

    // Computed property for wheel segments
    private var wheelSegments: [WheelSegmentData] {
        if singleCategoryManager.isEnabled, singleCategoryManager.selectedCategory != nil {
            // Get subcategories for the selected category, filtering out those with no remaining questions
            let subcategories = singleCategoryManager.getSubcategoriesForSelectedCategory(from: gameViewModel.questions, difficultyMode: difficultyManager.selectedDifficulty)

            return subcategories.compactMap { subcategory in
                // Only include subcategories that have unanswered questions
                if singleCategoryManager.hasQuestionsRemaining(for: subcategory.name, in: gameViewModel.questions, difficultyMode: difficultyManager.selectedDifficulty, answeredManager: answeredQuestionsManager) {
                    return WheelSegmentData(
                        name: subcategory.name,
                        icon: subcategory.icon,
                        color: subcategory.color,
                        subcategory: subcategory.name
                    )
                }
                return nil
            }
        } else {
            // Default mode: show main categories, filtering out completed ones
            return TriviaCategory.allCases.compactMap { category in
                // Only include categories that have unanswered questions
                if !answeredQuestionsManager.areAllCategoryQuestionsAnswered(category.rawValue, in: gameViewModel.questions, difficultyMode: difficultyManager.selectedDifficulty) {
                    return WheelSegmentData(
                        name: category.rawValue,
                        icon: category.icon,
                        color: category.color,
                        subcategory: nil
                    )
                }
                return nil
            }
        }
    }

    private var segmentAngle: Double {
        let count = wheelSegments.count
        return count > 0 ? 360.0 / Double(count) : 0
    }
    
    var body: some View {
        GeometryReader { geometry in
            mainContentView(geometry: geometry)
        }
    }
    
    private func mainContentView(geometry: GeometryProxy) -> some View {
        ZStack {
            backgroundGradient
            uiContentLayer(geometry: geometry)
            wheelLayer(geometry: geometry)
            homeBarGradient

            // Toast notification for subcategory/category completion
            if showingCompletionToast {
                VStack {
                    Spacer()
                    if !completedSubcategoryName.isEmpty {
                        VStack(spacing: 8) {
                            Text("🎉 \(completedSubcategoryName) Complete!")
                                .font(.headline)
                                .fontWeight(.bold)
                            Text("This section has been removed from the wheel")
                                .font(.subheadline)
                        }
                        .padding()
                        .background(Color.black.opacity(0.8))
                        .foregroundColor(.white)
                        .cornerRadius(10)
                        .padding(.bottom, 200)
                        .padding(.horizontal, 20)
                    } else if !completedCategoryName.isEmpty {
                        VStack(spacing: 8) {
                            Text("🎉 \(completedCategoryName) Complete!")
                                .font(.headline)
                                .fontWeight(.bold)
                            Text("This category has been removed from the wheel")
                                .font(.subheadline)
                        }
                        .padding()
                        .background(Color.black.opacity(0.8))
                        .foregroundColor(.white)
                        .cornerRadius(10)
                        .padding(.bottom, 200)
                        .padding(.horizontal, 20)
                    }
                    Spacer()
                }
                .transition(.move(edge: .bottom).combined(with: .opacity))
            }

            // Toast notification for new high score
            if showingHighScoreToast {
                newHighScoreToastView
            }

            // Toast notification for no questions available
            if showingNoQuestionsToast {
                noQuestionsToastView
            }

            // Celebration overlay for completion
            if gameViewModel.showCompletionCelebration {
                completionCelebrationOverlay
            }
        }
    }
    
    private var backgroundGradient: some View {
        LinearGradient(
            colors: [Color.fizBackground, Color.fizBackgroundSecondary],
            startPoint: .topLeading,
            endPoint: .bottomTrailing
        )
        .ignoresSafeArea()
    }
    
    private func uiContentLayer(geometry: GeometryProxy) -> some View {
        VStack(spacing: 0) {
            topToolbar
            questionAreaWithCalculatedSpacing(geometry: geometry)
            Spacer()
        }
    }
    
    private var topToolbar: some View {
        HStack(spacing: 12) {
            // Left side: Leaderboard + Subtitle
            HStack(spacing: 12) {
                Button(action: {
                    HapticManager.shared.buttonTapEffect()
                    gameViewModel.showLeaderboard()
                }) {
                    Image(systemName: "list.number")
                        .font(.title2)
                }
                .glassButtonStyle()
                .disabled(navigationButtonsDisabled)
                .opacity(navigationButtonsDisabled ? 0.5 : 1.0)
                .triviaAccessibility(
                    label: "Leaderboard",
                    hint: "View top scores",
                    traits: .isButton
                )

                Text(userManager.personalizedTagline)
                    .font(.system(size: 16, weight: .medium))
                    .foregroundColor(.secondary)
            }

            Spacer()

            // Right side: Streak Badge + Settings
            HStack(spacing: 12) {
                // Minimal streak badge with glass effect
                HStack(spacing: 4) {
                    Text("🔥")
                        .font(.caption)
                    Text("\(gameViewModel.gameSession.currentStreak)")
                        .font(.system(size: 14, weight: .semibold))
                        .foregroundColor(Color.fizTeal)
                }
                .padding(.horizontal, 8)
                .padding(.vertical, 4)
                .background(Color.fizTeal.opacity(0.15))
                .cornerRadius(8)

                Button(action: {
                    HapticManager.shared.buttonTapEffect()
                    gameViewModel.showSettings()
                }) {
                    Image(systemName: "gear")
                        .font(.title2)
                }
                .glassButtonStyle()
                .disabled(navigationButtonsDisabled)
                .opacity(navigationButtonsDisabled ? 0.5 : 1.0)
                .triviaAccessibility(
                    label: "Settings",
                    hint: "Open app settings",
                    traits: .isButton
                )
            }
        }
        .padding(.horizontal, 20)
        .padding(.top, 10)
        .frame(height: 50)
    }
    
    private var titleAndStreakSection: some View {
        HStack {
            VStack (alignment: .leading, spacing: 4) {
                HStack(spacing: 8) {
                    Text("Fiz")
                        .font(.system(size: 40, weight: .bold))
                        .foregroundColor(.primary)
                    Image("fiz-regular pose")
                        .resizable()
                        .scaledToFit()
                        .frame(width: 40, height: 40)
                }

                Text(userManager.personalizedTagline)
                    .font(.system(size: 18, weight: .regular))
                    .foregroundColor(.secondary)
            }
            .padding(.leading, 20)
           
            Spacer()
            
            // Current streak display
            VStack(spacing: 4) {
                Text("Current Streak")
                    .font(.caption)
                    .foregroundColor(Color.fizBrown)
                Text("\(gameViewModel.gameSession.currentStreak)")
                    .font(.title2)
                    .fontWeight(.bold)
                    .foregroundColor(Color.fizTeal)
            }
            .padding(.horizontal, 12)
            .padding(.vertical, 8)
            .background(Color.fizTeal.opacity(0.2))
            .cornerRadius(12)
            .padding(.trailing, 20)
        }
        .frame(height: 80)
        .frame(maxWidth: .infinity)
    }
    
    private var questionArea: some View {
        ZStack {
            Group {
                if showingResult {
                    resultView
                } else if showingQuestion, let question = currentQuestion {
                    questionView(for: question)
                } else {
                    placeholderView
                }
            }
            .animation(.easeInOut(duration: 0.3), value: showingQuestion)
            .animation(.easeInOut(duration: 0.3), value: showingResult)
        }
        .frame(height: 300)
        .frame(maxWidth: .infinity)
        .padding(.horizontal, 16)
    }

    private func questionAreaWithCalculatedSpacing(geometry: GeometryProxy) -> some View {
        let toolbarHeight: CGFloat = 50
        let wheelTopY = geometry.size.height - 325  // Wheel center (height - 100) minus radius (225)
        let safeZoneHeight = wheelTopY - toolbarHeight
        let topPadding = (safeZoneHeight - 300) / 2  // Center 300pt questionArea in safe zone

        return questionArea
            .padding(.top, max(topPadding, 20))  // Minimum 20pt padding
    }
    
    private var resultView: some View {
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
                    .lineLimit(2)
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
                        .lineLimit(2)
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
                                .lineLimit(3)
                                .minimumScaleFactor(0.8)
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
    
    private func questionView(for question: TriviaQuestion) -> some View {
        VStack(spacing: 16) {
            VStack(spacing: 8) {
                // Show category with subcategory underneath
                VStack(spacing: 2) {
                    // Main category
                    if let category = gameViewModel.gameSession.selectedCategory {
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
                    .fixedSize(horizontal: false, vertical: true)
            }
            
            LazyVGrid(columns: [
                GridItem(.flexible(), spacing: 12),
                GridItem(.flexible(), spacing: 12)
            ], spacing: 12) {
                ForEach(Array(question.options.enumerated()), id: \.offset) { index, option in
                    Button(action: {
                        selectAnswer(option)
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
    
    private var placeholderView: some View {
        Text("Spin the wheel to start!")
            .font(.title2)
            .foregroundColor(.secondary)
            .padding()
    }
    
    private func wheelLayer(geometry: GeometryProxy) -> some View {
        ZStack {
            wheelShadow
            wheelWithGesture
            centerCircleAndButton
            wheelPointer
        }
        .position(x: geometry.size.width / 2, y: geometry.size.height - 100)
    }
    
    private var wheelShadow: some View {
        Circle()
            .fill(Color.fizBrown.opacity(0.25))
            .frame(width: 450, height: 450)
            .blur(radius: 15)
            .offset(y: 8)
    }
    
    private var wheelWithGesture: some View {
        ZStack {
            ForEach(Array(wheelSegments.enumerated()), id: \.element) { index, segmentData in
                WheelSegment(
                    segmentData: segmentData,
                    index: index,
                    totalSegments: wheelSegments.count
                )
            }
        }
        .frame(width: 450, height: 450)
        .rotationEffect(.degrees(gameViewModel.wheelRotation + dragRotation))
        .animation(.easeOut(duration: AccessibilitySettings.adjustedAnimationDuration(3.0)), value: gameViewModel.wheelRotation)
        .gesture(wheelDragGesture)
    }
    
    private var wheelDragGesture: some Gesture {
        DragGesture()
            .onChanged { value in
                // Only allow dragging when buttons are enabled (not spinning, not showing question/result)
                guard !gameViewModel.isSpinning && !navigationButtonsDisabled else { return }
                isDragging = true
                // Convert drag translation to rotation angle
                let angle = atan2(value.translation.height, value.translation.width) * 180 / .pi
                dragRotation = angle * 0.5 // Dampening factor for smoother feel
            }
            .onEnded { value in
                // Only process drag end if we were actually dragging
                guard !gameViewModel.isSpinning && !navigationButtonsDisabled else {
                    // Reset any accumulated drag rotation if gesture happened during disabled state
                    dragRotation = 0
                    isDragging = false
                    return
                }

                isDragging = false

                let dragDistance = sqrt(pow(value.translation.width, 2) + pow(value.translation.height, 2))
                if dragDistance > 50 {
                    // Add the drag rotation to the wheel's final position for continuity
                    gameViewModel.wheelRotation += dragRotation
                    dragRotation = 0
                    spinWheelInline()
                } else {
                    // Reset drag rotation if not spinning
                    withAnimation(.easeOut(duration: 0.3)) {
                        dragRotation = 0
                    }
                }
            }
    }
    
    private var centerCircleAndButton: some View {
        ZStack {
            Circle()
                .fill(Color.fizBackground)
                .frame(width: 100, height: 100)
                .shadow(color: Color.fizBrown.opacity(0.3), radius: 8)

            if gameViewModel.isSpinning {
                // Random Fiz image while spinning
                Image(currentSpinFizImage)
                    .resizable()
                    .scaledToFit()
                    .frame(width: 70, height: 70)
                    .clipShape(Circle())
            } else {
                Button("SPIN") {
                    spinWheelInline()
                }
                .font(.title2)
                .fontWeight(.bold)
                .foregroundColor(.fizOrange)
                .disabled(navigationButtonsDisabled)
                .opacity(navigationButtonsDisabled ? 0.5 : 1.0)
            }
        }
    }

    // Helper to pick random Fiz image
    private func selectRandomFizImage() {
        let fizImages = [
            "fiz-regular pose",
            "fiz-happy smirk",
            "fiz-leaderboard",
            "fiz-new high score"
            // Add your app icon Fiz images here once you provide the names
        ]
        currentSpinFizImage = fizImages.randomElement() ?? "fiz-regular pose"
    }
    
    private var wheelPointer: some View {
        ZStack {
            Triangle()
                .fill(Color.fizBackground)
                .frame(width: 30, height: 20)
        }
        .offset(y: -53)
    }
    
    private var homeBarGradient: some View {
        VStack {
            Spacer()
            
            LinearGradient(
                colors: [
                    Color.clear,
                    Color.black.opacity(0.05),
                    Color.black.opacity(0.1)
                ],
                startPoint: .top,
                endPoint: .bottom
            )
            .frame(height: 40)
        }
        .ignoresSafeArea(.all, edges: .bottom)
    }
    
    // MARK: - Inline Wheel Spin Logic
    private func spinWheelInline() {
        guard !gameViewModel.isSpinning else { return }

        // Disable all buttons during spin and question
        navigationButtonsDisabled = true

        // Clear any previous state
        showingQuestion = false
        showingResult = false
        currentQuestion = nil
        answerResult = .unanswered

        // Reset drag rotation to ensure wheel position is accurate
        dragRotation = 0
        
        // Start the wheel spin
        gameViewModel.isSpinning = true
        selectRandomFizImage()  // Pick a random Fiz for this spin
        HapticManager.shared.wheelSpinEffect()
        
        let randomSpins = Double.random(in: 5...8)
        let finalRotation = gameViewModel.wheelRotation + (randomSpins * 360)
        
        withAnimation(.easeOut(duration: 3.0)) {
            gameViewModel.wheelRotation = finalRotation
        }
        
        // After spin completes
        DispatchQueue.main.asyncAfter(deadline: .now() + 3.0) {
            gameViewModel.isSpinning = false
            selectCategoryAndLoadQuestion()
            HapticManager.shared.mediumImpact()
        }
    }
    
    private func selectCategoryAndLoadQuestion() {
        // Check if there are any segments available
        guard !wheelSegments.isEmpty else {
            print("No wheel segments available - all categories completed!")
            // Show notification that all questions are answered
            let modeDescription = singleCategoryManager.isEnabled
                ? (singleCategoryManager.selectedCategory?.rawValue ?? "this category")
                : "all categories"
            noQuestionsMessage = "🎉 You've completed all questions in \(modeDescription) for \(difficultyManager.selectedDifficulty.rawValue) mode!"
            withAnimation {
                showingNoQuestionsToast = true
            }
            DispatchQueue.main.asyncAfter(deadline: .now() + 3.0) {
                withAnimation {
                    showingNoQuestionsToast = false
                }
            }
            navigationButtonsDisabled = false
            return
        }

        // Determine which segment was selected based on rotation
        let normalizedRotation = gameViewModel.wheelRotation.truncatingRemainder(dividingBy: 360)
        let segmentIndex = Int((360 - normalizedRotation) / segmentAngle) % wheelSegments.count
        let selectedSegment = wheelSegments[segmentIndex]

        // Filter questions based on mode
        var filteredQuestions: [TriviaQuestion]

        if singleCategoryManager.isEnabled, let subcategoryName = selectedSegment.subcategory {
            // Single Category Mode: filter by subcategory
            filteredQuestions = gameViewModel.questions.filter { question in
                question.subcategory == subcategoryName &&
                !answeredQuestionsManager.isQuestionAnswered(question.id) &&
                difficultyManager.selectedDifficulty.shouldInclude(questionDifficulty: question.difficulty)
            }

            // Set the main category for display purposes
            if let mainCategory = singleCategoryManager.selectedCategory {
                gameViewModel.gameSession.selectedCategory = mainCategory
            }
        } else {
            // Default Mode: filter by main category
            guard let selectedCategory = TriviaCategory(rawValue: selectedSegment.name) else {
                print("Invalid category: \(selectedSegment.name)")
                navigationButtonsDisabled = false
                return
            }

            gameViewModel.gameSession.selectedCategory = selectedCategory

            filteredQuestions = gameViewModel.questions.filter { question in
                question.category == selectedCategory.rawValue &&
                !answeredQuestionsManager.isQuestionAnswered(question.id) &&
                difficultyManager.selectedDifficulty.shouldInclude(questionDifficulty: question.difficulty)
            }
        }

        guard let randomQuestion = filteredQuestions.randomElement() else {
            print("No unanswered questions available for segment: \(selectedSegment.name)")
            // This should not happen since we filter wheelSegments, but just in case
            noQuestionsMessage = "No more questions in \(selectedSegment.name). Try spinning again!"
            withAnimation {
                showingNoQuestionsToast = true
            }
            DispatchQueue.main.asyncAfter(deadline: .now() + 2.0) {
                withAnimation {
                    showingNoQuestionsToast = false
                }
            }
            navigationButtonsDisabled = false
            return
        }

        // Set up question state
        currentQuestion = randomQuestion
        gameViewModel.gameSession.currentQuestion = randomQuestion
        gameViewModel.gameSession.answerState = .unanswered

        // Show question after a brief delay
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) {
            withAnimation(.easeInOut(duration: 0.3)) {
                showingQuestion = true
            }
        }
    }
    
    // MARK: - Answer Selection Logic
    private func selectAnswer(_ answer: String) {
        guard let question = currentQuestion else { return }

        HapticManager.shared.buttonTapEffect()

        // Check subcategory before answering (for completion detection)
        let questionSubcategory = question.subcategory

        // Check if this answer would create a new high score
        let currentStreak = gameViewModel.gameSession.currentStreak
        let isCorrect = (answer == question.correctAnswer)
        if isCorrect {
            let potentialStreak = currentStreak + 1
            let previousBest = leaderboardEntries.first?.streak ?? 0
            if potentialStreak > previousBest {
                achievedNewHighScore = true
                newHighScoreValue = potentialStreak
            }
        }

        // Use GameViewModel's answer selection method with ModelContext
        gameViewModel.selectAnswer(answer, modelContext: modelContext)
        answerResult = gameViewModel.gameSession.answerState

        // Check for completion (subcategory in Single Category Mode, or category in Default Mode)
        if singleCategoryManager.isEnabled,
           let subcategory = questionSubcategory,
           answeredQuestionsManager.areAllSubcategoryQuestionsAnswered(subcategory, in: gameViewModel.questions, difficultyMode: difficultyManager.selectedDifficulty) {
            // Show toast notification for subcategory completion
            completedSubcategoryName = subcategory
            completedCategoryName = ""
            withAnimation {
                showingCompletionToast = true
            }

            // Track subcategory completion
            let questionsAnswered = answeredQuestionsManager.getAnsweredCountForSubcategory(subcategory, in: gameViewModel.questions, difficultyMode: difficultyManager.selectedDifficulty)
            AnalyticsManager.shared.trackCategoryCompleted(
                category: subcategory,
                difficultyMode: difficultyManager.selectedDifficulty.rawValue,
                questionsAnswered: questionsAnswered
            )

            // Auto-dismiss toast after 3 seconds (longer to read the message)
            DispatchQueue.main.asyncAfter(deadline: .now() + 3.0) {
                withAnimation {
                    showingCompletionToast = false
                    completedSubcategoryName = ""
                }
            }
        } else if !singleCategoryManager.isEnabled,
                  let selectedCategory = gameViewModel.gameSession.selectedCategory,
                  answeredQuestionsManager.areAllCategoryQuestionsAnswered(selectedCategory.rawValue, in: gameViewModel.questions, difficultyMode: difficultyManager.selectedDifficulty) {
            // Show toast notification for category completion (Default Mode)
            completedCategoryName = selectedCategory.rawValue
            completedSubcategoryName = ""
            withAnimation {
                showingCompletionToast = true
            }

            // Track category completion
            let questionsAnswered = answeredQuestionsManager.getAnsweredCountForCategory(selectedCategory.rawValue, in: gameViewModel.questions, difficultyMode: difficultyManager.selectedDifficulty)
            AnalyticsManager.shared.trackCategoryCompleted(
                category: selectedCategory.rawValue,
                difficultyMode: difficultyManager.selectedDifficulty.rawValue,
                questionsAnswered: questionsAnswered
            )

            // Auto-dismiss toast after 3 seconds (longer to read the message)
            DispatchQueue.main.asyncAfter(deadline: .now() + 3.0) {
                withAnimation {
                    showingCompletionToast = false
                    completedCategoryName = ""
                }
            }
        }

        // Show result
        showingQuestion = false
        showingResult = true

        // Capture answer state before clearing
        let wasIncorrect = (answerResult == .incorrect)

        // Auto-clear after delay (longer for incorrect answers to allow reading the correct answer)
        let clearDelay = wasIncorrect ? 3.0 : 1.5
        DispatchQueue.main.asyncAfter(deadline: .now() + clearDelay) {
            withAnimation(.easeOut(duration: 0.3)) {
                showingResult = false
                currentQuestion = nil
                answerResult = .unanswered
                navigationButtonsDisabled = false // Re-enable all buttons
            }

            // If incorrect answer and new high score achieved, show toast
            if wasIncorrect && achievedNewHighScore {
                DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) {
                    withAnimation {
                        showingHighScoreToast = true
                    }

                    // Auto-dismiss after 5 seconds (longer to celebrate the achievement)
                    DispatchQueue.main.asyncAfter(deadline: .now() + 5.0) {
                        withAnimation {
                            showingHighScoreToast = false
                            achievedNewHighScore = false
                        }
                    }
                }
            }
        }
    }
    
    private var newHighScoreToastView: some View {
        VStack {
            // Larger notification card without dark background
            VStack(spacing: 24) {
                // Fiz celebrating - larger size
                Image("fiz-new high score")
                    .resizable()
                    .scaledToFit()
                    .frame(width: 180, height: 180)
                    .scaleEffect(showingHighScoreToast ? 1.0 : 0.5)
                    .animation(.spring(response: 0.6, dampingFraction: 0.6), value: showingHighScoreToast)

                // Text content - larger and more prominent
                VStack(spacing: 12) {
                    Text("🎉 New High Score! 🎉")
                        .font(.system(size: 32, weight: .bold))
                        .foregroundColor(Color.fizOrange)
                        .multilineTextAlignment(.center)

                    Text("\(newHighScoreValue) correct in a row!")
                        .font(.title)
                        .fontWeight(.semibold)
                        .foregroundColor(.primary)
                        .multilineTextAlignment(.center)

                    Text("Amazing work, \(userManager.displayName)!")
                        .font(.title3)
                        .foregroundColor(.secondary)
                        .multilineTextAlignment(.center)
                }
            }
            .padding(.horizontal, 40)
            .padding(.vertical, 32)
            .background(
                RoundedRectangle(cornerRadius: 24)
                    .fill(Color.fizBackground)
                    .shadow(color: Color.fizOrange.opacity(0.4), radius: 30, x: 0, y: 15)
            )
            .overlay(
                RoundedRectangle(cornerRadius: 24)
                    .stroke(
                        LinearGradient(
                            colors: [Color.fizOrange.opacity(0.6), Color.fizTeal.opacity(0.4)],
                            startPoint: .topLeading,
                            endPoint: .bottomTrailing
                        ),
                        lineWidth: 3
                    )
            )
            .padding(.horizontal, 24)
            .scaleEffect(showingHighScoreToast ? 1.0 : 0.8)
            .opacity(showingHighScoreToast ? 1.0 : 0)
            .animation(.spring(response: 0.6, dampingFraction: 0.7), value: showingHighScoreToast)
            .onTapGesture {
                // Dismiss on tap
                withAnimation {
                    showingHighScoreToast = false
                    achievedNewHighScore = false
                }
            }

            Spacer()
        }
        .padding(.top, 120)
        .transition(.move(edge: .top).combined(with: .opacity))
    }

    private var noQuestionsToastView: some View {
        VStack {
            Spacer()
            Text(noQuestionsMessage)
                .font(.headline)
                .padding()
                .background(Color.black.opacity(0.8))
                .foregroundColor(.white)
                .cornerRadius(10)
                .padding(.bottom, 200)
            Spacer()
        }
        .transition(.move(edge: .bottom).combined(with: .opacity))
    }

    private var completionCelebrationOverlay: some View {
        ZStack {
            // Semi-transparent background
            Color.black.opacity(0.8)
                .ignoresSafeArea()
                .onTapGesture {
                    // Prevent taps from going through
                }

            VStack(spacing: 30) {
                // Fiz celebrating new high score
                Image("fiz-new high score")
                    .resizable()
                    .scaledToFit()
                    .frame(width: 180, height: 180)
                    .scaleEffect(gameViewModel.showCompletionCelebration ? 1.0 : 0.5)
                    .animation(.spring(response: 0.8, dampingFraction: 0.6).delay(0.2), value: gameViewModel.showCompletionCelebration)

                VStack(spacing: 16) {
                    Text("Congratulations, \(userManager.displayName)!")
                        .font(.largeTitle)
                        .fontWeight(.bold)
                        .foregroundColor(.white)
                        .multilineTextAlignment(.center)
                        .opacity(gameViewModel.showCompletionCelebration ? 1 : 0)
                        .animation(.easeInOut(duration: 0.8).delay(0.4), value: gameViewModel.showCompletionCelebration)

                    // Different messages for single category vs all categories
                    if singleCategoryManager.isEnabled, let category = singleCategoryManager.selectedCategory {
                        Text("You've answered all \(category.rawValue) questions in \(difficultyManager.selectedDifficulty.rawValue) mode!")
                            .font(.title2)
                            .foregroundColor(.white.opacity(0.9))
                            .multilineTextAlignment(.center)
                            .padding(.horizontal, 20)
                            .opacity(gameViewModel.showCompletionCelebration ? 1 : 0)
                            .animation(.easeInOut(duration: 0.8).delay(0.6), value: gameViewModel.showCompletionCelebration)
                    } else {
                        Text("You've answered all questions in the \(difficultyManager.selectedDifficulty.rawValue) difficulty mode!")
                            .font(.title2)
                            .foregroundColor(.white.opacity(0.9))
                            .multilineTextAlignment(.center)
                            .padding(.horizontal, 20)
                            .opacity(gameViewModel.showCompletionCelebration ? 1 : 0)
                            .animation(.easeInOut(duration: 0.8).delay(0.6), value: gameViewModel.showCompletionCelebration)
                    }

                    HStack(spacing: 8) {
                        Text("Total Questions Answered:")
                            .font(.body)
                            .foregroundColor(.white.opacity(0.8))
                        Text("\(gameViewModel.getAnsweredQuestionsCount())")
                            .font(.title2)
                            .fontWeight(.bold)
                            .foregroundColor(Color.fizCream)
                    }
                    .opacity(gameViewModel.showCompletionCelebration ? 1 : 0)
                    .animation(.easeInOut(duration: 0.8).delay(0.8), value: gameViewModel.showCompletionCelebration)
                }

                // Action buttons
                VStack(spacing: 12) {
                    Button(action: {
                        HapticManager.shared.buttonTapEffect()
                        gameViewModel.resetAllProgress()
                    }) {
                        HStack(spacing: 12) {
                            Text("🔄")
                            Text("Play Again")
                        }
                    }
                    .prominentActionButton(color: Color.fizOrange)
                    .padding(.horizontal, 32)

                    // Settings button for Single Category Mode
                    if singleCategoryManager.isEnabled {
                        Button(action: {
                            HapticManager.shared.buttonTapEffect()
                            gameViewModel.showCompletionCelebration = false
                            gameViewModel.showSettings()
                        }) {
                            HStack(spacing: 12) {
                                Image(systemName: "gear")
                                Text("Change Category")
                            }
                        }
                        .prominentActionButton(color: Color.fizTeal)
                        .padding(.horizontal, 32)
                    }
                }
                .scaleEffect(gameViewModel.showCompletionCelebration ? 1 : 0.8)
                .opacity(gameViewModel.showCompletionCelebration ? 1 : 0)
                .animation(.spring(response: 0.8, dampingFraction: 0.7).delay(1.0), value: gameViewModel.showCompletionCelebration)
            }
            .padding(40)
        }
        .transition(.opacity.combined(with: .scale))
    }
}

struct WheelSegment: View {
    let segmentData: WheelSegmentData
    let index: Int
    let totalSegments: Int

    private var segmentAngle: Double {
        360.0 / Double(totalSegments)
    }

    private var startAngle: Double {
        Double(index) * segmentAngle
    }

    var body: some View {
        ZStack {
            // Segment background
            Path { path in
                let center = CGPoint(x: 225, y: 225)
                let radius: CGFloat = 225

                path.move(to: center)
                path.addArc(
                    center: center,
                    radius: radius,
                    startAngle: .degrees(startAngle - 90),
                    endAngle: .degrees(startAngle + segmentAngle - 90),
                    clockwise: false
                )
                path.closeSubpath()
            }
            .fill(Color(hex: segmentData.color))
            .overlay(
                Path { path in
                    let center = CGPoint(x: 225, y: 225)
                    let radius: CGFloat = 225

                    path.move(to: center)
                    path.addArc(
                        center: center,
                        radius: radius,
                        startAngle: .degrees(startAngle - 90),
                        endAngle: .degrees(startAngle + segmentAngle - 90),
                        clockwise: false
                    )
                    path.closeSubpath()
                }
                .stroke(Color.fizBackground, lineWidth: 3)
            )

            // Category/Subcategory icon - larger and radially oriented
            Image(systemName: segmentData.icon)
                .font(.system(size: 45))
                .foregroundColor(.black.opacity(0.75))
                .rotationEffect(.degrees(startAngle + segmentAngle/2)) // Rotate so bottom points to center
                .position(
                    x: 225 + cos(Angle.degrees(startAngle + segmentAngle/2 - 90).radians) * 145,
                    y: 225 + sin(Angle.degrees(startAngle + segmentAngle/2 - 90).radians) * 145
                )
                .overlay(
                        Image(systemName: segmentData.icon)
                            .font(.system(size: 45))
                            .foregroundColor(Color.fizBackground.opacity(0.5))
                            .blur(radius: 1)
                            .offset(x: -1, y: -1)
                    )
                    .shadow(color: Color.fizBrown.opacity(0.3), radius: 2, x: 2, y: 2)
        }
    }
}

struct Triangle: Shape {
    func path(in rect: CGRect) -> Path {
        var path = Path()
        path.move(to: CGPoint(x: rect.midX, y: rect.minY))
        path.addLine(to: CGPoint(x: rect.maxX, y: rect.maxY))
        path.addLine(to: CGPoint(x: rect.minX, y: rect.maxY))
        path.closeSubpath()
        return path
    }
}

extension Color {
    init(hex: String) {
        let hex = hex.trimmingCharacters(in: CharacterSet.alphanumerics.inverted)
        var int: UInt64 = 0
        Scanner(string: hex).scanHexInt64(&int)
        let a, r, g, b: UInt64
        switch hex.count {
        case 3: // RGB (12-bit)
            (a, r, g, b) = (255, (int >> 8) * 17, (int >> 4 & 0xF) * 17, (int & 0xF) * 17)
        case 6: // RGB (24-bit)
            (a, r, g, b) = (255, int >> 16, int >> 8 & 0xFF, int & 0xFF)
        case 8: // ARGB (32-bit)
            (a, r, g, b) = (int >> 24, int >> 16 & 0xFF, int >> 8 & 0xFF, int & 0xFF)
        default:
            (a, r, g, b) = (1, 1, 1, 0)
        }
        
        self.init(
            .sRGB,
            red: Double(r) / 255,
            green: Double(g) / 255,
            blue:  Double(b) / 255,
            opacity: Double(a) / 255
        )
    }
}

#Preview("Light Mode") {
    CategoryWheelView(gameViewModel: GameViewModel())
        .modelContainer(for: LeaderboardEntry.self, inMemory: true)
        .preferredColorScheme(.light)
}

#Preview("Dark Mode") {
    CategoryWheelView(gameViewModel: GameViewModel())
        .modelContainer(for: LeaderboardEntry.self, inMemory: true)
        .preferredColorScheme(.dark)
}
