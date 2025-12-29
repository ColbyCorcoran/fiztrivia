#!/usr/bin/env python3
"""Replace 8 duplicate World Geography questions"""
import json

# Replacement questions for the 8 duplicates found
replacements = {
    "geo_048": {
        "id": "geo_048",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "What is the capital of Canada?",
        "options": ["Ottawa", "Toronto", "Montreal", "Vancouver"],
        "correct_answer": "Ottawa",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "geo_049": {
        "id": "geo_049",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "Which river flows through London?",
        "options": ["Thames", "Seine", "Danube", "Rhine"],
        "correct_answer": "Thames",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "geo_051": {
        "id": "geo_051",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "What is the capital of Brazil?",
        "options": ["Brasília", "Rio de Janeiro", "São Paulo", "Salvador"],
        "correct_answer": "Brasília",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "geo_052": {
        "id": "geo_052",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "Which European mountain range includes Mont Blanc?",
        "options": ["The Alps", "The Pyrenees", "The Carpathians", "The Apennines"],
        "correct_answer": "The Alps",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "geo_054": {
        "id": "geo_054",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "What is the largest freshwater lake by surface area?",
        "options": ["Lake Superior", "Lake Baikal", "Lake Michigan", "Lake Huron"],
        "correct_answer": "Lake Superior",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "geo_058": {
        "id": "geo_058",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "Which country has the longest coastline in the world?",
        "options": ["Canada", "Indonesia", "Russia", "Australia"],
        "correct_answer": "Canada",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "geo_060": {
        "id": "geo_060",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "What is the world's largest hot desert?",
        "options": ["Sahara Desert", "Arabian Desert", "Kalahari Desert", "Gobi Desert"],
        "correct_answer": "Sahara Desert",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "geo_061": {
        "id": "geo_061",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "Which continent has the highest average elevation?",
        "options": ["Antarctica", "Asia", "South America", "Africa"],
        "correct_answer": "Antarctica",
        "difficulty": "hard",
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
