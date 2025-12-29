#!/usr/bin/env python3
"""Renumber all Entertainment questions sequentially from ent_001 to ent_051"""
import json

def renumber_entertainment():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    entertainment_questions = data['categories']['Entertainment']

    # Sort by subcategory for consistent ordering
    subcategory_order = ['Action/Adventure', 'Animation', 'Drama/Comedy', 'Sci-Fi/Fantasy']
    sorted_questions = []

    for subcat in subcategory_order:
        subcat_questions = [q for q in entertainment_questions if q['subcategory'] == subcat]
        # Sort by difficulty within subcategory
        difficulty_order = {'easy': 0, 'medium': 1, 'hard': 2}
        subcat_questions.sort(key=lambda q: difficulty_order[q['difficulty']])
        sorted_questions.extend(subcat_questions)

    # Renumber sequentially
    for i, question in enumerate(sorted_questions, start=1):
        question['id'] = f"ent_{i:03d}"

    data['categories']['Entertainment'] = sorted_questions

    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Renumbered {len(sorted_questions)} Entertainment questions (ent_001 to ent_{len(sorted_questions):03d})")

    # Show breakdown
    subcats = {}
    for q in sorted_questions:
        subcat = q['subcategory']
        if subcat not in subcats:
            subcats[subcat] = 0
        subcats[subcat] += 1

    print("\nSubcategory distribution:")
    for subcat in subcategory_order:
        print(f"  {subcat}: {subcats.get(subcat, 0)} questions")

if __name__ == '__main__':
    renumber_entertainment()
