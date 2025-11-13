import json

# Load the current database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Find highest Sports ID
sports_ids = [q['id'] for q in data['categories']['Sports']]
sports_ids.sort()
print(f"Last Sports ID: {sports_ids[-1]}")

# New replacement Sports questions (7 total) - spt_204 to spt_210
new_sports_questions = [
    {
        "id": "spt_204",
        "category": "Sports",
        "subcategory": "Basketball",
        "question": "Which NBA team has won the most championships in league history?",
        "options": ["Boston Celtics", "Los Angeles Lakers", "Chicago Bulls", "Golden State Warriors"],
        "correct_answer": "Boston Celtics",
        "difficulty": "hard"
    },
    {
        "id": "spt_205",
        "category": "Sports",
        "subcategory": "Tennis",
        "question": "What surface is used at the US Open tennis tournament?",
        "options": ["Hard court", "Clay", "Grass", "Carpet"],
        "correct_answer": "Hard court",
        "difficulty": "medium"
    },
    {
        "id": "spt_206",
        "category": "Sports",
        "subcategory": "Soccer",
        "question": "How long is each half of a professional soccer match?",
        "options": ["45 minutes", "40 minutes", "30 minutes", "50 minutes"],
        "correct_answer": "45 minutes",
        "difficulty": "medium"
    },
    {
        "id": "spt_207",
        "category": "Sports",
        "subcategory": "Olympics",
        "question": "In which city were the first modern Olympic Games held?",
        "options": ["Athens", "Paris", "London", "Rome"],
        "correct_answer": "Athens",
        "difficulty": "hard"
    },
    {
        "id": "spt_208",
        "category": "Sports",
        "subcategory": "Hockey",
        "question": "What is the name of the trophy awarded to the NHL champions?",
        "options": ["Stanley Cup", "Conn Smythe Trophy", "Hart Memorial Trophy", "Presidents' Trophy"],
        "correct_answer": "Stanley Cup",
        "difficulty": "medium"
    },
    {
        "id": "spt_209",
        "category": "Sports",
        "subcategory": "Golf",
        "question": "What is the maximum number of clubs a golfer can carry in their bag?",
        "options": ["14", "12", "16", "18"],
        "correct_answer": "14",
        "difficulty": "hard"
    },
    {
        "id": "spt_210",
        "category": "Sports",
        "subcategory": "American Football",
        "question": "What is the line of scrimmage in American football?",
        "options": ["The imaginary line where the ball is placed", "The 50-yard line", "The goal line", "The sideline"],
        "correct_answer": "The imaginary line where the ball is placed",
        "difficulty": "medium"
    }
]

# Add the new questions
data['categories']['Sports'].extend(new_sports_questions)
data['categories']['Sports'].sort(key=lambda x: x['id'])

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Added {len(new_sports_questions)} replacement Sports questions")
print(f"New Sports total: {len(data['categories']['Sports'])} questions")
