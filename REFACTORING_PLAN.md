# Question Database Refactoring Plan
## Major Update: 7 Categories → 12 Categories + Topics/Subtopics

**Date**: 2025-12-28
**Total Current Questions**: 1,905
**Current Categories**: 7
**Target Categories**: 12

---

## Executive Summary

This refactoring involves:
1. **Expanding from 7 to 12 categories** (5 new categories)
2. **Renaming**: "Earth" → "Nature"
3. **Promoting**: Geography from subcategory to full category
4. **Adding structure**: Every question gets `topic` and `subtopic` fields
5. **Reorganizing**: Broader subcategories with granular topics/subtopics
6. **Migrating**: ~500+ questions will move to different categories
7. **Renaming IDs**: All affected questions need new ID prefixes

---

## New Category Structure Overview

| # | Category | Subcategories | Status |
|---|----------|---------------|--------|
| 1 | Entertainment (Movies & TV Shows) | 4 | Modified from existing |
| 2 | Literature | 6 | **NEW** |
| 3 | Music | 5 | **NEW** |
| 4 | Technology | 5 | **NEW** |
| 5 | Art | 5 | **NEW** |
| 6 | Geography | 5 | **NEW** (promoted) |
| 7 | Sports | 6 | Modified from existing |
| 8 | Science | 4 | Stays same structure |
| 9 | Nature | 5 | Renamed from "Earth" |
| 10 | History | 4 | Stays same |
| 11 | Bible | 6 | Stays same |
| 12 | Food | 10 | Stays same |

---

## Phase 1: Question Migration Mapping

### 1.1 ENTERTAINMENT → Multiple Destinations

**Current Entertainment (299 questions)**

#### **Staying in Entertainment (Movies & TV Shows)**
- **Pixar (34 questions)** → Entertainment > Animation [topic: "Pixar"]
- **Star Wars (38 questions)** → Entertainment > Sci-Fi/Fantasy [topic: "Star Wars"]
- **Superheroes (89 questions)** → Entertainment > Sci-Fi/Fantasy OR Action/Adventure [topic: "Marvel", "DC", "General Superheroes"] - *needs analysis*
- **The Office (31 questions)** → Entertainment > Drama/Comedy [topic: "The Office"]
- **Film (1 question)** → Entertainment > *TBD based on question content*

**Total staying in Entertainment: ~193 questions**

#### **Moving to LITERATURE**
- **Harry Potter (43 questions)** → Literature > Fantasy Literature [topic: "Harry Potter"]

**Total moving to Literature: 43 questions**

#### **Moving to MUSIC**
- **Film Score Composers (21 questions)** → Music > Music in Film & TV [topic: "Film Composers"]

**Total moving to Music: 21 questions**

#### **Needs Analysis**
- **Pokémon (42 questions)** → Could be:
  - Entertainment > Animation [topic: "Pokémon"] (if anime-focused)
  - Technology > Video Games [topic: "Pokémon"] (if game-focused)
  - **Action needed**: Read sample questions to determine best fit

**Total needing analysis: 42 questions**

---

### 1.2 EARTH → NATURE + GEOGRAPHY

**Current Earth (276 questions)**

#### **Moving to NATURE**
- **Animals (103 questions)** → Nature > Animals & Wildlife
- **Weather (49 questions)** → Nature > Weather
- **Plants (40 questions)** → Nature > Plants & Flowers
- **Trees (38 questions)** → Nature > Trees

**Total moving to Nature: 230 questions**

#### **Moving to GEOGRAPHY**
- **Geography (46 questions)** → Geography > *subcategory TBD* (U.S. Geography, World Geography, etc.)
  - **Action needed**: Analyze questions to distribute across 5 geography subcategories

**Total moving to Geography: 46 questions**

---

### 1.3 SPORTS → Reorganized SPORTS

**Current Sports (240 questions, 8 subcategories)**

#### **New Organization by Subcategory**

**Team Sports:**
- American Football (31 questions) → Sports > Team Sports [topic: "American Football"]
- Baseball (28 questions) → Sports > Team Sports [topic: "Baseball"]
- Basketball (43 questions) → Sports > Team Sports [topic: "Basketball"]
- Hockey (31 questions) → Sports > Team Sports [topic: "Hockey"]
- Soccer (26 questions) → Sports > Team Sports [topic: "Soccer"]

