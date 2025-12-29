#!/usr/bin/env python3
"""
Replace 17 duplicate Bible questions with unique ones
"""

import json

# Load database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

bible_questions = data['categories']['Bible']

# IDs to replace (10 exact + 7 semantic/potential duplicates)
ids_to_replace = [
    'bib_267', 'bib_268', 'bib_269', 'bib_270', 'bib_271', 'bib_272', 'bib_273',
    'bib_274', 'bib_275', 'bib_277', 'bib_278', 'bib_281', 'bib_282',
    'bib_284', 'bib_285', 'bib_287', 'bib_291'
]

# Remove the duplicate questions
bible_questions = [q for q in bible_questions if q['id'] not in ids_to_replace]

# NEW REPLACEMENT QUESTIONS (completely different topics)
replacements = [
    # Bible Trivia replacements
    {"id": "bib_267", "category": "Bible", "subcategory": "Bible Trivia", "question": "What animal spoke to Balaam?", "options": ["Donkey", "Serpent", "Burning bush", "Dove"], "correct_answer": "Donkey", "difficulty": "easy"},
    {"id": "bib_268", "category": "Bible", "subcategory": "Bible Trivia", "question": "What did Jacob use as a pillow when he dreamed of a ladder to heaven?", "options": ["A stone", "A bundle of clothes", "His sandals", "Nothing"], "correct_answer": "A stone", "difficulty": "easy"},
    {"id": "bib_269", "category": "Bible", "subcategory": "Bible Trivia", "question": "How many stones did David pick up to fight Goliath?", "options": ["5", "1", "3", "7"], "correct_answer": "5", "difficulty": "easy"},
    {"id": "bib_270", "category": "Bible", "subcategory": "Bible Trivia", "question": "What bird did Noah send out first from the ark?", "options": ["Raven", "Dove", "Eagle", "Sparrow"], "correct_answer": "Raven", "difficulty": "medium"},
    {"id": "bib_271", "category": "Bible", "subcategory": "Bible Trivia", "question": "How many times did Peter deny Jesus?", "options": ["3", "2", "7", "12"], "correct_answer": "3", "difficulty": "easy"},
    {"id": "bib_272", "category": "Bible", "subcategory": "Bible Trivia", "question": "What did Jesus ride into Jerusalem on Palm Sunday?", "options": ["A donkey", "A horse", "A camel", "He walked"], "correct_answer": "A donkey", "difficulty": "easy"},
    {"id": "bib_273", "category": "Bible", "subcategory": "Bible Trivia", "question": "How many loaves and fish did Jesus use to feed the 5000?", "options": ["5 loaves and 2 fish", "2 loaves and 5 fish", "7 loaves and 7 fish", "12 loaves and 2 fish"], "correct_answer": "5 loaves and 2 fish", "difficulty": "easy"},
    {"id": "bib_274", "category": "Bible", "subcategory": "Bible Trivia", "question": "How many pieces of silver was Joseph sold for?", "options": ["20", "30", "40", "50"], "correct_answer": "20", "difficulty": "medium"},
    {"id": "bib_275", "category": "Bible", "subcategory": "Bible Trivia", "question": "What was the first miracle Jesus performed?", "options": ["Turning water into wine", "Healing the blind", "Walking on water", "Feeding 5000"], "correct_answer": "Turning water into wine", "difficulty": "easy"},
    {"id": "bib_277", "category": "Bible", "subcategory": "Bible Trivia", "question": "Who was the oldest person in the Bible?", "options": ["Methuselah", "Noah", "Adam", "Moses"], "correct_answer": "Methuselah", "difficulty": "medium"},
    {"id": "bib_278", "category": "Bible", "subcategory": "Bible Trivia", "question": "What sea did the Israelites cross to escape Egypt?", "options": ["Red Sea", "Dead Sea", "Mediterranean Sea", "Sea of Galilee"], "correct_answer": "Red Sea", "difficulty": "easy"},
    {"id": "bib_281", "category": "Bible", "subcategory": "Bible Trivia", "question": "What color was the robe placed on Jesus before his crucifixion?", "options": ["Purple", "White", "Red", "Blue"], "correct_answer": "Purple", "difficulty": "medium"},
    
    # Bible Languages replacements
    {"id": "bib_282", "category": "Bible", "subcategory": "Bible Languages", "question": "What does 'Shalom' mean?", "options": ["Peace", "Hello", "Goodbye", "Friend"], "correct_answer": "Peace", "difficulty": "easy"},
    {"id": "bib_284", "category": "Bible", "subcategory": "Bible Languages", "question": "What does 'Abba' mean?", "options": ["Father", "Son", "Spirit", "Lord"], "correct_answer": "Father", "difficulty": "easy"},
    {"id": "bib_285", "category": "Bible", "subcategory": "Bible Languages", "question": "What does 'Maranatha' mean?", "options": ["Our Lord, come!", "Blessed be God", "Holy Spirit", "Give thanks"], "correct_answer": "Our Lord, come!", "difficulty": "medium"},
    {"id": "bib_287", "category": "Bible", "subcategory": "Bible Languages", "question": "What does 'Elohim' mean?", "options": ["God", "Angel", "Prophet", "King"], "correct_answer": "God", "difficulty": "easy"},
    {"id": "bib_291", "category": "Bible", "subcategory": "Bible Languages", "question": "What does 'Beelzebub' mean?", "options": ["Lord of the flies", "Prince of darkness", "Evil one", "Deceiver"], "correct_answer": "Lord of the flies", "difficulty": "medium"}
]

# Add replacement questions
bible_questions.extend(replacements)

# Update the data
data['categories']['Bible'] = bible_questions

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✓ Replaced 17 duplicate questions with unique ones")
print(f"\nBible total: {len(bible_questions)} questions")

# Show breakdown
print("\nBreakdown by subcategory:")
subcats = {}
for q in bible_questions:
    subcat = q['subcategory']
    if subcat not in subcats:
        subcats[subcat] = 0
    subcats[subcat] += 1

for subcat in sorted(subcats.keys()):
    print(f"  {subcat}: {subcats[subcat]} questions")
