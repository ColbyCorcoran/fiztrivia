#!/usr/bin/env python3
"""
Comprehensive quality audit for main questions.json file
"""

import json
import re
from difflib import SequenceMatcher
from collections import defaultdict

def load_questions(filepath):
    """Load questions from main questions.json"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # questions.json has structure: {"categories": {"CategoryName": [questions]}}
    all_questions = []

    if 'categories' in data:
        for category_name, questions in data['categories'].items():
            all_questions.extend(questions)
    else:
        # Fallback if it's a different structure
        all_questions = data if isinstance(data, list) else []

    return all_questions

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

def check_semantic_duplicates(questions, threshold=0.90):
    """Find semantic duplicates (>threshold% similar)"""
    duplicates = []

    for i, q1 in enumerate(questions):
        for q2 in questions[i+1:]:
            ratio = similarity_ratio(q1['question'], q2['question'])
            if ratio > threshold:
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
        (r'\b(a)\s+(hour|NBA|NFL|NHL|UFC|Apple|Elvish|Elf|Orc|island)\b', 'a_vs_an', 'Should use "an" instead of "a"'),
        (r'\b(an)\s+(one|university|European|user|hobbit|unicorn)\b', 'an_vs_a', 'Should use "a" instead of "an"'),
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
            issues.append({
                'type': 'self_revealing',
                'question_id': q['id'],
                'question': q['question'],
                'answer': q['correct_answer'],
                'description': 'Answer appears in question text (may need review)'
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

def generate_report(questions, output_file):
    """Generate comprehensive QA report"""
    report = []
    report.append("=" * 80)
    report.append("MAIN QUESTIONS.JSON - QUALITY ASSURANCE AUDIT REPORT")
    report.append("=" * 80)
    report.append(f"\nTotal questions analyzed: {len(questions)}")

    # Analyze by category
    categories = defaultdict(int)
    for q in questions:
        categories[q.get('category', 'Unknown')] += 1

    report.append("\nQuestions by category:")
    for cat, count in sorted(categories.items()):
        report.append(f"  {cat}: {count}")

    # Analyze by difficulty
    difficulties = defaultdict(int)
    for q in questions:
        difficulties[q.get('difficulty', 'Unknown')] += 1

    report.append("\nQuestions by difficulty:")
    for diff, count in sorted(difficulties.items()):
        pct = (count / len(questions)) * 100
        report.append(f"  {diff}: {count} ({pct:.1f}%)")

    report.append("")

    # Check for all issues
    print("Checking exact duplicates...")
    exact_dupes = check_exact_duplicates(questions)

    print("Checking semantic duplicates (this may take a while)...")
    semantic_dupes = check_semantic_duplicates(questions)

    print("Checking grammar issues...")
    grammar_issues = check_grammar_issues(questions)

    print("Checking self-revealing answers...")
    self_revealing = check_self_revealing(questions)

    print("Checking answer options...")
    answer_issues = check_answer_options(questions)

    # Category 1: AUTO-FIX (Clear typos/grammar)
    report.append("=" * 80)
    report.append("CATEGORY 1: AUTO-FIX (Clear typos/grammar)")
    report.append("=" * 80)

    auto_fix = [g for g in grammar_issues if g.get('issue_type') in ['typo', 'double_space', 'space_before_punctuation', 'spelling']]

    if auto_fix:
        for issue in auto_fix[:20]:  # Show first 20
            report.append(f"\nQuestion ID: {issue['question_id']}")
            report.append(f"Issue: {issue['description']}")
            report.append(f"Question: {issue['question']}")
        if len(auto_fix) > 20:
            report.append(f"\n... and {len(auto_fix) - 20} more")
    else:
        report.append("\n✓ No auto-fix issues found!")

    report.append(f"\nTotal auto-fix issues: {len(auto_fix)}")

    # Category 2: FLAG FOR REPLACEMENT (Duplicates)
    report.append("\n" + "=" * 80)
    report.append("CATEGORY 2: FLAG FOR REPLACEMENT (Exact/Semantic Duplicates)")
    report.append("=" * 80)

    if exact_dupes:
        report.append("\n--- EXACT DUPLICATES ---")
        for dup in exact_dupes[:20]:  # Show first 20
            report.append(f"\n⚠ Question ID: {dup['question_id']} (duplicate of {dup['duplicate_of']})")
            report.append(f"Question: {dup['question']}")
        if len(exact_dupes) > 20:
            report.append(f"\n... and {len(exact_dupes) - 20} more")

    if semantic_dupes:
        report.append("\n--- SEMANTIC DUPLICATES (>90% similar) ---")
        report.append("(Showing first 20 - many may be intentional)")
        for dup in semantic_dupes[:20]:  # Show first 20
            report.append(f"\n? Question ID: {dup['question_id']} vs {dup['duplicate_of']} ({dup['similarity']} similar)")
            report.append(f"Q1: {dup['question1']}")
            report.append(f"Q2: {dup['question2']}")
        if len(semantic_dupes) > 20:
            report.append(f"\n... and {len(semantic_dupes) - 20} more")

    if not exact_dupes and not semantic_dupes:
        report.append("\n✓ No duplicates found!")

    report.append(f"\nTotal duplicates: {len(exact_dupes)} exact, {len(semantic_dupes)} semantic")

    # Category 3: NEEDS VERIFICATION
    report.append("\n" + "=" * 80)
    report.append("CATEGORY 3: NEEDS VERIFICATION (Questionable accuracy/clarity)")
    report.append("=" * 80)

    if self_revealing:
        report.append("\n--- POTENTIAL SELF-REVEALING ANSWERS ---")
        report.append("(Note: Many may be false positives - manual review needed)")
        report.append("(Showing first 20)")
        for issue in self_revealing[:20]:
            report.append(f"\n? Question ID: {issue['question_id']}")
            report.append(f"Question: {issue['question']}")
            report.append(f"Answer: {issue['answer']}")
        if len(self_revealing) > 20:
            report.append(f"\n... and {len(self_revealing) - 20} more")

    if answer_issues:
        report.append("\n--- ANSWER OPTION ISSUES ---")
        for issue in answer_issues[:20]:  # Show first 20
            report.append(f"\n⚠ Question ID: {issue['question_id']}")
            report.append(f"Issue: {issue['description']}")
            report.append(f"Question: {issue['question'][:60]}...")
            if issue['type'] == 'answer_not_in_options':
                report.append(f"Correct Answer: {issue['correct_answer']}")
                report.append(f"Options: {issue['options']}")
            elif issue['type'] == 'duplicate_options':
                report.append(f"Options: {issue['options']}")
        if len(answer_issues) > 20:
            report.append(f"\n... and {len(answer_issues) - 20} more")

    if not self_revealing and not answer_issues:
        report.append("\n✓ No verification issues found!")

    report.append(f"\nTotal verification issues: {len(self_revealing) + len(answer_issues)}")

    # Summary
    total_issues = len(auto_fix) + len(exact_dupes) + len(semantic_dupes) + len(self_revealing) + len(answer_issues)
    quality_score = ((len(questions) - (len(exact_dupes) + len(auto_fix) + len(answer_issues))) / len(questions)) * 100 if len(questions) > 0 else 0

    report.append("\n" + "=" * 80)
    report.append("SUMMARY")
    report.append("=" * 80)
    report.append(f"Total questions: {len(questions)}")
    report.append(f"Auto-fix issues: {len(auto_fix)}")
    report.append(f"Exact duplicates: {len(exact_dupes)}")
    report.append(f"Semantic duplicates: {len(semantic_dupes)} (may be intentional)")
    report.append(f"Self-revealing (potential): {len(self_revealing)}")
    report.append(f"Answer option issues: {len(answer_issues)}")
    report.append(f"TOTAL CRITICAL ISSUES: {len(auto_fix) + len(exact_dupes) + len(answer_issues)}")
    report.append(f"QUALITY SCORE: {quality_score:.1f}% (excluding semantic duplicates)")
    report.append("=" * 80)

    # Write to file and console
    report_text = "\n".join(report)
    with open(output_file, 'w') as f:
        f.write(report_text)

    print(report_text)
    print(f"\n✓ Report saved to: {output_file}\n")

    return {
        'total_questions': len(questions),
        'auto_fix': len(auto_fix),
        'exact_duplicates': len(exact_dupes),
        'semantic_duplicates': len(semantic_dupes),
        'self_revealing': len(self_revealing),
        'answer_issues': len(answer_issues),
        'total_critical': len(auto_fix) + len(exact_dupes) + len(answer_issues),
        'quality_score': quality_score
    }

def main():
    """Audit main questions.json file"""
    filepath = 'Fiz/Resources/questions.json'
    output_file = 'main_questions_audit_report.txt'

    print("Loading questions...")
    questions = load_questions(filepath)

    print(f"Loaded {len(questions)} questions\n")

    result = generate_report(questions, output_file)

    print("\n" + "="*80)
    print("AUDIT COMPLETE")
    print("="*80)
    print(f"\nCritical issues found: {result['total_critical']}")
    print(f"Quality score: {result['quality_score']:.1f}%")

if __name__ == '__main__':
    main()
