#!/usr/bin/env python3
"""Replace final duplicate World Geography question"""
import json

# Replacement for the last duplicate
replacement = {
    "id": "geo_051",
    "category": "Geography",
    "subcategory": "World Geography",
    "question": "What is the capital of Spain?",
    "options": ["Madrid", "Barcelona", "Valencia", "Seville"],
    "correct_answer": "Madrid",
    "difficulty": "easy",
    "topic": None,
    "subtopic": None
}

# Load existing data
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Replace the duplicate question
geography_questions = data['categories']['Geography']

for i, q in enumerate(geography_questions):
    if q['id'] == 'geo_051':
        print(f"Replaced {q['id']}: {q['question']}")
        print(f"     New: {replacement['question']}\n")
        geography_questions[i] = replacement
        break

# Save back
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Replaced final duplicate question")
