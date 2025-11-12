import json

# Load the current database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# 4 replacement Food questions - being VERY careful to be unique
new_food_questions = [
    {
        "id": "foo_257",
        "category": "Food",
        "subcategory": "Cooking Techniques",
        "question": "What is the French term for vegetables cut into thin, matchstick-like strips?",
        "options": ["Julienne", "Brunoise", "Chiffonade", "Mirepoix"],
        "correct_answer": "Julienne",
        "difficulty": "hard"
    },
    {
        "id": "foo_258",
        "category": "Food",
        "subcategory": "Sauces & Condiments",
        "question": "What is the traditional base of a béarnaise sauce?",
        "options": ["Hollandaise with tarragon", "Butter and wine", "Cream and egg", "Mayonnaise"],
        "correct_answer": "Hollandaise with tarragon",
        "difficulty": "hard"
    },
    {
        "id": "foo_259",
        "category": "Food",
        "subcategory": "Desserts",
        "question": "What Italian dessert consists of coffee-soaked ladyfingers layered with mascarpone cheese?",
        "options": ["Tiramisu", "Panna cotta", "Zabaglione", "Affogato"],
        "correct_answer": "Tiramisu",
        "difficulty": "medium"
    },
    {
        "id": "foo_260",
        "category": "Food",
        "subcategory": "Food History",
        "question": "Which food preservation method involves submerging food in vinegar or brine?",
        "options": ["Pickling", "Curing", "Smoking", "Drying"],
        "correct_answer": "Pickling",
        "difficulty": "medium"
    }
]

# Add the new questions
data['categories']['Food'].extend(new_food_questions)
data['categories']['Food'].sort(key=lambda x: x['id'])

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Added {len(new_food_questions)} replacement Food questions")
print(f"New Food total: {len(data['categories']['Food'])} questions")
