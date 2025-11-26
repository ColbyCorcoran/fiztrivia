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

**Current Database (as of last update): 2,107 total questions**

**Reorganized Categories** (7 total categories):
- **Entertainment** (307 questions): Harry Potter, Marvel, DC, Star Wars, Pokémon, Superheroes, Pixar, etc.
- **Sports** (300 questions): Football, Basketball, Baseball, Tennis, Olympics, Hockey, Soccer, Golf
- **Bible** (300 questions): Old Testament, New Testament, Biblical History, Biblical Theology, Biblical Languages, Bible Trivia
- **History** (300 questions): Ancient, Medieval, Modern, Church History
- **Science** (300 questions): Physics, Chemistry, Biology, Astronomy
- **Earth** (300 questions): Animals, Geography, Weather, Plants, Trees
- **Food** (300 questions): Ingredients, Dishes, Famous Chefs/Restaurants, Cuisines, Baking, Beverages, Desserts, Cooking Techniques, Food History, Sauces & Condiments

**Question ID System**:
- Entertainment: `ent_001` through `ent_307`
- Sports: `spt_001` through `spt_326`
- Bible: `bib_001` through `bib_327`
- History: `his_001` through `his_314`
- Science: `sci_001` through `sci_324`
- Earth: `ear_001` through `ear_317`
- Food: `foo_001` through `foo_307`

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

---

## Database Expansion Workflow

**Current Database Status (as of last update):**
- **Total Questions**: 2,107
- **Target per Category**: All categories at 300 (except Entertainment)
- **Entertainment**: 307 questions (naturally larger due to content variety)
- **All Other Categories**: 300 questions each

### Quick Command

When you want to expand the database, use this command format:

```
Let's expand our question database by [X] questions per category
```

Or for total expansion across all categories:

```
Let's expand our question database to [X] questions per category
```

### Automated Workflow Process

When the expansion command is given, follow this systematic process:

#### **Phase 1: Analysis & Planning (5-10 minutes)**

1. **Database Analysis**
   - Run analysis on `Fiz/Resources/questions.json`
   - Count current questions per category and subcategory
   - Identify which categories need questions to reach target
   - Calculate total questions needed

2. **Create Expansion Plan**
   - Determine question distribution across subcategories
   - Set difficulty targets (prioritize: Hard > Medium > Easy)
   - Identify any imbalanced subcategories
   - Create todo list with all tasks

3. **Generate Summary Report**
   ```
   Current: Category breakdown
   Target: X questions per category
   Needed: Y total new questions
   Distribution: By category and subcategory
   ```

#### **Phase 2: Initial Duplicate Check (2-3 minutes)**

1. **Run Pre-Expansion Duplicate Analysis**
   - Check existing database for any duplicates
   - If duplicates found, remove them first
   - Report how many duplicates were removed
   - Update baseline counts

2. **Create Timestamped Backup**
   ```bash
   cp Fiz/Resources/questions.json Fiz/Resources/questions_backup_$(date +%Y%m%d_%H%M%S).json
   ```

#### **Phase 3: Question Generation (Work One Category at a Time)**

For each category that needs expansion:

1. **Review Existing Questions**
   - Read sample questions from each subcategory
   - Note common topics, question patterns, difficulty styles
   - Identify gaps or underrepresented topics

2. **Generate New Questions**
   - Create questions in batches (10-50 at a time depending on total needed)
   - Follow existing ID numbering system
   - Distribute across all subcategories proportionally
   - Emphasize hard and medium difficulty
   - Use specific, detailed questions to avoid duplicates

3. **Content Guidelines**
   - **Family-friendly**: No violence, sexual content, or graphic material
   - **Non-controversial**: Avoid divisive political or religious interpretations
   - **Factual**: Based on verifiable information
   - **Varied**: Different question types, topics, and angles
   - **Specific**: Detailed enough to avoid semantic duplicates
   - **No snakes or spiders**: Never include questions about snakes or spiders in any category

4. **Commit After Each Category**
   ```bash
   git add Fiz/Resources/questions.json [script_files]
   git commit -m "Add [X] [Category] questions to reach [target]

   Distribution across subcategories:
   - [Subcategory]: old → new (+added)

   Difficulty: X hard, Y medium, Z easy
   [Category]: old_count → new_count questions ✓"
   ```

#### **Phase 4: Incremental Duplicate Checking**

After adding questions to each category:

1. **Quick Duplicate Check**
   - Check only the newly added questions against existing database
   - Use similarity matching (exact, semantic >90%, essential >70%)
   - Report any duplicates immediately

