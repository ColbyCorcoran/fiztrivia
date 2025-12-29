#!/usr/bin/env python3
"""Add 65 Drama/Comedy questions to reach 75 total (ent_172 to ent_236)"""
import json

new_questions = [
    # EASY QUESTIONS (22 total)
    {
        "id": "ent_172",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of the coffee shop in Friends?",
        "options": ["Central Perk", "Starbucks", "Coffee Bean", "The Grind"],
        "correct_answer": "Central Perk",
        "difficulty": "easy"
    },
    {
        "id": "ent_173",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "Who plays Forrest Gump in the 1994 film?",
        "options": ["Tom Hanks", "Brad Pitt", "Matt Damon", "Leonardo DiCaprio"],
        "correct_answer": "Tom Hanks",
        "difficulty": "easy"
    },
    {
        "id": "ent_174",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of the high school chemistry teacher in Breaking Bad?",
        "options": ["Walter White", "Jesse Pinkman", "Hank Schrader", "Saul Goodman"],
        "correct_answer": "Walter White",
        "difficulty": "easy"
    },
    {
        "id": "ent_175",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of the bar in How I Met Your Mother?",
        "options": ["MacLaren's Pub", "Cheers", "Paddy's Pub", "The Ale House"],
        "correct_answer": "MacLaren's Pub",
        "difficulty": "easy"
    },
    {
        "id": "ent_176",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "Who plays Andy Dwyer in Parks and Recreation?",
        "options": ["Chris Pratt", "Nick Offerman", "Aziz Ansari", "Adam Scott"],
        "correct_answer": "Chris Pratt",
        "difficulty": "easy"
    },
    {
        "id": "ent_177",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the precinct number in Brooklyn Nine-Nine?",
        "options": ["99", "98", "100", "97"],
        "correct_answer": "99",
        "difficulty": "easy"
    },
    {
        "id": "ent_178",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "Who directed The Shawshank Redemption?",
        "options": ["Frank Darabont", "Steven Spielberg", "Martin Scorsese", "Christopher Nolan"],
        "correct_answer": "Frank Darabont",
        "difficulty": "easy"
    },
    {
        "id": "ent_179",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of the family in Modern Family?",
        "options": ["Pritchett-Dunphy-Tucker", "The Simpsons", "The Griffins", "The Belchers"],
        "correct_answer": "Pritchett-Dunphy-Tucker",
        "difficulty": "easy"
    },
    {
        "id": "ent_180",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "Who plays Michael Scott in The Office (US)?",
        "options": ["Steve Carell", "Rainn Wilson", "John Krasinski", "B.J. Novak"],
        "correct_answer": "Steve Carell",
        "difficulty": "easy"
    },
    {
        "id": "ent_181",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of the band in School of Rock?",
        "options": ["School of Rock", "The Rockers", "Kid Rock", "Rock Academy"],
        "correct_answer": "School of Rock",
        "difficulty": "easy"
    },
    {
        "id": "ent_182",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "Who plays Jack Dawson in Titanic?",
        "options": ["Leonardo DiCaprio", "Brad Pitt", "Tom Cruise", "Johnny Depp"],
        "correct_answer": "Leonardo DiCaprio",
        "difficulty": "easy"
    },
    {
        "id": "ent_183",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is Sheldon Cooper's catchphrase in The Big Bang Theory?",
        "options": ["Bazinga!", "How you doin'?", "That's what she said", "D'oh!"],
        "correct_answer": "Bazinga!",
        "difficulty": "easy"
    },
    {
        "id": "ent_184",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "Who plays Tony Soprano in The Sopranos?",
        "options": ["James Gandolfini", "Robert De Niro", "Al Pacino", "Joe Pesci"],
        "correct_answer": "James Gandolfini",
        "difficulty": "easy"
    },
    {
        "id": "ent_185",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What city does Seinfeld take place in?",
        "options": ["New York City", "Los Angeles", "Chicago", "Boston"],
        "correct_answer": "New York City",
        "difficulty": "easy"
    },
    {
        "id": "ent_186",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "Who plays Vito Corleone in The Godfather?",
        "options": ["Marlon Brando", "Al Pacino", "Robert De Niro", "James Caan"],
        "correct_answer": "Marlon Brando",
        "difficulty": "easy"
    },
    {
        "id": "ent_187",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of the department store in The Office (UK)?",
        "options": ["Wernham Hogg", "Dunder Mifflin", "Staples", "Office Depot"],
        "correct_answer": "Wernham Hogg",
        "difficulty": "easy"
    },
    {
        "id": "ent_188",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "Who plays Elle Woods in Legally Blonde?",
        "options": ["Reese Witherspoon", "Jennifer Aniston", "Cameron Diaz", "Gwyneth Paltrow"],
        "correct_answer": "Reese Witherspoon",
        "difficulty": "easy"
    },
    {
        "id": "ent_189",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of the town in Gilmore Girls?",
        "options": ["Stars Hollow", "Stars Valley", "Hollow Creek", "Gilmore Town"],
        "correct_answer": "Stars Hollow",
        "difficulty": "easy"
    },
    {
        "id": "ent_190",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "Who plays Dwight Schrute in The Office (US)?",
        "options": ["Rainn Wilson", "Steve Carell", "John Krasinski", "Ed Helms"],
        "correct_answer": "Rainn Wilson",
        "difficulty": "easy"
    },
    {
        "id": "ent_191",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of the paper company in The Office (US)?",
        "options": ["Dunder Mifflin", "Staples", "Office Max", "Wernham Hogg"],
        "correct_answer": "Dunder Mifflin",
        "difficulty": "easy"
    },
    {
        "id": "ent_192",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "Who plays Ron Swanson in Parks and Recreation?",
        "options": ["Nick Offerman", "Chris Pratt", "Aziz Ansari", "Adam Scott"],
        "correct_answer": "Nick Offerman",
        "difficulty": "easy"
    },
    {
        "id": "ent_193",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of the ship in Titanic?",
        "options": ["RMS Titanic", "HMS Titanic", "SS Titanic", "USS Titanic"],
        "correct_answer": "RMS Titanic",
        "difficulty": "easy"
    },

    # MEDIUM QUESTIONS (26 total)
    {
        "id": "ent_194",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In Friends, what is the name of Ross's second wife?",
        "options": ["Emily", "Rachel", "Carol", "Julie"],
        "correct_answer": "Emily",
        "difficulty": "medium"
    },
    {
        "id": "ent_195",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What year was Breaking Bad first aired?",
        "options": ["2008", "2006", "2010", "2005"],
        "correct_answer": "2008",
        "difficulty": "medium"
    },
    {
        "id": "ent_196",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In The Shawshank Redemption, what does Andy Dufresne use to escape?",
        "options": ["A rock hammer", "A spoon", "A knife", "A screwdriver"],
        "correct_answer": "A rock hammer",
        "difficulty": "medium"
    },
    {
        "id": "ent_197",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of the department in Parks and Recreation?",
        "options": ["Parks and Recreation Department", "City Planning", "Public Works", "Community Development"],
        "correct_answer": "Parks and Recreation Department",
        "difficulty": "medium"
    },
    {
        "id": "ent_198",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In How I Met Your Mother, what is Barney's job?",
        "options": ["P.L.E.A.S.E.", "Lawyer", "Architect", "Banker"],
        "correct_answer": "P.L.E.A.S.E.",
        "difficulty": "medium"
    },
    {
        "id": "ent_199",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of the paper company that buys Dunder Mifflin?",
        "options": ["Sabre", "Staples", "Office Depot", "Michael Scott Paper Company"],
        "correct_answer": "Sabre",
        "difficulty": "medium"
    },
    {
        "id": "ent_200",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In Seinfeld, what is the name of Jerry's neighbor?",
        "options": ["Cosmo Kramer", "George Costanza", "Elaine Benes", "Newman"],
        "correct_answer": "Cosmo Kramer",
        "difficulty": "medium"
    },
    {
        "id": "ent_201",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of Michael Corleone's wife in The Godfather?",
        "options": ["Kay Adams", "Connie Corleone", "Apollonia Vitelli", "Sandra Corleone"],
        "correct_answer": "Kay Adams",
        "difficulty": "medium"
    },
    {
        "id": "ent_202",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In Brooklyn Nine-Nine, what is Jake Peralta's favorite movie?",
        "options": ["Die Hard", "Lethal Weapon", "Speed", "The Rock"],
        "correct_answer": "Die Hard",
        "difficulty": "medium"
    },
    {
        "id": "ent_203",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of Walter White's drug alias in Breaking Bad?",
        "options": ["Heisenberg", "The Cook", "Blue Sky", "Mr. White"],
        "correct_answer": "Heisenberg",
        "difficulty": "medium"
    },
    {
        "id": "ent_204",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In The Big Bang Theory, what is Leonard's last name?",
        "options": ["Hofstadter", "Cooper", "Wolowitz", "Koothrappali"],
        "correct_answer": "Hofstadter",
        "difficulty": "medium"
    },
    {
        "id": "ent_205",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of the advertising agency in Mad Men?",
        "options": ["Sterling Cooper", "Draper Advertising", "Madison Avenue Agency", "Cooper & Associates"],
        "correct_answer": "Sterling Cooper",
        "difficulty": "medium"
    },
    {
        "id": "ent_206",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In Friends, what is Phoebe's twin sister's name?",
        "options": ["Ursula", "Rachel", "Monica", "Carol"],
        "correct_answer": "Ursula",
        "difficulty": "medium"
    },
    {
        "id": "ent_207",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of the prison in The Shawshank Redemption?",
        "options": ["Shawshank State Penitentiary", "Alcatraz", "San Quentin", "Folsom Prison"],
        "correct_answer": "Shawshank State Penitentiary",
        "difficulty": "medium"
    },
    {
        "id": "ent_208",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In Forrest Gump, what company does Forrest invest in?",
        "options": ["Apple", "Microsoft", "IBM", "Coca-Cola"],
        "correct_answer": "Apple",
        "difficulty": "medium"
    },
    {
        "id": "ent_209",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of the boat in The Office (US) episode 'Booze Cruise'?",
        "options": ["Captain Jack", "Love Boat", "SS Michael", "Party Cruise"],
        "correct_answer": "Captain Jack",
        "difficulty": "medium"
    },
    {
        "id": "ent_210",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In Arrested Development, what is the family's frozen banana stand called?",
        "options": ["Bluth's Original Frozen Banana Stand", "The Banana Stand", "Frozen Delights", "Banana Bay"],
        "correct_answer": "Bluth's Original Frozen Banana Stand",
        "difficulty": "medium"
    },
    {
        "id": "ent_211",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of the judge in The Good Place?",
        "options": ["Gen", "Michael", "Janet", "Shawn"],
        "correct_answer": "Gen",
        "difficulty": "medium"
    },
    {
        "id": "ent_212",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In Pulp Fiction, what is in Marsellus Wallace's briefcase?",
        "options": ["Unknown", "Gold", "Diamonds", "Money"],
        "correct_answer": "Unknown",
        "difficulty": "medium"
    },
    {
        "id": "ent_213",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of the high school in Freaks and Geeks?",
        "options": ["William McKinley High School", "Freaks High", "Geeks Academy", "McKinley Prep"],
        "correct_answer": "William McKinley High School",
        "difficulty": "medium"
    },
    {
        "id": "ent_214",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In Good Will Hunting, what subject is Will a genius in?",
        "options": ["Mathematics", "Physics", "Chemistry", "Engineering"],
        "correct_answer": "Mathematics",
        "difficulty": "medium"
    },
    {
        "id": "ent_215",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of the mother in How I Met Your Mother?",
        "options": ["Tracy McConnell", "Robin Scherbatsky", "Victoria", "Stella Zinman"],
        "correct_answer": "Tracy McConnell",
        "difficulty": "medium"
    },
    {
        "id": "ent_216",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In 30 Rock, what network does TGS with Tracy Jordan air on?",
        "options": ["NBC", "CBS", "ABC", "FOX"],
        "correct_answer": "NBC",
        "difficulty": "medium"
    },
    {
        "id": "ent_217",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of Andy's a cappella group in The Office (US)?",
        "options": ["Here Comes Treble", "The Office Singers", "Paper Company Harmony", "Acappella Express"],
        "correct_answer": "Here Comes Treble",
        "difficulty": "medium"
    },
    {
        "id": "ent_218",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In The Sopranos, what is the name of Tony's psychiatrist?",
        "options": ["Dr. Jennifer Melfi", "Dr. Carmela Soprano", "Dr. Anthony Soprano", "Dr. Christopher Moltisanti"],
        "correct_answer": "Dr. Jennifer Melfi",
        "difficulty": "medium"
    },
    {
        "id": "ent_219",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What year did Friends first air?",
        "options": ["1994", "1995", "1993", "1996"],
        "correct_answer": "1994",
        "difficulty": "medium"
    },

    # HARD QUESTIONS (17 total)
    {
        "id": "ent_220",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In Breaking Bad, what is the name of the fast food chain Gus Fring owns?",
        "options": ["Los Pollos Hermanos", "El Pollo Loco", "Chicken Brothers", "The Chicken Shack"],
        "correct_answer": "Los Pollos Hermanos",
        "difficulty": "hard"
    },
    {
        "id": "ent_221",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In The Shawshank Redemption, what is Red's full name?",
        "options": ["Ellis Boyd Redding", "Red Boyd", "Ellis Redding", "Boyd Red"],
        "correct_answer": "Ellis Boyd Redding",
        "difficulty": "hard"
    },
    {
        "id": "ent_222",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of the apartment number Monica lives in on Friends?",
        "options": ["Apartment 20", "Apartment 5", "Apartment 10", "Apartment 15"],
        "correct_answer": "Apartment 20",
        "difficulty": "hard"
    },
    {
        "id": "ent_223",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In The Godfather, what is the name of the horse whose head is placed in a bed?",
        "options": ["Khartoum", "Seabiscuit", "Secretariat", "Man o' War"],
        "correct_answer": "Khartoum",
        "difficulty": "hard"
    },
    {
        "id": "ent_224",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In Parks and Recreation, what is the name of the candy bar Leslie creates?",
        "options": ["Sweetums Nutriyums", "The Leslie Bar", "Pawnee Treat", "Knope Candy"],
        "correct_answer": "Sweetums Nutriyums",
        "difficulty": "hard"
    },
    {
        "id": "ent_225",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of the improv group in The Office (US)?",
        "options": ["The Finer Things Club", "Here Comes Treble", "Threat Level Midnight", "Scrantonicity"],
        "correct_answer": "The Finer Things Club",
        "difficulty": "hard"
    },
    {
        "id": "ent_226",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In Seinfeld, what is the name of the doctor who treats Kramer?",
        "options": ["Dr. Martin van Nostrand", "Dr. Cosmo Kramer", "Dr. Bob Sacamano", "Dr. Peter Lorre"],
        "correct_answer": "Dr. Martin van Nostrand",
        "difficulty": "hard"
    },
    {
        "id": "ent_227",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In How I Met Your Mother, what is the name of Robin's Canadian pop star alter ego?",
        "options": ["Robin Sparkles", "Robin Star", "Robin Canada", "Robin Shine"],
        "correct_answer": "Robin Sparkles",
        "difficulty": "hard"
    },
    {
        "id": "ent_228",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In The Big Bang Theory, what is the name of Sheldon's online video show?",
        "options": ["Fun with Flags", "Science with Sheldon", "Sheldon's Lab", "The Cooper Show"],
        "correct_answer": "Fun with Flags",
        "difficulty": "hard"
    },
    {
        "id": "ent_229",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In Brooklyn Nine-Nine, what is Captain Holt's husband's name?",
        "options": ["Kevin", "Raymond", "Terry", "Charles"],
        "correct_answer": "Kevin",
        "difficulty": "hard"
    },
    {
        "id": "ent_230",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of the fictional brand of cigarettes in Mad Men?",
        "options": ["Lucky Strike", "Marlboro", "Camel", "Winston"],
        "correct_answer": "Lucky Strike",
        "difficulty": "hard"
    },
    {
        "id": "ent_231",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In Arrested Development, what is Tobias Fünke's profession?",
        "options": ["Analrapist (Analyst/Therapist)", "Lawyer", "Doctor", "Magician"],
        "correct_answer": "Analrapist (Analyst/Therapist)",
        "difficulty": "hard"
    },
    {
        "id": "ent_232",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In Forrest Gump, what is Forrest's IQ?",
        "options": ["75", "80", "70", "85"],
        "correct_answer": "75",
        "difficulty": "hard"
    },
    {
        "id": "ent_233",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In The Office (US), what is the name of Michael's screenplay?",
        "options": ["Threat Level Midnight", "Agent Michael Scarn", "The Office Movie", "Scarn Identity"],
        "correct_answer": "Threat Level Midnight",
        "difficulty": "hard"
    },
    {
        "id": "ent_234",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In Good Will Hunting, what university does Will work as a janitor at?",
        "options": ["MIT", "Harvard", "Boston University", "Yale"],
        "correct_answer": "MIT",
        "difficulty": "hard"
    },
    {
        "id": "ent_235",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In Pulp Fiction, what is the name of the boxer who refuses to throw the fight?",
        "options": ["Butch Coolidge", "Vincent Vega", "Jules Winnfield", "Marsellus Wallace"],
        "correct_answer": "Butch Coolidge",
        "difficulty": "hard"
    },
    {
        "id": "ent_236",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In 30 Rock, what is Jack Donaghy's middle name?",
        "options": ["Francis", "Patrick", "William", "Michael"],
        "correct_answer": "Francis",
        "difficulty": "hard"
    }
]

def add_drama_comedy_questions():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    # Add new questions
    data['categories']['Entertainment'].extend(new_questions)

    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Added {len(new_questions)} Drama/Comedy questions")
    print(f"   Easy: {sum(1 for q in new_questions if q['difficulty'] == 'easy')}")
    print(f"   Medium: {sum(1 for q in new_questions if q['difficulty'] == 'medium')}")
    print(f"   Hard: {sum(1 for q in new_questions if q['difficulty'] == 'hard')}")
    print(f"\n📊 Drama/Comedy now has 75 total questions (10 → 75)")

if __name__ == '__main__':
    add_drama_comedy_questions()
