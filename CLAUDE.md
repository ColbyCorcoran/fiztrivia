# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Fiz is a SwiftUI iOS application that provides an interactive trivia game experience. The app features a spinning wheel for category selection, inline question display, automatic streak tracking, personalized user experience, difficulty modes, game mode system (Regular, Single Category, Single Topic), **IAP expansion packs** with topic-based gameplay, runtime app icon customization, privacy-first analytics, and persistent leaderboard storage across 12 categories with detailed subcategory organization.

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
8. **Game Mode System**: Three distinct modes with mode-specific state management
   - **Multi-Category Mode**: Mix of all selected categories (with customizable category selection)
   - **Single Category Mode**: Focus on subcategories within one category
   - **Single Topic Mode**: Focus on subtopics from purchased expansion packs
9. **Expansion Pack System**: IAP-based topic packs with optional install/uninstall
   - One-time purchases with Family Sharing support
   - Free preview questions (10% per pack)
   - Bundled in app (JSON files, not downloads)
   - Seamless integration into existing categories
10. **Privacy-First Analytics**: Opt-out by default PostHog integration with user consent management
11. **iOS Version Adaptability**: Native iOS 26 glass buttons with iOS 18 fallback styling
12. **Adaptive Question Display**: Questions display inline by default, but automatically switch to scrollable modal for Dynamic Type sizes of .accessibility3 and above, ensuring content remains readable for users with large text preferences

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
- `TriviaQuestion` - Individual trivia question with category, subcategory, topic, subtopic, options, correct answer, difficulty
- `TriviaCategory` - Enum of 12 categories (Entertainment, Sports, Music, Technology, Art, Geography, Science, Literature, Nature, History, Bible, Food) with icons and colors
- `GameSession` - Current game state with persistent streak tracking
- `LeaderboardEntry` - SwiftData model for persistent streak storage showing all achievements
- `GameState` - Simplified navigation state enum (3 states)
- `AnswerState` - Question result state (unanswered, correct, incorrect)
- `DifficultyMode` - Question difficulty filtering (Casual, Normal, Difficult)
- `GameMode` - Game mode enum (Multi-Category, Single Category, Single Topic)
- `ExpansionPack` - Expansion pack model with packId, packName, subtopics, questions, pricing
- `DifficultyBreakdown` - Question distribution by difficulty level

**Subcategory System**:
- `TriviaSubcategory` - Protocol defining subcategory interface with name, icon, and color
- Category-specific subcategory enums: `EntertainmentSubcategory`, `SportsSubcategory`, `BibleSubcategory`, `HistorySubcategory`, `ScienceSubcategory`, `EarthSubcategory`, `FoodSubcategory`

**Manager Classes** (Singleton Pattern):
- `UserManager` - Persistent username and personalization management
- `DifficultyManager` - Persistent difficulty preference management
- `StreakPersistenceManager` - Cross-session streak persistence
- `AnsweredQuestionsManager` - Tracks answered questions across sessions with completion calculations
- `GameModeManager` - Manages game mode state (Multi-Category, Single Category, Single Topic) with mode-specific settings
- `ExpansionPackManager` - Manages expansion pack state (available, purchased, installed), loads pack JSONs
- `StoreManager` - StoreKit 2 integration for IAP purchases, transaction verification, Family Sharing
- `HapticSettingsManager` - User haptic feedback preferences
- `AppIconManager` - Runtime app icon switching (6 variants: Correct, Regular Pose, Happy Smirk, Incorrect, Leaderboard, New High Score)
- `AnalyticsManager` - Privacy-conscious PostHog analytics integration

### Question Database Structure

**Current Database (as of last update): 2,107 base questions + expansion packs**

