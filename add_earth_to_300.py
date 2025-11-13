import json

# Load database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# 50 new Earth questions (ear_251 to ear_300)
# Distribution: Animals (18), Weather (8), Geography (8), Trees (8), Plants (8)
# Emphasis on hard/medium difficulty

new_questions = [
    # Animals (18 questions) - ear_251-268
    {
        "id": "ear_251",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "What is the only mammal capable of true flight?",
        "options": ["Flying squirrel", "Bat", "Sugar glider", "Flying lemur"],
        "correct_answer": "Bat",
        "difficulty": "medium"
    },
    {
        "id": "ear_252",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "Which animal has three hearts?",
        "options": ["Octopus", "Squid", "Whale", "Elephant"],
        "correct_answer": "Octopus",
        "difficulty": "hard"
    },
    {
        "id": "ear_253",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "What is the most venomous fish in the world?",
        "options": ["Stonefish", "Pufferfish", "Lionfish", "Stingray"],
        "correct_answer": "Stonefish",
        "difficulty": "hard"
    },
    {
        "id": "ear_254",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "How long is the gestation period for an African elephant?",
        "options": ["22 months", "18 months", "12 months", "15 months"],
        "correct_answer": "22 months",
        "difficulty": "hard"
    },
    {
        "id": "ear_255",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "Which bird can fly backwards?",
        "options": ["Hummingbird", "Woodpecker", "Swift", "Kingfisher"],
        "correct_answer": "Hummingbird",
        "difficulty": "medium"
    },
    {
        "id": "ear_256",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "What is the largest species of bear?",
        "options": ["Polar bear", "Grizzly bear", "Kodiak bear", "Black bear"],
        "correct_answer": "Polar bear",
        "difficulty": "medium"
    },
    {
        "id": "ear_257",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "Which animal has the highest blood pressure?",
        "options": ["Giraffe", "Elephant", "Whale", "Horse"],
        "correct_answer": "Giraffe",
        "difficulty": "hard"
    },
    {
        "id": "ear_258",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "How many chambers does a fish's heart have?",
        "options": ["2", "3", "4", "1"],
        "correct_answer": "2",
        "difficulty": "hard"
    },
    {
        "id": "ear_259",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "What is the fastest swimming fish?",
        "options": ["Sailfish", "Marlin", "Tuna", "Swordfish"],
        "correct_answer": "Sailfish",
        "difficulty": "hard"
    },
    {
        "id": "ear_260",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "Which animal has the longest migration route?",
        "options": ["Arctic tern", "Monarch butterfly", "Gray whale", "Caribou"],
        "correct_answer": "Arctic tern",
        "difficulty": "hard"
    },
    {
        "id": "ear_261",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "What is the only marsupial native to North America?",
        "options": ["Opossum", "Kangaroo rat", "Flying squirrel", "Raccoon"],
        "correct_answer": "Opossum",
        "difficulty": "hard"
    },
    {
        "id": "ear_262",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "How many eyes does a honeybee have?",
        "options": ["5", "2", "6", "8"],
        "correct_answer": "5",
        "difficulty": "hard"
    },
    {
        "id": "ear_263",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "Which primate is known for having the most complex social structure?",
        "options": ["Chimpanzee", "Gorilla", "Orangutan", "Baboon"],
        "correct_answer": "Chimpanzee",
        "difficulty": "medium"
    },
    {
        "id": "ear_264",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "What is the smallest mammal in the world by weight?",
        "options": ["Etruscan shrew", "Pygmy shrew", "Bumblebee bat", "Pygmy mouse"],
        "correct_answer": "Bumblebee bat",
        "difficulty": "hard"
    },
    {
        "id": "ear_265",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "Which animal has a tongue longer than its body?",
        "options": ["Chameleon", "Anteater", "Giraffe", "Frog"],
        "correct_answer": "Chameleon",
        "difficulty": "hard"
    },
    {
        "id": "ear_266",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "How many bones does a shark have?",
        "options": ["0", "50", "100", "200"],
        "correct_answer": "0",
        "difficulty": "medium"
    },
    {
        "id": "ear_267",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "What is the lifespan of a mayfly?",
        "options": ["24 hours", "1 week", "1 month", "3 days"],
        "correct_answer": "24 hours",
        "difficulty": "medium"
    },
    {
        "id": "ear_268",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "Which animal can survive the longest without water?",
        "options": ["Kangaroo rat", "Camel", "Desert tortoise", "Jerboa"],
        "correct_answer": "Kangaroo rat",
        "difficulty": "hard"
    },

    # Weather (8 questions) - ear_269-276
    {
        "id": "ear_269",
        "category": "Earth",
        "subcategory": "Weather",
        "question": "What is the name of the phenomenon when rain freezes before hitting the ground?",
        "options": ["Sleet", "Hail", "Freezing rain", "Graupel"],
        "correct_answer": "Sleet",
        "difficulty": "medium"
    },
    {
        "id": "ear_270",
        "category": "Earth",
        "subcategory": "Weather",
        "question": "What is the calm center of a hurricane called?",
        "options": ["Eye", "Core", "Center", "Vortex"],
        "correct_answer": "Eye",
        "difficulty": "easy"
    },
    {
        "id": "ear_271",
        "category": "Earth",
        "subcategory": "Weather",
        "question": "What scale measures tornado intensity?",
        "options": ["Enhanced Fujita scale", "Richter scale", "Saffir-Simpson scale", "Beaufort scale"],
        "correct_answer": "Enhanced Fujita scale",
        "difficulty": "hard"
    },
    {
        "id": "ear_272",
        "category": "Earth",
        "subcategory": "Weather",
        "question": "What is the driest place on Earth?",
        "options": ["Atacama Desert", "Death Valley", "Sahara Desert", "Antarctica"],
        "correct_answer": "Atacama Desert",
        "difficulty": "hard"
    },
    {
        "id": "ear_273",
        "category": "Earth",
        "subcategory": "Weather",
        "question": "What causes the Northern Lights (Aurora Borealis)?",
        "options": ["Solar wind interacting with Earth's magnetic field", "Ice crystals in the atmosphere", "Volcanic ash", "Moon's gravity"],
        "correct_answer": "Solar wind interacting with Earth's magnetic field",
        "difficulty": "hard"
    },
    {
        "id": "ear_274",
        "category": "Earth",
        "subcategory": "Weather",
        "question": "What is the most common gas in Earth's atmosphere?",
        "options": ["Nitrogen", "Oxygen", "Carbon dioxide", "Argon"],
        "correct_answer": "Nitrogen",
        "difficulty": "medium"
    },
    {
        "id": "ear_275",
        "category": "Earth",
        "subcategory": "Weather",
        "question": "What is a haboob?",
        "options": ["A dust storm", "A type of cloud", "A wind pattern", "A rain phenomenon"],
        "correct_answer": "A dust storm",
        "difficulty": "hard"
    },
    {
        "id": "ear_276",
        "category": "Earth",
        "subcategory": "Weather",
        "question": "At what temperature do Celsius and Fahrenheit scales meet?",
        "options": ["-40 degrees", "0 degrees", "-32 degrees", "32 degrees"],
        "correct_answer": "-40 degrees",
        "difficulty": "hard"
    },

    # Geography (8 questions) - ear_277-284
    {
        "id": "ear_277",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "What is the deepest point in the ocean?",
        "options": ["Mariana Trench", "Puerto Rico Trench", "Java Trench", "Philippine Trench"],
        "correct_answer": "Mariana Trench",
        "difficulty": "medium"
    },
    {
        "id": "ear_278",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "Which desert is the largest hot desert in the world?",
        "options": ["Sahara Desert", "Arabian Desert", "Gobi Desert", "Kalahari Desert"],
        "correct_answer": "Sahara Desert",
        "difficulty": "easy"
    },
    {
        "id": "ear_279",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "What is the longest mountain range on Earth?",
        "options": ["Andes", "Himalayas", "Rocky Mountains", "Alps"],
        "correct_answer": "Andes",
        "difficulty": "medium"
    },
    {
        "id": "ear_280",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "Which country has the most volcanoes?",
        "options": ["Indonesia", "Japan", "United States", "Philippines"],
        "correct_answer": "Indonesia",
        "difficulty": "hard"
    },
    {
        "id": "ear_281",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "What is the largest island in the Mediterranean Sea?",
        "options": ["Sicily", "Sardinia", "Cyprus", "Crete"],
        "correct_answer": "Sicily",
        "difficulty": "hard"
    },
    {
        "id": "ear_282",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "Which waterfall has the greatest single drop?",
        "options": ["Angel Falls", "Niagara Falls", "Victoria Falls", "Iguazu Falls"],
        "correct_answer": "Angel Falls",
        "difficulty": "hard"
    },
    {
        "id": "ear_283",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "What percentage of Earth's water is fresh water?",
        "options": ["2.5%", "10%", "5%", "15%"],
        "correct_answer": "2.5%",
        "difficulty": "hard"
    },
    {
        "id": "ear_284",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "Which continent has the most countries?",
        "options": ["Africa", "Asia", "Europe", "South America"],
        "correct_answer": "Africa",
        "difficulty": "medium"
    },

    # Trees (8 questions) - ear_285-292
    {
        "id": "ear_285",
        "category": "Earth",
        "subcategory": "Trees",
        "question": "What is the tallest tree species in the world?",
        "options": ["Coast redwood", "Giant sequoia", "Douglas fir", "Sitka spruce"],
        "correct_answer": "Coast redwood",
        "difficulty": "hard"
    },
    {
        "id": "ear_286",
        "category": "Earth",
        "subcategory": "Trees",
        "question": "Which tree produces the seed called a conker?",
        "options": ["Horse chestnut", "Oak", "Walnut", "Beech"],
        "correct_answer": "Horse chestnut",
        "difficulty": "hard"
    },
    {
        "id": "ear_287",
        "category": "Earth",
        "subcategory": "Trees",
        "question": "What is the national tree of Canada?",
        "options": ["Maple", "Oak", "Pine", "Birch"],
        "correct_answer": "Maple",
        "difficulty": "medium"
    },
    {
        "id": "ear_288",
        "category": "Earth",
        "subcategory": "Trees",
        "question": "Which tree's wood is traditionally used to make cricket bats?",
        "options": ["Willow", "Ash", "Oak", "Maple"],
        "correct_answer": "Willow",
        "difficulty": "hard"
    },
    {
        "id": "ear_289",
        "category": "Earth",
        "subcategory": "Trees",
        "question": "What is the process of a tree losing its leaves called?",
        "options": ["Abscission", "Photosynthesis", "Transpiration", "Germination"],
        "correct_answer": "Abscission",
        "difficulty": "hard"
    },
    {
        "id": "ear_290",
        "category": "Earth",
        "subcategory": "Trees",
        "question": "Which tree produces the hardest wood in the world?",
        "options": ["Lignum vitae", "Ebony", "Teak", "Mahogany"],
        "correct_answer": "Lignum vitae",
        "difficulty": "hard"
    },
    {
        "id": "ear_291",
        "category": "Earth",
        "subcategory": "Trees",
        "question": "What type of tree is a bonsai tree typically?",
        "options": ["Any tree species grown in miniature", "Only pine trees", "Only maple trees", "Only juniper trees"],
        "correct_answer": "Any tree species grown in miniature",
        "difficulty": "medium"
    },
    {
        "id": "ear_292",
        "category": "Earth",
        "subcategory": "Trees",
        "question": "Which tree is known as the 'Tree of Life' in Africa?",
        "options": ["Baobab", "Acacia", "Palm", "Fig"],
        "correct_answer": "Baobab",
        "difficulty": "medium"
    },

    # Plants (8 questions) - ear_293-300
    {
        "id": "ear_293",
        "category": "Earth",
        "subcategory": "Plants",
        "question": "What is the largest flower in the world?",
        "options": ["Rafflesia arnoldii", "Sunflower", "Titan arum", "Lotus"],
        "correct_answer": "Rafflesia arnoldii",
        "difficulty": "hard"
    },
    {
        "id": "ear_294",
        "category": "Earth",
        "subcategory": "Plants",
        "question": "Which plant is the fastest growing in the world?",
        "options": ["Bamboo", "Kudzu", "Hyacinth", "Eucalyptus"],
        "correct_answer": "Bamboo",
        "difficulty": "medium"
    },
    {
        "id": "ear_295",
        "category": "Earth",
        "subcategory": "Plants",
        "question": "What is the study of plants called?",
        "options": ["Botany", "Zoology", "Ecology", "Biology"],
        "correct_answer": "Botany",
        "difficulty": "easy"
    },
    {
        "id": "ear_296",
        "category": "Earth",
        "subcategory": "Plants",
        "question": "Which plant can eat insects?",
        "options": ["Venus flytrap", "Cactus", "Fern", "Moss"],
        "correct_answer": "Venus flytrap",
        "difficulty": "easy"
    },
    {
        "id": "ear_297",
        "category": "Earth",
        "subcategory": "Plants",
        "question": "What is the most expensive spice in the world by weight?",
        "options": ["Saffron", "Vanilla", "Cardamom", "Cinnamon"],
        "correct_answer": "Saffron",
        "difficulty": "hard"
    },
    {
        "id": "ear_298",
        "category": "Earth",
        "subcategory": "Plants",
        "question": "Which plant takes the longest to bloom?",
        "options": ["Puya raimondii", "Agave", "Bamboo", "Century plant"],
        "correct_answer": "Puya raimondii",
        "difficulty": "hard"
    },
    {
        "id": "ear_299",
        "category": "Earth",
        "subcategory": "Plants",
        "question": "What percentage of Earth's oxygen is produced by ocean plants?",
        "options": ["70%", "50%", "30%", "90%"],
        "correct_answer": "70%",
        "difficulty": "hard"
    },
    {
        "id": "ear_300",
        "category": "Earth",
        "subcategory": "Plants",
        "question": "Which plant is known for closing its leaves when touched?",
        "options": ["Mimosa pudica (sensitive plant)", "Venus flytrap", "Dandelion", "Clover"],
        "correct_answer": "Mimosa pudica (sensitive plant)",
        "difficulty": "hard"
    }
]

# Add new questions to Earth category
data['categories']['Earth'].extend(new_questions)

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ Added {len(new_questions)} Earth questions")
print(f"New range: ear_251 to ear_300")
print(f"\nDistribution:")
print(f"  Animals: 18 questions")
print(f"  Weather: 8 questions")
print(f"  Geography: 8 questions")
print(f"  Trees: 8 questions")
print(f"  Plants: 8 questions")
print(f"\nTotal Earth questions: {len(data['categories']['Earth'])}")
