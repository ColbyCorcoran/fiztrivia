#!/usr/bin/env python3
"""
Replace 15 duplicate Sports questions with unique ones
"""

import json

with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

sports_questions = data['categories']['Sports']

# Remove 15 duplicates
ids_to_replace = ['spt_162', 'spt_171', 'spt_193', 'spt_211', 'spt_216', 'spt_218', 'spt_220', 'spt_231', 'spt_232', 'spt_237', 'spt_241', 'spt_263', 'spt_271', 'spt_277', 'spt_281']

sports_questions = [q for q in sports_questions if q['id'] not in ids_to_replace]

# NEW unique replacements (15 questions)
replacements = [
    # Team Sports (5 replacements)
    {"id": "spt_162", "category": "Sports", "subcategory": "Team Sports", "question": "What is the line of scrimmage in football?", "options": ["The yard line where the ball is placed for the next play", "The 50-yard line", "The goal line", "The sideline"], "correct_answer": "The yard line where the ball is placed for the next play", "difficulty": "easy"},
    {"id": "spt_171", "category": "Sports", "subcategory": "Team Sports", "question": "What is the warning track in baseball?", "options": ["The dirt or gravel area before the outfield wall", "The pitcher's mound area", "The baseline", "The coach's box"], "correct_answer": "The dirt or gravel area before the outfield wall", "difficulty": "easy"},
    {"id": "spt_193", "category": "Sports", "subcategory": "Team Sports", "question": "What is a 'nutmeg' in soccer?", "options": ["Kicking the ball through an opponent's legs", "Scoring with the head", "A bicycle kick", "A corner kick"], "correct_answer": "Kicking the ball through an opponent's legs", "difficulty": "medium"},
    {"id": "spt_220", "category": "Sports", "subcategory": "Team Sports", "question": "What is a pick-six in American football?", "options": ["An interception returned for a touchdown", "A six-yard touchdown run", "A blocked field goal", "A fumble recovery"], "correct_answer": "An interception returned for a touchdown", "difficulty": "hard"},
    {"id": "spt_277", "category": "Sports", "subcategory": "Team Sports", "question": "What is a hat-trick in hockey?", "options": ["Scoring three goals in one game by one player", "Three assists in one game", "Blocking three shots", "Three penalties in one period"], "correct_answer": "Scoring three goals in one game by one player", "difficulty": "easy"},

    # Individual Sports (8 replacements)
    {"id": "spt_211", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the net height at the center in tennis?", "options": ["3 feet", "3.5 feet", "2.5 feet", "4 feet"], "correct_answer": "3 feet", "difficulty": "easy"},
    {"id": "spt_216", "category": "Sports", "subcategory": "Individual Sports", "question": "What is a tiebreaker in tennis typically played to?", "options": ["7 points", "10 points", "5 points", "15 points"], "correct_answer": "7 points", "difficulty": "easy"},
    {"id": "spt_218", "category": "Sports", "subcategory": "Individual Sports", "question": "What is a 'mulligan' in golf?", "options": ["A do-over shot (informal)", "A type of club", "A penalty stroke", "A type of putt"], "correct_answer": "A do-over shot (informal)", "difficulty": "easy"},
    {"id": "spt_231", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the 'kitchen' in pickleball?", "options": ["The non-volley zone near the net", "The service area", "The backcourt", "The sideline area"], "correct_answer": "The non-volley zone near the net", "difficulty": "medium"},
    {"id": "spt_232", "category": "Sports", "subcategory": "Individual Sports", "question": "What is a 'break point' in tennis?", "options": ["A point that if won, breaks the opponent's serve", "A rest period between sets", "A fault on serve", "A challenge to a call"], "correct_answer": "A point that if won, breaks the opponent's serve", "difficulty": "medium"},
    {"id": "spt_237", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the 'water hazard' rule in golf?", "options": ["One-stroke penalty and drop behind hazard", "Two-stroke penalty", "No penalty if found", "Replay from tee"], "correct_answer": "One-stroke penalty and drop behind hazard", "difficulty": "medium"},
    {"id": "spt_241", "category": "Sports", "subcategory": "Individual Sports", "question": "What is a 'scratch golfer'?", "options": ["A golfer with a handicap of zero", "A beginner golfer", "A professional golfer", "A golfer who plays once a year"], "correct_answer": "A golfer with a handicap of zero", "difficulty": "medium"},
    {"id": "spt_263", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the 'green jacket' tradition in golf?", "options": ["Awarded to The Masters champion", "Worn by all PGA Tour pros", "Given to hole-in-one achievers", "Worn by caddies at major tournaments"], "correct_answer": "Awarded to The Masters champion", "difficulty": "hard"},

    # International Competition (2 replacements)
    {"id": "spt_271", "category": "Sports", "subcategory": "International Competition", "question": "What do the five Olympic rings symbolize?", "options": ["Unity of five continents", "Five sports", "Five Olympic values", "Five founding nations"], "correct_answer": "Unity of five continents", "difficulty": "easy"},
    {"id": "spt_281", "category": "Sports", "subcategory": "International Competition", "question": "What is the marathon distance in kilometers?", "options": ["42.195 km", "40 km", "45 km", "50 km"], "correct_answer": "42.195 km", "difficulty": "medium"}
]

sports_questions.extend(replacements)
data['categories']['Sports'] = sports_questions

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✓ Replaced 15 duplicate questions with unique ones")
print(f"Sports total: {len(sports_questions)} questions")
