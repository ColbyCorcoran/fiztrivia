#!/usr/bin/env python3
"""
Replace the 5 duplicate Science questions with unique ones
"""

import json

def fix_duplicates():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    science_questions = data['categories']['Science']

    # IDs to replace
    ids_to_replace = ['sci_052', 'sci_144', 'sci_170', 'sci_179', 'sci_203']

    # Remove the duplicate questions
    science_questions = [q for q in science_questions if q['id'] not in ids_to_replace]

    # NEW REPLACEMENT QUESTIONS (completely different topics)
    replacements = [
        # sci_052 - Astronomy easy (replace "largest planet")
        {
            "id": "sci_052",
            "category": "Science",
            "subcategory": "Astronomy",
            "question": "What celestial object type includes Halley's and Hale-Bopp?",
            "options": ["Comets", "Asteroids", "Meteors", "Planets"],
            "correct_answer": "Comets",
            "difficulty": "easy"
        },
        # sci_144 - Astronomy medium (replace "nearest galaxy")
        {
            "id": "sci_144",
            "category": "Science",
            "subcategory": "Astronomy",
            "question": "What is the term for a star that suddenly increases in brightness and then fades?",
            "options": ["Nova", "Supernova", "Pulsar", "Quasar"],
            "correct_answer": "Nova",
            "difficulty": "medium"
        },
        # sci_170 - Biology medium (replace "hemoglobin")
        {
            "id": "sci_170",
            "category": "Science",
            "subcategory": "Biology",
            "question": "What type of immunity is provided by vaccination?",
            "options": ["Acquired immunity", "Innate immunity", "Passive immunity", "Natural immunity"],
            "correct_answer": "Acquired immunity",
            "difficulty": "medium"
        },
        # sci_179 - Chemistry easy (replace "most abundant gas")
        {
            "id": "sci_179",
            "category": "Science",
            "subcategory": "Chemistry",
            "question": "What is the common name for sodium chloride?",
            "options": ["Table salt", "Baking soda", "Sugar", "Vinegar"],
            "correct_answer": "Table salt",
            "difficulty": "easy"
        },
        # sci_203 - Physics hard (replace "refraction")
        {
            "id": "sci_203",
            "category": "Science",
            "subcategory": "Physics",
            "question": "What is the unit of force in the International System of Units (SI)?",
            "options": ["Newton", "Joule", "Watt", "Pascal"],
            "correct_answer": "Newton",
            "difficulty": "hard"
        }
    ]

    # Add replacement questions
    science_questions.extend(replacements)

    # Update the data
    data['categories']['Science'] = science_questions

    # Save updated database
    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("✓ Replaced 5 duplicate questions with unique ones")
    print(f"\nScience total: {len(science_questions)} questions")
    
    # Show breakdown
    print("\nBreakdown by subcategory:")
    subcats = {}
    for q in science_questions:
        subcat = q['subcategory']
        if subcat not in subcats:
            subcats[subcat] = 0
        subcats[subcat] += 1

    for subcat in sorted(subcats.keys()):
        print(f"  {subcat}: {subcats[subcat]} questions")

if __name__ == "__main__":
    fix_duplicates()
