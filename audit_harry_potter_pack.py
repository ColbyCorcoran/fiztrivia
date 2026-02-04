#!/usr/bin/env python3
"""
Quality Assurance Audit for Harry Potter Expansion Pack
Checks for duplicates, grammar issues, incorrect answers, and other quality problems
"""

import json
from collections import defaultdict
from difflib import SequenceMatcher

def load_pack(filepath):
    """Load the expansion pack JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def similarity_ratio(a, b):
    """Calculate similarity between two strings"""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def check_exact_duplicates(questions):
    """Find exact duplicate questions"""
    duplicates = []
    seen = {}

    for q in questions:
        question_text = q['question'].strip()
        if question_text in seen:
            duplicates.append({
                'type': 'EXACT_DUPLICATE',
                'question_id': q['id'],
                'duplicate_of': seen[question_text],
                'question': question_text,
                'subtopic': q.get('subtopic', 'N/A')
            })
        else:
            seen[question_text] = q['id']

    return duplicates

def check_semantic_duplicates(questions, threshold=0.85):
    """Find semantic duplicates (similar questions about same topic)"""
    duplicates = []

    for i, q1 in enumerate(questions):
        for q2 in questions[i+1:]:
            ratio = similarity_ratio(q1['question'], q2['question'])
            if ratio >= threshold:
                # Additional check: are the correct answers similar?
                answer_ratio = similarity_ratio(q1['correct_answer'], q2['correct_answer'])
                if answer_ratio > 0.7 or ratio > 0.9:
                    duplicates.append({
                        'type': 'SEMANTIC_DUPLICATE',
                        'question_id_1': q1['id'],
                        'question_id_2': q2['id'],
                        'question_1': q1['question'],
                        'question_2': q2['question'],
                        'similarity': f"{ratio:.2%}",
                        'answer_similarity': f"{answer_ratio:.2%}",
                        'subtopic_1': q1.get('subtopic', 'N/A'),
                        'subtopic_2': q2.get('subtopic', 'N/A')
                    })

    return duplicates

def check_grammar_issues(questions):
    """Check for common grammar issues"""
    issues = []

    grammar_patterns = [
        ('  ', 'double space'),
        (' ?', 'space before question mark'),
        (' .', 'space before period'),
        ('..', 'double period'),
        ('??', 'double question mark'),
        (' ,', 'space before comma'),
    ]

    for q in questions:
        text = q['question']

        # Check for grammar patterns
        for pattern, issue_type in grammar_patterns:
            if pattern in text:
                issues.append({
                    'type': 'GRAMMAR',
                    'issue': issue_type,
                    'question_id': q['id'],
                    'question': text,
                    'subtopic': q.get('subtopic', 'N/A')
                })

        # Check if question ends with ?
        if not text.strip().endswith('?'):
            issues.append({
                'type': 'GRAMMAR',
                'issue': 'missing question mark',
                'question_id': q['id'],
                'question': text,
                'subtopic': q.get('subtopic', 'N/A')
            })

        # Check for lowercase start
        if text and text[0].islower():
            issues.append({
                'type': 'GRAMMAR',
                'issue': 'lowercase start',
                'question_id': q['id'],
                'question': text,
                'subtopic': q.get('subtopic', 'N/A')
            })

    return issues

def check_self_revealing(questions):
    """Check if answer appears in question text"""
    issues = []

    for q in questions:
        question_lower = q['question'].lower()
        answer_lower = q['correct_answer'].lower()

        # Skip single word answers or very short answers
        if len(answer_lower) < 4:
            continue

        if answer_lower in question_lower:
            issues.append({
                'type': 'SELF_REVEALING',
                'question_id': q['id'],
                'question': q['question'],
                'answer': q['correct_answer'],
                'subtopic': q.get('subtopic', 'N/A')
            })

    return issues

def check_typos_and_common_errors(questions):
    """Check for common typos and errors"""
    issues = []

    # Common typos in Harry Potter context
    typo_patterns = [
        ('harry potter', 'Harry Potter'),
        ('hogwarts', 'Hogwarts'),
        ('gryffindor', 'Gryffindor'),
        ('slytherin', 'Slytherin'),
        ('hufflepuff', 'Hufflepuff'),
        ('ravenclaw', 'Ravenclaw'),
        ('voldemort', 'Voldemort'),
        ('dumbledore', 'Dumbledore'),
        ('hermione', 'Hermione'),
        ('ron weasley', 'Ron Weasley'),
        ('draco malfoy', 'Draco Malfoy'),
    ]

    for q in questions:
        text = q['question']

        # Check for common capitalization issues (only if lowercase version exists)
        for wrong, correct in typo_patterns:
            if wrong in text and correct not in text:
                # Make sure it's actually wrong (lowercase when it should be capitalized)
                if wrong in text.lower() and text != text.lower():
                    continue  # Skip if entire text is lowercase
                issues.append({
                    'type': 'CAPITALIZATION',
                    'issue': f'"{wrong}" should be "{correct}"',
                    'question_id': q['id'],
                    'question': text,
                    'subtopic': q.get('subtopic', 'N/A')
                })

    return issues

def check_question_quality(questions):
    """Check for confusing or poorly worded questions"""
    issues = []

    for q in questions:
        text = q['question']

        # Check for very short questions (might be incomplete)
        if len(text.strip()) < 10:
            issues.append({
                'type': 'QUALITY',
                'issue': 'very short question',
                'question_id': q['id'],
                'question': text,
                'subtopic': q.get('subtopic', 'N/A')
            })

        # Check for very long questions (might be confusing)
        if len(text) > 250:
            issues.append({
                'type': 'QUALITY',
                'issue': 'very long question',
                'question_id': q['id'],
                'question': text,
                'subtopic': q.get('subtopic', 'N/A')
            })

        # Check for multiple question marks
        if text.count('?') > 1:
            issues.append({
                'type': 'QUALITY',
                'issue': 'multiple questions in one',
                'question_id': q['id'],
                'question': text,
                'subtopic': q.get('subtopic', 'N/A')
            })

    return issues

def categorize_issues(all_issues):
    """Categorize issues into AUTO-FIX, FLAG FOR REPLACEMENT, and NEEDS VERIFICATION"""
    auto_fix = []
    flag_for_replacement = []
    needs_verification = []

    for issue in all_issues:
        issue_type = issue['type']

        if issue_type in ['EXACT_DUPLICATE', 'SEMANTIC_DUPLICATE']:
            flag_for_replacement.append(issue)
        elif issue_type == 'GRAMMAR':
            if issue['issue'] in ['double space', 'space before question mark', 'space before period',
                                  'space before comma', 'double period', 'double question mark']:
                auto_fix.append(issue)
            else:
                needs_verification.append(issue)
        elif issue_type == 'CAPITALIZATION':
            auto_fix.append(issue)
        elif issue_type == 'SELF_REVEALING':
            needs_verification.append(issue)
        elif issue_type == 'QUALITY':
            needs_verification.append(issue)
        else:
            needs_verification.append(issue)

    return auto_fix, flag_for_replacement, needs_verification

def generate_report(pack_data, auto_fix, flag_for_replacement, needs_verification):
    """Generate the quality audit report"""
    report = []
    report.append("=" * 80)
    report.append("HARRY POTTER EXPANSION PACK - QUALITY AUDIT REPORT")
    report.append("=" * 80)
    report.append("")

    # Get all questions (free + paid)
    all_questions = pack_data.get('freePreviewQuestions', []) + pack_data.get('paidQuestions', [])
    report.append(f"Total Questions: {len(all_questions)}")
    report.append(f"Free Preview: {len(pack_data.get('freePreviewQuestions', []))}")
    report.append(f"Paid Questions: {len(pack_data.get('paidQuestions', []))}")
    report.append("")

    total_issues = len(auto_fix) + len(flag_for_replacement) + len(needs_verification)
    report.append(f"Total Issues Found: {total_issues}")
    report.append(f"  - Auto-Fix: {len(auto_fix)}")
    report.append(f"  - Flag for Replacement: {len(flag_for_replacement)}")
    report.append(f"  - Needs Verification: {len(needs_verification)}")
    report.append("")
    report.append("=" * 80)

    # AUTO-FIX section
    if auto_fix:
        report.append("")
        report.append("1. AUTO-FIX ISSUES")
        report.append("=" * 80)
        report.append("These are clear typos/grammar issues that can be automatically fixed.")
        report.append("")

        for i, issue in enumerate(auto_fix, 1):
            report.append(f"{i}. [{issue['type']}] {issue.get('issue', '')}")
            report.append(f"   ID: {issue['question_id']}")
            report.append(f"   Subtopic: {issue.get('subtopic', 'N/A')}")
            report.append(f"   Question: {issue['question']}")
            report.append("")
    else:
        report.append("")
        report.append("1. AUTO-FIX ISSUES")
        report.append("=" * 80)
        report.append("No auto-fix issues found!")
        report.append("")

    # FLAG FOR REPLACEMENT section
    if flag_for_replacement:
        report.append("")
        report.append("2. FLAG FOR REPLACEMENT")
        report.append("=" * 80)
        report.append("These are exact or semantic duplicates that should be replaced.")
        report.append("")

        for i, issue in enumerate(flag_for_replacement, 1):
            if issue['type'] == 'EXACT_DUPLICATE':
                report.append(f"{i}. [EXACT DUPLICATE]")
                report.append(f"   ID: {issue['question_id']} (duplicate of {issue['duplicate_of']})")
                report.append(f"   Subtopic: {issue['subtopic']}")
                report.append(f"   Question: {issue['question']}")
            else:  # SEMANTIC_DUPLICATE
                report.append(f"{i}. [SEMANTIC DUPLICATE] (Similarity: {issue['similarity']})")
                report.append(f"   ID 1: {issue['question_id_1']} | Subtopic: {issue['subtopic_1']}")
                report.append(f"   Question 1: {issue['question_1']}")
                report.append(f"   ID 2: {issue['question_id_2']} | Subtopic: {issue['subtopic_2']}")
                report.append(f"   Question 2: {issue['question_2']}")
                report.append(f"   Answer Similarity: {issue['answer_similarity']}")
            report.append("")
    else:
        report.append("")
        report.append("2. FLAG FOR REPLACEMENT")
        report.append("=" * 80)
        report.append("No duplicates found!")
        report.append("")

    # NEEDS VERIFICATION section
    if needs_verification:
        report.append("")
        report.append("3. NEEDS VERIFICATION")
        report.append("=" * 80)
        report.append("These issues need manual review for accuracy or clarity.")
        report.append("")

        for i, issue in enumerate(needs_verification, 1):
            report.append(f"{i}. [{issue['type']}] {issue.get('issue', '')}")
            report.append(f"   ID: {issue['question_id']}")
            report.append(f"   Subtopic: {issue.get('subtopic', 'N/A')}")
            report.append(f"   Question: {issue['question']}")
            if 'answer' in issue:
                report.append(f"   Answer: {issue['answer']}")
            report.append("")
    else:
        report.append("")
        report.append("3. NEEDS VERIFICATION")
        report.append("=" * 80)
        report.append("No verification issues found!")
        report.append("")

    report.append("=" * 80)
    report.append("END OF REPORT")
    report.append("=" * 80)

    return "\n".join(report)

def main():
    """Main audit function"""
    filepath = '/home/user/fiztrivia/Fiz/Resources/Expansion Packs/expansion_harry_potter.json'

    print("Loading Harry Potter expansion pack...")
    pack_data = load_pack(filepath)

    # Get all questions
    all_questions = pack_data.get('freePreviewQuestions', []) + pack_data.get('paidQuestions', [])
    print(f"Total questions: {len(all_questions)}")

    print("\nRunning quality checks...")
    all_issues = []

    print("  - Checking for exact duplicates...")
    all_issues.extend(check_exact_duplicates(all_questions))

    print("  - Checking for semantic duplicates...")
    all_issues.extend(check_semantic_duplicates(all_questions))

    print("  - Checking for grammar issues...")
    all_issues.extend(check_grammar_issues(all_questions))

    print("  - Checking for self-revealing answers...")
    all_issues.extend(check_self_revealing(all_questions))

    print("  - Checking for typos and capitalization...")
    all_issues.extend(check_typos_and_common_errors(all_questions))

    print("  - Checking question quality...")
    all_issues.extend(check_question_quality(all_questions))

    print("\nCategorizing issues...")
    auto_fix, flag_for_replacement, needs_verification = categorize_issues(all_issues)

    print("\nGenerating report...")
    report = generate_report(pack_data, auto_fix, flag_for_replacement, needs_verification)

    # Save report
    report_path = '/home/user/fiztrivia/Harry_Potter_Quality_Audit_Report.md'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\nReport saved to: {report_path}")
    print(f"\nTotal issues found: {len(all_issues)}")
    print(f"  - Auto-Fix: {len(auto_fix)}")
    print(f"  - Flag for Replacement: {len(flag_for_replacement)}")
    print(f"  - Needs Verification: {len(needs_verification)}")

    # Also print report to console
    print("\n" + report)

if __name__ == '__main__':
    main()
