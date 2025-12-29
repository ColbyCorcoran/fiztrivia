#!/usr/bin/env python3
"""
Replace last 5 duplicate Bible questions with very specific, unique ones
"""

import json

with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

bible_questions = data['categories']['Bible']

# Remove last 5 duplicates
ids_to_replace = ['bib_269', 'bib_272', 'bib_275', 'bib_277', 'bib_285']
bible_questions = [q for q in bible_questions if q['id'] not in ids_to_replace]

# VERY SPECIFIC unique replacements
replacements = [
    {"id": "bib_269", "category": "Bible", "subcategory": "Bible Trivia", "question": "What was the name of the cupbearer who became governor of Judah?", "options": ["Nehemiah", "Ezra", "Zerubbabel", "Haggai"], "correct_answer": "Nehemiah", "difficulty": "medium"},
    {"id": "bib_272", "category": "Bible", "subcategory": "Bible Trivia", "question": "What was the name of Ruth's mother-in-law?", "options": ["Naomi", "Orpah", "Hannah", "Deborah"], "correct_answer": "Naomi", "difficulty": "easy"},
    {"id": "bib_275", "category": "Bible", "subcategory": "Bible Trivia", "question": "Which apostle was a tax collector before following Jesus?", "options": ["Matthew", "Luke", "John", "Thomas"], "correct_answer": "Matthew", "difficulty": "easy"},
    {"id": "bib_277", "category": "Bible", "subcategory": "Bible Trivia", "question": "What was the name of the prophetess who recognized baby Jesus at the temple?", "options": ["Anna", "Mary", "Elizabeth", "Deborah"], "correct_answer": "Anna", "difficulty": "medium"},
    {"id": "bib_285", "category": "Bible", "subcategory": "Bible Languages", "question": "What does 'Immanuel' mean?", "options": ["God with us", "God is good", "The Anointed One", "Prince of Peace"], "correct_answer": "God with us", "difficulty": "easy"}
]

bible_questions.extend(replacements)
data['categories']['Bible'] = bible_questions

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✓ Replaced last 5 duplicate questions")
print(f"Bible total: {len(bible_questions)} questions")
