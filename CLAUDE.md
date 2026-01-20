# CLAUDE.md

Project guidance for Claude Code when working with Fiz codebase.

## Project Overview

Fiz is a SwiftUI iOS trivia game with spinning wheel category selection, inline questions, automatic streak tracking, personalized experience, difficulty modes, 3 game modes (Multi-Category, Single Category, Single Topic), IAP expansion packs, runtime app icon switching, privacy-first analytics, and persistent leaderboard across 12 categories.

## Build Commands

- **Build**: Cmd+B in Xcode
- **Run**: Cmd+R
- **Clean**: Product → Clean Build Folder
- **Tests**: Cmd+U

## Architecture

**MVVM** with SwiftUI, single-screen inline experience, persistent state management.

### Key Design Decisions

1. **Single-Screen**: All interactions inline on wheel view, no navigation
2. **Auto-Save/Dismiss**: Streaks auto-save on break, results clear after 1.5s
3. **Inline Questions**: Fixed area below wheel
4. **Pull-to-Spin**: Drag gesture interaction
5. **Personalization**: Username messaging, onboarding, app icon switching
6. **Difficulty Modes**: Casual (easy), Normal (all), Difficult (med+hard)
7. **Game Modes**: Multi-Category (2-12 categories), Single Category (subcategories), Single Topic (expansion pack subtopics)
8. **Expansion Packs**: IAP topic packs, optional install/uninstall, 10% free preview, Family Sharing, bundled JSON
9. **Analytics**: Opt-in by default, PostHog, 57+ events, privacy-conscious
10. **Accessibility**: iOS 26 glass buttons w/ iOS 18 fallback, inline→modal for large Dynamic Type (.accessibility3+)

### State Flow
```
Launch → Onboarding → Wheel → Question → Result → Repeat
```

**GameState enum**: `selectingCategory`, `leaderboard`, `settings`

### Data Models (`TriviaModels.swift`)

**Core**: `TriviaQuestion`, `TriviaCategory` (12 categories), `GameSession`, `LeaderboardEntry` (SwiftData), `GameState`, `AnswerState`, `DifficultyMode`, `GameMode`, `ExpansionPack`, `DifficultyBreakdown`

**Subcategories**: Protocol `TriviaSubcategory` + enums per category (Entertainment, Sports, Bible, History, Science, Earth, Food)

**Managers** (Singletons):
- `UserManager` - Username/personalization
- `DifficultyManager` - Difficulty preference
- `StreakPersistenceManager` - Cross-session streaks
- `AnsweredQuestionsManager` - Question tracking/completion
- `GameModeManager` - Mode state & settings
- `ExpansionPackManager` - Pack state/loading
- `StoreManager` - StoreKit 2 IAP
- `CartManager` - Shopping cart
- `DiscountCodeManager` - Discount validation
- `HapticSettingsManager` - Haptic preferences
- `AppIconManager` - Icon switching (6 variants)
- `AnalyticsManager` - PostHog (57+ events)

### Question Database

**2,107 base questions + 5 expansion packs**

**12 Categories**: Entertainment, Sports, Music, Technology, Art, Geography, Science, Literature, Nature, History, Bible, Food (each with 4-6 subcategories)

**Expansion Packs**:
1. Harry Potter (500q, $2.99) - 6 subtopics
2. Pokémon (500q, $2.99) - 6 subtopics
3. 80s Trivia (400q, $2.99) - 6 subtopics
4. Disney (500q, $2.99) - 6 subtopics
5. The Office (300q, $1.99) - 6 subtopics

**Question Fields**: Base has `id`, `category`, `subcategory`, `question`, `options[]`, `correct_answer`, `difficulty`. Expansion adds `topic` (packId), `subtopic`.

### Key Components

**CategoryWheelView**: Single-screen, inline questions, 450x450 wheel, pull-to-spin gesture, button disabling during spins, auto-clear results (1.5s), radial icons, fixed-height containers, 3 states (placeholder/question/result)

**GameViewModel**: Loads JSON DB, difficulty filtering, answer processing, persistent streaks

