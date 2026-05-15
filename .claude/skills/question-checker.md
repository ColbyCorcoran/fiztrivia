# Question Checker

Perform a deep, systematic accuracy audit on any Fiz trivia question database file — base `questions.json` or any expansion pack — and fix every issue found. This skill is informed by real patterns discovered through manual review of hundreds of questions and captures the subtle problems that generic linters miss.

## Usage

```
/question-checker <path-to-json-file>
```

Works on:
- `Fiz/Resources/questions.json` (base question database)
- `Fiz/Resources/Expansion Packs/expansion_*.json` (any expansion pack)

---

## Phase 1: Setup

1. **Read the full file** into memory.
2. **Determine the question pool**: for expansion packs, check both `freePreviewQuestions` and `paidQuestions`. For base questions.json, check the top-level array.
3. **Build a quick-reference index** of all question texts and correct answers by scanning for `"question":` and `"correct_answer":` fields. You will use this index for duplicate detection throughout.
4. **Note the source material** (show, franchise, topic) so you can apply domain knowledge when verifying facts.

---

## Phase 2: The 15 Issue Categories

For each question, run all 15 checks below. Flag every issue with its category number and severity.

---

### CATEGORY 1 — Wrong Character Attribution
**What it is:** The question assigns an action, quote, or trait to the wrong character.

**How to detect:**
- A question says Character A did X, but it was actually Character B who did X.
- A question uses "said by [character]" framing but the quote belongs to someone else.
- Common pattern: impression/parody quotes attributed to the original character instead of the imitator.

**Canonical example from this codebase:**
- ❌ "What does Dwight say about beets?" → "Bears, Beets, Battlestar Galactica" — this is *Jim's impression of Dwight*, not Dwight's own words.
- ❌ "What is Angela's cat's name that Michael kills?" — Dwight killed the cat (Sprinkles), not Michael.

**Severity:** REPLACE — the entire premise is wrong.

---

### CATEGORY 2 — Factually Wrong Job Title, Role, or Relationship
**What it is:** A character is described with the wrong occupation, rank, or relationship to another character.

**How to detect:**
- Question says "CEO" but character is CFO (or VP, COO, etc.).
- Question says character "owns" a location but they actually rent/lease it.
- Question says character "works at [place]" but they work somewhere else.
- Question describes a relationship incorrectly (e.g., says married when engaged, says boss when peer).

