import json

# Load the database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Remove sci_276
data['categories']['Science'] = [
    q for q in data['categories']['Science'] 
    if q['id'] != 'sci_276'
]

# Add a truly unique replacement - checking a topic I haven't covered
new_question = {
    "id": "sci_277",
    "category": "Science",
    "subcategory": "Chemistry",
    "question": "What is the chemical symbol for lead?",
    "options": ["Pb", "Ld", "Le", "Pl"],
    "correct_answer": "Pb",
    "difficulty": "hard"
}

data['categories']['Science'].append(new_question)
data['categories']['Science'].sort(key=lambda x: x['id'])

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Replaced sci_276 with sci_277 (lead symbol)")
print(f"Science total: {len(data['categories']['Science'])}")
print(f"Total database: {sum(len(data['categories'][cat]) for cat in data['categories'])}")
