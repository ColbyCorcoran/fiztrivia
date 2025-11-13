import json

# Load database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# 7 unique replacement questions
replacements = [
    {
        "id": "foo_301",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "What is the Japanese name for the fermented soybean paste used in soup?",
        "options": ["Miso", "Natto", "Tofu", "Edamame"],
        "correct_answer": "Miso",
        "difficulty": "medium"
    },
    {
        "id": "foo_302",
        "category": "Food",
        "subcategory": "Dishes",
        "question": "What is the French term for vegetables cut into thin strips?",
        "options": ["Julienne", "Brunoise", "Chiffonade", "Dice"],
        "correct_answer": "Julienne",
        "difficulty": "hard"
    },
    {
        "id": "foo_303",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "Which spice comes from the dried stigma of a crocus flower?",
        "options": ["Saffron", "Turmeric", "Paprika", "Cumin"],
        "correct_answer": "Saffron",
        "difficulty": "hard"
    },
    {
        "id": "foo_304",
        "category": "Food",
        "subcategory": "Beverages",
        "question": "What is the name of the traditional Japanese rice wine?",
        "options": ["Sake", "Soju", "Baijiu", "Shochu"],
        "correct_answer": "Sake",
        "difficulty": "easy"
    },
    {
        "id": "foo_305",
        "category": "Food",
        "subcategory": "Cuisines",
        "question": "Which country is the origin of the dish ceviche?",
        "options": ["Peru", "Mexico", "Spain", "Brazil"],
        "correct_answer": "Peru",
        "difficulty": "medium"
    },
    {
        "id": "foo_306",
        "category": "Food",
        "subcategory": "Ingredients",
        "question": "What type of flour is used to make traditional Japanese tempura batter?",
        "options": ["All-purpose wheat flour", "Rice flour", "Corn flour", "Buckwheat flour"],
        "correct_answer": "All-purpose wheat flour",
        "difficulty": "hard"
    },
    {
        "id": "foo_307",
        "category": "Food",
        "subcategory": "Food History",
        "question": "Which fruit was once so valuable it was used as currency?",
        "options": ["Pineapple", "Banana", "Orange", "Apple"],
        "correct_answer": "Pineapple",
        "difficulty": "hard"
    }
]

# Add replacements
data['categories']['Food'].extend(replacements)

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ Added {len(replacements)} replacement Food questions")
print(f"IDs: foo_301 to foo_307")
print(f"Total Food questions: {len(data['categories']['Food'])}")
