import json

# Load the current database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# 12 replacement Bible questions - being VERY specific and unique
new_bible_questions = [
    {
        "id": "bib_260",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Who was the wise king known for building the Temple in Jerusalem?",
        "options": ["Solomon", "David", "Saul", "Hezekiah"],
        "correct_answer": "Solomon",
        "difficulty": "easy"
    },
    {
        "id": "bib_261",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "Which disciple walked on water with Jesus?",
        "options": ["Peter", "John", "James", "Andrew"],
        "correct_answer": "Peter",
        "difficulty": "medium"
    },
    {
        "id": "bib_262",
        "category": "Bible",
        "subcategory": "Biblical Languages",
        "question": "What does 'Maranatha' mean?",
        "options": ["Our Lord, come", "God be with you", "Peace", "Blessed"],
        "correct_answer": "Our Lord, come",
        "difficulty": "hard"
    },
    {
        "id": "bib_263",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "What type of tree did Zacchaeus climb to see Jesus?",
        "options": ["Sycamore", "Fig", "Olive", "Cedar"],
        "correct_answer": "Sycamore",
        "difficulty": "hard"
    },
    {
        "id": "bib_264",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What did God create on the third day?",
        "options": ["Land and vegetation", "Sky and sea", "Sun and moon", "Animals"],
        "correct_answer": "Land and vegetation",
        "difficulty": "medium"
    },
    {
        "id": "bib_265",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "Where did Jesus perform his first miracle?",
        "options": ["Cana", "Capernaum", "Jerusalem", "Nazareth"],
        "correct_answer": "Cana",
        "difficulty": "hard"
    },
    {
        "id": "bib_266",
        "category": "Bible",
        "subcategory": "Biblical History",
        "question": "What river did the Israelites cross to enter the Promised Land?",
        "options": ["Jordan River", "Euphrates", "Nile", "Tigris"],
        "correct_answer": "Jordan River",
        "difficulty": "medium"
    },
    {
        "id": "bib_267",
        "category": "Bible",
        "subcategory": "Biblical Theology",
        "question": "What are the first four books of the New Testament called?",
        "options": ["The Gospels", "The Epistles", "The Prophets", "The Pentateuch"],
        "correct_answer": "The Gospels",
        "difficulty": "medium"
    },
    {
        "id": "bib_268",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What did Cain offer to God as a sacrifice?",
        "options": ["Crops from the field", "A lamb", "Gold", "Incense"],
        "correct_answer": "Crops from the field",
        "difficulty": "hard"
    },
    {
        "id": "bib_269",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "What was the name of the Roman centurion whose servant Jesus healed?",
        "options": ["Cornelius", "Julius", "Marcus", "Gaius"],
        "correct_answer": "Cornelius",
        "difficulty": "hard"
    },
    {
        "id": "bib_270",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "How many books are in the entire Protestant Bible?",
        "options": ["66", "73", "39", "27"],
        "correct_answer": "66",
        "difficulty": "hard"
    },
    {
        "id": "bib_271",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which prophet was known for his visions of dry bones coming to life?",
        "options": ["Ezekiel", "Jeremiah", "Isaiah", "Daniel"],
        "correct_answer": "Ezekiel",
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
