#!/usr/bin/env python3
"""
Renumber all Food questions sequentially from foo_001 to foo_278
"""

import json

def renumber_food():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    food_questions = data['categories']['Food']

    print(f"Total Food questions: {len(food_questions)}")
    print("Renumbering from foo_001 to foo_{:03d}...".format(len(food_questions)))
    
    # Sort by subcategory for consistent ordering
    # Order: Baking, Beverages, Cooking Techniques, Cuisines, Desserts, Dishes, 
    #        Famous Chefs/Restaurants, Food History, Ingredients, Sauces & Condiments
    subcategory_order = [
        'Baking', 'Beverages', 'Cooking Techniques', 'Cuisines', 'Desserts',
        'Dishes', 'Famous Chefs/Restaurants', 'Food History', 'Ingredients',
        'Sauces & Condiments'
    ]
    
    sorted_questions = []
    for subcat in subcategory_order:
        subcat_questions = [q for q in food_questions if q['subcategory'] == subcat]
        # Within each subcategory, sort by difficulty (easy, medium, hard)
        difficulty_order = {'easy': 0, 'medium': 1, 'hard': 2}
        subcat_questions.sort(key=lambda q: difficulty_order[q['difficulty']])
        sorted_questions.extend(subcat_questions)
    
    # Renumber sequentially
    for i, question in enumerate(sorted_questions, start=1):
        old_id = question['id']
        new_id = f"foo_{i:03d}"
        question['id'] = new_id
        if i <= 10 or i > len(sorted_questions) - 10:  # Show first 10 and last 10 changes
            print(f"  {old_id} → {new_id}")
        elif i == 11:
            print(f"  ... ({len(sorted_questions) - 20} more renumberings) ...")
    
    # Update the data
    data['categories']['Food'] = sorted_questions
    
    # Save updated database
    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Renumbered all {len(sorted_questions)} Food questions")
    print(f"✓ IDs now run sequentially: foo_001 → foo_{len(sorted_questions):03d}")
    
    # Show breakdown
    print("\nBreakdown by subcategory:")
    current_id = 1
    for subcat in subcategory_order:
        subcat_questions = [q for q in sorted_questions if q['subcategory'] == subcat]
        if subcat_questions:
            start_id = f"foo_{current_id:03d}"
            end_id = f"foo_{current_id + len(subcat_questions) - 1:03d}"
            print(f"  {subcat}: {start_id} - {end_id} ({len(subcat_questions)} questions)")
            current_id += len(subcat_questions)

if __name__ == "__main__":
    renumber_food()
