#!/usr/bin/env python3
"""
Analyze questions.json for compound answers that may be in wrong positions.
Checks for:
- "all of the above" (should be in slot D)
- "both A and B" / "both A and C" / "both B and C" (should be in slot C or D)
- "none of the above" (should be in slot D)
"""

import json
import re

def analyze_compound_answers(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    issues = []

    # Patterns to check
    compound_patterns = [
        (r'all of the above', 'all of the above', 3),  # Should be in index 3 (slot D)
        (r'both [A-D] and [A-D]', 'both X and Y', [2, 3]),  # Should be in index 2 or 3 (slot C or D)
        (r'none of the above', 'none of the above', 3),  # Should be in index 3 (slot D)
        (r'all of these', 'all of these', 3),  # Should be in index 3 (slot D)
        (r'both', 'both (generic)', [2, 3]),  # Generic "both" should be in C or D
    ]

    for category_name, questions in data['categories'].items():
        for q in questions:
            question_id = q.get('id', 'UNKNOWN')
            question_text = q.get('question', '')
            options = q.get('options', [])
            correct_answer = q.get('correct_answer', '')

            if not options or not correct_answer:
                continue

            # Find which slot the correct answer is in
            try:
                correct_slot_index = options.index(correct_answer)
                correct_slot_letter = ['A', 'B', 'C', 'D'][correct_slot_index]
            except (ValueError, IndexError):
                issues.append({
                    'id': question_id,
                    'category': category_name,
                    'issue': 'Correct answer not found in options',
                    'question': question_text,
                    'correct_answer': correct_answer,
                    'options': options
                })
                continue

            # Check if correct answer matches any compound pattern
            for pattern, pattern_name, expected_slots in compound_patterns:
                if re.search(pattern, correct_answer, re.IGNORECASE):
                    expected_slots_list = expected_slots if isinstance(expected_slots, list) else [expected_slots]

                    if correct_slot_index not in expected_slots_list:
                        expected_letters = [['A', 'B', 'C', 'D'][i] for i in expected_slots_list]
                        issues.append({
                            'id': question_id,
                            'category': category_name,
                            'issue': f'"{pattern_name}" in wrong slot',
                            'current_slot': f'{correct_slot_letter} (index {correct_slot_index})',
                            'expected_slot': f'{"/".join(expected_letters)} (index {"/".join(map(str, expected_slots_list))})',
                            'question': question_text,
                            'correct_answer': correct_answer,
                            'options': options
                        })

    return issues

def main():
    questions_file = '/Users/colbycorcoran/Documents/App Development/Fiz/Fiz/Resources/questions.json'

    print("Analyzing main questions.json for compound answer issues...\n")
    print("=" * 80)

    issues = analyze_compound_answers(questions_file)

    if not issues:
        print("✅ No compound answer issues found!")
    else:
        print(f"⚠️  Found {len(issues)} issues:\n")

        for i, issue in enumerate(issues, 1):
            print(f"{i}. ID: {issue['id']} ({issue['category']})")
            print(f"   Issue: {issue['issue']}")
            if 'current_slot' in issue:
                print(f"   Current slot: {issue['current_slot']}")
                print(f"   Expected slot: {issue['expected_slot']}")
            print(f"   Question: {issue['question'][:80]}...")
            print(f"   Correct answer: {issue['correct_answer']}")
            print(f"   All options: {issue['options']}")
            print()

    print("=" * 80)
    print(f"Total issues found: {len(issues)}")

if __name__ == '__main__':
    main()
