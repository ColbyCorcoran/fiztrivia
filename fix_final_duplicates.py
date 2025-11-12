import json

# Load the database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Remove the 4 duplicates
ids_to_remove = ['spt_267', 'sci_270', 'ear_254', 'ear_263']

for category in data['categories']:
    data['categories'][category] = [
        q for q in data['categories'][category] 
        if q['id'] not in ids_to_remove
    ]

# Add 4 unique replacements
new_questions = [
    {
        "id": "spt_271",
        "category": "Sports",
        "subcategory": "Hockey",
        "question": "What protective equipment do goalies wear on their legs?",
        "options": ["Pads", "Shin guards", "Skates", "Helmets"],
        "correct_answer": "Pads",
        "difficulty": "easy"
    },
    {
        "id": "sci_276",
        "category": "Science",
        "subcategory": "Chemistry",
        "question": "What is the chemical symbol for mercury?",
        "options": ["Hg", "Me", "Mc", "Mr"],
        "correct_answer": "Hg",
        "difficulty": "hard"
    },
    {
        "id": "ear_265",
        "category": "Earth",
        "subcategory": "Geography",
        "question": "What is the capital of Japan?",
        "options": ["Tokyo", "Osaka", "Kyoto", "Nagoya"],
        "correct_answer": "Tokyo",
        "difficulty": "easy"
    },
    {
        "id": "ear_266",
        "category": "Earth",
        "subcategory": "Animals",
        "question": "What is a group of whales called?",
        "options": ["Pod", "School", "Herd", "Pack"],
        "correct_answer": "Pod",
        "difficulty": "medium"
    }
]

# Add new questions
for q in new_questions:
    data['categories'][q['category']].append(q)

# Sort each category
for category in data['categories']:
    data['categories'][category].sort(key=lambda x: x['id'])

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Removed 4 duplicates and added 4 unique replacements")
for cat in ['Bible', 'Earth', 'Entertainment', 'Food', 'History', 'Science', 'Sports']:
    count = len(data['categories'][cat])
    print(f"  {cat}: {count}")
print(f"\nTotal: {sum(len(data['categories'][cat]) for cat in data['categories'])}")
