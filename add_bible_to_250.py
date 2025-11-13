import json

# Load the current database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# New Bible questions (bib_210 to bib_259) - 50 total
# Distribution: OT (20), NT (15), History (5), Theology (5), Languages (3), Trivia (2)
new_bible_questions = [
    # Old Testament (20 questions)
    {
        "id": "bib_210",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What was the name of Jacob's favorite son?",
        "options": ["Joseph", "Benjamin", "Judah", "Reuben"],
        "correct_answer": "Joseph",
        "difficulty": "medium"
    },
    {
        "id": "bib_211",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Who interpreted Pharaoh's dreams in Egypt?",
        "options": ["Joseph", "Daniel", "Moses", "Aaron"],
        "correct_answer": "Joseph",
        "difficulty": "medium"
    },
    {
        "id": "bib_212",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What did Esau sell to Jacob for a bowl of stew?",
        "options": ["His birthright", "His inheritance", "His land", "His servants"],
        "correct_answer": "His birthright",
        "difficulty": "medium"
    },
    {
        "id": "bib_213",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which king had 700 wives and 300 concubines?",
        "options": ["Solomon", "David", "Saul", "Rehoboam"],
        "correct_answer": "Solomon",
        "difficulty": "hard"
    },
    {
        "id": "bib_214",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What did God use to speak to Moses on Mount Sinai?",
        "options": ["A burning bush", "Thunder and lightning", "An angel", "A pillar of cloud"],
        "correct_answer": "Thunder and lightning",
        "difficulty": "hard"
    },
    {
        "id": "bib_215",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Who was the first king of Israel?",
        "options": ["Saul", "David", "Solomon", "Samuel"],
        "correct_answer": "Saul",
        "difficulty": "medium"
    },
    {
        "id": "bib_216",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What musical instrument did David play?",
        "options": ["Harp", "Trumpet", "Flute", "Drum"],
        "correct_answer": "Harp",
        "difficulty": "medium"
    },
    {
        "id": "bib_217",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "How many plagues did God send on Egypt?",
        "options": ["10", "7", "12", "40"],
        "correct_answer": "10",
        "difficulty": "medium"
    },
    {
        "id": "bib_218",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What was the name of Abraham's wife?",
        "options": ["Sarah", "Rebecca", "Rachel", "Leah"],
        "correct_answer": "Sarah",
        "difficulty": "easy"
    },
    {
        "id": "bib_219",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which prophet confronted King Ahab about Naboth's vineyard?",
        "options": ["Elijah", "Elisha", "Isaiah", "Jeremiah"],
        "correct_answer": "Elijah",
        "difficulty": "hard"
    },
    {
        "id": "bib_220",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What did Samson use to kill 1,000 Philistines?",
        "options": ["Jawbone of a donkey", "Sword", "Spear", "Slingshot"],
        "correct_answer": "Jawbone of a donkey",
        "difficulty": "medium"
    },
    {
        "id": "bib_221",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Who was thrown into a den of lions?",
        "options": ["Daniel", "Shadrach", "Meshach", "Abednego"],
        "correct_answer": "Daniel",
        "difficulty": "easy"
    },
    {
        "id": "bib_222",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What was the name of the garden where Adam and Eve lived?",
        "options": ["Garden of Eden", "Garden of Gethsemane", "Paradise", "Zion"],
        "correct_answer": "Garden of Eden",
        "difficulty": "easy"
    },
    {
        "id": "bib_223",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which book of the Bible is a collection of wise sayings?",
        "options": ["Proverbs", "Psalms", "Ecclesiastes", "Song of Solomon"],
        "correct_answer": "Proverbs",
        "difficulty": "medium"
    },
    {
        "id": "bib_224",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Who led the Israelites into the Promised Land after Moses died?",
        "options": ["Joshua", "Caleb", "Aaron", "Eleazar"],
        "correct_answer": "Joshua",
        "difficulty": "medium"
    },
    {
        "id": "bib_225",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What animal did Balaam ride when it saw an angel?",
        "options": ["Donkey", "Horse", "Camel", "Ox"],
        "correct_answer": "Donkey",
        "difficulty": "hard"
    },
    {
        "id": "bib_226",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "How many sons did Jacob have?",
        "options": ["12", "10", "7", "13"],
        "correct_answer": "12",
        "difficulty": "medium"
    },
    {
        "id": "bib_227",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What did God create on the seventh day?",
        "options": ["He rested", "Animals", "Humans", "Light"],
        "correct_answer": "He rested",
        "difficulty": "easy"
    },
    {
        "id": "bib_228",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which prophet was fed by ravens?",
        "options": ["Elijah", "Elisha", "Ezekiel", "Jeremiah"],
        "correct_answer": "Elijah",
        "difficulty": "hard"
    },
    {
        "id": "bib_229",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What was the source of Samson's strength?",
        "options": ["His long hair", "A special diet", "Divine weapons", "Prayer"],
        "correct_answer": "His long hair",
        "difficulty": "medium"
    },
    
    # New Testament (15 questions)
    {
        "id": "bib_230",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "Who baptized Jesus?",
        "options": ["John the Baptist", "Peter", "James", "Andrew"],
        "correct_answer": "John the Baptist",
        "difficulty": "easy"
    },
    {
        "id": "bib_231",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "What was Matthew's occupation before following Jesus?",
        "options": ["Tax collector", "Fisherman", "Carpenter", "Physician"],
        "correct_answer": "Tax collector",
        "difficulty": "medium"
    },
    {
        "id": "bib_232",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "How many loaves of bread did Jesus use to feed the 5,000?",
        "options": ["5", "7", "12", "2"],
        "correct_answer": "5",
        "difficulty": "medium"
    },
    {
        "id": "bib_233",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "Who denied Jesus three times before the rooster crowed?",
        "options": ["Peter", "Judas", "Thomas", "John"],
        "correct_answer": "Peter",
        "difficulty": "medium"
    },
    {
        "id": "bib_234",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "What was the name of the disciple who betrayed Jesus?",
        "options": ["Judas Iscariot", "Peter", "Thomas", "Matthew"],
        "correct_answer": "Judas Iscariot",
        "difficulty": "easy"
    },
    {
        "id": "bib_235",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "In which city was Jesus born?",
        "options": ["Bethlehem", "Nazareth", "Jerusalem", "Capernaum"],
        "correct_answer": "Bethlehem",
        "difficulty": "easy"
    },
    {
        "id": "bib_236",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "Who rolled away the stone from Jesus' tomb?",
        "options": ["An angel", "Mary Magdalene", "Peter", "Joseph of Arimathea"],
        "correct_answer": "An angel",
        "difficulty": "medium"
    },
    {
        "id": "bib_237",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "What was the name of the Roman governor who sentenced Jesus?",
        "options": ["Pontius Pilate", "Herod", "Caesar", "Felix"],
        "correct_answer": "Pontius Pilate",
        "difficulty": "medium"
    },
    {
        "id": "bib_238",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "Which disciple was known as 'the beloved disciple'?",
        "options": ["John", "Peter", "James", "Andrew"],
        "correct_answer": "John",
        "difficulty": "hard"
    },
    {
        "id": "bib_239",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "How many days did Jesus fast in the wilderness?",
        "options": ["40", "30", "7", "14"],
        "correct_answer": "40",
        "difficulty": "medium"
    },
    {
        "id": "bib_240",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "Who was the first person to see Jesus after his resurrection?",
        "options": ["Mary Magdalene", "Peter", "John", "Thomas"],
        "correct_answer": "Mary Magdalene",
        "difficulty": "hard"
    },
    {
        "id": "bib_241",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "What was Paul's name before his conversion?",
        "options": ["Saul", "Simon", "Samuel", "Solomon"],
        "correct_answer": "Saul",
        "difficulty": "medium"
    },
    {
        "id": "bib_242",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "Which Gospel is written by a tax collector?",
        "options": ["Matthew", "Mark", "Luke", "John"],
        "correct_answer": "Matthew",
        "difficulty": "hard"
    },
    {
        "id": "bib_243",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "How many pieces of silver did Judas receive for betraying Jesus?",
        "options": ["30", "20", "40", "50"],
        "correct_answer": "30",
        "difficulty": "hard"
    },
    {
        "id": "bib_244",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "What did Jesus turn water into at a wedding?",
        "options": ["Wine", "Oil", "Milk", "Honey"],
        "correct_answer": "Wine",
        "difficulty": "easy"
    },
    
    # Biblical History (5 questions)
    {
        "id": "bib_245",
        "category": "Bible",
        "subcategory": "Biblical History",
        "question": "What empire conquered Jerusalem in 586 BC?",
        "options": ["Babylonian Empire", "Assyrian Empire", "Persian Empire", "Greek Empire"],
        "correct_answer": "Babylonian Empire",
        "difficulty": "hard"
    },
    {
        "id": "bib_246",
        "category": "Bible",
        "subcategory": "Biblical History",
        "question": "Who rebuilt the walls of Jerusalem after the exile?",
        "options": ["Nehemiah", "Ezra", "Zerubbabel", "Joshua"],
        "correct_answer": "Nehemiah",
        "difficulty": "hard"
    },
    {
        "id": "bib_247",
        "category": "Bible",
        "subcategory": "Biblical History",
        "question": "Which Persian king allowed the Jews to return to Jerusalem?",
        "options": ["Cyrus", "Darius", "Xerxes", "Artaxerxes"],
        "correct_answer": "Cyrus",
        "difficulty": "hard"
    },
    {
        "id": "bib_248",
        "category": "Bible",
        "subcategory": "Biblical History",
        "question": "How many years did the Israelites wander in the wilderness?",
        "options": ["40", "30", "50", "70"],
        "correct_answer": "40",
        "difficulty": "medium"
    },
    {
        "id": "bib_249",
        "category": "Bible",
        "subcategory": "Biblical History",
        "question": "What sea did the Israelites cross when fleeing Egypt?",
        "options": ["Red Sea", "Dead Sea", "Mediterranean Sea", "Sea of Galilee"],
        "correct_answer": "Red Sea",
        "difficulty": "medium"
    },
    
    # Biblical Theology (5 questions)
    {
        "id": "bib_250",
        "category": "Bible",
        "subcategory": "Biblical Theology",
        "question": "How many books are in the New Testament?",
        "options": ["27", "39", "66", "22"],
        "correct_answer": "27",
        "difficulty": "hard"
    },
    {
        "id": "bib_251",
        "category": "Bible",
        "subcategory": "Biblical Theology",
        "question": "What does the word 'Gospel' mean?",
        "options": ["Good news", "Holy word", "Sacred text", "Divine message"],
        "correct_answer": "Good news",
        "difficulty": "medium"
    },
    {
        "id": "bib_252",
        "category": "Bible",
        "subcategory": "Biblical Theology",
        "question": "How many books of the Bible did Moses write?",
        "options": ["5", "3", "7", "10"],
        "correct_answer": "5",
        "difficulty": "hard"
    },
    {
        "id": "bib_253",
        "category": "Bible",
        "subcategory": "Biblical Theology",
        "question": "What is the last book of the Old Testament?",
        "options": ["Malachi", "Zechariah", "Nehemiah", "Chronicles"],
        "correct_answer": "Malachi",
        "difficulty": "hard"
    },
    {
        "id": "bib_254",
        "category": "Bible",
        "subcategory": "Biblical Theology",
        "question": "How many commandments did God give to Moses?",
        "options": ["10", "7", "12", "40"],
        "correct_answer": "10",
        "difficulty": "easy"
    },
    
    # Biblical Languages (3 questions)
    {
        "id": "bib_255",
        "category": "Bible",
        "subcategory": "Biblical Languages",
        "question": "What does 'Emmanuel' mean?",
        "options": ["God with us", "Prince of Peace", "Messiah", "Savior"],
        "correct_answer": "God with us",
        "difficulty": "medium"
    },
    {
        "id": "bib_256",
        "category": "Bible",
        "subcategory": "Biblical Languages",
        "question": "What does 'Hosanna' mean?",
        "options": ["Save now", "Praise God", "Holy one", "Blessed be"],
        "correct_answer": "Save now",
        "difficulty": "hard"
    },
    {
        "id": "bib_257",
        "category": "Bible",
        "subcategory": "Biblical Languages",
        "question": "What does 'Messiah' mean?",
        "options": ["Anointed one", "King", "Prophet", "Savior"],
        "correct_answer": "Anointed one",
        "difficulty": "medium"
    },
    
    # Bible Trivia (2 questions)
    {
        "id": "bib_258",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "What is the longest book in the Bible?",
        "options": ["Psalms", "Genesis", "Isaiah", "Jeremiah"],
        "correct_answer": "Psalms",
        "difficulty": "hard"
    },
    {
        "id": "bib_259",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "What is the shortest verse in the Bible?",
        "options": ["Jesus wept", "God is love", "Rejoice always", "Pray continually"],
        "correct_answer": "Jesus wept",
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
