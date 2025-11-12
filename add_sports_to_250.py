import json

# Load the current database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# New Sports questions (spt_211 to spt_260) - 50 total
new_sports_questions = [
    # Soccer (7 questions)
    {
        "id": "spt_211",
        "category": "Sports",
        "subcategory": "Soccer",
        "question": "What country has won the most FIFA World Cups?",
        "options": ["Brazil", "Germany", "Italy", "Argentina"],
        "correct_answer": "Brazil",
        "difficulty": "medium"
    },
    {
        "id": "spt_212",
        "category": "Sports",
        "subcategory": "Soccer",
        "question": "What is a yellow card used for in soccer?",
        "options": ["Caution/warning", "Ejection", "Goal celebration", "Substitution"],
        "correct_answer": "Caution/warning",
        "difficulty": "easy"
    },
    {
        "id": "spt_213",
        "category": "Sports",
        "subcategory": "Soccer",
        "question": "What is it called when a player scores three goals in one game?",
        "options": ["Hat trick", "Triple", "Grand slam", "Perfect game"],
        "correct_answer": "Hat trick",
        "difficulty": "easy"
    },
    {
        "id": "spt_214",
        "category": "Sports",
        "subcategory": "Soccer",
        "question": "Which English club has won the most Premier League titles?",
        "options": ["Manchester United", "Liverpool", "Arsenal", "Chelsea"],
        "correct_answer": "Manchester United",
        "difficulty": "hard"
    },
    {
        "id": "spt_215",
        "category": "Sports",
        "subcategory": "Soccer",
        "question": "What is the maximum time for a professional soccer match including stoppage time?",
        "options": ["90+ minutes", "80 minutes", "100 minutes", "120 minutes"],
        "correct_answer": "90+ minutes",
        "difficulty": "medium"
    },
    {
        "id": "spt_216",
        "category": "Sports",
        "subcategory": "Soccer",
        "question": "What is the name of the position that defends the goal?",
        "options": ["Goalkeeper", "Defender", "Sweeper", "Fullback"],
        "correct_answer": "Goalkeeper",
        "difficulty": "easy"
    },
    {
        "id": "spt_217",
        "category": "Sports",
        "subcategory": "Soccer",
        "question": "Which country hosted the 2014 FIFA World Cup?",
        "options": ["Brazil", "South Africa", "Russia", "Germany"],
        "correct_answer": "Brazil",
        "difficulty": "medium"
    },
    
    # Hockey (7 questions)
    {
        "id": "spt_218",
        "category": "Sports",
        "subcategory": "Hockey",
        "question": "How many periods are in a standard NHL game?",
        "options": ["3", "2", "4", "5"],
        "correct_answer": "3",
        "difficulty": "medium"
    },
    {
        "id": "spt_219",
        "category": "Sports",
        "subcategory": "Hockey",
        "question": "What is the puck made of?",
        "options": ["Vulcanized rubber", "Plastic", "Wood", "Metal"],
        "correct_answer": "Vulcanized rubber",
        "difficulty": "hard"
    },
    {
        "id": "spt_220",
        "category": "Sports",
        "subcategory": "Hockey",
        "question": "What country is considered the birthplace of ice hockey?",
        "options": ["Canada", "United States", "Russia", "Sweden"],
        "correct_answer": "Canada",
        "difficulty": "medium"
    },
    {
        "id": "spt_221",
        "category": "Sports",
        "subcategory": "Hockey",
        "question": "What is it called when a team has more players on the ice due to a penalty?",
        "options": ["Power play", "Penalty kill", "Advantage", "Man-up"],
        "correct_answer": "Power play",
        "difficulty": "medium"
    },
    {
        "id": "spt_222",
        "category": "Sports",
        "subcategory": "Hockey",
        "question": "Who holds the NHL record for most career goals?",
        "options": ["Wayne Gretzky", "Gordie Howe", "Mario Lemieux", "Bobby Orr"],
        "correct_answer": "Wayne Gretzky",
        "difficulty": "hard"
    },
    {
        "id": "spt_223",
        "category": "Sports",
        "subcategory": "Hockey",
        "question": "How long is each period in a standard NHL game?",
        "options": ["20 minutes", "15 minutes", "25 minutes", "30 minutes"],
        "correct_answer": "20 minutes",
        "difficulty": "medium"
    },
    {
        "id": "spt_224",
        "category": "Sports",
        "subcategory": "Hockey",
        "question": "What line divides the ice into two halves?",
        "options": ["Center red line", "Blue line", "Goal line", "Faceoff line"],
        "correct_answer": "Center red line",
        "difficulty": "medium"
    },
    
    # Olympics (7 questions)
    {
        "id": "spt_225",
        "category": "Sports",
        "subcategory": "Olympics",
        "question": "Where were the first modern Olympics held?",
        "options": ["Athens, Greece", "Paris, France", "London, England", "Rome, Italy"],
        "correct_answer": "Athens, Greece",
        "difficulty": "medium"
    },
    {
        "id": "spt_226",
        "category": "Sports",
        "subcategory": "Olympics",
        "question": "What year were the first modern Olympics?",
        "options": ["1896", "1900", "1880", "1912"],
        "correct_answer": "1896",
        "difficulty": "hard"
    },
    {
        "id": "spt_227",
        "category": "Sports",
        "subcategory": "Olympics",
        "question": "How often are the Summer Olympics held?",
        "options": ["Every 4 years", "Every 2 years", "Every 5 years", "Annually"],
        "correct_answer": "Every 4 years",
        "difficulty": "easy"
    },
    {
        "id": "spt_228",
        "category": "Sports",
        "subcategory": "Olympics",
        "question": "Who is the most decorated Olympian of all time?",
        "options": ["Michael Phelps", "Usain Bolt", "Simone Biles", "Larisa Latynina"],
        "correct_answer": "Michael Phelps",
        "difficulty": "medium"
    },
    {
        "id": "spt_229",
        "category": "Sports",
        "subcategory": "Olympics",
        "question": "What do the five Olympic rings represent?",
        "options": ["Five continents", "Five sports", "Five countries", "Five values"],
        "correct_answer": "Five continents",
        "difficulty": "medium"
    },
    {
        "id": "spt_230",
        "category": "Sports",
        "subcategory": "Olympics",
        "question": "What metal is the Olympic gold medal mostly made of?",
        "options": ["Silver", "Gold", "Bronze", "Platinum"],
        "correct_answer": "Silver",
        "difficulty": "hard"
    },
    {
        "id": "spt_231",
        "category": "Sports",
        "subcategory": "Olympics",
        "question": "Which city has hosted the Summer Olympics three times?",
        "options": ["London", "Paris", "Los Angeles", "Athens"],
        "correct_answer": "London",
        "difficulty": "hard"
    },
    
    # Golf (6 questions)
    {
        "id": "spt_232",
        "category": "Sports",
        "subcategory": "Golf",
        "question": "What is par for a standard 18-hole golf course?",
        "options": ["72", "70", "68", "74"],
        "correct_answer": "72",
        "difficulty": "medium"
    },
    {
        "id": "spt_233",
        "category": "Sports",
        "subcategory": "Golf",
        "question": "What is two strokes under par on a hole called?",
        "options": ["Eagle", "Birdie", "Albatross", "Bogey"],
        "correct_answer": "Eagle",
        "difficulty": "medium"
    },
    {
        "id": "spt_234",
        "category": "Sports",
        "subcategory": "Golf",
        "question": "What are the four major golf tournaments called?",
        "options": ["The Majors", "The Grand Slam", "The Championship Tour", "The Elite Four"],
        "correct_answer": "The Majors",
        "difficulty": "medium"
    },
    {
        "id": "spt_235",
        "category": "Sports",
        "subcategory": "Golf",
        "question": "What is a hole-in-one also called?",
        "options": ["Ace", "Perfect shot", "Eagle", "Albatross"],
        "correct_answer": "Ace",
        "difficulty": "medium"
    },
    {
        "id": "spt_236",
        "category": "Sports",
        "subcategory": "Golf",
        "question": "Who has won the most major golf championships?",
        "options": ["Jack Nicklaus", "Tiger Woods", "Arnold Palmer", "Gary Player"],
        "correct_answer": "Jack Nicklaus",
        "difficulty": "hard"
    },
    {
        "id": "spt_237",
        "category": "Sports",
        "subcategory": "Golf",
        "question": "What is one stroke over par called?",
        "options": ["Bogey", "Birdie", "Par", "Double bogey"],
        "correct_answer": "Bogey",
        "difficulty": "easy"
    },
    
    # Tennis (6 questions)
    {
        "id": "spt_238",
        "category": "Sports",
        "subcategory": "Tennis",
        "question": "How many Grand Slam tournaments are there in tennis?",
        "options": ["4", "3", "5", "6"],
        "correct_answer": "4",
        "difficulty": "easy"
    },
    {
        "id": "spt_239",
        "category": "Sports",
        "subcategory": "Tennis",
        "question": "What surface is Wimbledon played on?",
        "options": ["Grass", "Clay", "Hard court", "Carpet"],
        "correct_answer": "Grass",
        "difficulty": "medium"
    },
    {
        "id": "spt_240",
        "category": "Sports",
        "subcategory": "Tennis",
        "question": "What is the scoring sequence in a tennis game?",
        "options": ["Love, 15, 30, 40, Game", "0, 1, 2, 3, Game", "Love, 10, 20, 30, Game", "0, 5, 10, 15, Game"],
        "correct_answer": "Love, 15, 30, 40, Game",
        "difficulty": "medium"
    },
    {
        "id": "spt_241",
        "category": "Sports",
        "subcategory": "Tennis",
        "question": "What is it called when the score is tied at 40-40?",
        "options": ["Deuce", "Tie", "Match point", "Set point"],
        "correct_answer": "Deuce",
        "difficulty": "medium"
    },
    {
        "id": "spt_242",
        "category": "Sports",
        "subcategory": "Tennis",
        "question": "How many sets must a player win to win a men's Grand Slam match?",
        "options": ["3 out of 5", "2 out of 3", "4 out of 7", "2 out of 5"],
        "correct_answer": "3 out of 5",
        "difficulty": "hard"
    },
    {
        "id": "spt_243",
        "category": "Sports",
        "subcategory": "Tennis",
        "question": "What is the French Open played on?",
        "options": ["Clay", "Grass", "Hard court", "Carpet"],
        "correct_answer": "Clay",
        "difficulty": "medium"
    },
    
    # Baseball (6 questions)
    {
        "id": "spt_244",
        "category": "Sports",
        "subcategory": "Baseball",
        "question": "How many strikes result in an out?",
        "options": ["3", "4", "2", "5"],
        "correct_answer": "3",
        "difficulty": "easy"
    },
    {
        "id": "spt_245",
        "category": "Sports",
        "subcategory": "Baseball",
        "question": "What is the World Series?",
        "options": ["MLB championship", "All-Star game", "Spring training", "Draft event"],
        "correct_answer": "MLB championship",
        "difficulty": "easy"
    },
    {
        "id": "spt_246",
        "category": "Sports",
        "subcategory": "Baseball",
        "question": "How many bases are on a baseball diamond?",
        "options": ["4", "3", "5", "6"],
        "correct_answer": "4",
        "difficulty": "easy"
    },
    {
        "id": "spt_247",
        "category": "Sports",
        "subcategory": "Baseball",
        "question": "What is a perfect game in baseball?",
        "options": ["No hits, walks, or errors", "No runs allowed", "All strikeouts", "27 outs in a row"],
        "correct_answer": "No hits, walks, or errors",
        "difficulty": "hard"
    },
    {
        "id": "spt_248",
        "category": "Sports",
        "subcategory": "Baseball",
        "question": "Which team has won the most World Series?",
        "options": ["New York Yankees", "Boston Red Sox", "St. Louis Cardinals", "Los Angeles Dodgers"],
        "correct_answer": "New York Yankees",
        "difficulty": "hard"
    },
    {
        "id": "spt_249",
        "category": "Sports",
        "subcategory": "Baseball",
        "question": "What is a walk in baseball?",
        "options": ["Four balls pitched", "Three strikes", "Home run", "Sacrifice fly"],
        "correct_answer": "Four balls pitched",
        "difficulty": "medium"
    },
    
    # American Football (6 questions)
    {
        "id": "spt_250",
        "category": "Sports",
        "subcategory": "American Football",
        "question": "How many points is a touchdown worth?",
        "options": ["6", "7", "3", "8"],
        "correct_answer": "6",
        "difficulty": "easy"
    },
    {
        "id": "spt_251",
        "category": "Sports",
        "subcategory": "American Football",
        "question": "What is the championship game of the NFL called?",
        "options": ["Super Bowl", "Championship Bowl", "NFL Finals", "Grand Bowl"],
        "correct_answer": "Super Bowl",
        "difficulty": "easy"
    },
    {
        "id": "spt_252",
        "category": "Sports",
        "subcategory": "American Football",
        "question": "How many yards must a team advance to get a first down?",
        "options": ["10", "5", "15", "20"],
        "correct_answer": "10",
        "difficulty": "medium"
    },
    {
        "id": "spt_253",
        "category": "Sports",
        "subcategory": "American Football",
        "question": "How many quarters are in an NFL game?",
        "options": ["4", "2", "3", "6"],
        "correct_answer": "4",
        "difficulty": "easy"
    },
    {
        "id": "spt_254",
        "category": "Sports",
        "subcategory": "American Football",
        "question": "What is it called when the quarterback is tackled behind the line of scrimmage?",
        "options": ["Sack", "Tackle", "Blitz", "Loss"],
        "correct_answer": "Sack",
        "difficulty": "medium"
    },
    {
        "id": "spt_255",
        "category": "Sports",
        "subcategory": "American Football",
        "question": "Which team has won the most Super Bowls?",
        "options": ["New England Patriots", "Pittsburgh Steelers", "Dallas Cowboys", "San Francisco 49ers"],
        "correct_answer": "New England Patriots",
        "difficulty": "hard"
    },
    
    # Basketball (5 questions)
    {
        "id": "spt_256",
        "category": "Sports",
        "subcategory": "Basketball",
        "question": "How many points is a free throw worth?",
        "options": ["1", "2", "3", "0"],
        "correct_answer": "1",
        "difficulty": "easy"
    },
    {
        "id": "spt_257",
        "category": "Sports",
        "subcategory": "Basketball",
        "question": "What is the painted area under the basket called?",
        "options": ["The key", "The paint", "The lane", "All of the above"],
        "correct_answer": "All of the above",
        "difficulty": "medium"
    },
    {
        "id": "spt_258",
        "category": "Sports",
        "subcategory": "Basketball",
        "question": "How many quarters are in an NBA game?",
        "options": ["4", "2", "3", "6"],
        "correct_answer": "4",
        "difficulty": "easy"
    },
    {
        "id": "spt_259",
        "category": "Sports",
        "subcategory": "Basketball",
        "question": "What is a double-double in basketball?",
        "options": ["10+ in two stat categories", "20 points", "Two consecutive wins", "Double overtime"],
        "correct_answer": "10+ in two stat categories",
        "difficulty": "medium"
    },
    {
        "id": "spt_260",
        "category": "Sports",
        "subcategory": "Basketball",
        "question": "How high is an NBA basketball hoop?",
        "options": ["10 feet", "9 feet", "11 feet", "12 feet"],
        "correct_answer": "10 feet",
        "difficulty": "medium"
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
