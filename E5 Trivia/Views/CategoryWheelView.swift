import SwiftUI

struct CategoryWheelView: View {
    @Bindable var gameViewModel: GameViewModel
    @StateObject private var userManager = UserManager.shared
    @StateObject private var difficultyManager = DifficultyManager.shared
    @StateObject private var answeredQuestionsManager = AnsweredQuestionsManager.shared
    @Environment(\.modelContext) private var modelContext
    
    private let categories = TriviaCategory.allCases
    private let segmentAngle = 360.0 / Double(TriviaCategory.allCases.count)
    
    // New state management for inline questions/results
    @State private var showingQuestion = false
    @State private var showingResult = false  
    @State private var navigationButtonsDisabled = false
    @State private var currentQuestion: TriviaQuestion?
    @State private var answerResult: AnswerState = .unanswered
    
    // Drag gesture state for pull-to-spin
    @State private var dragRotation: Double = 0
    @State private var isDragging = false
    
    var body: some View {
        GeometryReader { geometry in
            mainContentView(geometry: geometry)
        }
    }
    
    private func mainContentView(geometry: GeometryProxy) -> some View {
        ZStack {
            backgroundGradient
            uiContentLayer
            wheelLayer(geometry: geometry)
            homeBarGradient
            
            // Celebration overlay for completion
            if gameViewModel.showCompletionCelebration {
                completionCelebrationOverlay
            }
        }
    }
    
    private var backgroundGradient: some View {
        LinearGradient(
            colors: [Color(hex: "#f3eddf"), Color(hex: "#e8dcc8")],
            startPoint: .topLeading,
            endPoint: .bottomTrailing
        )
        .ignoresSafeArea()
    }
    
    private var uiContentLayer: some View {
        VStack(spacing: 0) {
            topToolbar
            titleAndStreakSection
            questionArea
            Spacer()
        }
    }
    
