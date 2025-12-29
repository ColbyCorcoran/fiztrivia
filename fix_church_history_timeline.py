#!/usr/bin/env python3
"""
Replace 2 Biblical-era questions with proper post-Biblical Church History questions
"""

import json

def fix_timeline():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    history = data['categories']['History']

    # Remove the 2 problematic questions
    history = [q for q in history if q['id'] not in ['his_073', 'his_075']]

    # Add 2 new POST-BIBLICAL Church History questions
    replacements = [
        {
            "id": "his_073",
            "category": "History",
            "subcategory": "Church History",
            "question": "What was the name of the monastic movement that emphasized strict poverty, founded in the 13th century?",
            "options": ["Franciscan Order", "Dominican Order", "Benedictine Order", "Carthusian Order"],
            "correct_answer": "Franciscan Order",
            "difficulty": "medium"
        },
        {
            "id": "his_075",
            "category": "History",
            "subcategory": "Church History",
            "question": "What year marked the beginning of the Great Schism between Eastern and Western Christianity?",
            "options": ["1054", "1095", "1215", "1453"],
            "correct_answer": "1054",
            "difficulty": "medium"
        }
    ]

    # Add the replacement questions
    history.extend(replacements)

    # Update the data
    data['categories']['History'] = history

    # Save
    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("✓ Replaced 2 Biblical-era questions with post-Biblical Church History questions")
    print()
    print("Removed:")
    print("  • [his_073] Who was the apostle to the Gentiles? (Paul - Biblical era)")
    print("  • [his_075] What were the first four books of the NT called? (Biblical content)")
    print()
    print("Added:")
    print("  • [his_073] Franciscan Order question (13th century)")
    print("  • [his_075] Great Schism question (1054 AD)")
    print()
    print(f"History total: {len(history)} questions")

if __name__ == "__main__":
    fix_timeline()
