#!/usr/bin/env python3
"""Replace potential duplicate Maps & Borders question"""
import json

# Replacement for geo_070
replacement = {
    "id": "geo_070",
    "category": "Geography",
    "subcategory": "Maps & Borders",
    "question": "Which mountain range forms the natural border between France and Italy?",
    "options": ["The Alps", "The Pyrenees", "The Apennines", "The Dolomites"],
    "correct_answer": "The Alps",
    "difficulty": "easy",
    "topic": None,
    "subtopic": None
}

# Load existing data
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Replace the question
geography_questions = data['categories']['Geography']

for i, q in enumerate(geography_questions):
    if q['id'] == 'geo_070':
        print(f"Replaced {q['id']}: {q['question']}")
        print(f"     New: {replacement['question']}\n")
        geography_questions[i] = replacement
        break

# Save back
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Replaced potential duplicate question")
