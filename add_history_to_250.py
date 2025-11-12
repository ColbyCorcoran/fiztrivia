import json

# Load the current database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# New History questions (his_210 to his_259) - 50 total
# Distribution: Ancient (15), Medieval (13), Church (12), Modern (10)
new_history_questions = [
    # Ancient History (15 questions)
    {
        "id": "his_210",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "Who was the first Roman Emperor?",
        "options": ["Augustus", "Julius Caesar", "Nero", "Constantine"],
        "correct_answer": "Augustus",
        "difficulty": "medium"
    },
    {
        "id": "his_211",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "What was the capital of the Aztec Empire?",
        "options": ["Tenochtitlan", "Cuzco", "Tikal", "Chichen Itza"],
        "correct_answer": "Tenochtitlan",
        "difficulty": "hard"
    },
    {
        "id": "his_212",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "Which ancient wonder was located in Babylon?",
        "options": ["Hanging Gardens", "Lighthouse", "Colossus", "Temple of Artemis"],
        "correct_answer": "Hanging Gardens",
        "difficulty": "medium"
    },
    {
        "id": "his_213",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "Who was the famous Carthaginian general who crossed the Alps?",
        "options": ["Hannibal", "Scipio", "Hamilcar", "Hasdrubal"],
        "correct_answer": "Hannibal",
        "difficulty": "medium"
    },
    {
        "id": "his_214",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "What year did Rome fall to barbarian invaders?",
        "options": ["476 AD", "410 AD", "455 AD", "500 AD"],
        "correct_answer": "476 AD",
        "difficulty": "hard"
    },
    {
        "id": "his_215",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "Who was the Greek philosopher who taught Alexander the Great?",
        "options": ["Aristotle", "Plato", "Socrates", "Pythagoras"],
        "correct_answer": "Aristotle",
        "difficulty": "medium"
    },
    {
        "id": "his_216",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "What was the ancient Egyptian writing system called?",
        "options": ["Hieroglyphics", "Cuneiform", "Sanskrit", "Linear B"],
        "correct_answer": "Hieroglyphics",
        "difficulty": "easy"
    },
    {
        "id": "his_217",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "Which river valley was home to ancient Mesopotamia?",
        "options": ["Tigris and Euphrates", "Nile", "Indus", "Yellow River"],
        "correct_answer": "Tigris and Euphrates",
        "difficulty": "medium"
    },
    {
        "id": "his_218",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "What was the name of the Athenian general who led during the Peloponnesian War?",
        "options": ["Pericles", "Themistocles", "Alcibiades", "Leonidas"],
        "correct_answer": "Pericles",
        "difficulty": "hard"
    },
    {
        "id": "his_219",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "Which Roman emperor divided the empire into East and West?",
        "options": ["Diocletian", "Constantine", "Theodosius", "Augustus"],
        "correct_answer": "Diocletian",
        "difficulty": "hard"
    },
    {
        "id": "his_220",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "What was the official language of the Roman Empire?",
        "options": ["Latin", "Greek", "Aramaic", "Hebrew"],
        "correct_answer": "Latin",
        "difficulty": "easy"
    },
    {
        "id": "his_221",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "Who was the last pharaoh of Egypt?",
        "options": ["Cleopatra VII", "Tutankhamun", "Ramses II", "Nefertiti"],
        "correct_answer": "Cleopatra VII",
        "difficulty": "medium"
    },
    {
        "id": "his_222",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "What was the largest contiguous land empire in history?",
        "options": ["Mongol Empire", "Roman Empire", "British Empire", "Persian Empire"],
        "correct_answer": "Mongol Empire",
        "difficulty": "hard"
    },
    {
        "id": "his_223",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "Which ancient civilization invented the wheel?",
        "options": ["Mesopotamians", "Egyptians", "Greeks", "Chinese"],
        "correct_answer": "Mesopotamians",
        "difficulty": "hard"
    },
    {
        "id": "his_224",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "What was the code of laws created by a Babylonian king?",
        "options": ["Code of Hammurabi", "Twelve Tables", "Justinian Code", "Napoleonic Code"],
        "correct_answer": "Code of Hammurabi",
        "difficulty": "medium"
    },
    
    # Medieval History (13 questions)
    {
        "id": "his_225",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What year did the Norman Conquest of England occur?",
        "options": ["1066", "1215", "1337", "1485"],
        "correct_answer": "1066",
        "difficulty": "medium"
    },
    {
        "id": "his_226",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "Who was the first Holy Roman Emperor?",
        "options": ["Charlemagne", "Otto I", "Frederick Barbarossa", "Charles V"],
        "correct_answer": "Charlemagne",
        "difficulty": "hard"
    },
    {
        "id": "his_227",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What was the name of the Muslim warrior who recaptured Jerusalem in 1187?",
        "options": ["Saladin", "Suleiman", "Mehmed II", "Umar"],
        "correct_answer": "Saladin",
        "difficulty": "hard"
    },
    {
        "id": "his_228",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What system governed medieval European society?",
        "options": ["Feudalism", "Democracy", "Capitalism", "Socialism"],
        "correct_answer": "Feudalism",
        "difficulty": "easy"
    },
    {
        "id": "his_229",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What was the series of wars between England and France from 1337-1453?",
        "options": ["Hundred Years' War", "War of the Roses", "Thirty Years' War", "Seven Years' War"],
        "correct_answer": "Hundred Years' War",
        "difficulty": "medium"
    },
    {
        "id": "his_230",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "Who was the famous French heroine burned at the stake?",
        "options": ["Joan of Arc", "Marie Antoinette", "Catherine de Medici", "Eleanor of Aquitaine"],
        "correct_answer": "Joan of Arc",
        "difficulty": "medium"
    },
    {
        "id": "his_231",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What empire conquered Constantinople in 1453?",
        "options": ["Ottoman Empire", "Mongol Empire", "Persian Empire", "Russian Empire"],
        "correct_answer": "Ottoman Empire",
        "difficulty": "medium"
    },
    {
        "id": "his_232",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What was the name of the Viking settlement in North America?",
        "options": ["Vinland", "Greenland", "Iceland", "Nova Scotia"],
        "correct_answer": "Vinland",
        "difficulty": "hard"
    },
    {
        "id": "his_233",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "Which king signed the Magna Carta?",
        "options": ["King John", "King Richard", "King Henry", "King Edward"],
        "correct_answer": "King John",
        "difficulty": "medium"
    },
    {
        "id": "his_234",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What was the medieval organization of craftsmen called?",
        "options": ["Guild", "Union", "Corporation", "Cartel"],
        "correct_answer": "Guild",
        "difficulty": "medium"
    },
    {
        "id": "his_235",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "Who invaded England and won the Battle of Hastings?",
        "options": ["William the Conqueror", "Harold Godwinson", "Alfred the Great", "Edward the Confessor"],
        "correct_answer": "William the Conqueror",
        "difficulty": "medium"
    },
    {
        "id": "his_236",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What was the name of the series of Christian military expeditions to the Holy Land?",
        "options": ["The Crusades", "The Inquisition", "The Reconquista", "The Jihad"],
        "correct_answer": "The Crusades",
        "difficulty": "easy"
    },
    {
        "id": "his_237",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "Which Chinese dynasty invented gunpowder?",
        "options": ["Tang Dynasty", "Han Dynasty", "Ming Dynasty", "Qing Dynasty"],
        "correct_answer": "Tang Dynasty",
        "difficulty": "hard"
    },
    
    # Church History (12 questions)
    {
        "id": "his_238",
        "category": "History",
        "subcategory": "Church History",
        "question": "What year did Martin Luther post his 95 Theses?",
        "options": ["1517", "1492", "1054", "1648"],
        "correct_answer": "1517",
        "difficulty": "hard"
    },
    {
        "id": "his_239",
        "category": "History",
        "subcategory": "Church History",
        "question": "Which council established the Nicene Creed?",
        "options": ["Council of Nicaea", "Council of Trent", "Council of Chalcedon", "Council of Constantinople"],
        "correct_answer": "Council of Nicaea",
        "difficulty": "hard"
    },
    {
        "id": "his_240",
        "category": "History",
        "subcategory": "Church History",
        "question": "Who translated the Bible into Latin?",
        "options": ["St. Jerome", "St. Augustine", "St. Thomas Aquinas", "Martin Luther"],
        "correct_answer": "St. Jerome",
        "difficulty": "hard"
    },
    {
        "id": "his_241",
        "category": "History",
        "subcategory": "Church History",
        "question": "What religious order did St. Ignatius of Loyola found?",
        "options": ["Jesuits", "Franciscans", "Dominicans", "Benedictines"],
        "correct_answer": "Jesuits",
        "difficulty": "hard"
    },
    {
        "id": "his_242",
        "category": "History",
        "subcategory": "Church History",
        "question": "What was the Council of Trent's response to?",
        "options": ["Protestant Reformation", "Great Schism", "Crusades", "Inquisition"],
        "correct_answer": "Protestant Reformation",
        "difficulty": "medium"
    },
    {
        "id": "his_243",
        "category": "History",
        "subcategory": "Church History",
        "question": "Who was the first Archbishop of Canterbury?",
        "options": ["Augustine of Canterbury", "Thomas Becket", "Anselm", "Lanfranc"],
        "correct_answer": "Augustine of Canterbury",
        "difficulty": "hard"
    },
    {
        "id": "his_244",
        "category": "History",
        "subcategory": "Church History",
        "question": "What was the religious conflict in France from 1562-1598 called?",
        "options": ["French Wars of Religion", "Thirty Years' War", "Hundred Years' War", "War of Spanish Succession"],
        "correct_answer": "French Wars of Religion",
        "difficulty": "hard"
    },
    {
        "id": "his_245",
        "category": "History",
        "subcategory": "Church History",
        "question": "Which monastic order followed the rule of St. Benedict?",
        "options": ["Benedictines", "Cistercians", "Carthusians", "All of the above"],
        "correct_answer": "All of the above",
        "difficulty": "hard"
    },
    {
        "id": "his_246",
        "category": "History",
        "subcategory": "Church History",
        "question": "What religious movement emphasized personal conversion in 18th century England?",
        "options": ["Methodism", "Puritanism", "Anglicanism", "Presbyterianism"],
        "correct_answer": "Methodism",
        "difficulty": "medium"
    },
    {
        "id": "his_247",
        "category": "History",
        "subcategory": "Church History",
        "question": "Who founded the Methodist movement?",
        "options": ["John Wesley", "George Whitefield", "Jonathan Edwards", "Charles Finney"],
        "correct_answer": "John Wesley",
        "difficulty": "medium"
    },
    {
        "id": "his_248",
        "category": "History",
        "subcategory": "Church History",
        "question": "What year did the Church of England separate from Rome?",
        "options": ["1534", "1517", "1648", "1689"],
        "correct_answer": "1534",
        "difficulty": "hard"
    },
    {
        "id": "his_249",
        "category": "History",
        "subcategory": "Church History",
        "question": "Which Roman emperor legalized Christianity in 313 AD?",
        "options": ["Constantine", "Theodosius", "Diocletian", "Nero"],
        "correct_answer": "Constantine",
        "difficulty": "medium"
    },
    
    # Modern History (10 questions)
    {
        "id": "his_250",
        "category": "History",
        "subcategory": "Modern History",
        "question": "What year did the United States declare independence?",
        "options": ["1776", "1789", "1783", "1791"],
        "correct_answer": "1776",
        "difficulty": "easy"
    },
    {
        "id": "his_251",
        "category": "History",
        "subcategory": "Modern History",
        "question": "Who was the first president of the United States?",
        "options": ["George Washington", "Thomas Jefferson", "John Adams", "Benjamin Franklin"],
        "correct_answer": "George Washington",
        "difficulty": "easy"
    },
    {
        "id": "his_252",
        "category": "History",
        "subcategory": "Modern History",
        "question": "What year did World War I begin?",
        "options": ["1914", "1917", "1939", "1941"],
        "correct_answer": "1914",
        "difficulty": "medium"
    },
    {
        "id": "his_253",
        "category": "History",
        "subcategory": "Modern History",
        "question": "Who was the British Prime Minister during most of World War II?",
        "options": ["Winston Churchill", "Neville Chamberlain", "Clement Attlee", "Anthony Eden"],
        "correct_answer": "Winston Churchill",
        "difficulty": "medium"
    },
    {
        "id": "his_254",
        "category": "History",
        "subcategory": "Modern History",
        "question": "What treaty ended World War I?",
        "options": ["Treaty of Versailles", "Treaty of Paris", "Treaty of Ghent", "Treaty of Vienna"],
        "correct_answer": "Treaty of Versailles",
        "difficulty": "medium"
    },
    {
        "id": "his_255",
        "category": "History",
        "subcategory": "Modern History",
        "question": "What year did the Soviet Union collapse?",
        "options": ["1991", "1989", "1985", "1993"],
        "correct_answer": "1991",
        "difficulty": "medium"
    },
    {
        "id": "his_256",
        "category": "History",
        "subcategory": "Modern History",
        "question": "Which country was divided by a wall from 1961 to 1989?",
        "options": ["Germany", "Korea", "Vietnam", "Cyprus"],
        "correct_answer": "Germany",
        "difficulty": "easy"
    },
    {
        "id": "his_257",
        "category": "History",
        "subcategory": "Modern History",
        "question": "What was the name of the first artificial satellite launched into space?",
        "options": ["Sputnik", "Explorer", "Vanguard", "Luna"],
        "correct_answer": "Sputnik",
        "difficulty": "medium"
    },
    {
        "id": "his_258",
        "category": "History",
        "subcategory": "Modern History",
        "question": "Who led the Indian independence movement?",
        "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Muhammad Ali Jinnah", "Subhas Chandra Bose"],
        "correct_answer": "Mahatma Gandhi",
        "difficulty": "medium"
    },
    {
        "id": "his_259",
        "category": "History",
        "subcategory": "Modern History",
        "question": "What year did the French Revolution begin?",
        "options": ["1789", "1776", "1799", "1804"],
        "correct_answer": "1789",
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