**Individual Sports:**
- Tennis (27 questions) → Sports > Individual Sports [topic: "Tennis"]
- Golf (28 questions) → Sports > Individual Sports [topic: "Golf"]

**International Competition:**
- Olympics (26 questions) → Sports > International Competition [topic: "Olympics"]

**Notes:**
- All 240 questions stay in Sports category
- Subcategories consolidate from 8 → 6
- Topics preserve original sport specificity
- New subcategories needed: Extreme & Action Sports, Sports History & Records, Athletes & Biography (0 questions initially)

---

### 1.4 SCIENCE → Stays Same

**Current Science (278 questions, 4 subcategories)**

- Chemistry (71 questions) → Science > Chemistry
- Physics (73 questions) → Science > Physics
- Biology (70 questions) → Science > Biology
- Astronomy (64 questions) → Science > Astronomy

**No changes needed** - structure already matches new plan

---

### 1.5 HISTORY → Stays Same

**Current History (268 questions, 4 subcategories)**

- Ancient History (72 questions) → History > Ancient History
- Medieval History (61 questions) → History > Medieval History
- Modern History (79 questions) → History > Modern History
- Church History (56 questions) → History > Church History

**No changes needed** - structure already matches new plan

---

### 1.6 BIBLE → Stays Same

**Current Bible (266 questions, 6 subcategories)**

- Old Testament (131 questions) → Bible > Old Testament
- New Testament (81 questions) → Bible > New Testament
- Bible Trivia (3 questions) → Bible > Bible Trivia
- Biblical History (20 questions) → Bible > Biblical History
- Biblical Theology (18 questions) → Bible > Biblical Theology
- Biblical Languages (13 questions) → Bible > Bible Languages

**No changes needed** - structure already matches new plan

---

### 1.7 FOOD → Stays Same

**Current Food (278 questions, 10 subcategories)**

All subcategories match exactly:
- Ingredients (62 questions) → Food > Ingredients
- Dishes (51 questions) → Food > Dishes
- Famous Chefs/Restaurants (42 questions) → Food > Famous Chefs/Restaurants
- Baking (23 questions) → Food > Baking
- Cooking Techniques (22 questions) → Food > Cooking Techniques
- Cuisines (21 questions) → Food > Cuisines
- Beverages (21 questions) → Food > Beverages
- Desserts (18 questions) → Food > Desserts
- Food History (10 questions) → Food > Food History
- Sauces & Condiments (8 questions) → Food > Sauces & Condiments

**No changes needed** - structure already matches new plan

---

## Phase 2: ID Renaming Strategy

### 2.1 Category Prefix Mapping

| Category | Old Prefix | New Prefix | Affected Questions |
|----------|------------|------------|-------------------|
| Entertainment | `ent_` | `ent_` | ~193 staying |
| Literature | N/A | `lit_` | 43 new (from ent) |
| Music | N/A | `mus_` | 21 new (from ent) |
| Technology | N/A | `tec_` | 42 new? (from ent - Pokémon) |
| Art | N/A | `art_` | 0 (no existing questions) |
| Geography | N/A | `geo_` | 46 new (from ear) |
| Sports | `spt_` | `spt_` | 240 staying |
| Science | `sci_` | `sci_` | 278 staying |
| Nature | `ear_` | `nat_` | **230 (ALL need renaming)** |
| History | `his_` | `his_` | 268 staying |
| Bible | `bib_` | `bib_` | 266 staying |
| Food | `foo_` | `foo_` | 278 staying |

### 2.2 Questions Requiring New IDs

**Total questions needing ID changes: ~382 questions minimum**

1. **Earth → Nature (230 questions)**: `ear_XXX` → `nat_XXX`
2. **Earth → Geography (46 questions)**: `ear_XXX` → `geo_XXX`
3. **Entertainment → Literature (43 questions)**: `ent_XXX` → `lit_XXX`
4. **Entertainment → Music (21 questions)**: `ent_XXX` → `mus_XXX`
5. **Entertainment → Technology (42 questions?)**: `ent_XXX` → `tec_XXX`

### 2.3 ID Numbering Strategy

For new category IDs, start from `001` and assign sequentially:
- `lit_001` through `lit_043` (Harry Potter questions)
- `mus_001` through `mus_021` (Film Score Composers)
- `geo_001` through `geo_046` (Geography questions)
- `nat_001` through `nat_230` (Nature questions - Animals, Weather, Plants, Trees)
- `tec_001` through `tec_042` (Pokémon questions IF moving to Technology)

