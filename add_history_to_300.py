#!/usr/bin/env python3
"""
Add 32 History questions to reach 300 total
Prioritize Church History and Medieval History (smallest subcategories)
Emphasize easy and hard questions (medium already balanced)
"""

import json

def add_history_questions():
    # Load current database
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    history_questions = data['categories']['History']
    
    print(f"Current History questions: {len(history_questions)}")
    print(f"Adding 32 questions (his_269 to his_300)")
    print()
    print("Distribution strategy:")
    print("  Church History: +19 (56 → 75)")
    print("  Medieval History: +13 (61 → 74)")
    print()
    print("Difficulty emphasis:")
    print("  Easy: +23 (need more easy questions)")
    print("  Hard: +9 (need more hard questions)")
    print()

    # NEW UNIQUE QUESTIONS
    new_questions = [
        # CHURCH HISTORY (19 questions: 10 easy, 0 medium, 9 hard)
        # Easy (10)
        {
            "id": "his_269",
            "category": "History",
            "subcategory": "Church History",
            "question": "Who is considered the first pope of the Catholic Church?",
            "options": ["Saint Peter", "Saint Paul", "Saint John", "Saint James"],
            "correct_answer": "Saint Peter",
            "difficulty": "easy"
        },
        {
            "id": "his_270",
            "category": "History",
            "subcategory": "Church History",
            "question": "In what year did the Protestant Reformation begin?",
            "options": ["1517", "1492", "1618", "1453"],
            "correct_answer": "1517",
            "difficulty": "easy"
        },
        {
            "id": "his_271",
            "category": "History",
            "subcategory": "Church History",
            "question": "Who wrote the 95 Theses?",
            "options": ["Martin Luther", "John Calvin", "John Knox", "Huldrych Zwingli"],
            "correct_answer": "Martin Luther",
            "difficulty": "easy"
        },
        {
            "id": "his_272",
            "category": "History",
            "subcategory": "Church History",
            "question": "What is the name of the Christian holiday celebrating the resurrection of Jesus?",
            "options": ["Easter", "Christmas", "Pentecost", "Epiphany"],
            "correct_answer": "Easter",
            "difficulty": "easy"
        },
        {
            "id": "his_273",
            "category": "History",
            "subcategory": "Church History",
            "question": "Which council established the Nicene Creed in 325 AD?",
            "options": ["Council of Nicaea", "Council of Trent", "Council of Chalcedon", "Council of Constantinople"],
            "correct_answer": "Council of Nicaea",
            "difficulty": "easy"
        },
        {
            "id": "his_274",
            "category": "History",
            "subcategory": "Church History",
            "question": "Who founded the Methodist movement in the 18th century?",
            "options": ["John Wesley", "Charles Spurgeon", "George Whitefield", "Jonathan Edwards"],
            "correct_answer": "John Wesley",
            "difficulty": "easy"
        },
        {
            "id": "his_275",
            "category": "History",
            "subcategory": "Church History",
            "question": "What term describes the split between the Eastern Orthodox and Roman Catholic churches in 1054?",
            "options": ["The Great Schism", "The Reformation", "The Inquisition", "The Crusades"],
            "correct_answer": "The Great Schism",
            "difficulty": "easy"
        },
        {
            "id": "his_276",
            "category": "History",
            "subcategory": "Church History",
            "question": "Who translated the Bible into English in the 1380s?",
            "options": ["John Wycliffe", "William Tyndale", "John Calvin", "Martin Luther"],
            "correct_answer": "John Wycliffe",
            "difficulty": "easy"
        },
        {
            "id": "his_277",
            "category": "History",
            "subcategory": "Church History",
            "question": "What religious order did Saint Francis of Assisi found?",
            "options": ["Franciscans", "Dominicans", "Jesuits", "Benedictines"],
            "correct_answer": "Franciscans",
            "difficulty": "easy"
        },
        {
            "id": "his_278",
            "category": "History",
            "subcategory": "Church History",
            "question": "Which Roman emperor made Christianity legal in 313 AD?",
            "options": ["Constantine", "Nero", "Augustus", "Diocletian"],
            "correct_answer": "Constantine",
            "difficulty": "easy"
        },
        # Hard (9)
        {
            "id": "his_279",
            "category": "History",
            "subcategory": "Church History",
            "question": "What 1648 treaty ended the Thirty Years' War and recognized religious diversity in Europe?",
            "options": ["Peace of Westphalia", "Treaty of Versailles", "Edict of Nantes", "Peace of Augsburg"],
            "correct_answer": "Peace of Westphalia",
            "difficulty": "hard"
        },
        {
            "id": "his_280",
            "category": "History",
            "subcategory": "Church History",
            "question": "Who was the founder of the Jesuit order in 1540?",
            "options": ["Ignatius of Loyola", "Francis Xavier", "Thomas Aquinas", "Augustine of Hippo"],
            "correct_answer": "Ignatius of Loyola",
            "difficulty": "hard"
        },
        {
            "id": "his_281",
            "category": "History",
            "subcategory": "Church History",
            "question": "What heresy, claiming Jesus was not divine, was condemned at the Council of Nicaea?",
            "options": ["Arianism", "Gnosticism", "Pelagianism", "Nestorianism"],
            "correct_answer": "Arianism",
            "difficulty": "hard"
        },
        {
            "id": "his_282",
            "category": "History",
            "subcategory": "Church History",
            "question": "Which pope initiated the First Crusade in 1095?",
            "options": ["Pope Urban II", "Pope Gregory VII", "Pope Innocent III", "Pope Leo IX"],
            "correct_answer": "Pope Urban II",
            "difficulty": "hard"
        },
        {
            "id": "his_283",
            "category": "History",
            "subcategory": "Church History",
            "question": "What 1555 agreement allowed German princes to choose Lutheranism or Catholicism for their territories?",
            "options": ["Peace of Augsburg", "Edict of Worms", "Diet of Speyer", "Treaty of Westphalia"],
            "correct_answer": "Peace of Augsburg",
            "difficulty": "hard"
        },
        {
            "id": "his_284",
            "category": "History",
            "subcategory": "Church History",
            "question": "Who was the influential theologian who wrote 'City of God' in the 5th century?",
            "options": ["Augustine of Hippo", "Thomas Aquinas", "Jerome", "Ambrose"],
            "correct_answer": "Augustine of Hippo",
            "difficulty": "hard"
        },
        {
            "id": "his_285",
            "category": "History",
            "subcategory": "Church History",
            "question": "What was the name of the papal decree that excommunicated Martin Luther in 1521?",
            "options": ["Decet Romanum Pontificem", "Exsurge Domine", "Unam Sanctam", "Clericis Laicos"],
            "correct_answer": "Decet Romanum Pontificem",
            "difficulty": "hard"
        },
        {
            "id": "his_286",
            "category": "History",
            "subcategory": "Church History",
            "question": "Which monastic order follows the Rule of Saint Benedict?",
            "options": ["Benedictines", "Cistercians", "Carthusians", "All of the above"],
            "correct_answer": "All of the above",
            "difficulty": "hard"
        },
        {
            "id": "his_287",
            "category": "History",
            "subcategory": "Church History",
            "question": "What 16th-century council reformed Catholic doctrine in response to the Reformation?",
            "options": ["Council of Trent", "Second Vatican Council", "Council of Constance", "Council of Basel"],
            "correct_answer": "Council of Trent",
            "difficulty": "hard"
        },

        # MEDIEVAL HISTORY (13 questions: all easy)
        {
            "id": "his_288",
            "category": "History",
            "subcategory": "Medieval History",
            "question": "What were the heavily armored soldiers of medieval Europe called?",
            "options": ["Knights", "Samurai", "Legionaries", "Hoplites"],
            "correct_answer": "Knights",
            "difficulty": "easy"
        },
        {
            "id": "his_289",
            "category": "History",
            "subcategory": "Medieval History",
            "question": "What was the feudal system based on?",
            "options": ["Land ownership and loyalty", "Money and trade", "Democratic voting", "Religious authority"],
            "correct_answer": "Land ownership and loyalty",
            "difficulty": "easy"
        },
        {
            "id": "his_290",
            "category": "History",
            "subcategory": "Medieval History",
            "question": "What was a castle's defensive ditch filled with water called?",
            "options": ["Moat", "Trench", "Canal", "Aqueduct"],
            "correct_answer": "Moat",
            "difficulty": "easy"
        },
        {
            "id": "his_291",
            "category": "History",
            "subcategory": "Medieval History",
            "question": "Who led the Norman conquest of England in 1066?",
            "options": ["William the Conqueror", "Richard the Lionheart", "Alfred the Great", "Charlemagne"],
            "correct_answer": "William the Conqueror",
            "difficulty": "easy"
        },
        {
            "id": "his_292",
            "category": "History",
            "subcategory": "Medieval History",
            "question": "What was the Black Death?",
            "options": ["A devastating plague", "A military campaign", "A religious movement", "A famine"],
            "correct_answer": "A devastating plague",
            "difficulty": "easy"
        },
        {
            "id": "his_293",
            "category": "History",
            "subcategory": "Medieval History",
            "question": "What famous document did King John sign in 1215, limiting royal power?",
            "options": ["Magna Carta", "Bill of Rights", "Declaration of Independence", "Petition of Right"],
            "correct_answer": "Magna Carta",
            "difficulty": "easy"
        },
        {
            "id": "his_294",
            "category": "History",
            "subcategory": "Medieval History",
            "question": "What were the religious military campaigns to reclaim the Holy Land called?",
            "options": ["Crusades", "Jihads", "Inquisitions", "Pilgrimages"],
            "correct_answer": "Crusades",
            "difficulty": "easy"
        },
        {
            "id": "his_295",
            "category": "History",
            "subcategory": "Medieval History",
            "question": "Who was the famous French heroine who led troops during the Hundred Years' War?",
            "options": ["Joan of Arc", "Eleanor of Aquitaine", "Catherine de' Medici", "Marie Antoinette"],
            "correct_answer": "Joan of Arc",
            "difficulty": "easy"
        },
        {
            "id": "his_296",
            "category": "History",
            "subcategory": "Medieval History",
            "question": "What empire did Charlemagne rule in the 9th century?",
            "options": ["Holy Roman Empire", "Byzantine Empire", "Ottoman Empire", "Mongol Empire"],
            "correct_answer": "Holy Roman Empire",
            "difficulty": "easy"
        },
        {
            "id": "his_297",
            "category": "History",
            "subcategory": "Medieval History",
            "question": "What title was given to a feudal lord's land?",
            "options": ["Manor", "Borough", "County", "Province"],
            "correct_answer": "Manor",
            "difficulty": "easy"
        },
        {
            "id": "his_298",
            "category": "History",
            "subcategory": "Medieval History",
            "question": "What were medieval trade associations of craftsmen called?",
            "options": ["Guilds", "Unions", "Cartels", "Cooperatives"],
            "correct_answer": "Guilds",
            "difficulty": "easy"
        },
        {
            "id": "his_299",
            "category": "History",
            "subcategory": "Medieval History",
            "question": "What was the name of the conflict between England and France from 1337-1453?",
            "options": ["Hundred Years' War", "War of the Roses", "Thirty Years' War", "Seven Years' War"],
            "correct_answer": "Hundred Years' War",
            "difficulty": "easy"
        },
        {
            "id": "his_300",
            "category": "History",
            "subcategory": "Medieval History",
            "question": "What were the Viking warriors who raided Europe called?",
            "options": ["Norsemen", "Goths", "Vandals", "Huns"],
            "correct_answer": "Norsemen",
            "difficulty": "easy"
        }
    ]

    # Add new questions
    history_questions.extend(new_questions)

    # Save updated database
    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✓ Added 32 new History questions")
    print(f"\nNew History total: {len(history_questions)} questions")

    # Show breakdown
    print("\nBreakdown by subcategory:")
    subcats = {}
    for q in history_questions:
        subcat = q['subcategory']
        if subcat not in subcats:
            subcats[subcat] = 0
        subcats[subcat] += 1

    for subcat in sorted(subcats.keys()):
        print(f"  {subcat}: {subcats[subcat]} questions")

    # Show difficulty breakdown
    print("\nBreakdown by difficulty:")
    diffs = {'easy': 0, 'medium': 0, 'hard': 0}
    for q in history_questions:
        diffs[q['difficulty']] += 1

    for diff in ['easy', 'medium', 'hard']:
        pct = (diffs[diff] / len(history_questions)) * 100
        print(f"  {diff.capitalize()}: {diffs[diff]} ({pct:.1f}%)")

    print("\n✓ History category complete: 300/300 questions")

if __name__ == "__main__":
    add_history_questions()
