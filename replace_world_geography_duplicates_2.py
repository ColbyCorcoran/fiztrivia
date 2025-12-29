#!/usr/bin/env python3
"""Replace 3 more duplicate World Geography questions"""
import json

# Replacement questions for the 3 remaining duplicates
replacements = {
    "geo_048": {
        "id": "geo_048",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "What is the capital of Germany?",
        "options": ["Berlin", "Munich", "Hamburg", "Frankfurt"],
        "correct_answer": "Berlin",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "geo_051": {
        "id": "geo_051",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "What is the smallest ocean?",
        "options": ["Arctic Ocean", "Indian Ocean", "Southern Ocean", "Atlantic Ocean"],
        "correct_answer": "Arctic Ocean",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "geo_058": {
        "id": "geo_058",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "Which sea is bordered by Jordan, Israel, and the West Bank?",
        "options": ["Dead Sea", "Red Sea", "Mediterranean Sea", "Black Sea"],
        "correct_answer": "Dead Sea",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    }
}

# Load existing data
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Replace the duplicate questions
geography_questions = data['categories']['Geography']
replaced_count = 0

for i, q in enumerate(geography_questions):
    if q['id'] in replacements:
        geography_questions[i] = replacements[q['id']]
        replaced_count += 1
        print(f"Replaced {q['id']}: {q['question']}")
        print(f"     New: {replacements[q['id']]['question']}\n")

# Save back
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Replaced {replaced_count} duplicate questions")
