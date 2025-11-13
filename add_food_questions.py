import json

# Load the current database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# New Food questions (foo_176 to foo_203) - 28 total
new_food_questions = [
    # Sauces & Condiments (4 questions)
    {
        "id": "foo_176",
        "category": "Food",
        "subcategory": "Sauces & Condiments",
        "question": "What is the main ingredient in traditional pesto sauce?",
        "options": ["Basil", "Parsley", "Cilantro", "Oregano"],
        "correct_answer": "Basil",
        "difficulty": "medium"
    },
    {
        "id": "foo_177",
        "category": "Food",
        "subcategory": "Sauces & Condiments",
        "question": "What French sauce is made with egg yolks and butter?",
        "options": ["Hollandaise", "Béarnaise", "Beurre blanc", "Mornay"],
        "correct_answer": "Hollandaise",
        "difficulty": "hard"
    },
    {
        "id": "foo_178",
        "category": "Food",
        "subcategory": "Sauces & Condiments",
        "question": "What is sriracha sauce primarily made from?",
        "options": ["Chili peppers", "Tomatoes", "Soybeans", "Fish"],
        "correct_answer": "Chili peppers",
        "difficulty": "medium"
    },
    {
        "id": "foo_179",
        "category": "Food",
        "subcategory": "Sauces & Condiments",
        "question": "What is the main ingredient in Worcestershire sauce?",
        "options": ["Anchovies", "Oysters", "Sardines", "Clams"],
        "correct_answer": "Anchovies",
        "difficulty": "hard"
    },
    
    # Food History (3 questions)
    {
        "id": "foo_180",
        "category": "Food",
        "subcategory": "Food History",
        "question": "Which ancient civilization is credited with inventing ice cream?",
        "options": ["China", "Egypt", "Greece", "Rome"],
        "correct_answer": "China",
        "difficulty": "hard"
    },
    {
        "id": "foo_181",
        "category": "Food",
        "subcategory": "Food History",
        "question": "What food did the Aztecs use as currency?",
        "options": ["Cacao beans", "Corn", "Vanilla pods", "Chili peppers"],
        "correct_answer": "Cacao beans",
        "difficulty": "medium"
    },
    {
        "id": "foo_182",
        "category": "Food",
        "subcategory": "Food History",
        "question": "Which fruit was historically known as a 'love apple'?",
        "options": ["Tomato", "Strawberry", "Apple", "Peach"],
        "correct_answer": "Tomato",
        "difficulty": "hard"
    },
    
    # Desserts (3 questions)
    {
        "id": "foo_183",
        "category": "Food",
        "subcategory": "Desserts",
        "question": "What Italian dessert translates to 'pick me up'?",
        "options": ["Tiramisu", "Panna cotta", "Cannoli", "Gelato"],
        "correct_answer": "Tiramisu",
        "difficulty": "medium"
    },
    {
        "id": "foo_184",
        "category": "Food",
        "subcategory": "Desserts",
        "question": "What is the main flavoring in a traditional crème brûlée?",
        "options": ["Vanilla", "Chocolate", "Coffee", "Caramel"],
        "correct_answer": "Vanilla",
        "difficulty": "medium"
    },
    {
        "id": "foo_185",
        "category": "Food",
        "subcategory": "Desserts",
        "question": "What French pastry is made of choux dough filled with cream?",
        "options": ["Éclair", "Macaron", "Madeleine", "Croissant"],
        "correct_answer": "Éclair",
        "difficulty": "hard"
    },
    
    # Cooking Techniques (3 questions)
    {
        "id": "foo_186",
        "category": "Food",
        "subcategory": "Cooking Techniques",
        "question": "What cooking technique involves submerging food in vacuum-sealed bags in temperature-controlled water?",
        "options": ["Sous vide", "Braising", "Poaching", "Steaming"],
        "correct_answer": "Sous vide",
        "difficulty": "hard"
    },
    {
        "id": "foo_187",
        "category": "Food",
        "subcategory": "Cooking Techniques",
        "question": "What is the process of briefly cooking vegetables in boiling water, then plunging them into ice water?",
        "options": ["Blanching", "Parboiling", "Simmering", "Poaching"],
        "correct_answer": "Blanching",
        "difficulty": "medium"
    },
    {
        "id": "foo_188",
        "category": "Food",
        "subcategory": "Cooking Techniques",
        "question": "What does it mean to 'deglaze' a pan?",
        "options": ["Add liquid to dissolve browned bits", "Remove excess oil", "Season with salt", "Cool it rapidly"],
        "correct_answer": "Add liquid to dissolve browned bits",
        "difficulty": "hard"
    },
    
    # Cuisines (3 questions)
    {
        "id": "foo_189",
        "category": "Food",
        "subcategory": "Cuisines",
        "question": "What is the staple grain in traditional Ethiopian cuisine?",
        "options": ["Teff", "Rice", "Wheat", "Quinoa"],
        "correct_answer": "Teff",
        "difficulty": "hard"
    },
    {
        "id": "foo_190",
        "category": "Food",
        "subcategory": "Cuisines",
        "question": "What spice blend is essential in Indian garam masala?",
        "options": ["Multiple warming spices", "Only chili peppers", "Turmeric and ginger", "Curry leaves"],
        "correct_answer": "Multiple warming spices",
        "difficulty": "medium"
    },
    {
        "id": "foo_191",
        "category": "Food",
        "subcategory": "Cuisines",
        "question": "What is miso made from?",
        "options": ["Fermented soybeans", "Rice flour", "Seaweed", "Fish paste"],
        "correct_answer": "Fermented soybeans",
        "difficulty": "medium"
    },
    
    # Baking (3 questions)
    {
        "id": "foo_192",
        "category": "Food",
        "subcategory": "Baking",
        "question": "What ingredient causes bread to rise?",
        "options": ["Yeast", "Baking soda", "Salt", "Sugar"],
        "correct_answer": "Yeast",
        "difficulty": "easy"
    },
    {
        "id": "foo_193",
        "category": "Food",
        "subcategory": "Baking",
        "question": "What is the process of working dough to develop gluten called?",
        "options": ["Kneading", "Folding", "Laminating", "Proofing"],
        "correct_answer": "Kneading",
        "difficulty": "medium"
    },
    {
        "id": "foo_194",
        "category": "Food",
        "subcategory": "Baking",
        "question": "What is a 'poolish' in baking?",
        "options": ["A wet pre-ferment", "A type of flour", "A glazing technique", "A decorative pattern"],
        "correct_answer": "A wet pre-ferment",
        "difficulty": "hard"
    },
    
    # Beverages (3 questions)
    {
        "id": "foo_195",
        "category": "Food",
        "subcategory": "Beverages",
        "question": "What type of tea is Earl Grey flavored with?",
        "options": ["Bergamot", "Jasmine", "Lavender", "Rose"],
        "correct_answer": "Bergamot",
        "difficulty": "medium"
    },
    {
        "id": "foo_196",
        "category": "Food",
        "subcategory": "Beverages",
        "question": "What is the main difference between ale and lager?",
        "options": ["Type of yeast and fermentation temperature", "Hop content", "Alcohol percentage", "Color"],
        "correct_answer": "Type of yeast and fermentation temperature",
        "difficulty": "hard"
    },
    {
        "id": "foo_197",
        "category": "Food",
        "subcategory": "Beverages",
        "question": "What spirit is traditionally used in a mojito?",
        "options": ["Rum", "Vodka", "Tequila", "Gin"],
        "correct_answer": "Rum",
        "difficulty": "medium"
    },
    
    # Famous Chefs/Restaurants (2 questions)
    {
        "id": "foo_198",
        "category": "Food",
        "subcategory": "Famous Chefs/Restaurants",
        "question": "Which chef is known for pioneering California cuisine at Chez Panisse?",
        "options": ["Alice Waters", "Thomas Keller", "Wolfgang Puck", "Julia Child"],
        "correct_answer": "Alice Waters",
        "difficulty": "hard"
    },
    {
        "id": "foo_199",
        "category": "Food",
        "subcategory": "Famous Chefs/Restaurants",
        "question": "What restaurant holds the record for the most Michelin stars ever awarded?",
        "options": ["El Bulli", "The French Laundry", "Noma", "Per Se"],
        "correct_answer": "El Bulli",
        "difficulty": "hard"
    },
    
    # Dishes (2 questions)
    {
        "id": "foo_200",
        "category": "Food",
        "subcategory": "Dishes",
        "question": "What is the main protein in a traditional Greek moussaka?",
        "options": ["Lamb", "Chicken", "Beef", "Pork"],
        "correct_answer": "Lamb",
        "difficulty": "medium"
    },
    {
        "id": "foo_201",
        "category": "Food",
        "subcategory": "Dishes",
        "question": "What dish is traditionally served at a Thanksgiving dinner?",
        "options": ["Turkey", "Ham", "Chicken", "Beef"],
        "correct_answer": "Turkey",
        "difficulty": "easy"
    },
    
    # Ingredients (2 questions)
    {
        "id": "foo_202",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "What vegetable is sauerkraut made from?",
        "options": ["Cabbage", "Cucumber", "Radish", "Turnip"],
        "correct_answer": "Cabbage",
        "difficulty": "medium"
    },
    {
        "id": "foo_203",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "What gives saffron its distinctive yellow color?",
        "options": ["Crocin pigment", "Beta-carotene", "Turmeric", "Paprika"],
        "correct_answer": "Crocin pigment",
        "difficulty": "hard"
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
