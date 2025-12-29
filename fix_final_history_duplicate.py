#!/usr/bin/env python3
"""
Replace the final duplicate History question (his_271)
"""

import json

def fix_final_duplicate():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    history_questions = data['categories']['History']

    # Remove the duplicate question
    history_questions = [q for q in history_questions if q['id'] != 'his_271']

    # NEW REPLACEMENT (completely different)
    replacement = {
        "id": "his_271",
        "category": "History",
        "subcategory": "Church History",
        "question": "What was the name of the first printed Bible using movable type?",
        "options": ["Gutenberg Bible", "King James Bible", "Vulgate", "Septuagint"],
        "correct_answer": "Gutenberg Bible",
        "difficulty": "easy"
    }

    # Add replacement question
    history_questions.append(replacement)

    # Update the data
    data['categories']['History'] = history_questions

    # Save updated database
    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("✓ Replaced final duplicate question")
    print(f"History total: {len(history_questions)} questions")

if __name__ == "__main__":
    fix_final_duplicate()
