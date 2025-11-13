import json

# Load database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# 22 unique questions with fresh IDs (bib_301-322)
final_22_questions = [
    # Old Testament (10 questions)
    {
        "id": "bib_301",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which prophet married a prostitute as a symbol of God's love for Israel?",
        "options": ["Hosea", "Jeremiah", "Ezekiel", "Amos"],
        "correct_answer": "Hosea",
        "difficulty": "hard"
    },
    {
        "id": "bib_302",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What instrument did the Israelites blow to make the walls of Jericho fall?",
        "options": ["Trumpets (shofars)", "Drums", "Cymbals", "Harps"],
        "correct_answer": "Trumpets (shofars)",
        "difficulty": "medium"
    },
    {
        "id": "bib_303",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which king of Judah found the Book of the Law in the temple?",
        "options": ["Josiah", "Hezekiah", "Manasseh", "Amon"],
        "correct_answer": "Josiah",
        "difficulty": "hard"
    },
    {
        "id": "bib_304",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What food did God provide the Israelites in the wilderness besides manna?",
        "options": ["Quail", "Fish", "Bread", "Honey"],
        "correct_answer": "Quail",
        "difficulty": "medium"
    },
    {
        "id": "bib_305",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which prophet's name means 'The Lord is my God'?",
        "options": ["Elijah", "Isaiah", "Jeremiah", "Ezekiel"],
        "correct_answer": "Elijah",
        "difficulty": "hard"
    },
    {
        "id": "bib_306",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What did Esau trade to Jacob for a bowl of stew?",
        "options": ["His birthright", "His cattle", "His land", "His servants"],
        "correct_answer": "His birthright",
        "difficulty": "medium"
    },
    {
        "id": "bib_307",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which book follows Deuteronomy in the Old Testament?",
        "options": ["Joshua", "Judges", "Ruth", "1 Samuel"],
        "correct_answer": "Joshua",
        "difficulty": "medium"
    },
    {
        "id": "bib_308",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What precious metals did the Israelites take from Egypt before the Exodus?",
        "options": ["Gold and silver", "Only gold", "Only silver", "Bronze"],
        "correct_answer": "Gold and silver",
        "difficulty": "hard"
    },
    {
        "id": "bib_309",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What was the name of King Saul's father?",
        "options": ["Kish", "Jesse", "Nahor", "Terah"],
        "correct_answer": "Kish",
        "difficulty": "hard"
    },
    {
        "id": "bib_310",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which book contains the story of Queen Esther saving the Jewish people?",
        "options": ["Esther", "Ruth", "Judges", "1 Samuel"],
        "correct_answer": "Esther",
        "difficulty": "easy"
    },

    # New Testament (8 questions)
    {
        "id": "bib_311",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "What gifts did the wise men bring to baby Jesus?",
        "options": ["Gold, frankincense, and myrrh", "Gold, silver, and bronze", "Jewels, spices, and cloth", "Gold, incense, and oil"],
        "correct_answer": "Gold, frankincense, and myrrh",
        "difficulty": "medium"
    },
    {
        "id": "bib_312",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "What was the name of the garden where Jesus prayed before His arrest?",
        "options": ["Gethsemane", "Eden", "Kidron", "Olivet"],
        "correct_answer": "Gethsemane",
        "difficulty": "medium"
    },
    {
        "id": "bib_313",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "Which disciple was a Zealot before following Jesus?",
        "options": ["Simon the Zealot", "Simon Peter", "Judas Iscariot", "Matthew"],
        "correct_answer": "Simon the Zealot",
        "difficulty": "hard"
    },
    {
        "id": "bib_314",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "Which epistle is addressed to a man named Theophilus?",
        "options": ["Luke (Gospel) and Acts", "1 Timothy", "Philemon", "Titus"],
        "correct_answer": "Luke (Gospel) and Acts",
        "difficulty": "hard"
    },
    {
        "id": "bib_315",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "Which church did Paul address in his letter about the 'fruit of the Spirit'?",
        "options": ["Galatians", "Ephesians", "Colossians", "Philippians"],
        "correct_answer": "Galatians",
        "difficulty": "hard"
    },
    {
        "id": "bib_316",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "Which New Testament book contains only one chapter?",
        "options": ["Philemon", "Jude", "2 John", "3 John"],
        "correct_answer": "Philemon",
        "difficulty": "hard"
    },
    {
        "id": "bib_317",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "What was the occupation of Simon Peter before becoming a disciple?",
        "options": ["Fisherman", "Tax collector", "Carpenter", "Physician"],
        "correct_answer": "Fisherman",
        "difficulty": "easy"
    },
    {
        "id": "bib_318",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "On what day of the week did Jesus rise from the dead?",
        "options": ["Sunday", "Saturday", "Friday", "Monday"],
        "correct_answer": "Sunday",
        "difficulty": "easy"
    },

    # Biblical History (1 question)
    {
        "id": "bib_319",
        "category": "Bible",
        "subcategory": "Biblical History",
        "question": "Which Jewish festival commemorates the Israelites' deliverance from Egypt?",
        "options": ["Passover", "Pentecost", "Tabernacles", "Purim"],
        "correct_answer": "Passover",
        "difficulty": "medium"
    },

    # Biblical Theology (2 questions)
    {
        "id": "bib_320",
        "category": "Bible",
        "subcategory": "Biblical Theology",
        "question": "What does the word 'Christ' literally mean?",
        "options": ["Anointed One", "Savior", "King", "Prophet"],
        "correct_answer": "Anointed One",
        "difficulty": "hard"
    },
    {
        "id": "bib_321",
        "category": "Bible",
        "subcategory": "Biblical Theology",
        "question": "What does the doctrine of the Trinity teach?",
        "options": ["One God in three persons", "Three separate Gods", "Three stages of God", "Three names of God"],
        "correct_answer": "One God in three persons",
        "difficulty": "medium"
    },

    # Biblical Languages (1 question)
    {
        "id": "bib_322",
        "category": "Bible",
        "subcategory": "Biblical Languages",
        "question": "What does 'Eloi, Eloi, lama sabachthani' mean?",
        "options": ["My God, my God, why have you forsaken me?", "Father, into your hands I commit my spirit", "It is finished", "Father, forgive them"],
        "correct_answer": "My God, my God, why have you forsaken me?",
        "difficulty": "hard"
    }
]

# Add questions
data['categories']['Bible'].extend(final_22_questions)

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ Added {len(final_22_questions)} Bible questions")
print(f"IDs: bib_301 to bib_322")
print(f"Total Bible questions: {len(data['categories']['Bible'])}")
