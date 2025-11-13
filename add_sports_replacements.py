import json

# Load the current database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# 10 replacement Sports questions - being VERY specific and unique
new_sports_questions = [
    {
        "id": "spt_261",
        "category": "Sports",
        "subcategory": "Basketball",
        "question": "What violation occurs when a player dribbles, stops, then dribbles again?",
        "options": ["Double dribble", "Traveling", "Carrying", "Palming"],
        "correct_answer": "Double dribble",
        "difficulty": "medium"
    },
    {
        "id": "spt_262",
        "category": "Sports",
        "subcategory": "Soccer",
        "question": "What is the penalty for a handball in the penalty area?",
        "options": ["Penalty kick", "Free kick", "Corner kick", "Yellow card"],
        "correct_answer": "Penalty kick",
        "difficulty": "medium"
    },
    {
        "id": "spt_263",
        "category": "Sports",
        "subcategory": "Tennis",
        "question": "What is the area between the baseline and service line called?",
        "options": ["No man's land", "The alley", "The court", "The box"],
        "correct_answer": "No man's land",
        "difficulty": "hard"
    },
    {
        "id": "spt_264",
        "category": "Sports",
        "subcategory": "Golf",
        "question": "What is three strokes under par on a hole called?",
        "options": ["Albatross", "Eagle", "Birdie", "Condor"],
        "correct_answer": "Albatross",
        "difficulty": "hard"
    },
    {
        "id": "spt_265",
        "category": "Sports",
        "subcategory": "Baseball",
        "question": "What is it called when a batter gets on base due to four balls?",
        "options": ["Walk", "Hit by pitch", "Single", "Error"],
        "correct_answer": "Walk",
        "difficulty": "easy"
    },
    {
        "id": "spt_266",
        "category": "Sports",
        "subcategory": "American Football",
        "question": "What is the offensive line position in the center called?",
        "options": ["Center", "Guard", "Tackle", "Tight end"],
        "correct_answer": "Center",
        "difficulty": "medium"
    },
    {
        "id": "spt_267",
        "category": "Sports",
        "subcategory": "Hockey",
        "question": "What is the area in front of the goal called?",
        "options": ["Crease", "Slot", "Circle", "Zone"],
        "correct_answer": "Crease",
        "difficulty": "medium"
    },
    {
        "id": "spt_268",
        "category": "Sports",
        "subcategory": "Olympics",
        "question": "What event combines cross-country skiing and rifle shooting?",
        "options": ["Biathlon", "Nordic combined", "Pentathlon", "Decathlon"],
        "correct_answer": "Biathlon",
        "difficulty": "hard"
    },
    {
        "id": "spt_269",
        "category": "Sports",
        "subcategory": "Basketball",
        "question": "How long is the shot clock in the NBA?",
        "options": ["24 seconds", "30 seconds", "20 seconds", "35 seconds"],
        "correct_answer": "24 seconds",
        "difficulty": "hard"
    },
    {
        "id": "spt_270",
        "category": "Sports",
        "subcategory": "Soccer",
        "question": "How many substitutions are typically allowed in a standard soccer match?",
        "options": ["3", "5", "Unlimited", "7"],
        "correct_answer": "3",
        "difficulty": "medium"
    }
]

# Add the new questions
data['categories']['Sports'].extend(new_sports_questions)
data['categories']['Sports'].sort(key=lambda x: x['id'])

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Added {len(new_sports_questions)} replacement Sports questions")
print(f"New Sports total: {len(data['categories']['Sports'])} questions")
