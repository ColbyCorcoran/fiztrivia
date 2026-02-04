#!/usr/bin/env python3
"""
Quality audit script for Disney expansion pack.
Checks for duplicates, grammar issues, and other quality problems.
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

def check_exact_duplicates(questions):
    """Find questions with identical text."""
    seen = defaultdict(list)
    duplicates = []

    for q in questions:
        text = q['question'].strip().lower()
        seen[text].append(q['id'])

    for text, ids in seen.items():
        if len(ids) > 1:
            duplicates.append({
                'question': text,
                'ids': ids,
                'count': len(ids)
            })

    return duplicates

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
                    'similarity': ratio
                })

    return duplicates

def check_grammar_issues(questions):
    """Check for common grammar issues."""
    issues = []

    # Patterns to check
    patterns = {
        'missing_article': [
            (r'\b(is|was|has|had|in|on|at|to|from)\s+(character|movie|film|song|park|princess|villain|hero|scene|story|actor|actress)\b',
             'Missing article (a/an/the)'),
            (r'\b(voice|name|color|title|year|date|location|place)\s+of\s+(character|movie|film|song|park)\b',
             'Missing article (a/an/the)'),
        ],
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
        'punctuation': [
            (r'\?\?', 'Double question mark'),
            (r'[,;]\s*$', 'Question ends with comma/semicolon instead of ?'),
            (r'^[a-z]', 'Question starts with lowercase'),
            (r'[^?!.]$', 'Question missing ending punctuation'),
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
                'issues': q_issues
            })

    return issues

def check_self_revealing(questions):
    """Check if answer appears in question text."""
    issues = []

    for q in questions:
        question_lower = q['question'].lower()
        answer_lower = q['correct_answer'].lower()

        # Remove common words from answer for checking
        answer_words = set(answer_lower.split())
        common_words = {'a', 'an', 'the', 'in', 'on', 'at', 'to', 'of', 'and', 'or', 'is', 'was'}
        significant_words = answer_words - common_words

        # Check if answer or significant parts appear in question
        if len(answer_lower) > 3 and answer_lower in question_lower:
            # Make sure it's not just mentioning the movie/character in context
            # Look for direct reveals
            if not any(phrase in question_lower for phrase in [
                f"'{answer_lower}'", f'"{answer_lower}"',
                f"called {answer_lower}", f"named {answer_lower}",
                "in " + answer_lower, "from " + answer_lower
            ]):
                issues.append({
                    'id': q['id'],
                    'question': q['question'],
                    'answer': q['correct_answer'],
                    'reason': 'Answer appears in question text'
                })
        elif len(significant_words) > 0:
            # Check if multiple significant words from answer appear
            matches = sum(1 for word in significant_words if word in question_lower)
            if len(significant_words) <= 2 and matches == len(significant_words):
                # All significant words appear (for short answers)
                if not any(phrase in question_lower for phrase in [
                    f"'{answer_lower}'", f'"{answer_lower}"'
                ]):
                    issues.append({
                        'id': q['id'],
                        'question': q['question'],
                        'answer': q['correct_answer'],
                        'reason': 'Answer components appear in question'
                    })

    return issues

def check_confusing_wording(questions):
    """Check for potentially confusing or ambiguous questions."""
    issues = []

    confusing_patterns = [
        (r'\b(this|that|these|those|it|they|he|she)\b', 'Ambiguous pronoun without clear reference'),
        (r'\bor\b.*\bor\b.*\bor\b', 'Multiple "or" clauses may be confusing'),
        (r'^(What|Which|Who|Where|When|How)\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+\w+\s+',
         'Very long question (may be confusing)'),
        (r'\b(not|except|never|without)\b.*\b(not|except|never|without)\b', 'Double negative'),
    ]

    for q in questions:
        text = q['question']
        q_issues = []

        for pattern, description in confusing_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                # Some patterns need manual review
                q_issues.append(description)

        # Check for very short questions that might be unclear
        if len(text.split()) < 4 and '?' in text:
            q_issues.append('Very short question (may lack context)')

        if q_issues:
            issues.append({
                'id': q['id'],
                'question': text,
                'concerns': q_issues
            })

    return issues

def check_answer_correctness(questions):
    """Flag questions that might have incorrect answers (pattern-based)."""
    issues = []

    # Common factual issues to flag for review
    review_patterns = [
        (r'(first|original|oldest|earliest)', 'Claims about "first/original" - verify accuracy'),
        (r'(never|always|only|exclusively)', 'Absolute claims - verify accuracy'),
        (r'(most|largest|biggest|smallest|longest|shortest)', 'Superlative claims - verify accuracy'),
        (r'\d{4}', 'Contains year - verify date accuracy'),
        (r'\$[\d,]+', 'Contains price/money - verify amount'),
        (r'\d+\s+(million|billion|thousand)', 'Contains large numbers - verify accuracy'),
    ]

    for q in questions:
        text = q['question']
        answer = q['correct_answer']
        q_issues = []

        for pattern, description in review_patterns:
            if re.search(pattern, text, re.IGNORECASE) or re.search(pattern, answer, re.IGNORECASE):
                q_issues.append(description)

        if q_issues:
            issues.append({
                'id': q['id'],
                'question': text,
                'answer': answer,
                'review_reasons': q_issues
            })

    return issues

def generate_report(questions):
    """Generate comprehensive quality audit report."""
    print("=" * 80)
    print("DISNEY EXPANSION PACK QUALITY AUDIT REPORT")
    print("=" * 80)
    print(f"\nTotal questions analyzed: {len(questions)}\n")

    # Check all issues
    exact_dupes = check_exact_duplicates(questions)
    semantic_dupes = check_semantic_duplicates(questions)
    grammar = check_grammar_issues(questions)
    self_revealing = check_self_revealing(questions)
    confusing = check_confusing_wording(questions)
    verify_answers = check_answer_correctness(questions)

    # Categorize for report
    auto_fix = []
    flag_replacement = []
    needs_verification = []

    # Process grammar issues (mostly auto-fix)
    for issue in grammar:
        for sub_issue in issue['issues']:
            if sub_issue['category'] in ['double_space', 'missing_apostrophe', 'typos', 'spacing']:
                auto_fix.append({
                    'id': issue['id'],
                    'question': issue['question'],
                    'issue_type': 'Grammar/Typo',
                    'description': sub_issue['description'],
                    'fix': 'AUTO-FIX'
                })
            else:
                needs_verification.append({
                    'id': issue['id'],
                    'question': issue['question'],
                    'issue_type': 'Grammar',
                    'description': sub_issue['description']
                })

    # Exact duplicates - flag for replacement
    for dupe in exact_dupes:
        flag_replacement.append({
            'ids': dupe['ids'],
            'question': dupe['question'],
            'issue_type': 'Exact Duplicate',
            'description': f'{dupe["count"]} identical questions found',
            'action': 'Keep first, replace others with new questions'
        })

    # Semantic duplicates - flag for replacement
    for dupe in semantic_dupes:
        flag_replacement.append({
            'ids': [dupe['id1'], dupe['id2']],
            'question': f"Q1: {dupe['q1']}\nQ2: {dupe['q2']}",
            'issue_type': 'Semantic Duplicate',
            'description': f'{dupe["similarity"]:.0%} similar',
            'action': 'Keep one, replace the other'
        })

    # Self-revealing - needs verification
    for issue in self_revealing:
        needs_verification.append({
            'id': issue['id'],
            'question': issue['question'],
            'issue_type': 'Self-Revealing Answer',
            'description': f"Answer '{issue['answer']}' may appear in question - {issue['reason']}"
        })

    # Confusing wording - needs verification
    for issue in confusing:
        needs_verification.append({
            'id': issue['id'],
            'question': issue['question'],
            'issue_type': 'Confusing Wording',
            'description': ', '.join(issue['concerns'])
        })

    # Answer verification needed
    for issue in verify_answers:
        needs_verification.append({
            'id': issue['id'],
            'question': issue['question'],
            'issue_type': 'Verify Answer',
            'description': ', '.join(issue['review_reasons']),
            'answer': issue['answer']
        })

    # Print report sections
    print("\n" + "=" * 80)
    print("1. AUTO-FIX ISSUES")
    print("=" * 80)
    print(f"\nTotal auto-fix issues: {len(auto_fix)}\n")

    if auto_fix:
        for idx, item in enumerate(auto_fix, 1):
            print(f"{idx}. ID: {item['id']}")
            print(f"   Type: {item['issue_type']}")
            print(f"   Issue: {item['description']}")
            print(f"   Question: {item['question']}")
            print(f"   Action: {item['fix']}")
            print()
    else:
        print("No auto-fix issues found.\n")

    print("\n" + "=" * 80)
    print("2. FLAG FOR REPLACEMENT")
    print("=" * 80)
    print(f"\nTotal questions flagged for replacement: {len(flag_replacement)}\n")

    if flag_replacement:
        for idx, item in enumerate(flag_replacement, 1):
            print(f"{idx}. IDs: {', '.join(item['ids'])}")
            print(f"   Type: {item['issue_type']}")
            print(f"   Issue: {item['description']}")
            print(f"   Question(s): {item['question'][:200]}...")
            print(f"   Action: {item['action']}")
            print()
    else:
        print("No questions flagged for replacement.\n")

    print("\n" + "=" * 80)
    print("3. NEEDS VERIFICATION")
    print("=" * 80)
    print(f"\nTotal items needing verification: {len(needs_verification)}\n")

    if needs_verification:
        # Group by type for easier review
        by_type = defaultdict(list)
        for item in needs_verification:
            by_type[item['issue_type']].append(item)

        for issue_type, items in sorted(by_type.items()):
            print(f"\n--- {issue_type} ({len(items)} items) ---\n")
            for idx, item in enumerate(items, 1):
                print(f"{idx}. ID: {item['id']}")
                print(f"   Issue: {item['description']}")
                print(f"   Question: {item['question']}")
                if 'answer' in item:
                    print(f"   Answer: {item['answer']}")
                print()
    else:
        print("No items need verification.\n")

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total questions: {len(questions)}")
    print(f"Auto-fix issues: {len(auto_fix)}")
    print(f"Flagged for replacement: {len(flag_replacement)}")
    print(f"Needs verification: {len(needs_verification)}")
    print(f"Total issues found: {len(auto_fix) + len(flag_replacement) + len(needs_verification)}")
    print()

if __name__ == '__main__':
    filepath = '/home/user/fiztrivia/Fiz/Resources/Expansion Packs/expansion_disney.json'
    questions = load_questions(filepath)
    generate_report(questions)
