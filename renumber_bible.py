#!/usr/bin/env python3
"""
Renumber all Bible questions sequentially from bib_001 to bib_266
"""

import json

def renumber_bible():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    bible_questions = data['categories']['Bible']

    print(f"Total Bible questions: {len(bible_questions)}")
    print("Renumbering from bib_001 to bib_{:03d}...".format(len(bible_questions)))
    
    # Sort by subcategory for consistent ordering
    # Order: Bible Languages, Bible Trivia, Biblical History, Biblical Theology, New Testament, Old Testament
    subcategory_order = [
        'Bible Languages', 'Bible Trivia', 'Biblical History', 
        'Biblical Theology', 'New Testament', 'Old Testament'
    ]
    
    sorted_questions = []
    for subcat in subcategory_order:
        subcat_questions = [q for q in bible_questions if q['subcategory'] == subcat]
        # Within each subcategory, sort by difficulty (easy, medium, hard)
        difficulty_order = {'easy': 0, 'medium': 1, 'hard': 2}
        subcat_questions.sort(key=lambda q: difficulty_order[q['difficulty']])
        sorted_questions.extend(subcat_questions)
    
    # Renumber sequentially
    for i, question in enumerate(sorted_questions, start=1):
        old_id = question['id']
        new_id = f"bib_{i:03d}"
        question['id'] = new_id
        if i <= 10 or i > len(sorted_questions) - 10:
            print(f"  {old_id} → {new_id}")
        elif i == 11:
            print(f"  ... ({len(sorted_questions) - 20} more renumberings) ...")
    
    # Update the data
    data['categories']['Bible'] = sorted_questions
    
    # Save updated database
    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Renumbered all {len(sorted_questions)} Bible questions")
    print(f"✓ IDs now run sequentially: bib_001 → bib_{len(sorted_questions):03d}")
    
    # Show breakdown
    print("\nBreakdown by subcategory:")
    current_id = 1
    for subcat in subcategory_order:
        subcat_questions = [q for q in sorted_questions if q['subcategory'] == subcat]
        if subcat_questions:
            start_id = f"bib_{current_id:03d}"
            end_id = f"bib_{current_id + len(subcat_questions) - 1:03d}"
            print(f"  {subcat}: {start_id} - {end_id} ({len(subcat_questions)} questions)")
            current_id += len(subcat_questions)

if __name__ == "__main__":
    renumber_bible()
