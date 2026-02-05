#!/usr/bin/env python3
"""
Quality assurance audit for Sports expansion pack
"""

import json
import re
from difflib import SequenceMatcher
from collections import defaultdict

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
        (r'\b(a)\s+(hour|NBA|NFL|NHL|NBA|UFC)\b', 'a_vs_an', 'Should use "an" instead of "a"'),
        (r'\b(an)\s+(one|university|European)\b', 'an_vs_a', 'Should use "a" instead of "an"'),
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
            ('atheletes', 'athletes'),
            ('occured', 'occurred'),
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
        common_words = {'the', 'a', 'an', 'and', 'or', 'in', 'on', 'at', 'to', 'for', 'of', 'with'}

        if correct_answer not in common_words and len(correct_answer) > 3:
            if correct_answer in question_lower:
                issues.append({
                    'type': 'self_revealing',
                    'question_id': q['id'],
                    'question': q['question'],
                    'answer': q['correct_answer'],
                    'description': 'Answer appears in question text'
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

    return issues

def generate_report(questions):
    """Generate comprehensive QA report"""
    print("=" * 80)
    print("SPORTS EXPANSION PACK QUALITY ASSURANCE REPORT")
    print("=" * 80)
    print(f"\nTotal questions analyzed: {len(questions)}")
    print()

    # Check for all issues
    exact_dupes = check_exact_duplicates(questions)
    semantic_dupes = check_semantic_duplicates(questions)
    grammar_issues = check_grammar_issues(questions)
    self_revealing = check_self_revealing(questions)
    confusing = check_confusing_wording(questions)
    answer_issues = check_answer_options(questions)

    # Category 1: AUTO-FIX (Clear typos/grammar)
    print("=" * 80)
    print("CATEGORY 1: AUTO-FIX (Clear typos/grammar)")
    print("=" * 80)

    auto_fix = [g for g in grammar_issues if g['issue_type'] in ['typo', 'double_space', 'space_before_punctuation']]

    if auto_fix:
        for issue in auto_fix:
            print(f"\nQuestion ID: {issue['question_id']}")
            print(f"Issue: {issue['description']}")
            print(f"Question: {issue['question']}")
    else:
        print("\nNo auto-fix issues found!")

    print(f"\nTotal auto-fix issues: {len(auto_fix)}")

    # Category 2: FLAG FOR REPLACEMENT (Duplicates)
    print("\n" + "=" * 80)
    print("CATEGORY 2: FLAG FOR REPLACEMENT (Exact/Semantic Duplicates)")
    print("=" * 80)

    if exact_dupes:
        print("\n--- EXACT DUPLICATES ---")
        for dup in exact_dupes:
            print(f"\nQuestion ID: {dup['question_id']} (duplicate of {dup['duplicate_of']})")
            print(f"Question: {dup['question']}")

    if semantic_dupes:
        print("\n--- SEMANTIC DUPLICATES (>90% similar) ---")
        for dup in semantic_dupes:
            print(f"\nQuestion ID: {dup['question_id']} vs {dup['duplicate_of']} ({dup['similarity']} similar)")
            print(f"Q1: {dup['question1']}")
            print(f"Q2: {dup['question2']}")

    if not exact_dupes and not semantic_dupes:
        print("\nNo duplicates found!")

    print(f"\nTotal duplicates: {len(exact_dupes) + len(semantic_dupes)}")

    # Category 3: NEEDS VERIFICATION
    print("\n" + "=" * 80)
    print("CATEGORY 3: NEEDS VERIFICATION (Questionable accuracy/clarity)")
    print("=" * 80)

    if self_revealing:
        print("\n--- SELF-REVEALING ANSWERS ---")
        for issue in self_revealing:
            print(f"\nQuestion ID: {issue['question_id']}")
            print(f"Question: {issue['question']}")
            print(f"Answer: {issue['answer']}")

    if confusing:
        print("\n--- CONFUSING WORDING ---")
        for issue in confusing:
            print(f"\nQuestion ID: {issue['question_id']}")
            print(f"Issue: {issue['description']}")
            print(f"Question: {issue['question']}")

    if answer_issues:
        print("\n--- ANSWER OPTION ISSUES ---")
        for issue in answer_issues:
            print(f"\nQuestion ID: {issue['question_id']}")
            print(f"Issue: {issue['description']}")
            print(f"Question: {issue['question']}")
            if issue['type'] == 'answer_not_in_options':
                print(f"Correct Answer: {issue['correct_answer']}")
                print(f"Options: {issue['options']}")

    if not self_revealing and not confusing and not answer_issues:
        print("\nNo verification issues found!")

    print(f"\nTotal verification issues: {len(self_revealing) + len(confusing) + len(answer_issues)}")

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total questions: {len(questions)}")
    print(f"Auto-fix issues: {len(auto_fix)}")
    print(f"Duplicates: {len(exact_dupes) + len(semantic_dupes)}")
    print(f"Needs verification: {len(self_revealing) + len(confusing) + len(answer_issues)}")
    print(f"TOTAL ISSUES: {len(auto_fix) + len(exact_dupes) + len(semantic_dupes) + len(self_revealing) + len(confusing) + len(answer_issues)}")
    print("=" * 80)

def main():
    filepath = '/home/user/fiztrivia/Fiz/Resources/Expansion Packs/expansion_sports.json'
    questions = load_questions(filepath)
    generate_report(questions)

if __name__ == '__main__':
    main()
