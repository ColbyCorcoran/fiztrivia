# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Fiz is a SwiftUI iOS application that provides an interactive trivia game experience. The app features a spinning wheel for category selection, inline question display, automatic streak tracking, personalized user experience, difficulty modes, and persistent leaderboard storage across 7 reorganized categories.

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
6. **Personalized Experience**: Username-based messaging and onboarding flow
7. **Difficulty Filtering**: Configurable question difficulty modes

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
- `DifficultyMode` - Question difficulty filtering (Normal, Easy, Medium, Hard, Difficult)
- `UserManager` - Persistent username and personalization management
- `DifficultyManager` - Persistent difficulty preference management
- `StreakPersistenceManager` - Cross-session streak persistence

### Question Database Structure

**Reorganized Categories** (7 total categories):
- **Entertainment** (209 questions): Harry Potter, Marvel, DC, Star Wars, Pokémon, etc.
- **Sports** (155 questions): Football, Basketball, Baseball, Tennis, Olympics, etc.
- **Bible** (142 questions): Biblical knowledge and teachings
- **History** (176 questions): Ancient, Medieval, Modern, Church History
- **Science** (164 questions): Physics, Chemistry, Biology, Astronomy
- **Earth** (192 questions): Animals, Geography, Weather, Plants, Trees
- **Food** (64 questions): Ingredients, Dishes, Famous Chefs/Restaurants

**Question ID System**:
- Entertainment: `ent_001` through `ent_209`
- Sports: `spt_001` through `spt_155`  
- Bible: `bib_001` through `bib_142`
- History: `his_001` through `his_176`
- Science: `sci_001` through `sci_164`
- Earth: `ear_001` through `ear_192`
- Food: `foo_001` through `foo_064`

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
- **SettingsView**: Username editing, difficulty mode selection, audio/haptic toggles

### Difficulty System

**Difficulty Modes** (`DifficultyMode` enum):
- **Normal**: Mix of all difficulty levels (default)
- **Easy**: Only easy questions
- **Medium**: Only medium questions  
- **Hard**: Only hard questions
- **Difficult**: Medium and hard questions only

**Implementation**:
- Persistent user preference via `DifficultyManager`
- Real-time question filtering in both `GameViewModel` and `CategoryWheelView`
- Settings UI with descriptions for each difficulty mode

### Personalization System

**UserManager Features**:
- **Persistent username storage** across app launches
- **First-time onboarding flow** with optional name entry
- **Personalized messaging** throughout the app
- **Settings integration** for username editing
- **Fallback to "Player"** when no username provided

**Personalized Elements**:
- Welcome tagline: "Trivia, just for [Username]"
- Congratulatory messages: "Excellent, [Username]!"
- Encouraging messages: "Good try, [Username]!"
- Leaderboard headers: "[Username]'s Current Streak"

### UI/UX Patterns

1. **Fixed Layout Architecture**: UI elements never move, only content changes
2. **Immediate Visual Feedback**: Haptic effects, animations, button states
3. **Accessibility First**: Custom helpers, VoiceOver support, button traits
4. **Consistent Visual Design**: Gradient backgrounds across main screens
5. **Auto-Clearing Interfaces**: Minimal user intervention required
6. **Pull-to-Spin Interaction**: Enhanced engagement through gesture controls
7. **Grammar-Aware Text**: Proper singular/plural handling ("1 correct answer" vs "2 correct answers")

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
├── Models/
│   └── TriviaModels.swift       # All data models, managers, enums
├── ViewModels/
│   └── GameViewModel.swift      # Core game logic and state
├── Views/
│   ├── CategoryWheelView.swift  # Main single-screen game interface
│   ├── LeaderboardView.swift    # Achievement history display
│   ├── SettingsView.swift       # User preferences
│   └── OnboardingView.swift     # First-time setup
├── Utils/
│   ├── AccessibilityHelpers.swift
│   └── HapticManager.swift
└── Resources/
    ├── questions.json           # Reorganized trivia database
    └── questions_backup_*.json  # Timestamped backups
```

### Removed Components
- **MainMenuView.swift**: Deleted - no longer needed with single-screen design
- **QuestionView.swift**: Deleted - questions now display inline
- **ResultView.swift**: Deleted - results show inline with auto-clear
- **Random Trivia category**: Removed - questions redistributed to proper categories