---

## Phase 3: New JSON Structure Design

### 3.1 Current Structure
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

### 3.2 New Structure
```json
{
  "id": "lit_001",
  "category": "Literature",
  "subcategory": "Fantasy Literature",
  "topic": "Harry Potter",
  "subtopic": "Characters",
  "question": "What is the name of Harry Potter's owl?",
  "options": ["Hedwig", "Errol", "Pigwidgeon", "Crookshanks"],
  "correct_answer": "Hedwig",
  "difficulty": "easy"
}
```

### 3.3 Field Definitions

- **category**: One of 12 main categories
- **subcategory**: Broader grouping (e.g., "Fantasy Literature", "Animation")
- **topic**: Specific subject within subcategory (e.g., "Harry Potter", "Pixar", "Star Wars")
- **subtopic**: Optional granular classification (e.g., "Characters", "Spells", "Locations")

### 3.4 Topic/Subtopic Strategy

**For existing questions moving to topics:**
- Current subcategory becomes the topic
- Subtopics need to be inferred/assigned based on question content

**Examples:**

| Old Subcategory | New Subcategory | Topic | Potential Subtopics |
|----------------|-----------------|-------|---------------------|
| Harry Potter | Fantasy Literature | Harry Potter | Characters, Spells, Houses, Locations, Books, Movies |
| Pixar | Animation | Pixar | Movies, Characters, Production, History |
| Film Score Composers | Music in Film & TV | Film Composers | Composers, Scores, Awards, Techniques |
| Star Wars | Sci-Fi/Fantasy | Star Wars | Characters, Planets, Ships, Movies, TV Shows |
| American Football | Team Sports | American Football | NFL, Rules, Players, Super Bowl, History |

---

## Phase 4: Detailed Migration Steps

### Step 1: Pre-Migration Analysis (CURRENT STEP)
- [x] Analyze existing database structure
- [ ] Read sample Pokémon questions to determine best category fit
- [ ] Read sample Superhero questions to determine subcategory (Sci-Fi/Fantasy vs Action/Adventure)
- [ ] Read sample Geography questions to determine subcategory distribution
- [ ] Create detailed question-by-question migration map

### Step 2: Design & Planning
- [ ] Finalize topic/subtopic assignments for all existing questions
- [ ] Create comprehensive migration spreadsheet/document
- [ ] Design new JSON database structure
- [ ] Plan database backup strategy
- [ ] Document all category/subcategory enum changes needed in Swift code

### Step 3: Database Backup
- [ ] Create timestamped backup of current `questions.json`
- [ ] Verify backup integrity
- [ ] Document backup location

### Step 4: Create Migration Scripts
- [ ] Script 1: Add `topic` and `subtopic` fields to all questions (initially empty/default)
- [ ] Script 2: Rename category "Earth" → "Nature" for applicable questions
- [ ] Script 3: Migrate Geography questions (ear → geo, update category/subcategory)
- [ ] Script 4: Migrate Literature questions (ent → lit, update category/subcategory/topic)
- [ ] Script 5: Migrate Music questions (ent → mus, update category/subcategory/topic)
- [ ] Script 6: Migrate Technology questions if applicable (ent → tec)
- [ ] Script 7: Reorganize Sports subcategories and add topics
- [ ] Script 8: Update Entertainment remaining questions with new subcategories/topics
- [ ] Script 9: Renumber all Nature questions (ear → nat)
- [ ] Script 10: Validate all migrations and verify database integrity

### Step 5: Execute Database Migration
- [ ] Run migration scripts in sequence
- [ ] Verify question counts at each step
- [ ] Check for orphaned questions
- [ ] Validate JSON structure
- [ ] Verify no duplicate IDs
- [ ] Confirm all questions have category/subcategory/topic/subtopic

### Step 6: Update Swift Code - Models
- [ ] Update `TriviaCategory` enum in `TriviaModels.swift` (7 → 12 categories)
- [ ] Add new category cases: `literature`, `music`, `technology`, `art`, `geography`
- [ ] Rename `earth` → `nature`
- [ ] Update category icons for all 12 categories
- [ ] Update category colors for all 12 categories
- [ ] Create new subcategory protocols for 5 new categories
- [ ] Update existing subcategory enums (Sports, Entertainment, Nature)
- [ ] Add `topic` and `subtopic` properties to `TriviaQuestion` model
- [ ] Update `Codable` conformance for new fields

