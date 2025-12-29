# Topic Assignments for Database Migration
**Date**: 2025-12-28
**Status**: FINALIZED

---

## Topic Assignment Rules

**Topics are ONLY assigned to questions that:**
1. Come from very specific, sellable content (e.g., Harry Potter, Pokémon)
2. Were previously specific subcategories that are now consolidated
3. Represent potential future expansion packs

**Topics are NOT assigned to:**
- Broad categories (Science > Chemistry, History > Ancient History, etc.)
- Questions moved between categories without specific content focus
- Generic questions within subcategories

---

## Questions That GET Topics

### **Entertainment Category**

#### Animation Subcategory
- **Pixar (34 questions)** → topic: "Pixar"
  - IDs: ent_223 - ent_256

#### Sci-Fi/Fantasy Subcategory
- **Star Wars (38 questions)** → topic: "Star Wars"
  - IDs: ent_257 - ent_294
- **Film (1 question)** → NO TOPIC
  - ID: ent_160 (cinematographer question)

#### Action/Adventure Subcategory
- **Marvel (53 questions)** → topic: "Marvel"
  - IDs: See analyze_superheroes.py output
- **DC (36 questions)** → topic: "DC"
  - IDs: See analyze_superheroes.py output

#### Drama/Comedy Subcategory
- **The Office (31 questions)** → topic: "The Office"
  - IDs: ent_295 - ent_325

---

### **Literature Category**

#### Fantasy Literature Subcategory
- **Harry Potter (43 questions)** → topic: "Harry Potter"
  - Old IDs: ent_001 - ent_043
  - New IDs: lit_001 - lit_043

---

### **Music Category**

#### Film & TV Subcategory
- **Film Composers (21 questions)** → NO TOPIC
  - Old IDs: ent_139 - ent_159
  - New IDs: mus_001 - mus_021
  - NOTE: Just moved to new subcategory, no topic assigned

---

### **Technology Category**

#### Video Games Subcategory
- **Pokémon (42 questions)** → topic: "Pokémon"
  - Old IDs: ent_181 - ent_222
  - New IDs: tec_001 - tec_042

---

### **Sports Category**

All old sport-specific subcategories become topics under broader subcategories:

#### Team Sports Subcategory
- **American Football (31 questions)** → topic: "American Football"
  - IDs: spt_001 - spt_031
- **Baseball (28 questions)** → topic: "Baseball"
  - IDs: spt_032 - spt_059
- **Basketball (43 questions)** → topic: "Basketball"
  - IDs: spt_060 - spt_102
- **Hockey (31 questions)** → topic: "Hockey"
  - IDs: spt_103 - spt_133
- **Soccer (26 questions)** → topic: "Soccer"
  - IDs: spt_134 - spt_159

#### Individual Sports Subcategory
- **Tennis (27 questions)** → topic: "Tennis"
  - IDs: spt_160 - spt_186
- **Golf (28 questions)** → topic: "Golf"
  - IDs: spt_187 - spt_214

#### International Competition Subcategory
- **Olympics (26 questions)** → topic: "Olympics"
  - IDs: spt_215 - spt_240

---

## Questions That DO NOT Get Topics

### **Geography Category** (NEW)
- All 46 questions → NO TOPICS
  - Old IDs: ear_XXX (scattered)
  - New IDs: geo_001 - geo_046
  - Distributed across: World Geography, U.S. Geography, Maps & Borders

### **Nature Category** (renamed from Earth)
- All 230 questions → NO TOPICS
  - Old IDs: ear_XXX
  - New IDs: nat_001 - nat_230
  - Subcategories: Animals & Wildlife, Weather, Plants & Flowers, Trees

### **Science Category**
- All 278 questions → NO TOPICS
  - Subcategories: Chemistry, Physics, Biology, Astronomy
  - These are broad scientific fields, not specific sellable content

### **History Category**
- All 268 questions → NO TOPICS
  - Subcategories: Ancient History, Medieval History, Modern History, Church History
  - These are broad historical periods, not specific topics

### **Bible Category**
- All 266 questions → NO TOPICS
  - Subcategories: Old Testament, New Testament, Bible Trivia, Biblical History, Biblical Theology, Biblical Languages
  - These are broad categories of biblical content

### **Food Category**
- All 278 questions → NO TOPICS
  - Subcategories: Ingredients, Dishes, Famous Chefs/Restaurants, Baking, Cooking Techniques, Cuisines, Beverages, Desserts, Food History, Sauces & Condiments
  - These are broad food categories, not specific topics

---

## Art Category (NEW - Empty)
- 0 questions
- Will not have topics until specific content is added

---

## Summary Statistics

### Questions WITH Topics: 357 total

| Topic | Category | Subcategory | Count |
|-------|----------|-------------|-------|
| Pixar | Entertainment | Animation | 34 |
| Star Wars | Entertainment | Sci-Fi/Fantasy | 38 |
| Marvel | Entertainment | Action/Adventure | 53 |
| DC | Entertainment | Action/Adventure | 36 |
| The Office | Entertainment | Drama/Comedy | 31 |
| Harry Potter | Literature | Fantasy Literature | 43 |
| Pokémon | Technology | Video Games | 42 |
| American Football | Sports | Team Sports | 31 |
| Baseball | Sports | Team Sports | 28 |
| Basketball | Sports | Team Sports | 43 |
| Hockey | Sports | Team Sports | 31 |
| Soccer | Sports | Team Sports | 26 |
| Tennis | Sports | Individual Sports | 27 |
| Golf | Sports | Individual Sports | 28 |
| Olympics | Sports | International Competition | 26 |

### Questions WITHOUT Topics: 1,548 total

- Geography: 46 questions
- Nature: 230 questions
- Music (Film Composers): 21 questions
- Science: 278 questions
- History: 268 questions
- Bible: 266 questions
- Food: 278 questions
- Entertainment (1 film question): 1 question
- Art: 0 questions

### Grand Total: 1,905 questions

---

## Implementation Notes

1. **Optional Fields**: `topic` and `subtopic` fields must be optional in TriviaQuestion model
2. **Null Handling**: Questions without topics should have `null` or omitted `topic` field in JSON
3. **Future Expansion**: Topics are designed for:
   - Single-topic game mode (e.g., play only Pokémon questions)
   - Expansion pack store (e.g., purchase "Pokémon Expansion Pack")
   - More granular progress tracking
4. **Subtopics**: Reserved for future use, all questions will have `null` or omitted subtopic initially

---

## Next Step: Database Migration Script

Create script that:
1. Adds optional `topic` and `subtopic` fields to TriviaQuestion model
2. Migrates questions with ID changes
3. Assigns topics per table above
4. Leaves topic as null/omitted for questions without topics
5. Validates all changes
