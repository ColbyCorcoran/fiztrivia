import json

# Load database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# 4 completely unique questions
final_4 = [
    {
        "id": "bib_323",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which judge of Israel had 30 sons who rode 30 donkeys?",
        "options": ["Jair", "Gideon", "Samson", "Tola"],
        "correct_answer": "Jair",
        "difficulty": "hard"
    },
    {
        "id": "bib_324",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "What was the name of the sorcerer who tried to buy the power of the Holy Spirit?",
        "options": ["Simon", "Elymas", "Bar-Jesus", "Apollos"],
        "correct_answer": "Simon",
        "difficulty": "hard"
    },
    {
        "id": "bib_325",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which king of Israel reigned for only seven days before committing suicide?",
        "options": ["Zimri", "Ahab", "Jehu", "Baasha"],
        "correct_answer": "Zimri",
        "difficulty": "hard"
    },
    {
        "id": "bib_326",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "What was the name of Paul's companion who was left sick in Miletus?",
        "options": ["Trophimus", "Tychicus", "Titus", "Timothy"],
        "correct_answer": "Trophimus",
        "difficulty": "hard"
    }
]

# Add questions
data['categories']['Bible'].extend(final_4)

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ Added {len(final_4)} final Bible questions")
print(f"IDs: bib_323 to bib_326")
print(f"Total Bible questions: {len(data['categories']['Bible'])}")
