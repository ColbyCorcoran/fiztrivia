import json

# Load database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# 50 new Food questions (foo_251 to foo_300)
# Distribution: Ingredients (10), Dishes (8), Famous Chefs/Restaurants (6),
# Cuisines (5), Beverages (5), Cooking Techniques (4), Baking (4),
# Desserts (4), Food History (2), Sauces & Condiments (2)
# Emphasis on hard/medium difficulty

new_questions = [
    # Ingredients (10 questions) - foo_251-260
    {
        "id": "foo_251",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "What is the world's most expensive spice by weight?",
        "options": ["Saffron", "Vanilla", "Cardamom", "Cinnamon"],
        "correct_answer": "Saffron",
        "difficulty": "medium"
    },
    {
        "id": "foo_252",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "Which type of rice is traditionally used in risotto?",
        "options": ["Arborio", "Basmati", "Jasmine", "Wild rice"],
        "correct_answer": "Arborio",
        "difficulty": "hard"
    },
    {
        "id": "foo_253",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "What is tahini made from?",
        "options": ["Sesame seeds", "Chickpeas", "Sunflower seeds", "Almonds"],
        "correct_answer": "Sesame seeds",
        "difficulty": "hard"
    },
    {
        "id": "foo_254",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "Which vegetable is also known as aubergine?",
        "options": ["Eggplant", "Zucchini", "Squash", "Cucumber"],
        "correct_answer": "Eggplant",
        "difficulty": "medium"
    },
    {
        "id": "foo_255",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "What type of fish are anchovies?",
        "options": ["Small saltwater fish", "Freshwater fish", "Shellfish", "Crustaceans"],
        "correct_answer": "Small saltwater fish",
        "difficulty": "medium"
    },
    {
        "id": "foo_256",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "Which grain is used to make polenta?",
        "options": ["Cornmeal", "Wheat", "Rice", "Barley"],
        "correct_answer": "Cornmeal",
        "difficulty": "hard"
    },
    {
        "id": "foo_257",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "What is the main ingredient in kimchi?",
        "options": ["Napa cabbage", "Radish", "Cucumber", "Bean sprouts"],
        "correct_answer": "Napa cabbage",
        "difficulty": "medium"
    },
    {
        "id": "foo_258",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "Which nut is technically a legume?",
        "options": ["Peanut", "Almond", "Cashew", "Walnut"],
        "correct_answer": "Peanut",
        "difficulty": "hard"
    },
    {
        "id": "foo_259",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "What is capers?",
        "options": ["Pickled flower buds", "A type of olive", "Pickled onions", "A spice"],
        "correct_answer": "Pickled flower buds",
        "difficulty": "hard"
    },
    {
        "id": "foo_260",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "Which fruit is dried to make prunes?",
        "options": ["Plums", "Apricots", "Dates", "Figs"],
        "correct_answer": "Plums",
        "difficulty": "medium"
    },

    # Dishes (8 questions) - foo_261-268
    {
        "id": "foo_261",
        "category": "Food",
        "subcategory": "Dishes",
        "question": "What is the main ingredient in the Middle Eastern dish falafel?",
        "options": ["Chickpeas", "Lentils", "Beans", "Rice"],
        "correct_answer": "Chickpeas",
        "difficulty": "medium"
    },
    {
        "id": "foo_262",
        "category": "Food",
        "subcategory": "Dishes",
        "question": "What type of pasta is shaped like small rice grains?",
        "options": ["Orzo", "Penne", "Fusilli", "Farfalle"],
        "correct_answer": "Orzo",
        "difficulty": "hard"
    },
    {
        "id": "foo_263",
        "category": "Food",
        "subcategory": "Dishes",
        "question": "What is the primary ingredient in the Japanese dish tempura?",
        "options": ["Battered and fried seafood or vegetables", "Raw fish", "Rice", "Noodles"],
        "correct_answer": "Battered and fried seafood or vegetables",
        "difficulty": "medium"
    },
    {
        "id": "foo_264",
        "category": "Food",
        "subcategory": "Dishes",
        "question": "Which Indian bread is traditionally baked in a tandoor oven?",
        "options": ["Naan", "Chapati", "Paratha", "Roti"],
        "correct_answer": "Naan",
        "difficulty": "medium"
    },
    {
        "id": "foo_265",
        "category": "Food",
        "subcategory": "Dishes",
        "question": "What is the main protein in the Spanish dish paella?",
        "options": ["Seafood and/or chicken", "Beef", "Pork", "Lamb"],
        "correct_answer": "Seafood and/or chicken",
        "difficulty": "medium"
    },
    {
        "id": "foo_266",
        "category": "Food",
        "subcategory": "Dishes",
        "question": "What type of cheese is traditionally used in Greek salad?",
        "options": ["Feta", "Mozzarella", "Cheddar", "Gouda"],
        "correct_answer": "Feta",
        "difficulty": "easy"
    },
    {
        "id": "foo_267",
        "category": "Food",
        "subcategory": "Dishes",
        "question": "Which Vietnamese soup is traditionally made with beef or chicken broth?",
        "options": ["Pho", "Ramen", "Udon", "Tom yum"],
        "correct_answer": "Pho",
        "difficulty": "medium"
    },
    {
        "id": "foo_268",
        "category": "Food",
        "subcategory": "Dishes",
        "question": "What is the main ingredient in the Scottish dish haggis?",
        "options": ["Sheep's offal", "Beef", "Chicken", "Fish"],
        "correct_answer": "Sheep's offal",
        "difficulty": "hard"
    },

    # Famous Chefs/Restaurants (6 questions) - foo_269-274
    {
        "id": "foo_269",
        "category": "Food",
        "subcategory": "Famous Chefs/Restaurants",
        "question": "Which chef is known for the quote 'Bam!'?",
        "options": ["Emeril Lagasse", "Gordon Ramsay", "Bobby Flay", "Wolfgang Puck"],
        "correct_answer": "Emeril Lagasse",
        "difficulty": "medium"
    },
    {
        "id": "foo_270",
        "category": "Food",
        "subcategory": "Famous Chefs/Restaurants",
        "question": "Who is the host of 'Hell's Kitchen'?",
        "options": ["Gordon Ramsay", "Jamie Oliver", "Anthony Bourdain", "Alton Brown"],
        "correct_answer": "Gordon Ramsay",
        "difficulty": "easy"
    },
    {
        "id": "foo_271",
        "category": "Food",
        "subcategory": "Famous Chefs/Restaurants",
        "question": "Which chef is known for molecular gastronomy and the restaurant elBulli?",
        "options": ["Ferran Adrià", "Heston Blumenthal", "Grant Achatz", "Thomas Keller"],
        "correct_answer": "Ferran Adrià",
        "difficulty": "hard"
    },
    {
        "id": "foo_272",
        "category": "Food",
        "subcategory": "Famous Chefs/Restaurants",
        "question": "Which city is home to the most Michelin-starred restaurants?",
        "options": ["Tokyo", "Paris", "New York", "London"],
        "correct_answer": "Tokyo",
        "difficulty": "hard"
    },
    {
        "id": "foo_273",
        "category": "Food",
        "subcategory": "Famous Chefs/Restaurants",
        "question": "Who wrote the bestselling kitchen memoir 'Kitchen Confidential'?",
        "options": ["Anthony Bourdain", "Gordon Ramsay", "Marco Pierre White", "Eric Ripert"],
        "correct_answer": "Anthony Bourdain",
        "difficulty": "medium"
    },
    {
        "id": "foo_274",
        "category": "Food",
        "subcategory": "Famous Chefs/Restaurants",
        "question": "Which chef owns the Fat Duck restaurant in England?",
        "options": ["Heston Blumenthal", "Gordon Ramsay", "Jamie Oliver", "Marco Pierre White"],
        "correct_answer": "Heston Blumenthal",
        "difficulty": "hard"
    },

    # Cuisines (5 questions) - foo_275-279
    {
        "id": "foo_275",
        "category": "Food",
        "subcategory": "Cuisines",
        "question": "What is the staple grain in Ethiopian cuisine?",
        "options": ["Teff", "Rice", "Wheat", "Corn"],
        "correct_answer": "Teff",
        "difficulty": "hard"
    },
    {
        "id": "foo_276",
        "category": "Food",
        "subcategory": "Cuisines",
        "question": "Which cuisine is known for using the 'five-spice' powder?",
        "options": ["Chinese", "Indian", "Thai", "Korean"],
        "correct_answer": "Chinese",
        "difficulty": "medium"
    },
    {
        "id": "foo_277",
        "category": "Food",
        "subcategory": "Cuisines",
        "question": "What is the traditional cooking pot used in Moroccan cuisine?",
        "options": ["Tagine", "Wok", "Paella pan", "Dutch oven"],
        "correct_answer": "Tagine",
        "difficulty": "hard"
    },
    {
        "id": "foo_278",
        "category": "Food",
        "subcategory": "Cuisines",
        "question": "Which country's cuisine features the dish bibimbap?",
        "options": ["Korea", "Japan", "China", "Vietnam"],
        "correct_answer": "Korea",
        "difficulty": "medium"
    },
    {
        "id": "foo_279",
        "category": "Food",
        "subcategory": "Cuisines",
        "question": "What is the main herb used in pesto sauce?",
        "options": ["Basil", "Parsley", "Cilantro", "Oregano"],
        "correct_answer": "Basil",
        "difficulty": "easy"
    },

    # Beverages (5 questions) - foo_280-284
    {
        "id": "foo_280",
        "category": "Food",
        "subcategory": "Beverages",
        "question": "What type of tea is fermented and aged?",
        "options": ["Pu-erh", "Green tea", "Black tea", "White tea"],
        "correct_answer": "Pu-erh",
        "difficulty": "hard"
    },
    {
        "id": "foo_281",
        "category": "Food",
        "subcategory": "Beverages",
        "question": "What is the primary ingredient in kombucha?",
        "options": ["Tea", "Coffee", "Fruit juice", "Milk"],
        "correct_answer": "Tea",
        "difficulty": "medium"
    },
    {
        "id": "foo_282",
        "category": "Food",
        "subcategory": "Beverages",
        "question": "Which country is the world's largest producer of coffee?",
        "options": ["Brazil", "Colombia", "Ethiopia", "Vietnam"],
        "correct_answer": "Brazil",
        "difficulty": "medium"
    },
    {
        "id": "foo_283",
        "category": "Food",
        "subcategory": "Beverages",
        "question": "What is the main difference between ale and lager beer?",
        "options": ["Fermentation temperature", "Grain type", "Hops variety", "Alcohol content"],
        "correct_answer": "Fermentation temperature",
        "difficulty": "hard"
    },
    {
        "id": "foo_284",
        "category": "Food",
        "subcategory": "Beverages",
        "question": "What plant is tequila made from?",
        "options": ["Agave", "Cactus", "Corn", "Sugar cane"],
        "correct_answer": "Agave",
        "difficulty": "medium"
    },

    # Cooking Techniques (4 questions) - foo_285-288
    {
        "id": "foo_285",
        "category": "Food",
        "subcategory": "Cooking Techniques",
        "question": "What cooking technique involves cooking food in a small amount of fat over high heat?",
        "options": ["Sautéing", "Braising", "Poaching", "Steaming"],
        "correct_answer": "Sautéing",
        "difficulty": "medium"
    },
    {
        "id": "foo_286",
        "category": "Food",
        "subcategory": "Cooking Techniques",
        "question": "What is the term for cooking food slowly in liquid at low temperature?",
        "options": ["Braising", "Grilling", "Roasting", "Frying"],
        "correct_answer": "Braising",
        "difficulty": "medium"
    },
    {
        "id": "foo_287",
        "category": "Food",
        "subcategory": "Cooking Techniques",
        "question": "What is the French term for 'cooked under pressure'?",
        "options": ["Sous vide", "En papillote", "Au gratin", "Flambé"],
        "correct_answer": "Sous vide",
        "difficulty": "hard"
    },
    {
        "id": "foo_288",
        "category": "Food",
        "subcategory": "Cooking Techniques",
        "question": "What does it mean to 'blanch' a vegetable?",
        "options": ["Briefly boil then plunge in ice water", "Grill until charred", "Roast at high heat", "Steam until soft"],
        "correct_answer": "Briefly boil then plunge in ice water",
        "difficulty": "hard"
    },

    # Baking (4 questions) - foo_289-292
    {
        "id": "foo_289",
        "category": "Food",
        "subcategory": "Baking",
        "question": "What ingredient makes baked goods rise?",
        "options": ["Baking powder or yeast", "Sugar", "Butter", "Eggs"],
        "correct_answer": "Baking powder or yeast",
        "difficulty": "easy"
    },
    {
        "id": "foo_290",
        "category": "Food",
        "subcategory": "Baking",
        "question": "What is the protein in flour that gives bread its structure?",
        "options": ["Gluten", "Starch", "Fiber", "Albumin"],
        "correct_answer": "Gluten",
        "difficulty": "hard"
    },
    {
        "id": "foo_291",
        "category": "Food",
        "subcategory": "Baking",
        "question": "What is a 'roux' used for in baking and cooking?",
        "options": ["Thickening sauces", "Leavening cakes", "Sweetening desserts", "Coloring pastries"],
        "correct_answer": "Thickening sauces",
        "difficulty": "hard"
    },
    {
        "id": "foo_292",
        "category": "Food",
        "subcategory": "Baking",
        "question": "What temperature should egg whites be at for optimal meringue?",
        "options": ["Room temperature", "Cold", "Warm", "Hot"],
        "correct_answer": "Room temperature",
        "difficulty": "hard"
    },

    # Desserts (4 questions) - foo_293-296
    {
        "id": "foo_293",
        "category": "Food",
        "subcategory": "Desserts",
        "question": "What is the main flavoring in tiramisu?",
        "options": ["Coffee", "Chocolate", "Vanilla", "Almond"],
        "correct_answer": "Coffee",
        "difficulty": "medium"
    },
    {
        "id": "foo_294",
        "category": "Food",
        "subcategory": "Desserts",
        "question": "Which French dessert is made of choux pastry filled with cream?",
        "options": ["Éclair", "Macaron", "Crêpe", "Tarte"],
        "correct_answer": "Éclair",
        "difficulty": "medium"
    },
    {
        "id": "foo_295",
        "category": "Food",
        "subcategory": "Desserts",
        "question": "What is the primary ingredient in traditional Turkish delight?",
        "options": ["Sugar and starch", "Honey and nuts", "Chocolate", "Fruit puree"],
        "correct_answer": "Sugar and starch",
        "difficulty": "hard"
    },
    {
        "id": "foo_296",
        "category": "Food",
        "subcategory": "Desserts",
        "question": "What type of pastry is used to make baklava?",
        "options": ["Phyllo", "Puff pastry", "Choux", "Shortcrust"],
        "correct_answer": "Phyllo",
        "difficulty": "hard"
    },

    # Food History (2 questions) - foo_297-298
    {
        "id": "foo_297",
        "category": "Food",
        "subcategory": "Food History",
        "question": "Which ancient civilization is credited with inventing pizza?",
        "options": ["Ancient Rome", "Ancient Greece", "Ancient Egypt", "Ancient Persia"],
        "correct_answer": "Ancient Rome",
        "difficulty": "hard"
    },
    {
        "id": "foo_298",
        "category": "Food",
        "subcategory": "Food History",
        "question": "What vegetable was originally purple before selective breeding?",
        "options": ["Carrot", "Potato", "Onion", "Corn"],
        "correct_answer": "Carrot",
        "difficulty": "hard"
    },

    # Sauces & Condiments (2 questions) - foo_299-300
    {
        "id": "foo_299",
        "category": "Food",
        "subcategory": "Sauces & Condiments",
        "question": "What are the five 'mother sauces' in French cuisine?",
        "options": ["Béchamel, Velouté, Espagnole, Hollandaise, Tomato", "Marinara, Alfredo, Pesto, Carbonara, Bolognese", "Soy, Teriyaki, Hoisin, Oyster, Fish sauce", "Ketchup, Mustard, Mayo, BBQ, Ranch"],
        "correct_answer": "Béchamel, Velouté, Espagnole, Hollandaise, Tomato",
        "difficulty": "hard"
    },
    {
        "id": "foo_300",
        "category": "Food",
        "subcategory": "Sauces & Condiments",
        "question": "What ingredient gives Worcestershire sauce its distinctive flavor?",
        "options": ["Anchovies", "Soy sauce", "Vinegar", "Molasses"],
        "correct_answer": "Anchovies",
        "difficulty": "hard"
    }
]

# Add new questions to Food category
data['categories']['Food'].extend(new_questions)

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ Added {len(new_questions)} Food questions")
print(f"New range: foo_251 to foo_300")
print(f"\nDistribution:")
print(f"  Ingredients: 10 questions")
print(f"  Dishes: 8 questions")
print(f"  Famous Chefs/Restaurants: 6 questions")
print(f"  Cuisines: 5 questions")
print(f"  Beverages: 5 questions")
print(f"  Cooking Techniques: 4 questions")
print(f"  Baking: 4 questions")
print(f"  Desserts: 4 questions")
print(f"  Food History: 2 questions")
print(f"  Sauces & Condiments: 2 questions")
print(f"\nTotal Food questions: {len(data['categories']['Food'])}")
