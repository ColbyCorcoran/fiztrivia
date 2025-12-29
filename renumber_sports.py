#!/usr/bin/env python3
"""
Renumber all Sports questions sequentially from spt_001 to spt_160
"""

import json

def renumber_sports():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    sports_questions = data['categories']['Sports']

    print(f"Current Sports questions: {len(sports_questions)}")

    # Sort by subcategory for consistent ordering
    subcategory_order = ['Team Sports', 'Individual Sports', 'International Competition']

    sorted_questions = []
    for subcat in subcategory_order:
        subcat_questions = [q for q in sports_questions if q['subcategory'] == subcat]
        # Sort by difficulty within subcategory
        difficulty_order = {'easy': 0, 'medium': 1, 'hard': 2}
        subcat_questions.sort(key=lambda q: difficulty_order[q['difficulty']])
        sorted_questions.extend(subcat_questions)

    # Renumber sequentially
    for i, question in enumerate(sorted_questions, start=1):
        old_id = question['id']
        new_id = f"spt_{i:03d}"
        question['id'] = new_id
        if i <= 10 or i > 150:  # Show first 10 and last 10
            print(f"  {old_id} → {new_id}")

    data['categories']['Sports'] = sorted_questions

    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Renumbered {len(sorted_questions)} Sports questions")
    print(f"  New range: spt_001 to spt_{len(sorted_questions):03d}")

if __name__ == "__main__":
    renumber_sports()