**Main Categories** (12 total categories):
- **Entertainment**: Animation, Sci-Fi/Fantasy, Action/Adventure, Drama/Comedy
- **Sports**: Team Sports, Individual Sports, International Competition, Extreme & Action Sports, Sports History & Records, Athletes & Biography
- **Music**: History & Eras, Musicians & Bands, Awards & Records, Instruments & Theory, Film & TV
- **Technology**: Video Games, Computers & Software, Internet & Social Media, Tech Companies, Inventions
- **Art**: Famous Painters, Art History & Movements, Sculpture, Architecture, Photography
- **Geography**: U.S. Geography, World Geography, Flags, Landmarks & Monuments, Maps & Borders
- **Science**: Biology, Chemistry, Physics, Astronomy
- **Literature**: Fantasy Literature, Classic Literature, Modern Fiction, Poetry, Children's Books, Authors & Biography
- **Nature**: Trees, Weather, Plants & Flowers, Animals & Wildlife, Oceans & Marine Life
- **History**: Modern History, Ancient History, Medieval History, Church History
- **Bible**: Bible Trivia, Biblical History, Biblical Theology, Bible Languages
- **Food**: Ingredients, Baking & Desserts, Cooking, Food History, Dishes & Cuisines, Beverages

**Expansion Packs** (5 launch packs):
1. **Harry Potter** (500 questions, $2.99) - Subtopics: Characters, Spells, Locations, Books, Movies, Trivia
2. **Pokémon** (500 questions, $2.99) - Subtopics: Gen 1-3, Gen 4-6, Gen 7-9, Games, Anime, Cards
3. **80s Trivia** (400 questions, $2.99) - Subtopics: Movies, Music, TV Shows, Sports, History, Pop Culture
4. **Disney** (500 questions, $2.99) - Subtopics: Animated Classics, Pixar, Live Action, Parks, Characters, Songs
5. **The Office** (300 questions, $1.99) - Subtopics: Characters, Episodes, Quotes, Relationships, Locations, Trivia

**Question Structure** (Base Questions):
```json
{
  "id": "ent_001",
  "category": "Entertainment",
  "subcategory": "Animation",
  "question": "What is the name of Harry Potter's owl?",
  "options": ["Hedwig", "Errol", "Pigwidgeon", "Crookshanks"],
  "correct_answer": "Hedwig",
  "difficulty": "easy"
}
```