**Views**:
- OnboardingView - First-time setup
- LeaderboardView - All achievements
- SettingsView - Settings hub
- PersonalizationSettingsView - Username, icon, haptics, analytics
- GameModesSettingsView - Mode selection, category/topic pickers
- StoreView - Expansion pack browsing/purchase
- CartView - Multi-pack checkout, discounts
- QuestionContentView - Shared question rendering (inline/modal)
- ResultContentView - Shared result feedback
- QuestionModalView - Large Dynamic Type modal wrapper

### Difficulty & Game Modes

**Difficulty** (`DifficultyMode`): Casual (easy only), Normal (all - default), Difficult (med+hard). Persistent via `DifficultyManager`, real-time filtering.

**Game Modes** (`GameMode`):
1. Multi-Category - Mix 2-12 categories (default)
2. Single Category - Subcategories within one category
3. Single Topic - Subtopics from expansion packs

Features: Mode-specific wheel config, streak preservation alerts, persistent selection, progress tracking, state validation. Managed by `GameModeManager`.

### Analytics

**PostHog** (`AnalyticsManager`): Opt-in by default, 57+ events, consent toggle, data clearing on opt-out.

**Event Categories**: Lifecycle (2), Onboarding (8), What's New (3), Settings (8), Phobia Filters (3), Game Modes (4), Gameplay (4), Progress (1), Store Browsing (3), Cart (8), Discounts (3), Purchases (4), Support (3)

**Key Funnels**: Store→Cart→Checkout→Purchase, Cart abandonment, Discount effectiveness

**Privacy**: Never collects usernames, question content, phobia terms, leaderboard data. Only usage patterns, conversion metrics, aggregate stats.

### Personalization & Utils

**UserManager**: Persistent username, onboarding, personalized messaging, fallback to "Player"

**AppIconManager**: 6 icon variants (Correct, Regular Pose, Happy Smirk, Incorrect, Leaderboard, New High Score), visual picker in settings

**FizColors**: Hex-based, light/dark mode, 8 colors (fizBackground, fizOrange, fizCream, fizBrown, fizTeal, fizGray, fizDarkGold, fizLightGold, fizBackgroundSecondary)

**ButtonStyles**: iOS 26 glass w/ iOS 18 fallback, `glassButtonStyle()`, `answerButtonStyle()`, `prominentActionButton()`, scale animations

**HapticManager**: Impact/notification feedback, `correctAnswerEffect()` celebration, integrated with `HapticSettingsManager`

**AccessibilityHelpers**: VoiceOver, reduce motion, adaptive durations

### UI/UX Patterns

Fixed layout (content changes, not UI), immediate feedback (haptics/animations), accessibility first, gradient backgrounds, auto-clearing interfaces, pull-to-spin, grammar-aware text, iOS 26 w/ fallbacks, Dynamic Type adaptive modals

### Development Notes

**Database**: Reorganized categories, timestamped backups
**Previews**: All major views, `.modelContainer(for: LeaderboardEntry.self, inMemory: true)`
**Performance**: Single JSON load at launch, in-memory filtering, persistent state, fixed-height containers
**Persistence**: UserDefaults (username, difficulty, streak), SwiftData (achievements)

### File Organization
```
Fiz/
├── FizApp.swift, ContentView.swift, Configuration.storekit
├── CLAUDE.md, ANALYTICS_LAUNCH_SUMMARY.md
├── Models/TriviaModels.swift
├── ViewModels/GameViewModel.swift
├── Views/ - CategoryWheelView, QuestionContentView, ResultContentView,
│   QuestionModalView, LeaderboardView, SettingsView, StoreView, CartView,
│   OnboardingView, Settings/*
├── Utils/ - FizColors, ButtonStyles, HapticManager, AnalyticsManager,
│   StoreManager, AccessibilityHelpers
└── Resources/ - questions.json, expansion_*.json (5 packs)
```

### Recent Updates

**Analytics** (Jan 19, 2026): Opt-in by default, 57+ events, store/cart/checkout funnel tracking, cart abandonment, discount analytics

**Expansion Packs**: StoreKit 2 IAP, store UI, cart system, Single Topic Mode, 5 launch packs (HP, Pokémon, 80s, Disney, The Office), 10% free previews

