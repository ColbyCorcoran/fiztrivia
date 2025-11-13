import json

# Load database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# 51 new Science questions (sci_250 to sci_300)
# Distribution: Chemistry (13), Biology (13), Physics (13), Astronomy (12)
# Emphasis on hard/medium difficulty

new_questions = [
    # Chemistry (13 questions) - sci_250-262
    {
        "id": "sci_250",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is the most abundant gas in Earth's atmosphere?",
        "options": ["Nitrogen", "Oxygen", "Carbon dioxide", "Argon"],
        "correct_answer": "Nitrogen",
        "difficulty": "easy"
    },
    {
        "id": "sci_251",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is the pH of pure water at 25°C?",
        "options": ["7", "0", "14", "10"],
        "correct_answer": "7",
        "difficulty": "medium"
    },
    {
        "id": "sci_252",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "Which element has the highest electronegativity?",
        "options": ["Fluorine", "Oxygen", "Chlorine", "Nitrogen"],
        "correct_answer": "Fluorine",
        "difficulty": "hard"
    },
    {
        "id": "sci_253",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is Avogadro's number?",
        "options": ["6.022 × 10²³", "6.626 × 10⁻³⁴", "3.14159", "2.998 × 10⁸"],
        "correct_answer": "6.022 × 10²³",
        "difficulty": "hard"
    },
    {
        "id": "sci_254",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "Which type of bond involves the sharing of electron pairs?",
        "options": ["Covalent bond", "Ionic bond", "Metallic bond", "Hydrogen bond"],
        "correct_answer": "Covalent bond",
        "difficulty": "medium"
    },
    {
        "id": "sci_255",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is the chemical symbol for tungsten?",
        "options": ["W", "T", "Tu", "Tg"],
        "correct_answer": "W",
        "difficulty": "hard"
    },
    {
        "id": "sci_256",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "Which element is liquid at room temperature besides mercury?",
        "options": ["Bromine", "Gallium", "Cesium", "Francium"],
        "correct_answer": "Bromine",
        "difficulty": "hard"
    },
    {
        "id": "sci_257",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What process do plants use to convert light energy into chemical energy?",
        "options": ["Photosynthesis", "Respiration", "Fermentation", "Oxidation"],
        "correct_answer": "Photosynthesis",
        "difficulty": "easy"
    },
    {
        "id": "sci_258",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "Which noble gas is used in neon signs?",
        "options": ["Neon", "Argon", "Helium", "Krypton"],
        "correct_answer": "Neon",
        "difficulty": "easy"
    },
    {
        "id": "sci_259",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is the lightest element in the periodic table?",
        "options": ["Hydrogen", "Helium", "Lithium", "Carbon"],
        "correct_answer": "Hydrogen",
        "difficulty": "easy"
    },
    {
        "id": "sci_260",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "Which acid is found in vinegar?",
        "options": ["Acetic acid", "Citric acid", "Sulfuric acid", "Hydrochloric acid"],
        "correct_answer": "Acetic acid",
        "difficulty": "medium"
    },
    {
        "id": "sci_261",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is the molecular formula for water?",
        "options": ["H₂O", "H₂O₂", "HO", "H₃O"],
        "correct_answer": "H₂O",
        "difficulty": "easy"
    },
    {
        "id": "sci_262",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "Which element has the atomic number 79?",
        "options": ["Gold", "Silver", "Platinum", "Copper"],
        "correct_answer": "Gold",
        "difficulty": "hard"
    },

    # Biology (13 questions) - sci_263-275
    {
        "id": "sci_263",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the largest organ in the human body?",
        "options": ["Skin", "Liver", "Brain", "Heart"],
        "correct_answer": "Skin",
        "difficulty": "easy"
    },
    {
        "id": "sci_264",
        "category": "Science",
        "subcategory": "Biology",
        "question": "How many chromosomes do humans have?",
        "options": ["46", "23", "48", "44"],
        "correct_answer": "46",
        "difficulty": "medium"
    },
    {
        "id": "sci_265",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the process by which cells divide to produce two identical daughter cells?",
        "options": ["Mitosis", "Meiosis", "Fission", "Budding"],
        "correct_answer": "Mitosis",
        "difficulty": "medium"
    },
    {
        "id": "sci_266",
        "category": "Science",
        "subcategory": "Biology",
        "question": "Which blood type is known as the universal donor?",
        "options": ["O negative", "AB positive", "A positive", "B negative"],
        "correct_answer": "O negative",
        "difficulty": "medium"
    },
    {
        "id": "sci_267",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the name of the molecule that carries genetic information?",
        "options": ["DNA", "RNA", "Protein", "Lipid"],
        "correct_answer": "DNA",
        "difficulty": "easy"
    },
    {
        "id": "sci_268",
        "category": "Science",
        "subcategory": "Biology",
        "question": "Which organelle is responsible for protein synthesis?",
        "options": ["Ribosome", "Golgi apparatus", "Lysosome", "Peroxisome"],
        "correct_answer": "Ribosome",
        "difficulty": "hard"
    },
    {
        "id": "sci_269",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the smallest unit of life?",
        "options": ["Cell", "Atom", "Molecule", "Tissue"],
        "correct_answer": "Cell",
        "difficulty": "easy"
    },
    {
        "id": "sci_270",
        "category": "Science",
        "subcategory": "Biology",
        "question": "Which part of the brain controls balance and coordination?",
        "options": ["Cerebellum", "Cerebrum", "Medulla", "Hypothalamus"],
        "correct_answer": "Cerebellum",
        "difficulty": "hard"
    },
    {
        "id": "sci_271",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the study of fungi called?",
        "options": ["Mycology", "Botany", "Zoology", "Microbiology"],
        "correct_answer": "Mycology",
        "difficulty": "hard"
    },
    {
        "id": "sci_272",
        "category": "Science",
        "subcategory": "Biology",
        "question": "Which vitamin is produced when skin is exposed to sunlight?",
        "options": ["Vitamin D", "Vitamin C", "Vitamin A", "Vitamin K"],
        "correct_answer": "Vitamin D",
        "difficulty": "medium"
    },
    {
        "id": "sci_273",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the gestation period of a human pregnancy?",
        "options": ["9 months", "10 months", "8 months", "7 months"],
        "correct_answer": "9 months",
        "difficulty": "easy"
    },
    {
        "id": "sci_274",
        "category": "Science",
        "subcategory": "Biology",
        "question": "Which biological process converts food into energy?",
        "options": ["Cellular respiration", "Photosynthesis", "Digestion", "Metabolism"],
        "correct_answer": "Cellular respiration",
        "difficulty": "medium"
    },
    {
        "id": "sci_275",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the largest bone in the human body?",
        "options": ["Femur", "Tibia", "Humerus", "Fibula"],
        "correct_answer": "Femur",
        "difficulty": "easy"
    },

    # Physics (13 questions) - sci_276-288
    {
        "id": "sci_276",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the SI unit of force?",
        "options": ["Newton", "Joule", "Watt", "Pascal"],
        "correct_answer": "Newton",
        "difficulty": "medium"
    },
    {
        "id": "sci_277",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What law states that for every action, there is an equal and opposite reaction?",
        "options": ["Newton's third law", "Newton's first law", "Law of gravity", "Law of inertia"],
        "correct_answer": "Newton's third law",
        "difficulty": "medium"
    },
    {
        "id": "sci_278",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the speed of sound in air at sea level?",
        "options": ["343 m/s", "300 m/s", "400 m/s", "500 m/s"],
        "correct_answer": "343 m/s",
        "difficulty": "hard"
    },
    {
        "id": "sci_279",
        "category": "Science",
        "subcategory": "Physics",
        "question": "Which fundamental force is responsible for holding atomic nuclei together?",
        "options": ["Strong nuclear force", "Weak nuclear force", "Electromagnetic force", "Gravity"],
        "correct_answer": "Strong nuclear force",
        "difficulty": "hard"
    },
    {
        "id": "sci_280",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is absolute zero in Kelvin?",
        "options": ["0 K", "-273 K", "273 K", "-100 K"],
        "correct_answer": "0 K",
        "difficulty": "medium"
    },
    {
        "id": "sci_281",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What phenomenon explains why light bends when passing through a prism?",
        "options": ["Refraction", "Reflection", "Diffraction", "Interference"],
        "correct_answer": "Refraction",
        "difficulty": "medium"
    },
    {
        "id": "sci_282",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the SI unit of electrical current?",
        "options": ["Ampere", "Volt", "Ohm", "Coulomb"],
        "correct_answer": "Ampere",
        "difficulty": "medium"
    },
    {
        "id": "sci_283",
        "category": "Science",
        "subcategory": "Physics",
        "question": "Who formulated the uncertainty principle in quantum mechanics?",
        "options": ["Werner Heisenberg", "Erwin Schrödinger", "Niels Bohr", "Max Planck"],
        "correct_answer": "Werner Heisenberg",
        "difficulty": "hard"
    },
    {
        "id": "sci_284",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the acceleration due to gravity on Earth's surface?",
        "options": ["9.8 m/s²", "10 m/s²", "9.5 m/s²", "11 m/s²"],
        "correct_answer": "9.8 m/s²",
        "difficulty": "medium"
    },
    {
        "id": "sci_285",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What type of energy does a moving object possess?",
        "options": ["Kinetic energy", "Potential energy", "Thermal energy", "Chemical energy"],
        "correct_answer": "Kinetic energy",
        "difficulty": "easy"
    },
    {
        "id": "sci_286",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the law of conservation of energy?",
        "options": ["Energy cannot be created or destroyed", "Energy always increases", "Energy always decreases", "Energy can appear from nothing"],
        "correct_answer": "Energy cannot be created or destroyed",
        "difficulty": "medium"
    },
    {
        "id": "sci_287",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the electromagnetic spectrum range that humans can see?",
        "options": ["Visible light", "Infrared", "Ultraviolet", "X-rays"],
        "correct_answer": "Visible light",
        "difficulty": "easy"
    },
    {
        "id": "sci_288",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is Planck's constant approximately equal to?",
        "options": ["6.626 × 10⁻³⁴ J·s", "6.022 × 10²³", "3.00 × 10⁸ m/s", "1.602 × 10⁻¹⁹ C"],
        "correct_answer": "6.626 × 10⁻³⁴ J·s",
        "difficulty": "hard"
    },

    # Astronomy (12 questions) - sci_289-300
    {
        "id": "sci_289",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is the largest planet in our solar system?",
        "options": ["Jupiter", "Saturn", "Neptune", "Uranus"],
        "correct_answer": "Jupiter",
        "difficulty": "easy"
    },
    {
        "id": "sci_290",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "How long does it take for light from the Sun to reach Earth?",
        "options": ["8 minutes", "1 second", "1 hour", "1 day"],
        "correct_answer": "8 minutes",
        "difficulty": "medium"
    },
    {
        "id": "sci_291",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is the name of the galaxy that contains our solar system?",
        "options": ["Milky Way", "Andromeda", "Triangulum", "Sombrero"],
        "correct_answer": "Milky Way",
        "difficulty": "easy"
    },
    {
        "id": "sci_292",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "Which planet is known for its prominent ring system?",
        "options": ["Saturn", "Jupiter", "Uranus", "Neptune"],
        "correct_answer": "Saturn",
        "difficulty": "easy"
    },
    {
        "id": "sci_293",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is a supernova?",
        "options": ["An exploding star", "A new star", "A black hole", "A comet"],
        "correct_answer": "An exploding star",
        "difficulty": "medium"
    },
    {
        "id": "sci_294",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is the closest star to Earth besides the Sun?",
        "options": ["Proxima Centauri", "Alpha Centauri", "Sirius", "Betelgeuse"],
        "correct_answer": "Proxima Centauri",
        "difficulty": "hard"
    },
    {
        "id": "sci_295",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What phenomenon causes the Moon to appear red during a lunar eclipse?",
        "options": ["Rayleigh scattering", "Reflection", "Absorption", "Refraction"],
        "correct_answer": "Rayleigh scattering",
        "difficulty": "hard"
    },
    {
        "id": "sci_296",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "How many planets are in our solar system?",
        "options": ["8", "9", "7", "10"],
        "correct_answer": "8",
        "difficulty": "easy"
    },
    {
        "id": "sci_297",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is the largest moon of Saturn?",
        "options": ["Titan", "Europa", "Ganymede", "Callisto"],
        "correct_answer": "Titan",
        "difficulty": "hard"
    },
    {
        "id": "sci_298",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is the term for a rocky body that orbits the Sun?",
        "options": ["Asteroid", "Comet", "Meteor", "Satellite"],
        "correct_answer": "Asteroid",
        "difficulty": "medium"
    },
    {
        "id": "sci_299",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "Which planet has the shortest day (rotation period)?",
        "options": ["Jupiter", "Saturn", "Earth", "Mars"],
        "correct_answer": "Jupiter",
        "difficulty": "hard"
    },
    {
        "id": "sci_300",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is the name of the telescope launched by NASA in 1990?",
        "options": ["Hubble Space Telescope", "James Webb Space Telescope", "Spitzer Space Telescope", "Kepler Space Telescope"],
        "correct_answer": "Hubble Space Telescope",
        "difficulty": "medium"
    }
]

# Add new questions to Science category
data['categories']['Science'].extend(new_questions)

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ Added {len(new_questions)} Science questions")
print(f"New range: sci_250 to sci_300")
print(f"\nDistribution:")
print(f"  Chemistry: 13 questions")
print(f"  Biology: 13 questions")
print(f"  Physics: 13 questions")
print(f"  Astronomy: 12 questions")
print(f"\nTotal Science questions: {len(data['categories']['Science'])}")
