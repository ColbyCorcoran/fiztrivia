import json

# Load the current database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# New Science questions (sci_176 to sci_209) - 34 total
new_science_questions = [
    # Astronomy (9 questions)
    {
        "id": "sci_176",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is the name of the largest moon of Saturn?",
        "options": ["Titan", "Europa", "Ganymede", "Callisto"],
        "correct_answer": "Titan",
        "difficulty": "medium"
    },
    {
        "id": "sci_177",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What type of galaxy is the Milky Way classified as?",
        "options": ["Spiral", "Elliptical", "Irregular", "Lenticular"],
        "correct_answer": "Spiral",
        "difficulty": "medium"
    },
    {
        "id": "sci_178",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is the Roche limit?",
        "options": ["The distance at which tidal forces destroy an object", "The maximum distance a comet can travel", "The temperature limit of a star", "The speed of light barrier"],
        "correct_answer": "The distance at which tidal forces destroy an object",
        "difficulty": "hard"
    },
    {
        "id": "sci_179",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "Which planet has the shortest day in our solar system?",
        "options": ["Jupiter", "Saturn", "Neptune", "Mars"],
        "correct_answer": "Jupiter",
        "difficulty": "hard"
    },
    {
        "id": "sci_180",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is a pulsar?",
        "options": ["A rapidly rotating neutron star", "A dying red giant", "A forming protostar", "A black hole's event horizon"],
        "correct_answer": "A rapidly rotating neutron star",
        "difficulty": "hard"
    },
    {
        "id": "sci_181",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "Which spacecraft was the first to visit Pluto?",
        "options": ["New Horizons", "Voyager 2", "Cassini", "Pioneer 10"],
        "correct_answer": "New Horizons",
        "difficulty": "medium"
    },
    {
        "id": "sci_182",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is the Great Red Spot on Jupiter?",
        "options": ["A giant storm", "A volcanic crater", "An impact scar", "A frozen ocean"],
        "correct_answer": "A giant storm",
        "difficulty": "medium"
    },
    {
        "id": "sci_183",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "What is the approximate temperature at the core of the Sun?",
        "options": ["15 million degrees Celsius", "5,500 degrees Celsius", "100,000 degrees Celsius", "1 million degrees Celsius"],
        "correct_answer": "15 million degrees Celsius",
        "difficulty": "hard"
    },
    {
        "id": "sci_184",
        "category": "Science",
        "subcategory": "Astronomy",
        "question": "Which moon in our solar system has active geysers?",
        "options": ["Enceladus", "Titan", "Io", "Triton"],
        "correct_answer": "Enceladus",
        "difficulty": "hard"
    },
    
    # Physics (9 questions)
    {
        "id": "sci_185",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the SI unit of electric charge?",
        "options": ["Coulomb", "Ampere", "Volt", "Ohm"],
        "correct_answer": "Coulomb",
        "difficulty": "medium"
    },
    {
        "id": "sci_186",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What phenomenon describes the bending of light as it passes from one medium to another?",
        "options": ["Refraction", "Reflection", "Diffraction", "Dispersion"],
        "correct_answer": "Refraction",
        "difficulty": "medium"
    },
    {
        "id": "sci_187",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the Heisenberg Uncertainty Principle?",
        "options": ["You cannot simultaneously know a particle's exact position and momentum", "Light behaves as both a wave and particle", "Energy cannot be created or destroyed", "Objects in motion stay in motion"],
        "correct_answer": "You cannot simultaneously know a particle's exact position and momentum",
        "difficulty": "hard"
    },
    {
        "id": "sci_188",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the term for the resistance of a fluid to flow?",
        "options": ["Viscosity", "Density", "Elasticity", "Plasticity"],
        "correct_answer": "Viscosity",
        "difficulty": "medium"
    },
    {
        "id": "sci_189",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What particles are exchanged in the strong nuclear force?",
        "options": ["Gluons", "Photons", "W and Z bosons", "Gravitons"],
        "correct_answer": "Gluons",
        "difficulty": "hard"
    },
    {
        "id": "sci_190",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the Doppler effect?",
        "options": ["The change in frequency of a wave relative to an observer", "The splitting of light into colors", "The interference of two waves", "The absorption of light by matter"],
        "correct_answer": "The change in frequency of a wave relative to an observer",
        "difficulty": "medium"
    },
    {
        "id": "sci_191",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is the name of the theoretical temperature at which all molecular motion stops?",
        "options": ["Absolute zero", "Freezing point", "Critical point", "Triple point"],
        "correct_answer": "Absolute zero",
        "difficulty": "medium"
    },
    {
        "id": "sci_192",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What is superfluidity?",
        "options": ["A phase of matter with zero viscosity", "A state of maximum density", "A form of plasma", "A type of superconductor"],
        "correct_answer": "A phase of matter with zero viscosity",
        "difficulty": "hard"
    },
    {
        "id": "sci_193",
        "category": "Science",
        "subcategory": "Physics",
        "question": "What does a Tesla measure?",
        "options": ["Magnetic field strength", "Electric current", "Voltage", "Resistance"],
        "correct_answer": "Magnetic field strength",
        "difficulty": "hard"
    },
    
    # Chemistry (8 questions)
    {
        "id": "sci_194",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is the most abundant element in Earth's crust?",
        "options": ["Oxygen", "Silicon", "Aluminum", "Iron"],
        "correct_answer": "Oxygen",
        "difficulty": "medium"
    },
    {
        "id": "sci_195",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What type of bond involves the sharing of electron pairs between atoms?",
        "options": ["Covalent", "Ionic", "Metallic", "Hydrogen"],
        "correct_answer": "Covalent",
        "difficulty": "medium"
    },
    {
        "id": "sci_196",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is Avogadro's number approximately equal to?",
        "options": ["6.022 × 10²³", "3.14 × 10⁸", "9.81 × 10²", "1.602 × 10⁻¹⁹"],
        "correct_answer": "6.022 × 10²³",
        "difficulty": "hard"
    },
    {
        "id": "sci_197",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is a catalyst?",
        "options": ["A substance that speeds up a reaction without being consumed", "A product of a chemical reaction", "A type of acid", "A radioactive element"],
        "correct_answer": "A substance that speeds up a reaction without being consumed",
        "difficulty": "medium"
    },
    {
        "id": "sci_198",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is the electron configuration of a noble gas called?",
        "options": ["Stable octet", "Valence shell", "Orbital maximum", "Ionic state"],
        "correct_answer": "Stable octet",
        "difficulty": "hard"
    },
    {
        "id": "sci_199",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is an allotrope?",
        "options": ["Different structural forms of the same element", "An isotope with extra neutrons", "A compound with two elements", "A radioactive decay product"],
        "correct_answer": "Different structural forms of the same element",
        "difficulty": "hard"
    },
    {
        "id": "sci_200",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is the pH of a neutral solution at 25°C?",
        "options": ["7", "0", "14", "1"],
        "correct_answer": "7",
        "difficulty": "easy"
    },
    {
        "id": "sci_201",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What process converts a solid directly to a gas without passing through a liquid state?",
        "options": ["Sublimation", "Evaporation", "Condensation", "Deposition"],
        "correct_answer": "Sublimation",
        "difficulty": "medium"
    },
    
    # Biology (8 questions)
    {
        "id": "sci_202",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the powerhouse organelle of the cell?",
        "options": ["Mitochondria", "Nucleus", "Ribosome", "Chloroplast"],
        "correct_answer": "Mitochondria",
        "difficulty": "easy"
    },
    {
        "id": "sci_203",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the process by which plants make their own food using sunlight?",
        "options": ["Photosynthesis", "Cellular respiration", "Fermentation", "Glycolysis"],
        "correct_answer": "Photosynthesis",
        "difficulty": "easy"
    },
    {
        "id": "sci_204",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the term for animals that are active at night?",
        "options": ["Nocturnal", "Diurnal", "Crepuscular", "Cathemeral"],
        "correct_answer": "Nocturnal",
        "difficulty": "medium"
    },
    {
        "id": "sci_205",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What are the three domains of life?",
        "options": ["Bacteria, Archaea, Eukarya", "Animals, Plants, Fungi", "Prokaryotes, Eukaryotes, Viruses", "Vertebrates, Invertebrates, Microbes"],
        "correct_answer": "Bacteria, Archaea, Eukarya",
        "difficulty": "hard"
    },
    {
        "id": "sci_206",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the name of the protein that carries oxygen in red blood cells?",
        "options": ["Hemoglobin", "Myoglobin", "Insulin", "Collagen"],
        "correct_answer": "Hemoglobin",
        "difficulty": "medium"
    },
    {
        "id": "sci_207",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the process of programmed cell death called?",
        "options": ["Apoptosis", "Necrosis", "Mitosis", "Meiosis"],
        "correct_answer": "Apoptosis",
        "difficulty": "hard"
    },
    {
        "id": "sci_208",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What type of organisms can produce their own food from inorganic substances?",
        "options": ["Autotrophs", "Heterotrophs", "Decomposers", "Parasites"],
        "correct_answer": "Autotrophs",
        "difficulty": "medium"
    },
    {
        "id": "sci_209",
        "category": "Science",
        "subcategory": "Biology",
        "question": "What is the genetic material of most organisms?",
        "options": ["DNA", "RNA", "Proteins", "Lipids"],
        "correct_answer": "DNA",
        "difficulty": "easy"
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
