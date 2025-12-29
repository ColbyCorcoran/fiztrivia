#!/usr/bin/env python3
import json

with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

bible_questions = data['categories']['Bible']
bible_questions = [q for q in bible_questions if q['id'] not in ['bib_272', 'bib_285']]

replacements = [
    {"id": "bib_272", "category": "Bible", "subcategory": "Bible Trivia", "question": "Who was the first king of Israel?", "options": ["Saul", "David", "Solomon", "Samuel"], "correct_answer": "Saul", "difficulty": "easy"},
    {"id": "bib_285", "category": "Bible", "subcategory": "Bible Languages", "question": "What does 'Paraclete' mean?", "options": ["Helper/Comforter", "Savior", "Teacher", "Prophet"], "correct_answer": "Helper/Comforter", "difficulty": "medium"}
]

bible_questions.extend(replacements)
data['categories']['Bible'] = bible_questions

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✓ Final replacements complete")
print(f"Bible total: {len(bible_questions)} questions")
