# Duplicate Questions Analysis Report
**Date:** November 12, 2025
**Database:** `/home/user/fiztrivia/Fiz/Resources/questions.json`
**Total Questions:** 1,511
**New Questions Analyzed:** 118

---

## Executive Summary

Found **28 duplicate questions** across **32 duplicate groups** (some questions appear in multiple groups).

- **8 Exact Duplicates** - Identical question text
- **13 Semantic Duplicates** - Very similar wording (85%+ similarity), same answer
- **11 Essential Duplicates** - Different wording (70-85% similarity), same knowledge/answer

**Recommendation:** Remove 28 questions, reducing database from **1,511 → 1,483 questions** (1.9% reduction)

---

## Breakdown by Category

### Sports (8 duplicates to remove)
- `spt_190` - Olympic rings colors (duplicate of spt_106)
- `spt_192` - Hat trick definition (duplicate of spt_041 AND spt_052)
- `spt_194` - Players on field (duplicate of spt_171)
- `spt_196` - Birdie in golf (duplicate of spt_017)
- `spt_198` - Tennis "love" score (duplicate of spt_030)
- `spt_200` - Home run definition (duplicate of spt_185, spt_029, AND spt_135)
- `spt_201` - Barry Bonds record (duplicate of spt_187)

### Bible (5 duplicates to remove)
- `bib_190` - Hebrew "Shalom" (duplicate of bib_173)
- `bib_196` - OT book count (duplicate of bib_013)
- `bib_197` - First book of Bible (duplicate of bib_009)
- `bib_201` - Number of disciples (duplicate of bib_008)
- `bib_203` - Jonah and fish (duplicate of bib_012)

### History (8 duplicates to remove)
- `his_175` - Great Schism year (duplicate of his_145)
- `his_189` - Genghis Khan (duplicate of his_102)
- `his_190` - Byzantine capital (duplicate of his_022)
- `his_193` - Alexandria lighthouse (duplicate of his_005)
- `his_195` - First Chinese emperor (duplicate of his_038)
- `his_196` - Machu Picchu builder (duplicate of his_014 AND his_169)
- `his_198` - Berlin Wall fall (duplicate of his_004)
- `his_200` - Titanic sinking year (duplicate of his_023)

### Science (5 duplicates to remove)
- `sci_179` - Shortest day planet (duplicate of sci_063)
- `sci_185` - Electric charge unit (duplicate of sci_121)
- `sci_202` - Mitochondria powerhouse (duplicate of sci_007)
- `sci_203` - Photosynthesis definition (duplicate of sci_141)
- `sci_204` - Nocturnal animals (duplicate of sci_082)

### Food (3 duplicates to remove)
- `foo_176` - Main ingredient in pesto (duplicate of foo_046)
- `foo_185` - Éclair pastry (duplicate of foo_101)
- `foo_192` - Bread rising ingredient (duplicate of foo_100)

---

## Detailed Findings

### EXACT DUPLICATES (8 groups)

#### Group #1: Tennis "Love" Score
- **KEEP:** `spt_030` (Sports → Tennis)
- **REMOVE:** `spt_198` (Sports → Tennis)
- **Question:** "What is a score of zero called in tennis?"
- **Answer:** Love

#### Group #2: Hat Trick Definition
- **KEEP:** `spt_052` (Sports → Soccer)
- **REMOVE:** `spt_192` (Sports → Hockey)
- **Question:** "What is it called when a player scores three goals in one game?"
- **Answer:** Hat trick
- **Note:** Same question used for two different sports

#### Group #3: Home Run - Out of Field
- **KEEP:** `spt_185` (Sports → Baseball)
- **REMOVE:** `spt_200` (Sports → Baseball)
- **Question:** "What is it called when a batter hits the ball out of the playing field?"
- **Answer:** Home run

#### Group #4: Barry Bonds Record
- **KEEP:** `spt_187` (Sports → Baseball)
- **REMOVE:** `spt_201` (Sports → Baseball)
- **Question:** "Who holds the record for most career home runs in MLB?"
- **Answer:** Barry Bonds

#### Group #5: Jonah and the Fish
- **KEEP:** `bib_012` (Bible → Old Testament)
- **REMOVE:** `bib_203` (Bible → Old Testament)
- **Question:** "Who was swallowed by a great fish?"
- **Answer:** Jonah

#### Group #6: Hebrew "Shalom"
- **KEEP:** `bib_173` (Bible → Biblical Languages)
- **REMOVE:** `bib_190` (Bible → Biblical Languages)
- **Question:** "What does the Hebrew word 'Shalom' mean?"
- **Answer:** Peace

#### Group #7: Byzantine Capital
- **KEEP:** `his_022` (History → Ancient History)
- **REMOVE:** `his_190` (History → Medieval History)
- **Question:** "What was the capital of the Byzantine Empire?"
- **Answer:** Constantinople

