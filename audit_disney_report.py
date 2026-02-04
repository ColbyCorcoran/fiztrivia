#!/usr/bin/env python3
"""
Improved Disney expansion pack quality audit report.
Filters false positives and provides actionable insights.
"""

import json
import re
from collections import defaultdict
from difflib import SequenceMatcher

def load_questions(filepath):
    """Load questions from JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    all_questions = []
    all_questions.extend(data.get('freePreviewQuestions', []))
    all_questions.extend(data.get('paidQuestions', []))
    return all_questions

def similarity_ratio(str1, str2):
    """Calculate similarity between two strings."""
    return SequenceMatcher(None, str1.lower(), str2.lower()).ratio()

def check_semantic_duplicates(questions, threshold=0.85):
    """Find questions that are semantically similar."""
    duplicates = []
    checked = set()

    for i, q1 in enumerate(questions):
        for j, q2 in enumerate(questions[i+1:], start=i+1):
            pair = tuple(sorted([q1['id'], q2['id']]))
            if pair in checked:
                continue
            checked.add(pair)

            ratio = similarity_ratio(q1['question'], q2['question'])
            if ratio >= threshold:
                duplicates.append({
                    'id1': q1['id'],
                    'id2': q2['id'],
                    'q1': q1['question'],
                    'q2': q2['question'],
                    'similarity': ratio,
                    'subtopic1': q1.get('subtopic', 'Unknown'),
                    'subtopic2': q2.get('subtopic', 'Unknown')
                })

    return duplicates

def check_grammar_issues(questions):
    """Check for real grammar issues (excluding false positives)."""
    issues = []

    patterns = {
        'double_space': [(r'  +', 'Double space')],
        'missing_apostrophe': [
            (r"\bdont\b", "Should be \"don't\""),
            (r"\bcant\b", "Should be \"can't\""),
            (r"\bwont\b", "Should be \"won't\""),
            (r"\bisnt\b", "Should be \"isn't\""),
            (r"\barent\b", "Should be \"aren't\""),
            (r"\bwasnt\b", "Should be \"wasn't\""),
            (r"\bwerent\b", "Should be \"weren't\""),
            (r"\bhasnt\b", "Should be \"hasn't\""),
            (r"\bhavent\b", "Should be \"haven't\""),
            (r"\bdidnt\b", "Should be \"didn't\""),
        ],
        'typos': [
            (r'\bDiseny\b', 'Typo: should be "Disney"'),
            (r'\bcharater\b', 'Typo: should be "character"'),
            (r'\bpriness\b', 'Typo: should be "princess"'),
            (r'\bmovei\b', 'Typo: should be "movie"'),
            (r'\bfilim\b', 'Typo: should be "film"'),
            (r'\bthe the\b', 'Duplicate word'),
            (r'\ba a\b', 'Duplicate word'),
            (r'\bin in\b', 'Duplicate word'),
        ],
        'spacing': [
            (r'\s+\?', 'Space before question mark'),
            (r'\s+,', 'Space before comma'),
            (r'\(\s+', 'Space after opening parenthesis'),
            (r'\s+\)', 'Space before closing parenthesis'),
        ]
    }

    for q in questions:
        q_issues = []
        text = q['question']

        for category, pattern_list in patterns.items():
            for pattern, description in pattern_list:
                if re.search(pattern, text, re.IGNORECASE):
                    q_issues.append({
                        'category': category,
                        'description': description,
                        'pattern': pattern
                    })

        if q_issues:
            issues.append({
                'id': q['id'],
                'question': text,
                'issues': q_issues,
                'subtopic': q.get('subtopic', 'Unknown')
            })

    return issues

def find_problematic_patterns(questions):
    """Find specific problematic patterns that need attention."""
    issues = []

    for q in questions:
        text = q['question']
        answer = q['correct_answer']
        q_issues = []

        # Check for grammar issue: missing article
        if re.search(r'\b(one of|name of)\s+the\s+one\b', text, re.IGNORECASE):
            q_issues.append('Redundant phrasing: "one of the one"')

        # Check for confusing double negatives
        double_neg_matches = re.findall(r'\b(not|never|no)\b', text, re.IGNORECASE)
        if len(double_neg_matches) >= 2:
            q_issues.append('Contains double negative (may be confusing)')

        # Check if answer might be self-revealing
        if len(answer) > 4:  # Only check non-trivial answers
            # Remove quote marks from question for checking
            clean_question = re.sub(r"['\"]", '', text.lower())
            clean_answer = answer.lower()

            # Check if full answer appears outside quotes
            if clean_answer in clean_question:
                # Check if it's in a movie title (which is OK)
                if not re.search(rf"in ['\"]?{re.escape(answer)}['\"]?", text, re.IGNORECASE):
                    q_issues.append(f'Answer "{answer}" may be revealed in question')

        if q_issues:
            issues.append({
                'id': q['id'],
                'question': text,
                'answer': answer,
                'concerns': q_issues,
                'subtopic': q.get('subtopic', 'Unknown')
            })

    return issues

def generate_clean_report(questions):
    """Generate a clean, actionable quality audit report."""
    print("=" * 80)
    print("DISNEY EXPANSION PACK - QUALITY AUDIT REPORT")
    print("=" * 80)
    print(f"\nTotal questions analyzed: {len(questions)}\n")

    # Run all checks
    semantic_dupes = check_semantic_duplicates(questions)
    grammar = check_grammar_issues(questions)
    problematic = find_problematic_patterns(questions)

    # SECTION 1: AUTO-FIX ISSUES
    print("\n" + "=" * 80)
    print("1. AUTO-FIX ISSUES")
    print("=" * 80)
    print("\nClear typos and grammar errors that can be automatically fixed.\n")

    if grammar:
        for idx, item in enumerate(grammar, 1):
            print(f"{idx}. ID: {item['id']} | Subtopic: {item['subtopic']}")
            for issue in item['issues']:
                print(f"   Issue: {issue['description']}")
            print(f"   Question: {item['question']}")
            print()
    else:
        print("✓ No auto-fix issues found!\n")

    # SECTION 2: FLAG FOR REPLACEMENT
    print("\n" + "=" * 80)
    print("2. FLAG FOR REPLACEMENT - SEMANTIC DUPLICATES")
    print("=" * 80)
    print(f"\nFound {len(semantic_dupes)} pairs of semantically similar questions.\n")
    print("These questions use very similar wording and should be replaced with")
    print("unique questions to add variety to the quiz experience.\n")

    if semantic_dupes:
        # Group by similarity level
        very_high = [d for d in semantic_dupes if d['similarity'] >= 0.95]
        high = [d for d in semantic_dupes if 0.90 <= d['similarity'] < 0.95]
        medium = [d for d in semantic_dupes if 0.85 <= d['similarity'] < 0.90]

        if very_high:
            print(f"--- VERY HIGH SIMILARITY (≥95%) - {len(very_high)} pairs ---\n")
            for idx, item in enumerate(very_high[:20], 1):  # Show first 20
                print(f"{idx}. IDs: {item['id1']}, {item['id2']} ({item['similarity']:.0%} similar)")
                print(f"   Subtopics: {item['subtopic1']}, {item['subtopic2']}")
                print(f"   Q1: {item['q1']}")
                print(f"   Q2: {item['q2']}")
                print(f"   → ACTION: These are nearly identical - keep one, replace the other\n")

        if high:
            print(f"\n--- HIGH SIMILARITY (90-94%) - {len(high)} pairs ---\n")
            for idx, item in enumerate(high[:15], 1):  # Show first 15
                print(f"{idx}. IDs: {item['id1']}, {item['id2']} ({item['similarity']:.0%} similar)")
                print(f"   Subtopics: {item['subtopic1']}, {item['subtopic2']}")
                print(f"   Q1: {item['q1']}")
                print(f"   Q2: {item['q2']}")
                print(f"   → ACTION: Very similar pattern - consider replacing one\n")

        if medium:
            print(f"\n--- MEDIUM SIMILARITY (85-89%) - {len(medium)} pairs ---\n")
            print(f"Showing first 10 of {len(medium)} medium-similarity pairs:\n")
            for idx, item in enumerate(medium[:10], 1):
                print(f"{idx}. IDs: {item['id1']}, {item['id2']} ({item['similarity']:.0%} similar)")
                print(f"   Q1: {item['q1']}")
                print(f"   Q2: {item['q2']}\n")

    # SECTION 3: NEEDS VERIFICATION
    print("\n" + "=" * 80)
    print("3. NEEDS HUMAN VERIFICATION")
    print("=" * 80)
    print("\nQuestions that may have issues requiring human review.\n")

    if problematic:
        print(f"Found {len(problematic)} questions with potential issues:\n")
        for idx, item in enumerate(problematic, 1):
            print(f"{idx}. ID: {item['id']} | Subtopic: {item['subtopic']}")
            print(f"   Question: {item['question']}")
            print(f"   Answer: {item['answer']}")
            for concern in item['concerns']:
                print(f"   ⚠ {concern}")
            print()
    else:
        print("✓ No verification issues found!\n")

    # SUMMARY
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total questions analyzed:        {len(questions)}")
    print(f"Auto-fix grammar issues:         {len(grammar)}")
    print(f"Semantic duplicate pairs:        {len(semantic_dupes)}")
    print(f"Questions needing verification:  {len(problematic)}")
    print(f"\nPriority: Address semantic duplicates first ({len(semantic_dupes)} pairs)")
    print(f"This means {len(semantic_dupes)} questions should be replaced with new ones.")
    print()

if __name__ == '__main__':
    filepath = '/home/user/fiztrivia/Fiz/Resources/Expansion Packs/expansion_disney.json'
    questions = load_questions(filepath)
    generate_clean_report(questions)
