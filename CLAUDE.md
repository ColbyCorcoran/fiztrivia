# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Fiz is a SwiftUI iOS application that provides an interactive trivia game experience. The app features a spinning wheel for category selection, inline question display, automatic streak tracking, personalized user experience, difficulty modes, single-category focus mode, runtime app icon customization, privacy-first analytics, and persistent leaderboard storage across 7 reorganized categories with detailed subcategory organization.

## Build and Development Commands

### Building the Project
- **Build**: Open `Fiz.xcodeproj` in Xcode and use Cmd+B to build
- **Run**: Use Cmd+R to run in simulator or on device
- **Clean Build**: Product → Clean Build Folder in Xcode

### Testing
- **Run Tests**: Cmd+U in Xcode
- **UI Tests**: Available in `Fiz UITests/` directory

## Architecture Overview

### Core Design Pattern
The app uses **MVVM (Model-View-ViewModel)** architecture with SwiftUI and follows a **single-screen inline experience** with persistent state management.

### Key Architectural Decisions

1. **Single-Screen Experience**: No navigation between screens - everything happens inline on the main wheel view
2. **Auto-Saving Streaks**: Streaks are automatically saved to leaderboard when broken and persist across app launches
3. **Auto-Dismissing Results**: Result screens automatically clear after 1.5 seconds
4. **Inline Question Display**: Questions appear in a fixed area below the wheel without navigation
5. **Pull-to-Spin Gesture**: Enhanced interaction with drag-to-spin functionality
6. **Personalized Experience**: Username-based messaging, onboarding flow, and runtime app icon customization
7. **Difficulty Filtering**: Configurable question difficulty modes (Casual, Normal, Difficult)
8. **Single Category Mode**: Optional focused gameplay on subcategories within a single category
9. **Privacy-First Analytics**: Opt-out by default PostHog integration with user consent management
10. **iOS Version Adaptability**: Native iOS 26 glass buttons with iOS 18 fallback styling

### State Management Flow
```
App Launch → Onboarding (first time) → Category Wheel → Inline Question → Auto-Clear Result → Repeat
```

**Navigation States** (GameState enum):
- `selectingCategory` - Main wheel view (primary state)
- `leaderboard` - Achievement history display
- `settings` - User preferences and game configuration

### Data Models

**Core Models** (`TriviaModels.swift`):
- `TriviaQuestion` - Individual trivia question with category, subcategory, options, correct answer, difficulty
- `TriviaCategory` - Enum of 7 categories (Entertainment, Sports, Bible, History, Science, Earth, Food) with icons and colors
- `GameSession` - Current game state with persistent streak tracking
- `LeaderboardEntry` - SwiftData model for persistent streak storage showing all achievements
- `GameState` - Simplified navigation state enum (3 states)
- `AnswerState` - Question result state (unanswered, correct, incorrect)
- `DifficultyMode` - Question difficulty filtering (Casual, Normal, Difficult)

**Subcategory System**:
- `TriviaSubcategory` - Protocol defining subcategory interface with name, icon, and color
- Category-specific subcategory enums: `EntertainmentSubcategory`, `SportsSubcategory`, `BibleSubcategory`, `HistorySubcategory`, `ScienceSubcategory`, `EarthSubcategory`, `FoodSubcategory`

**Manager Classes** (Singleton Pattern):
- `UserManager` - Persistent username and personalization management
- `DifficultyManager` - Persistent difficulty preference management
- `StreakPersistenceManager` - Cross-session streak persistence
- `AnsweredQuestionsManager` - Tracks answered questions across sessions with completion calculations
- `SingleCategoryModeManager` - Manages single-category focus mode with subcategory filtering
- `HapticSettingsManager` - User haptic feedback preferences
- `AppIconManager` - Runtime app icon switching (6 variants: Correct, Regular Pose, Happy Smirk, Incorrect, Leaderboard, New High Score)

### Question Database Structure

**Reorganized Categories** (7 total categories, 1,408 total questions):
- **Entertainment** (307 questions): Harry Potter, Superheroes, Pokémon, Star Wars, Pixar, Film Score Composers, The Office
- **Sports** (187 questions): Basketball, Tennis, Golf, Soccer, Olympics, Hockey, American Football, Baseball
- **Bible** (185 questions): Old Testament, New Testament, Bible Trivia, Biblical History, Theology, Languages
- **History** (173 questions): Modern, Ancient, Medieval, Church History
- **Science** (175 questions): Biology, Chemistry, Physics, Astronomy
- **Earth** (206 questions): Animals, Weather, Plants, Trees, Geography
- **Food** (175 questions): Ingredients, Famous Chefs/Restaurants, Dishes

**Question ID System**:
- Entertainment: `ent_001` through `ent_307`
- Sports: `spt_001` through `spt_187`
- Bible: `bib_001` through `bib_185`
- History: `his_001` through `his_173`
- Science: `sci_001` through `sci_175`
- Earth: `ear_001` through `ear_206`
- Food: `foo_001` through `foo_175`

