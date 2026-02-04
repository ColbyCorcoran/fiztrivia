#!/usr/bin/env python3
"""
Pokémon Trivia Pack QA Audit Script
Checks for duplicates, grammar issues, incorrect answers, and other quality problems
"""

import json
import re
from collections import defaultdict
from difflib import SequenceMatcher

def load_pokemon_pack(filepath):
    """Load the Pokémon expansion pack JSON"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def similarity_ratio(a, b):
    """Calculate similarity between two strings"""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def check_exact_duplicates(questions):
    """Find exact duplicate questions"""
    seen = {}
    duplicates = []

    for q in questions:
        question_text = q['question'].lower().strip()
        if question_text in seen:
            duplicates.append({
                'type': 'exact_duplicate',
                'question1_id': seen[question_text]['id'],
                'question2_id': q['id'],
                'question': q['question']
            })
        else:
            seen[question_text] = q

    return duplicates

def check_semantic_duplicates(questions, threshold=0.85):
    """Find semantically similar questions (likely duplicates with rewording)"""
    duplicates = []
    checked = set()

    for i, q1 in enumerate(questions):
        for j, q2 in enumerate(questions[i+1:], i+1):
            pair_key = tuple(sorted([q1['id'], q2['id']]))
            if pair_key in checked:
                continue
            checked.add(pair_key)

            similarity = similarity_ratio(q1['question'], q2['question'])
            if similarity >= threshold:
                duplicates.append({
                    'type': 'semantic_duplicate',
                    'question1_id': q1['id'],
                    'question2_id': q2['id'],
                    'question1': q1['question'],
                    'question2': q2['question'],
                    'similarity': f"{similarity:.2%}"
                })

    return duplicates

def check_grammar_issues(questions):
    """Check for common grammar and typo issues"""
    issues = []

    grammar_patterns = [
        (r'\s{2,}', 'Multiple consecutive spaces'),
        (r'[a-z]\.[A-Z]', 'Missing space after period'),
        (r'\?[a-zA-Z]', 'Missing space after question mark'),
        (r',[a-zA-Z]', 'Missing space after comma'),
        (r'\b(a)\s+(apple|orange|evolution|electric|ice)\b', 'Article mismatch (should be "an")'),
        (r'\b(an)\s+(water|fire|grass|rock|ground|bug|normal|fighting|poison|psychic|dragon|dark|steel|fairy|flying)\b', 'Article mismatch (should be "a")'),
        (r'\bPokemon\b', 'Should be "Pokémon" with accent'),
        (r'\bPokemon\'s\b', 'Should be "Pokémon\'s" with accent'),
    ]

    for q in questions:
        question_text = q['question']

        # Check for missing question mark
        if not question_text.endswith('?'):
            issues.append({
                'type': 'grammar',
                'id': q['id'],
                'question': question_text,
                'issue': 'Missing question mark at end',
                'severity': 'high'
            })

        # Check grammar patterns
        for pattern, description in grammar_patterns:
            if re.search(pattern, question_text):
                issues.append({
                    'type': 'grammar',
                    'id': q['id'],
                    'question': question_text,
                    'issue': description,
                    'severity': 'medium'
                })

        # Check options for grammar issues
        for option in q['options']:
            if '  ' in option:
                issues.append({
                    'type': 'grammar',
                    'id': q['id'],
                    'question': question_text,
                    'issue': f'Multiple spaces in option: "{option}"',
                    'severity': 'medium'
                })

    return issues

def check_self_revealing(questions):
    """Check if answer appears in question text"""
    issues = []

    for q in questions:
        question_lower = q['question'].lower()
        answer_lower = q['correct_answer'].lower()

        # Simple check: if exact answer is in question
        if answer_lower in question_lower:
            # Exclude cases where it's a reasonable inclusion (e.g., "Which of these...")
            if not any(phrase in question_lower for phrase in ['which of these', 'which of the following', 'excluding']):
                issues.append({
                    'type': 'self_revealing',
                    'id': q['id'],
                    'question': q['question'],
                    'answer': q['correct_answer'],
                    'issue': f'Answer "{q["correct_answer"]}" appears in question text'
                })

    return issues

def check_confusing_wording(questions):
    """Check for potentially confusing or ambiguous wording"""
    issues = []

    confusing_patterns = [
        (r'\b(not|never|except|excluding)\b.*\b(not|never|except|excluding)\b', 'Double negative'),
        (r'\bWhich of these\b.*\?.*\?', 'Multiple question marks'),
    ]

    for q in questions:
        question_text = q['question']

        for pattern, description in confusing_patterns:
            if re.search(pattern, question_text, re.IGNORECASE):
                issues.append({
                    'type': 'confusing',
                    'id': q['id'],
                    'question': question_text,
                    'issue': description
                })

        # Check if question is too long (might be confusing)
        if len(question_text) > 200:
            issues.append({
                'type': 'confusing',
                'id': q['id'],
                'question': question_text,
                'issue': f'Very long question ({len(question_text)} characters)'
            })

    return issues

def analyze_pack(filepath):
    """Run all QA checks on the pack"""
    print(f"Loading Pokémon pack from {filepath}...")
    pack = load_pokemon_pack(filepath)

    # Combine all questions
    all_questions = pack.get('freePreviewQuestions', []) + pack.get('paidQuestions', [])
    print(f"Total questions: {len(all_questions)}")

    print("\n" + "="*80)
    print("POKÉMON TRIVIA PACK - QA AUDIT REPORT")
    print("="*80)

    # Check exact duplicates
    print("\n1. Checking for exact duplicates...")
    exact_dupes = check_exact_duplicates(all_questions)

    # Check semantic duplicates
    print("2. Checking for semantic duplicates...")
    semantic_dupes = check_semantic_duplicates(all_questions)

    # Check grammar issues
    print("3. Checking for grammar issues...")
    grammar_issues = check_grammar_issues(all_questions)

    # Check self-revealing
    print("4. Checking for self-revealing answers...")
    self_revealing = check_self_revealing(all_questions)

    # Check confusing wording
    print("5. Checking for confusing wording...")
    confusing = check_confusing_wording(all_questions)

    # Categorize findings
    auto_fix = []
    flag_for_replacement = []
    needs_verification = []

    # Grammar issues are auto-fix
    for issue in grammar_issues:
        auto_fix.append(issue)

    # Exact and semantic duplicates are flagged for replacement
    for dupe in exact_dupes:
        flag_for_replacement.append(dupe)

    for dupe in semantic_dupes:
        flag_for_replacement.append(dupe)

    # Self-revealing and confusing need verification
    for issue in self_revealing:
        needs_verification.append(issue)

    for issue in confusing:
        needs_verification.append(issue)

    # Print report
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total Issues Found: {len(auto_fix) + len(flag_for_replacement) + len(needs_verification)}")
    print(f"  - AUTO-FIX (grammar/typos): {len(auto_fix)}")
    print(f"  - FLAG FOR REPLACEMENT (duplicates): {len(flag_for_replacement)}")
    print(f"  - NEEDS VERIFICATION (accuracy/clarity): {len(needs_verification)}")

    # Detailed reports
    if auto_fix:
        print("\n" + "="*80)
        print("AUTO-FIX: Grammar and Typo Issues")
        print("="*80)
        for i, issue in enumerate(auto_fix, 1):
            print(f"\n{i}. ID: {issue['id']}")
            print(f"   Issue: {issue['issue']}")
            print(f"   Question: {issue['question']}")

    if flag_for_replacement:
        print("\n" + "="*80)
        print("FLAG FOR REPLACEMENT: Duplicates")
        print("="*80)
        for i, issue in enumerate(flag_for_replacement, 1):
            print(f"\n{i}. Type: {issue['type']}")
            if 'question1_id' in issue:
                print(f"   ID 1: {issue['question1_id']}")
                print(f"   ID 2: {issue['question2_id']}")
                if 'question1' in issue:
                    print(f"   Q1: {issue['question1']}")
                    print(f"   Q2: {issue['question2']}")
                    print(f"   Similarity: {issue.get('similarity', 'N/A')}")
                else:
                    print(f"   Question: {issue['question']}")

    if needs_verification:
        print("\n" + "="*80)
        print("NEEDS VERIFICATION: Accuracy and Clarity Issues")
        print("="*80)
        for i, issue in enumerate(needs_verification, 1):
            print(f"\n{i}. ID: {issue['id']}")
            print(f"   Type: {issue['type']}")
            print(f"   Issue: {issue['issue']}")
            print(f"   Question: {issue['question']}")
            if 'answer' in issue:
                print(f"   Answer: {issue['answer']}")

    print("\n" + "="*80)
    print("AUDIT COMPLETE")
    print("="*80)

    return {
        'auto_fix': auto_fix,
        'flag_for_replacement': flag_for_replacement,
        'needs_verification': needs_verification
    }

if __name__ == '__main__':
    filepath = '/home/user/fiztrivia/Fiz/Resources/Expansion Packs/expansion_pokemon.json'
    results = analyze_pack(filepath)
