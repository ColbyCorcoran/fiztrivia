#!/usr/bin/env python3
"""
Replace final 8 duplicate Bible questions
"""

import json

with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

bible_questions = data['categories']['Bible']

# Remove 8 duplicates
ids_to_replace = ['bib_269', 'bib_272', 'bib_275', 'bib_277', 'bib_278', 'bib_282', 'bib_284', 'bib_285']
bible_questions = [q for q in bible_questions if q['id'] not in ids_to_replace]

# NEW unique replacements
replacements = [
    {"id": "bib_269", "category": "Bible", "subcategory": "Bible Trivia", "question": "What was the name of Abraham's wife?", "options": ["Sarah", "Rebecca", "Rachel", "Leah"], "correct_answer": "Sarah", "difficulty": "easy"},
    {"id": "bib_272", "category": "Bible", "subcategory": "Bible Trivia", "question": "What instrument did David play for King Saul?", "options": ["Harp", "Lyre", "Flute", "Trumpet"], "correct_answer": "Harp", "difficulty": "easy"},
    {"id": "bib_275", "category": "Bible", "subcategory": "Bible Trivia", "question": "What was the name of the garden where Jesus prayed before his arrest?", "options": ["Gethsemane", "Eden", "Bethany", "Olivet"], "correct_answer": "Gethsemane", "difficulty": "easy"},
    {"id": "bib_277", "category": "Bible", "subcategory": "Bible Trivia", "question": "Who was swallowed by a great fish?", "options": ["Jonah", "Job", "Jeremiah", "Joshua"], "correct_answer": "Jonah", "difficulty": "easy"},
    {"id": "bib_278", "category": "Bible", "subcategory": "Bible Trivia", "question": "What fell from heaven to feed the Israelites in the wilderness?", "options": ["Manna", "Quail", "Bread", "Honey"], "correct_answer": "Manna", "difficulty": "easy"},
    {"id": "bib_282", "category": "Bible", "subcategory": "Bible Languages", "question": "What does 'Rabbi' mean?", "options": ["Teacher", "Master", "Lord", "Father"], "correct_answer": "Teacher", "difficulty": "easy"},
    {"id": "bib_284", "category": "Bible", "subcategory": "Bible Languages", "question": "What does 'Alpha and Omega' mean?", "options": ["Beginning and End", "First and Last", "Creator and Judge", "All answers are correct"], "correct_answer": "All answers are correct", "difficulty": "easy"},
    {"id": "bib_285", "category": "Bible", "subcategory": "Bible Languages", "question": "What language did Jesus primarily speak?", "options": ["Aramaic", "Hebrew", "Greek", "Latin"], "correct_answer": "Aramaic", "difficulty": "medium"}
]

bible_questions.extend(replacements)
data['categories']['Bible'] = bible_questions

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✓ Replaced final 8 duplicate questions")
print(f"Bible total: {len(bible_questions)} questions")
