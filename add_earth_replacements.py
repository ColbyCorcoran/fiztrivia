import json

# Load the current database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# 12 replacement Earth questions - being VERY specific and unique
new_earth_questions = [
    {
        "id": "ear_253",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "What is the only venomous primate?",
        "options": ["Slow loris", "Howler monkey", "Lemur", "Tarsier"],
        "correct_answer": "Slow loris",
        "difficulty": "hard"
    },
    {
        "id": "ear_254",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "What is the capital of Australia?",
        "options": ["Canberra", "Sydney", "Melbourne", "Brisbane"],
        "correct_answer": "Canberra",
        "difficulty": "medium"
    },
    {
        "id": "ear_255",
        "category": "Earth",
        "subcategory": "Weather",
        "question": "What instrument measures humidity?",
        "options": ["Hygrometer", "Barometer", "Thermometer", "Anemometer"],
        "correct_answer": "Hygrometer",
        "difficulty": "hard"
    },
    {
        "id": "ear_256",
        "category": "Earth",
        "subcategory": "Plants",
        "question": "What part of the plant absorbs water and nutrients from the soil?",
        "options": ["Roots", "Stems", "Leaves", "Flowers"],
        "correct_answer": "Roots",
        "difficulty": "easy"
    },
    {
        "id": "ear_257",
        "category": "Earth",
        "subcategory": "Trees",
        "question": "What coniferous tree loses its needles in winter?",
        "options": ["Larch", "Pine", "Spruce", "Fir"],
        "correct_answer": "Larch",
        "difficulty": "hard"
    },
    {
        "id": "ear_258",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "What is the largest species of penguin?",
        "options": ["Emperor penguin", "King penguin", "Gentoo penguin", "Adélie penguin"],
        "correct_answer": "Emperor penguin",
        "difficulty": "medium"
    },
    {
        "id": "ear_259",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "Which U.S. state has the most active volcanoes?",
        "options": ["Alaska", "Hawaii", "Washington", "California"],
        "correct_answer": "Alaska",
        "difficulty": "hard"
    },
    {
        "id": "ear_260",
        "category": "Earth",
        "subcategory": "Weather",
        "question": "What is the rotating column of air over water called?",
        "options": ["Waterspout", "Tornado", "Hurricane", "Cyclone"],
        "correct_answer": "Waterspout",
        "difficulty": "medium"
    },
    {
        "id": "ear_261",
        "category": "Earth",
        "subcategory": "Plants",
        "question": "What is the process by which plants release water vapor?",
        "options": ["Transpiration", "Photosynthesis", "Respiration", "Germination"],
        "correct_answer": "Transpiration",
        "difficulty": "hard"
    },
    {
        "id": "ear_262",
        "category": "Earth",
        "subcategory": "Trees",
        "question": "What tree produces helicopter seeds?",
        "options": ["Maple", "Oak", "Pine", "Birch"],
        "correct_answer": "Maple",
        "difficulty": "medium"
    },
    {
        "id": "ear_263",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "What is a group of lions called?",
        "options": ["Pride", "Pack", "Herd", "Troop"],
        "correct_answer": "Pride",
        "difficulty": "medium"
    },
    {
        "id": "ear_264",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "What mountain range separates Europe from Asia?",
        "options": ["Ural Mountains", "Alps", "Himalayas", "Caucasus"],
        "correct_answer": "Ural Mountains",
        "difficulty": "hard"
    }
]

# Add the new questions
data['categories']['Earth'].extend(new_earth_questions)
data['categories']['Earth'].sort(key=lambda x: x['id'])

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Added {len(new_earth_questions)} replacement Earth questions")
print(f"New Earth total: {len(data['categories']['Earth'])} questions")