**Canonical examples from this codebase:**
- ❌ "Who is the CEO of Dunder Mifflin?" → David Wallace (he's CFO, not CEO).
- ❌ "What does the building owner do?" referencing Bob Vance (he's a *tenant*, not the building owner — Dwight owns the building).
- ❌ "Who does Michael date that works at the Scranton school system?" → Carol Stills (she's a *real estate agent*, not a school employee).

**Severity:** LIGHT FIX if only the description is wrong; REPLACE if the false description is load-bearing (removing it makes the question trivial or pointless).

---

### CATEGORY 3 — Self-Referential / Tautological Question
**What it is:** The correct answer is just a restatement or synonym of the question itself. Answering requires no actual knowledge.

**How to detect:**
- Read the question, cover the options, and ask: "Could someone answer this correctly just by rephrasing the question?" If yes, it's tautological.
- Watch for question stems like "What is X's [trait]?" where the answer literally names that trait.
- Watch for options structured as abstractions: "No issues / Depression / Anger management problems / Anxiety" — where "Anger management problems" directly mirrors the question "What is Andy's anger issue?"

**Canonical example from this codebase:**
- ❌ "What is Andy's anger issue?" → "Anger management problems" — the answer restates the question.

**Severity:** REPLACE — no light fix can salvage a tautological premise.

---

### CATEGORY 4 — Answer Revealed in Question Text
**What it is:** The exact answer word or a very strong clue appears inside the question text itself.

**How to detect:**
- Read the question and highlight every noun or proper name. If any highlighted word is also the correct answer (or makes one option obviously correct), it's self-revealing.
- Also flag when qualifier phrases in the question eliminate all wrong answers: "featuring a frog" makes it obvious the answer is "Pepe the Frog" since it's the only frog among the options.

**Canonical example from this codebase:**
- ❌ "Which family of **violins** were made by Antonio Stradivari?" → answer "Violins and cellos" — the word "violins" appears in the question.
- ❌ "Which internet meme **featuring a frog** was designated a hate symbol?" — among the options (Pepe the Frog, Nyan Cat, Grumpy Cat, Doge) only one is a frog, making it trivially easy.

**Severity:** LIGHT FIX (rephrase question to remove the giveaway) unless the question is also tautological, in which case REPLACE.

---

### CATEGORY 5 — Hint Embedded in Answer Option Text
**What it is:** The text of one option contains extra information that identifies it as correct, while other options have no such annotation.

**How to detect:**
- Scan all 4 options for parenthetical annotations, explanatory clauses, or qualifying phrases that only appear on one option.
- Any option formatted as "Answer (explanation)" when the others are just "Answer" is suspicious.

**Canonical example from this codebase:**
- ❌ Options: "Survivor: Nicaragua **(2 quits)**" / "Survivor: Kaôh Rōng" / "Survivor: Island of the Idols" / "Survivor: Samoa" — the "(2 quits)" annotation marks the answer since the question is asking which season had the most quits.

**Severity:** LIGHT FIX — remove the annotation from the option and correct_answer fields.

---

### CATEGORY 6 — Misattributed Quote
**What it is:** A specific quote is used as a question/answer but attributed to the wrong speaker or the wrong context (wrong episode, wrong moment).

**How to detect:**
- When a question asks "What does [Character] say?" verify the quote actually came from that character in that context.
- When a question ties a quote to a specific scene ("during the proposal", "on their first date"), verify the quote actually came from that scene — not an earlier or later scene with a superficially similar theme.
- Be especially careful with: confessions vs. proposals, in-character vs. out-of-character moments, parody vs. sincere delivery.

**Canonical examples from this codebase:**
- ❌ Question about Jim's proposal used the Casino Night (Season 2) confession quote — not the actual proposal moment.
- ❌ "What does Dwight say about beets?" used Jim's impression line "Bears, Beets, Battlestar Galactica."

**Severity:** REPLACE (the quote-context pairing is wrong; the entire question needs a new anchor).

---

### CATEGORY 7 — Vague Question / Non-Specific Answer
**What it is:** The question is too broad to have one defensible correct answer. Multiple characters, episodes, or facts could legitimately satisfy it.

**How to detect:**
- Read the question and ask: "Could more than one character or situation satisfy this?" If yes, flag it.
- **Red flag option patterns** (these almost always indicate a vague question):
  - Count-based options: "Nobody / One person / Several / Everyone"
  - Sentiment-based options: "Good / Bad / Mixed / Unknown"
  - Boolean options: "Yes / No / Sometimes / Always"
- Questions with "Who has..." or "Who does..." that don't specify enough context to narrow to a single character.
- Questions where all four options are equally plausible to a knowledgeable fan.

**Canonical examples from this codebase:**
- ❌ "Who has workplace affairs?" → options: Nobody / One / Several / Everyone
- ❌ "Who has secret relationships?" → multiple character pairs qualify
- ❌ "What does Michael wear to work sometimes?" → non-specific, no single defensible answer

**Severity:** REPLACE — vagueness cannot be fixed with light edits; a new specific question is needed.

---

### CATEGORY 8 — Generic Real-World Knowledge (Not Franchise-Specific)
**What it is:** The correct answer is something any person with general knowledge would know, not something that tests knowledge of the specific show/franchise.

**How to detect:**
- Ask: "Could someone who has never seen this show answer this correctly?" If yes, flag it.
- Watch for questions about generic professional behavior, obvious common sense, or real-world geography/facts with no show-specific twist.

**Canonical example from this codebase:**
- ❌ "Where do salespeople go?" → "Client meetings" — any salesperson anywhere does this; no Office knowledge required.

**Severity:** REPLACE — the question needs to be reanchored to a specific, franchise-unique fact.

---

### CATEGORY 9 — Duplicate or Near-Duplicate Coverage
**What it is:** The same fact is already tested by another question in the same file. One of the two must be replaced.

**How to detect:**
This requires active searching, not just reading. For any question about Topic X:
1. `grep` the file for key terms from Topic X.
2. Count how many other questions cover the same fact.
3. Flag if 2+ questions cover the identical fact, even with different wording.

**What counts as a duplicate:**
- Same character performing the same action (even if one question asks "who" and the other asks "what")
- Same quote asked from two angles ("What does Jim say?" vs. "Who says 'Bears, Beets...'?")
- Same relationship covered from both partners' perspectives with the same answer

**Canonical examples from this codebase:**
- Oscar/Senator affair was covered by 3 separate questions.
- Andy's anger management was covered by 3 separate questions (off_paid_080, off_paid_112, off_paid_203).

**Severity:** REPLACE one of the duplicates with a different topic entirely. Keep the better-worded version of the duplicate pair.

---

### CATEGORY 10 — Subtopic Mismatch
**What it is:** The question is filed under the wrong subtopic category.

**How to detect:**
- Check whether the question actually tests knowledge of its listed subtopic.
- For expansion packs: subtopics are e.g., Characters / Quotes / Episodes / Relationships / Locations / Trivia.
- A question about what a character owns or does belongs in "Characters" not "Quotes."
- A question that contains a quote should be in "Quotes" not "Trivia."
- A question about where something happens belongs in "Locations" not "Characters."

**Canonical example from this codebase:**
- ❌ "What does Dwight grow on his farm?" filed under subtopic "Quotes" — should be "Characters."

**Severity:** LIGHT FIX — change only the `subtopic` field.

---

### CATEGORY 11 — Duplicate or Repeated Option Values
**What it is:** Two or more of the four answer options are effectively the same answer (same person, same place, same concept — just with different wording or spelling).

**How to detect:**
- Read all 4 options together and check for:
  - Same name with/without title ("Philip" and "Phillip Schrute" — same person)
  - All options from the same category with only one distinguishing feature ("Tom Vance / Bob Vance / Joe Vance / Vance Refrigeration")
  - Options that overlap in meaning (e.g., two options that would both be counted as correct)

**Canonical examples from this codebase:**
- ❌ Options included "Philip" and "Phillip Schrute" — same person, different spelling.
- ❌ All four options were "[Name] Vance" — not meaningful distractors.

**Severity:** LIGHT FIX — replace the duplicate/overlapping options with distinct, plausible alternatives from the same domain.

---

### CATEGORY 12 — False Premise in Question
**What it is:** The question contains a factual error in its setup that makes the "correct" answer only correct if you accept the false premise.

**How to detect:**
- Ask: "Is the premise of this question actually true?" separately from "Is the answer correct given the premise?"
- Watch for questions structured as "What did [Character] do when [false event]?" where the false event never happened.
- Particularly dangerous: "gotcha" questions that try to correct themselves via a "None of the above / actually it was..." option — this is always bad design.

**Canonical examples from this codebase:**
- ❌ "What is Angela's cat's name that **Michael** kills?" — Michael didn't kill any cat; Dwight did.
- ❌ "Who does Michael date that works at the **Scranton school system**?" — Carol Stills is a realtor, not a school employee.

**Severity:** REPLACE — the false premise cannot be lightly corrected without changing the entire question.

---

### CATEGORY 13 — Unverifiable Specific Claim
**What it is:** The question asks about a very specific detail that cannot be confirmed from the source material, or the "correct" answer is based on an assumption rather than a fact shown in the show/book/film.

**How to detect:**
- Ask: "Is this something that was explicitly shown/stated in the source, or is this an inference?"
- Be skeptical of: exact quotes for minor scenes, off-screen actions described as fact, backstory claims that were implied but never stated.
- Watch for options that seem too specific to be verifiable (e.g., "He says 'I hereby declare...' exactly").

**Canonical example from this codebase:**
- ❌ "What does Dwight say when he first takes over as interim manager?" — the specific quote was not confirmed as exact.

**Severity:** REPLACE — use the slot for a fact that IS verifiable from the source material.

---

### CATEGORY 14 — Inappropriate Content for a Family-Friendly App
**What it is:** The question involves controversial political content, hate groups, adult themes, or graphic subject matter that conflicts with the app's family-friendly audience.

**How to detect:**
- Would a parent be uncomfortable seeing this question pop up during a game with their child?
- Does the question involve hate symbols, slurs, graphic violence, explicit content, or deeply partisan political topics?
- Is the "interesting" fact about the question actually just shock value?

**Canonical example from this codebase:**
- ❌ "Which internet meme was designated a hate symbol?" — introduces hate symbol terminology in a casual trivia context.

**Severity:** REPLACE — find a neutral, family-friendly fact on the same general topic.

---

### CATEGORY 15 — Confusing or Ambiguous Question Logic
**What it is:** The question can be read in multiple ways that lead to different correct answers, or the question structure creates false ambiguity.

**How to detect:**
- Read the question twice from different angles. Do you get the same intended answer both times?
- Watch for questions using "original" — does it mean the very first version, or the most recent name before the current one?
- Watch for questions where one option is a meta-commentary ("Twitter (it's now called X)") rather than a factual answer.
- Watch for "before" and "after" timeline questions where the direction is ambiguous.

**Canonical example from this codebase:**
- ❌ "What was the original name of Twitter before rebranding to X?" — "original" could mean Twttr (the 2006 prototype name) OR Twitter (the name used until 2023 rebranding). The options included both plus a meta-joke option.

**Severity:** LIGHT FIX if rephrase makes intent unambiguous; REPLACE if the ambiguity is structural.

---

## Phase 3: The Duplicate-Check Workflow (Required Before Every Replacement)

Before writing any replacement question, you MUST verify the proposed new topic isn't already covered:

1. Choose your intended replacement topic (e.g., "Where does Jim propose to Pam?")
2. Extract 2–3 key terms (e.g., "propose", "Jim", "Pam", "rest stop")
3. `grep` the file for each key term — check `question` fields AND `correct_answer` fields
4. If ANY existing question covers the same fact from ANY angle, choose a different replacement topic
5. Only write the replacement after confirming it's genuinely uncovered

**This step is non-negotiable.** Skipping it creates the exact duplicate problem you're trying to fix.

---

## Phase 4: The Fix Decision Tree

```
Is the question factually wrong?
├── Yes, the entire premise is wrong → REPLACE
├── Yes, one specific field is wrong (job title, subtopic, option text) → LIGHT FIX
└── No → continue checking

Is the question self-referential or tautological?
├── Yes → REPLACE
└── No → continue checking

Is the question too vague to have one defensible answer?
├── Yes → REPLACE
└── No → continue checking

Is the question a duplicate of existing coverage?
├── Yes → REPLACE (run duplicate-check to pick non-covered topic)
└── No → continue checking

Does the answer appear in the question text?
├── Yes, and the question can be rephrased to remove it → LIGHT FIX
├── Yes, and removing it makes the question trivial → REPLACE
└── No → continue checking

Is the question inappropriate for family audiences?
├── Yes → REPLACE
└── No → PASS ✓
```

---

## Phase 5: Writing Good Replacements

A good replacement question meets ALL of these criteria:

**Specific:** Tests a single, concrete, verifiable fact. Not "Who does X relate to?" but "What is the name of X's [specific relationship]?"

**Franchise-unique:** Someone who has never seen/read the source material cannot guess the answer from general knowledge.

**Unambiguous:** Only one reading of the question is possible. Only one option is clearly correct.

**Balanced options:** All four options should be plausible to someone with partial knowledge. Avoid: options from the same quote/scene, name variants of the same person, obviously absurd distractors.

**Correct difficulty:** Easy = main character/central plot fact. Medium = secondary character or specific episode detail. Hard = minor background detail, specific line of dialogue, or behind-the-scenes fact.

**Verified:** You are confident the fact is correct and explicitly shown in the source material (not inferred or assumed).

---

## Phase 6: Execution

For each flagged question:

1. Note the ID, category number, and severity (LIGHT FIX vs. REPLACE).
2. For LIGHT FIX: make the minimal targeted change. Update only the affected field(s).
3. For REPLACE:
   a. Run the duplicate-check workflow for your intended new topic.
   b. Write the replacement question meeting all Phase 5 criteria.
   c. Update: `question`, `options`, `correct_answer`, `difficulty`, and `subtopic` if needed.
   d. Leave `id`, `category`, `subcategory`, `topic` unchanged.
4. After completing all fixes in a batch, commit with a descriptive message listing each changed ID and why.
5. Push to the current branch.

---

## Phase 7: Output Report

After all fixes are complete, output a summary:

```
QUESTION CHECKER REPORT
File: [filename]
Total questions checked: [X]
Issues found: [Y]

LIGHT FIXES ([count]):
- [id]: [category] — [one-line description of change]

FULL REPLACEMENTS ([count]):
- [id]: [category] — [original topic] → [new topic]

ALREADY CORRECT (stale screenshots / previously fixed): [count]
- [id]: [why it was flagged but is actually fine]

SKIPPED (could not verify without source material): [count]
- [id]: [what would need to be verified]

Commit: [commit hash]
```

---

## Common Pitfalls to Avoid

**Don't fix what isn't broken.** Some questions that look suspicious are actually correct. Confirm before changing.

**Don't assume — verify.** Before flagging a fact as wrong, check surrounding questions in the file for context. Often neighboring questions about the same character or episode will confirm or deny the fact.

**Don't introduce new duplicates.** Always grep before writing a replacement. The most common mistake is replacing one duplicate with a question that duplicates something else.

**Don't change the ID.** IDs are used for tracking answered questions. Changing an ID resets a player's history for that question.

**Don't change the category or subcategory** unless it's clearly wrong. These affect how questions are routed to the wheel.

**Don't replace with a less interesting question.** A bad question replaced by a boring one is a net loss for the product. Replacements should be genuinely fun to answer.

**Batch your commits.** Fix a logical group (one batch of screenshots, one category of issues), then commit and push. Don't commit after every single edit.
