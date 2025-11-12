import json

# Load the current database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# New Bible questions (bib_190 to bib_204) - 15 total
new_bible_questions = [
    # Biblical Languages (3 questions)
    {
        "id": "bib_190",
        "category": "Bible",
        "subcategory": "Biblical Languages",
        "question": "What does the Hebrew word 'Shalom' mean?",
        "options": ["Peace", "Love", "Faith", "Hope"],
        "correct_answer": "Peace",
        "difficulty": "medium"
    },
    {
        "id": "bib_191",
        "category": "Bible",
        "subcategory": "Biblical Languages",
        "question": "What does the Greek word 'Agape' refer to?",
        "options": ["Unconditional love", "Friendship", "Joy", "Wisdom"],
        "correct_answer": "Unconditional love",
        "difficulty": "medium"
    },
    {
        "id": "bib_192",
        "category": "Bible",
        "subcategory": "Biblical Languages",
        "question": "What does 'Amen' mean?",
        "options": ["So be it/Truly", "Praise God", "Forever", "The end"],
        "correct_answer": "So be it/Truly",
        "difficulty": "hard"
    },
    
    # Biblical History (3 questions)
    {
        "id": "bib_193",
        "category": "Bible",
        "subcategory": "Biblical History",
        "question": "Which empire destroyed the Temple in Jerusalem in 70 AD?",
        "options": ["Roman Empire", "Babylonian Empire", "Persian Empire", "Greek Empire"],
        "correct_answer": "Roman Empire",
        "difficulty": "hard"
    },
    {
        "id": "bib_194",
        "category": "Bible",
        "subcategory": "Biblical History",
        "question": "Who led the Israelites out of Egypt?",
        "options": ["Moses", "Aaron", "Joshua", "Abraham"],
        "correct_answer": "Moses",
        "difficulty": "easy"
    },
    {
        "id": "bib_195",
        "category": "Bible",
        "subcategory": "Biblical History",
        "question": "Which king built the first Temple in Jerusalem?",
        "options": ["Solomon", "David", "Saul", "Hezekiah"],
        "correct_answer": "Solomon",
        "difficulty": "medium"
    },
    
    # Biblical Theology (3 questions)
    {
        "id": "bib_196",
        "category": "Bible",
        "subcategory": "Biblical Theology",
        "question": "How many books are in the Protestant Old Testament?",
        "options": ["39", "27", "66", "46"],
        "correct_answer": "39",
        "difficulty": "hard"
    },
    {
        "id": "bib_197",
        "category": "Bible",
        "subcategory": "Biblical Theology",
        "question": "What is the first book of the Bible?",
        "options": ["Genesis", "Exodus", "Matthew", "Psalms"],
        "correct_answer": "Genesis",
        "difficulty": "easy"
    },
    {
        "id": "bib_198",
        "category": "Bible",
        "subcategory": "Biblical Theology",
        "question": "What are the first five books of the Bible called?",
        "options": ["The Pentateuch", "The Gospels", "The Epistles", "The Prophets"],
        "correct_answer": "The Pentateuch",
        "difficulty": "hard"
    },
    
    # Bible Trivia (2 questions)
    {
        "id": "bib_199",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "What was the occupation of the apostle Peter before following Jesus?",
        "options": ["Fisherman", "Tax collector", "Carpenter", "Tentmaker"],
        "correct_answer": "Fisherman",
        "difficulty": "medium"
    },
    {
        "id": "bib_200",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "How many days and nights did it rain during Noah's flood?",
        "options": ["40", "7", "100", "30"],
        "correct_answer": "40",
        "difficulty": "medium"
    },
    
    # New Testament (2 questions)
    {
        "id": "bib_201",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "How many disciples did Jesus choose?",
        "options": ["12", "10", "7", "70"],
        "correct_answer": "12",
        "difficulty": "easy"
    },
    {
        "id": "bib_202",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "Which Gospel was written by a physician?",
        "options": ["Luke", "Mark", "Matthew", "John"],
        "correct_answer": "Luke",
        "difficulty": "hard"
    },
    
    # Old Testament (2 questions)
    {
        "id": "bib_203",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Who was swallowed by a great fish?",
        "options": ["Jonah", "Daniel", "Elijah", "Elisha"],
        "correct_answer": "Jonah",
        "difficulty": "easy"
    },
    {
        "id": "bib_204",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What was the name of Abraham's nephew?",
        "options": ["Lot", "Isaac", "Ishmael", "Jacob"],
        "correct_answer": "Lot",
        "difficulty": "medium"
    }
]

# Add the new questions to Bible category
data['categories']['Bible'].extend(new_bible_questions)

# Sort Bible questions by ID
data['categories']['Bible'].sort(key=lambda x: x['id'])

# Save the updated database
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Added {len(new_bible_questions)} new Bible questions")
print(f"New Bible total: {len(data['categories']['Bible'])} questions")

# Show breakdown by subcategory
from collections import Counter
subcats = Counter(q['subcategory'] for q in data['categories']['Bible'])
print("\nBible subcategory distribution:")
for subcat, count in sorted(subcats.items(), key=lambda x: x[1], reverse=True):
    print(f"  {subcat}: {count}")

# Show difficulty distribution of new questions
difficulties = Counter(q['difficulty'] for q in new_bible_questions)
print(f"\nDifficulty distribution of new questions:")
for diff, count in sorted(difficulties.items()):
    print(f"  {diff}: {count}")
