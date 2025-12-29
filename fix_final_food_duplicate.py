#!/usr/bin/env python3
"""
Replace the final duplicate Food question (foo_279)
"""

import json

def fix_final_duplicate():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    food_questions = data['categories']['Food']

    # Remove the duplicate question
    food_questions = [q for q in food_questions if q['id'] != 'foo_279']

    # NEW REPLACEMENT (completely different from hollandaise)
    replacement = {
        "id": "foo_279",
        "category": "Food",
        "subcategory": "Sauces & Condiments",
        "question": "What is the name of the spicy North African chili paste made from roasted red peppers?",
        "options": ["Harissa", "Sriracha", "Gochujang", "Sambal"],
        "correct_answer": "Harissa",
        "difficulty": "hard"
    }

    # Add replacement question
    food_questions.append(replacement)

    # Update the data
    data['categories']['Food'] = food_questions

    # Save updated database
    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("✓ Replaced final duplicate question")
    print(f"Food total: {len(food_questions)} questions")

if __name__ == "__main__":
    fix_final_duplicate()
