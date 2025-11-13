import json

# Load the current database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Find highest Food ID
food_ids = [q['id'] for q in data['categories']['Food']]
food_ids.sort()
print(f"Last Food ID: {food_ids[-1]}")

# New replacement Food questions (3 total) - foo_204 to foo_206
new_food_questions = [
    {
        "id": "foo_204",
        "category": "Food",
        "subcategory": "Cooking Techniques",
        "question": "What cooking method uses dry heat in an oven?",
        "options": ["Baking", "Boiling", "Steaming", "Frying"],
        "correct_answer": "Baking",
        "difficulty": "easy"
    },
    {
        "id": "foo_205",
        "category": "Food",
        "subcategory": "Desserts",
        "question": "What French dessert consists of caramelized sugar on top of custard?",
        "options": ["Crème brûlée", "Crème caramel", "Mousse", "Flan"],
        "correct_answer": "Crème brûlée",
        "difficulty": "medium"
    },
    {
        "id": "foo_206",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "What is tofu made from?",
        "options": ["Soybeans", "Rice", "Wheat", "Chickpeas"],
        "correct_answer": "Soybeans",
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