**Question Structure**:
```json
{
  "id": "ent_001",
  "category": "Entertainment",
  "subcategory": "Harry Potter",
  "question": "What is the name of Harry Potter's owl?",
  "options": ["Hedwig", "Errol", "Pigwidgeon", "Crookshanks"],
  "correct_answer": "Hedwig",
  "difficulty": "easy"
}
```

### Key Components

**CategoryWheelView** (`CategoryWheelView.swift`):
- **Single-screen experience** with fixed UI layout
- **Inline question display** in a bordered container below the wheel
- **Oversized wheel** (450x450) with shadow effects for dramatic visual impact
- **Pull-to-spin gesture** with drag rotation for enhanced interaction
- **Button disabling system** prevents actions during spins and questions
- **Auto-clear results** after 1.5 seconds
- **Radially oriented category icons** pointing toward wheel center
- **Fixed-height containers** prevent layout shifts
- **Three display states**: placeholder, question, result

**GameViewModel** (`GameViewModel.swift`):
- Loads and parses reorganized JSON question database
- **Difficulty-aware question filtering** based on user preferences
- Handles answer processing with automatic streak persistence
- **Persistent streak management** across app launches
- Simplified state management (3 states instead of navigation-heavy)

**User Experience Components**:
- **OnboardingView**: First-time username setup with skip option
- **LeaderboardView**: Shows ALL streak achievements (not just top unique) with fixed positioning
- **SettingsView**: Navigation hub with personalization and game settings sections
- **PersonalizationSettingsView**: Username editing, app icon selection, haptic toggles, analytics consent
- **GameSettingsView**: Difficulty mode selection, single-category mode, progress tracking, statistics

### Difficulty System

**Difficulty Modes** (`DifficultyMode` enum):
- **Casual**: Easy questions only - perfect for beginners
- **Normal**: Mix of all difficulty levels (default) - balanced experience
- **Difficult**: Medium and hard questions only - challenging gameplay

**Implementation**:
- Persistent user preference via `DifficultyManager`
- Real-time question filtering in both `GameViewModel` and `CategoryWheelView`
- Settings UI with descriptions for each difficulty mode

### Single Category Mode

**Features**:
- Optional focus mode for practicing specific categories
- Wheel displays subcategories instead of main categories when enabled
- Category selection with remaining question counts
- Streak preservation alerts when switching modes
- Progress tracking per subcategory

**Implementation** (`SingleCategoryModeManager`):
- Toggle for enabling/disabling single-category mode
- Persistent selected category storage
- Real-time question filtering by subcategory
- Integration with answered questions tracking

### Analytics Integration

**PostHog Integration** (`AnalyticsManager`):
- Privacy-first approach with opt-out by default
- User consent management with settings toggle
- Data clearing on opt-out

**Tracked Events**:
- App lifecycle (opened, backgrounded)
- Setting changes (difficulty, single-category mode)
- Category completion milestones
- Mode switching behavior

**Privacy Features**:
- Explicit user consent required
- Clear opt-out mechanism in settings
- Data deletion on consent withdrawal

### Personalization System

**UserManager Features**:
- **Persistent username storage** across app launches
- **First-time onboarding flow** with optional name entry
- **Personalized messaging** throughout the app
- **Settings integration** for username editing
- **Fallback to "Player"** when no username provided

**App Icon Customization** (`AppIconManager`):
- **Runtime icon switching** with 6 available variants
- **Visual selection UI** with 3x3 grid in settings
- **Icon variants**: Correct (default), Regular Pose, Happy Smirk, Incorrect, Leaderboard, New High Score
- **Persistent selection** across app launches
- **Touch animations** and visual feedback

**Personalized Elements**:
- Welcome tagline: "Trivia, just for [Username]"
- Congratulatory messages: "Excellent, [Username]!"
- Encouraging messages: "Good try, [Username]!"
- Leaderboard headers: "[Username]'s Current Streak"
- Custom app icon reflecting user preference

### Utility System

**FizColors.swift**:
- Hex-based color system with UIColor extensions
- Adaptive light/dark mode support
- Centralized color palette (8 primary colors: fizBackground, fizOrange, fizCream, fizBrown, fizTeal, fizGray, fizDarkGold, fizLightGold, fizBackgroundSecondary)

**ButtonStyles.swift**:
- iOS 26 native glass button support with iOS 18 fallbacks
- Custom button styles: `glassButtonStyle()`, `answerButtonStyle()`, `prominentActionButton()`
- Scale animation effects (0.95x on press)

**HapticManager.swift**:
- Comprehensive haptic feedback system
- Impact generators (light, medium, heavy) and notification feedback
- Celebration patterns: `correctAnswerEffect()` with bounce sequence
- Integration with user preferences via `HapticSettingsManager`

