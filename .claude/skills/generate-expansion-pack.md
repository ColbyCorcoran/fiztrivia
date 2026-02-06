# Generate Expansion Pack

Generate high-quality trivia questions for new or existing expansion packs with proper distribution across subtopics and difficulty levels.

## Usage

```
/generate-expansion-pack <pack-name> <question-count> [options]
```

## Arguments

- `pack-name`: Name/theme of the pack (e.g., "Narnia", "Candy", "Mario")
- `question-count`: Total questions to generate (e.g., 300, 400, 500)
- `options`: Optional JSON with pack configuration

## What It Does

Generates comprehensive trivia questions with:
- Proper difficulty distribution (easy/medium/hard)
- Even distribution across subtopics
- Sequential ID numbering
- Complete JSON structure ready to use
- Quality checks to prevent common issues

## Configuration

**Question Count by Price:**
- $1.99 → 300 questions (30 preview + 270 paid)
- $2.99 → 400 questions (40 preview + 360 paid)
- $3.99 → 500 questions (50 preview + 450 paid)

**Difficulty Distribution:**
- Easy: 35-40% (basic facts, main characters, obvious plot points)
- Medium: 40-45% (specific details, secondary characters, plot sequences)
- Hard: 15-25% (deep lore, minor details, expert knowledge)

**Subtopic Distribution:**
- Distribute evenly across all subtopics
- Example: 400 questions / 6 subtopics = ~65-70 per subtopic

## Content Requirements

### ✅ DO Include

**Family-Friendly Content**
- Age-appropriate for all audiences
- No explicit or controversial topics
- No graphic violence or gore details

**Factually Accurate**
- Verify all facts from official sources
- Double-check dates, names, numbers
- Avoid speculation or fan theories as facts

**Varied Question Types**
- Character questions (names, relationships, traits, voice actors)
- Plot questions (events, sequences, outcomes, key moments)
- World building (locations, creatures, magic/technology, rules)
- Meta questions (publication dates, creators, behind-the-scenes)
- Trivia (easter eggs, interesting facts, cultural impact)

**Clear Wording**
- 5-25 words typically
- Grammatically correct
- End with question mark
- Provide context when needed
- No ambiguity

### ❌ DON'T Include

**Self-Revealing Questions**
- ❌ BAD: "What is the name of the **Dinner Party** episode?" → "Dinner Party"
- ❌ BAD: "What spell creates a **Fidelius** Charm?" → "Fidelius"
- ✅ GOOD: "What episode features Michael hosting guests at his condo?" → "Dinner Party"

**Duplicate Questions**
- Check all existing questions in pack
- Don't ask same thing in different ways
- Vary question structures and angles

**Trick Questions**
- No questions with false premises
- No "gotcha" questions
- All options should be plausible

**Obvious Wrong Answers**
- All 4 options should be reasonable
- Don't make correct answer too obvious by elimination

## Question Structure

### Required JSON Format

```json
{
  "id": "[prefix]_[preview|paid]_[number]",
  "category": "Category Name",
  "subcategory": "Subcategory Name",
  "topic": "com.fiz.pack.[packid]",
  "subtopic": "Subtopic Name",
  "question": "Question text ending with ?",
  "options": [
    "Option 1",
    "Option 2",
    "Option 3",
    "Option 4"
  ],
  "correct_answer": "Exact match to one option",
  "difficulty": "easy|medium|hard"
}
```

### ID Naming Convention

**Preview Questions (10% of total):**
- Format: `[prefix]_preview_001` through `[prefix]_preview_[count]`
- Example: `nar_preview_001` through `nar_preview_040`

**Paid Questions (90% of total):**
- Format: `[prefix]_paid_001` through `[prefix]_paid_[count]`
- Example: `nar_paid_001` through `nar_paid_360`

**Prefix Examples:**
- 3 letters from pack name or acronym
- `nar` (Narnia), `can` (Candy), `mar` (Mario), `90s` (90s Trivia)

### Answer Options

