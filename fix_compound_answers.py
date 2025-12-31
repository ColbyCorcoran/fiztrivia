#!/usr/bin/env python3
"""
Fix compound answers that are in wrong positions.
- "all of the above" → move to slot D (index 3)
- "both X and Y" → move to slot D (index 3)
- "none of the above" → move to slot D (index 3)
"""

import json
import re
from datetime import datetime

def should_fix_answer(answer_text):
    """Check if answer should be moved to slot D."""
    patterns = [
        r'all of the above',
        r'both [A-D] and [A-D]',
        r'none of the above',
        r'all of these',
    ]

    for pattern in patterns:
        if re.search(pattern, answer_text, re.IGNORECASE):
            return True
    return False

def fix_compound_answers(json_file, output_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    fixed_count = 0
    fixed_questions = []

    for category_name, questions in data['categories'].items():
        for q in questions:
            question_id = q.get('id', 'UNKNOWN')
            options = q.get('options', [])
            correct_answer = q.get('correct_answer', '')

            if not options or not correct_answer:
                continue

            # Check if correct answer should be in slot D
            if should_fix_answer(correct_answer):
                try:
                    current_index = options.index(correct_answer)
                except ValueError:
                    print(f"⚠️  Warning: Correct answer not found in options for {question_id}")
                    continue

                # If already in slot D, skip
                if current_index == 3:
                    continue

                # Move to slot D
                # Remove from current position
                options_copy = options.copy()
                options_copy.remove(correct_answer)

                # Insert at end (slot D)
                options_copy.append(correct_answer)

                # Update the question
                q['options'] = options_copy

                fixed_count += 1
                fixed_questions.append({
                    'id': question_id,
                    'category': category_name,
                    'question': q['question'],
                    'correct_answer': correct_answer,
                    'old_slot': ['A', 'B', 'C', 'D'][current_index],
                    'new_slot': 'D',
                    'old_options': options,
                    'new_options': options_copy
                })

    # Write fixed data
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return fixed_count, fixed_questions

def main():
    questions_file = '/Users/colbycorcoran/Documents/App Development/Fiz/Fiz/Resources/questions.json'

    # Create backup
    backup_file = f'/Users/colbycorcoran/Documents/App Development/Fiz/Fiz/Resources/questions_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'

    print("Creating backup...")
    import shutil
    shutil.copy(questions_file, backup_file)
    print(f"✅ Backup created: {backup_file}\n")

    print("Fixing compound answers in questions.json...\n")
    print("=" * 80)

    fixed_count, fixed_questions = fix_compound_answers(questions_file, questions_file)

    if fixed_count == 0:
        print("✅ No fixes needed - all compound answers already in correct slots!")
    else:
        print(f"✅ Fixed {fixed_count} questions:\n")

        for i, fix in enumerate(fixed_questions, 1):
            print(f"{i}. ID: {fix['id']} ({fix['category']})")
            print(f"   Moved: {fix['old_slot']} → {fix['new_slot']}")
            print(f"   Answer: {fix['correct_answer']}")
            print(f"   Question: {fix['question'][:70]}...")
            print(f"   Old order: {fix['old_options']}")
            print(f"   New order: {fix['new_options']}")
            print()

    print("=" * 80)
    print(f"Total fixes applied: {fixed_count}")

if __name__ == '__main__':
    main()
