#!/usr/bin/env python3
"""Replace duplicate Music in Film & TV questions"""
import json

# Replacement questions for the 3 duplicates
replacements = {
    "mus_037": {
        "id": "mus_037",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who composed the music for The Avengers (2012)?",
        "options": ["Alan Silvestri", "Hans Zimmer", "Brian Tyler", "Danny Elfman"],
        "correct_answer": "Alan Silvestri",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "mus_039": {
        "id": "mus_039",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who composed the score for Mad Max: Fury Road?",
        "options": ["Junkie XL", "Hans Zimmer", "Cliff Martinez", "John Powell"],
        "correct_answer": "Junkie XL",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "mus_045": {
        "id": "mus_045",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who composed the music for Up?",
        "options": ["Michael Giacchino", "Randy Newman", "Thomas Newman", "James Newton Howard"],
        "correct_answer": "Michael Giacchino",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    }
}

# Load existing data
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Replace the duplicate questions
music_questions = data['categories']['Music']
replaced_count = 0

for i, q in enumerate(music_questions):
    if q['id'] in replacements:
        print(f"Replaced {q['id']}: {q['question']}")
        print(f"     New: {replacements[q['id']]['question']}\n")
        music_questions[i] = replacements[q['id']]
        replaced_count += 1

# Save back
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Replaced {replaced_count} duplicate questions")