### Step 7: Update Swift Code - ViewModels
- [ ] Update `GameViewModel.swift` to handle new categories
- [ ] Update question loading logic for new structure
- [ ] Update filtering logic to handle topics/subtopics
- [ ] Verify difficulty filtering still works
- [ ] Update single-category mode for new structure

### Step 8: Update Swift Code - Views
- [ ] Update `CategoryWheelView.swift` for 12 category wheel
- [ ] Adjust wheel layout for 12 segments instead of 7
- [ ] Update category icon positioning
- [ ] Update `GameSettingsView.swift` for new categories in single-category mode
- [ ] Update any hardcoded category references
- [ ] Update analytics events for new categories

### Step 9: Update Swift Code - Managers
- [ ] Update `SingleCategoryModeManager` for new category structure
- [ ] Update `AnsweredQuestionsManager` for topic/subtopic tracking
- [ ] Update `AnalyticsManager` for new category events
- [ ] Verify all managers handle 12 categories correctly

### Step 10: Testing & Validation
- [ ] Test question loading with new structure
- [ ] Test category wheel with 12 categories
- [ ] Test all difficulty modes
- [ ] Test single-category mode for all 12 categories
- [ ] Test topic/subtopic filtering (if applicable)
- [ ] Test answered questions tracking
- [ ] Test streak persistence
- [ ] Test leaderboard with new categories
- [ ] Verify analytics tracking

### Step 11: Documentation Updates
- [ ] Update `CLAUDE.md` with new category structure
- [ ] Update question database section
- [ ] Update ID range documentation
- [ ] Document topic/subtopic system
- [ ] Update file organization if needed
- [ ] Update database expansion workflow

### Step 12: Final Verification
- [ ] Verify total question count unchanged (1,905)
- [ ] Verify all questions have valid category/subcategory
- [ ] Verify all questions have topic/subtopic
- [ ] Verify no broken references
- [ ] Verify app builds successfully
- [ ] Run full test suite
- [ ] Test on simulator/device

### Step 13: Commit & Push
- [ ] Commit database changes
- [ ] Commit Swift code changes
- [ ] Commit documentation updates
- [ ] Push to remote branch
- [ ] Create pull request with detailed migration notes

---

## Phase 5: Questions Needing Content Analysis

Before finalizing migration paths, these questions need manual review:

### 5.1 Pokémon Questions (42 questions, IDs ent_110 - ent_151 approximately)
**Potential Destinations:**
1. Entertainment > Animation [if anime/show focused]
2. Technology > Video Games [if game focused]

**Action Required:**
- Read sample questions
- Determine primary focus (anime vs games)
- Make category decision
- Could split if clear distinction exists

### 5.2 Superheroes Questions (89 questions)
**Potential Destinations:**
1. Entertainment > Sci-Fi/Fantasy [if fantasy/powers focused]
2. Entertainment > Action/Adventure [if action focused]

**Action Required:**
- Could stay unified under Sci-Fi/Fantasy with topics: "Marvel", "DC", "General"
- Or split by topic if content suggests different subcategories
- Read sample questions to decide

### 5.3 Geography Questions (46 questions)
**Need Distribution Across:**
- U.S. Geography
- World Geography
- Flags
- Landmarks & Monuments
- Maps & Borders

**Action Required:**
- Read all 46 questions
- Classify each into one of 5 subcategories
- Create distribution map

### 5.4 Film Question (1 question, ID ent_334)
**Action Required:**
- Read the question
- Determine appropriate subcategory (Animation, Sci-Fi/Fantasy, Action/Adventure, or Drama/Comedy)

---

## Phase 6: New Empty Categories

These categories will initially have 0 questions (future expansion targets):

### 6.1 Literature (except Harry Potter)
- Fantasy Literature: 43 (Harry Potter)
- Classic Literature: 0
- Modern Fiction: 0
- Poetry: 0
- Children's Books: 0
- Authors & Biography: 0

### 6.2 Music (except Film Composers)
- Music in Film & TV: 21 (Film Composers)
- Music History & Eras: 0
- Musicians & Bands: 0
- Music Awards & Records: 0
- Instruments & Music Theory: 0

### 6.3 Technology (except possibly Pokémon)
- Video Games: 0 or 42 (Pokémon TBD)
- Computers & Software: 0
- Internet & Social Media: 0
- Tech Companies: 0
- Inventions: 0