2. **If Duplicates Found**
   - Remove duplicate questions
   - Generate replacement questions
   - Verify replacements are unique
   - Re-commit with updated questions

#### **Phase 5: Final Verification (5-10 minutes)**

After all categories completed:

1. **Comprehensive Duplicate Analysis**
   - Run full database duplicate check (all 1,800+ questions)
   - Check for:
     - Exact duplicates (identical text)
     - Semantic duplicates (>90% similar, same answer)
     - Essential duplicates (test same knowledge, 70-90% similar)
   - Generate detailed report

2. **Remove Any Found Duplicates**
   - Create list of all duplicate question IDs
   - Remove duplicates (keep lower ID number)
   - Count how many questions each category needs to reach target

3. **Generate Replacement Questions**
   - Work through each category that needs replacements
   - Generate VERY specific, unique questions
   - Check each replacement against entire database
   - Iterate until all replacements are verified unique

4. **Final Verification**
   - Confirm all categories at target count
   - Verify zero duplicates in database
   - Run final count check

#### **Phase 6: Documentation & Commit**

1. **Update CLAUDE.md**
   - Update "Current Database Status" section at top of this workflow
   - Update question counts in "Question Database Structure" section
   - Update ID ranges if changed

2. **Create Summary Report**
   - Total questions added
   - Duplicates removed
   - Final database statistics
   - Breakdown by category and difficulty

3. **Final Commit and Push**
   ```bash
   git add -A
   git commit -m "Complete database expansion to [X] questions per category

   Summary:
   - Added: X new questions
   - Removed: Y duplicates
   - Replaced: Z questions
   - Final total: [total] questions

   All categories at [target] questions (except Entertainment at [count])
   ✅ All questions verified unique"

   git push -u origin [branch-name]
   ```

### Quality Control Checklist

Before considering expansion complete, verify:

- ✅ All target categories at desired question count
- ✅ Zero duplicates in entire database (verified with analysis tool)
- ✅ Questions distributed across all subcategories
- ✅ Difficulty emphasis on hard/medium as specified
- ✅ All questions follow content guidelines (family-friendly, factual)
- ✅ Backup created before expansion
- ✅ All changes committed and pushed
- ✅ Documentation updated

### Tools & Scripts

**Key Scripts Created During Expansions:**
- `analyze_duplicates.py` - Comprehensive duplicate detection
- `remove_duplicates.py` - Batch duplicate removal
- `add_[category]_to_[target].py` - Category-specific question addition
- `verify_replacements.py` - Replacement question verification

**Duplicate Detection Method:**
```python
# Uses difflib.SequenceMatcher for similarity ratio
# Exact: 100% match
# Semantic: >90% match + same answer
# Essential: 70-90% match + same answer
```

### Common Pitfalls to Avoid

1. **Don't Generate Questions Without Checking Existing Database**
   - Always read existing questions first
   - Note common topics and patterns
   - Avoid creating questions on already-covered facts

2. **Don't Skip Incremental Duplicate Checks**
   - Check after each category, not just at the end
   - Easier to fix 10 duplicates than 50

3. **Don't Batch Commit Too Many Categories**
   - Commit after each category completion
   - Easier to track and debug issues

4. **Don't Ignore Semantic Duplicates**
   - "What is X called?" vs "What is the name of X?" = duplicate
   - Check meaning, not just exact text

5. **Don't Rush Replacement Questions**
   - Take time to make them truly unique
   - Verify each one individually
   - Better to be slow and accurate than fast and duplicate

### Example Expansion Command Interpretations

| User Command | Interpretation | Action |
|--------------|----------------|--------|
| "Expand database by 50 questions per category" | Add 50 to each non-Entertainment category | Add 300 total (6 categories × 50) |
| "Expand database to 300 per category" | Bring all categories to 300 | Calculate difference from current count |
| "Add 100 more questions" | Distribute 100 across all categories | ~16-17 per category |
| "Balance the database with 25 more questions" | Add to underrepresented categories first | Prioritize smallest categories |

### Workflow Efficiency Notes

**Typical Timings:**
- Analysis & Planning: 5-10 minutes
- Question Generation (per category): 10-15 minutes for 50 questions
- Duplicate Checking: 2-5 minutes per check
- Replacement Generation: 5-10 minutes
- Final Verification: 10-15 minutes
- **Total for 50 questions per category (300 total)**: ~2-3 hours

**Optimization Tips:**
- Work category-by-category, not all at once
- Commit frequently (after each category)
- Run duplicate checks incrementally
- Keep replacement batches small (easier to verify)
- Use specific, detailed questions to naturally avoid duplicates
