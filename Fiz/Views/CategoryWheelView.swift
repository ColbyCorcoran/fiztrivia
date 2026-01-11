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
    var onSwipe: ((SwipeDirection) -> Void)? = nil
    @StateObject private var userManager = UserManager.shared
    @StateObject private var difficultyManager = DifficultyManager.shared
    @StateObject private var gameModeManager = GameModeManager.shared
    @StateObject private var answeredQuestionsManager = AnsweredQuestionsManager.shared
    @StateObject private var phobiaManager = PhobiaExclusionManager.shared
    @StateObject private var categorySelectionManager = CategorySelectionManager.shared
    @StateObject private var popupDurationManager = PopupDurationManager.shared
    @StateObject private var swipeNavigationManager = SwipeNavigationManager.shared
    @Environment(\.modelContext) private var modelContext
    @Environment(\.sizeCategory) private var sizeCategory
    @Query(sort: [SortDescriptor(\LeaderboardEntry.streak, order: .reverse)]) private var leaderboardEntries: [LeaderboardEntry]

    // New state management for inline questions/results
    @State private var showingQuestion = false
    @State private var showingResult = false
    @State private var navigationButtonsDisabled = false
    @State private var currentQuestion: TriviaQuestion?
    @State private var answerResult: AnswerState = .unanswered

    // Modal presentation for large Dynamic Type sizes
    @State private var showingQuestionModal = false

    // Drag gesture state for pull-to-spin
    @State private var dragRotation: Double = 0
    @State private var isDragging = false
    @State private var dragSpinDirection: Double = 1.0 // 1.0 for clockwise, -1.0 for counter-clockwise
    @State private var dragStartAngle: Double = 0
    @State private var dragCurrentAngle: Double = 0

    // Toast notification for subcategory/category/subtopic completion
    @State private var showingCompletionToast = false
    @State private var completedSubcategoryName = ""
    @State private var completedCategoryName = ""
    @State private var completedSubtopicName = ""

    // New high score tracking
    @State private var achievedNewHighScore = false
    @State private var showingHighScoreToast = false
    @State private var newHighScoreValue = 0

    // Random Fiz selection for spin button
    @State private var currentSpinFizImage = "fiz-regular pose"

    // No questions available notification
    @State private var showingNoQuestionsToast = false
    @State private var noQuestionsMessage = ""

    // Swipe navigation state
    @State private var swipeStartX: CGFloat = 0
    @State private var swipeTranslation: CGFloat = 0

    // Store modal presentation
    @State private var showingStore = false

    // Preview pack completion alert
    @State private var showingPreviewCompletionAlert = false
    @State private var completedPreviewPackId = ""

    // Computed property for wheel segments
    private var wheelSegments: [WheelSegmentData] {
        // First, create segments with base colors
        let baseSegments: [WheelSegmentData]

        if gameModeManager.isSingleTopicMode, gameModeManager.selectedTopic != nil {
            // Get subtopics for the selected expansion pack
            let subtopics = gameModeManager.getSubtopicsForSelectedTopic()

            // Get the pack to access its icons
            let pack = ExpansionPackManager.shared.availablePacks.first(where: { $0.packId == gameModeManager.selectedTopic })

            // Create segments with individual subtopic icons, filtering out empty subtopics
            baseSegments = subtopics.compactMap { subtopic in
                // Only include subtopics that have unanswered questions
                guard hasQuestionsForSubtopic(subtopic, topicPackId: gameModeManager.selectedTopic!) else {
                    return nil
                }

                // Use subtopic-specific icon if available, otherwise fall back to pack icon
                let subtopicIcon = pack?.icon(for: subtopic) ?? "star.fill"

                return WheelSegmentData(
                    name: subtopic,
                    icon: subtopicIcon,  // Individual subtopic icon
                    color: "#FFFFFF",  // Placeholder - will be replaced by smart color logic
                    subcategory: subtopic // Using subcategory field to store subtopic
                )
            }
        } else if gameModeManager.isSingleCategoryMode, gameModeManager.selectedCategory != nil {
            // Get subcategories for the selected category, filtering out those with no remaining questions
            let subcategories = gameModeManager.getSubcategoriesForSelectedCategory(from: gameViewModel.questions, difficultyMode: difficultyManager.selectedDifficulty)

            baseSegments = subcategories.compactMap { subcategory in
                // Only include subcategories that have unanswered questions
                if gameModeManager.hasQuestionsRemaining(for: subcategory.name, in: gameViewModel.questions, difficultyMode: difficultyManager.selectedDifficulty, answeredManager: answeredQuestionsManager) {
                    return WheelSegmentData(
                        name: subcategory.name,
                        icon: subcategory.icon,
                        color: "#FFFFFF",  // Placeholder - will be replaced by smart color logic
                        subcategory: subcategory.name
                    )
                }
                return nil
            }
        } else {
            // Multi-Category mode: show selected categories only, filtering out completed ones
            baseSegments = TriviaCategory.allCases.compactMap { category in
                // Filter by selected categories FIRST
                guard categorySelectionManager.isSelected(category) else {
                    return nil
                }

                // Then filter by completion status
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

        // Apply smart color assignment to avoid duplicates/adjacency
        // Build segments iteratively to track assigned colors
        var smartSegments: [WheelSegmentData] = []
        var assignedColors: [String] = []

        for (index, segment) in baseSegments.enumerated() {
            let smartColorHex = smartColor(
                for: segment,
                at: index,
                totalSegments: baseSegments.count,
                allSegments: baseSegments,
                assignedColors: assignedColors
            )

            smartSegments.append(WheelSegmentData(
                name: segment.name,
                icon: segment.icon,
                color: smartColorHex,
                subcategory: segment.subcategory
            ))

            assignedColors.append(smartColorHex)
        }

        return smartSegments
    }

    private var segmentAngle: Double {
        let count = wheelSegments.count
        return count > 0 ? 360.0 / Double(count) : 0
    }

    // MARK: - Smart Color Assignment
    private func smartColor(
        for segment: WheelSegmentData,
        at index: Int,
        totalSegments: Int,
        allSegments: [WheelSegmentData],
        assignedColors: [String]
    ) -> String {
        // Shared color palette for all segment types
        let colorPalette = [
            "#F7B500",  // Gold
            "#FF7F0F",  // Orange
            "#8E44AD",  // Purple
            "#3498DB",  // Blue
            "#2ECC71",  // Green
            "#E91E63"   // Pink
        ]

        // For subcategories and subtopics, always apply smart logic
        if segment.subcategory != nil {
            // Subcategories/subtopics are always flexible - use smart color assignment
            if totalSegments <= 6 {
                // 2-6 segments: Ensure NO duplicate colors
                return assignUniqueColorForFlexible(
                    currentIndex: index,
                    allSegments: allSegments,
                    assignedColors: assignedColors,
                    palette: colorPalette,
                    defaultColor: colorPalette[index % colorPalette.count]
                )
            } else {
                // 7+ segments: Avoid adjacent same colors
                return assignNonAdjacentColorForFlexible(
                    for: index,
                    totalSegments: totalSegments,
                    allSegments: allSegments,
                    assignedColors: assignedColors,
                    palette: colorPalette,
                    defaultColor: colorPalette[index % colorPalette.count]
                )
            }
        }

        // For categories, use existing logic
        guard let category = TriviaCategory(rawValue: segment.name) else {
            // Fallback: use palette cycling
            return colorPalette[index % colorPalette.count]
        }

        // If it's a locked category, always use its specific color
        if category.isColorLocked {
            return category.color
        }

        // For flexible categories, apply smart logic based on number of segments
        if totalSegments <= 6 {
            // 2-6 categories: Ensure NO duplicate colors
            return assignUniqueColor(
                category: category,
                currentIndex: index,
                allSegments: allSegments,
                assignedColors: assignedColors,
                palette: colorPalette
            )
        } else {
            // 7-12 categories: Avoid adjacent same colors
            return assignNonAdjacentColor(
                for: index,
                category: category,
                totalSegments: totalSegments,
                allSegments: allSegments,
                assignedColors: assignedColors,
                palette: colorPalette
            )
        }
    }

    private func assignUniqueColor(
        category: TriviaCategory,
        currentIndex: Int,
        allSegments: [WheelSegmentData],
        assignedColors: [String],
        palette: [String]
    ) -> String {
        // Colors already assigned to previous segments
        var usedColors = Set(assignedColors)

        // Also reserve colors needed by locked categories that come after this one
        for i in (currentIndex + 1)..<allSegments.count {
            if let futureCat = TriviaCategory(rawValue: allSegments[i].name),
               futureCat.isColorLocked {
                usedColors.insert(futureCat.color)
            }
        }

        // Try to use the category's static color first if it's not used/reserved
        if !usedColors.contains(category.color) {
            return category.color
        }

        // Find first color in palette not already used or reserved
        for color in palette {
            if !usedColors.contains(color) {
                return color
            }
        }

        // Fallback: use default color (shouldn't happen with 6 colors and ≤6 categories)
        return category.color
    }

    private func assignNonAdjacentColor(
        for index: Int,
        category: TriviaCategory,
        totalSegments: Int,
        allSegments: [WheelSegmentData],
        assignedColors: [String],
        palette: [String]
    ) -> String {
        let usedColors = Set(assignedColors)
        var adjacentColors: Set<String> = []

        // Get previous segment's color (it's already been assigned)
        let prevIndex = (index - 1 + totalSegments) % totalSegments
        if prevIndex < assignedColors.count && prevIndex >= 0 {
            adjacentColors.insert(assignedColors[prevIndex])
        }

        // Get next segment's color if it's a locked category (we know its future color)
        let nextIndex = (index + 1) % totalSegments
        if nextIndex < allSegments.count {
            if let nextCat = TriviaCategory(rawValue: allSegments[nextIndex].name),
               nextCat.isColorLocked {
                adjacentColors.insert(nextCat.color)
            }
        }

        // CRITICAL: Check wrap-around for last segment
        // On a circular wheel, the last segment is adjacent to the first segment
        if index == totalSegments - 1 && !assignedColors.isEmpty {
            // Last segment is adjacent to first segment (index 0)
            adjacentColors.insert(assignedColors[0])
        }

        // STRATEGY: Maximize color variety while avoiding adjacency
        // Priority 1: Use category's static color if unused and not adjacent (most predictable)
        if !usedColors.contains(category.color) && !adjacentColors.contains(category.color) {
            return category.color
        }

        // Priority 2: Find any other unused color that's not adjacent (maximize variety)
        for color in palette {
            if !usedColors.contains(color) && !adjacentColors.contains(color) {
                return color
            }
        }

        // Priority 3: Use category's static color if not adjacent (even if used, better than random)
        if !adjacentColors.contains(category.color) {
            return category.color
        }

        // Priority 4: Find any color that's not adjacent (last resort)
        for color in palette {
            if !adjacentColors.contains(color) {
                return color
            }
        }

        // Final fallback (should never reach here)
        return category.color
    }

    // MARK: - Flexible Segment Color Assignment (Subcategories & Subtopics)

    private func assignUniqueColorForFlexible(
        currentIndex: Int,
        allSegments: [WheelSegmentData],
        assignedColors: [String],
        palette: [String],
        defaultColor: String
    ) -> String {
        // Colors already assigned to previous segments
        let usedColors = Set(assignedColors)

        // Try to use a unique color from the palette
        for color in palette {
            if !usedColors.contains(color) {
                return color
            }
        }

        // Fallback: use default color (cycling through palette)
        return defaultColor
    }

    private func assignNonAdjacentColorForFlexible(
        for index: Int,
        totalSegments: Int,
        allSegments: [WheelSegmentData],
        assignedColors: [String],
        palette: [String],
        defaultColor: String
    ) -> String {
        let usedColors = Set(assignedColors)
        var adjacentColors: Set<String> = []

        // Get previous segment's color (already assigned)
        let prevIndex = (index - 1 + totalSegments) % totalSegments
        if prevIndex < assignedColors.count && prevIndex >= 0 {
            adjacentColors.insert(assignedColors[prevIndex])
        }

        // CRITICAL: Check wrap-around for last segment
        // On a circular wheel, the last segment is adjacent to the first segment
        if index == totalSegments - 1 && !assignedColors.isEmpty {
            // Last segment is adjacent to first segment (index 0)
            adjacentColors.insert(assignedColors[0])
        }

        // Priority 1: Find unused color that's not adjacent
        for color in palette {
            if !usedColors.contains(color) && !adjacentColors.contains(color) {
                return color
            }
        }

        // Priority 2: Find any color that's not adjacent (even if used)
        for color in palette {
            if !adjacentColors.contains(color) {
                return color
            }
        }

        // Fallback: use default color
        return defaultColor
    }

    // MARK: - Question Filtering Helpers
    private func hasQuestionsForSubtopic(_ subtopic: String, topicPackId: String) -> Bool {
        let questions = gameViewModel.questions.filter { question in
            question.topic == topicPackId &&
            question.subtopic == subtopic &&
            !answeredQuestionsManager.isQuestionAnswered(question.id) &&
            difficultyManager.selectedDifficulty.shouldInclude(questionDifficulty: question.difficulty) &&
            !phobiaManager.isQuestionExcluded(question.id)
        }
        return !questions.isEmpty
    }

    // MARK: - Dynamic Type & Accessibility
    // Questions display inline for normal text sizes, but switch to modal
    // for accessibility text sizes (.accessibility3+) to prevent
    // content from being hidden behind the wheel
    private var shouldUseModalPresentation: Bool {
        sizeCategory.shouldUseModalQuestions
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

            // Toast notification for subcategory/category/subtopic completion
            if showingCompletionToast {
                VStack {
                    Spacer()
                    if !completedSubtopicName.isEmpty {
                        VStack(spacing: 8) {
                            Text("🎉 \(completedSubtopicName) Complete!")
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
                    } else if !completedSubcategoryName.isEmpty {
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
        .gesture(navigationSwipeGesture)
        .alert("All Questions Completed! 🎉", isPresented: $gameViewModel.showSingleCategoryCompletionAlert) {
            Button("Change Game Mode") {
                HapticManager.shared.buttonTapEffect()
                gameViewModel.showSingleCategoryCompletionAlert = false
                gameViewModel.showSettings()
            }

            Button("Return to Multi-Category Mode") {
                HapticManager.shared.buttonTapEffect()
                gameModeManager.setMode(.multiCategory)
                gameViewModel.showSingleCategoryCompletionAlert = false
            }

            Button("Cancel", role: .cancel) {
                gameViewModel.showSingleCategoryCompletionAlert = false
            }
        } message: {
            if let category = gameModeManager.selectedCategory {
                Text("You've completed all questions in \(category.rawValue) for \(difficultyManager.selectedDifficulty.rawValue) mode.\n\nSwitch to a different category, return to Multi-Category mode, or change your game settings.")
            } else {
                Text("You've completed all questions for your selected game mode.\n\nSwitch to a different category, return to Multi-Category mode, or change your game settings.")
            }
        }
        .alert("Preview Pack Completed! 🎉", isPresented: $gameViewModel.showPreviewPackCompletionAlert) {
            Button("Buy Full Pack") {
                HapticManager.shared.buttonTapEffect()
                gameViewModel.showPreviewPackCompletionAlert = false
                // Open Store view
                showingStore = true
            }

            Button("Maybe Later") {
                HapticManager.shared.buttonTapEffect()
                gameViewModel.showPreviewPackCompletionAlert = false
                gameViewModel.showSettings()
            }
        } message: {
            if let packId = gameViewModel.completedPreviewPackId,
               let pack = ExpansionPackManager.shared.availablePacks.first(where: { $0.packId == packId }) {
                Text("You've completed all \(pack.freePreviewCount) preview questions for \(pack.packName)!\n\nEnjoy the preview? Unlock \(pack.questionCount - pack.freePreviewCount) more questions for $\(String(format: "%.2f", pack.price)).\n\nYou can also switch to a different topic or return to regular mode in Game Modes Settings.")
            } else {
                Text("You've completed all preview questions for this pack!\n\nYou can purchase the full pack or switch to a different game mode in settings.")
            }
        }
        .sheet(isPresented: $showingQuestionModal, onDismiss: handleModalDismiss) {
            if let question = currentQuestion {
                QuestionModalView(
                    isPresented: $showingQuestionModal,
                    question: question,
                    selectedCategory: gameViewModel.gameSession.selectedCategory,
                    answerResult: answerResult,
                    showingResult: showingResult,
                    onAnswerSelected: selectAnswer,
                    onDismiss: handleModalDismiss
                )
                .presentationDetents([.medium, .large], selection: .constant(sizeCategory.preferredModalDetent))
                .presentationDragIndicator(.visible)
                .interactiveDismissDisabled(true) // Cannot skip questions - must answer
            }
        }
        .sheet(isPresented: $showingStore) {
            StoreView()
                .presentationDragIndicator(.visible)
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
        VStack(spacing: 0) {
            // Toolbar buttons area
            HStack {
                Button(action: {
                    HapticManager.shared.buttonTapEffect()
                    gameViewModel.showLeaderboard()
                }) {
                    Image(systemName: "trophy")
                        .font(.title3.weight(.semibold))
                }
                .glassButtonStyle()
                .tint(.fizTeal)
                .disabled(navigationButtonsDisabled)
                .opacity(navigationButtonsDisabled ? 0.5 : 1.0)
                .triviaAccessibility(
                    label: "Leaderboard",
                    hint: "View top scores",
                    traits: .isButton
                )


                Spacer()

                Button(action: {
                    HapticManager.shared.buttonTapEffect()
                    showingStore = true
                }) {
                    Image(systemName: "rectangle.stack.badge.plus")
                        .font(.title3.weight(.semibold))
                }
                .glassButtonStyle()
                .tint(.fizOrange)
                .disabled(navigationButtonsDisabled)
                .opacity(navigationButtonsDisabled ? 0.5 : 1.0)
                .triviaAccessibility(
                    label: "Store",
                    hint: "Browse expansion packs",
                    traits: .isButton
                )

                Spacer()

                Button(action: {
                    HapticManager.shared.buttonTapEffect()
                    gameViewModel.showSettings()
                }) {
                    Image(systemName: "gear")
                        .font(.title3.weight(.semibold))
                }
                .glassButtonStyle()
                .tint(.fizTeal)
                .disabled(navigationButtonsDisabled)
                .opacity(navigationButtonsDisabled ? 0.5 : 1.0)
                .triviaAccessibility(
                    label: "Settings",
                    hint: "Open app settings",
                    traits: .isButton
                )
            }
            .padding(.horizontal, 10)
            .padding(.top, 10)
            .padding(.bottom, 15)
            .frame(height: 44)

            // Tagline and streak counter line - hide entire row at accessibility sizes
            if sizeCategory < .accessibilityMedium {
                HStack {
                    // Tagline - hide at extreme accessibility sizes to save space
                    if !sizeCategory.shouldUseCompactLayout {
                        Text(userManager.personalizedTagline)
                            .font(.system(size: 18, weight: .medium))
                            .foregroundColor(.secondary)
                            .minimumScaleFactor(0.85)
                    }

                    Spacer()

                    // Right side: Mode indicator (if applicable) and streak badge
                    HStack(spacing: 8) {
                    // Game mode indicator - always visible for all modes
                    HStack(spacing: 4) {
                        Image(systemName: gameModeManager.selectedMode.icon)
                            .font(.caption)
                        Text("Mode")
                            .font(.system(size: 14))
                            .fontWeight(.semibold)
                            .minimumScaleFactor(0.9)
                            .lineLimit(1)
                    }
                    .padding(.horizontal, 8)
                    .padding(.vertical, 4)
                    .background(Color.fizOrange.opacity(0.15))
                    .foregroundColor(Color.fizOrange)
                    .cornerRadius(8)

                    // Streak badge
                    HStack(spacing: 4) {
                        Text("🔥")
                            .font(.caption)
                        Text("\(gameViewModel.gameSession.currentStreak)")
                            .font(.system(size: 14))
                            .fontWeight(.semibold)
                            .minimumScaleFactor(0.9)
                            .lineLimit(1)
                            .foregroundColor(Color.fizTeal)
                    }
                    .padding(.horizontal, 8)
                    .padding(.vertical, 4)
                    .background(Color.fizTeal.opacity(0.15))
                    .cornerRadius(8)
                    }
                }
                .padding(.horizontal, 15)
                .padding(.top, 4)
                .frame(height: 32)
            }
        }
    }
    
    private var questionArea: some View {
        ZStack {
            Group {
                if shouldUseModalPresentation {
                    // Modal mode: Show placeholder when modal is active
                    if showingQuestionModal {
                        Text("Question displayed in modal")
                            .font(.callout)
                            .foregroundColor(.secondary)
                            .padding()
                    } else {
                        placeholderView
                    }
                } else {
                    // Inline mode: Use shared components
                    if showingResult {
                        ResultContentView(
                            answerResult: answerResult,
                            currentQuestion: currentQuestion,
                            showingResult: showingResult
                        )
                    } else if showingQuestion, let question = currentQuestion {
                        QuestionContentView(
                            question: question,
                            selectedCategory: gameViewModel.gameSession.selectedCategory,
                            onAnswerSelected: selectAnswer
                        )
                    } else {
                        placeholderView
                    }
                }
            }
            .animation(.easeInOut(duration: 0.3), value: showingQuestion)
            .animation(.easeInOut(duration: 0.3), value: showingResult)
        }
        .frame(height: 300 * sizeCategory.conservativeScaleFactor)
        .frame(maxWidth: .infinity)
        .padding(.horizontal, 16)
    }

    private var navigationSwipeGesture: some Gesture {
        DragGesture(minimumDistance: 30)
            .onEnded { value in
                // Enhanced guards to prevent conflicts
                guard swipeNavigationManager.isSwipeNavigationEnabled,
                      !showingQuestion,
                      !showingResult,
                      !gameViewModel.isSpinning,
                      !navigationButtonsDisabled,
                      !isDragging else {
                    return
                }

                let horizontalDistance = value.translation.width
                let verticalDistance = value.translation.height
                let horizontalVelocity = value.predictedEndTranslation.width
                let verticalVelocity = value.predictedEndTranslation.height

                // Determine if this is primarily a horizontal or vertical swipe
                let isHorizontal = abs(horizontalDistance) > abs(verticalDistance)

                // Relaxed thresholds for smoother detection
                // 30pt minimum OR 60pt/s velocity (down from 50pt / 100pt/s)
                if isHorizontal {
                    // Horizontal swipes (left/right)
                    if abs(horizontalDistance) > 30 || abs(horizontalVelocity) > 60 {
                        if horizontalDistance > 0 {
                            // Swipe right -> Leaderboard
                            HapticManager.shared.lightImpact()
                            onSwipe?(.right)
                        } else {
                            // Swipe left -> Settings
                            HapticManager.shared.lightImpact()
                            onSwipe?(.left)
                        }
                    }
                } else {
                    // Vertical swipes (up/down)
                    if abs(verticalDistance) > 30 || abs(verticalVelocity) > 60 {
                        if verticalDistance < 0 {
                            // Swipe up -> Store
                            HapticManager.shared.lightImpact()
                            showingStore = true
                        }
                        // Swipe down does nothing (reserved for future use)
                    }
                }
            }
    }

    private func questionAreaWithCalculatedSpacing(geometry: GeometryProxy) -> some View {
        // Calculate actual toolbar height based on what's visible
        let buttonRowHeight: CGFloat = 44 + 10 + 15  // height (44) + top padding (10) + bottom padding (15) = 69pt
        let taglineRowHeight: CGFloat = sizeCategory < .accessibilityMedium ? (32 + 4) : 0  // height (32) + top padding (4) when visible
        let toolbarHeight = buttonRowHeight + taglineRowHeight

        let questionAreaHeight: CGFloat = 300 * sizeCategory.conservativeScaleFactor
        let wheelTopY = geometry.size.height - 325  // Wheel center (height - 100) minus radius (225)
        let safeZoneHeight = wheelTopY - toolbarHeight
        let topPadding = (safeZoneHeight - questionAreaHeight) / 2  // Center questionArea in safe zone

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
        VStack {
            if sizeCategory.isAccessibilitySize {
                // At accessibility sizes, position text higher (near top of container)
                Text("Spin the wheel to start!")
                    .font(.title2)
                    .foregroundColor(.secondary)
                    .padding()
                Spacer()
            } else {
                // Normal sizes: centered (default behavior)
                Text("Spin the wheel to start!")
                    .font(.title2)
                    .foregroundColor(.secondary)
                    .padding()
            }
        }
        .frame(maxHeight: .infinity)
    }
    
    private func wheelLayer(geometry: GeometryProxy) -> some View {
        let wheelCenter = CGPoint(x: geometry.size.width / 2, y: geometry.size.height - 100)

        return ZStack {
            wheelShadow
            wheelWithGesture
            centerCircleAndButton
            wheelPointer
        }
        .position(wheelCenter)
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

                // Wheel's local center (the wheel is 450x450, so center is at 225, 225)
                let wheelCenter = CGPoint(x: 225, y: 225)

                if !isDragging {
                    // First drag event - record starting angle
                    isDragging = true
                    let dx = value.location.x - wheelCenter.x
                    let dy = value.location.y - wheelCenter.y
                    dragStartAngle = atan2(dy, dx) * 180 / .pi
                    dragCurrentAngle = dragStartAngle
                    dragRotation = 0
                } else {
                    // Calculate current angle from wheel center to touch point
                    let dx = value.location.x - wheelCenter.x
                    let dy = value.location.y - wheelCenter.y
                    let newAngle = atan2(dy, dx) * 180 / .pi

                    // Calculate the angular change
                    var angleDelta = newAngle - dragCurrentAngle

                    // Handle wrap-around (crossing from 180 to -180 or vice versa)
                    if angleDelta > 180 {
                        angleDelta -= 360
                    } else if angleDelta < -180 {
                        angleDelta += 360
                    }

                    // Accumulate the rotation
                    dragRotation += angleDelta
                    dragCurrentAngle = newAngle
                }
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

                // Check if user dragged far enough (at least 30 degrees of rotation)
                if abs(dragRotation) > 30 {
                    // Determine spin direction based on accumulated rotation
                    // In screen coordinates (Y increases downward):
                    // Positive dragRotation = clockwise drag → spin clockwise
                    // Negative dragRotation = counter-clockwise drag → spin counter-clockwise
                    dragSpinDirection = dragRotation > 0 ? 1.0 : -1.0

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
                    dragSpinDirection = 1.0 // Default to clockwise for button spin
                    spinWheelInline()
                }
                .font(.system(size: 22, weight: .bold))  // Fixed size - doesn't scale with Dynamic Type
                .foregroundColor(.fizOrange)
                .minimumScaleFactor(0.8)
                .lineLimit(1)
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
        // Apply the drag direction to the spin (1.0 = clockwise, -1.0 = counter-clockwise)
        let finalRotation = gameViewModel.wheelRotation + (dragSpinDirection * randomSpins * 360)
        
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
            let modeDescription = gameModeManager.isSingleCategoryMode
                ? (gameModeManager.selectedCategory?.rawValue ?? "this category")
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

        if gameModeManager.isSingleTopicMode, let subtopicName = selectedSegment.subcategory {
            // Single Topic Mode: filter by topic and subtopic
            guard let topicPackId = gameModeManager.selectedTopic else {
                print("No topic selected for Single Topic Mode")
                navigationButtonsDisabled = false
                return
            }

            filteredQuestions = gameViewModel.questions.filter { question in
                question.topic == topicPackId &&
                question.subtopic == subtopicName &&
                !answeredQuestionsManager.isQuestionAnswered(question.id) &&
                difficultyManager.selectedDifficulty.shouldInclude(questionDifficulty: question.difficulty)
            }

            // Set selectedCategory to nil for topic mode (or could set to the question's category)
            gameViewModel.gameSession.selectedCategory = nil
        } else if gameModeManager.isSingleCategoryMode, let subcategoryName = selectedSegment.subcategory {
            // Single Category Mode: filter by subcategory
            filteredQuestions = gameViewModel.questions.filter { question in
                question.subcategory == subcategoryName &&
                !answeredQuestionsManager.isQuestionAnswered(question.id) &&
                difficultyManager.selectedDifficulty.shouldInclude(questionDifficulty: question.difficulty)
            }

            // Set the main category for display purposes
            if let mainCategory = gameModeManager.selectedCategory {
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

                // Show modal if using large text size
                if shouldUseModalPresentation {
                    showingQuestionModal = true
                }
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

        // Save to question history
        let historyEntry = QuestionHistoryEntry(
            questionId: question.id,
            questionText: question.question,
            correctAnswer: question.correctAnswer,
            userAnswer: answer,
            wasCorrect: isCorrect,
            category: question.category,
            subcategory: question.subcategory,
            topic: question.topic
        )
        modelContext.insert(historyEntry)
        do {
            try modelContext.save()
        } catch {
            print("Failed to save question history: \(error)")
        }

        // Check for completion (subcategory in Single Category Mode, or category in Default Mode)
        if gameModeManager.isSingleCategoryMode,
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
        } else if gameModeManager.isRegularMode,
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
        } else if gameModeManager.isSingleTopicMode,
                  let subtopic = currentQuestion?.subtopic,
                  let topicId = gameModeManager.selectedTopic {
            // Check for subtopic completion in Single Topic Mode
            if areAllSubtopicQuestionsAnswered(subtopic: subtopic, topicId: topicId) {
                completedSubtopicName = subtopic
                completedSubcategoryName = ""
                completedCategoryName = ""
                withAnimation {
                    showingCompletionToast = true
                }

                let questionsAnswered = getAnsweredCountForSubtopic(subtopic: subtopic, topicId: topicId)
                AnalyticsManager.shared.trackCategoryCompleted(
                    category: subtopic,
                    difficultyMode: difficultyManager.selectedDifficulty.rawValue,
                    questionsAnswered: questionsAnswered
                )

                // Auto-dismiss toast after 3 seconds
                DispatchQueue.main.asyncAfter(deadline: .now() + 3.0) {
                    withAnimation {
                        showingCompletionToast = false
                        completedSubtopicName = ""
                    }
                }
            }
        }

        // Show result
        showingQuestion = false
        showingResult = true

        // Capture answer state before clearing
        let wasIncorrect = (answerResult == .incorrect)

        // Auto-clear after delay (use user-configured durations)
        let clearDelay = wasIncorrect ? popupDurationManager.incorrectPopupDuration : popupDurationManager.correctPopupDuration
        DispatchQueue.main.asyncAfter(deadline: .now() + clearDelay) {
            withAnimation(.easeOut(duration: 0.3)) {
                showingResult = false
                currentQuestion = nil
                answerResult = .unanswered
                navigationButtonsDisabled = false // Re-enable all buttons

                // Close modal if it was open
                if shouldUseModalPresentation {
                    showingQuestionModal = false
                }
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

    // MARK: - Modal Dismissal Handler
    private func handleModalDismiss() {
        // Called when modal is dismissed (should not normally happen since dismissal is disabled)
        // This is a fallback in case the modal is dismissed unexpectedly
        withAnimation(.easeOut(duration: 0.3)) {
            showingResult = false
            showingQuestionModal = false
            currentQuestion = nil
            answerResult = .unanswered
            navigationButtonsDisabled = false
        }
    }

    // MARK: - Subtopic Completion Helpers

    private func areAllSubtopicQuestionsAnswered(subtopic: String, topicId: String) -> Bool {
        let subtopicQuestions = gameViewModel.questions.filter { question in
            question.topic == topicId &&
            question.subtopic == subtopic &&
            difficultyManager.selectedDifficulty.shouldInclude(questionDifficulty: question.difficulty) &&
            !phobiaManager.isQuestionExcluded(question.id)
        }

        if subtopicQuestions.isEmpty {
            return true
        }

        return subtopicQuestions.allSatisfy { answeredQuestionsManager.isQuestionAnswered($0.id) }
    }

    private func getAnsweredCountForSubtopic(subtopic: String, topicId: String) -> Int {
        let subtopicQuestions = gameViewModel.questions.filter { question in
            question.topic == topicId &&
            question.subtopic == subtopic &&
            difficultyManager.selectedDifficulty.shouldInclude(questionDifficulty: question.difficulty) &&
            !phobiaManager.isQuestionExcluded(question.id)
        }

        return subtopicQuestions.filter { answeredQuestionsManager.isQuestionAnswered($0.id) }.count
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
                    if gameModeManager.isSingleCategoryMode, let category = gameModeManager.selectedCategory {
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
                    if gameModeManager.isSingleCategoryMode {
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

    private var iconSize: CGFloat {
        switch totalSegments {
        case 0...7:
            return 45  // 2-7 categories: keep current size
        case 8...9:
            return 40  // 8-9 categories: slightly smaller
        case 10...11:
            return 35  // 10-11 categories: medium reduction
        case 12:
            return 30  // 12 categories: most compact
        default:
            return 45  // Fallback to original size
        }
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
                .font(.system(size: iconSize))
                .foregroundColor(.black.opacity(0.75))
                .rotationEffect(.degrees(startAngle + segmentAngle/2)) // Rotate so bottom points to center
                .position(
                    x: 225 + cos(Angle.degrees(startAngle + segmentAngle/2 - 90).radians) * 145,
                    y: 225 + sin(Angle.degrees(startAngle + segmentAngle/2 - 90).radians) * 145
                )
                .overlay(
                        Image(systemName: segmentData.icon)
                            .font(.system(size: iconSize))
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
