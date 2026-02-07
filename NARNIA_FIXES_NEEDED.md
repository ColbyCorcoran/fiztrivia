# NARNIA PACK - QUICK FIX GUIDE

## 🔴 CRITICAL FIX: Remove 5 Duplicate Questions

### Delete These IDs:

1. **nar_cre_001** - "What type of creature is Mr. Tumnus?" (Creatures & Beings, easy)
   - Keep: nar_char_003 instead

2. **nar_cre_005** - "What type of creature is Aslan?" (Creatures & Beings, easy)
   - Keep: nar_char_002 instead

3. **nar_mag_003** - "What gift does Lucy receive from Father Christmas?" (Magic & Objects, easy)
   - Keep: nar_char_017 instead

4. **nar_mag_004** - "What gift does Susan receive from Father Christmas?" (Magic & Objects, easy/medium)
   - Keep: nar_char_023 instead

5. **nar_mag_008** - "What is the name of the ship in 'The Voyage of the Dawn Treader'?" (Magic & Objects, easy)
   - Keep: nar_plot_020 instead

### Replacement Questions Needed:

After removing duplicates, create 5 NEW questions:

- **2 questions** for "Creatures & Beings" subtopic (both easy difficulty)
- **3 questions** for "Magic & Objects" subtopic (all easy difficulty)

Total after fix: Still 400 questions (40 free + 360 paid)

---

## 🟡 MINOR FIX: Add subtopicIcons Field

Add this to the root level of the JSON (after "subtopics" array):

```json
"subtopicIcons": {
  "Books & Plot": "book.fill",
  "Characters": "person.3.fill",
  "Locations & Worlds": "map.fill",
  "Creatures & Beings": "pawprint.fill",
  "Magic & Objects": "sparkles",
  "Themes & Symbolism": "lightbulb.fill"
}
```

---

## 📋 After Fixes Checklist

- [ ] Deleted 5 duplicate question IDs
- [ ] Created 5 new replacement questions
- [ ] Added subtopicIcons field
- [ ] Verified total count: 400 questions
- [ ] Verified difficulty: 120 easy, 190 medium, 90 hard
- [ ] Verified free preview: 40 questions
- [ ] JSON validates (no syntax errors)
- [ ] Re-run audit script to confirm 100% pass

---

## 🎯 Estimated Fix Time: 35-65 minutes

- Delete duplicates: 5 min
- Create 5 new questions: 25-50 min
- Add subtopicIcons: 5 min
- Verify & test: 5-10 min

---

## ✅ What's Already Perfect (No Changes Needed)

- All 400 questions present
- All IDs unique and properly formatted
- All questions have 4 options
- All correct_answers match options
- Difficulty distribution correct
- No actual profanity (false positives only)
- No prohibited content
- Metadata accurate
- Family-friendly content
- High question quality
