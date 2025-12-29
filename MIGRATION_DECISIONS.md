# Migration Decisions Summary
**Date**: 2025-12-28
**Status**: FINALIZED - Ready for Implementation

---

## Classification Decisions

### 1. Pokémon (42 questions)
- **Current**: Entertainment > Pokémon
- **New Destination**: Technology > Video Games
- **Topic**: "Pokémon"
- **ID Change**: `ent_181` through `ent_222` → `tec_001` through `tec_042`

### 2. Superheroes (89 questions)
- **Current**: Entertainment > Superheroes
- **New Destination**: Entertainment > Action/Adventure
- **Topics**: Will need to analyze for "Marvel", "DC", "General Superheroes"
- **ID Change**: None (staying in Entertainment)

### 3. Geography (46 questions)
- **Current**: Earth > Geography
- **New Destination**: Geography (new category)
- **Distribution**:
  - **World Geography**: 39 questions (85%)
  - **Maps & Borders**: 5 questions (11%)
  - **U.S. Geography**: 2 questions (4%)
  - **Flags**: 0 questions
  - **Landmarks & Monuments**: 0 questions
- **ID Change**: `ear_165` through `ear_310` → `geo_001` through `geo_046`

**Geography Question IDs to Migrate:**
- ear_165, ear_166, ear_169, ear_171, ear_173, ear_178, ear_180, ear_181, ear_182, ear_184
- ear_185, ear_186, ear_188, ear_189, ear_190, ear_191, ear_192, ear_193, ear_194, ear_195
- ear_196, ear_197, ear_198, ear_199, ear_200, ear_201, ear_202, ear_203, ear_204, ear_206
- ear_223, ear_225, ear_226, ear_227, ear_228, ear_230, ear_231, ear_232, ear_265, ear_284
- ear_285, ear_286, ear_287, ear_288, ear_308, ear_310

### 4. Film (1 question)
- **Current**: Entertainment > Film
- **Question**: "Which cinematographer won Academy Awards for both 'Blade Runner 2049' and 'Dune'?"
- **New Destination**: Entertainment > Sci-Fi/Fantasy
- **Topic**: "Cinematography" or "Film Production"
- **ID**: ent_160 (stays the same)

---

## Complete Entertainment Category Breakdown

**Current Entertainment (299 questions):**

### STAYING in Entertainment (193 questions total)

#### Entertainment > Animation (34 questions)
- **Pixar** (34 questions): ent_223 - ent_256
  - Topic: "Pixar"
  - IDs stay the same

#### Entertainment > Sci-Fi/Fantasy (39 questions)
- **Star Wars** (38 questions): ent_257 - ent_294
  - Topic: "Star Wars"
  - IDs stay the same
- **Film** (1 question): ent_160
  - Topic: "Cinematography"
  - ID stays the same

#### Entertainment > Action/Adventure (89 questions)
- **Superheroes** (89 questions): ent_006 - ent_094
  - Topics: Need to classify as "Marvel", "DC", or "General"
  - IDs stay the same

#### Entertainment > Drama/Comedy (31 questions)
- **The Office** (31 questions): ent_295 - ent_325
  - Topic: "The Office"
  - IDs stay the same

### LEAVING Entertainment

#### → Literature > Fantasy Literature (43 questions)
- **Harry Potter** (43 questions): ent_001 - ent_043
  - Topic: "Harry Potter"
  - **New IDs**: `lit_001` through `lit_043`

#### → Music > Music in Film & TV (21 questions)
- **Film Score Composers** (21 questions): ent_139 - ent_159
  - Topic: "Film Composers"
  - **New IDs**: `mus_001` through `mus_021`

#### → Technology > Video Games (42 questions)
- **Pokémon** (42 questions): ent_181 - ent_222
  - Topic: "Pokémon"
  - **New IDs**: `tec_001` through `tec_042`

---

## Complete Earth → Nature/Geography Split

**Current Earth (276 questions):**

### → Nature (230 questions)
All keep topic from current subcategory, IDs change from `ear_` → `nat_`

- **Animals**: 103 questions → Nature > Animals & Wildlife
- **Weather**: 49 questions → Nature > Weather
- **Plants**: 40 questions → Nature > Plants & Flowers
- **Trees**: 38 questions → Nature > Trees

**ID Changes Required**: All 230 questions (ear_001 through ear_317, excluding geography questions)

### → Geography (46 questions)
IDs change from `ear_` → `geo_`

- **World Geography**: 39 questions
- **Maps & Borders**: 5 questions
- **U.S. Geography**: 2 questions

**ID Changes Required**: All 46 questions → geo_001 through geo_046

---

## Sports Reorganization

**Current Sports (240 questions, 8 subcategories)**
**New Sports (240 questions, 6 subcategories)**

All IDs stay with `spt_` prefix, only subcategories change:

