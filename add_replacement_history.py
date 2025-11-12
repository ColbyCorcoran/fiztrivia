import json

# Load the current database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Find highest History ID
history_ids = [q['id'] for q in data['categories']['History']]
history_ids.sort()
print(f"Last History ID: {history_ids[-1]}")

# New replacement History questions (8 total) - his_202 to his_209
new_history_questions = [
    {
        "id": "his_202",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "What ancient library was located in Egypt and destroyed by fire?",
        "options": ["Library of Alexandria", "Library of Pergamum", "Library of Nineveh", "Library of Athens"],
        "correct_answer": "Library of Alexandria",
        "difficulty": "medium"
    },
    {
        "id": "his_203",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "What writing system did ancient Mesopotamians use?",
        "options": ["Cuneiform", "Hieroglyphics", "Sanskrit", "Pictographs"],
        "correct_answer": "Cuneiform",
        "difficulty": "hard"
    },
    {
        "id": "his_204",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What was the name of the Viking explorer who reached North America around 1000 AD?",
        "options": ["Leif Erikson", "Erik the Red", "Ragnar Lothbrok", "Bjorn Ironside"],
        "correct_answer": "Leif Erikson",
        "difficulty": "hard"
    },
    {
        "id": "his_205",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What disease was known as the 'sweating sickness' in Tudor England?",
        "options": ["English sweating sickness", "Plague", "Typhoid", "Cholera"],
        "correct_answer": "English sweating sickness",
        "difficulty": "hard"
    },
    {
        "id": "his_206",
        "category": "History",
        "subcategory": "Modern History",
        "question": "What year did Nelson Mandela become President of South Africa?",
        "options": ["1994", "1990", "1989", "1995"],
        "correct_answer": "1994",
        "difficulty": "medium"
    },
    {
        "id": "his_207",
        "category": "History",
        "subcategory": "Modern History",
        "question": "Which country gifted the Statue of Liberty to the United States?",
        "options": ["France", "England", "Spain", "Italy"],
        "correct_answer": "France",
        "difficulty": "easy"
    },
    {
        "id": "his_208",
        "category": "History",
        "subcategory": "Church History",
        "question": "What year was the King James Bible first published?",
        "options": ["1611", "1517", "1455", "1689"],
        "correct_answer": "1611",
        "difficulty": "hard"
    },
    {
        "id": "his_209",
        "category": "History",
        "subcategory": "Church History",
        "question": "What religious group was founded by George Fox in the 17th century?",
        "options": ["Quakers", "Methodists", "Baptists", "Presbyterians"],
        "correct_answer": "Quakers",
        "difficulty": "hard"
    }
]

# Add the new questions
data['categories']['History'].extend(new_history_questions)
data['categories']['History'].sort(key=lambda x: x['id'])

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Added {len(new_history_questions)} replacement History questions")
print(f"New History total: {len(data['categories']['History'])} questions")