- **Exactly 4 options** (no more, no less)
- All plausible (avoid obviously wrong answers)
- Similar length/format when possible
- **Correct answer must exactly match one option** (including punctuation)
- Mix up position of correct answer (don't always make it A or D)

## Category Mapping

**Literature** - Books, novels, written works
- Subcategories: Fantasy Literature, Science Fiction, Classic Literature

**Entertainment** - Movies, TV shows, animation
- Subcategories: Action/Adventure, Drama/Comedy, Animation, Film & TV, Sci-Fi/Fantasy

**Technology** - Video games, tech topics
- Subcategories: Video Games

**Music** - Songs, artists, albums
- Subcategories: Pop, Rock, Film & TV

**Sports** - Athletic topics
- Subcategories: Team Sports, Individual Sports, International Sports

**History** - Historical events
- Subcategories: Modern History, History & Eras

**Food** - Culinary topics
- Subcategories: Cuisine & Cooking

**Geography** - Places and locations
- Subcategories: World Geography

## Quality Checklist

Before finalizing, verify:

- [ ] All questions have exactly 4 options
- [ ] Correct answer matches one option exactly
- [ ] No self-revealing questions
- [ ] No duplicate questions
- [ ] Proper difficulty distribution (35-40% easy, 40-45% medium, 15-25% hard)
- [ ] Even subtopic distribution
- [ ] All questions grammatically correct
- [ ] All facts verified and accurate
- [ ] IDs properly formatted and sequential
- [ ] All required JSON fields present
- [ ] JSON is valid and properly formatted
- [ ] Family-friendly content only

## Example Questions

### ✅ Good Examples

```json
{
  "id": "nar_preview_001",
  "category": "Literature",
  "subcategory": "Fantasy Literature",
  "topic": "com.fiz.pack.narnia",
  "subtopic": "Characters",
  "question": "Who is the lion and true king of Narnia?",
  "options": ["Aslan", "Caspian", "Rilian", "Tumnus"],
  "correct_answer": "Aslan",
  "difficulty": "easy"
}

{
  "id": "can_paid_042",
  "category": "Food",
  "subcategory": "Cuisine & Cooking",
  "topic": "com.fiz.pack.candy",
  "subtopic": "History & Origins",
  "question": "Which candy bar was named after the Mars family's favorite horse?",
  "options": ["Snickers", "Milky Way", "Twix", "Mars Bar"],
  "correct_answer": "Snickers",
  "difficulty": "hard"
}

{
  "id": "90s_paid_123",
  "category": "Entertainment",
  "subcategory": "Film & TV",
  "topic": "com.fiz.pack.90s",
  "subtopic": "Movies",
  "question": "What 1997 film became the highest-grossing movie of all time?",
  "options": ["Jurassic Park", "Titanic", "The Lion King", "Independence Day"],
  "correct_answer": "Titanic",
  "difficulty": "medium"
}
```

### ❌ Bad Examples (Avoid)

```json
// Self-revealing
{
  "question": "What is the name of the Dinner Party episode?",
  "correct_answer": "Dinner Party"
}

// Ambiguous
{
  "question": "What happened next?",
  "options": ["This", "That", "Other", "Another"]
}

// Trick question
{
  "question": "What 1980s movie featured Tom Hanks?",
  "correct_answer": "Forrest Gump (1994)"
}

// Obvious wrong answers
{
  "question": "Who is the main character in Mario games?",
  "options": ["Mario", "Zebra", "Toaster", "Purple"],
  "correct_answer": "Mario"
}
```

## Output Format

Complete JSON ready to insert:

```json
{
  "packId": "com.fiz.pack.[name]",
  "packName": "Pack Display Name",
  "packDescription": "Description of pack content",
  "subtopics": ["Topic1", "Topic2", ...],
  "questionCount": 400,
  "freePreviewCount": 40,
  "difficulty": {
    "easy": 150,
    "medium": 170,
    "hard": 80
  },
  "price": 0.99,
  "icon": "SF Symbol name",
  "releaseDate": "YYYY-MM-DDTHH:MM:SSZ",
  "freePreviewQuestions": [...],
  "paidQuestions": [...]
}
```

## Example Usage

```bash
# Generate a new 400-question Narnia pack
/generate-expansion-pack Narnia 400

# Generate a 300-question Candy pack
/generate-expansion-pack Candy 300

# Generate with custom configuration
/generate-expansion-pack "90s Trivia" 400 '{"subtopics": ["Movies", "Music", "TV Shows", "Technology", "Fashion & Trends", "Sports & Events", "Pop Culture"]}'
```

## Tips for Best Results

1. **Research First**: Review source material before generating
2. **Check Existing Packs**: Look at similar packs for quality standards
3. **Run Audit After**: Use `/audit-expansion-pack` after generation
4. **Test Questions**: Try answering questions yourself to verify difficulty
5. **Get Feedback**: Have others review before finalizing
6. **Iterate**: Generate in batches, review, adjust as needed

## When to Use

- ✅ Creating brand new expansion packs
- ✅ Replacing duplicate questions from audits
- ✅ Expanding existing packs with more content
- ✅ Filling content gaps in specific subtopics
- ✅ Refreshing outdated questions