**Question Structure** (Expansion Pack Questions):
```json
{
  "id": "hp_001",
  "category": "Entertainment",
  "subcategory": "Sci-Fi/Fantasy",
  "topic": "com.fiz.pack.harry_potter",
  "subtopic": "Characters",
  "question": "What is Hermione Granger's patronus?",
  "options": ["Otter", "Cat", "Dog", "Horse"],
  "correct_answer": "Otter",
  "difficulty": "medium"
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
- **GameModesSettingsView**: Game mode selection (Multi-Category, Single Category, Single Topic), mode-specific configuration, category selection and management for Multi-Category mode
- **StoreView**: Full-screen modal for browsing and purchasing expansion packs with beautiful card UI
- **StoreManager**: StoreKit 2 implementation for IAP management, transaction verification, Family Sharing

**Shared Question Components**:
- **QuestionContentView** (`QuestionContentView.swift`): Shared question display component used in both inline and modal contexts. Displays category header, question text, and answer button grid with callback-based answer selection.
- **ResultContentView** (`ResultContentView.swift`): Shared result display component for correct/incorrect feedback. Shows Fiz mascot, personalized messages, and correct answer. Consistent presentation across inline and modal modes.
- **QuestionModalView** (`QuestionModalView.swift`): Modal wrapper for question presentation with large Dynamic Type. Includes ScrollView for accessibility with large text sizes. Prevents dismissal during result display and handles graceful fallback.

### Difficulty System

**Difficulty Modes** (`DifficultyMode` enum):
- **Casual**: Easy questions only - perfect for beginners
- **Normal**: Mix of all difficulty levels (default) - balanced experience
- **Difficult**: Medium and hard questions only - challenging gameplay

**Implementation**:
- Persistent user preference via `DifficultyManager`
- Real-time question filtering in both `GameViewModel` and `CategoryWheelView`
- Settings UI with descriptions for each difficulty mode

### Game Mode System

**Three Game Modes** (`GameMode` enum):
1. **Multi-Category Mode**: Mix of all selected categories (default) - includes category selection UI with 2-12 category picker, save/reset defaults
2. **Single Category Mode**: Focus on subcategories within one category
3. **Single Topic Mode**: Focus on subtopics from purchased expansion packs

**Features**:
- Mode-specific wheel configuration (categories, subcategories, or subtopics)
- Streak preservation alerts when switching modes
- Persistent mode selection across app launches
- Progress tracking per mode
- Category/topic selection with remaining question counts
- Invalid state validation (e.g., ensures selected topic is still installed)

**Implementation** (`GameModeManager`):
- Centralized game mode state management
- Mode-specific settings persistence (selectedCategory, selectedTopic)
- Real-time question filtering by mode
- Automatic state validation and cleanup
- Integration with ExpansionPackManager for topic mode

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
9. **Dynamic Type Adaptive Modals**: Conditional modal presentation based on user's text size preference for enhanced accessibility with large text

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
├── Configuration.storekit       # StoreKit testing configuration
├── Models/
│   └── TriviaModels.swift       # All data models, managers, enums
├── ViewModels/
│   └── GameViewModel.swift      # Core game logic and state
├── Views/
│   ├── CategoryWheelView.swift  # Main single-screen game interface with adaptive modal
│   ├── QuestionContentView.swift # Shared question rendering component
│   ├── ResultContentView.swift  # Shared result rendering component
│   ├── QuestionModalView.swift  # Modal wrapper for large text accessibility
│   ├── LeaderboardView.swift    # Achievement history display
│   ├── SettingsView.swift       # Settings navigation hub
│   ├── StoreView.swift          # Expansion pack store UI
│   ├── OnboardingView.swift     # First-time setup
│   └── Settings/
│       ├── GameModesSettingsView.swift # Game mode selection & configuration
│       ├── PersonalizationSettingsView.swift # Profile & app icon
│       └── [other settings views]
├── Utils/
│   ├── FizColors.swift          # Color palette & hex utilities
│   ├── ButtonStyles.swift       # iOS 26 glass button styles
│   ├── HapticManager.swift      # Haptic feedback system
│   ├── AnalyticsManager.swift   # PostHog integration
│   ├── StoreManager.swift       # StoreKit 2 IAP integration
│   └── AccessibilityHelpers.swift # Accessibility extensions
└── Resources/
    ├── questions.json           # Base trivia database
    ├── expansion_harry_potter.json   # Harry Potter expansion pack
    ├── expansion_pokemon.json        # Pokémon expansion pack
    ├── expansion_80s_trivia.json     # 80s Trivia expansion pack
    ├── expansion_disney.json         # Disney expansion pack
    └── expansion_the_office.json     # The Office expansion pack
```

### Recent Major Updates

**Expansion Pack System** (Latest):
1. **IAP Integration** - StoreKit 2 with modern async/await, Family Sharing support
2. **Store UI** - Beautiful scrollable store with pack cards, purchase flow, install/uninstall
3. **Single Topic Mode** - New game mode focusing on expansion pack subtopics
4. **Expansion Packs** - 5 launch packs with sample data (Harry Potter, Pokémon, 80s Trivia, Disney, The Office)
5. **Free Previews** - 10% of questions in each pack available to all users
6. **Game Mode Migration** - Replaced SingleCategoryModeManager with unified GameModeManager

**Previous Features**:
1. **Game Mode Consolidation** - Renamed Regular mode to Multi-Category, integrated category selection into GameModesSettingsView, mode indicator now visible for all modes
2. **Game Mode System** - Three modes (Multi-Category, Single Category, Single Topic) with unified management
3. **App Icon Customization** - Runtime switching between 6 icon variants
4. **Privacy-First Analytics** - PostHog integration with opt-out by default
5. **Enhanced Settings Architecture** - Reorganized into GameModesSettingsView and PersonalizationSettingsView
6. **iOS 26 Glass Buttons** - Native glass styling with iOS 18 fallbacks
7. **Comprehensive Progress Tracking** - Detailed completion statistics per category/subcategory
8. **Enhanced Subcategory System** - Protocol-based subcategory organization with icons and colors

