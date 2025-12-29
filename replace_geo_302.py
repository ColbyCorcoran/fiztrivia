#!/usr/bin/env python3
"""Replace geo_302 duplicate"""
import json

# Replacement for geo_302
replacement = {
    "id": "geo_302",
    "category": "Geography",
    "subcategory": "World Geography",
    "question": "What is the capital of Poland?",
    "options": ["Warsaw", "Krakow", "Gdansk", "Wroclaw"],
    "correct_answer": "Warsaw",
    "difficulty": "medium",
    "topic": None,
    "subtopic": None
}

# Load existing data
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Replace the question
geography_questions = data['categories']['Geography']

for i, q in enumerate(geography_questions):
    if q['id'] == 'geo_302':
        print(f"Replaced {q['id']}: {q['question']}")
        print(f"     New: {replacement['question']}\n")
        geography_questions[i] = replacement
        break

# Save back
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Replaced duplicate question")