**Features**: Multi-Category mode consolidation, 6 app icons, settings reorganization, iOS 26 glass buttons, progress tracking, protocol-based subcategories

**Managers**: ExpansionPackManager, StoreManager, CartManager, DiscountCodeManager, GameModeManager (replaced SingleCategoryModeManager), AnalyticsManager, AnsweredQuestionsManager, HapticSettingsManager, AppIconManager

**Removed**: MainMenuView, QuestionView, ResultView, Random Trivia category, SingleCategoryModeManager, CategorySelectionSettingsView

---

## Expansion Pack System

**Principles**: Bundled JSON, optional install/uninstall, 10% free preview, Family Sharing, cross-category

**Data**: `ExpansionPack` model with packId, name, subtopics[], questions, pricing. `ExpansionPackManager` loads `expansion_*.json`, tracks purchased/installed IDs. `StoreManager` handles StoreKit 2 IAP, transactions, Family Sharing.

**Pack JSON**: packId, packName, packDescription, subtopics[], questionCount, freePreviewCount, difficulty{}, price, icon, freePreviewQuestions[], paidQuestions[]

**Questions**: Base fields + `topic` (packId), `subtopic`. Questions span main categories.

**User Flow**: Store→Browse→Purchase→Auto-install→Single Topic Mode. Manage: uninstall/reinstall (no repurchase), restore purchases

**Integration**: GameViewModel merges base+free+installed questions at launch. CategoryWheelView switches wheel config by mode. GameModeManager validates topic installed, persists selection.

**StoreKit**: Configuration.storekit (5 products, Family Sharing). Production: match product IDs, pricing tiers, localization

---

## Adding New Expansion Packs

**Command**: `Let's create a new expansion pack: [Name] with [X] questions`

**Steps**:
1. **Design**: Define packId (`com.fiz.pack.[name]`), 6-8 subtopics, pricing ($1.99-$4.99), icon, target count (200-500)
2. **Create JSON**: `expansion_[name].json` with metadata (packId, name, description, subtopics[], counts, difficulty{}, price, icon, questions arrays)
3. **Generate Questions**: Batches of 50-100, distribute across subtopics, ID format `[prefix]_[number]`, add topic/subtopic fields, 10% free preview
4. **Content Rules**: Family-friendly, factual, varied, specific, NO snakes/spiders
5. **StoreKit**: Update Configuration.storekit (product ID, price, Family Sharing, localization)
6. **Test**: Validate JSON, launch app, test store/purchase/install/play/uninstall flow
7. **Commit**: `git add`, descriptive commit message, update CLAUDE.md expansion pack list

**Pricing**: 200-300q=$1.99, 300-400q=$2.99, 400-500q=$3.99, 500+q=$4.99

**Future Ideas**: Star Wars, Marvel, Lord of the Rings, Friends, Soccer, 90s Nostalgia

---

## Database Expansion

**Status**: 2,107 total (Entertainment: 307, All others: 300 each)

**Commands**: `Expand database by [X] per category` OR `Expand to [X] per category`

**Workflow**:
1. **Analyze**: Count per category/subcategory, calculate needed, create todo list
2. **Backup**: `cp questions.json questions_backup_$(date +%Y%m%d_%H%M%S).json`
3. **Duplicate Check**: Check existing DB, remove any found
4. **Generate** (per category): Review existing, create batches (10-50), distribute across subcategories, follow ID system, emphasize hard/medium, commit after each
5. **Content Rules**: Family-friendly, non-controversial, factual, varied, specific, NO snakes/spiders
6. **Incremental Check**: Check new questions vs DB after each category, fix duplicates immediately
7. **Final Verify**: Full DB duplicate check (exact 100%, semantic >90%, essential 70-90%), remove dupes (keep lower ID), generate replacements
8. **Document**: Update CLAUDE.md counts, create summary, commit & push

**Scripts**: `analyze_duplicates.py`, `remove_duplicates.py`, `add_[category]_to_[target].py`, `verify_replacements.py`

**Pitfalls**: Read existing first, check incrementally, commit per category, catch semantic dupes, don't rush replacements
