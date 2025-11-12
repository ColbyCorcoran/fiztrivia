import json

# Load the current database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Find highest Bible ID
bible_ids = [q['id'] for q in data['categories']['Bible']]
bible_ids.sort()
print(f"Last Bible ID: {bible_ids[-1]}")

# New replacement Bible questions (5 total) - bib_205 to bib_209
new_bible_questions = [
    {
        "id": "bib_205",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which prophet was taken up to heaven in a whirlwind?",
        "options": ["Elijah", "Elisha", "Isaiah", "Jeremiah"],
        "correct_answer": "Elijah",
        "difficulty": "medium"
    },
    {
        "id": "bib_206",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What was the name of Ruth's mother-in-law?",
        "options": ["Naomi", "Hannah", "Rachel", "Leah"],
        "correct_answer": "Naomi",
        "difficulty": "medium"
    },
    {
        "id": "bib_207",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "On which island was the apostle John when he wrote Revelation?",
        "options": ["Patmos", "Cyprus", "Crete", "Malta"],
        "correct_answer": "Patmos",
        "difficulty": "hard"
    },
    {
        "id": "bib_208",
        "category": "Bible",
        "subcategory": "Biblical Languages",
        "question": "What does 'Hallelujah' mean?",
        "options": ["Praise the Lord", "God is great", "Peace be with you", "Thank God"],
        "correct_answer": "Praise the Lord",
        "difficulty": "medium"
    },
    {
        "id": "bib_209",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "What is the shortest book in the New Testament?",
        "options": ["2 John", "Philemon", "Jude", "3 John"],
        "correct_answer": "2 John",
        "difficulty": "hard"
    }
]

# Add the new questions
data['categories']['Bible'].extend(new_bible_questions)
data['categories']['Bible'].sort(key=lambda x: x['id'])

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Added {len(new_bible_questions)} replacement Bible questions")
print(f"New Bible total: {len(data['categories']['Bible'])} questions")
