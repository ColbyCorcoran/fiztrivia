import json

# Load existing questions
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# New Bible questions (bib_251 to bib_300) - 50 questions
# Distribution: Old Testament (20), New Testament (15), Biblical History (5),
# Bible Trivia (4), Biblical Theology (3), Biblical Languages (3)
# Emphasis on hard/medium difficulty

new_questions = [
    # Old Testament (20 questions) - bib_251-270
    {
        "id": "bib_251",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which book of the Bible contains the story of the Tower of Babel?",
        "options": ["Genesis", "Exodus", "Numbers", "Deuteronomy"],
        "correct_answer": "Genesis",
        "difficulty": "hard"
    },
    {
        "id": "bib_252",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What did Esau sell to Jacob for a bowl of stew?",
        "options": ["His birthright", "His cattle", "His land", "His servants"],
        "correct_answer": "His birthright",
        "difficulty": "medium"
    },
    {
        "id": "bib_253",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "How many times did Naaman dip himself in the Jordan River to be healed?",
        "options": ["7", "3", "10", "12"],
        "correct_answer": "7",
        "difficulty": "hard"
    },
    {
        "id": "bib_254",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which prophetess was the only female judge of Israel mentioned in the Bible?",
        "options": ["Deborah", "Miriam", "Huldah", "Esther"],
        "correct_answer": "Deborah",
        "difficulty": "hard"
    },
    {
        "id": "bib_255",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What did Lot's wife turn into when she looked back at Sodom?",
        "options": ["A pillar of salt", "Stone", "Dust", "Ashes"],
        "correct_answer": "A pillar of salt",
        "difficulty": "medium"
    },
    {
        "id": "bib_256",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which king had a dream about a statue made of different materials?",
        "options": ["Nebuchadnezzar", "Belshazzar", "Darius", "Cyrus"],
        "correct_answer": "Nebuchadnezzar",
        "difficulty": "hard"
    },
    {
        "id": "bib_257",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What was the name of Ruth's mother-in-law?",
        "options": ["Naomi", "Rachel", "Leah", "Hannah"],
        "correct_answer": "Naomi",
        "difficulty": "medium"
    },
    {
        "id": "bib_258",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which prophet confronted King Ahab about killing Naboth for his vineyard?",
        "options": ["Elijah", "Elisha", "Isaiah", "Jeremiah"],
        "correct_answer": "Elijah",
        "difficulty": "hard"
    },
    {
        "id": "bib_259",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "How many sons of Jesse did Samuel see before anointing David as king?",
        "options": ["7", "6", "8", "5"],
        "correct_answer": "7",
        "difficulty": "hard"
    },
    {
        "id": "bib_260",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What material was the Ark of the Covenant made of?",
        "options": ["Acacia wood overlaid with gold", "Cedar wood", "Pure gold", "Bronze"],
        "correct_answer": "Acacia wood overlaid with gold",
        "difficulty": "hard"
    },
    {
        "id": "bib_261",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which book of poetry contains the phrase 'For everything there is a season'?",
        "options": ["Ecclesiastes", "Proverbs", "Psalms", "Song of Solomon"],
        "correct_answer": "Ecclesiastes",
        "difficulty": "medium"
    },
    {
        "id": "bib_262",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What did the Israelites use to mark their doorposts during the final plague in Egypt?",
        "options": ["Lamb's blood", "Oil", "Red paint", "Ashes"],
        "correct_answer": "Lamb's blood",
        "difficulty": "medium"
    },
    {
        "id": "bib_263",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which prophet was taken up to heaven in a whirlwind?",
        "options": ["Elijah", "Elisha", "Enoch", "Moses"],
        "correct_answer": "Elijah",
        "difficulty": "medium"
    },
    {
        "id": "bib_264",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "How many years did the Israelites wander in the wilderness?",
        "options": ["40", "30", "50", "70"],
        "correct_answer": "40",
        "difficulty": "medium"
    },
    {
        "id": "bib_265",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which son of David tried to overthrow him as king?",
        "options": ["Absalom", "Solomon", "Adonijah", "Amnon"],
        "correct_answer": "Absalom",
        "difficulty": "hard"
    },
    {
        "id": "bib_266",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What was the name of the garden where Adam and Eve lived?",
        "options": ["Eden", "Gethsemane", "Olivet", "Paradise"],
        "correct_answer": "Eden",
        "difficulty": "easy"
    },
    {
        "id": "bib_267",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which book contains the story of Job's suffering and faith?",
        "options": ["Job", "Psalms", "Ecclesiastes", "Proverbs"],
        "correct_answer": "Job",
        "difficulty": "easy"
    },
    {
        "id": "bib_268",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What sign did God give Noah that He would never flood the earth again?",
        "options": ["A rainbow", "A dove", "A cloud", "Lightning"],
        "correct_answer": "A rainbow",
        "difficulty": "easy"
    },
    {
        "id": "bib_269",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "Which priest's sons were killed by God for offering unauthorized fire?",
        "options": ["Aaron", "Eli", "Samuel", "Zadok"],
        "correct_answer": "Aaron",
        "difficulty": "hard"
    },
    {
        "id": "bib_270",
        "category": "Bible",
        "subcategory": "Old Testament",
        "question": "What did Solomon ask God for when given the opportunity to request anything?",
        "options": ["Wisdom", "Wealth", "Long life", "Victory in battle"],
        "correct_answer": "Wisdom",
        "difficulty": "medium"
    },

    # New Testament (15 questions) - bib_271-285
    {
        "id": "bib_271",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "On which mountain did Jesus deliver the Sermon on the Mount?",
        "options": ["Mount of Beatitudes", "Mount Sinai", "Mount Hermon", "Mount Tabor"],
        "correct_answer": "Mount of Beatitudes",
        "difficulty": "hard"
    },
    {
        "id": "bib_272",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "What was the name of the high priest who questioned Jesus before his crucifixion?",
        "options": ["Caiaphas", "Annas", "Nicodemus", "Gamaliel"],
        "correct_answer": "Caiaphas",
        "difficulty": "hard"
    },
    {
        "id": "bib_273",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "Which Gospel was written by a physician?",
        "options": ["Luke", "Matthew", "Mark", "John"],
        "correct_answer": "Luke",
        "difficulty": "hard"
    },
    {
        "id": "bib_274",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "How many lepers did Jesus heal, but only one returned to thank Him?",
        "options": ["10", "7", "12", "5"],
        "correct_answer": "10",
        "difficulty": "medium"
    },
    {
        "id": "bib_275",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "What was the name of the man Jesus raised from the dead in Bethany?",
        "options": ["Lazarus", "Jairus", "Nicodemus", "Joseph"],
        "correct_answer": "Lazarus",
        "difficulty": "medium"
    },
    {
        "id": "bib_276",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "Which disciple doubted Jesus' resurrection until he saw Him?",
        "options": ["Thomas", "Peter", "Philip", "Nathanael"],
        "correct_answer": "Thomas",
        "difficulty": "medium"
    },
    {
        "id": "bib_277",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "What was the occupation of Matthew before becoming a disciple?",
        "options": ["Tax collector", "Fisherman", "Carpenter", "Physician"],
        "correct_answer": "Tax collector",
        "difficulty": "medium"
    },
    {
        "id": "bib_278",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "Which book of the New Testament has only one chapter?",
        "options": ["Philemon", "Jude", "2 John", "3 John"],
        "correct_answer": "Philemon",
        "difficulty": "hard"
    },
    {
        "id": "bib_279",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "What was the name of the island where John wrote the book of Revelation?",
        "options": ["Patmos", "Cyprus", "Crete", "Malta"],
        "correct_answer": "Patmos",
        "difficulty": "hard"
    },
    {
        "id": "bib_280",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "Which woman is mentioned as a seller of purple cloth in the book of Acts?",
        "options": ["Lydia", "Priscilla", "Phoebe", "Dorcas"],
        "correct_answer": "Lydia",
        "difficulty": "hard"
    },
    {
        "id": "bib_281",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "How many days after His resurrection did Jesus ascend into heaven?",
        "options": ["40", "30", "50", "7"],
        "correct_answer": "40",
        "difficulty": "hard"
    },
    {
        "id": "bib_282",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "What parable did Jesus tell about a father and his two sons?",
        "options": ["The Prodigal Son", "The Good Samaritan", "The Lost Sheep", "The Sower"],
        "correct_answer": "The Prodigal Son",
        "difficulty": "medium"
    },
    {
        "id": "bib_283",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "Which two disciples were brothers and fishermen?",
        "options": ["Peter and Andrew", "James and John", "Matthew and Thomas", "Philip and Bartholomew"],
        "correct_answer": "Peter and Andrew",
        "difficulty": "medium"
    },
    {
        "id": "bib_284",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "What language was most of the New Testament originally written in?",
        "options": ["Greek", "Hebrew", "Aramaic", "Latin"],
        "correct_answer": "Greek",
        "difficulty": "hard"
    },
    {
        "id": "bib_285",
        "category": "Bible",
        "subcategory": "New Testament",
        "question": "Who was released instead of Jesus during Pilate's trial?",
        "options": ["Barabbas", "Simon", "Judas", "Ananias"],
        "correct_answer": "Barabbas",
        "difficulty": "medium"
    },

    # Biblical History (5 questions) - bib_286-290
    {
        "id": "bib_286",
        "category": "Bible",
        "subcategory": "Biblical History",
        "question": "What year is traditionally given for the fall of Jerusalem to Babylon?",
        "options": ["586 BC", "722 BC", "70 AD", "135 AD"],
        "correct_answer": "586 BC",
        "difficulty": "hard"
    },
    {
        "id": "bib_287",
        "category": "Bible",
        "subcategory": "Biblical History",
        "question": "Which empire conquered the Northern Kingdom of Israel in 722 BC?",
        "options": ["Assyrian Empire", "Babylonian Empire", "Persian Empire", "Greek Empire"],
        "correct_answer": "Assyrian Empire",
        "difficulty": "hard"
    },
    {
        "id": "bib_288",
        "category": "Bible",
        "subcategory": "Biblical History",
        "question": "How many years did the Babylonian exile last?",
        "options": ["70", "40", "50", "100"],
        "correct_answer": "70",
        "difficulty": "hard"
    },
    {
        "id": "bib_289",
        "category": "Bible",
        "subcategory": "Biblical History",
        "question": "Which Roman emperor destroyed the Second Temple in Jerusalem in 70 AD?",
        "options": ["Titus", "Nero", "Vespasian", "Hadrian"],
        "correct_answer": "Titus",
        "difficulty": "hard"
    },
    {
        "id": "bib_290",
        "category": "Bible",
        "subcategory": "Biblical History",
        "question": "What was the name of the Jewish revolt against Rome that occurred in 66-73 AD?",
        "options": ["First Jewish-Roman War", "Bar Kokhba Revolt", "Maccabean Revolt", "Hasmonean Rebellion"],
        "correct_answer": "First Jewish-Roman War",
        "difficulty": "hard"
    },

    # Bible Trivia (4 questions) - bib_291-294
    {
        "id": "bib_291",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "Which book of the Bible does not mention the word 'God'?",
        "options": ["Esther", "Ruth", "Song of Solomon", "Obadiah"],
        "correct_answer": "Esther",
        "difficulty": "hard"
    },
    {
        "id": "bib_292",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "How many chapters are in the book of Genesis?",
        "options": ["50", "40", "66", "27"],
        "correct_answer": "50",
        "difficulty": "hard"
    },
    {
        "id": "bib_293",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "Which book of the Bible is the shortest?",
        "options": ["2 John", "3 John", "Philemon", "Obadiah"],
        "correct_answer": "2 John",
        "difficulty": "hard"
    },
    {
        "id": "bib_294",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "How many psalms are in the book of Psalms?",
        "options": ["150", "100", "120", "200"],
        "correct_answer": "150",
        "difficulty": "medium"
    },

    # Biblical Theology (3 questions) - bib_295-297
    {
        "id": "bib_295",
        "category": "Bible",
        "subcategory": "Biblical Theology",
        "question": "What does the term 'Trinity' refer to in Christian theology?",
        "options": ["Father, Son, and Holy Spirit", "Three patriarchs", "Three kingdoms", "Three covenants"],
        "correct_answer": "Father, Son, and Holy Spirit",
        "difficulty": "medium"
    },
    {
        "id": "bib_296",
        "category": "Bible",
        "subcategory": "Biblical Theology",
        "question": "What is the term for God becoming human in Jesus Christ?",
        "options": ["Incarnation", "Transfiguration", "Ascension", "Resurrection"],
        "correct_answer": "Incarnation",
        "difficulty": "hard"
    },
    {
        "id": "bib_297",
        "category": "Bible",
        "subcategory": "Biblical Theology",
        "question": "What does 'justification by faith' mean in Christian theology?",
        "options": ["Being declared righteous through belief", "Proving one's worthiness", "Earning salvation", "Following the law"],
        "correct_answer": "Being declared righteous through belief",
        "difficulty": "hard"
    },

    # Biblical Languages (3 questions) - bib_298-300
    {
        "id": "bib_298",
        "category": "Bible",
        "subcategory": "Biblical Languages",
        "question": "What does 'Hallelujah' mean?",
        "options": ["Praise the Lord", "God is good", "Amen", "Peace"],
        "correct_answer": "Praise the Lord",
        "difficulty": "medium"
    },
    {
        "id": "bib_299",
        "category": "Bible",
        "subcategory": "Biblical Languages",
        "question": "What does 'Emmanuel' or 'Immanuel' mean?",
        "options": ["God with us", "God saves", "God is mighty", "God is holy"],
        "correct_answer": "God with us",
        "difficulty": "medium"
    },
    {
        "id": "bib_300",
        "category": "Bible",
        "subcategory": "Biblical Languages",
        "question": "What does 'Abba' mean in Aramaic?",
        "options": ["Father", "Lord", "Master", "Teacher"],
        "correct_answer": "Father",
        "difficulty": "hard"
    }
]

# Add new questions to Bible category
data['categories']['Bible'].extend(new_questions)

# Save updated database
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ Added {len(new_questions)} Bible questions")
print(f"New range: bib_251 to bib_300")
print(f"\nDistribution:")
print(f"  Old Testament: 20 questions (emphasis on hard/medium)")
print(f"  New Testament: 15 questions (emphasis on hard/medium)")
print(f"  Biblical History: 5 questions (all hard)")
print(f"  Bible Trivia: 4 questions (hard/medium)")
print(f"  Biblical Theology: 3 questions (hard/medium)")
print(f"  Biblical Languages: 3 questions (medium/hard)")
print(f"\nTotal Bible questions: {len(data['categories']['Bible'])}")
