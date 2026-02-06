# Audit Expansion Pack

Perform comprehensive quality audit on trivia expansion pack JSON files to identify duplicates, self-revealing answers, grammar errors, and factual inaccuracies.

## Usage

```
/audit-expansion-pack <path-to-json-file>
```

## What It Does

This skill audits trivia expansion pack JSON files and generates a comprehensive quality report with three categories of issues:

1. **AUTO-FIX**: Grammar and typos that can be corrected automatically
2. **FLAG FOR REPLACEMENT**: Duplicate questions needing replacement
3. **NEEDS VERIFICATION**: Questionable accuracy requiring human review

## Audit Process

### 1. Load and Validate
- Reads the expansion pack JSON file
- Validates JSON structure and required fields
- Counts total questions (freePreviewQuestions + paidQuestions)

### 2. Check for Issues

**Grammar & Typos (AUTO-FIX)**
- Missing articles (a, an, the)
- Misspelled character/place names
- Double spaces, incorrect punctuation
- Malformed sentences

**Exact Duplicates (FLAG FOR REPLACEMENT)**
- Identical question text
- Same question ID used twice

**Semantic Duplicates (FLAG FOR REPLACEMENT)**
- Same question about same subject with different wording
- ✅ DIFFERENT: "Who plays Thor?" vs "Who plays Hulk?" (different subjects - OK)
- ❌ DUPLICATE: "Who plays Iron Man?" vs "In Iron Man, who plays Tony Stark?" (same subject)

**Self-Revealing Questions (FLAG FOR REPLACEMENT)**
- Answer appears directly in question text
- ❌ BAD: "What is the **Dinner Party** episode called?" → "Dinner Party"
- ❌ BAD: "What battle took place on **Hoth**?" → "Battle of Hoth"
- ✅ GOOD: "What does Michael say?" → "That's what she said"

**Factual Accuracy (NEEDS VERIFICATION)**
- Incorrect answers
- Outdated information
- Conflicting answers to similar questions
- Wrong categorization

**Confusing Wording (NEEDS VERIFICATION)**
- Ambiguous questions
- Tautological questions (answer = question)
- Questions missing context

### 3. Generate Report

For each issue found, provide:
- Question ID
- Issue type
- Current question text
- Why it's problematic
- Suggested fix (if applicable)

### 4. Output Format

```
EXPANSION PACK QUALITY AUDIT
Pack: [Name]
Total Questions: [X]
Issues Found: [Y] ([Z]%)

AUTO-FIX (Grammar/Typos): [count]
- [id]: [issue description]

FLAG FOR REPLACEMENT (Duplicates): [count]
- [id1] & [id2]: [why they're duplicates]

NEEDS VERIFICATION: [count]
- [id]: [issue description]

Quality Score: [X]%

RECOMMENDATIONS:
[Prioritized list of fixes needed]
```

## Important Notes

**Avoid False Positives:**
- Don't flag questions with similar structures about DIFFERENT subjects
  - "What type of animal is Dumbo?" vs "What type of animal is Pumbaa?" → DIFFERENT (OK)
  - "Who wrote music for Aladdin?" vs "Who wrote music for Frozen?" → DIFFERENT (OK)

**Common Words Don't Count:**
- Words like "what", "the", "is", "battle", "jedi" alone don't make questions self-revealing
- Only flag when the actual answer word/phrase appears in the question

**Context Matters:**
- Some questions need the subject in the question
- Example: "What is the bar in 'Cheers' called?" → "Cheers" (may be acceptable if bar name = show name)

## Example Usage

```bash
# Audit a specific expansion pack
/audit-expansion-pack Fiz/Resources/Expansion\ Packs/expansion_pixar.json

# Audit all expansion packs
for file in Fiz/Resources/Expansion\ Packs/expansion_*.json; do
  /audit-expansion-pack "$file"
done
```

## Output Files

The skill generates:
- `[pack_name]_audit_report.txt` - Detailed findings
- `[pack_name]_audit_summary.md` - Executive summary with metrics

## When to Use

- ✅ After creating a new expansion pack
- ✅ Before releasing pack updates
- ✅ During routine quality checks
- ✅ When users report question issues
- ✅ After importing questions from external sources

## Quality Metrics

The audit calculates:
- Total issues found
- Issue percentage
- Quality score (100% - issue %)
- Issues by category
- Recommendations prioritized by severity
