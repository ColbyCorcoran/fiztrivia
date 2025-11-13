import json

# Load database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# 50 new Sports questions (spt_251 to spt_300)
# Distribution: Basketball (7), American Football (6), Baseball (6), Tennis (6),
# Soccer (6), Hockey (6), Golf (6), Olympics (7)
# Emphasis on hard/medium difficulty

new_questions = [
    # Basketball (7 questions) - spt_251-257
    {
        "id": "spt_251",
        "category": "Sports",
        "subcategory": "Basketball",
        "question": "What is the regulation height of a basketball hoop in feet?",
        "options": ["10 feet", "9 feet", "11 feet", "12 feet"],
        "correct_answer": "10 feet",
        "difficulty": "easy"
    },
    {
        "id": "spt_252",
        "category": "Sports",
        "subcategory": "Basketball",
        "question": "Who holds the NBA record for most career points?",
        "options": ["LeBron James", "Kareem Abdul-Jabbar", "Michael Jordan", "Kobe Bryant"],
        "correct_answer": "LeBron James",
        "difficulty": "medium"
    },
    {
        "id": "spt_253",
        "category": "Sports",
        "subcategory": "Basketball",
        "question": "What is the diameter of a basketball hoop in inches?",
        "options": ["18 inches", "16 inches", "20 inches", "22 inches"],
        "correct_answer": "18 inches",
        "difficulty": "hard"
    },
    {
        "id": "spt_254",
        "category": "Sports",
        "subcategory": "Basketball",
        "question": "Which team did Michael Jordan play for during most of his career?",
        "options": ["Chicago Bulls", "Washington Wizards", "Los Angeles Lakers", "Boston Celtics"],
        "correct_answer": "Chicago Bulls",
        "difficulty": "easy"
    },
    {
        "id": "spt_255",
        "category": "Sports",
        "subcategory": "Basketball",
        "question": "What is the three-point line distance in the NBA (in feet)?",
        "options": ["23.75 feet", "22 feet", "24 feet", "25 feet"],
        "correct_answer": "23.75 feet",
        "difficulty": "hard"
    },
    {
        "id": "spt_256",
        "category": "Sports",
        "subcategory": "Basketball",
        "question": "How many minutes is each quarter in an NBA game?",
        "options": ["12 minutes", "10 minutes", "15 minutes", "20 minutes"],
        "correct_answer": "12 minutes",
        "difficulty": "medium"
    },
    {
        "id": "spt_257",
        "category": "Sports",
        "subcategory": "Basketball",
        "question": "Which player is known as 'The Greek Freak'?",
        "options": ["Giannis Antetokounmpo", "Nikola Jokić", "Luka Dončić", "Kristaps Porziņģis"],
        "correct_answer": "Giannis Antetokounmpo",
        "difficulty": "medium"
    },

    # American Football (6 questions) - spt_258-263
    {
        "id": "spt_258",
        "category": "Sports",
        "subcategory": "American Football",
        "question": "How many yards is a football field from end zone to end zone?",
        "options": ["100 yards", "110 yards", "120 yards", "90 yards"],
        "correct_answer": "100 yards",
        "difficulty": "easy"
    },
    {
        "id": "spt_259",
        "category": "Sports",
        "subcategory": "American Football",
        "question": "Which team has won the most Super Bowl championships?",
        "options": ["New England Patriots", "Pittsburgh Steelers", "Dallas Cowboys", "San Francisco 49ers"],
        "correct_answer": "New England Patriots",
        "difficulty": "medium"
    },
    {
        "id": "spt_260",
        "category": "Sports",
        "subcategory": "American Football",
        "question": "Who has thrown the most touchdown passes in NFL history?",
        "options": ["Tom Brady", "Peyton Manning", "Drew Brees", "Brett Favre"],
        "correct_answer": "Tom Brady",
        "difficulty": "medium"
    },
    {
        "id": "spt_261",
        "category": "Sports",
        "subcategory": "American Football",
        "question": "How many points is a field goal worth?",
        "options": ["3", "2", "6", "7"],
        "correct_answer": "3",
        "difficulty": "easy"
    },
    {
        "id": "spt_262",
        "category": "Sports",
        "subcategory": "American Football",
        "question": "How many players from each team are on the field during a play?",
        "options": ["11", "10", "12", "9"],
        "correct_answer": "11",
        "difficulty": "easy"
    },
    {
        "id": "spt_263",
        "category": "Sports",
        "subcategory": "American Football",
        "question": "What is the trophy awarded to the Super Bowl winner called?",
        "options": ["Vince Lombardi Trophy", "Stanley Cup", "Larry O'Brien Trophy", "Commissioner's Trophy"],
        "correct_answer": "Vince Lombardi Trophy",
        "difficulty": "medium"
    },

    # Baseball (6 questions) - spt_264-269
    {
        "id": "spt_264",
        "category": "Sports",
        "subcategory": "Baseball",
        "question": "How many innings are in a regulation baseball game?",
        "options": ["9", "7", "10", "12"],
        "correct_answer": "9",
        "difficulty": "easy"
    },
    {
        "id": "spt_265",
        "category": "Sports",
        "subcategory": "Baseball",
        "question": "Who holds the record for most home runs in a single MLB season?",
        "options": ["Barry Bonds", "Mark McGwire", "Sammy Sosa", "Babe Ruth"],
        "correct_answer": "Barry Bonds",
        "difficulty": "hard"
    },
    {
        "id": "spt_266",
        "category": "Sports",
        "subcategory": "Baseball",
        "question": "What is it called when a batter hits the ball over the outfield fence?",
        "options": ["Home run", "Grand slam", "Triple", "Double"],
        "correct_answer": "Home run",
        "difficulty": "easy"
    },
    {
        "id": "spt_267",
        "category": "Sports",
        "subcategory": "Baseball",
        "question": "Which team has won the most World Series championships?",
        "options": ["New York Yankees", "St. Louis Cardinals", "Boston Red Sox", "San Francisco Giants"],
        "correct_answer": "New York Yankees",
        "difficulty": "medium"
    },
    {
        "id": "spt_268",
        "category": "Sports",
        "subcategory": "Baseball",
        "question": "How many bases are on a baseball diamond?",
        "options": ["4", "3", "5", "6"],
        "correct_answer": "4",
        "difficulty": "easy"
    },
    {
        "id": "spt_269",
        "category": "Sports",
        "subcategory": "Baseball",
        "question": "What is the distance between bases on a baseball field?",
        "options": ["90 feet", "80 feet", "100 feet", "85 feet"],
        "correct_answer": "90 feet",
        "difficulty": "hard"
    },

    # Tennis (6 questions) - spt_270-275
    {
        "id": "spt_270",
        "category": "Sports",
        "subcategory": "Tennis",
        "question": "What are the four Grand Slam tournaments?",
        "options": ["Australian Open, French Open, Wimbledon, US Open", "Davis Cup, French Open, Wimbledon, US Open", "Australian Open, Italian Open, Wimbledon, US Open", "Masters Cup, French Open, Wimbledon, US Open"],
        "correct_answer": "Australian Open, French Open, Wimbledon, US Open",
        "difficulty": "medium"
    },
    {
        "id": "spt_271",
        "category": "Sports",
        "subcategory": "Tennis",
        "question": "Which male player has won the most Grand Slam singles titles?",
        "options": ["Novak Djokovic", "Rafael Nadal", "Roger Federer", "Pete Sampras"],
        "correct_answer": "Novak Djokovic",
        "difficulty": "medium"
    },
    {
        "id": "spt_272",
        "category": "Sports",
        "subcategory": "Tennis",
        "question": "What is a score of zero called in tennis?",
        "options": ["Love", "Nil", "Zero", "Deuce"],
        "correct_answer": "Love",
        "difficulty": "easy"
    },
    {
        "id": "spt_273",
        "category": "Sports",
        "subcategory": "Tennis",
        "question": "What surface is the French Open played on?",
        "options": ["Clay", "Grass", "Hard court", "Carpet"],
        "correct_answer": "Clay",
        "difficulty": "medium"
    },
    {
        "id": "spt_274",
        "category": "Sports",
        "subcategory": "Tennis",
        "question": "What is it called when the score is tied at 40-40?",
        "options": ["Deuce", "Advantage", "Match point", "Game point"],
        "correct_answer": "Deuce",
        "difficulty": "easy"
    },
    {
        "id": "spt_275",
        "category": "Sports",
        "subcategory": "Tennis",
        "question": "Which tournament is played on grass courts?",
        "options": ["Wimbledon", "French Open", "Australian Open", "US Open"],
        "correct_answer": "Wimbledon",
        "difficulty": "easy"
    },

    # Soccer (6 questions) - spt_276-281
    {
        "id": "spt_276",
        "category": "Sports",
        "subcategory": "Soccer",
        "question": "How many players are on a soccer team on the field at one time?",
        "options": ["11", "10", "12", "9"],
        "correct_answer": "11",
        "difficulty": "easy"
    },
    {
        "id": "spt_277",
        "category": "Sports",
        "subcategory": "Soccer",
        "question": "What is it called when a player scores three goals in one match?",
        "options": ["Hat trick", "Triple threat", "Trifecta", "Triple play"],
        "correct_answer": "Hat trick",
        "difficulty": "easy"
    },
    {
        "id": "spt_278",
        "category": "Sports",
        "subcategory": "Soccer",
        "question": "Which player has won the most Ballon d'Or awards?",
        "options": ["Lionel Messi", "Cristiano Ronaldo", "Michel Platini", "Johan Cruyff"],
        "correct_answer": "Lionel Messi",
        "difficulty": "medium"
    },
    {
        "id": "spt_279",
        "category": "Sports",
        "subcategory": "Soccer",
        "question": "What is the penalty for a handball in the penalty box?",
        "options": ["Penalty kick", "Free kick", "Corner kick", "Yellow card"],
        "correct_answer": "Penalty kick",
        "difficulty": "medium"
    },
    {
        "id": "spt_280",
        "category": "Sports",
        "subcategory": "Soccer",
        "question": "What color card results in a player being ejected from the match?",
        "options": ["Red", "Yellow", "Blue", "Black"],
        "correct_answer": "Red",
        "difficulty": "easy"
    },
    {
        "id": "spt_281",
        "category": "Sports",
        "subcategory": "Soccer",
        "question": "Which country hosted the 2014 FIFA World Cup?",
        "options": ["Brazil", "Germany", "Russia", "South Africa"],
        "correct_answer": "Brazil",
        "difficulty": "medium"
    },

    # Hockey (6 questions) - spt_282-287
    {
        "id": "spt_282",
        "category": "Sports",
        "subcategory": "Hockey",
        "question": "What is the championship trophy in the NHL called?",
        "options": ["Stanley Cup", "Calder Cup", "Conn Smythe Trophy", "Hart Trophy"],
        "correct_answer": "Stanley Cup",
        "difficulty": "easy"
    },
    {
        "id": "spt_283",
        "category": "Sports",
        "subcategory": "Hockey",
        "question": "How many players from each team are on the ice at one time (not including goalie)?",
        "options": ["5", "6", "4", "7"],
        "correct_answer": "5",
        "difficulty": "medium"
    },
    {
        "id": "spt_284",
        "category": "Sports",
        "subcategory": "Hockey",
        "question": "What is a hat trick in hockey?",
        "options": ["Scoring three goals in one game", "Blocking three shots", "Three assists", "Three penalties"],
        "correct_answer": "Scoring three goals in one game",
        "difficulty": "easy"
    },
    {
        "id": "spt_285",
        "category": "Sports",
        "subcategory": "Hockey",
        "question": "How long is each period in an NHL hockey game?",
        "options": ["20 minutes", "15 minutes", "25 minutes", "30 minutes"],
        "correct_answer": "20 minutes",
        "difficulty": "medium"
    },
    {
        "id": "spt_286",
        "category": "Sports",
        "subcategory": "Hockey",
        "question": "Which team has won the most Stanley Cup championships?",
        "options": ["Montreal Canadiens", "Toronto Maple Leafs", "Detroit Red Wings", "Boston Bruins"],
        "correct_answer": "Montreal Canadiens",
        "difficulty": "hard"
    },
    {
        "id": "spt_287",
        "category": "Sports",
        "subcategory": "Hockey",
        "question": "What is the blue line used for in hockey?",
        "options": ["Marks the offensive/defensive zones", "Goal line", "Center line", "Penalty box boundary"],
        "correct_answer": "Marks the offensive/defensive zones",
        "difficulty": "hard"
    },

    # Golf (6 questions) - spt_288-293
    {
        "id": "spt_288",
        "category": "Sports",
        "subcategory": "Golf",
        "question": "What is par on a typical golf course for 18 holes?",
        "options": ["72", "70", "74", "68"],
        "correct_answer": "72",
        "difficulty": "medium"
    },
    {
        "id": "spt_289",
        "category": "Sports",
        "subcategory": "Golf",
        "question": "What is one stroke under par called?",
        "options": ["Birdie", "Eagle", "Bogey", "Par"],
        "correct_answer": "Birdie",
        "difficulty": "easy"
    },
    {
        "id": "spt_290",
        "category": "Sports",
        "subcategory": "Golf",
        "question": "How many clubs is a golfer allowed to carry during a round?",
        "options": ["14", "12", "16", "18"],
        "correct_answer": "14",
        "difficulty": "hard"
    },
    {
        "id": "spt_291",
        "category": "Sports",
        "subcategory": "Golf",
        "question": "Which major golf tournament is held at Augusta National?",
        "options": ["The Masters", "US Open", "PGA Championship", "The Open Championship"],
        "correct_answer": "The Masters",
        "difficulty": "medium"
    },
    {
        "id": "spt_292",
        "category": "Sports",
        "subcategory": "Golf",
        "question": "What is two strokes under par called?",
        "options": ["Eagle", "Birdie", "Albatross", "Bogey"],
        "correct_answer": "Eagle",
        "difficulty": "easy"
    },
    {
        "id": "spt_293",
        "category": "Sports",
        "subcategory": "Golf",
        "question": "Who has won the most major championships in men's golf?",
        "options": ["Jack Nicklaus", "Tiger Woods", "Arnold Palmer", "Gary Player"],
        "correct_answer": "Jack Nicklaus",
        "difficulty": "medium"
    },

    # Olympics (7 questions) - spt_294-300
    {
        "id": "spt_294",
        "category": "Sports",
        "subcategory": "Olympics",
        "question": "Where were the first modern Olympic Games held?",
        "options": ["Athens, Greece", "Paris, France", "London, England", "Rome, Italy"],
        "correct_answer": "Athens, Greece",
        "difficulty": "medium"
    },
    {
        "id": "spt_295",
        "category": "Sports",
        "subcategory": "Olympics",
        "question": "Which athlete has won the most Olympic gold medals?",
        "options": ["Michael Phelps", "Usain Bolt", "Simone Biles", "Carl Lewis"],
        "correct_answer": "Michael Phelps",
        "difficulty": "easy"
    },
    {
        "id": "spt_296",
        "category": "Sports",
        "subcategory": "Olympics",
        "question": "What are the five Olympic rings colors?",
        "options": ["Blue, yellow, black, green, red", "Blue, yellow, white, green, red", "Blue, orange, black, green, red", "Purple, yellow, black, green, red"],
        "correct_answer": "Blue, yellow, black, green, red",
        "difficulty": "hard"
    },
    {
        "id": "spt_297",
        "category": "Sports",
        "subcategory": "Olympics",
        "question": "What year were the first modern Olympics held?",
        "options": ["1896", "1900", "1892", "1888"],
        "correct_answer": "1896",
        "difficulty": "hard"
    },
    {
        "id": "spt_298",
        "category": "Sports",
        "subcategory": "Olympics",
        "question": "Which country has hosted the Summer Olympics the most times?",
        "options": ["United States", "France", "United Kingdom", "Greece"],
        "correct_answer": "United States",
        "difficulty": "medium"
    },
    {
        "id": "spt_299",
        "category": "Sports",
        "subcategory": "Olympics",
        "question": "What is the Olympic motto?",
        "options": ["Faster, Higher, Stronger", "United in Sport", "Excellence in Competition", "Victory and Honor"],
        "correct_answer": "Faster, Higher, Stronger",
        "difficulty": "medium"
    },
    {
        "id": "spt_300",
        "category": "Sports",
        "subcategory": "Olympics",
        "question": "What metal are Olympic gold medals primarily made of?",
        "options": ["Silver with gold plating", "Pure gold", "Bronze with gold plating", "Copper with gold plating"],
        "correct_answer": "Silver with gold plating",
        "difficulty": "hard"
    }
]

# Add new questions to Sports category
data['categories']['Sports'].extend(new_questions)

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ Added {len(new_questions)} Sports questions")
print(f"New range: spt_251 to spt_300")
print(f"\nDistribution:")
print(f"  Basketball: 7 questions")
print(f"  American Football: 6 questions")
print(f"  Baseball: 6 questions")
print(f"  Tennis: 6 questions")
print(f"  Soccer: 6 questions")
print(f"  Hockey: 6 questions")
print(f"  Golf: 6 questions")
print(f"  Olympics: 7 questions")
print(f"\nTotal Sports questions: {len(data['categories']['Sports'])}")
