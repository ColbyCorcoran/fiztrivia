import json

# Load database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# 22 unique replacement questions
# Distribution: Basketball (3), American Football (3), Baseball (3), Tennis (3),
# Soccer (3), Hockey (3), Golf (2), Olympics (2)
replacements = [
    # Basketball (3 questions)
    {
        "id": "spt_301",
        "category": "Sports",
        "subcategory": "Basketball",
        "question": "What is the shot clock time limit in the NBA?",
        "options": ["24 seconds", "30 seconds", "20 seconds", "35 seconds"],
        "correct_answer": "24 seconds",
        "difficulty": "hard"
    },
    {
        "id": "spt_302",
        "category": "Sports",
        "subcategory": "Basketball",
        "question": "Which player is known as 'His Airness'?",
        "options": ["Michael Jordan", "LeBron James", "Kobe Bryant", "Magic Johnson"],
        "correct_answer": "Michael Jordan",
        "difficulty": "medium"
    },
    {
        "id": "spt_303",
        "category": "Sports",
        "subcategory": "Basketball",
        "question": "What is a 'double-double' in basketball?",
        "options": ["Double digits in two statistical categories", "Two points scored twice", "Two players scoring 20 points", "Scoring 20 points"],
        "correct_answer": "Double digits in two statistical categories",
        "difficulty": "hard"
    },

    # American Football (3 questions)
    {
        "id": "spt_304",
        "category": "Sports",
        "subcategory": "American Football",
        "question": "What is the line of scrimmage?",
        "options": ["The imaginary line where the ball is placed", "The end zone line", "The sideline", "The 50-yard line"],
        "correct_answer": "The imaginary line where the ball is placed",
        "difficulty": "medium"
    },
    {
        "id": "spt_305",
        "category": "Sports",
        "subcategory": "American Football",
        "question": "How many downs does a team have to gain 10 yards?",
        "options": ["4", "3", "5", "6"],
        "correct_answer": "4",
        "difficulty": "easy"
    },
    {
        "id": "spt_306",
        "category": "Sports",
        "subcategory": "American Football",
        "question": "What is a 'safety' worth in points?",
        "options": ["2", "1", "3", "6"],
        "correct_answer": "2",
        "difficulty": "medium"
    },

    # Baseball (3 questions)
    {
        "id": "spt_307",
        "category": "Sports",
        "subcategory": "Baseball",
        "question": "What is a 'perfect game' in baseball?",
        "options": ["No opposing player reaches base", "A no-hitter", "Winning by 10 runs", "27 strikeouts"],
        "correct_answer": "No opposing player reaches base",
        "difficulty": "hard"
    },
    {
        "id": "spt_308",
        "category": "Sports",
        "subcategory": "Baseball",
        "question": "What is the pitching rubber distance from home plate in MLB?",
        "options": ["60 feet 6 inches", "55 feet", "65 feet", "50 feet"],
        "correct_answer": "60 feet 6 inches",
        "difficulty": "hard"
    },
    {
        "id": "spt_309",
        "category": "Sports",
        "subcategory": "Baseball",
        "question": "What is a 'ground rule double'?",
        "options": ["Ball bounces over the fence", "Hit to the warning track", "Double play", "Base hit that rolls to the wall"],
        "correct_answer": "Ball bounces over the fence",
        "difficulty": "hard"
    },

    # Tennis (3 questions)
    {
        "id": "spt_310",
        "category": "Sports",
        "subcategory": "Tennis",
        "question": "How many games must be won to win a set in tennis?",
        "options": ["6 (with 2-game advantage)", "5", "7", "8"],
        "correct_answer": "6 (with 2-game advantage)",
        "difficulty": "medium"
    },
    {
        "id": "spt_311",
        "category": "Sports",
        "subcategory": "Tennis",
        "question": "What is the term for winning all four Grand Slams in one year?",
        "options": ["Calendar Grand Slam", "Golden Slam", "Career Grand Slam", "Super Slam"],
        "correct_answer": "Calendar Grand Slam",
        "difficulty": "hard"
    },
    {
        "id": "spt_312",
        "category": "Sports",
        "subcategory": "Tennis",
        "question": "Which female player has won the most Grand Slam titles?",
        "options": ["Margaret Court", "Serena Williams", "Steffi Graf", "Martina Navratilova"],
        "correct_answer": "Margaret Court",
        "difficulty": "hard"
    },

    # Soccer (3 questions)
    {
        "id": "spt_313",
        "category": "Sports",
        "subcategory": "Soccer",
        "question": "What is the standard size of a soccer goal in feet?",
        "options": ["8 feet high by 24 feet wide", "7 feet high by 21 feet wide", "9 feet high by 27 feet wide", "10 feet high by 30 feet wide"],
        "correct_answer": "8 feet high by 24 feet wide",
        "difficulty": "hard"
    },
    {
        "id": "spt_314",
        "category": "Sports",
        "subcategory": "Soccer",
        "question": "What is stoppage time in soccer?",
        "options": ["Extra time added for delays", "Halftime break", "Penalty shootout time", "Water break"],
        "correct_answer": "Extra time added for delays",
        "difficulty": "medium"
    },
    {
        "id": "spt_315",
        "category": "Sports",
        "subcategory": "Soccer",
        "question": "What is an 'own goal'?",
        "options": ["When a player scores on their own net", "A penalty kick", "A corner kick goal", "A free kick goal"],
        "correct_answer": "When a player scores on their own net",
        "difficulty": "easy"
    },

    # Hockey (3 questions)
    {
        "id": "spt_316",
        "category": "Sports",
        "subcategory": "Hockey",
        "question": "What is icing in hockey?",
        "options": ["Shooting the puck from behind center line past goal line", "Freezing the puck", "A penalty", "Scoring three goals"],
        "correct_answer": "Shooting the puck from behind center line past goal line",
        "difficulty": "hard"
    },
    {
        "id": "spt_317",
        "category": "Sports",
        "subcategory": "Hockey",
        "question": "What is a power play in hockey?",
        "options": ["Playing with a man advantage", "A strong offensive play", "A penalty shot", "Overtime play"],
        "correct_answer": "Playing with a man advantage",
        "difficulty": "medium"
    },
    {
        "id": "spt_318",
        "category": "Sports",
        "subcategory": "Hockey",
        "question": "What is the neutral zone in hockey?",
        "options": ["Area between the two blue lines", "The crease", "Behind the goal", "The penalty box"],
        "correct_answer": "Area between the two blue lines",
        "difficulty": "hard"
    },

    # Golf (2 questions)
    {
        "id": "spt_319",
        "category": "Sports",
        "subcategory": "Golf",
        "question": "What is a 'mulligan' in golf?",
        "options": ["A second chance shot (informal)", "A type of club", "A golf course", "A score of par"],
        "correct_answer": "A second chance shot (informal)",
        "difficulty": "medium"
    },
    {
        "id": "spt_320",
        "category": "Sports",
        "subcategory": "Golf",
        "question": "What is the green in golf?",
        "options": ["The putting surface around the hole", "The fairway", "The rough", "The tee box"],
        "correct_answer": "The putting surface around the hole",
        "difficulty": "easy"
    },

    # Olympics (2 questions)
    {
        "id": "spt_321",
        "category": "Sports",
        "subcategory": "Olympics",
        "question": "What does the Olympic Torch represent?",
        "options": ["Peace and unity", "Victory", "Competition", "Excellence"],
        "correct_answer": "Peace and unity",
        "difficulty": "medium"
    },
    {
        "id": "spt_322",
        "category": "Sports",
        "subcategory": "Olympics",
        "question": "Which event includes swimming, cycling, and running?",
        "options": ["Triathlon", "Pentathlon", "Decathlon", "Heptathlon"],
        "correct_answer": "Triathlon",
        "difficulty": "easy"
    }
]

# Add replacements
data['categories']['Sports'].extend(replacements)

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ Added {len(replacements)} replacement Sports questions")
print(f"IDs: spt_301 to spt_322")
print(f"Total Sports questions: {len(data['categories']['Sports'])}")