**Manager Classes Added**:
- `ExpansionPackManager` - Expansion pack state and question management
- `StoreManager` - StoreKit 2 IAP integration
- `GameModeManager` - Unified game mode state management (replaced SingleCategoryModeManager)
- `AnalyticsManager` - Privacy-conscious PostHog analytics
- `AnsweredQuestionsManager` - Session-persistent question tracking
- `HapticSettingsManager` - User haptic feedback preferences
- `AppIconManager` - Runtime app icon switching

### Removed Components
- **MainMenuView.swift**: Deleted - no longer needed with single-screen design
- **QuestionView.swift**: Deleted - questions now display inline
- **ResultView.swift**: Deleted - results show inline with auto-clear
- **Random Trivia category**: Removed - questions redistributed to proper categories
- **SingleCategoryModeManager**: Migrated to unified GameModeManager
- **CategorySelectionSettingsView**: Deleted - functionality integrated into GameModesSettingsView

---

## Expansion Pack System

### Architecture Overview

The expansion pack system enables optional IAP topic packs that seamlessly integrate into the existing game. Each pack contains questions organized by **subtopics** that populate the wheel in Single Topic Mode.

**Key Design Principles**:
- **Bundled in App**: JSON files shipped with the app, not downloads
- **Optional Install**: Users can uninstall packs they own to save space
- **Free Previews**: 10% of questions in each pack available to all users
- **Family Sharing**: One-time purchases shared across family members
- **Cross-Category**: Topic questions can span multiple main categories

### Data Architecture

**ExpansionPack Model** (`TriviaModels.swift`):
```swift
struct ExpansionPack: Codable, Identifiable {
    let packId: String  // "com.fiz.pack.harry_potter"
    let packName: String
    let packDescription: String
    let subtopics: [String]  // ["Characters", "Spells", "Locations", ...]
    let questionCount: Int
    let freePreviewCount: Int
    let difficulty: DifficultyBreakdown
    let price: Double
    let icon: String
    let freePreviewQuestions: [TriviaQuestion]
    let paidQuestions: [TriviaQuestion]
}
```

**ExpansionPackManager** (`TriviaModels.swift`):
- Loads all `expansion_*.json` files from bundle on init
- Tracks purchased pack IDs (synced with StoreKit)
- Tracks installed pack IDs (user preference, separate from purchase)
- Provides questions based on purchase/install state
- Persists state to UserDefaults

**StoreManager** (`Utils/StoreManager.swift`):
- StoreKit 2 async/await integration
- Product loading and caching
- Purchase flow with transaction verification
- Transaction listener for Family Sharing
- Restore purchases functionality
- Automatic sync with ExpansionPackManager

### Pack Structure

**JSON File Format** (`expansion_[name].json`):
```json
{
  "packId": "com.fiz.pack.harry_potter",
  "packName": "Harry Potter",
  "packDescription": "Dive deep into the wizarding world...",
  "subtopics": ["Characters", "Spells", "Locations", "Books", "Movies", "Trivia"],
  "questionCount": 500,
  "freePreviewCount": 50,
  "difficulty": {
    "easy": 150,
    "medium": 250,
    "hard": 100
  },
  "price": 2.99,
  "icon": "wand.and.stars",
  "freePreviewQuestions": [...],  // 10% of total
  "paidQuestions": [...]           // Remaining 90%
}
```

**Question Tagging**:
- All questions have `topic` (packId) and `subtopic` fields
- Questions also have `category` and `subcategory` for proper categorization
- Example: A Harry Potter question about wands would be:
  - `category`: "Entertainment"
  - `subcategory`: "Sci-Fi/Fantasy"
  - `topic`: "com.fiz.pack.harry_potter"
  - `subtopic`: "Spells"

### User Flow

**Purchase & Install**:
1. User opens Store from CategoryWheelView
2. Browses expansion packs with pricing
3. Purchases pack via StoreKit 2
4. Pack auto-installs after purchase
5. Pack immediately available in Single Topic Mode

**Playing in Single Topic Mode**:
1. Navigate to Settings → Game Modes
2. Select "Single Topic" mode
3. Choose installed pack from picker
4. Wheel displays pack's subtopics
5. Questions filtered by topic AND subtopic