### Sports > Team Sports (159 questions)
- **American Football** (31 questions): spt_001 - spt_031
  - Topic: "American Football"
- **Baseball** (28 questions): spt_032 - spt_059
  - Topic: "Baseball"
- **Basketball** (43 questions): spt_060 - spt_102
  - Topic: "Basketball"
- **Hockey** (31 questions): spt_103 - spt_133
  - Topic: "Hockey"
- **Soccer** (26 questions): spt_134 - spt_159
  - Topic: "Soccer"

### Sports > Individual Sports (55 questions)
- **Tennis** (27 questions): spt_160 - spt_186
  - Topic: "Tennis"
- **Golf** (28 questions): spt_187 - spt_214
  - Topic: "Golf"

### Sports > International Competition (26 questions)
- **Olympics** (26 questions): spt_215 - spt_240
  - Topic: "Olympics"

### Sports > Extreme & Action Sports (0 questions)
- Empty - future expansion

### Sports > Sports History & Records (0 questions)
- Empty - future expansion

### Sports > Athletes & Biography (0 questions)
- Empty - future expansion

---

## Categories with NO Changes

These categories maintain their exact structure:

### Science (278 questions)
- Chemistry (71 questions)
- Physics (73 questions)
- Biology (70 questions)
- Astronomy (64 questions)
- IDs: `sci_001` through `sci_326`

### History (268 questions)
- Ancient History (72 questions)
- Medieval History (61 questions)
- Modern History (79 questions)
- Church History (56 questions)
- IDs: `his_001` through `his_314`

### Bible (266 questions)
- Old Testament (131 questions)
- New Testament (81 questions)
- Bible Trivia (3 questions)
- Biblical History (20 questions)
- Biblical Theology (18 questions)
- Biblical Languages (13 questions)
- IDs: `bib_001` through `bib_327`

### Food (278 questions)
- Ingredients (62 questions)
- Dishes (51 questions)
- Famous Chefs/Restaurants (42 questions)
- Baking (23 questions)
- Cooking Techniques (22 questions)
- Cuisines (21 questions)
- Beverages (21 questions)
- Desserts (18 questions)
- Food History (10 questions)
- Sauces & Condiments (8 questions)
- IDs: `foo_001` through `foo_307`

---

## New Empty Categories

Categories created with initial questions:

### Literature (43 questions)
- Fantasy Literature: 43 (Harry Potter from Entertainment)
- Classic Literature: 0
- Modern Fiction: 0
- Poetry: 0
- Children's Books: 0
- Authors & Biography: 0

### Music (21 questions)
- Music in Film & TV: 21 (Film Composers from Entertainment)
- Music History & Eras: 0
- Musicians & Bands: 0
- Music Awards & Records: 0
- Instruments & Music Theory: 0

### Technology (42 questions)
- Video Games: 42 (Pokémon from Entertainment)
- Computers & Software: 0
- Internet & Social Media: 0
- Tech Companies: 0
- Inventions: 0

### Art (0 questions)
- Famous Painters: 0
- Art History & Movements: 0
- Sculpture: 0
- Architecture: 0
- Photography: 0

---

## Summary Statistics

### Questions Requiring ID Changes: 382 total

| Migration Path | Count | Old Prefix | New Prefix |
|----------------|-------|------------|------------|
| Earth → Nature | 230 | ear_ | nat_ |
| Earth → Geography | 46 | ear_ | geo_ |
| Entertainment → Literature | 43 | ent_ | lit_ |
| Entertainment → Music | 21 | ent_ | mus_ |
| Entertainment → Technology | 42 | ent_ | tec_ |

### Questions Staying in Same Category: 1,523

| Category | Questions | Changes |
|----------|-----------|---------|
| Entertainment | 193 | Subcategory reorganization only |
| Sports | 240 | Subcategory consolidation only |
| Science | 278 | None |
| History | 268 | None |
| Bible | 266 | None |
| Food | 278 | None |

### Final Distribution Across 12 Categories

| Category | Questions | Status |
|----------|-----------|--------|
| Entertainment | 193 | Modified |
| Literature | 43 | New |
| Music | 21 | New |
| Technology | 42 | New |
| Art | 0 | New (empty) |
| Geography | 46 | New (promoted) |
| Sports | 240 | Reorganized |
| Science | 278 | Unchanged |
| Nature | 230 | Renamed from Earth |
| History | 268 | Unchanged |
| Bible | 266 | Unchanged |
| Food | 278 | Unchanged |
| **TOTAL** | **1,905** | **Same** |

---

## Next Steps for Implementation

1. ✅ Decisions finalized
2. Create migration scripts for ID changes
3. Add topic/subtopic fields to all questions
4. Execute database migration
5. Update Swift models and enums
6. Update views for 12-category wheel
7. Test and validate
8. Update documentation
9. Commit and push

---

**Status**: Ready to proceed with migration script development
