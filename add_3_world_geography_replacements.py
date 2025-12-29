#!/usr/bin/env python3
"""Add 3 replacement World Geography questions"""
import json

# 3 replacement World Geography questions to replace removed duplicates
replacement_questions = [
    {
        "id": "geo_301",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "What is the capital of Argentina?",
        "options": ["Buenos Aires", "Santiago", "Montevideo", "Lima"],
        "correct_answer": "Buenos Aires",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_302",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "Which sea is the saltiest body of water on Earth?",
        "options": ["Dead Sea", "Red Sea", "Caspian Sea", "Baltic Sea"],
        "correct_answer": "Dead Sea",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_303",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "What is the world's largest archipelago by number of islands?",
        "options": ["Indonesia", "Philippines", "Japan", "Greece"],
        "correct_answer": "Indonesia",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    }
]

# Load existing data
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Add replacement questions
data['categories']['Geography'].extend(replacement_questions)

# Sort by ID to maintain order
data['categories']['Geography'].sort(key=lambda q: int(q['id'].split('_')[1]))

# Save back
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Added 3 replacement World Geography questions")
print(f"Geography now has {len(data['categories']['Geography'])} total questions")

# Count World Geography
world_geo = [q for q in data['categories']['Geography'] if q['subcategory'] == 'World Geography']
print(f"World Geography: {len(world_geo)} questions")
