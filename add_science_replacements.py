import json

# Load the current database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# 11 replacement Science questions - being VERY specific and unique
new_science_questions = [
    {
        "id": "sci_265",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the study of motion without considering its causes called?",
        "options": ["Kinematics", "Dynamics", "Statics", "Mechanics"],
        "correct_answer": "Kinematics",
        "difficulty": "hard"
    },
    {
        "id": "sci_266",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is the process of a gas turning directly into a solid called?",
        "options": ["Deposition", "Sublimation", "Condensation", "Freezing"],
        "correct_answer": "Deposition",
        "difficulty": "hard"
    },
    {
        "id": "sci_267",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the green pigment in plants that captures sunlight?",
        "options": ["Chlorophyll", "Carotene", "Xanthophyll", "Anthocyanin"],
        "correct_answer": "Chlorophyll",
        "difficulty": "medium"
    },
    {
        "id": "sci_268",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is a comet's tail made of?",
        "options": ["Gas and dust", "Ice", "Rock", "Metal"],
        "correct_answer": "Gas and dust",
        "difficulty": "medium"
    },
    {
        "id": "sci_269",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the bending of waves around obstacles called?",
        "options": ["Diffraction", "Refraction", "Reflection", "Dispersion"],
        "correct_answer": "Diffraction",
        "difficulty": "hard"
    },
    {
        "id": "sci_270",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is the chemical symbol for silver?",
        "options": ["Ag", "Si", "Au", "Sr"],
        "correct_answer": "Ag",
        "difficulty": "medium"
    },
    {
        "id": "sci_271",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the control center of a cell called?",
        "options": ["Nucleus", "Mitochondria", "Ribosome", "Endoplasmic reticulum"],
        "correct_answer": "Nucleus",
        "difficulty": "easy"
    },
    {
        "id": "sci_272",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is the name of Mars' larger moon?",
        "options": ["Phobos", "Deimos", "Titan", "Europa"],
        "correct_answer": "Phobos",
        "difficulty": "hard"
    },
    {
        "id": "sci_273",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the SI unit of frequency?",
        "options": ["Hertz", "Watt", "Joule", "Volt"],
        "correct_answer": "Hertz",
        "difficulty": "medium"
    },
    {
        "id": "sci_274",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is the pH of a strong base?",
        "options": ["Greater than 7", "Equal to 7", "Less than 7", "Zero"],
        "correct_answer": "Greater than 7",
        "difficulty": "medium"
    },
    {
        "id": "sci_275",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the tough outer layer of a tree called?",
        "options": ["Bark", "Cambium", "Phloem", "Xylem"],
        "correct_answer": "Bark",
        "difficulty": "easy"
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
