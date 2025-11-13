import json

# Load database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# 7 more replacement questions - very specific
final_questions = [
    {
        "id": "bib_252",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What precious metal did the Israelites take from Egypt before the Exodus?",
        "options": ["Gold and silver", "Only gold", "Only silver", "Bronze"],
        "correct_answer": "Gold and silver",
        "difficulty": "hard"
    },
    {
        "id": "bib_254",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which book follows Deuteronomy in the Old Testament?",
        "options": ["Joshua", "Judges", "Ruth", "1 Samuel"],
        "correct_answer": "Joshua",
        "difficulty": "medium"
    },
    {
        "id": "bib_257",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What was the name of King Saul's father?",
        "options": ["Kish", "Jesse", "Nahor", "Terah"],
        "correct_answer": "Kish",
        "difficulty": "hard"
    },
    {
        "id": "bib_263",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which prophet's name means 'The Lord is my God'?",
        "options": ["Elijah", "Isaiah", "Jeremiah", "Ezekiel"],
        "correct_answer": "Elijah",
        "difficulty": "hard"
    },
    {
        "id": "bib_266",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which king of Judah found the Book of the Law in the temple?",
        "options": ["Josiah", "Hezekiah", "Manasseh", "Amon"],
        "correct_answer": "Josiah",
        "difficulty": "hard"
    },
    {
        "id": "bib_273",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "What gifts did the wise men bring to baby Jesus?",
        "options": ["Gold, frankincense, and myrrh", "Gold, silver, and bronze", "Jewels, spices, and cloth", "Gold, incense, and oil"],
        "correct_answer": "Gold, frankincense, and myrrh",
        "difficulty": "medium"
    },
    {
        "id": "bib_281",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "What was the name of the garden where Jesus prayed before His arrest?",
        "options": ["Gethsemane", "Eden", "Kidron", "Olivet"],
        "correct_answer": "Gethsemane",
        "difficulty": "medium"
    }
]

# Add questions
data['categories']['Bible'].extend(final_questions)

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ Added {len(final_questions)} final Bible questions")
print(f"Total Bible questions: {len(data['categories']['Bible'])}")