### 6.4 Art
- Famous Painters: 0
- Art History & Movements: 0
- Sculpture: 0
- Architecture: 0
- Photography: 0

### 6.5 Geography (new distribution)
- U.S. Geography: TBD (from 46 total)
- World Geography: TBD
- Flags: TBD
- Landmarks & Monuments: TBD
- Maps & Borders: TBD

### 6.6 Sports (new subcategories)
- Team Sports: 159 (existing)
- Individual Sports: 55 (existing)
- International Competition: 26 (existing)
- Extreme & Action Sports: 0
- Sports History & Records: 0
- Athletes & Biography: 0

---

## Phase 7: Expected Final Distribution

After migration, expected question counts by category:

| Category | Questions | Status |
|----------|-----------|--------|
| Entertainment | ~193 | Modified |
| Literature | 43 | New (from ent) |
| Music | 21 | New (from ent) |
| Technology | 0-42 | New (0 or Pokémon) |
| Art | 0 | New (empty) |
| Geography | 46 | New (from ear) |
| Sports | 240 | Reorganized |
| Science | 278 | Unchanged |
| Nature | 230 | Renamed from Earth |
| History | 268 | Unchanged |
| Bible | 266 | Unchanged |
| Food | 278 | Unchanged |
| **TOTAL** | **1,905** | **Same total** |

---

## Risk Assessment & Mitigation

### High Risk Items
1. **ID Renaming**: 382+ questions need new IDs - scripting errors could break references
   - *Mitigation*: Multiple backups, careful validation, test scripts on subset first

2. **Category Migration**: Questions moving between categories could be miscategorized
   - *Mitigation*: Manual review of sample questions, validation scripts, thorough testing

3. **Topic/Subtopic Assignment**: Wrong assignments could affect future filtering
   - *Mitigation*: Clear classification rules, review samples, iterative refinement

4. **Swift Code Updates**: Missing enum updates could cause crashes
   - *Mitigation*: Compiler will catch most issues, thorough testing required

### Medium Risk Items
1. **Database Integrity**: JSON corruption during migration
   - *Mitigation*: Multiple backups, validation at each step

2. **Answered Questions Tracking**: Existing user progress could break with ID changes
   - *Mitigation*: Migration strategy for AnsweredQuestionsManager, consider ID mapping

3. **Single Category Mode**: Could break with new category structure
   - *Mitigation*: Thorough testing, update manager logic

### Low Risk Items
1. **Documentation**: Could become outdated
   - *Mitigation*: Update docs as part of migration process

2. **Analytics**: Event names might need updates
   - *Mitigation*: Review all analytics calls, update as needed

---

## Success Criteria

Migration is complete and successful when:

- [ ] All 1,905 questions present in database (no lost questions)
- [ ] All questions have valid category (one of 12)
- [ ] All questions have valid subcategory
- [ ] All questions have topic field populated
- [ ] All questions have subtopic field populated (or explicit null/empty strategy)
- [ ] No duplicate IDs in database
- [ ] All ID prefixes match their categories
- [ ] JSON structure is valid and parses correctly
- [ ] App builds without errors
- [ ] All 12 categories appear in category wheel
- [ ] Questions load correctly for all categories
- [ ] Difficulty filtering works
- [ ] Single-category mode works for all 12 categories
- [ ] Answered questions tracking works
- [ ] No crashes during normal gameplay
- [ ] Documentation updated
- [ ] All changes committed and pushed

---

## Timeline Estimate

Based on complexity and scope:

- **Analysis & Planning**: 2-3 hours (current phase)
- **Migration Script Development**: 3-4 hours
- **Database Migration Execution**: 1-2 hours
- **Swift Code Updates**: 4-6 hours
- **Testing & Debugging**: 3-4 hours
- **Documentation**: 1-2 hours
- **Total Estimated Time**: 14-21 hours

---

## Next Immediate Actions

1. ✅ Complete this planning document
2. Read sample questions from:
   - Pokémon (determine category)
   - Superheroes (determine subcategory)
   - Geography (distribute across 5 subcategories)
   - Film (1 question - determine subcategory)
3. Create detailed question-by-question migration mapping
4. Get approval on migration strategy
5. Begin script development

---

**Document Status**: Draft - Pending Question Analysis
**Next Update**: After sample question review and category decisions
