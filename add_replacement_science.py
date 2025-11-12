import json

# Load the current database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Find highest Science ID
science_ids = [q['id'] for q in data['categories']['Science']]
science_ids.sort()
print(f"Last Science ID: {science_ids[-1]}")

# New replacement Science questions (5 total) - sci_210 to sci_214
new_science_questions = [
    {
        "id": "sci_210",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the largest internal organ in the human body?",
        "options": ["Liver", "Heart", "Brain", "Stomach"],
        "correct_answer": "Liver",
        "difficulty": "medium"
    },
    {
        "id": "sci_211",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the speed limit of the universe according to Einstein's theory?",
        "options": ["Speed of light", "Speed of sound", "Speed of gravity", "Speed of electricity"],
        "correct_answer": "Speed of light",
        "difficulty": "medium"
    },
    {
        "id": "sci_212",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "Which planet rotates on its side?",
        "options": ["Uranus", "Saturn", "Neptune", "Jupiter"],
        "correct_answer": "Uranus",
        "difficulty": "hard"
    },
    {
        "id": "sci_213",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is the chemical symbol for potassium?",
        "options": ["K", "P", "Po", "Pt"],
        "correct_answer": "K",
        "difficulty": "hard"
    },
    {
        "id": "sci_214",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the study of fungi called?",
        "options": ["Mycology", "Botany", "Zoology", "Bacteriology"],
        "correct_answer": "Mycology",
        "difficulty": "hard"
    }
]

# Add the new questions
data['categories']['Science'].extend(new_science_questions)
data['categories']['Science'].sort(key=lambda x: x['id'])

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Added {len(new_science_questions)} replacement Science questions")
print(f"New Science total: {len(data['categories']['Science'])} questions")