**Managing Packs**:
- **Uninstall**: Owned pack can be uninstalled to save space, questions removed from pool
- **Reinstall**: Uninstalled pack can be reinstalled anytime (no repurchase)
- **Restore Purchases**: Syncs purchase state across devices (Family Sharing)

### Integration Points

**GameViewModel**:
- `loadQuestions()` includes expansion pack questions
- Merges base questions + free previews + installed packs
- Questions loaded once at app launch

**CategoryWheelView**:
- Wheel configuration changes based on game mode
- Single Topic Mode: displays pack subtopics with pack icon
- Question filtering by `topic` and `subtopic`

**GameModeManager**:
- Validates selected topic is still installed
- Resets to Regular mode if topic becomes unavailable
- Persists selected topic across launches

**Analytics**:
- Tracks store views, pack views, purchases
- Tracks install/uninstall events
- Tracks topic mode usage

### StoreKit Configuration

**Configuration.storekit** (for testing):
- 5 non-consumable products
- Family Sharing enabled
- Matches pack pricing from JSONs

**Production** (App Store Connect):
- Create matching product IDs
- Set actual pricing tiers
- Enable Family Sharing
- Add localized descriptions

---

## Adding New Expansion Packs Workflow

Use this workflow when creating new expansion pack content.

### Quick Command

```
Let's create a new expansion pack: [Pack Name] with [X] questions
```

### Step-by-Step Process

#### **Phase 1: Pack Design (5 minutes)**

1. **Define Pack Details**
   - Pack name (e.g., "Star Wars")
   - Pack ID format: `com.fiz.pack.[lowercase_name]`
   - Target question count (200-500 recommended)
   - Price point ($1.99 - $4.99 typical)
   - SF Symbol icon name

2. **Design Subtopics** (6-8 recommended)
   - List specific subtopics that will populate the wheel
   - Ensure good variety and coverage
   - Examples:
     - Star Wars: "Original Trilogy", "Prequels", "Sequels", "Characters", "Planets", "Vehicles"
     - Marvel: "Avengers", "X-Men", "Spider-Man", "Villains", "MCU", "Comics"

3. **Plan Category Distribution**
   - Identify which main categories questions will use
   - Tag with appropriate category/subcategory combinations
   - Topics can span multiple categories (e.g., Star Wars uses Entertainment, Science, History)

#### **Phase 2: Create JSON Structure (2 minutes)**

1. **Create File**: `Fiz/Resources/expansion_[name].json`

2. **Set Up Metadata**:
```json
{
  "packId": "com.fiz.pack.[name]",
  "packName": "[Display Name]",
  "packDescription": "[One sentence description for Store UI]",
  "subtopics": ["Sub 1", "Sub 2", "Sub 3", "Sub 4", "Sub 5", "Sub 6"],
  "questionCount": 500,
  "freePreviewCount": 50,
  "difficulty": {
    "easy": 150,
    "medium": 250,
    "hard": 100
  },
  "price": 2.99,
  "icon": "sf.symbol.name",
  "freePreviewQuestions": [],
  "paidQuestions": []
}
```

#### **Phase 3: Generate Questions (30-60 minutes for 500 questions)**

1. **Review Existing Packs**
   - Read sample questions from similar packs
   - Note ID format, difficulty distribution, question styles

2. **Generate Questions in Batches**
   - Create 50-100 questions at a time
   - Distribute across all subtopics evenly
   - Follow difficulty targets (emphasize medium/hard)
   - Use ID format: `[prefix]_[number]` (e.g., `hp_001`, `sw_042`)

3. **Question Structure**:
```json
{
  "id": "sw_001",
  "category": "Entertainment",
  "subcategory": "Sci-Fi/Fantasy",
  "topic": "com.fiz.pack.star_wars",
  "subtopic": "Original Trilogy",
  "question": "What planet is Luke Skywalker from?",
  "options": ["Tatooine", "Hoth", "Dagobah", "Endor"],
  "correct_answer": "Tatooine",
  "difficulty": "easy"
}
```

