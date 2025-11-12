import json

# Load the current database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# New Earth questions (ear_207 to ear_252) - 46 total
# Distribution: Animals (15), Geography (12), Weather (8), Plants (6), Trees (5)
new_earth_questions = [
    # Animals (15 questions)
    {
        "id": "ear_207",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "What is the largest species of bear?",
        "options": ["Polar bear", "Grizzly bear", "Kodiak bear", "Black bear"],
        "correct_answer": "Polar bear",
        "difficulty": "medium"
    },
    {
        "id": "ear_208",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "What is the only mammal capable of true flight?",
        "options": ["Bat", "Flying squirrel", "Sugar glider", "Flying lemur"],
        "correct_answer": "Bat",
        "difficulty": "medium"
    },
    {
        "id": "ear_209",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "What is a group of crows called?",
        "options": ["A murder", "A flock", "A gaggle", "A pack"],
        "correct_answer": "A murder",
        "difficulty": "hard"
    },
    {
        "id": "ear_210",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "Which animal has the longest gestation period?",
        "options": ["African elephant", "Blue whale", "Giraffe", "Rhinoceros"],
        "correct_answer": "African elephant",
        "difficulty": "hard"
    },
    {
        "id": "ear_211",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "What is the fastest swimming fish?",
        "options": ["Sailfish", "Marlin", "Tuna", "Swordfish"],
        "correct_answer": "Sailfish",
        "difficulty": "hard"
    },
    {
        "id": "ear_212",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "How many legs does a spider have?",
        "options": ["8", "6", "10", "12"],
        "correct_answer": "8",
        "difficulty": "easy"
    },
    {
        "id": "ear_213",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "What is the largest living reptile?",
        "options": ["Saltwater crocodile", "Komodo dragon", "Anaconda", "Leatherback sea turtle"],
        "correct_answer": "Saltwater crocodile",
        "difficulty": "medium"
    },
    {
        "id": "ear_214",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "Which bird is known for its elaborate tail display?",
        "options": ["Peacock", "Pheasant", "Turkey", "Ostrich"],
        "correct_answer": "Peacock",
        "difficulty": "easy"
    },
    {
        "id": "ear_215",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "What is the only continent without native reptiles?",
        "options": ["Antarctica", "Europe", "Australia", "North America"],
        "correct_answer": "Antarctica",
        "difficulty": "hard"
    },
    {
        "id": "ear_216",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "What is the world's most venomous land snake?",
        "options": ["Inland taipan", "King cobra", "Black mamba", "Death adder"],
        "correct_answer": "Inland taipan",
        "difficulty": "hard"
    },
    {
        "id": "ear_217",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "What is a baby kangaroo called?",
        "options": ["Joey", "Cub", "Pup", "Kit"],
        "correct_answer": "Joey",
        "difficulty": "medium"
    },
    {
        "id": "ear_218",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "Which animal can sleep standing up?",
        "options": ["Horse", "Cow", "Giraffe", "All of the above"],
        "correct_answer": "All of the above",
        "difficulty": "medium"
    },
    {
        "id": "ear_219",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "What is the largest living bird by wingspan?",
        "options": ["Wandering albatross", "Andean condor", "California condor", "Golden eagle"],
        "correct_answer": "Wandering albatross",
        "difficulty": "hard"
    },
    {
        "id": "ear_220",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "What color is a polar bear's skin?",
        "options": ["Black", "White", "Pink", "Gray"],
        "correct_answer": "Black",
        "difficulty": "hard"
    },
    {
        "id": "ear_221",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "Which mammal has the most powerful bite?",
        "options": ["Hippopotamus", "Lion", "Tiger", "Grizzly bear"],
        "correct_answer": "Hippopotamus",
        "difficulty": "hard"
    },
    
    # Geography (12 questions)
    {
        "id": "ear_222",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "What is the longest river in the world?",
        "options": ["Nile", "Amazon", "Yangtze", "Mississippi"],
        "correct_answer": "Nile",
        "difficulty": "medium"
    },
    {
        "id": "ear_223",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "Which continent is the Sahara Desert located on?",
        "options": ["Africa", "Asia", "Australia", "South America"],
        "correct_answer": "Africa",
        "difficulty": "easy"
    },
    {
        "id": "ear_224",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "What is the capital of Canada?",
        "options": ["Ottawa", "Toronto", "Montreal", "Vancouver"],
        "correct_answer": "Ottawa",
        "difficulty": "medium"
    },
    {
        "id": "ear_225",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "Which ocean is the largest?",
        "options": ["Pacific", "Atlantic", "Indian", "Arctic"],
        "correct_answer": "Pacific",
        "difficulty": "easy"
    },
    {
        "id": "ear_226",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "What is the deepest point in the ocean?",
        "options": ["Mariana Trench", "Puerto Rico Trench", "Java Trench", "Tonga Trench"],
        "correct_answer": "Mariana Trench",
        "difficulty": "medium"
    },
    {
        "id": "ear_227",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "Which country has the most islands?",
        "options": ["Sweden", "Indonesia", "Norway", "Finland"],
        "correct_answer": "Sweden",
        "difficulty": "hard"
    },
    {
        "id": "ear_228",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "What is the capital of Brazil?",
        "options": ["Brasília", "Rio de Janeiro", "São Paulo", "Salvador"],
        "correct_answer": "Brasília",
        "difficulty": "medium"
    },
    {
        "id": "ear_229",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "Which desert is the largest hot desert in the world?",
        "options": ["Sahara", "Arabian", "Gobi", "Kalahari"],
        "correct_answer": "Sahara",
        "difficulty": "medium"
    },
    {
        "id": "ear_230",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "What is the smallest ocean?",
        "options": ["Arctic", "Indian", "Southern", "Atlantic"],
        "correct_answer": "Arctic",
        "difficulty": "medium"
    },
    {
        "id": "ear_231",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "Which African country was formerly known as Abyssinia?",
        "options": ["Ethiopia", "Eritrea", "Sudan", "Somalia"],
        "correct_answer": "Ethiopia",
        "difficulty": "hard"
    },
    {
        "id": "ear_232",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "What is the world's largest island?",
        "options": ["Greenland", "New Guinea", "Borneo", "Madagascar"],
        "correct_answer": "Greenland",
        "difficulty": "medium"
    },
    {
        "id": "ear_233",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "Which sea is the saltiest natural body of water?",
        "options": ["Dead Sea", "Red Sea", "Mediterranean Sea", "Caspian Sea"],
        "correct_answer": "Dead Sea",
        "difficulty": "medium"
    },
    
    # Weather (8 questions)
    {
        "id": "ear_234",
        "category": "Earth",
        "subcategory": "Weather",
        "question": "What causes thunder?",
        "options": ["Rapid expansion of heated air", "Clouds colliding", "Lightning striking ground", "Rain hitting surfaces"],
        "correct_answer": "Rapid expansion of heated air",
        "difficulty": "hard"
    },
    {
        "id": "ear_235",
        "category": "Earth",
        "subcategory": "Weather",
        "question": "What is the study of weather called?",
        "options": ["Meteorology", "Climatology", "Geology", "Astronomy"],
        "correct_answer": "Meteorology",
        "difficulty": "medium"
    },
    {
        "id": "ear_236",
        "category": "Earth",
        "subcategory": "Weather",
        "question": "What is frozen rain called?",
        "options": ["Hail", "Sleet", "Snow", "Graupel"],
        "correct_answer": "Hail",
        "difficulty": "medium"
    },
    {
        "id": "ear_237",
        "category": "Earth",
        "subcategory": "Weather",
        "question": "What type of cloud produces thunderstorms?",
        "options": ["Cumulonimbus", "Cumulus", "Stratus", "Cirrus"],
        "correct_answer": "Cumulonimbus",
        "difficulty": "hard"
    },
    {
        "id": "ear_238",
        "category": "Earth",
        "subcategory": "Weather",
        "question": "What is the calm center of a hurricane called?",
        "options": ["Eye", "Core", "Center", "Vortex"],
        "correct_answer": "Eye",
        "difficulty": "medium"
    },
    {
        "id": "ear_239",
        "category": "Earth",
        "subcategory": "Weather",
        "question": "What instrument measures air pressure?",
        "options": ["Barometer", "Thermometer", "Hygrometer", "Anemometer"],
        "correct_answer": "Barometer",
        "difficulty": "hard"
    },
    {
        "id": "ear_240",
        "category": "Earth",
        "subcategory": "Weather",
        "question": "What is a rapidly rotating column of air that touches the ground called?",
        "options": ["Tornado", "Hurricane", "Cyclone", "Typhoon"],
        "correct_answer": "Tornado",
        "difficulty": "easy"
    },
    {
        "id": "ear_241",
        "category": "Earth",
        "subcategory": "Weather",
        "question": "What scale measures tornado intensity?",
        "options": ["Enhanced Fujita Scale", "Richter Scale", "Saffir-Simpson Scale", "Beaufort Scale"],
        "correct_answer": "Enhanced Fujita Scale",
        "difficulty": "hard"
    },
    
    # Plants (6 questions)
    {
        "id": "ear_242",
        "category": "Earth",
        "subcategory": "Plants",
        "question": "What process do plants use to make food from sunlight?",
        "options": ["Photosynthesis", "Respiration", "Transpiration", "Germination"],
        "correct_answer": "Photosynthesis",
        "difficulty": "easy"
    },
    {
        "id": "ear_243",
        "category": "Earth",
        "subcategory": "Plants",
        "question": "What is the largest flower in the world?",
        "options": ["Rafflesia arnoldii", "Titan arum", "Sunflower", "Victoria amazonica"],
        "correct_answer": "Rafflesia arnoldii",
        "difficulty": "hard"
    },
    {
        "id": "ear_244",
        "category": "Earth",
        "subcategory": "Plants",
        "question": "What part of the plant conducts photosynthesis?",
        "options": ["Leaves", "Roots", "Stems", "Flowers"],
        "correct_answer": "Leaves",
        "difficulty": "easy"
    },
    {
        "id": "ear_245",
        "category": "Earth",
        "subcategory": "Plants",
        "question": "What is the study of plants called?",
        "options": ["Botany", "Zoology", "Ecology", "Biology"],
        "correct_answer": "Botany",
        "difficulty": "medium"
    },
    {
        "id": "ear_246",
        "category": "Earth",
        "subcategory": "Plants",
        "question": "Which plant is known for tracking the sun's movement?",
        "options": ["Sunflower", "Daisy", "Tulip", "Rose"],
        "correct_answer": "Sunflower",
        "difficulty": "medium"
    },
    {
        "id": "ear_247",
        "category": "Earth",
        "subcategory": "Plants",
        "question": "What is the fastest-growing plant?",
        "options": ["Bamboo", "Kudzu", "Water hyacinth", "Algae"],
        "correct_answer": "Bamboo",
        "difficulty": "hard"
    },
    
    # Trees (5 questions)
    {
        "id": "ear_248",
        "category": "Earth",
        "subcategory": "Trees",
        "question": "What is the tallest species of tree?",
        "options": ["Coast redwood", "Giant sequoia", "Douglas fir", "Eucalyptus"],
        "correct_answer": "Coast redwood",
        "difficulty": "hard"
    },
    {
        "id": "ear_249",
        "category": "Earth",
        "subcategory": "Trees",
        "question": "What tree produces acorns?",
        "options": ["Oak", "Maple", "Pine", "Birch"],
        "correct_answer": "Oak",
        "difficulty": "medium"
    },
    {
        "id": "ear_250",
        "category": "Earth",
        "subcategory": "Trees",
        "question": "What is the national tree of Canada?",
        "options": ["Maple", "Oak", "Pine", "Spruce"],
        "correct_answer": "Maple",
        "difficulty": "medium"
    },
    {
        "id": "ear_251",
        "category": "Earth",
        "subcategory": "Trees",
        "question": "Which tree is known for its white bark?",
        "options": ["Birch", "Aspen", "Poplar", "Willow"],
        "correct_answer": "Birch",
        "difficulty": "medium"
    },
    {
        "id": "ear_252",
        "category": "Earth",
        "subcategory": "Trees",
        "question": "What type of tree loses its leaves in autumn?",
        "options": ["Deciduous", "Evergreen", "Coniferous", "Tropical"],
        "correct_answer": "Deciduous",
        "difficulty": "medium"
    }
]

# Add the new questions to Earth category
data['categories']['Earth'].extend(new_earth_questions)

# Sort Earth questions by ID
data['categories']['Earth'].sort(key=lambda x: x['id'])

# Save the updated database
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Added {len(new_earth_questions)} new Earth questions")
print(f"New Earth total: {len(data['categories']['Earth'])} questions")

# Show breakdown by subcategory
from collections import Counter
subcats = Counter(q['subcategory'] for q in data['categories']['Earth'])
print("\nEarth subcategory distribution:")
for subcat, count in sorted(subcats.items(), key=lambda x: x[1], reverse=True):
    print(f"  {subcat}: {count}")

# Show difficulty distribution of new questions
difficulties = Counter(q['difficulty'] for q in new_earth_questions)
print(f"\nDifficulty distribution of new questions:")
for diff, count in sorted(difficulties.items()):
    print(f"  {diff}: {count}")
