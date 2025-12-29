#!/usr/bin/env python3
"""Replace Entertainment questions that overlap with expansion packs"""
import json

# Define all replacement questions organized by what they're replacing
replacements = {
    # Replace PIXAR questions (26 total) with diverse animation (TV & movies)
    "ent_063": {
        "id": "ent_063",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of the robot in Transformers?",
        "options": ["Optimus Prime", "Bumblebee", "Megatron", "Starscream"],
        "correct_answer": "Optimus Prime",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_078": {
        "id": "ent_078",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of the organization in Kingsman?",
        "options": ["Kingsman", "The Statesman", "The Secret Service", "MI6"],
        "correct_answer": "Kingsman",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_100": {
        "id": "ent_100",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "In Mad Max: Fury Road, what is the name of the tyrannical leader?",
        "options": ["Immortan Joe", "The War Boys", "Max Rockatansky", "Furiosa"],
        "correct_answer": "Immortan Joe",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },

    # Animation - Replace with TV shows and non-Disney/Pixar content
    "ent_118": {
        "id": "ent_118",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the family in The Simpsons?",
        "options": ["The Simpsons", "The Griffins", "The Belchers", "The Smiths"],
        "correct_answer": "The Simpsons",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_119": {
        "id": "ent_119",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What color is Papa Smurf in The Smurfs?",
        "options": ["Red", "Blue", "White", "Yellow"],
        "correct_answer": "Red",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_120": {
        "id": "ent_120",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the cat in Tom and Jerry?",
        "options": ["Tom", "Jerry", "Spike", "Tyke"],
        "correct_answer": "Tom",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_123": {
        "id": "ent_123",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the family dog in Family Guy?",
        "options": ["Brian", "Stewie", "Peter", "Quagmire"],
        "correct_answer": "Brian",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_124": {
        "id": "ent_124",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the restaurant in Bob's Burgers?",
        "options": ["Bob's Burgers", "Jimmy Pesto's", "The Burger Joint", "Teddy's"],
        "correct_answer": "Bob's Burgers",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_127": {
        "id": "ent_127",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is Scooby-Doo's favorite food?",
        "options": ["Scooby Snacks", "Pizza", "Sandwiches", "Burgers"],
        "correct_answer": "Scooby Snacks",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_130": {
        "id": "ent_130",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What town do the Flintstones live in?",
        "options": ["Bedrock", "Stone City", "Rock Town", "Prehistoric Park"],
        "correct_answer": "Bedrock",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_134": {
        "id": "ent_134",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Avatar: The Last Airbender, what element can't Aang bend at first?",
        "options": ["Fire", "Water", "Earth", "Air"],
        "correct_answer": "Fire",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_137": {
        "id": "ent_137",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of Bart Simpson's best friend?",
        "options": ["Milhouse", "Nelson", "Ralph", "Martin"],
        "correct_answer": "Milhouse",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_138": {
        "id": "ent_138",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In South Park, what is Cartman's first name?",
        "options": ["Eric", "Kyle", "Stan", "Kenny"],
        "correct_answer": "Eric",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_141": {
        "id": "ent_141",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the boy in Adventure Time?",
        "options": ["Finn", "Jake", "Ice King", "Marceline"],
        "correct_answer": "Finn",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_143": {
        "id": "ent_143",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Futurama, what is Fry's first name?",
        "options": ["Philip", "Peter", "Frank", "Fred"],
        "correct_answer": "Philip",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_145": {
        "id": "ent_145",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the ogre princess in Shrek 2?",
        "options": ["Fiona", "Shrek", "Donkey", "Dragon"],
        "correct_answer": "Fiona",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_147": {
        "id": "ent_147",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In SpongeBob SquarePants, what is Mr. Krabs' daughter's name?",
        "options": ["Pearl", "Sandy", "Karen", "Mindy"],
        "correct_answer": "Pearl",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_153": {
        "id": "ent_153",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the penguin in Wallace and Gromit?",
        "options": ["Feathers McGraw", "Wendolene", "Preston", "Piella"],
        "correct_answer": "Feathers McGraw",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_154": {
        "id": "ent_154",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Looney Tunes, what is Bugs Bunny's catchphrase?",
        "options": ["What's up, Doc?", "That's all folks!", "Beep beep!", "I tawt I taw a puddy tat"],
        "correct_answer": "What's up, Doc?",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_159": {
        "id": "ent_159",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the dragon in The Hobbit animated film?",
        "options": ["Smaug", "Drogon", "Toothless", "Mushu"],
        "correct_answer": "Smaug",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    "ent_162": {
        "id": "ent_162",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In BoJack Horseman, what is BoJack's species?",
        "options": ["Horse", "Dog", "Cat", "Human"],
        "correct_answer": "Horse",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    "ent_163": {
        "id": "ent_163",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What year did The Simpsons first air?",
        "options": ["1989", "1990", "1987", "1992"],
        "correct_answer": "1989",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    "ent_164": {
        "id": "ent_164",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Avatar: The Last Airbender, what is Zuko's sister's name?",
        "options": ["Azula", "Katara", "Toph", "Mai"],
        "correct_answer": "Azula",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    "ent_169": {
        "id": "ent_169",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the city in Futurama?",
        "options": ["New New York", "New York", "Future City", "Planet Express City"],
        "correct_answer": "New New York",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },

    # Replace DISNEY ANIMATION questions (22 total)
    "ent_107": {
        "id": "ent_107",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the titular character in Coraline?",
        "options": ["Coraline Jones", "Wybie", "The Other Mother", "The Cat"],
        "correct_answer": "Coraline Jones",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_108": {
        "id": "ent_108",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the robot in The Iron Giant?",
        "options": ["The Iron Giant", "Hogarth", "Dean", "Kent"],
        "correct_answer": "The Iron Giant",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_110": {
        "id": "ent_110",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In The Nightmare Before Christmas, what is the main character's name?",
        "options": ["Jack Skellington", "Sally", "Oogie Boogie", "Zero"],
        "correct_answer": "Jack Skellington",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_111": {
        "id": "ent_111",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What animal is Arthur in the TV show Arthur?",
        "options": ["Aardvark", "Bear", "Rabbit", "Dog"],
        "correct_answer": "Aardvark",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_112": {
        "id": "ent_112",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the snail who dreams of racing in Turbo?",
        "options": ["Turbo", "Theo", "Whiplash", "Chet"],
        "correct_answer": "Turbo",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_117": {
        "id": "ent_117",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is Homer Simpson's job?",
        "options": ["Nuclear safety inspector", "Beer taster", "Farmer", "Mayor"],
        "correct_answer": "Nuclear safety inspector",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_122": {
        "id": "ent_122",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the boy in The Polar Express?",
        "options": ["Hero Boy", "Billy", "The Conductor", "Santa"],
        "correct_answer": "Hero Boy",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_125": {
        "id": "ent_125",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Archer, what is Sterling Archer's job?",
        "options": ["Spy", "Bartender", "Detective", "Pilot"],
        "correct_answer": "Spy",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_128": {
        "id": "ent_128",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the main character in Megamind?",
        "options": ["Megamind", "Metro Man", "Roxanne", "Minion"],
        "correct_answer": "Megamind",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_131": {
        "id": "ent_131",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Dragon Ball Z, what is Goku's alien race called?",
        "options": ["Saiyan", "Namekian", "Frieza Race", "Human"],
        "correct_answer": "Saiyan",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_132": {
        "id": "ent_132",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the town in South Park?",
        "options": ["South Park", "Park County", "Colorado Springs", "Mountain Town"],
        "correct_answer": "South Park",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_133": {
        "id": "ent_133",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Teenage Mutant Ninja Turtles, who is their sensei?",
        "options": ["Splinter", "Shredder", "April", "Casey"],
        "correct_answer": "Splinter",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_142": {
        "id": "ent_142",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the princess in Anastasia?",
        "options": ["Anastasia", "Anya", "Dimitri", "Sophie"],
        "correct_answer": "Anastasia",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_144": {
        "id": "ent_144",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Samurai Jack, what is Jack trying to destroy?",
        "options": ["Aku", "The Samurai", "The Portal", "The Sword"],
        "correct_answer": "Aku",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_150": {
        "id": "ent_150",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the horse in Spirit: Stallion of the Cimarron?",
        "options": ["Spirit", "Rain", "Strider", "Little Creek"],
        "correct_answer": "Spirit",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_151": {
        "id": "ent_151",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Courage the Cowardly Dog, where do Courage and his owners live?",
        "options": ["Nowhere, Kansas", "Somewhere, Texas", "Anywhere, Oklahoma", "Everywhere, Nebraska"],
        "correct_answer": "Nowhere, Kansas",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_152": {
        "id": "ent_152",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What year did Family Guy first air?",
        "options": ["1999", "2000", "1998", "2001"],
        "correct_answer": "1999",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_157": {
        "id": "ent_157",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In The Boondocks, what are the main characters' last name?",
        "options": ["Freeman", "Johnson", "Williams", "Jackson"],
        "correct_answer": "Freeman",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    "ent_158": {
        "id": "ent_158",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the company in Monsters University?",
        "options": ["Monsters University", "Fear Tech", "Scare Games Inc", "Roar Omega Roar"],
        "correct_answer": "Monsters University",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    "ent_160": {
        "id": "ent_160",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Gravity Falls, what are the main characters' names?",
        "options": ["Dipper and Mabel", "Stan and Ford", "Soos and Wendy", "Bill and Gideon"],
        "correct_answer": "Dipper and Mabel",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    "ent_167": {
        "id": "ent_167",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the king in The Prince of Egypt?",
        "options": ["Rameses", "Moses", "Pharaoh", "Seti"],
        "correct_answer": "Rameses",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    "ent_210": {
        "id": "ent_210",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In Community, what is the study group's favorite game?",
        "options": ["Dungeons & Dragons", "Paintball", "Foosball", "Video games"],
        "correct_answer": "Paintball",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },

    # Replace THE OFFICE questions (4 total) and Drama/Comedy Pixar overlaps
    "ent_180": {
        "id": "ent_180",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "Who plays Walter White in Breaking Bad?",
        "options": ["Bryan Cranston", "Aaron Paul", "Dean Norris", "Bob Odenkirk"],
        "correct_answer": "Bryan Cranston",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_187": {
        "id": "ent_187",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of the law firm in Suits?",
        "options": ["Pearson Hardman", "Harvey & Associates", "Legal Services", "Specter Litt"],
        "correct_answer": "Pearson Hardman",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_190": {
        "id": "ent_190",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In Scrubs, what is J.D.'s real first name?",
        "options": ["John", "James", "Jonathan", "Jason"],
        "correct_answer": "John",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_199": {
        "id": "ent_199",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of the hospital in Grey's Anatomy?",
        "options": ["Grey Sloan Memorial Hospital", "Seattle Grace Hospital", "Sacred Heart", "County General"],
        "correct_answer": "Grey Sloan Memorial Hospital",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_217": {
        "id": "ent_217",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "In New Girl, what is the name of the bar where the characters hang out?",
        "options": ["The Griffin", "MacLaren's", "The Regal Beagle", "Cheers"],
        "correct_answer": "The Griffin",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_225": {
        "id": "ent_225",
        "category": "Entertainment",
        "subcategory": "Drama/Comedy",
        "question": "What is the name of the high school in Buffy the Vampire Slayer?",
        "options": ["Sunnydale High", "Riverdale High", "Degrassi", "West Beverly"],
        "correct_answer": "Sunnydale High",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },

    # Replace STAR WARS questions (6 total)
    "ent_242": {
        "id": "ent_242",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "Who plays Ellen Ripley in Alien?",
        "options": ["Sigourney Weaver", "Linda Hamilton", "Jamie Lee Curtis", "Carrie Fisher"],
        "correct_answer": "Sigourney Weaver",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_248": {
        "id": "ent_248",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What is the name of the AI in 2001: A Space Odyssey?",
        "options": ["HAL 9000", "GLaDOS", "Skynet", "JARVIS"],
        "correct_answer": "HAL 9000",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_257": {
        "id": "ent_257",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What is the name of the ship in Alien?",
        "options": ["Nostromo", "Sulaco", "Prometheus", "Covenant"],
        "correct_answer": "Nostromo",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_268": {
        "id": "ent_268",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In The Matrix Reloaded, what is the name of the Keymaker's city?",
        "options": ["The Source", "Zion", "The Matrix", "The Construct"],
        "correct_answer": "The Source",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_279": {
        "id": "ent_279",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What is the name of the hoverboard company in Back to the Future Part II?",
        "options": ["Mattel", "Griff's", "Texaco", "Cafe 80s"],
        "correct_answer": "Mattel",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_284": {
        "id": "ent_284",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Inception, what is the name of the device used to enter dreams?",
        "options": ["The PASIV", "The Totem", "The Architect", "The Extractor"],
        "correct_answer": "The PASIV",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },

    # Replace MARVEL questions (9 total: 6 non-Thor + 3 Thor)
    "ent_062": {
        "id": "ent_062",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "Who plays Sarah Connor in Terminator 2?",
        "options": ["Linda Hamilton", "Sigourney Weaver", "Jamie Lee Curtis", "Arnold Schwarzenegger"],
        "correct_answer": "Linda Hamilton",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_064": {
        "id": "ent_064",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of the prison in The Rock?",
        "options": ["Alcatraz", "San Quentin", "Rikers Island", "Sing Sing"],
        "correct_answer": "Alcatraz",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_065": {
        "id": "ent_065",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "Who plays Katniss Everdeen in The Hunger Games?",
        "options": ["Jennifer Lawrence", "Emma Stone", "Kristen Stewart", "Shailene Woodley"],
        "correct_answer": "Jennifer Lawrence",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_079": {
        "id": "ent_079",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "In Kill Bill, what is The Bride's real name?",
        "options": ["Beatrix Kiddo", "O-Ren Ishii", "Elle Driver", "Vernita Green"],
        "correct_answer": "Beatrix Kiddo",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_080": {
        "id": "ent_080",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of the organization in Salt?",
        "options": ["CIA", "KGB", "FBI", "NSA"],
        "correct_answer": "CIA",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_083": {
        "id": "ent_083",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "In Lethal Weapon, what are the main characters' last names?",
        "options": ["Riggs and Murtaugh", "Tango and Cash", "Turner and Hooch", "Butch and Sundance"],
        "correct_answer": "Riggs and Murtaugh",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_101": {
        "id": "ent_101",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What year was Speed released?",
        "options": ["1994", "1995", "1993", "1996"],
        "correct_answer": "1994",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    "ent_244": {
        "id": "ent_244",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Inception, what is Cobb's totem?",
        "options": ["A spinning top", "A chess piece", "A die", "A poker chip"],
        "correct_answer": "A spinning top",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    "ent_252": {
        "id": "ent_252",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In The Truman Show, what is Truman's job?",
        "options": ["Insurance salesman", "Teacher", "Banker", "Architect"],
        "correct_answer": "Insurance salesman",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },

    # Replace DC questions (2 total)
    "ent_081": {
        "id": "ent_081",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "Who plays Lara Croft in the 2001 Tomb Raider film?",
        "options": ["Angelina Jolie", "Alicia Vikander", "Milla Jovovich", "Charlize Theron"],
        "correct_answer": "Angelina Jolie",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    "ent_102": {
        "id": "ent_102",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "In Point Break, what extreme sport do the bank robbers participate in?",
        "options": ["Surfing", "Skydiving", "Snowboarding", "Rock climbing"],
        "correct_answer": "Surfing",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    }
}

def replace_expansion_overlaps():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    entertainment = data['categories']['Entertainment']

    replaced_count = 0
    for i, q in enumerate(entertainment):
        if q['id'] in replacements:
            entertainment[i] = replacements[q['id']]
            replaced_count += 1
            print(f"✅ Replaced {q['id']}: {replacements[q['id']]['question'][:70]}...")

    data['categories']['Entertainment'] = entertainment

    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n📊 Total questions replaced: {replaced_count}/69")
    print("\n🎯 Diversified Entertainment content:")
    print("   - Removed expansion franchise overlaps")
    print("   - Added TV animation (Simpsons, Family Guy, Avatar, etc.)")
    print("   - Added diverse action/adventure franchises")
    print("   - Added diverse sci-fi films")
    print("   - Added diverse drama/comedy shows")

if __name__ == '__main__':
    replace_expansion_overlaps()