**AccessibilityHelpers.swift**:
- VoiceOver support extensions
- Reduce motion detection and adaptive animation durations
- Specialized accessibility labels for trivia components

### UI/UX Patterns

1. **Fixed Layout Architecture**: UI elements never move, only content changes
2. **Immediate Visual Feedback**: Haptic effects, animations, button states
3. **Accessibility First**: Custom helpers, VoiceOver support, button traits
4. **Consistent Visual Design**: Gradient backgrounds across main screens with adaptive color system
5. **Auto-Clearing Interfaces**: Minimal user intervention required
6. **Pull-to-Spin Interaction**: Enhanced engagement through gesture controls
7. **Grammar-Aware Text**: Proper singular/plural handling ("1 correct answer" vs "2 correct answers")
8. **iOS Version Adaptability**: Native iOS 26 features with graceful fallbacks

### Development Notes

**Database Management**:
- **Reorganized from 8 to 7 categories** with logical groupings
- **Questions moved between categories** for better organization (Pokémon to Entertainment, Church History to History, etc.)
- **Systematic ID renaming** for consistency across categories
- **Backup files available** with timestamped naming

**SwiftUI Previews**:
- All major views include preview support for real-time iteration
- Uses `.modelContainer(for: LeaderboardEntry.self, inMemory: true)` for data-dependent previews

**Performance Considerations**:
- **Single question load at app launch** - no repeated JSON parsing
- **Difficulty filtering** happens in-memory for fast response
- **Persistent state management** reduces unnecessary recomputation
- **Fixed-height containers** prevent layout recalculations

**State Persistence**:
- **Username**: UserDefaults with UserManager
- **Difficulty preference**: UserDefaults with DifficultyManager  
- **Current streak**: UserDefaults with StreakPersistenceManager
- **Achievement history**: SwiftData with LeaderboardEntry

### File Organization
```
Fiz/
├── FizApp.swift                 # App entry point with SwiftData setup
├── ContentView.swift            # Root navigation controller
├── Models/
│   └── TriviaModels.swift       # All data models, managers, enums (664 lines)
├── ViewModels/
│   └── GameViewModel.swift      # Core game logic and state (230 lines)
├── Views/
│   ├── CategoryWheelView.swift  # Main single-screen game interface (1,052 lines)
│   ├── LeaderboardView.swift    # Achievement history display (199 lines)
│   ├── SettingsView.swift       # Settings navigation hub (78 lines)
│   ├── GameSettingsView.swift   # Game-specific settings (259 lines)
│   ├── PersonalizationSettingsView.swift # Profile & app icon (149 lines)
│   └── OnboardingView.swift     # First-time setup (144 lines)
├── Utils/
│   ├── FizColors.swift          # Color palette & hex utilities
│   ├── ButtonStyles.swift       # iOS 26 glass button styles
│   ├── HapticManager.swift      # Haptic feedback system
│   ├── AnalyticsManager.swift   # PostHog integration
│   └── AccessibilityHelpers.swift # Accessibility extensions
└── Resources/
    ├── questions.json           # Trivia database (19,729 lines)
    ├── questions_backup_20251104_205250.json
    └── questions_backup_20251112_161007.json
```

### Recent Major Updates

**New Features Added**:
1. **Single Category Mode** - Focus gameplay on subcategories within a single category
2. **App Icon Customization** - Runtime switching between 6 icon variants
3. **Privacy-First Analytics** - PostHog integration with opt-out by default
4. **Enhanced Settings Architecture** - Split into PersonalizationSettingsView and GameSettingsView
5. **iOS 26 Glass Buttons** - Native glass styling with iOS 18 fallbacks
6. **Comprehensive Progress Tracking** - Detailed completion statistics per category/subcategory
7. **Enhanced Subcategory System** - Protocol-based subcategory organization with icons and colors

**New Manager Classes**:
- `AnsweredQuestionsManager` - Session-persistent question tracking
- `SingleCategoryModeManager` - Single-category mode state management
- `HapticSettingsManager` - User haptic feedback preferences
- `AppIconManager` - Runtime app icon switching
- `AnalyticsManager` - Privacy-conscious PostHog analytics

**Enhanced Systems**:
- **Difficulty Modes**: Simplified to Casual/Normal/Difficult for better UX
- **Haptic Feedback**: Comprehensive system with celebration patterns
- **Color System**: Hex-based palette with adaptive light/dark mode
- **Button Styling**: Version-aware styling system
- **Accessibility**: Enhanced VoiceOver support and motion preferences

### Removed Components
- **MainMenuView.swift**: Deleted - no longer needed with single-screen design
- **QuestionView.swift**: Deleted - questions now display inline
- **ResultView.swift**: Deleted - results show inline with auto-clear
- **Random Trivia category**: Removed - questions redistributed to proper categories