    private var topToolbar: some View {
        HStack {
            Button(action: {
                HapticManager.shared.buttonTapEffect()
                gameViewModel.showLeaderboard()
            }) {
                Image(systemName: "list.number")
                    .font(.title2)
                    .foregroundColor(.primary)
            }
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
                gameViewModel.showSettings()
            }) {
                Image(systemName: "gear")
                    .font(.title2)
                    .foregroundColor(.primary)
            }
            .disabled(navigationButtonsDisabled)
            .opacity(navigationButtonsDisabled ? 0.5 : 1.0)
            .triviaAccessibility(
                label: "Settings",
                hint: "Open app settings",
                traits: .isButton
            )
        }
        .padding(.horizontal, 20)
        .padding(.top, 10)
        .frame(height: 50)
    }
    
    private var titleAndStreakSection: some View {
        HStack {
            VStack (alignment: .leading, spacing: 4) {
                HStack {
                    Text("E5")
                        .font(.system(size: 40, weight: .bold))
                        .foregroundColor(.primary)
                    Image(systemName: "exclamationmark.magnifyingglass")
                        .font(.system(size: 30))
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
                    .foregroundColor(Color(hex: "#533214"))
                Text("\(gameViewModel.gameSession.currentStreak)")
                    .font(.title2)
                    .fontWeight(.bold)
                    .foregroundColor(Color(hex: "#dd7423"))
            }
            .padding(.horizontal, 12)
            .padding(.vertical, 8)
            .background(Color(hex: "#f4d29b"))
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
    
    private var resultView: some View {
        VStack(spacing: 12) {
            Text(answerResult == .correct ? "✅" : "❌")
                .font(.system(size: 40))
                .scaleEffect(showingResult ? 1.2 : 0.5)
                .animation(.spring(response: 0.6, dampingFraction: 0.6), value: showingResult)
            
            Text(answerResult == .correct 
                 ? userManager.personalizedCongratulatoryMessage()
                 : userManager.personalizedEncouragingMessage())
                .font(.title2)
                .fontWeight(.bold)
                .foregroundColor(.primary)
                .multilineTextAlignment(.center)
            
            if answerResult == .incorrect, let question = currentQuestion {
                VStack(spacing: 6) {
                    Text("Correct Answer:")
                        .font(.body)
                        .foregroundColor(.secondary)
                    
                    Text(question.correctAnswer)
                        .font(.title3)
                        .fontWeight(.semibold)
                        .foregroundColor(Color(hex: "#39766d"))
                        .multilineTextAlignment(.center)
                        .padding(.horizontal, 10)
                        .padding(.vertical, 6)
                        .background(Color(hex: "#39766d").opacity(0.15))
                        .cornerRadius(6)
                }
            }
        }
        .padding(20)
    }
    
    private func questionView(for question: TriviaQuestion) -> some View {
        VStack(spacing: 16) {
            VStack(spacing: 8) {
                if let category = gameViewModel.gameSession.selectedCategory {
                    HStack {
                        Image(systemName: category.icon)
                            .font(.title2)
                        Text(category.rawValue)
                            .font(.body)
                            .fontWeight(.semibold)
                    }
                    .foregroundColor(.secondary)
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
                GridItem(.flexible(), spacing: 8),
                GridItem(.flexible(), spacing: 8)
            ], spacing: 8) {
                ForEach(Array(question.options.enumerated()), id: \.offset) { index, option in
                    Button(action: {
                        selectAnswer(option)
                    }) {
                        Text(option)
                            .font(.body)
                            .fontWeight(.medium)
                            .foregroundColor(.primary)
                            .multilineTextAlignment(.center)
                            .lineLimit(nil)
                            .fixedSize(horizontal: false, vertical: true)
                            .frame(maxWidth: .infinity, minHeight: 44)
                            .padding(.horizontal, 12)
                            .padding(.vertical, 10)
                            .background(Color(hex: "#f4d29b"))
                            .cornerRadius(12)
                            .shadow(color: Color(hex: "#533214").opacity(0.15), radius: 2, x: 0, y: 1)
                    }
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
            .fill(Color(hex: "#533214").opacity(0.25))
            .frame(width: 450, height: 450)
            .blur(radius: 15)
            .offset(y: 8)
    }
    
    private var wheelWithGesture: some View {
        ZStack {
            ForEach(Array(categories.enumerated()), id: \.element) { index, category in
                WheelSegment(
                    category: category,
                    index: index,
                    totalSegments: categories.count
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
                if !gameViewModel.isSpinning && !navigationButtonsDisabled {
                    isDragging = true
                    // Convert drag translation to rotation angle
                    let angle = atan2(value.translation.height, value.translation.width) * 180 / .pi
                    dragRotation = angle * 0.5 // Dampening factor for smoother feel
                }
            }
            .onEnded { value in
                isDragging = false
                
                let dragDistance = sqrt(pow(value.translation.width, 2) + pow(value.translation.height, 2))
                if dragDistance > 50 && !gameViewModel.isSpinning && !navigationButtonsDisabled {
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
                .fill(Color(hex: "#f3eddf"))
                .frame(width: 100, height: 100)
                .shadow(color: Color(hex: "#533214").opacity(0.3), radius: 8)
            
            if gameViewModel.isSpinning {
                Image(systemName: "arrow.trianglehead.2.counterclockwise.rotate.90")
                    .font(.system(size: 40))
            } else {
                Button("SPIN") {
                    spinWheelInline()
                }
                .font(.title2)
                .fontWeight(.bold)
                .foregroundColor(.black)
                .disabled(navigationButtonsDisabled)
                .opacity(navigationButtonsDisabled ? 0.5 : 1.0)
            }
        }
    }
    
    private var wheelPointer: some View {
        ZStack {
            Triangle()
                .fill(Color(hex: "#dd7423"))
                .frame(width: 30, height: 20)
                .shadow(color: Color(hex: "#533214").opacity(0.3), radius: 3, x: 0, y: 2)
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
        
        // Start the wheel spin
        gameViewModel.isSpinning = true
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
        // Determine which category was selected
        let normalizedRotation = gameViewModel.wheelRotation.truncatingRemainder(dividingBy: 360)
        let categoryIndex = Int((360 - normalizedRotation) / 51.43) % TriviaCategory.allCases.count
        let selectedCategory = TriviaCategory.allCases[categoryIndex]
        
        gameViewModel.gameSession.selectedCategory = selectedCategory
        
        // Load a random unanswered question from that category
        let categoryQuestions = gameViewModel.questions.filter { question in
            question.category == selectedCategory.rawValue &&
            !answeredQuestionsManager.isQuestionAnswered(question.id) &&
            difficultyManager.selectedDifficulty.shouldInclude(questionDifficulty: question.difficulty)
        }
        
        guard let randomQuestion = categoryQuestions.randomElement() else {
            print("No unanswered questions available for category: \(selectedCategory.rawValue) with difficulty: \(difficultyManager.selectedDifficulty.rawValue)")
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
        guard currentQuestion != nil else { return }
        
        HapticManager.shared.buttonTapEffect()
        
        // Use GameViewModel's answer selection method with ModelContext
        gameViewModel.selectAnswer(answer, modelContext: modelContext)
        answerResult = gameViewModel.gameSession.answerState
        
        // Show result
        showingQuestion = false
        showingResult = true
        
        // Auto-clear after 1.5 seconds and re-enable buttons
        DispatchQueue.main.asyncAfter(deadline: .now() + 1.5) {
            withAnimation(.easeOut(duration: 0.3)) {
                showingResult = false
                currentQuestion = nil
                answerResult = .unanswered
                navigationButtonsDisabled = false // Re-enable all buttons
            }
        }
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
                // Celebration emojis
                HStack(spacing: 20) {
                    Text("🎉")
                        .font(.system(size: 60))
                        .scaleEffect(gameViewModel.showCompletionCelebration ? 1.2 : 0.5)
                        .animation(.spring(response: 0.8, dampingFraction: 0.6).delay(0.1), value: gameViewModel.showCompletionCelebration)
                    
                    Text("🏆")
                        .font(.system(size: 60))
                        .scaleEffect(gameViewModel.showCompletionCelebration ? 1.2 : 0.5)
                        .animation(.spring(response: 0.8, dampingFraction: 0.6).delay(0.2), value: gameViewModel.showCompletionCelebration)
                    
                    Text("🎊")
                        .font(.system(size: 60))
                        .scaleEffect(gameViewModel.showCompletionCelebration ? 1.2 : 0.5)
                        .animation(.spring(response: 0.8, dampingFraction: 0.6).delay(0.3), value: gameViewModel.showCompletionCelebration)
                }
                
                VStack(spacing: 16) {
                    Text("Congratulations, \(userManager.displayName)!")
                        .font(.largeTitle)
                        .fontWeight(.bold)
                        .foregroundColor(.white)
                        .multilineTextAlignment(.center)
                        .opacity(gameViewModel.showCompletionCelebration ? 1 : 0)
                        .animation(.easeInOut(duration: 0.8).delay(0.4), value: gameViewModel.showCompletionCelebration)
                    
                    Text("You've answered all questions in the \(difficultyManager.selectedDifficulty.rawValue) difficulty mode!")
                        .font(.title2)
                        .foregroundColor(.white.opacity(0.9))
                        .multilineTextAlignment(.center)
                        .padding(.horizontal, 20)
                        .opacity(gameViewModel.showCompletionCelebration ? 1 : 0)
                        .animation(.easeInOut(duration: 0.8).delay(0.6), value: gameViewModel.showCompletionCelebration)
                    
                    HStack(spacing: 8) {
                        Text("Total Questions Answered:")
                            .font(.body)
                            .foregroundColor(.white.opacity(0.8))
                        Text("\(gameViewModel.getAnsweredQuestionsCount())")
                            .font(.title2)
                            .fontWeight(.bold)
                            .foregroundColor(Color(hex: "#f3d29d"))
                    }
                    .opacity(gameViewModel.showCompletionCelebration ? 1 : 0)
                    .animation(.easeInOut(duration: 0.8).delay(0.8), value: gameViewModel.showCompletionCelebration)
                }
                
                Button(action: {
                    HapticManager.shared.buttonTapEffect()
                    gameViewModel.resetAllProgress()
                }) {
                    HStack(spacing: 12) {
                        Text("🔄")
                            .font(.title2)
                        Text("Play Again")
                            .font(.title2)
                            .fontWeight(.semibold)
                    }
                    .foregroundColor(.white)
                    .padding(.horizontal, 32)
                    .padding(.vertical, 16)
                    .background(Color(hex: "#dd7423"))
                    .cornerRadius(25)
                    .shadow(color: Color(hex: "#533214").opacity(0.3), radius: 10, x: 0, y: 5)
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
    let category: TriviaCategory
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
            .fill(Color(hex: category.color))
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
                .stroke(Color.white, lineWidth: 3)
            )
            
            // Category icon - larger and radially oriented
            Image(systemName: category.icon)
                .font(.system(size: 45))
                .foregroundColor(.black.opacity(0.75))
                .rotationEffect(.degrees(startAngle + segmentAngle/2)) // Rotate so bottom points to center
                .position(
                    x: 225 + cos(Angle.degrees(startAngle + segmentAngle/2 - 90).radians) * 145,
                    y: 225 + sin(Angle.degrees(startAngle + segmentAngle/2 - 90).radians) * 145
                )
                .overlay(
                        Image(systemName: category.icon)
                            .font(.system(size: 45))
                            .foregroundColor(.white.opacity(0.5))
                            .blur(radius: 1)
                            .offset(x: -1, y: -1)
                    )
                    .shadow(color: Color.black.opacity(0.3), radius: 2, x: 2, y: 2)
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

#Preview {
    CategoryWheelView(gameViewModel: GameViewModel())
        .modelContainer(for: LeaderboardEntry.self, inMemory: true)
}