#### Group #8: Titanic Sinking
- **KEEP:** `his_023` (History → Modern History)
- **REMOVE:** `his_200` (History → Modern History)
- **Question:** "What year did the Titanic sink?"
- **Answer:** 1912

---

### SEMANTIC DUPLICATES (13 groups)

#### Group #9: Hat Trick Term (88.2% similar)
- **KEEP:** `spt_041` (Sports → Hockey)
- **REMOVE:** `spt_192` (Sports → Hockey)
- Q1: "What is the term for when a player scores three goals in one game?"
- Q2: "What is it called when a player scores three goals in one game?"

#### Group #10: Players on Field (85.5% similar)
- **KEEP:** `spt_171` (Sports → American Football)
- **REMOVE:** `spt_194` (Sports → Soccer)
- Q1: "What is the maximum number of players allowed on the field for one team at a time?"
- Q2: "What is the maximum number of players on the field for one team during a match?"
- **Note:** Both answer "11" but for different sports

#### Group #11: Old Testament Books (87.6% similar)
- **KEEP:** `bib_013` (Bible → Bible Trivia)
- **REMOVE:** `bib_196` (Bible → Biblical Theology)
- Q1: "How many books are in the Old Testament?"
- Q2: "How many books are in the Protestant Old Testament?"

#### Group #12: First Book of Bible (95.8% similar)
- **KEEP:** `bib_009` (Bible → Old Testament)
- **REMOVE:** `bib_197` (Bible → Biblical Theology)
- Q1: "What was the first book of the Bible?"
- Q2: "What is the first book of the Bible?"

#### Group #13: Number of Disciples (91.2% similar)
- **KEEP:** `bib_008` (Bible → New Testament)
- **REMOVE:** `bib_201` (Bible → New Testament)
- Q1: "How many disciples did Jesus have?"
- Q2: "How many disciples did Jesus choose?"

#### Group #14: First Chinese Emperor (89.5% similar)
- **KEEP:** `his_038` (History → Ancient History)
- **REMOVE:** `his_195` (History → Ancient History)
- Q1: "Who was the first emperor of China?"
- Q2: "Who was the first emperor of unified China?"

#### Group #15: Machu Picchu Builder #1 (90.0% similar)
- **KEEP:** `his_014` (History → Ancient History)
- **REMOVE:** `his_196` (History → Ancient History)
- Q1: "What civilization built Machu Picchu?"
- Q2: "What ancient civilization built Machu Picchu?"

#### Group #16: Machu Picchu Builder #2 (94.4% similar)
- **KEEP:** `his_169` (History → Ancient History)
- **REMOVE:** `his_196` (History → Ancient History)
- Q1: "Which ancient civilization built Machu Picchu?"
- Q2: "What ancient civilization built Machu Picchu?"
- **Note:** `his_196` appears in TWO duplicate groups

#### Group #17: Berlin Wall Fall (88.9% similar)
- **KEEP:** `his_004` (History → Modern History)
- **REMOVE:** `his_198` (History → Modern History)
- Q1: "When did the Berlin Wall fall?"
- Q2: "What year did the Berlin Wall fall?"

#### Group #18: Shortest Day Planet (94.3% similar)
- **KEEP:** `sci_063` (Science → Astronomy)
- **REMOVE:** `sci_179` (Science → Astronomy)
- Q1: "Which planet has the shortest day in the Solar System?"
- Q2: "Which planet has the shortest day in our solar system?"

#### Group #19: Electric Charge Unit (96.2% similar)
- **KEEP:** `sci_121` (Science → Physics)
- **REMOVE:** `sci_185` (Science → Physics)
- Q1: "What is the basic unit of electric charge?"
- Q2: "What is the SI unit of electric charge?"

#### Group #20: Mitochondria Powerhouse (87.2% similar)
- **KEEP:** `sci_007` (Science → Biology)
- **REMOVE:** `sci_202` (Science → Biology)
- Q1: "What is the powerhouse of the cell?"
- Q2: "What is the powerhouse organelle of the cell?"

#### Group #21: Éclair Pastry (91.9% similar)
- **KEEP:** `foo_101` (Food → Baking)
- **REMOVE:** `foo_185` (Food → Desserts)
- Q1: "What French pastry is made with choux dough and filled with cream?"
- Q2: "What French pastry is made of choux dough filled with cream?"

---

### ESSENTIAL DUPLICATES (11 groups)

#### Group #22: Olympic Rings Colors (82.1% similar)
- **KEEP:** `spt_106` (Sports → Olympics)
- **REMOVE:** `spt_190` (Sports → Olympics)
- Q1: "What are the colors of the Olympic rings?"
- Q2: "What five colors are the Olympic rings?"

#### Group #23: Golf Birdie (70.2% similar)
- **KEEP:** `spt_017` (Sports → Golf)
- **REMOVE:** `spt_196` (Sports → Golf)
- Q1: "What is one stroke under par called in golf?"
- Q2: "What is the term for one stroke under par on a hole?"

