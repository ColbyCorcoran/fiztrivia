#!/usr/bin/env python3
"""Replace duplicate U.S. Geography question"""
import json

# Replacement for geo_138
replacement = {
    "id": "geo_138",
    "category": "Geography",
    "subcategory": "U.S. Geography",
    "question": "Which U.S. state is known as the \"Buckeye State\"?",
    "options": ["Ohio", "Michigan", "Indiana", "Pennsylvania"],
    "correct_answer": "Ohio",
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
    if q['id'] == 'geo_138':
        print(f"Replaced {q['id']}: {q['question']}")
        print(f"     New: {replacement['question']}\n")
        geography_questions[i] = replacement
        break

# Save back
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Replaced duplicate question")
