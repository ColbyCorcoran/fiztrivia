#!/usr/bin/env python3
"""
Replace the 11 duplicate History questions with unique ones
"""

import json

def fix_duplicates():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    history_questions = data['categories']['History']

    # IDs to replace
    ids_to_replace = [
        'his_270', 'his_271', 'his_273', 'his_274', 'his_277',
        'his_280', 'his_286', 'his_291', 'his_293', 'his_296', 'his_299'
    ]

    # Remove the duplicate questions
    history_questions = [q for q in history_questions if q['id'] not in ids_to_replace]

    # NEW REPLACEMENT QUESTIONS (completely different topics)
    replacements = [
        # Church History replacements
        {
            "id": "his_270",
            "category": "History",
            "subcategory": "Church History",
            "question": "What religious movement emphasized adult baptism and began in the 16th century?",
            "options": ["Anabaptism", "Presbyterianism", "Lutheranism", "Anglicanism"],
            "correct_answer": "Anabaptism",
            "difficulty": "easy"
        },
        {
            "id": "his_271",
            "category": "History",
            "subcategory": "Church History",
            "question": "Which missionary is known as the 'Apostle to the Gentiles'?",
            "options": ["Paul", "Peter", "John", "James"],
            "correct_answer": "Paul",
            "difficulty": "easy"
        },
        {
            "id": "his_273",
            "category": "History",
            "subcategory": "Church History",
            "question": "What was the Great Awakening?",
            "options": ["A religious revival in America", "A church council", "A papal decree", "A monastic reform"],
            "correct_answer": "A religious revival in America",
            "difficulty": "easy"
        },
        {
            "id": "his_274",
            "category": "History",
            "subcategory": "Church History",
            "question": "What is the name of the first English Bible translation by William Tyndale?",
            "options": ["Tyndale Bible", "King James Bible", "Geneva Bible", "Wycliffe Bible"],
            "correct_answer": "Tyndale Bible",
            "difficulty": "easy"
        },
        {
            "id": "his_277",
            "category": "History",
            "subcategory": "Church History",
            "question": "Which denomination emerged from the teachings of John Calvin?",
            "options": ["Reformed/Presbyterian", "Baptist", "Methodist", "Anglican"],
            "correct_answer": "Reformed/Presbyterian",
            "difficulty": "easy"
        },
        {
            "id": "his_280",
            "category": "History",
            "subcategory": "Church History",
            "question": "What was the Spanish Inquisition primarily concerned with?",
            "options": ["Enforcing Catholic orthodoxy", "Converting Muslims", "Witch trials", "Crusades"],
            "correct_answer": "Enforcing Catholic orthodoxy",
            "difficulty": "hard"
        },
        {
            "id": "his_286",
            "category": "History",
            "subcategory": "Church History",
            "question": "What heretical movement believed in two gods, one good and one evil?",
            "options": ["Manichaeism", "Arianism", "Pelagianism", "Montanism"],
            "correct_answer": "Manichaeism",
            "difficulty": "hard"
        },
        
        # Medieval History replacements
        {
            "id": "his_291",
            "category": "History",
            "subcategory": "Medieval History",
            "question": "What was the primary weapon used by English longbowmen in medieval warfare?",
            "options": ["Longbow", "Crossbow", "Pike", "Halberd"],
            "correct_answer": "Longbow",
            "difficulty": "easy"
        },
        {
            "id": "his_293",
            "category": "History",
            "subcategory": "Medieval History",
            "question": "What was the system of agricultural labor in medieval Europe where peasants worked land for a lord?",
            "options": ["Serfdom", "Slavery", "Tenancy", "Sharecropping"],
            "correct_answer": "Serfdom",
            "difficulty": "easy"
        },
        {
            "id": "his_296",
            "category": "History",
            "subcategory": "Medieval History",
            "question": "What was the fortified central tower of a castle called?",
            "options": ["Keep", "Bailey", "Barbican", "Gatehouse"],
            "correct_answer": "Keep",
            "difficulty": "easy"
        },
        {
            "id": "his_299",
            "category": "History",
            "subcategory": "Medieval History",
            "question": "What medieval weapon consisted of a spiked ball on a chain?",
            "options": ["Flail", "Mace", "Morning star", "Halberd"],
            "correct_answer": "Flail",
            "difficulty": "easy"
        }
    ]

    # Add replacement questions
    history_questions.extend(replacements)

    # Update the data
    data['categories']['History'] = history_questions

    # Save updated database
    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("✓ Replaced 11 duplicate questions with unique ones")
    print(f"\nHistory total: {len(history_questions)} questions")
    
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

if __name__ == "__main__":
    fix_duplicates()
