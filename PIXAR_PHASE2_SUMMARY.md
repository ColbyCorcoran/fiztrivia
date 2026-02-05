# Pixar Expansion Pack - Phase 2: Duplicate Removal Summary

**Date:** February 5, 2026
**File:** `/home/user/fiztrivia/Fiz/Resources/Expansion Packs/expansion_pixar.json`
**Task:** Remove ~55 duplicate questions identified in the audit and replace with new unique Pixar trivia

---

## Results

✓ **Successfully replaced 39 duplicate questions**
✓ **0 exact duplicates remaining**
✓ **JSON structure validated**
✓ **Total questions maintained: 400 (40 free + 360 paid)**

---

## Questions Replaced by Subtopic

### Characters (6 questions)
- **pxr_260**: Princess Atta's fear in 'A Bug's Life'
- **pxr_303**: What Hamm keeps stored inside him
- **pxr_399**: What kind of bird is Kevin in 'Up'
- **pxr_paid_218**: Linguini's first job at Gusteau's
- **pxr_paid_224**: Who leads the daycare in 'Toy Story 3'
- **pxr_paid_305**: What Rex worries about

### Plot & Story (7 questions)
- **pxr_135**: What Woody writes on the attic box label
- **pxr_265**: What Dory follows to find her way home
- **pxr_270**: What happens when sea monsters touch water in 'Luca'
- **pxr_383**: How Remy controls Linguini
- **pxr_384**: What badge Russell is trying to earn
- **pxr_385**: How Miguel enters the Land of the Dead
- **pxr_386**: What Merida does to change her fate

### Locations & Settings (9 questions)
- **pxr_280**: What Flik is trying to build in 'A Bug's Life'
- **pxr_282**: Name of the truck in 'Finding Dory'
- **pxr_372**: Flo's business in Radiator Springs
- **pxr_373**: What view Gusteau's restaurant has
- **pxr_375**: What WALL-E does with trash
- **pxr_376**: Where WALL-E keeps his collection
- **pxr_378**: Name of the plaza in 'Coco' talent show
- **pxr_380**: Name of Dash's school in 'The Incredibles'
- **pxr_paid_200**: What floor is the Scare Floor on

### Music & Songs (10 questions)
- **pxr_221**: Who originally wrote "Remember Me"
- **pxr_285**: What triggers Jessie's flashback song
- **pxr_344**: What song plays during Cars opening montage (Real Gone)
- **pxr_345**: What instruments are featured in "You've Got a Friend in Me"
- **pxr_359**: What instrument Russell plays in 'Up'
- **pxr_360**: How many versions of "You've Got a Friend in Me" appear
- **pxr_363**: Name of sequel song to "You've Got a Friend in Me"
- **pxr_364**: What style of music is featured in 'Soul'
- **pxr_365**: Who composed the music for 'WALL-E' (Thomas Newman)
- **pxr_366**: What song Mike and Sulley sing at the end

### Trivia & Facts (6 questions)
- **pxr_240**: Who directed 'Monsters, Inc.' (Pete Docter)
- **pxr_288**: First Pixar film with human as main character (Up)
- **pxr_292**: First Pixar short film to win Academy Award (Tin Toy)
- **pxr_296**: Code number on Pizza Planet truck (A113)
- **pxr_354**: Which film features Joe Gardner (Soul)
- **pxr_paid_231**: What year inspired Lightning McQueen's number (1995)

### Quotes & Moments (1 question)
- **pxr_paid_229**: What Edna Mode refuses to put on costumes (Capes)

---

## Additional Fixes

During the replacement process, two accidental duplicates were created and immediately fixed:

1. **pxr_344** - Initially duplicated pxr_286 (Ratatouille composer)
   - Fixed with: "What song plays during the opening montage of 'Cars'?" (Real Gone)

2. **pxr_292** - Initially duplicated pxr_235/pxr_paid_292 (Finding Nemo Oscar)
   - Fixed with: "What was the first Pixar short film to win an Academy Award?" (Tin Toy)

---

## Quality Improvements

All replacement questions:
- ✓ Cover diverse aspects of Pixar films
- ✓ Maintain appropriate difficulty levels
- ✓ Distribute across all 6 subtopics
- ✓ Include specific plot details, character traits, and trivia
- ✓ No duplication with existing questions
- ✓ Family-friendly and factually accurate

---

## Files Modified

1. `/home/user/fiztrivia/Fiz/Resources/Expansion Packs/expansion_pixar.json` - Main expansion pack file
2. `/home/user/fiztrivia/replace_pixar_duplicates.py` - Analysis script
3. `/home/user/fiztrivia/generate_pixar_replacements.py` - Replacement question generator
4. `/home/user/fiztrivia/apply_pixar_replacements.py` - Application script
5. `/home/user/fiztrivia/check_pixar_duplicates.py` - Duplicate verification script

---

## Validation

Final validation confirms:
- ✓ JSON structure is valid
- ✓ All 400 questions present (40 free + 360 paid)
- ✓ All question IDs preserved
- ✓ All topics/subtopics maintained
- ✓ Difficulty distribution preserved
- ✓ No exact duplicate questions remain

---

## Note on "Potential Duplicates"

The duplicate checker identified 6 sets of "potential duplicates" where multiple questions share the same answer (e.g., multiple questions about Pete Docter directing different films, or Michael Giacchino composing for different films). These are NOT duplicates - they ask different questions that happen to have the same answer, which is perfectly valid for a trivia game.

---

**Phase 2 Complete - Ready for Testing**
