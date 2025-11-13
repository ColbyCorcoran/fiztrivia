import json

# Load database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# 14 unique replacement questions
replacements = [
    {
        "id": "ear_301",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "Which animal has rectangular pupils?",
        "options": ["Goat", "Cat", "Horse", "Deer"],
        "correct_answer": "Goat",
        "difficulty": "hard"
    },
    {
        "id": "ear_302",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "What is the collective noun for a group of flamingos?",
        "options": ["Flamboyance", "Flock", "Colony", "Parade"],
        "correct_answer": "Flamboyance",
        "difficulty": "hard"
    },
    {
        "id": "ear_303",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "Which mammal has the most powerful bite force?",
        "options": ["Hippopotamus", "Lion", "Crocodile", "Bear"],
        "correct_answer": "Hippopotamus",
        "difficulty": "hard"
    },
    {
        "id": "ear_304",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "How many species of penguin exist in the world?",
        "options": ["18", "12", "25", "30"],
        "correct_answer": "18",
        "difficulty": "hard"
    },
    {
        "id": "ear_305",
        "category": "Earth",
        "subcategory": "Weather",
        "question": "What is the term for snow that has been compacted and recrystallized?",
        "options": ["Firn", "Névé", "Glacier ice", "Powder"],
        "correct_answer": "Firn",
        "difficulty": "hard"
    },
    {
        "id": "ear_306",
        "category": "Earth",
        "subcategory": "Weather",
        "question": "What is a downburst in meteorological terms?",
        "options": ["Strong downward wind from thunderstorm", "Tornado formation", "Hurricane eye", "Blizzard condition"],
        "correct_answer": "Strong downward wind from thunderstorm",
        "difficulty": "hard"
    },
    {
        "id": "ear_307",
        "category": "Earth",
        "subcategory": "Weather",
        "question": "What causes a whiteout in winter weather?",
        "options": ["Blowing snow reducing visibility to near zero", "Heavy fog", "Ice crystals", "Cloud cover"],
        "correct_answer": "Blowing snow reducing visibility to near zero",
        "difficulty": "medium"
    },
    {
        "id": "ear_308",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "Which ocean is the saltiest?",
        "options": ["Atlantic Ocean", "Pacific Ocean", "Indian Ocean", "Arctic Ocean"],
        "correct_answer": "Atlantic Ocean",
        "difficulty": "hard"
    },
    {
        "id": "ear_309",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "What is the smallest ocean on Earth?",
        "options": ["Arctic Ocean", "Indian Ocean", "Southern Ocean", "Atlantic Ocean"],
        "correct_answer": "Arctic Ocean",
        "difficulty": "medium"
    },
    {
        "id": "ear_310",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "Which country has the longest coastline in the world?",
        "options": ["Canada", "Russia", "Indonesia", "Australia"],
        "correct_answer": "Canada",
        "difficulty": "hard"
    },
    {
        "id": "ear_311",
        "category": "Earth",
        "subcategory": "Trees",
        "question": "Which tree species can clone itself through root sprouting?",
        "options": ["Quaking aspen", "Oak", "Pine", "Willow"],
        "correct_answer": "Quaking aspen",
        "difficulty": "hard"
    },
    {
        "id": "ear_312",
        "category": "Earth",
        "subcategory": "Trees",
        "question": "What is the only tree that naturally grows in both northern and southern hemispheres?",
        "options": ["Mangrove", "Palm", "Pine", "Eucalyptus"],
        "correct_answer": "Mangrove",
        "difficulty": "hard"
    },
    {
        "id": "ear_313",
        "category": "Earth",
        "subcategory": "Plants",
        "question": "Which plant is known as the 'corpse flower' due to its smell?",
        "options": ["Titan arum", "Rafflesia", "Skunk cabbage", "Dragon arum"],
        "correct_answer": "Titan arum",
        "difficulty": "hard"
    },
    {
        "id": "ear_314",
        "category": "Earth",
        "subcategory": "Plants",
        "question": "What is the smallest flowering plant in the world?",
        "options": ["Wolffia (watermeal)", "Baby's tears", "Pearlwort", "Duckweed"],
        "correct_answer": "Wolffia (watermeal)",
        "difficulty": "hard"
    }
]

# Add replacements
data['categories']['Earth'].extend(replacements)

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ Added {len(replacements)} replacement Earth questions")
print(f"IDs: ear_301 to ear_314")
print(f"Total Earth questions: {len(data['categories']['Earth'])}")
