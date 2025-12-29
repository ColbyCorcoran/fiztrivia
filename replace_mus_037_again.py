#!/usr/bin/env python3
"""Replace mus_037 again (duplicate with mus_012)"""
import json

# Replacement for mus_037
replacement = {
    "id": "mus_037",
    "category": "Music",
    "subcategory": "Music in Film & TV",
    "question": "Who composed the score for Dune (2021)?",
    "options": ["Hans Zimmer", "Ludwig Göransson", "Hildur Guðnadóttir", "Daniel Pemberton"],
    "correct_answer": "Hans Zimmer",
    "difficulty": "medium",
    "topic": None,
    "subtopic": None
}

# Load existing data
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Replace the question
music_questions = data['categories']['Music']

for i, q in enumerate(music_questions):
    if q['id'] == 'mus_037':
        print(f"Replaced {q['id']}: {q['question']}")
        print(f"     New: {replacement['question']}\n")
        music_questions[i] = replacement
        break

# Save back
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Replaced mus_037")