#### Group #24: Home Run - Over Fence (83.1% similar)
- **KEEP:** `spt_029` (Sports → Baseball)
- **REMOVE:** `spt_200` (Sports → Baseball)
- Q1: "What is it called when a batter hits the ball over the fence?"
- Q2: "What is it called when a batter hits the ball out of the playing field?"
- **Note:** `spt_200` appears in MULTIPLE duplicate groups

#### Group #25: Home Run - All Bases (70.2% similar)
- **KEEP:** `spt_135` (Sports → Baseball)
- **REMOVE:** `spt_200` (Sports → Baseball)
- Q1: "What is it called when you hit the ball and run all the bases?"
- Q2: "What is it called when a batter hits the ball out of the playing field?"
- **Note:** `spt_200` appears in MULTIPLE duplicate groups

#### Group #26: Great Schism Year (78.4% similar)
- **KEEP:** `his_145` (History → Church History)
- **REMOVE:** `his_175` (History → Church History)
- Q1: "In what year did the Great Schism occur, splitting the Eastern and Western churches?"
- Q2: "In what year did the Great Schism split the Christian church into Eastern and Western branches?"

#### Group #27: Genghis Khan (83.5% similar)
- **KEEP:** `his_102` (History → Medieval History)
- **REMOVE:** `his_189` (History → Medieval History)
- Q1: "Who led the Mongol Empire to its greatest extent?"
- Q2: "Who led the Mongol Empire during its greatest expansion?"

#### Group #28: Alexandria Lighthouse (74.5% similar)
- **KEEP:** `his_005` (History → Ancient History)
- **REMOVE:** `his_193` (History → Ancient History)
- Q1: "Which wonder of the ancient world was located in Alexandria?"
- Q2: "What ancient wonder was located in Alexandria, Egypt?"

#### Group #29: Photosynthesis (78.3% similar)
- **KEEP:** `sci_141` (Science → Biology)
- **REMOVE:** `sci_203` (Science → Biology)
- Q1: "What is the process by which plants make food?"
- Q2: "What is the process by which plants make their own food using sunlight?"

#### Group #30: Nocturnal Animals (81.2% similar)
- **KEEP:** `sci_082` (Science → Biology)
- **REMOVE:** `sci_204` (Science → Biology)
- Q1: "What do we call animals that are active at night?"
- Q2: "What is the term for animals that are active at night?"

#### Group #31: Pesto Ingredient (80.0% similar)
- **KEEP:** `foo_046` (Food → Ingredients)
- **REMOVE:** `foo_176` (Food → Sauces & Condiments)
- Q1: "What is the main ingredient in pesto?"
- Q2: "What is the main ingredient in traditional pesto sauce?"

#### Group #32: Bread Rising (83.1% similar)
- **KEEP:** `foo_100` (Food → Baking)
- **REMOVE:** `foo_192` (Food → Baking)
- Q1: "What leavening agent causes bread to rise?"
- Q2: "What ingredient causes bread to rise?"

---

## Questions Appearing in Multiple Duplicate Groups

### `spt_192` (3 groups)
Appears in Groups #2, #9 - Hat trick definition

### `spt_200` (4 groups)
Appears in Groups #3, #24, #25 - Home run definitions
**Most duplicated question in the database**

### `his_190` (2 groups)
Appears in Groups #7 - Byzantine capital

### `his_196` (3 groups)
Appears in Groups #15, #16 - Machu Picchu builder

### `foo_176` (2 groups)
Appears in Groups #31 - Pesto ingredient

---

## Complete List of Question IDs to Remove

```
bib_190, bib_196, bib_197, bib_201, bib_203
foo_176, foo_185, foo_192
his_175, his_189, his_190, his_193, his_195, his_196, his_198, his_200
sci_179, sci_185, sci_202, sci_203, sci_204
spt_190, spt_192, spt_194, spt_196, spt_198, spt_200, spt_201
```

**Total:** 28 questions

---

## Recommendations

1. **Immediate Action:** Remove all 28 duplicate questions listed above
2. **Quality Assurance:** All duplicates were from the newly added question ranges, suggesting the duplicate issue was introduced during the recent expansion
3. **Prevention:** Implement duplicate checking before adding new questions in the future
4. **Special Cases:**
   - `spt_200` appears in 4 duplicate groups - highest priority removal
   - `his_196` and `spt_192` appear in 3 groups each
   - Consider reviewing question generation process to prevent future duplicates

---

## Files Generated

- `/home/user/fiztrivia/duplicate_analysis_report.json` - Machine-readable detailed report
- `/home/user/fiztrivia/DUPLICATE_ANALYSIS_SUMMARY.md` - This human-readable summary
- `/home/user/fiztrivia/analyze_duplicates.py` - Initial analysis script
- `/home/user/fiztrivia/refined_duplicates_analysis.py` - Final analysis script with answer validation
