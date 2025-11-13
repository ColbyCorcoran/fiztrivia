import json

# Load database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# 13 unique replacement questions
replacements = [
    {
        "id": "his_301",
        "category": "History",
        "subcategory": "Modern History",
        "question": "Which country was the first to grant women the right to vote nationwide?",
        "options": ["New Zealand", "United States", "United Kingdom", "Australia"],
        "correct_answer": "New Zealand",
        "difficulty": "hard"
    },
    {
        "id": "his_302",
        "category": "History",
        "subcategory": "Modern History",
        "question": "What was the code name for the D-Day invasion?",
        "options": ["Operation Overlord", "Operation Barbarossa", "Operation Market Garden", "Operation Torch"],
        "correct_answer": "Operation Overlord",
        "difficulty": "hard"
    },
    {
        "id": "his_303",
        "category": "History",
        "subcategory": "Modern History",
        "question": "Which country did the United States purchase Alaska from?",
        "options": ["Russia", "Canada", "United Kingdom", "Denmark"],
        "correct_answer": "Russia",
        "difficulty": "medium"
    },
    {
        "id": "his_304",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "What was the ancient Roman aqueduct system primarily used for?",
        "options": ["Transporting water", "Military defense", "Trade routes", "Religious ceremonies"],
        "correct_answer": "Transporting water",
        "difficulty": "easy"
    },
    {
        "id": "his_305",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "Which ancient Greek city-state was known for its democracy?",
        "options": ["Athens", "Sparta", "Thebes", "Corinth"],
        "correct_answer": "Athens",
        "difficulty": "easy"
    },
    {
        "id": "his_306",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "What was the writing system of ancient Mesopotamia called?",
        "options": ["Cuneiform", "Hieroglyphics", "Linear B", "Phoenician alphabet"],
        "correct_answer": "Cuneiform",
        "difficulty": "hard"
    },
    {
        "id": "his_307",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "Which Roman emperor was known as 'the Mad Emperor' and allegedly made his horse a consul?",
        "options": ["Caligula", "Nero", "Commodus", "Elagabalus"],
        "correct_answer": "Caligula",
        "difficulty": "hard"
    },
    {
        "id": "his_308",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What was the name of the plague that devastated Europe in the 14th century?",
        "options": ["Black Death", "Spanish Flu", "Antonine Plague", "Plague of Justinian"],
        "correct_answer": "Black Death",
        "difficulty": "easy"
    },
    {
        "id": "his_309",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "Which empire conquered Constantinople in 1453?",
        "options": ["Ottoman Empire", "Mongol Empire", "Persian Empire", "Holy Roman Empire"],
        "correct_answer": "Ottoman Empire",
        "difficulty": "medium"
    },
    {
        "id": "his_310",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What was the name of the document that limited the power of the English monarch in 1215?",
        "options": ["Magna Carta", "Bill of Rights", "Petition of Right", "Habeas Corpus Act"],
        "correct_answer": "Magna Carta",
        "difficulty": "easy"
    },
    {
        "id": "his_311",
        "category": "History",
        "subcategory": "Church History",
        "question": "Which council established the Nicene Creed?",
        "options": ["Council of Nicaea", "Council of Trent", "Council of Chalcedon", "Council of Constantinople"],
        "correct_answer": "Council of Nicaea",
        "difficulty": "medium"
    },
    {
        "id": "his_312",
        "category": "History",
        "subcategory": "Church History",
        "question": "What was the name of the movement to convert pagans to Christianity in medieval Europe?",
        "options": ["Christianization", "Crusades", "Inquisition", "Reformation"],
        "correct_answer": "Christianization",
        "difficulty": "medium"
    },
    {
        "id": "his_313",
        "category": "History",
        "subcategory": "Church History",
        "question": "Which reformer translated the New Testament into German?",
        "options": ["Martin Luther", "John Calvin", "Huldrych Zwingli", "John Wycliffe"],
        "correct_answer": "Martin Luther",
        "difficulty": "medium"
    }
]

# Add replacements
data['categories']['History'].extend(replacements)

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ Added {len(replacements)} replacement History questions")
print(f"IDs: his_301 to his_313")
print(f"Total History questions: {len(data['categories']['History'])}")
