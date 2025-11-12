import json

# Load the current database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# New Food questions (foo_207 to foo_256) - 50 total
new_food_questions = [
    # Ingredients (8 questions)
    {
        "id": "foo_207",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "What spice is derived from the crocus flower?",
        "options": ["Saffron", "Turmeric", "Paprika", "Cumin"],
        "correct_answer": "Saffron",
        "difficulty": "hard"
    },
    {
        "id": "foo_208",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "What grain is used to make traditional Japanese sake?",
        "options": ["Rice", "Wheat", "Barley", "Corn"],
        "correct_answer": "Rice",
        "difficulty": "medium"
    },
    {
        "id": "foo_209",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "What is the main ingredient in hummus?",
        "options": ["Chickpeas", "Lentils", "White beans", "Black beans"],
        "correct_answer": "Chickpeas",
        "difficulty": "medium"
    },
    {
        "id": "foo_210",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "What type of pasta is shaped like little ears?",
        "options": ["Orecchiette", "Farfalle", "Penne", "Rigatoni"],
        "correct_answer": "Orecchiette",
        "difficulty": "hard"
    },
    {
        "id": "foo_211",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "What nut is used to make traditional pesto?",
        "options": ["Pine nut", "Walnut", "Almond", "Cashew"],
        "correct_answer": "Pine nut",
        "difficulty": "hard"
    },
    {
        "id": "foo_212",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "What is ghee?",
        "options": ["Clarified butter", "Vegetable oil", "Margarine", "Lard"],
        "correct_answer": "Clarified butter",
        "difficulty": "medium"
    },
    {
        "id": "foo_213",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "What gives wasabi its green color?",
        "options": ["Horseradish and food coloring", "Green tea", "Seaweed", "Matcha"],
        "correct_answer": "Horseradish and food coloring",
        "difficulty": "hard"
    },
    {
        "id": "foo_214",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "What is quinoa classified as?",
        "options": ["Pseudocereal", "Grain", "Legume", "Vegetable"],
        "correct_answer": "Pseudocereal",
        "difficulty": "hard"
    },
    
    # Dishes (8 questions)
    {
        "id": "foo_215",
        "category": "Food",
        "subcategory": "Dishes",
        "question": "What is the national dish of Spain?",
        "options": ["Paella", "Tapas", "Gazpacho", "Tortilla"],
        "correct_answer": "Paella",
        "difficulty": "medium"
    },
    {
        "id": "foo_216",
        "category": "Food",
        "subcategory": "Dishes",
        "question": "What type of food is Pad Thai?",
        "options": ["Noodle dish", "Curry", "Soup", "Rice dish"],
        "correct_answer": "Noodle dish",
        "difficulty": "easy"
    },
    {
        "id": "foo_217",
        "category": "Food",
        "subcategory": "Dishes",
        "question": "What is the main ingredient in ratatouille?",
        "options": ["Vegetables", "Meat", "Fish", "Pasta"],
        "correct_answer": "Vegetables",
        "difficulty": "medium"
    },
    {
        "id": "foo_218",
        "category": "Food",
        "subcategory": "Dishes",
        "question": "What country does sushi originate from?",
        "options": ["Japan", "China", "Korea", "Thailand"],
        "correct_answer": "Japan",
        "difficulty": "easy"
    },
    {
        "id": "foo_219",
        "category": "Food",
        "subcategory": "Dishes",
        "question": "What is bouillabaisse?",
        "options": ["Fish stew", "Beef stew", "Vegetable soup", "Pasta sauce"],
        "correct_answer": "Fish stew",
        "difficulty": "hard"
    },
    {
        "id": "foo_220",
        "category": "Food",
        "subcategory": "Dishes",
        "question": "What is traditionally served with fish and chips in the UK?",
        "options": ["Mushy peas", "Coleslaw", "Baked beans", "Corn"],
        "correct_answer": "Mushy peas",
        "difficulty": "medium"
    },
    {
        "id": "foo_221",
        "category": "Food",
        "subcategory": "Dishes",
        "question": "What is goulash?",
        "options": ["Hungarian stew", "German sausage", "Polish dumpling", "Austrian pastry"],
        "correct_answer": "Hungarian stew",
        "difficulty": "medium"
    },
    {
        "id": "foo_222",
        "category": "Food",
        "subcategory": "Dishes",
        "question": "What is the main protein in a traditional carbonara?",
        "options": ["Pork (guanciale or pancetta)", "Chicken", "Beef", "Shrimp"],
        "correct_answer": "Pork (guanciale or pancetta)",
        "difficulty": "hard"
    },
    
    # Famous Chefs/Restaurants (6 questions)
    {
        "id": "foo_223",
        "category": "Food",
        "subcategory": "Famous Chefs/Restaurants",
        "question": "Which chef is known for the catchphrase 'Bam!'?",
        "options": ["Emeril Lagasse", "Bobby Flay", "Gordon Ramsay", "Jamie Oliver"],
        "correct_answer": "Emeril Lagasse",
        "difficulty": "medium"
    },
    {
        "id": "foo_224",
        "category": "Food",
        "subcategory": "Famous Chefs/Restaurants",
        "question": "Who is the host of 'Kitchen Nightmares'?",
        "options": ["Gordon Ramsay", "Anthony Bourdain", "Jamie Oliver", "Marco Pierre White"],
        "correct_answer": "Gordon Ramsay",
        "difficulty": "easy"
    },
    {
        "id": "foo_225",
        "category": "Food",
        "subcategory": "Famous Chefs/Restaurants",
        "question": "Which chef is known for '30 Minute Meals'?",
        "options": ["Rachael Ray", "Giada De Laurentiis", "Ina Garten", "Paula Deen"],
        "correct_answer": "Rachael Ray",
        "difficulty": "medium"
    },
    {
        "id": "foo_226",
        "category": "Food",
        "subcategory": "Famous Chefs/Restaurants",
        "question": "What is the name of Guy Fieri's show where he visits diners?",
        "options": ["Diners, Drive-Ins and Dives", "Road Food", "Food Paradise", "Man v. Food"],
        "correct_answer": "Diners, Drive-Ins and Dives",
        "difficulty": "medium"
    },
    {
        "id": "foo_227",
        "category": "Food",
        "subcategory": "Famous Chefs/Restaurants",
        "question": "Which French chef is credited with creating haute cuisine?",
        "options": ["Auguste Escoffier", "Paul Bocuse", "Alain Ducasse", "Julia Child"],
        "correct_answer": "Auguste Escoffier",
        "difficulty": "hard"
    },
    {
        "id": "foo_228",
        "category": "Food",
        "subcategory": "Famous Chefs/Restaurants",
        "question": "What is the most expensive restaurant in the world known for?",
        "options": ["Sublimotion in Ibiza", "Noma in Copenhagen", "Eleven Madison Park in NYC", "Osteria Francescana in Italy"],
        "correct_answer": "Sublimotion in Ibiza",
        "difficulty": "hard"
    },
    
    # Cuisines (6 questions)
    {
        "id": "foo_229",
        "category": "Food",
        "subcategory": "Cuisines",
        "question": "What is the main spice in Indian curry?",
        "options": ["Turmeric", "Cumin", "Coriander", "Cardamom"],
        "correct_answer": "Turmeric",
        "difficulty": "medium"
    },
    {
        "id": "foo_230",
        "category": "Food",
        "subcategory": "Cuisines",
        "question": "What is kimchi?",
        "options": ["Fermented vegetables", "Rice dish", "Noodle soup", "Grilled meat"],
        "correct_answer": "Fermented vegetables",
        "difficulty": "medium"
    },
    {
        "id": "foo_231",
        "category": "Food",
        "subcategory": "Cuisines",
        "question": "What is the main ingredient in traditional Mexican mole sauce?",
        "options": ["Chocolate", "Tomatoes", "Peppers", "Avocado"],
        "correct_answer": "Chocolate",
        "difficulty": "hard"
    },
    {
        "id": "foo_232",
        "category": "Food",
        "subcategory": "Cuisines",
        "question": "What is tzatziki made from?",
        "options": ["Yogurt and cucumber", "Tahini and lemon", "Cream and dill", "Sour cream and herbs"],
        "correct_answer": "Yogurt and cucumber",
        "difficulty": "medium"
    },
    {
        "id": "foo_233",
        "category": "Food",
        "subcategory": "Cuisines",
        "question": "What is the base of a traditional French roux?",
        "options": ["Butter and flour", "Oil and flour", "Cream and flour", "Eggs and flour"],
        "correct_answer": "Butter and flour",
        "difficulty": "hard"
    },
    {
        "id": "foo_234",
        "category": "Food",
        "subcategory": "Cuisines",
        "question": "What is pho?",
        "options": ["Vietnamese soup", "Thai curry", "Chinese noodles", "Korean stew"],
        "correct_answer": "Vietnamese soup",
        "difficulty": "medium"
    },
    
    # Baking (5 questions)
    {
        "id": "foo_235",
        "category": "Food",
        "subcategory": "Baking",
        "question": "What makes bread rise?",
        "options": ["Yeast producing carbon dioxide", "Baking powder", "Steam", "Air incorporation"],
        "correct_answer": "Yeast producing carbon dioxide",
        "difficulty": "medium"
    },
    {
        "id": "foo_236",
        "category": "Food",
        "subcategory": "Baking",
        "question": "What is the difference between baking powder and baking soda?",
        "options": ["Baking powder contains acid, baking soda doesn't", "They're the same thing", "Baking soda is stronger", "Baking powder is for cakes only"],
        "correct_answer": "Baking powder contains acid, baking soda doesn't",
        "difficulty": "hard"
    },
    {
        "id": "foo_237",
        "category": "Food",
        "subcategory": "Baking",
        "question": "What is gluten?",
        "options": ["A protein in wheat", "A type of sugar", "A leavening agent", "A type of fat"],
        "correct_answer": "A protein in wheat",
        "difficulty": "medium"
    },
    {
        "id": "foo_238",
        "category": "Food",
        "subcategory": "Baking",
        "question": "What temperature is typically used for proofing bread dough?",
        "options": ["75-80°F", "90-100°F", "60-65°F", "100-110°F"],
        "correct_answer": "75-80°F",
        "difficulty": "hard"
    },
    {
        "id": "foo_239",
        "category": "Food",
        "subcategory": "Baking",
        "question": "What is a sourdough starter?",
        "options": ["Wild yeast and bacteria culture", "Commercial yeast", "Baking powder mixture", "Flavoring agent"],
        "correct_answer": "Wild yeast and bacteria culture",
        "difficulty": "medium"
    },
    
    # Beverages (5 questions)
    {
        "id": "foo_240",
        "category": "Food",
        "subcategory": "Beverages",
        "question": "What country produces the most coffee in the world?",
        "options": ["Brazil", "Colombia", "Vietnam", "Ethiopia"],
        "correct_answer": "Brazil",
        "difficulty": "medium"
    },
    {
        "id": "foo_241",
        "category": "Food",
        "subcategory": "Beverages",
        "question": "What is the main ingredient in a traditional margarita?",
        "options": ["Tequila", "Vodka", "Rum", "Gin"],
        "correct_answer": "Tequila",
        "difficulty": "medium"
    },
    {
        "id": "foo_242",
        "category": "Food",
        "subcategory": "Beverages",
        "question": "What type of tea is oolong?",
        "options": ["Partially fermented", "Fully fermented", "Unfermented", "Green tea"],
        "correct_answer": "Partially fermented",
        "difficulty": "hard"
    },
    {
        "id": "foo_243",
        "category": "Food",
        "subcategory": "Beverages",
        "question": "What is champagne?",
        "options": ["Sparkling wine from France", "Any sparkling wine", "Sweet dessert wine", "Fortified wine"],
        "correct_answer": "Sparkling wine from France",
        "difficulty": "medium"
    },
    {
        "id": "foo_244",
        "category": "Food",
        "subcategory": "Beverages",
        "question": "What plant is tequila made from?",
        "options": ["Blue agave", "Cactus", "Sugarcane", "Corn"],
        "correct_answer": "Blue agave",
        "difficulty": "hard"
    },
    
    # Desserts (4 questions)
    {
        "id": "foo_245",
        "category": "Food",
        "subcategory": "Desserts",
        "question": "What is the main ingredient in meringue?",
        "options": ["Egg whites", "Cream", "Flour", "Butter"],
        "correct_answer": "Egg whites",
        "difficulty": "medium"
    },
    {
        "id": "foo_246",
        "category": "Food",
        "subcategory": "Desserts",
        "question": "What is baklava made with?",
        "options": ["Phyllo dough and nuts", "Puff pastry and cream", "Cake and fruit", "Bread and honey"],
        "correct_answer": "Phyllo dough and nuts",
        "difficulty": "medium"
    },
    {
        "id": "foo_247",
        "category": "Food",
        "subcategory": "Desserts",
        "question": "What is the difference between ice cream and gelato?",
        "options": ["Gelato has less air and fat", "Gelato is frozen harder", "Ice cream is Italian", "They're the same"],
        "correct_answer": "Gelato has less air and fat",
        "difficulty": "hard"
    },
    {
        "id": "foo_248",
        "category": "Food",
        "subcategory": "Desserts",
        "question": "What is a profiterole?",
        "options": ["Cream-filled pastry", "Layered cake", "Fruit tart", "Chocolate truffle"],
        "correct_answer": "Cream-filled pastry",
        "difficulty": "hard"
    },
    
    # Cooking Techniques (3 questions)
    {
        "id": "foo_249",
        "category": "Food",
        "subcategory": "Cooking Techniques",
        "question": "What does it mean to 'julienne' vegetables?",
        "options": ["Cut into thin strips", "Dice into cubes", "Slice thinly", "Chop roughly"],
        "correct_answer": "Cut into thin strips",
        "difficulty": "medium"
    },
    {
        "id": "foo_250",
        "category": "Food",
        "subcategory": "Cooking Techniques",
        "question": "What is the Maillard reaction?",
        "options": ["Browning of proteins and sugars", "Caramelization of sugar", "Fermentation process", "Emulsification of fats"],
        "correct_answer": "Browning of proteins and sugars",
        "difficulty": "hard"
    },
    {
        "id": "foo_251",
        "category": "Food",
        "subcategory": "Cooking Techniques",
        "question": "What does 'al dente' mean when cooking pasta?",
        "options": ["Firm to the bite", "Fully cooked", "Undercooked", "Overcooked"],
        "correct_answer": "Firm to the bite",
        "difficulty": "medium"
    },
    
    # Food History (3 questions)
    {
        "id": "foo_252",
        "category": "Food",
        "subcategory": "Food History",
        "question": "Where was the sandwich invented?",
        "options": ["England", "France", "Italy", "United States"],
        "correct_answer": "England",
        "difficulty": "medium"
    },
    {
        "id": "foo_253",
        "category": "Food",
        "subcategory": "Food History",
        "question": "What was the first food eaten in space?",
        "options": ["Applesauce", "Bread", "Chocolate", "Ice cream"],
        "correct_answer": "Applesauce",
        "difficulty": "hard"
    },
    {
        "id": "foo_254",
        "category": "Food",
        "subcategory": "Food History",
        "question": "Which empire first cultivated potatoes?",
        "options": ["Inca", "Aztec", "Maya", "Roman"],
        "correct_answer": "Inca",
        "difficulty": "hard"
    },
    
    # Sauces & Condiments (2 questions)
    {
        "id": "foo_255",
        "category": "Food",
        "subcategory": "Sauces & Condiments",
        "question": "What are the five French mother sauces?",
        "options": ["Béchamel, Velouté, Espagnole, Hollandaise, Tomato", "Marinara, Alfredo, Pesto, Carbonara, Bolognese", "Soy, Teriyaki, Hoisin, Oyster, Fish", "Ranch, Blue cheese, Caesar, Thousand Island, Italian"],
        "correct_answer": "Béchamel, Velouté, Espagnole, Hollandaise, Tomato",
        "difficulty": "hard"
    },
    {
        "id": "foo_256",
        "category": "Food",
        "subcategory": "Sauces & Condiments",
        "question": "What is aioli?",
        "options": ["Garlic mayonnaise", "Tomato sauce", "Olive oil dip", "Herb butter"],
        "correct_answer": "Garlic mayonnaise",
        "difficulty": "medium"
    }
]

# Add the new questions to Food category
data['categories']['Food'].extend(new_food_questions)

# Sort Food questions by ID
data['categories']['Food'].sort(key=lambda x: x['id'])

# Save the updated database
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Added {len(new_food_questions)} new Food questions")
print(f"New Food total: {len(data['categories']['Food'])} questions")

# Show breakdown by subcategory
from collections import Counter
subcats = Counter(q['subcategory'] for q in data['categories']['Food'])
print("\nFood subcategory distribution:")
for subcat, count in sorted(subcats.items(), key=lambda x: x[1], reverse=True):
    print(f"  {subcat}: {count}")

# Show difficulty distribution of new questions
difficulties = Counter(q['difficulty'] for q in new_food_questions)
print(f"\nDifficulty distribution of new questions:")
for diff, count in sorted(difficulties.items()):
    print(f"  {diff}: {count}")
