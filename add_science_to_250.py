import json

# Load the current database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# New Science questions (sci_215 to sci_264) - 50 total
# Distribution: Astronomy (15), Physics (13), Biology (12), Chemistry (10)
new_science_questions = [
    # Astronomy (15 questions)
    {
        "id": "sci_215",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is the name of the galaxy that will collide with the Milky Way?",
        "options": ["Andromeda", "Triangulum", "Whirlpool", "Sombrero"],
        "correct_answer": "Andromeda",
        "difficulty": "hard"
    },
    {
        "id": "sci_216",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is the hottest planet in our solar system?",
        "options": ["Venus", "Mercury", "Mars", "Jupiter"],
        "correct_answer": "Venus",
        "difficulty": "medium"
    },
    {
        "id": "sci_217",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is the name of Saturn's largest moon?",
        "options": ["Titan", "Enceladus", "Rhea", "Iapetus"],
        "correct_answer": "Titan",
        "difficulty": "medium"
    },
    {
        "id": "sci_218",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What causes the Northern Lights (Aurora Borealis)?",
        "options": ["Solar wind particles hitting Earth's atmosphere", "Reflection of ice crystals", "Lightning in the upper atmosphere", "Volcanic activity"],
        "correct_answer": "Solar wind particles hitting Earth's atmosphere",
        "difficulty": "hard"
    },
    {
        "id": "sci_219",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "How long does it take light from the Sun to reach Earth?",
        "options": ["8 minutes", "1 hour", "1 day", "Instantly"],
        "correct_answer": "8 minutes",
        "difficulty": "medium"
    },
    {
        "id": "sci_220",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is a light-year a measure of?",
        "options": ["Distance", "Time", "Speed", "Brightness"],
        "correct_answer": "Distance",
        "difficulty": "medium"
    },
    {
        "id": "sci_221",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is the asteroid belt located between?",
        "options": ["Mars and Jupiter", "Earth and Mars", "Jupiter and Saturn", "Venus and Earth"],
        "correct_answer": "Mars and Jupiter",
        "difficulty": "medium"
    },
    {
        "id": "sci_222",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What type of celestial body is Pluto now classified as?",
        "options": ["Dwarf planet", "Asteroid", "Comet", "Moon"],
        "correct_answer": "Dwarf planet",
        "difficulty": "easy"
    },
    {
        "id": "sci_223",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is the Kuiper Belt?",
        "options": ["A region beyond Neptune with icy objects", "An asteroid belt", "A group of moons", "A type of nebula"],
        "correct_answer": "A region beyond Neptune with icy objects",
        "difficulty": "hard"
    },
    {
        "id": "sci_224",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is the name of the first human-made object to leave the solar system?",
        "options": ["Voyager 1", "Pioneer 10", "New Horizons", "Cassini"],
        "correct_answer": "Voyager 1",
        "difficulty": "hard"
    },
    {
        "id": "sci_225",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is the Oort Cloud?",
        "options": ["A theoretical cloud of comets", "A nebula", "A galaxy cluster", "A type of asteroid"],
        "correct_answer": "A theoretical cloud of comets",
        "difficulty": "hard"
    },
    {
        "id": "sci_226",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is the name of Jupiter's famous red spot?",
        "options": ["Great Red Spot", "Red Eye", "Crimson Storm", "Jupiter's Mark"],
        "correct_answer": "Great Red Spot",
        "difficulty": "easy"
    },
    {
        "id": "sci_227",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is a supernova?",
        "options": ["An exploding star", "A forming star", "A dying planet", "A black hole"],
        "correct_answer": "An exploding star",
        "difficulty": "medium"
    },
    {
        "id": "sci_228",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is the edge of a black hole called?",
        "options": ["Event horizon", "Singularity", "Photon sphere", "Schwarzschild radius"],
        "correct_answer": "Event horizon",
        "difficulty": "hard"
    },
    {
        "id": "sci_229",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "Which planet has the most moons?",
        "options": ["Saturn", "Jupiter", "Uranus", "Neptune"],
        "correct_answer": "Saturn",
        "difficulty": "hard"
    },
    
    # Physics (13 questions)
    {
        "id": "sci_230",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is Newton's first law of motion?",
        "options": ["An object in motion stays in motion unless acted upon", "Force equals mass times acceleration", "For every action there's an equal and opposite reaction", "Energy cannot be created or destroyed"],
        "correct_answer": "An object in motion stays in motion unless acted upon",
        "difficulty": "medium"
    },
    {
        "id": "sci_231",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the SI unit of force?",
        "options": ["Newton", "Joule", "Watt", "Pascal"],
        "correct_answer": "Newton",
        "difficulty": "medium"
    },
    {
        "id": "sci_232",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the acceleration due to gravity on Earth?",
        "options": ["9.8 m/s²", "10 m/s²", "8.9 m/s²", "11 m/s²"],
        "correct_answer": "9.8 m/s²",
        "difficulty": "hard"
    },
    {
        "id": "sci_233",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What type of energy does a moving object have?",
        "options": ["Kinetic", "Potential", "Thermal", "Chemical"],
        "correct_answer": "Kinetic",
        "difficulty": "easy"
    },
    {
        "id": "sci_234",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the law of conservation of energy?",
        "options": ["Energy cannot be created or destroyed", "Energy always increases", "Energy always decreases", "Energy can be created but not destroyed"],
        "correct_answer": "Energy cannot be created or destroyed",
        "difficulty": "medium"
    },
    {
        "id": "sci_235",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the study of sound called?",
        "options": ["Acoustics", "Optics", "Thermodynamics", "Mechanics"],
        "correct_answer": "Acoustics",
        "difficulty": "medium"
    },
    {
        "id": "sci_236",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What particle has no electric charge?",
        "options": ["Neutron", "Proton", "Electron", "Positron"],
        "correct_answer": "Neutron",
        "difficulty": "easy"
    },
    {
        "id": "sci_237",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the formula for kinetic energy?",
        "options": ["½mv²", "mgh", "mc²", "Fd"],
        "correct_answer": "½mv²",
        "difficulty": "hard"
    },
    {
        "id": "sci_238",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the SI unit of power?",
        "options": ["Watt", "Joule", "Newton", "Volt"],
        "correct_answer": "Watt",
        "difficulty": "medium"
    },
    {
        "id": "sci_239",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the term for the rate of change of velocity?",
        "options": ["Acceleration", "Speed", "Momentum", "Force"],
        "correct_answer": "Acceleration",
        "difficulty": "medium"
    },
    {
        "id": "sci_240",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is plasma?",
        "options": ["The fourth state of matter", "A type of liquid", "Ionized gas", "Both the fourth state of matter and ionized gas"],
        "correct_answer": "Both the fourth state of matter and ionized gas",
        "difficulty": "hard"
    },
    {
        "id": "sci_241",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the speed of sound in air at room temperature?",
        "options": ["343 m/s", "300 m/s", "400 m/s", "500 m/s"],
        "correct_answer": "343 m/s",
        "difficulty": "hard"
    },
    {
        "id": "sci_242",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is friction?",
        "options": ["A force that opposes motion", "A type of energy", "A form of acceleration", "A state of matter"],
        "correct_answer": "A force that opposes motion",
        "difficulty": "easy"
    },
    
    # Biology (12 questions)
    {
        "id": "sci_243",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the basic unit of life?",
        "options": ["Cell", "Atom", "Molecule", "Tissue"],
        "correct_answer": "Cell",
        "difficulty": "easy"
    },
    {
        "id": "sci_244",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What molecule carries genetic information?",
        "options": ["DNA", "RNA", "Protein", "Lipid"],
        "correct_answer": "DNA",
        "difficulty": "easy"
    },
    {
        "id": "sci_245",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the process of cell division called?",
        "options": ["Mitosis", "Meiosis", "Photosynthesis", "Respiration"],
        "correct_answer": "Mitosis",
        "difficulty": "medium"
    },
    {
        "id": "sci_246",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the largest organ in the human body?",
        "options": ["Skin", "Liver", "Brain", "Lungs"],
        "correct_answer": "Skin",
        "difficulty": "medium"
    },
    {
        "id": "sci_247",
        "category": "Science",
        "subcategory": "Biology",
        "question": "How many bones are in the adult human body?",
        "options": ["206", "190", "215", "180"],
        "correct_answer": "206",
        "difficulty": "hard"
    },
    {
        "id": "sci_248",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the study of plants called?",
        "options": ["Botany", "Zoology", "Ecology", "Mycology"],
        "correct_answer": "Botany",
        "difficulty": "medium"
    },
    {
        "id": "sci_249",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the human body's largest bone?",
        "options": ["Femur", "Tibia", "Humerus", "Fibula"],
        "correct_answer": "Femur",
        "difficulty": "medium"
    },
    {
        "id": "sci_250",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What type of blood cells fight infection?",
        "options": ["White blood cells", "Red blood cells", "Platelets", "Plasma"],
        "correct_answer": "White blood cells",
        "difficulty": "medium"
    },
    {
        "id": "sci_251",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the colored part of the eye called?",
        "options": ["Iris", "Pupil", "Retina", "Cornea"],
        "correct_answer": "Iris",
        "difficulty": "medium"
    },
    {
        "id": "sci_252",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the longest muscle in the human body?",
        "options": ["Sartorius", "Quadriceps", "Gluteus maximus", "Biceps"],
        "correct_answer": "Sartorius",
        "difficulty": "hard"
    },
    {
        "id": "sci_253",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What percentage of the human body is water?",
        "options": ["60%", "50%", "70%", "80%"],
        "correct_answer": "60%",
        "difficulty": "medium"
    },
    {
        "id": "sci_254",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the smallest bone in the human body?",
        "options": ["Stapes (in the ear)", "Phalanx", "Carpal", "Metacarpal"],
        "correct_answer": "Stapes (in the ear)",
        "difficulty": "hard"
    },
    
    # Chemistry (10 questions)
    {
        "id": "sci_255",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is the symbol for gold on the periodic table?",
        "options": ["Au", "Ag", "Fe", "Cu"],
        "correct_answer": "Au",
        "difficulty": "medium"
    },
    {
        "id": "sci_256",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is the atomic number of carbon?",
        "options": ["6", "12", "8", "14"],
        "correct_answer": "6",
        "difficulty": "hard"
    },
    {
        "id": "sci_257",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is H2O?",
        "options": ["Water", "Hydrogen peroxide", "Hydroxide", "Hydrochloric acid"],
        "correct_answer": "Water",
        "difficulty": "easy"
    },
    {
        "id": "sci_258",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is table salt chemically known as?",
        "options": ["Sodium chloride", "Potassium chloride", "Calcium chloride", "Magnesium chloride"],
        "correct_answer": "Sodium chloride",
        "difficulty": "medium"
    },
    {
        "id": "sci_259",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is the lightest element?",
        "options": ["Hydrogen", "Helium", "Lithium", "Carbon"],
        "correct_answer": "Hydrogen",
        "difficulty": "easy"
    },
    {
        "id": "sci_260",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is the chemical formula for methane?",
        "options": ["CH4", "CO2", "C2H6", "C3H8"],
        "correct_answer": "CH4",
        "difficulty": "hard"
    },
    {
        "id": "sci_261",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is an acid with a pH less than?",
        "options": ["7", "5", "10", "14"],
        "correct_answer": "7",
        "difficulty": "medium"
    },
    {
        "id": "sci_262",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is the study of carbon compounds called?",
        "options": ["Organic chemistry", "Inorganic chemistry", "Physical chemistry", "Analytical chemistry"],
        "correct_answer": "Organic chemistry",
        "difficulty": "medium"
    },
    {
        "id": "sci_263",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is a substance made of only one type of atom called?",
        "options": ["Element", "Compound", "Mixture", "Solution"],
        "correct_answer": "Element",
        "difficulty": "medium"
    },
    {
        "id": "sci_264",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is the most reactive metal?",
        "options": ["Francium", "Sodium", "Potassium", "Lithium"],
        "correct_answer": "Francium",
        "difficulty": "hard"
    }
]

# Add the new questions to Science category
data['categories']['Science'].extend(new_science_questions)

# Sort Science questions by ID
data['categories']['Science'].sort(key=lambda x: x['id'])

# Save the updated database
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Added {len(new_science_questions)} new Science questions")
print(f"New Science total: {len(data['categories']['Science'])} questions")

# Show breakdown by subcategory
from collections import Counter
subcats = Counter(q['subcategory'] for q in data['categories']['Science'])
print("\nScience subcategory distribution:")
for subcat, count in sorted(subcats.items(), key=lambda x: x[1], reverse=True):
    print(f"  {subcat}: {count}")

# Show difficulty distribution of new questions
difficulties = Counter(q['difficulty'] for q in new_science_questions)
print(f"\nDifficulty distribution of new questions:")
for diff, count in sorted(difficulties.items()):
    print(f"  {diff}: {count}")
