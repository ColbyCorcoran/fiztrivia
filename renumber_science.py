#!/usr/bin/env python3
"""
Renumber all Science questions sequentially from sci_001 to sci_300
"""

import json

def renumber_science():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    science_questions = data['categories']['Science']

    print(f"Total Science questions: {len(science_questions)}")
    print("Renumbering from sci_001 to sci_300...")
    
    # Sort by subcategory for consistent ordering
    # Order: Astronomy, Biology, Chemistry, Physics (alphabetical)
    subcategory_order = ['Astronomy', 'Biology', 'Chemistry', 'Physics']
    
    sorted_questions = []
    for subcat in subcategory_order:
        subcat_questions = [q for q in science_questions if q['subcategory'] == subcat]
        # Within each subcategory, sort by difficulty (easy, medium, hard)
        difficulty_order = {'easy': 0, 'medium': 1, 'hard': 2}
        subcat_questions.sort(key=lambda q: difficulty_order[q['difficulty']])
        sorted_questions.extend(subcat_questions)
    
    # Renumber sequentially
    for i, question in enumerate(sorted_questions, start=1):
        old_id = question['id']
        new_id = f"sci_{i:03d}"
        question['id'] = new_id
        if i <= 10 or i > 290:  # Show first 10 and last 10 changes
            print(f"  {old_id} → {new_id}")
        elif i == 11:
            print(f"  ... ({len(sorted_questions) - 20} more renumberings) ...")
    
    # Update the data
    data['categories']['Science'] = sorted_questions
    
    # Save updated database
    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Renumbered all {len(sorted_questions)} Science questions")
    print("✓ IDs now run sequentially: sci_001 → sci_300")
    
    # Show breakdown
    print("\nBreakdown by subcategory:")
    subcats = {}
    for q in sorted_questions:
        subcat = q['subcategory']
        if subcat not in subcats:
            subcats[subcat] = []
        subcats[subcat].append(q['id'])
    
    for subcat in subcategory_order:
        ids = subcats[subcat]
        print(f"  {subcat}: {ids[0]} - {ids[-1]} ({len(ids)} questions)")

if __name__ == "__main__":
    renumber_science()
