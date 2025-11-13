import json

# Load database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# 50 new History questions (his_251 to his_300)
# Distribution: Modern History (13), Ancient History (13), Medieval History (12), Church History (12)
# Emphasis on hard/medium difficulty

new_questions = [
    # Modern History (13 questions) - his_251-263
    {
        "id": "his_251",
        "category": "History",
        "subcategory": "Modern History",
        "question": "In what year did the Soviet Union collapse?",
        "options": ["1991", "1989", "1990", "1992"],
        "correct_answer": "1991",
        "difficulty": "medium"
    },
    {
        "id": "his_252",
        "category": "History",
        "subcategory": "Modern History",
        "question": "Which ship's sinking in 1915 helped bring the US into World War I?",
        "options": ["RMS Lusitania", "RMS Titanic", "USS Maine", "HMS Hood"],
        "correct_answer": "RMS Lusitania",
        "difficulty": "hard"
    },
    {
        "id": "his_253",
        "category": "History",
        "subcategory": "Modern History",
        "question": "What year did India gain independence from Britain?",
        "options": ["1947", "1945", "1950", "1948"],
        "correct_answer": "1947",
        "difficulty": "medium"
    },
    {
        "id": "his_254",
        "category": "History",
        "subcategory": "Modern History",
        "question": "Who was the first Chancellor of unified Germany after reunification?",
        "options": ["Helmut Kohl", "Willy Brandt", "Angela Merkel", "Gerhard Schröder"],
        "correct_answer": "Helmut Kohl",
        "difficulty": "hard"
    },
    {
        "id": "his_255",
        "category": "History",
        "subcategory": "Modern History",
        "question": "What was the name of the failed 1961 invasion of Cuba?",
        "options": ["Bay of Pigs", "Operation Mongoose", "Cuban Missile Crisis", "Operation Zapata"],
        "correct_answer": "Bay of Pigs",
        "difficulty": "medium"
    },
    {
        "id": "his_256",
        "category": "History",
        "subcategory": "Modern History",
        "question": "Which country did Iraq invade in 1990, leading to the Gulf War?",
        "options": ["Kuwait", "Iran", "Saudi Arabia", "Jordan"],
        "correct_answer": "Kuwait",
        "difficulty": "medium"
    },
    {
        "id": "his_257",
        "category": "History",
        "subcategory": "Modern History",
        "question": "What was the name of the policy of openness introduced in the Soviet Union by Gorbachev?",
        "options": ["Glasnost", "Perestroika", "Detente", "Solidarity"],
        "correct_answer": "Glasnost",
        "difficulty": "hard"
    },
    {
        "id": "his_258",
        "category": "History",
        "subcategory": "Modern History",
        "question": "Which Chinese leader initiated the Cultural Revolution?",
        "options": ["Mao Zedong", "Deng Xiaoping", "Zhou Enlai", "Jiang Zemin"],
        "correct_answer": "Mao Zedong",
        "difficulty": "medium"
    },
    {
        "id": "his_259",
        "category": "History",
        "subcategory": "Modern History",
        "question": "What year did the Rwandan genocide occur?",
        "options": ["1994", "1992", "1996", "1990"],
        "correct_answer": "1994",
        "difficulty": "hard"
    },
    {
        "id": "his_260",
        "category": "History",
        "subcategory": "Modern History",
        "question": "Who was the last Emperor of Vietnam?",
        "options": ["Bảo Đại", "Gia Long", "Minh Mạng", "Tự Đức"],
        "correct_answer": "Bảo Đại",
        "difficulty": "hard"
    },
    {
        "id": "his_261",
        "category": "History",
        "subcategory": "Modern History",
        "question": "Which treaty ended the First World War?",
        "options": ["Treaty of Versailles", "Treaty of Paris", "Treaty of Ghent", "Treaty of Westphalia"],
        "correct_answer": "Treaty of Versailles",
        "difficulty": "easy"
    },
    {
        "id": "his_262",
        "category": "History",
        "subcategory": "Modern History",
        "question": "What year did apartheid officially end in South Africa?",
        "options": ["1994", "1990", "1991", "1996"],
        "correct_answer": "1994",
        "difficulty": "medium"
    },
    {
        "id": "his_263",
        "category": "History",
        "subcategory": "Modern History",
        "question": "Which battle is considered the turning point of the American Civil War?",
        "options": ["Battle of Gettysburg", "Battle of Antietam", "Battle of Bull Run", "Battle of Shiloh"],
        "correct_answer": "Battle of Gettysburg",
        "difficulty": "medium"
    },

    # Ancient History (13 questions) - his_264-276
    {
        "id": "his_264",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "Which ancient civilization built Machu Picchu?",
        "options": ["Inca", "Maya", "Aztec", "Olmec"],
        "correct_answer": "Inca",
        "difficulty": "medium"
    },
    {
        "id": "his_265",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "What was the name of the ancient Greek city-state known for its military prowess?",
        "options": ["Sparta", "Athens", "Corinth", "Thebes"],
        "correct_answer": "Sparta",
        "difficulty": "easy"
    },
    {
        "id": "his_266",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "Which pharaoh built the Great Pyramid of Giza?",
        "options": ["Khufu", "Ramses II", "Tutankhamun", "Akhenaten"],
        "correct_answer": "Khufu",
        "difficulty": "hard"
    },
    {
        "id": "his_267",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "What was the ancient Persian religion founded by Zoroaster?",
        "options": ["Zoroastrianism", "Mithraism", "Manichaeism", "Mazd Yasna"],
        "correct_answer": "Zoroastrianism",
        "difficulty": "hard"
    },
    {
        "id": "his_268",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "Which Roman emperor split the empire into East and West?",
        "options": ["Diocletian", "Constantine", "Theodosius", "Marcus Aurelius"],
        "correct_answer": "Diocletian",
        "difficulty": "hard"
    },
    {
        "id": "his_269",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "What was the name of the Carthaginian general who crossed the Alps with elephants?",
        "options": ["Hannibal", "Scipio", "Hamilcar", "Hasdrubal"],
        "correct_answer": "Hannibal",
        "difficulty": "medium"
    },
    {
        "id": "his_270",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "Which ancient wonder was located in present-day Iraq?",
        "options": ["Hanging Gardens of Babylon", "Great Pyramid", "Temple of Artemis", "Colossus of Rhodes"],
        "correct_answer": "Hanging Gardens of Babylon",
        "difficulty": "medium"
    },
    {
        "id": "his_271",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "What was the ancient Greek competition that preceded the Olympics?",
        "options": ["Pythian Games", "Isthmian Games", "Nemean Games", "Panathenaic Games"],
        "correct_answer": "Pythian Games",
        "difficulty": "hard"
    },
    {
        "id": "his_272",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "Which Chinese dynasty is known for the Terracotta Army?",
        "options": ["Qin Dynasty", "Han Dynasty", "Tang Dynasty", "Ming Dynasty"],
        "correct_answer": "Qin Dynasty",
        "difficulty": "hard"
    },
    {
        "id": "his_273",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "What was the capital of the ancient Assyrian Empire?",
        "options": ["Nineveh", "Babylon", "Ur", "Persepolis"],
        "correct_answer": "Nineveh",
        "difficulty": "hard"
    },
    {
        "id": "his_274",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "Which ancient Greek philosopher was sentenced to death by drinking hemlock?",
        "options": ["Socrates", "Plato", "Aristotle", "Diogenes"],
        "correct_answer": "Socrates",
        "difficulty": "medium"
    },
    {
        "id": "his_275",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "What was the name of Alexander the Great's horse?",
        "options": ["Bucephalus", "Pegasus", "Incitatus", "Xanthus"],
        "correct_answer": "Bucephalus",
        "difficulty": "hard"
    },
    {
        "id": "his_276",
        "category": "History",
        "subcategory": "Ancient History",
        "question": "Which ancient library was one of the largest and most significant in the ancient world?",
        "options": ["Library of Alexandria", "Library of Pergamum", "Library of Athens", "Library of Babylon"],
        "correct_answer": "Library of Alexandria",
        "difficulty": "medium"
    },

    # Medieval History (12 questions) - his_277-288
    {
        "id": "his_277",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What year did the Battle of Hastings take place?",
        "options": ["1066", "1054", "1087", "1099"],
        "correct_answer": "1066",
        "difficulty": "medium"
    },
    {
        "id": "his_278",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "Who was the first Holy Roman Emperor?",
        "options": ["Charlemagne", "Otto I", "Frederick Barbarossa", "Henry IV"],
        "correct_answer": "Charlemagne",
        "difficulty": "hard"
    },
    {
        "id": "his_279",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "Which Muslim leader recaptured Jerusalem from the Crusaders in 1187?",
        "options": ["Saladin", "Suleiman", "Mehmed II", "Harun al-Rashid"],
        "correct_answer": "Saladin",
        "difficulty": "hard"
    },
    {
        "id": "his_280",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What was the name of the series of wars fought over the French throne?",
        "options": ["Hundred Years' War", "War of the Roses", "Thirty Years' War", "Wars of Religion"],
        "correct_answer": "Hundred Years' War",
        "difficulty": "medium"
    },
    {
        "id": "his_281",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "Which empire controlled Constantinople until 1453?",
        "options": ["Byzantine Empire", "Ottoman Empire", "Roman Empire", "Persian Empire"],
        "correct_answer": "Byzantine Empire",
        "difficulty": "medium"
    },
    {
        "id": "his_282",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What was the name of the Mongol leader who conquered most of Asia?",
        "options": ["Genghis Khan", "Kublai Khan", "Attila the Hun", "Tamerlane"],
        "correct_answer": "Genghis Khan",
        "difficulty": "easy"
    },
    {
        "id": "his_283",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "Which medieval English king signed the Magna Carta?",
        "options": ["King John", "Henry VIII", "Richard I", "Edward III"],
        "correct_answer": "King John",
        "difficulty": "medium"
    },
    {
        "id": "his_284",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What year did the Great Schism split the Christian church into East and West?",
        "options": ["1054", "1066", "1095", "1204"],
        "correct_answer": "1054",
        "difficulty": "hard"
    },
    {
        "id": "his_285",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "Who was the famous French heroine during the Hundred Years' War?",
        "options": ["Joan of Arc", "Eleanor of Aquitaine", "Blanche of Castile", "Catherine de' Medici"],
        "correct_answer": "Joan of Arc",
        "difficulty": "easy"
    },
    {
        "id": "his_286",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "Which Viking explorer is believed to have reached North America around 1000 AD?",
        "options": ["Leif Erikson", "Erik the Red", "Ragnar Lothbrok", "Harald Hardrada"],
        "correct_answer": "Leif Erikson",
        "difficulty": "hard"
    },
    {
        "id": "his_287",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "What was the pandemic that devastated Europe in the 14th century?",
        "options": ["Black Death", "Spanish Flu", "Plague of Justinian", "Antonine Plague"],
        "correct_answer": "Black Death",
        "difficulty": "easy"
    },
    {
        "id": "his_288",
        "category": "History",
        "subcategory": "Medieval History",
        "question": "Which medieval university is the oldest in the English-speaking world?",
        "options": ["University of Oxford", "University of Cambridge", "University of Paris", "University of Bologna"],
        "correct_answer": "University of Oxford",
        "difficulty": "hard"
    },

    # Church History (12 questions) - his_289-300
    {
        "id": "his_289",
        "category": "History",
        "subcategory": "Church History",
        "question": "In what year did Martin Luther post his 95 Theses?",
        "options": ["1517", "1520", "1530", "1545"],
        "correct_answer": "1517",
        "difficulty": "medium"
    },
    {
        "id": "his_290",
        "category": "History",
        "subcategory": "Church History",
        "question": "Which Roman emperor legalized Christianity in the Roman Empire?",
        "options": ["Constantine", "Theodosius", "Nero", "Diocletian"],
        "correct_answer": "Constantine",
        "difficulty": "medium"
    },
    {
        "id": "his_291",
        "category": "History",
        "subcategory": "Church History",
        "question": "What was the name of the council that addressed the Arian controversy?",
        "options": ["Council of Nicaea", "Council of Chalcedon", "Council of Trent", "Council of Constantinople"],
        "correct_answer": "Council of Nicaea",
        "difficulty": "hard"
    },
    {
        "id": "his_292",
        "category": "History",
        "subcategory": "Church History",
        "question": "Who founded the Jesuit order?",
        "options": ["Ignatius of Loyola", "Francis Xavier", "Thomas Aquinas", "Benedict of Nursia"],
        "correct_answer": "Ignatius of Loyola",
        "difficulty": "hard"
    },
    {
        "id": "his_293",
        "category": "History",
        "subcategory": "Church History",
        "question": "What was the name of the movement to reform the Catholic Church in the 16th century?",
        "options": ["Counter-Reformation", "Great Awakening", "Oxford Movement", "Iconoclasm"],
        "correct_answer": "Counter-Reformation",
        "difficulty": "hard"
    },
    {
        "id": "his_294",
        "category": "History",
        "subcategory": "Church History",
        "question": "Which English king broke from the Catholic Church to form the Church of England?",
        "options": ["Henry VIII", "Edward VI", "James I", "Charles I"],
        "correct_answer": "Henry VIII",
        "difficulty": "easy"
    },
    {
        "id": "his_295",
        "category": "History",
        "subcategory": "Church History",
        "question": "What year did the Protestant Reformation begin?",
        "options": ["1517", "1520", "1500", "1530"],
        "correct_answer": "1517",
        "difficulty": "medium"
    },
    {
        "id": "his_296",
        "category": "History",
        "subcategory": "Church History",
        "question": "Which pope called for the First Crusade?",
        "options": ["Urban II", "Gregory VII", "Innocent III", "Leo IX"],
        "correct_answer": "Urban II",
        "difficulty": "hard"
    },
    {
        "id": "his_297",
        "category": "History",
        "subcategory": "Church History",
        "question": "Who translated the Bible into English in the 14th century?",
        "options": ["John Wycliffe", "William Tyndale", "John Calvin", "John Knox"],
        "correct_answer": "John Wycliffe",
        "difficulty": "hard"
    },
    {
        "id": "his_298",
        "category": "History",
        "subcategory": "Church History",
        "question": "What was the Great Schism of 1378-1417 about?",
        "options": ["Multiple popes claiming authority", "East-West church split", "Protestant Reformation", "Crusades"],
        "correct_answer": "Multiple popes claiming authority",
        "difficulty": "hard"
    },
    {
        "id": "his_299",
        "category": "History",
        "subcategory": "Church History",
        "question": "Which reformer is known for his doctrine of predestination?",
        "options": ["John Calvin", "Martin Luther", "Huldrych Zwingli", "John Knox"],
        "correct_answer": "John Calvin",
        "difficulty": "hard"
    },
    {
        "id": "his_300",
        "category": "History",
        "subcategory": "Church History",
        "question": "What was the Edict of Nantes?",
        "options": ["Granted religious toleration to French Protestants", "Banned Protestantism in France", "Established Catholicism in England", "Called for the First Crusade"],
        "correct_answer": "Granted religious toleration to French Protestants",
        "difficulty": "hard"
    }
]

# Add new questions to History category
data['categories']['History'].extend(new_questions)

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ Added {len(new_questions)} History questions")
print(f"New range: his_251 to his_300")
print(f"\nDistribution:")
print(f"  Modern History: 13 questions")
print(f"  Ancient History: 13 questions")
print(f"  Medieval History: 12 questions")
print(f"  Church History: 12 questions")
print(f"\nTotal History questions: {len(data['categories']['History'])}")
