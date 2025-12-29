#!/usr/bin/env python3
"""
Replace the 6 duplicate Food questions with unique ones
"""

import json

def fix_duplicates():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    food_questions = data['categories']['Food']

    # IDs to replace
    ids_to_replace = ['foo_279', 'foo_292', 'foo_293', 'foo_294', 'foo_299', 'foo_300']

    # Remove the duplicate questions
    food_questions = [q for q in food_questions if q['id'] not in ids_to_replace]

    # NEW REPLACEMENT QUESTIONS (completely different topics)
    replacements = [
        # foo_279 - Sauces & Condiments (replace pesto question)
        {
            "id": "foo_279",
            "category": "Food",
            "subcategory": "Sauces & Condiments",
            "question": "What French sauce is made with butter, egg yolks, and lemon juice?",
            "options": ["Hollandaise", "Béarnaise", "Beurre blanc", "Mousseline"],
            "correct_answer": "Hollandaise",
            "difficulty": "medium"
        },
        # foo_292 - Desserts (replace tiramisu question)
        {
            "id": "foo_292",
            "category": "Food",
            "subcategory": "Desserts",
            "question": "What Austrian pastry features layers of thin dough filled with apple and cinnamon?",
            "options": ["Apple strudel", "Sachertorte", "Linzer torte", "Gugelhupf"],
            "correct_answer": "Apple strudel",
            "difficulty": "medium"
        },
        # foo_293 - Desserts (replace crème brûlée question)
        {
            "id": "foo_293",
            "category": "Food",
            "subcategory": "Desserts",
            "question": "What is the name of the Spanish custard dessert with a burnt sugar top, similar to crème brûlée?",
            "options": ["Crema catalana", "Flan", "Natillas", "Arroz con leche"],
            "correct_answer": "Crema catalana",
            "difficulty": "hard"
        },
        # foo_294 - Desserts (replace éclair question)
        {
            "id": "foo_294",
            "category": "Food",
            "subcategory": "Desserts",
            "question": "What Italian dessert consists of tube-shaped shells filled with sweet ricotta?",
            "options": ["Cannoli", "Biscotti", "Panna cotta", "Sfogliatelle"],
            "correct_answer": "Cannoli",
            "difficulty": "medium"
        },
        # foo_299 - Cuisines (replace tempura question)
        {
            "id": "foo_299",
            "category": "Food",
            "subcategory": "Cuisines",
            "question": "What is the name of the Greek dish featuring grape leaves stuffed with rice and herbs?",
            "options": ["Dolmades", "Spanakopita", "Moussaka", "Souvlaki"],
            "correct_answer": "Dolmades",
            "difficulty": "hard"
        },
        # foo_300 - Cooking Techniques (replace braising question)
        {
            "id": "foo_300",
            "category": "Food",
            "subcategory": "Cooking Techniques",
            "question": "What is the French term for cooking vegetables in their own juices over low heat?",
            "options": ["Sweating (étuver)", "Sautéing", "Blanching", "Poaching"],
            "correct_answer": "Sweating (étuver)",
            "difficulty": "hard"
        }
    ]

    # Add replacement questions
    food_questions.extend(replacements)

    # Update the data
    data['categories']['Food'] = food_questions

    # Save updated database
    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("✓ Replaced 6 duplicate questions with unique ones")
    print(f"\nFood total: {len(food_questions)} questions")
    
    # Show breakdown
    print("\nBreakdown by subcategory:")
    subcats = {}
    for q in food_questions:
        subcat = q['subcategory']
        if subcat not in subcats:
            subcats[subcat] = 0
        subcats[subcat] += 1

    for subcat in sorted(subcats.keys()):
        print(f"  {subcat}: {subcats[subcat]} questions")

if __name__ == "__main__":
    fix_duplicates()
