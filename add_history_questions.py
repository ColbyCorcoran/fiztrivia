import json

# Load the current database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# New History questions (his_175 to his_201) - 27 total
new_history_questions = [
    # Church History (9 questions - factual, non-controversial)
    {
        "id": "his_175",
        "category": "History",
        "subcategory": "Church History",
        "question": "In what year did the Great Schism split the Christian church into Eastern and Western branches?",
        "options": ["1054", "1204", "867", "1378"],
        "correct_answer": "1054",
        "difficulty": "hard"
    },
    {
        "id": "his_176",
        "category": "History",
        "subcategory": "Church History",
        "question": "What were the series of religious wars in the medieval period called?",
        "options": ["The Crusades", "The Inquisition", "The Reconquista", "The Reformation"],
        "correct_answer": "The Crusades",
        "difficulty": "medium"
    },
    {
        "id": "his_177",
        "category": "History",
        "subcategory": "Church History",
        "question": "Who is traditionally credited with starting the Protestant Reformation in 1517?",
        "options": ["Martin Luther", "John Calvin", "Henry VIII", "John Wycliffe"],
        "correct_answer": "Martin Luther",
        "difficulty": "medium"
    },
    {
        "id": "his_178",
        "category": "History",
        "subcategory": "Church History",
        "question": "What document did Martin Luther reportedly nail to a church door?",
        "options": ["95 Theses", "Diet of Worms", "Augsburg Confession", "Book of Concord"],
        "correct_answer": "95 Theses",
        "difficulty": "medium"
    },
    {
        "id": "his_179",
        "category": "History",
        "subcategory": "Church History",
        "question": "What religious order was founded by St. Francis of Assisi?",
        "options": ["Franciscans", "Dominicans", "Jesuits", "Benedictines"],
        "correct_answer": "Franciscans",
        "difficulty": "hard"
    },
    {
        "id": "his_180",
        "category": "History",
        "subcategory": "Church History",
        "question": "What council formally defined the Christian biblical canon?",
        "options": ["Council of Hippo", "Council of Nicaea", "Council of Trent", "Council of Chalcedon"],
        "correct_answer": "Council of Hippo",
        "difficulty": "hard"
    },
    {
        "id": "his_181",
        "category": "History",
        "subcategory": "Church History",
        "question": "Who was the first Archbishop of Canterbury?",
        "options": ["Augustine", "Anselm", "Thomas Becket", "Dunstan"],
        "correct_answer": "Augustine",
        "difficulty": "hard"
    },
    {
        "id": "his_182",
        "category": "History",
        "subcategory": "Church History",
        "question": "What year did the Vatican become an independent city-state?",
        "options": ["1929", "1870", "1517", "1492"],
        "correct_answer": "1929",
        "difficulty": "hard"
    },
    {
        "id": "his_183",
        "category": "History",
        "subcategory": "Church History",
        "question": "What religious text was translated by William Tyndale in the 16th century?",
        "options": ["The Bible", "The Quran", "The Torah", "The Vedas"],
        "correct_answer": "The Bible",
        "difficulty": "medium"
    },
    
    # Medieval History (9 questions)
    {
        "id": "his_184",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What year did William the Conqueror invade England?",
        "options": ["1066", "1215", "1348", "1492"],
        "correct_answer": "1066",
        "difficulty": "medium"
    },
    {
        "id": "his_185",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What document did King John sign in 1215 limiting royal power?",
        "options": ["Magna Carta", "Bill of Rights", "Constitution", "Charter of Liberties"],
        "correct_answer": "Magna Carta",
        "difficulty": "medium"
    },
    {
        "id": "his_186",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What pandemic killed approximately one-third of Europe's population in the 14th century?",
        "options": ["Black Death", "Spanish Flu", "Smallpox", "Cholera"],
        "correct_answer": "Black Death",
        "difficulty": "medium"
    },
    {
        "id": "his_187",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What empire did Charlemagne rule?",
        "options": ["Holy Roman Empire", "Byzantine Empire", "Ottoman Empire", "Mongol Empire"],
        "correct_answer": "Holy Roman Empire",
        "difficulty": "hard"
    },
    {
        "id": "his_188",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What was the feudal system's lowest class called?",
        "options": ["Serfs", "Knights", "Vassals", "Peasants"],
        "correct_answer": "Serfs",
        "difficulty": "medium"
    },
    {
        "id": "his_189",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "Who led the Mongol Empire during its greatest expansion?",
        "options": ["Genghis Khan", "Kublai Khan", "Tamerlane", "Attila"],
        "correct_answer": "Genghis Khan",
        "difficulty": "medium"
    },
    {
        "id": "his_190",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What was the capital of the Byzantine Empire?",
        "options": ["Constantinople", "Rome", "Athens", "Alexandria"],
        "correct_answer": "Constantinople",
        "difficulty": "medium"
    },
    {
        "id": "his_191",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What war lasted 116 years between England and France?",
        "options": ["Hundred Years' War", "War of the Roses", "Thirty Years' War", "Seven Years' War"],
        "correct_answer": "Hundred Years' War",
        "difficulty": "hard"
    },
    {
        "id": "his_192",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "Who was the legendary king associated with the Knights of the Round Table?",
        "options": ["King Arthur", "King Alfred", "King Richard", "King Edward"],
        "correct_answer": "King Arthur",
        "difficulty": "easy"
    },
    
    # Ancient History (5 questions)
    {
        "id": "his_193",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "What ancient wonder was located in Alexandria, Egypt?",
        "options": ["Lighthouse of Alexandria", "Colossus of Rhodes", "Statue of Zeus", "Mausoleum at Halicarnassus"],
        "correct_answer": "Lighthouse of Alexandria",
        "difficulty": "hard"
    },
    {
        "id": "his_194",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "What material did ancient Egyptians use to make paper?",
        "options": ["Papyrus", "Parchment", "Vellum", "Bark"],
        "correct_answer": "Papyrus",
        "difficulty": "medium"
    },
    {
        "id": "his_195",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "Who was the first emperor of unified China?",
        "options": ["Qin Shi Huang", "Emperor Wu", "Confucius", "Sun Tzu"],
        "correct_answer": "Qin Shi Huang",
        "difficulty": "hard"
    },
    {
        "id": "his_196",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "What ancient civilization built Machu Picchu?",
        "options": ["Inca", "Aztec", "Maya", "Olmec"],
        "correct_answer": "Inca",
        "difficulty": "medium"
    },
    {
        "id": "his_197",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "What battle ended Persian invasion attempts of Greece in 490 BCE?",
        "options": ["Battle of Marathon", "Battle of Thermopylae", "Battle of Salamis", "Battle of Plataea"],
        "correct_answer": "Battle of Marathon",
        "difficulty": "hard"
    },
    
    # Modern History (4 questions)
    {
        "id": "his_198",
        "category": "History",
        "subcategory": "Modern History",
        "question": "What year did the Berlin Wall fall?",
        "options": ["1989", "1991", "1987", "1985"],
        "correct_answer": "1989",
        "difficulty": "medium"
    },
    {
        "id": "his_199",
        "category": "History",
        "subcategory": "Modern History",
        "question": "Which country was the first to grant women the right to vote in national elections?",
        "options": ["New Zealand", "United States", "United Kingdom", "Australia"],
        "correct_answer": "New Zealand",
        "difficulty": "hard"
    },
    {
        "id": "his_200",
        "category": "History",
        "subcategory": "Modern History",
        "question": "What year did the Titanic sink?",
        "options": ["1912", "1914", "1910", "1920"],
        "correct_answer": "1912",
        "difficulty": "medium"
    },
    {
        "id": "his_201",
        "category": "History",
        "subcategory": "Modern History",
        "question": "What was the first artificial satellite launched into space?",
        "options": ["Sputnik 1", "Explorer 1", "Vanguard 1", "Luna 1"],
        "correct_answer": "Sputnik 1",
        "difficulty": "medium"
    }
]

# Add the new questions to History category
data['categories']['History'].extend(new_history_questions)

# Sort History questions by ID
data['categories']['History'].sort(key=lambda x: x['id'])

# Save the updated database
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Added {len(new_history_questions)} new History questions")
print(f"New History total: {len(data['categories']['History'])} questions")

# Show breakdown by subcategory
from collections import Counter
subcats = Counter(q['subcategory'] for q in data['categories']['History'])
print("\nHistory subcategory distribution:")
for subcat, count in sorted(subcats.items(), key=lambda x: x[1], reverse=True):
    print(f"  {subcat}: {count}")

# Show difficulty distribution of new questions
difficulties = Counter(q['difficulty'] for q in new_history_questions)
print(f"\nDifficulty distribution of new questions:")
for diff, count in sorted(difficulties.items()):
    print(f"  {diff}: {count}")
