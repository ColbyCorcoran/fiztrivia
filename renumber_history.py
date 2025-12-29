#!/usr/bin/env python3
"""
Renumber all History questions sequentially from his_001 to his_268
"""

import json

def renumber_history():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    history_questions = data['categories']['History']

    print(f"Total History questions: {len(history_questions)}")
    print("Renumbering from his_001 to his_{:03d}...".format(len(history_questions)))
    
    # Sort by subcategory for consistent ordering
    # Order: Ancient History, Church History, Medieval History, Modern History
    subcategory_order = ['Ancient History', 'Church History', 'Medieval History', 'Modern History']
    
    sorted_questions = []
    for subcat in subcategory_order:
        subcat_questions = [q for q in history_questions if q['subcategory'] == subcat]
        # Within each subcategory, sort by difficulty (easy, medium, hard)
        difficulty_order = {'easy': 0, 'medium': 1, 'hard': 2}
        subcat_questions.sort(key=lambda q: difficulty_order[q['difficulty']])
        sorted_questions.extend(subcat_questions)
    
    # Renumber sequentially
    for i, question in enumerate(sorted_questions, start=1):
        old_id = question['id']
        new_id = f"his_{i:03d}"
        question['id'] = new_id
        if i <= 10 or i > len(sorted_questions) - 10:
            print(f"  {old_id} → {new_id}")
        elif i == 11:
            print(f"  ... ({len(sorted_questions) - 20} more renumberings) ...")
    
    # Update the data
    data['categories']['History'] = sorted_questions
    
    # Save updated database
    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Renumbered all {len(sorted_questions)} History questions")
    print(f"✓ IDs now run sequentially: his_001 → his_{len(sorted_questions):03d}")
    
    # Show breakdown
    print("\nBreakdown by subcategory:")
    current_id = 1
    for subcat in subcategory_order:
        subcat_questions = [q for q in sorted_questions if q['subcategory'] == subcat]
        if subcat_questions:
            start_id = f"his_{current_id:03d}"
            end_id = f"his_{current_id + len(subcat_questions) - 1:03d}"
            print(f"  {subcat}: {start_id} - {end_id} ({len(subcat_questions)} questions)")
            current_id += len(subcat_questions)

if __name__ == "__main__":
    renumber_history()