4. **Content Guidelines**
   - **Family-friendly**: No violence, sexual content, or graphic material
   - **Factual**: Based on verifiable canon information
   - **Varied**: Different question types and angles
   - **Specific**: Detailed enough to avoid duplicates
   - **No snakes or spiders**: Never include these topics

5. **Split Free vs Paid**
   - First 10% of questions → `freePreviewQuestions`
   - Remaining 90% → `paidQuestions`
   - Include variety of difficulty in free preview

#### **Phase 4: StoreKit Configuration (2 minutes)**

1. **Update Configuration.storekit**
   - Add new product entry
   - Set product ID matching pack ID
   - Set display price
   - Enable Family Sharing
   - Add localized description

2. **Example Entry**:
```json
{
  "displayPrice": "2.99",
  "familyShareable": true,
  "internalID": "6736890006",
  "localizations": [
    {
      "description": "[Pack description]",
      "displayName": "[Pack Name] Expansion Pack",
      "locale": "en_US"
    }
  ],
  "productID": "com.fiz.pack.[name]",
  "referenceName": "[Pack Name] Pack",
  "type": "NonConsumable"
}
```

#### **Phase 5: Testing & Verification (5 minutes)**

1. **Validate JSON**
   - Run Python validation script (if available)
   - Check structure matches ExpansionPack model
   - Verify question counts match metadata

2. **Test in App**
   - Launch app, check Store loads pack
   - Verify pack card displays correctly
   - Test "purchase" in sandbox (auto-installs)
   - Enter Single Topic Mode, select pack
   - Verify wheel shows subtopics
   - Spin and answer questions from pack
   - Verify uninstall/reinstall flow

#### **Phase 6: Commit & Document (3 minutes)**

1. **Commit Pack**:
```bash
git add Fiz/Resources/expansion_[name].json Fiz/Configuration.storekit
git commit -m "Add [Pack Name] expansion pack

New pack: [Pack Name] ([X] questions, $[price])
Subtopics: [list]
Difficulty: XE / YM / ZH
Categories: [list of categories used]

Ready for production IAP setup in App Store Connect"
```

2. **Update CLAUDE.md**
   - Add pack to "Expansion Packs" list
   - Update pack count in Project Overview
   - Note in Recent Major Updates if significant

### Quality Checklist

Before marking pack complete:

- ✅ JSON file validated and loads in app
- ✅ All required fields present (packId, subtopics, questions, etc.)
- ✅ Question count matches metadata
- ✅ Free preview is exactly 10% of total
- ✅ Difficulty distribution matches target
- ✅ All questions have topic + subtopic fields
- ✅ All questions use valid category/subcategory combinations
- ✅ StoreKit configuration updated
- ✅ Pack displays correctly in Store UI
- ✅ Purchase/install flow tested
- ✅ Single Topic Mode works with pack
- ✅ Uninstall/reinstall tested
- ✅ All questions follow content guidelines
- ✅ Documentation updated

### Pack Pricing Strategy

**Recommended Pricing Tiers**:
- **200-300 questions**: $1.99
- **300-400 questions**: $2.99
- **400-500 questions**: $3.99
- **500+ questions**: $4.99

**Special Considerations**:
- Niche topics can command premium ($3.99-$4.99)
- Broad appeal topics (Disney, Marvel) → standard pricing
- Limited appeal (The Office) → lower pricing ($1.99)

### Example Pack Ideas

**Potential Future Packs**:
- **Star Wars** (500q, $2.99): OT, Prequels, Sequels, Characters, Planets, Vehicles
- **Marvel** (500q, $2.99): Avengers, X-Men, Spider-Man, Villains, MCU, Comics
- **Lord of the Rings** (400q, $2.99): Fellowship, Races, Locations, Books, Movies, Lore
- **Friends** (300q, $1.99): Characters, Episodes, Quotes, Relationships, Locations, Trivia
- **Soccer/Football** (400q, $2.99): Players, Teams, World Cup, Leagues, History, Records
- **90s Nostalgia** (400q, $2.99): Movies, Music, TV, Technology, Events, Culture

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
