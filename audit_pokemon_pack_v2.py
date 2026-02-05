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

    # Filter out "evolved form" questions - these are template questions about different Pokémon
    evolution_questions = []
    other_questions = []

    for q in questions:
        if "evolved form" in q['question'].lower() or "evolve into" in q['question'].lower():
            evolution_questions.append(q)
        else:
            other_questions.append(q)

    # Only check non-evolution questions for semantic duplicates
    for i, q1 in enumerate(other_questions):
        for j, q2 in enumerate(other_questions[i+1:], i+1):
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
        (r'\b(a)\s+(apple|orange|evolution|electric|ice|ability|attack|item|episode)\b', 'Article mismatch (should be "an")'),
        (r'\b(an)\s+(water|fire|grass|rock|ground|bug|normal|fighting|poison|psychic|dragon|dark|steel|fairy|flying|ghost|type|move|region|gym|pokemon|trainer)\b', 'Article mismatch (should be "a")'),
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
            # Exclude cases where it's a reasonable inclusion
            if not any(phrase in question_lower for phrase in [
                'which of these', 'which of the following', 'excluding',
                'what type', 'which type', 'what color', 'which color',
                'called', 'named', 'known as'
            ]):
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
        (r'\?.*\?', 'Multiple question marks'),
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

def analyze_pack(filepath, output_file):
    """Run all QA checks on the pack"""
    pack = load_pokemon_pack(filepath)

    # Combine all questions
    all_questions = pack.get('freePreviewQuestions', []) + pack.get('paidQuestions', [])

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Loading Pokémon pack from {filepath}...\n")
        f.write(f"Total questions: {len(all_questions)}\n")

        f.write("\n" + "="*80 + "\n")
        f.write("POKÉMON TRIVIA PACK - QA AUDIT REPORT\n")
        f.write("="*80 + "\n")

        # Check exact duplicates
        f.write("\n1. Checking for exact duplicates...\n")
        exact_dupes = check_exact_duplicates(all_questions)

        # Check semantic duplicates
        f.write("2. Checking for semantic duplicates...\n")
        semantic_dupes = check_semantic_duplicates(all_questions)

        # Check grammar issues
        f.write("3. Checking for grammar issues...\n")
        grammar_issues = check_grammar_issues(all_questions)

        # Check self-revealing
        f.write("4. Checking for self-revealing answers...\n")
        self_revealing = check_self_revealing(all_questions)

        # Check confusing wording
        f.write("5. Checking for confusing wording...\n")
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
        f.write("\n" + "="*80 + "\n")
        f.write("SUMMARY\n")
        f.write("="*80 + "\n")
        f.write(f"Total Issues Found: {len(auto_fix) + len(flag_for_replacement) + len(needs_verification)}\n")
        f.write(f"  - AUTO-FIX (grammar/typos): {len(auto_fix)}\n")
        f.write(f"  - FLAG FOR REPLACEMENT (duplicates): {len(flag_for_replacement)}\n")
        f.write(f"  - NEEDS VERIFICATION (accuracy/clarity): {len(needs_verification)}\n")

        # Detailed reports
        if auto_fix:
            f.write("\n" + "="*80 + "\n")
            f.write("AUTO-FIX: Grammar and Typo Issues\n")
            f.write("="*80 + "\n")
            for i, issue in enumerate(auto_fix, 1):
                f.write(f"\n{i}. ID: {issue['id']}\n")
                f.write(f"   Issue: {issue['issue']}\n")
                f.write(f"   Question: {issue['question']}\n")

        if flag_for_replacement:
            f.write("\n" + "="*80 + "\n")
            f.write("FLAG FOR REPLACEMENT: Duplicates\n")
            f.write("="*80 + "\n")
            for i, issue in enumerate(flag_for_replacement, 1):
                f.write(f"\n{i}. Type: {issue['type']}\n")
                if 'question1_id' in issue:
                    f.write(f"   ID 1: {issue['question1_id']}\n")
                    f.write(f"   ID 2: {issue['question2_id']}\n")
                    if 'question1' in issue:
                        f.write(f"   Q1: {issue['question1']}\n")
                        f.write(f"   Q2: {issue['question2']}\n")
                        f.write(f"   Similarity: {issue.get('similarity', 'N/A')}\n")
                    else:
                        f.write(f"   Question: {issue['question']}\n")

        if needs_verification:
            f.write("\n" + "="*80 + "\n")
            f.write("NEEDS VERIFICATION: Accuracy and Clarity Issues\n")
            f.write("="*80 + "\n")
            for i, issue in enumerate(needs_verification, 1):
                f.write(f"\n{i}. ID: {issue['id']}\n")
                f.write(f"   Type: {issue['type']}\n")
                f.write(f"   Issue: {issue['issue']}\n")
                f.write(f"   Question: {issue['question']}\n")
                if 'answer' in issue:
                    f.write(f"   Answer: {issue['answer']}\n")

        f.write("\n" + "="*80 + "\n")
        f.write("AUDIT COMPLETE\n")
        f.write("="*80 + "\n")

    return {
        'auto_fix': auto_fix,
        'flag_for_replacement': flag_for_replacement,
        'needs_verification': needs_verification
    }

if __name__ == '__main__':
    filepath = '/home/user/fiztrivia/Fiz/Resources/Expansion Packs/expansion_pokemon.json'
    output_file = '/home/user/fiztrivia/pokemon_pack_audit_report.txt'
    results = analyze_pack(filepath, output_file)
    print(f"Report saved to: {output_file}")
    print(f"\nSummary:")
    print(f"  - AUTO-FIX: {len(results['auto_fix'])}")
    print(f"  - FLAG FOR REPLACEMENT: {len(results['flag_for_replacement'])}")
    print(f"  - NEEDS VERIFICATION: {len(results['needs_verification'])}")
