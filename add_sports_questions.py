import json

# Load the current database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# New Sports questions (spt_190 to spt_203) - 14 total
new_sports_questions = [
    # Olympics (2 questions)
    {
        "id": "spt_190",
        "category": "Sports",
        "subcategory": "Olympics",
        "question": "What five colors are the Olympic rings?",
        "options": ["Blue, yellow, black, green, red", "Blue, yellow, orange, green, red", "Blue, yellow, black, white, red", "Blue, purple, black, green, red"],
        "correct_answer": "Blue, yellow, black, green, red",
        "difficulty": "medium"
    },
    {
        "id": "spt_191",
        "category": "Sports",
        "subcategory": "Olympics",
        "question": "Which country hosted the 2008 Summer Olympics?",
        "options": ["China", "Greece", "United Kingdom", "Brazil"],
        "correct_answer": "China",
        "difficulty": "medium"
    },
    
    # Hockey (2 questions)
    {
        "id": "spt_192",
        "category": "Sports",
        "subcategory": "Hockey",
        "question": "What is it called when a player scores three goals in one game?",
        "options": ["Hat trick", "Triple", "Treble", "Three-peat"],
        "correct_answer": "Hat trick",
        "difficulty": "medium"
    },
    {
        "id": "spt_193",
        "category": "Sports",
        "subcategory": "Hockey",
        "question": "How many players from each team are on the ice during regular play?",
        "options": ["6", "5", "7", "4"],
        "correct_answer": "6",
        "difficulty": "hard"
    },
    
    # Soccer (2 questions)
    {
        "id": "spt_194",
        "category": "Sports",
        "subcategory": "Soccer",
        "question": "What is the maximum number of players on the field for one team during a match?",
        "options": ["11", "10", "12", "9"],
        "correct_answer": "11",
        "difficulty": "medium"
    },
    {
        "id": "spt_195",
        "category": "Sports",
        "subcategory": "Soccer",
        "question": "Which player has won the most FIFA Ballon d'Or awards?",
        "options": ["Lionel Messi", "Cristiano Ronaldo", "Pelé", "Diego Maradona"],
        "correct_answer": "Lionel Messi",
        "difficulty": "hard"
    },
    
    # Golf (2 questions)
    {
        "id": "spt_196",
        "category": "Sports",
        "subcategory": "Golf",
        "question": "What is the term for one stroke under par on a hole?",
        "options": ["Birdie", "Eagle", "Bogey", "Par"],
        "correct_answer": "Birdie",
        "difficulty": "medium"
    },
    {
        "id": "spt_197",
        "category": "Sports",
        "subcategory": "Golf",
        "question": "Which golf tournament is held at Augusta National?",
        "options": ["The Masters", "US Open", "The Open Championship", "PGA Championship"],
        "correct_answer": "The Masters",
        "difficulty": "hard"
    },
    
    # Tennis (2 questions)
    {
        "id": "spt_198",
        "category": "Sports",
        "subcategory": "Tennis",
        "question": "What is a score of zero called in tennis?",
        "options": ["Love", "Nil", "Zero", "Deuce"],
        "correct_answer": "Love",
        "difficulty": "easy"
    },
    {
        "id": "spt_199",
        "category": "Sports",
        "subcategory": "Tennis",
        "question": "Which female tennis player has won the most Grand Slam singles titles?",
        "options": ["Margaret Court", "Serena Williams", "Steffi Graf", "Martina Navratilova"],
        "correct_answer": "Margaret Court",
        "difficulty": "hard"
    },
    
    # Baseball (2 questions)
    {
        "id": "spt_200",
        "category": "Sports",
        "subcategory": "Baseball",
        "question": "What is it called when a batter hits the ball out of the playing field?",
        "options": ["Home run", "Grand slam", "Triple", "Fly out"],
        "correct_answer": "Home run",
        "difficulty": "easy"
    },
    {
        "id": "spt_201",
        "category": "Sports",
        "subcategory": "Baseball",
        "question": "Who holds the record for most career home runs in MLB?",
        "options": ["Barry Bonds", "Hank Aaron", "Babe Ruth", "Alex Rodriguez"],
        "correct_answer": "Barry Bonds",
        "difficulty": "hard"
    },
    
    # American Football (1 question)
    {
        "id": "spt_202",
        "category": "Sports",
        "subcategory": "American Football",
        "question": "How many points is a safety worth?",
        "options": ["2", "3", "6", "1"],
        "correct_answer": "2",
        "difficulty": "hard"
    },
    
    # Basketball (1 question)
    {
        "id": "spt_203",
        "category": "Sports",
        "subcategory": "Basketball",
        "question": "What is the maximum number of players on a basketball court for one team?",
        "options": ["5", "6", "7", "4"],
        "correct_answer": "5",
        "difficulty": "easy"
    }
]

# Add the new questions to Sports category
data['categories']['Sports'].extend(new_sports_questions)

# Sort Sports questions by ID
data['categories']['Sports'].sort(key=lambda x: x['id'])

# Save the updated database
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Added {len(new_sports_questions)} new Sports questions")
print(f"New Sports total: {len(data['categories']['Sports'])} questions")

# Show breakdown by subcategory
from collections import Counter
subcats = Counter(q['subcategory'] for q in data['categories']['Sports'])
print("\nSports subcategory distribution:")
for subcat, count in sorted(subcats.items(), key=lambda x: x[1], reverse=True):
    print(f"  {subcat}: {count}")

# Show difficulty distribution of new questions
difficulties = Counter(q['difficulty'] for q in new_sports_questions)
print(f"\nDifficulty distribution of new questions:")
for diff, count in sorted(difficulties.items()):
    print(f"  {diff}: {count}")
