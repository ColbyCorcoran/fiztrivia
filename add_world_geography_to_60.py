#!/usr/bin/env python3
"""Add 21 World Geography questions to reach 60 total"""
import json

# 21 new World Geography questions (7 easy, 7 medium, 7 hard)
new_questions = [
    # EASY (7 questions)
    {
        "id": "geo_047",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "correct_answer": "Paris",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_048",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "Which continent is the Sahara Desert located on?",
        "options": ["Africa", "Asia", "Australia", "South America"],
        "correct_answer": "Africa",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_049",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "What is the capital of Japan?",
        "options": ["Tokyo", "Beijing", "Seoul", "Bangkok"],
        "correct_answer": "Tokyo",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_050",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "Which ocean is located between Africa and Australia?",
        "options": ["Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean"],
        "correct_answer": "Indian Ocean",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_051",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "What is the largest island in the world?",
        "options": ["Greenland", "New Guinea", "Borneo", "Madagascar"],
        "correct_answer": "Greenland",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_052",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "Which mountain range separates Europe from Asia?",
        "options": ["Ural Mountains", "Alps", "Himalayas", "Andes"],
        "correct_answer": "Ural Mountains",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_053",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "What is the capital of Italy?",
        "options": ["Rome", "Venice", "Milan", "Florence"],
        "correct_answer": "Rome",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },

    # MEDIUM (7 questions)
    {
        "id": "geo_054",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "What is the deepest point in the world's oceans?",
        "options": ["Mariana Trench", "Tonga Trench", "Philippine Trench", "Puerto Rico Trench"],
        "correct_answer": "Mariana Trench",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_055",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "Which African country has the most pyramids?",
        "options": ["Sudan", "Egypt", "Ethiopia", "Libya"],
        "correct_answer": "Sudan",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_056",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "What is the only sea without any coasts?",
        "options": ["Sargasso Sea", "Dead Sea", "Red Sea", "Black Sea"],
        "correct_answer": "Sargasso Sea",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_057",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "Which country has the most natural lakes?",
        "options": ["Canada", "Russia", "United States", "Finland"],
        "correct_answer": "Canada",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_058",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "What is the largest lake in Africa?",
        "options": ["Lake Victoria", "Lake Tanganyika", "Lake Malawi", "Lake Chad"],
        "correct_answer": "Lake Victoria",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_059",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "Which strait separates Europe from Africa?",
        "options": ["Strait of Gibraltar", "Bosphorus Strait", "Strait of Hormuz", "Strait of Malacca"],
        "correct_answer": "Strait of Gibraltar",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_060",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "What is the driest place on Earth?",
        "options": ["Atacama Desert", "Death Valley", "Sahara Desert", "Gobi Desert"],
        "correct_answer": "Atacama Desert",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },

    # HARD (7 questions)
    {
        "id": "geo_061",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "Which country has the most active volcanoes?",
        "options": ["Indonesia", "Japan", "Philippines", "United States"],
        "correct_answer": "Indonesia",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_062",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "What is the world's largest coral reef system?",
        "options": ["Great Barrier Reef", "Mesoamerican Reef", "New Caledonia Barrier Reef", "Red Sea Coral Reef"],
        "correct_answer": "Great Barrier Reef",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_063",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "Which country is home to the world's highest waterfall?",
        "options": ["Venezuela", "Norway", "Iceland", "New Zealand"],
        "correct_answer": "Venezuela",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_064",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "What is the largest peninsula in the world?",
        "options": ["Arabian Peninsula", "Indian Peninsula", "Iberian Peninsula", "Indochina Peninsula"],
        "correct_answer": "Arabian Peninsula",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_065",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "Which African lake is the deepest in the world by maximum depth?",
        "options": ["Lake Tanganyika", "Lake Malawi", "Lake Victoria", "Lake Turkana"],
        "correct_answer": "Lake Tanganyika",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_066",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "What is the largest plateau in the world?",
        "options": ["Tibetan Plateau", "Colorado Plateau", "Deccan Plateau", "Ethiopian Plateau"],
        "correct_answer": "Tibetan Plateau",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_067",
        "category": "Geography",
        "subcategory": "World Geography",
        "question": "Which country contains the most UNESCO World Heritage Sites?",
        "options": ["Italy", "China", "Spain", "France"],
        "correct_answer": "Italy",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    }
]

# Load existing data
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Add new questions
data['categories']['Geography'].extend(new_questions)

# Sort by ID to maintain order
data['categories']['Geography'].sort(key=lambda q: int(q['id'].split('_')[1]))

# Save back
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Added 21 World Geography questions")
print(f"Geography now has {len(data['categories']['Geography'])} total questions")

# Count World Geography
world_geo = [q for q in data['categories']['Geography'] if q['subcategory'] == 'World Geography']
print(f"World Geography: {len(world_geo)} questions")

# Count by difficulty
easy = len([q for q in new_questions if q['difficulty'] == 'easy'])
medium = len([q for q in new_questions if q['difficulty'] == 'medium'])
hard = len([q for q in new_questions if q['difficulty'] == 'hard'])
print(f"Added: {easy} easy, {medium} medium, {hard} hard")
