import json

# Load database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# 21 unique replacement questions
# Distribution: Chemistry (6), Biology (6), Physics (5), Astronomy (4)
replacements = [
    # Chemistry (6 questions)
    {
        "id": "sci_301",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is the only metal that is liquid at standard room temperature?",
        "options": ["Mercury", "Gallium", "Bromine", "Cesium"],
        "correct_answer": "Mercury",
        "difficulty": "medium"
    },
    {
        "id": "sci_302",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "Which element has the symbol 'K' on the periodic table?",
        "options": ["Potassium", "Krypton", "Kalium", "Ketone"],
        "correct_answer": "Potassium",
        "difficulty": "hard"
    },
    {
        "id": "sci_303",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What type of reaction absorbs energy from its surroundings?",
        "options": ["Endothermic", "Exothermic", "Combustion", "Synthesis"],
        "correct_answer": "Endothermic",
        "difficulty": "hard"
    },
    {
        "id": "sci_304",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "Which gas makes up approximately 21% of Earth's atmosphere?",
        "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Argon"],
        "correct_answer": "Oxygen",
        "difficulty": "easy"
    },
    {
        "id": "sci_305",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is the chemical name for table salt?",
        "options": ["Sodium chloride", "Potassium chloride", "Sodium carbonate", "Calcium chloride"],
        "correct_answer": "Sodium chloride",
        "difficulty": "medium"
    },
    {
        "id": "sci_306",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "Which element is essential for organic compounds?",
        "options": ["Carbon", "Hydrogen", "Oxygen", "Nitrogen"],
        "correct_answer": "Carbon",
        "difficulty": "easy"
    },

    # Biology (6 questions)
    {
        "id": "sci_307",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the basic unit of heredity?",
        "options": ["Gene", "Chromosome", "DNA", "Protein"],
        "correct_answer": "Gene",
        "difficulty": "medium"
    },
    {
        "id": "sci_308",
        "category": "Science",
        "subcategory": "Biology",
        "question": "Which system in the human body is responsible for transporting oxygen?",
        "options": ["Circulatory system", "Respiratory system", "Nervous system", "Digestive system"],
        "correct_answer": "Circulatory system",
        "difficulty": "easy"
    },
    {
        "id": "sci_309",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the process by which organisms produce offspring?",
        "options": ["Reproduction", "Photosynthesis", "Respiration", "Digestion"],
        "correct_answer": "Reproduction",
        "difficulty": "easy"
    },
    {
        "id": "sci_310",
        "category": "Science",
        "subcategory": "Biology",
        "question": "Which protein gives blood its red color?",
        "options": ["Hemoglobin", "Myoglobin", "Albumin", "Fibrinogen"],
        "correct_answer": "Hemoglobin",
        "difficulty": "medium"
    },
    {
        "id": "sci_311",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the largest artery in the human body?",
        "options": ["Aorta", "Pulmonary artery", "Carotid artery", "Femoral artery"],
        "correct_answer": "Aorta",
        "difficulty": "hard"
    },
    {
        "id": "sci_312",
        "category": "Science",
        "subcategory": "Biology",
        "question": "Which organelle contains the cell's genetic material?",
        "options": ["Nucleus", "Mitochondria", "Ribosome", "Golgi apparatus"],
        "correct_answer": "Nucleus",
        "difficulty": "easy"
    },

    # Physics (5 questions)
    {
        "id": "sci_313",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the SI unit of power?",
        "options": ["Watt", "Joule", "Newton", "Volt"],
        "correct_answer": "Watt",
        "difficulty": "medium"
    },
    {
        "id": "sci_314",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the formula for calculating work?",
        "options": ["Force × Distance", "Mass × Acceleration", "Force × Time", "Power × Time"],
        "correct_answer": "Force × Distance",
        "difficulty": "hard"
    },
    {
        "id": "sci_315",
        "category": "Science",
        "subcategory": "Physics",
        "question": "Which law states that objects at rest stay at rest unless acted upon by an external force?",
        "options": ["Newton's first law", "Newton's second law", "Newton's third law", "Law of gravity"],
        "correct_answer": "Newton's first law",
        "difficulty": "medium"
    },
    {
        "id": "sci_316",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the boiling point of water at sea level in Celsius?",
        "options": ["100°C", "212°C", "0°C", "50°C"],
        "correct_answer": "100°C",
        "difficulty": "easy"
    },
    {
        "id": "sci_317",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What type of wave requires a medium to travel through?",
        "options": ["Mechanical wave", "Electromagnetic wave", "Light wave", "Radio wave"],
        "correct_answer": "Mechanical wave",
        "difficulty": "hard"
    },

    # Astronomy (4 questions)
    {
        "id": "sci_318",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Mercury"],
        "correct_answer": "Mars",
        "difficulty": "easy"
    },
    {
        "id": "sci_319",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is the term for a star system with two stars?",
        "options": ["Binary star system", "Double star", "Twin stars", "Pair stars"],
        "correct_answer": "Binary star system",
        "difficulty": "hard"
    },
    {
        "id": "sci_320",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is the age of our solar system approximately?",
        "options": ["4.6 billion years", "13.8 billion years", "1 billion years", "10 billion years"],
        "correct_answer": "4.6 billion years",
        "difficulty": "hard"
    },
    {
        "id": "sci_321",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What causes tides on Earth?",
        "options": ["Moon's gravitational pull", "Sun's heat", "Earth's rotation", "Ocean currents"],
        "correct_answer": "Moon's gravitational pull",
        "difficulty": "medium"
    }
]

# Add replacements
data['categories']['Science'].extend(replacements)

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ Added {len(replacements)} replacement Science questions")
print(f"IDs: sci_301 to sci_321")
print(f"Total Science questions: {len(data['categories']['Science'])}")
