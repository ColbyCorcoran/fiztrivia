import json

# Load the current database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# 9 replacement History questions - being VERY specific and unique
new_history_questions = [
    {
        "id": "his_260",
        "category": "History",
        "subcategory": "Modern History",
        "question": "What year did the construction of the Panama Canal complete?",
        "options": ["1914", "1904", "1920", "1898"],
        "correct_answer": "1914",
        "difficulty": "hard"
    },
    {
        "id": "his_261",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "What metal did the Bronze Age get its name from?",
        "options": ["Bronze (copper and tin alloy)", "Iron", "Gold", "Silver"],
        "correct_answer": "Bronze (copper and tin alloy)",
        "difficulty": "medium"
    },
    {
        "id": "his_262",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What title did the leader of the Mongol Empire hold?",
        "options": ["Khan", "Sultan", "Emperor", "Caliph"],
        "correct_answer": "Khan",
        "difficulty": "medium"
    },
    {
        "id": "his_263",
        "category": "History",
        "subcategory": "Church History",
        "question": "What religious movement emphasized predestination and was founded by John Calvin?",
        "options": ["Calvinism", "Lutheranism", "Anglicanism", "Methodism"],
        "correct_answer": "Calvinism",
        "difficulty": "hard"
    },
    {
        "id": "his_264",
        "category": "History",
        "subcategory": "Modern History",
        "question": "Which two cities were hit by atomic bombs in 1945?",
        "options": ["Hiroshima and Nagasaki", "Tokyo and Kyoto", "Osaka and Kobe", "Nagoya and Yokohama"],
        "correct_answer": "Hiroshima and Nagasaki",
        "difficulty": "medium"
    },
    {
        "id": "his_265",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "What ancient trade route connected China to the Mediterranean?",
        "options": ["Silk Road", "Spice Route", "Amber Road", "Incense Route"],
        "correct_answer": "Silk Road",
        "difficulty": "medium"
    },
    {
        "id": "his_266",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What disease was also known as the 'Black Death'?",
        "options": ["Bubonic plague", "Smallpox", "Cholera", "Typhus"],
        "correct_answer": "Bubonic plague",
        "difficulty": "easy"
    },
    {
        "id": "his_267",
        "category": "History",
        "subcategory": "Church History",
        "question": "What year did Henry VIII establish the Church of England?",
        "options": ["1534", "1517", "1540", "1558"],
        "correct_answer": "1534",
        "difficulty": "hard"
    },
    {
        "id": "his_268",
        "category": "History",
        "subcategory": "Modern History",
        "question": "Which document declared the 13 American colonies independent from Britain?",
        "options": ["Declaration of Independence", "Constitution", "Bill of Rights", "Articles of Confederation"],
        "correct_answer": "Declaration of Independence",
        "difficulty": "easy"
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
