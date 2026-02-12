#!/usr/bin/env python3
"""
Comprehensive quality audit for the 4 newest expansion packs:
- LOTR (The Great Journey)
- Apple (Byte-Sized Brilliance)
- Friends (Central Perk Chronicles)
- Survivor (Torch & Tribe)
"""

import json
import re
from difflib import SequenceMatcher
from collections import defaultdict
import os

def load_questions(filepath):
    """Load questions from expansion pack JSON"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    all_questions = []

    # Combine free preview and paid questions
    if 'freePreviewQuestions' in data:
        all_questions.extend(data['freePreviewQuestions'])
    if 'paidQuestions' in data:
        all_questions.extend(data['paidQuestions'])

    return all_questions, data.get('packName', 'Unknown')

def similarity_ratio(str1, str2):
    """Calculate similarity ratio between two strings"""
    return SequenceMatcher(None, str1.lower(), str2.lower()).ratio()

def check_exact_duplicates(questions):
    """Find exact duplicate questions"""
    duplicates = []
    seen = {}

    for q in questions:
        question_text = q['question'].strip()
        if question_text in seen:
            duplicates.append({
                'type': 'exact_duplicate',
                'question_id': q['id'],
                'duplicate_of': seen[question_text],
                'question': question_text
            })
        else:
            seen[question_text] = q['id']

    return duplicates

def check_semantic_duplicates(questions):
    """Find semantic duplicates (>90% similar)"""
    duplicates = []

    for i, q1 in enumerate(questions):
        for q2 in questions[i+1:]:
            ratio = similarity_ratio(q1['question'], q2['question'])
            if ratio > 0.90:  # >90% similar
                duplicates.append({
                    'type': 'semantic_duplicate',
                    'question_id': q1['id'],
                    'duplicate_of': q2['id'],
                    'similarity': f"{ratio*100:.1f}%",
                    'question1': q1['question'],
                    'question2': q2['question']
                })

    return duplicates

def check_grammar_issues(questions):
    """Check for common grammar/typo issues"""
    issues = []

    grammar_patterns = [
        (r'\s\s+', 'double_space', 'Multiple spaces'),
        (r'\s[.?!]', 'space_before_punctuation', 'Space before punctuation'),
        (r'[.?!][a-zA-Z]', 'missing_space_after_punctuation', 'Missing space after punctuation'),
        (r'\b(a)\s+(hour|NBA|NFL|NHL|UFC|Apple|Elvish|Elf|Orc)\b', 'a_vs_an', 'Should use "an" instead of "a"'),
        (r'\b(an)\s+(one|university|European|user|hobbit)\b', 'an_vs_a', 'Should use "a" instead of "an"'),
        (r'[\w][?]', 'no_space_before_question', 'No space before question mark'),
    ]

    for q in questions:
        text = q['question']

        for pattern, issue_type, description in grammar_patterns:
            if re.search(pattern, text):
                issues.append({
                    'type': 'grammar',
                    'issue_type': issue_type,
                    'question_id': q['id'],
                    'question': text,
                    'description': description
                })

        # Check for common typos
        typo_checks = [
            ('teh', 'the'),
            ('wining', 'winning'),
            ('competetion', 'competition'),
            ('champoinship', 'championship'),
            ('occured', 'occurred'),
            ('recieve', 'receive'),
            ('seperate', 'separate'),
        ]

        for typo, correct in typo_checks:
            if re.search(r'\b' + typo + r'\b', text, re.IGNORECASE):
                issues.append({
                    'type': 'typo',
                    'issue_type': 'spelling',
                    'question_id': q['id'],
                    'question': text,
                    'description': f'Typo: "{typo}" should be "{correct}"'
                })

    return issues

def check_self_revealing(questions):
    """Check if answer appears in question text"""
    issues = []

    for q in questions:
        question_lower = q['question'].lower()
        correct_answer = q['correct_answer'].lower()

        # Check if answer is in question (ignoring common words)
        common_words = {'the', 'a', 'an', 'and', 'or', 'in', 'on', 'at', 'to', 'for', 'of', 'with',
                       'is', 'it', 'by', 'as', 'that', 'this', 'from', 'be', 'are', 'was', 'were'}

        # Skip if answer is too short or is a common word
        if correct_answer in common_words or len(correct_answer) <= 3:
            continue

        # Check if the full answer phrase appears in the question
        if correct_answer in question_lower:
            # Additional check: make sure it's not a false positive
            # (e.g., "Battle of Hoth" appearing in "What battle took place on Hoth?")
            # Allow if it's just a location/subject reference
            issues.append({
                'type': 'self_revealing',
                'question_id': q['id'],
                'question': q['question'],
                'answer': q['correct_answer'],
                'description': 'Answer appears in question text (may need review)'
            })

    return issues

def check_confusing_wording(questions):
    """Check for potentially confusing wording"""
    issues = []

    confusing_patterns = [
        (r'which of the following (is|are) not', 'double_negative', 'Double negative may be confusing'),
        (r'except', 'exception_question', 'Exception questions can be confusing'),
        (r'(all of the above|none of the above)', 'meta_option', 'Meta options in question text'),
    ]

    for q in questions:
        text = q['question']

        for pattern, issue_type, description in confusing_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                issues.append({
                    'type': 'confusing_wording',
                    'issue_type': issue_type,
                    'question_id': q['id'],
                    'question': text,
                    'description': description
                })

    return issues

def check_answer_options(questions):
    """Check answer options for issues"""
    issues = []

    for q in questions:
        options = q.get('options', [])
        correct_answer = q['correct_answer']

        # Check if correct answer is in options
        if correct_answer not in options:
            issues.append({
                'type': 'answer_not_in_options',
                'question_id': q['id'],
                'question': q['question'],
                'correct_answer': correct_answer,
                'options': options,
                'description': 'Correct answer not found in options'
            })

        # Check for duplicate options
        if len(options) != len(set(options)):
            issues.append({
                'type': 'duplicate_options',
                'question_id': q['id'],
                'question': q['question'],
                'options': options,
                'description': 'Duplicate answer options'
            })

        # Check if all options are provided (should be 4)
        if len(options) != 4:
            issues.append({
                'type': 'wrong_option_count',
                'question_id': q['id'],
                'question': q['question'],
                'options': options,
                'description': f'Expected 4 options, found {len(options)}'
            })

    return issues

def generate_report(questions, pack_name, output_file):
    """Generate comprehensive QA report"""
    report = []
    report.append("=" * 80)
    report.append(f"{pack_name.upper()} - QUALITY ASSURANCE AUDIT REPORT")
    report.append("=" * 80)
    report.append(f"\nTotal questions analyzed: {len(questions)}")
    report.append("")

    # Check for all issues
    exact_dupes = check_exact_duplicates(questions)
    semantic_dupes = check_semantic_duplicates(questions)
    grammar_issues = check_grammar_issues(questions)
    self_revealing = check_self_revealing(questions)
    confusing = check_confusing_wording(questions)
    answer_issues = check_answer_options(questions)

    # Category 1: AUTO-FIX (Clear typos/grammar)
    report.append("=" * 80)
    report.append("CATEGORY 1: AUTO-FIX (Clear typos/grammar)")
    report.append("=" * 80)

    auto_fix = [g for g in grammar_issues if g.get('issue_type') in ['typo', 'double_space', 'space_before_punctuation', 'spelling']]

    if auto_fix:
        for issue in auto_fix:
            report.append(f"\nQuestion ID: {issue['question_id']}")
            report.append(f"Issue: {issue['description']}")
            report.append(f"Question: {issue['question']}")
    else:
        report.append("\n✓ No auto-fix issues found!")

    report.append(f"\nTotal auto-fix issues: {len(auto_fix)}")

    # Category 2: FLAG FOR REPLACEMENT (Duplicates)
    report.append("\n" + "=" * 80)
    report.append("CATEGORY 2: FLAG FOR REPLACEMENT (Exact/Semantic Duplicates)")
    report.append("=" * 80)

    if exact_dupes:
        report.append("\n--- EXACT DUPLICATES ---")
        for dup in exact_dupes:
            report.append(f"\n⚠ Question ID: {dup['question_id']} (duplicate of {dup['duplicate_of']})")
            report.append(f"Question: {dup['question']}")

    if semantic_dupes:
        report.append("\n--- SEMANTIC DUPLICATES (>90% similar) ---")
        for dup in semantic_dupes:
            report.append(f"\n⚠ Question ID: {dup['question_id']} vs {dup['duplicate_of']} ({dup['similarity']} similar)")
            report.append(f"Q1: {dup['question1']}")
            report.append(f"Q2: {dup['question2']}")

    if not exact_dupes and not semantic_dupes:
        report.append("\n✓ No duplicates found!")

    report.append(f"\nTotal duplicates: {len(exact_dupes) + len(semantic_dupes)}")

    # Category 3: NEEDS VERIFICATION
    report.append("\n" + "=" * 80)
    report.append("CATEGORY 3: NEEDS VERIFICATION (Questionable accuracy/clarity)")
    report.append("=" * 80)

    if self_revealing:
        report.append("\n--- POTENTIAL SELF-REVEALING ANSWERS ---")
        report.append("(Note: Some may be false positives - manual review needed)")
        for issue in self_revealing:
            report.append(f"\n? Question ID: {issue['question_id']}")
            report.append(f"Question: {issue['question']}")
            report.append(f"Answer: {issue['answer']}")

    if confusing:
        report.append("\n--- CONFUSING WORDING ---")
        for issue in confusing:
            report.append(f"\n? Question ID: {issue['question_id']}")
            report.append(f"Issue: {issue['description']}")
            report.append(f"Question: {issue['question']}")

    if answer_issues:
        report.append("\n--- ANSWER OPTION ISSUES ---")
        for issue in answer_issues:
            report.append(f"\n⚠ Question ID: {issue['question_id']}")
            report.append(f"Issue: {issue['description']}")
            report.append(f"Question: {issue['question']}")
            if issue['type'] == 'answer_not_in_options':
                report.append(f"Correct Answer: {issue['correct_answer']}")
                report.append(f"Options: {issue['options']}")

    if not self_revealing and not confusing and not answer_issues:
        report.append("\n✓ No verification issues found!")

    report.append(f"\nTotal verification issues: {len(self_revealing) + len(confusing) + len(answer_issues)}")

    # Summary
    total_issues = len(auto_fix) + len(exact_dupes) + len(semantic_dupes) + len(self_revealing) + len(confusing) + len(answer_issues)
    quality_score = ((len(questions) - total_issues) / len(questions)) * 100 if len(questions) > 0 else 0

    report.append("\n" + "=" * 80)
    report.append("SUMMARY")
    report.append("=" * 80)
    report.append(f"Total questions: {len(questions)}")
    report.append(f"Auto-fix issues: {len(auto_fix)}")
    report.append(f"Duplicates: {len(exact_dupes) + len(semantic_dupes)}")
    report.append(f"Needs verification: {len(self_revealing) + len(confusing) + len(answer_issues)}")
    report.append(f"TOTAL ISSUES: {total_issues}")
    report.append(f"QUALITY SCORE: {quality_score:.1f}%")
    report.append("=" * 80)

    # Write to file and console
    report_text = "\n".join(report)
    with open(output_file, 'w') as f:
        f.write(report_text)

    print(report_text)
    print(f"\n✓ Report saved to: {output_file}\n")

    return {
        'total_questions': len(questions),
        'total_issues': total_issues,
        'quality_score': quality_score,
        'auto_fix': len(auto_fix),
        'duplicates': len(exact_dupes) + len(semantic_dupes),
        'verification': len(self_revealing) + len(confusing) + len(answer_issues)
    }

def main():
    """Audit all 4 newest expansion packs"""
    packs = [
        ('Fiz/Resources/Expansion Packs/expansion_lotr.json', 'lotr_audit_report.txt'),
        ('Fiz/Resources/Expansion Packs/expansion_apple.json', 'apple_audit_report.txt'),
        ('Fiz/Resources/Expansion Packs/expansion_friends.json', 'friends_audit_report.txt'),
        ('Fiz/Resources/Expansion Packs/expansion_survivor.json', 'survivor_audit_report.txt'),
    ]

    print("\n" + "=" * 80)
    print("COMPREHENSIVE AUDIT OF 4 NEWEST EXPANSION PACKS")
    print("=" * 80)
    print()

    results = []

    for filepath, output_file in packs:
        if not os.path.exists(filepath):
            print(f"⚠ Warning: {filepath} not found, skipping...")
            continue

        questions, pack_name = load_questions(filepath)
        result = generate_report(questions, pack_name, output_file)
        results.append((pack_name, result))
        print("\n")

    # Overall summary
    print("=" * 80)
    print("OVERALL SUMMARY - ALL 4 PACKS")
    print("=" * 80)

    for pack_name, result in results:
        print(f"\n{pack_name}:")
        print(f"  Questions: {result['total_questions']}")
        print(f"  Issues: {result['total_issues']}")
        print(f"  Quality Score: {result['quality_score']:.1f}%")
        print(f"  - Auto-fix: {result['auto_fix']}")
        print(f"  - Duplicates: {result['duplicates']}")
        print(f"  - Needs verification: {result['verification']}")

    total_qs = sum(r['total_questions'] for _, r in results)
    total_issues = sum(r['total_issues'] for _, r in results)
    avg_quality = sum(r['quality_score'] for _, r in results) / len(results) if results else 0

    print(f"\n{'─' * 80}")
    print(f"TOTALS:")
    print(f"  Total Questions: {total_qs}")
    print(f"  Total Issues: {total_issues}")
    print(f"  Average Quality Score: {avg_quality:.1f}%")
    print("=" * 80)

if __name__ == '__main__':
    main()
