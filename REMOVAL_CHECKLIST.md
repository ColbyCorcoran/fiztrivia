# Duplicate Questions Removal Checklist

## Quick Stats
- **Total Duplicates Found:** 28 questions (across 32 duplicate groups)
- **Database Impact:** 1,511 → 1,483 questions (1.9% reduction)
- **All duplicates from newly added questions (ranges 175-209)**

---

## Questions to Remove (by Category)

### Bible (5 questions)
- [ ] `bib_190` - Hebrew "Shalom" meaning
- [ ] `bib_196` - Old Testament book count
- [ ] `bib_197` - First book of Bible
- [ ] `bib_201` - Number of disciples
- [ ] `bib_203` - Jonah and the fish

### Food (3 questions)
- [ ] `foo_176` - Pesto main ingredient
- [ ] `foo_185` - Éclair pastry
- [ ] `foo_192` - Bread rising ingredient

### History (8 questions)
- [ ] `his_175` - Great Schism year
- [ ] `his_189` - Genghis Khan
- [ ] `his_190` - Byzantine capital
- [ ] `his_193` - Alexandria lighthouse
- [ ] `his_195` - First Chinese emperor
- [ ] `his_196` - Machu Picchu builder ⚠️ (appears in 3 groups!)
- [ ] `his_198` - Berlin Wall fall
- [ ] `his_200` - Titanic sinking

### Science (5 questions)
- [ ] `sci_179` - Shortest day planet
- [ ] `sci_185` - Electric charge unit
- [ ] `sci_202` - Mitochondria powerhouse
- [ ] `sci_203` - Photosynthesis process
- [ ] `sci_204` - Nocturnal animals

### Sports (7 questions)
- [ ] `spt_190` - Olympic rings colors
- [ ] `spt_192` - Hat trick definition ⚠️ (appears in 3 groups!)
- [ ] `spt_194` - Players on field
- [ ] `spt_196` - Golf birdie
- [ ] `spt_198` - Tennis "love" score
- [ ] `spt_200` - Home run definition ⚠️⚠️ (appears in 4 groups! HIGHEST PRIORITY)
- [ ] `spt_201` - Barry Bonds record

---

## Priority Removals (Worst Offenders)

### 🔴 CRITICAL: `spt_200`
- Appears in **4 duplicate groups**
- Question: "What is it called when a batter hits the ball out of the playing field?"
- Duplicates: `spt_185`, `spt_029`, `spt_135`

### 🟠 HIGH: `his_196`
- Appears in **3 duplicate groups**
- Question: "What ancient civilization built Machu Picchu?"
- Duplicates: `his_014`, `his_169`

### 🟠 HIGH: `spt_192`
- Appears in **3 duplicate groups**
- Question: "What is it called when a player scores three goals in one game?"
- Duplicates: `spt_041`, `spt_052`

---

## Verification Commands

### Before Removal
```bash
# Count questions per category
python3 -c "
import json
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)
for cat, questions in data['categories'].items():
    print(f'{cat}: {len(questions)} questions')
print(f'Total: {sum(len(q) for q in data[\"categories\"].values())} questions')
"
```

### After Removal
```bash
# Verify counts decreased correctly
# Expected results:
# Bible: 142 → 137 (-5)
# Food: 64 → 61 (-3)
# History: 176 → 168 (-8)
# Science: 164 → 159 (-5)
# Sports: 155 → 148 (-7)
# Total: 1511 → 1483 (-28)
```

---

## Copy-Paste Removal List (for scripts)

```python
QUESTIONS_TO_REMOVE = [
    'bib_190', 'bib_196', 'bib_197', 'bib_201', 'bib_203',
    'foo_176', 'foo_185', 'foo_192',
    'his_175', 'his_189', 'his_190', 'his_193', 'his_195', 'his_196', 'his_198', 'his_200',
    'sci_179', 'sci_185', 'sci_202', 'sci_203', 'sci_204',
    'spt_190', 'spt_192', 'spt_194', 'spt_196', 'spt_198', 'spt_200', 'spt_201'
]
```

---

## Post-Removal Validation

After removing duplicates, verify:

1. [ ] Total question count is 1,483
2. [ ] No broken ID sequences (e.g., if removing sci_179, sci_180 should still exist)
3. [ ] All categories load correctly in app
4. [ ] Run duplicate analysis again to confirm zero duplicates
5. [ ] Test spinning wheel with all categories
6. [ ] Verify difficulty filtering still works

---

## Notes

- All 28 duplicates were introduced in the recent question expansion
- Most duplicates are in the ID ranges: 175-204
- `spt_200` is the most problematic with 4 duplicate groups
- Some questions test same knowledge across different sports (e.g., hat trick, players on field)
- Always keep the lower ID number when choosing which to keep
