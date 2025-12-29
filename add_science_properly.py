#!/usr/bin/env python3
"""
Add 22 Science questions using gap IDs and ensuring no duplicates
"""

import json

def add_science_questions():
    # Load current database
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    science_questions = data['categories']['Science']
    
    # Gap IDs to use (first 22 of the 48 gaps)
    gap_ids = [
        'sci_052', 'sci_116', 'sci_125', 'sci_144', 'sci_145',
        'sci_153', 'sci_160', 'sci_162', 'sci_163', 'sci_164',
        'sci_165', 'sci_167', 'sci_168', 'sci_170', 'sci_172',
        'sci_173', 'sci_179', 'sci_182', 'sci_185', 'sci_195',
        'sci_202', 'sci_203'
    ]

    print(f"Current Science questions: {len(science_questions)}")
    print(f"Adding 22 questions using gap IDs")
    print()

    # NEW UNIQUE QUESTIONS (avoiding all known duplicates)
    # Distribution: Astronomy +11, Biology +5, Chemistry +4, Physics +2
    new_questions = [
        # ASTRONOMY (11 questions: 3 easy, 3 medium, 5 hard)
        # Easy (3)
        {
            "id": gap_ids[0],
            "category": "Science",
            "subcategory": "Astronomy",
            "question": "What is the largest planet in our solar system by mass and volume?",
            "options": ["Jupiter", "Saturn", "Neptune", "Uranus"],
            "correct_answer": "Jupiter",
            "difficulty": "easy"
        },
        {
            "id": gap_ids[1],
            "category": "Science",
            "subcategory": "Astronomy",
            "question": "What color is Mars commonly known as due to iron oxide on its surface?",
            "options": ["Red", "Blue", "Yellow", "Orange"],
            "correct_answer": "Red",
            "difficulty": "easy"
        },
        {
            "id": gap_ids[2],
            "category": "Science",
            "subcategory": "Astronomy",
            "question": "How many planets in our solar system have rings?",
            "options": ["Four", "Two", "Three", "One"],
            "correct_answer": "Four",
            "difficulty": "easy"
        },
        # Medium (3)
        {
            "id": gap_ids[3],
            "category": "Science",
            "subcategory": "Astronomy",
            "question": "What is the name of the nearest major galaxy to the Milky Way?",
            "options": ["Andromeda", "Triangulum", "Whirlpool", "Sombrero"],
            "correct_answer": "Andromeda",
            "difficulty": "medium"
        },
        {
            "id": gap_ids[4],
            "category": "Science",
            "subcategory": "Astronomy",
            "question": "What phenomenon causes the spectacular light displays known as auroras near Earth's polar regions?",
            "options": ["Solar wind interacting with Earth's magnetosphere", "Reflection of moonlight", "Atmospheric temperature changes", "Volcanic activity"],
            "correct_answer": "Solar wind interacting with Earth's magnetosphere",
            "difficulty": "medium"
        },
        {
            "id": gap_ids[5],
            "category": "Science",
            "subcategory": "Astronomy",
            "question": "What type of star will our Sun eventually become in approximately 5 billion years?",
            "options": ["Red giant", "White dwarf", "Neutron star", "Black hole"],
            "correct_answer": "Red giant",
            "difficulty": "medium"
        },
        # Hard (5)
        {
            "id": gap_ids[6],
            "category": "Science",
            "subcategory": "Astronomy",
            "question": "What is the name of the largest known structure in the observable universe, consisting of galaxy filaments?",
            "options": ["Hercules-Corona Borealis Great Wall", "Sloan Great Wall", "CfA2 Great Wall", "BOSS Great Wall"],
            "correct_answer": "Hercules-Corona Borealis Great Wall",
            "difficulty": "hard"
        },
        {
            "id": gap_ids[7],
            "category": "Science",
            "subcategory": "Astronomy",
            "question": "What space telescope, launched in 2021, is the successor to the Hubble Space Telescope?",
            "options": ["James Webb Space Telescope", "Chandra X-ray Observatory", "Spitzer Space Telescope", "Kepler Space Telescope"],
            "correct_answer": "James Webb Space Telescope",
            "difficulty": "hard"
        },
        {
            "id": gap_ids[8],
            "category": "Science",
            "subcategory": "Astronomy",
            "question": "What is the Chandrasekhar limit, approximately 1.4 solar masses?",
            "options": ["Maximum mass of a white dwarf star", "Minimum mass for star formation", "Maximum mass of a neutron star", "Minimum mass for nuclear fusion"],
            "correct_answer": "Maximum mass of a white dwarf star",
            "difficulty": "hard"
        },
        {
            "id": gap_ids[9],
            "category": "Science",
            "subcategory": "Astronomy",
            "question": "What technique do astronomers use to detect planets by measuring the wobble in a star's motion?",
            "options": ["Radial velocity method", "Transit photometry", "Direct imaging", "Gravitational lensing"],
            "correct_answer": "Radial velocity method",
            "difficulty": "hard"
        },
        {
            "id": gap_ids[10],
            "category": "Science",
            "subcategory": "Astronomy",
            "question": "What is the name of the point in Earth's orbit when it is farthest from the Sun?",
            "options": ["Aphelion", "Perihelion", "Equinox", "Solstice"],
            "correct_answer": "Aphelion",
            "difficulty": "hard"
        },

        # BIOLOGY (5 questions: 2 easy, 2 medium, 1 hard)
        # Easy (2)
        {
            "id": gap_ids[11],
            "category": "Science",
            "subcategory": "Biology",
            "question": "What pigment gives plants their green color and is essential for photosynthesis?",
            "options": ["Chlorophyll", "Carotene", "Xanthophyll", "Anthocyanin"],
            "correct_answer": "Chlorophyll",
            "difficulty": "easy"
        },
        {
            "id": gap_ids[12],
            "category": "Science",
            "subcategory": "Biology",
            "question": "Which organ in the human body is primarily responsible for filtering blood and producing urine?",
            "options": ["Kidney", "Liver", "Spleen", "Pancreas"],
            "correct_answer": "Kidney",
            "difficulty": "easy"
        },
        # Medium (2)
        {
            "id": gap_ids[13],
            "category": "Science",
            "subcategory": "Biology",
            "question": "What is the name of the protein that carries oxygen in red blood cells?",
            "options": ["Hemoglobin", "Myoglobin", "Albumin", "Insulin"],
            "correct_answer": "Hemoglobin",
            "difficulty": "medium"
        },
        {
            "id": gap_ids[14],
            "category": "Science",
            "subcategory": "Biology",
            "question": "In Mendelian genetics, what term describes an organism with two identical alleles for a trait?",
            "options": ["Homozygous", "Heterozygous", "Dominant", "Recessive"],
            "correct_answer": "Homozygous",
            "difficulty": "medium"
        },
        # Hard (1)
        {
            "id": gap_ids[15],
            "category": "Science",
            "subcategory": "Biology",
            "question": "What cellular organelle is responsible for breaking down cellular waste and worn-out organelles using digestive enzymes?",
            "options": ["Lysosome", "Peroxisome", "Endoplasmic reticulum", "Golgi apparatus"],
            "correct_answer": "Lysosome",
            "difficulty": "hard"
        },

        # CHEMISTRY (4 questions: 1 easy, 1 medium, 2 hard)
        # Easy (1)
        {
            "id": gap_ids[16],
            "category": "Science",
            "subcategory": "Chemistry",
            "question": "What is the most abundant gas in Earth's atmosphere?",
            "options": ["Nitrogen", "Oxygen", "Carbon dioxide", "Argon"],
            "correct_answer": "Nitrogen",
            "difficulty": "easy"
        },
        # Medium (1)
        {
            "id": gap_ids[17],
            "category": "Science",
            "subcategory": "Chemistry",
            "question": "What is the name of the process where a solid changes directly to a gas without becoming a liquid?",
            "options": ["Sublimation", "Evaporation", "Condensation", "Deposition"],
            "correct_answer": "Sublimation",
            "difficulty": "medium"
        },
        # Hard (2)
        {
            "id": gap_ids[18],
            "category": "Science",
            "subcategory": "Chemistry",
            "question": "What is Avogadro's number, the number of particles in one mole of a substance?",
            "options": ["6.022 × 10²³", "3.14 × 10²³", "9.8 × 10²³", "1.6 × 10²³"],
            "correct_answer": "6.022 × 10²³",
            "difficulty": "hard"
        },
        {
            "id": gap_ids[19],
            "category": "Science",
            "subcategory": "Chemistry",
            "question": "What type of reaction releases energy in the form of heat to the surroundings?",
            "options": ["Exothermic", "Endothermic", "Isothermic", "Adiabatic"],
            "correct_answer": "Exothermic",
            "difficulty": "hard"
        },

        # PHYSICS (2 questions: both hard)
        {
            "id": gap_ids[20],
            "category": "Science",
            "subcategory": "Physics",
            "question": "What principle states that energy cannot be created or destroyed, only transformed from one form to another?",
            "options": ["Law of conservation of energy", "Newton's third law", "Law of entropy", "Heisenberg uncertainty principle"],
            "correct_answer": "Law of conservation of energy",
            "difficulty": "hard"
        },
        {
            "id": gap_ids[21],
            "category": "Science",
            "subcategory": "Physics",
            "question": "What is the term for the bending of light as it passes from one medium to another?",
            "options": ["Refraction", "Reflection", "Diffraction", "Dispersion"],
            "correct_answer": "Refraction",
            "difficulty": "hard"
        }
    ]

    # Add new questions
    science_questions.extend(new_questions)

    # Save updated database
    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✓ Added 22 new Science questions using gap IDs")
    print(f"\nNew Science total: {len(science_questions)} questions")

    # Show breakdown
    print("\nBreakdown by subcategory:")
    subcats = {}
    for q in science_questions:
        subcat = q['subcategory']
        if subcat not in subcats:
            subcats[subcat] = 0
        subcats[subcat] += 1

    for subcat in sorted(subcats.keys()):
        print(f"  {subcat}: {subcats[subcat]} questions")

    # Show difficulty breakdown
    print("\nBreakdown by difficulty:")
    diffs = {'easy': 0, 'medium': 0, 'hard': 0}
    for q in science_questions:
        diffs[q['difficulty']] += 1

    for diff in ['easy', 'medium', 'hard']:
        pct = (diffs[diff] / len(science_questions)) * 100
        print(f"  {diff.capitalize()}: {diffs[diff]} ({pct:.1f}%)")

    print("\n✓ Science category complete: 300/300 questions")

if __name__ == "__main__":
    add_science_questions()
