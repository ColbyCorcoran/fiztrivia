#!/usr/bin/env python3
"""Add 64 Sci-Fi/Fantasy questions to reach 75 total (ent_237 to ent_300)"""
import json

new_questions = [
    # EASY QUESTIONS (21 total)
    {
        "id": "ent_237",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What is the name of the hobbit who carries the One Ring in Lord of the Rings?",
        "options": ["Frodo Baggins", "Bilbo Baggins", "Samwise Gamgee", "Merry Brandybuck"],
        "correct_answer": "Frodo Baggins",
        "difficulty": "easy"
    },
    {
        "id": "ent_238",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What is the name of the starship in Star Trek?",
        "options": ["USS Enterprise", "USS Voyager", "USS Discovery", "USS Defiant"],
        "correct_answer": "USS Enterprise",
        "difficulty": "easy"
    },
    {
        "id": "ent_239",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Game of Thrones, what are the undead creatures called?",
        "options": ["White Walkers", "Wights", "Wildlings", "Walkers"],
        "correct_answer": "White Walkers",
        "difficulty": "easy"
    },
    {
        "id": "ent_240",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What house does Harry Potter belong to at Hogwarts?",
        "options": ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"],
        "correct_answer": "Gryffindor",
        "difficulty": "easy"
    },
    {
        "id": "ent_241",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What time-traveling vehicle is used in Back to the Future?",
        "options": ["DeLorean", "TARDIS", "Time Machine", "Phone Booth"],
        "correct_answer": "DeLorean",
        "difficulty": "easy"
    },
    {
        "id": "ent_242",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "Who plays Luke Skywalker in Star Wars?",
        "options": ["Mark Hamill", "Harrison Ford", "Alec Guinness", "Carrie Fisher"],
        "correct_answer": "Mark Hamill",
        "difficulty": "easy"
    },
    {
        "id": "ent_243",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What is the name of the wizard in Lord of the Rings?",
        "options": ["Gandalf", "Saruman", "Radagast", "Merlin"],
        "correct_answer": "Gandalf",
        "difficulty": "easy"
    },
    {
        "id": "ent_244",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What is the name of Thor's brother in the Marvel films?",
        "options": ["Loki", "Odin", "Heimdall", "Balder"],
        "correct_answer": "Loki",
        "difficulty": "easy"
    },
    {
        "id": "ent_245",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What is the name of the time machine in Doctor Who?",
        "options": ["TARDIS", "DeLorean", "Time Turner", "Sonic Screwdriver"],
        "correct_answer": "TARDIS",
        "difficulty": "easy"
    },
    {
        "id": "ent_246",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "Who is Harry Potter's best friend?",
        "options": ["Ron Weasley", "Hermione Granger", "Neville Longbottom", "Draco Malfoy"],
        "correct_answer": "Ron Weasley",
        "difficulty": "easy"
    },
    {
        "id": "ent_247",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What is the name of the dark lord in Lord of the Rings?",
        "options": ["Sauron", "Saruman", "Morgoth", "Gandalf"],
        "correct_answer": "Sauron",
        "difficulty": "easy"
    },
    {
        "id": "ent_248",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What is the name of the first Star Wars film released?",
        "options": ["A New Hope", "The Empire Strikes Back", "The Phantom Menace", "Return of the Jedi"],
        "correct_answer": "A New Hope",
        "difficulty": "easy"
    },
    {
        "id": "ent_249",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "Who is the headmaster of Hogwarts in Harry Potter?",
        "options": ["Albus Dumbledore", "Severus Snape", "Minerva McGonagall", "Rubeus Hagrid"],
        "correct_answer": "Albus Dumbledore",
        "difficulty": "easy"
    },
    {
        "id": "ent_250",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What is the name of the dragon in The Hobbit?",
        "options": ["Smaug", "Drogon", "Viserion", "Rhaegal"],
        "correct_answer": "Smaug",
        "difficulty": "easy"
    },
    {
        "id": "ent_251",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "Who plays Captain Kirk in the original Star Trek series?",
        "options": ["William Shatner", "Leonard Nimoy", "Patrick Stewart", "Chris Pine"],
        "correct_answer": "William Shatner",
        "difficulty": "easy"
    },
    {
        "id": "ent_252",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What is the name of the villain in Harry Potter?",
        "options": ["Lord Voldemort", "Severus Snape", "Lucius Malfoy", "Bellatrix Lestrange"],
        "correct_answer": "Lord Voldemort",
        "difficulty": "easy"
    },
    {
        "id": "ent_253",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What speed must the DeLorean reach to time travel in Back to the Future?",
        "options": ["88 mph", "100 mph", "77 mph", "99 mph"],
        "correct_answer": "88 mph",
        "difficulty": "easy"
    },
    {
        "id": "ent_254",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What is the name of the Iron Throne kingdom in Game of Thrones?",
        "options": ["Westeros", "Essos", "The Seven Kingdoms", "King's Landing"],
        "correct_answer": "The Seven Kingdoms",
        "difficulty": "easy"
    },
    {
        "id": "ent_255",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "Who plays Mr. Spock in the original Star Trek?",
        "options": ["Leonard Nimoy", "William Shatner", "DeForest Kelley", "Zachary Quinto"],
        "correct_answer": "Leonard Nimoy",
        "difficulty": "easy"
    },
    {
        "id": "ent_256",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What is the name of the precious artifact in Lord of the Rings?",
        "options": ["The One Ring", "The Ring of Power", "The Master Ring", "The Golden Ring"],
        "correct_answer": "The One Ring",
        "difficulty": "easy"
    },
    {
        "id": "ent_257",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What color is Yoda's lightsaber in Star Wars?",
        "options": ["Green", "Blue", "Purple", "Red"],
        "correct_answer": "Green",
        "difficulty": "easy"
    },

    # MEDIUM QUESTIONS (26 total)
    {
        "id": "ent_258",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Lord of the Rings, what is the name of Aragorn's sword?",
        "options": ["Andúril", "Sting", "Glamdring", "Orcrist"],
        "correct_answer": "Andúril",
        "difficulty": "medium"
    },
    {
        "id": "ent_259",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What is the name of the desert planet in Star Wars?",
        "options": ["Tatooine", "Hoth", "Dagobah", "Endor"],
        "correct_answer": "Tatooine",
        "difficulty": "medium"
    },
    {
        "id": "ent_260",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Game of Thrones, what is the name of Jon Snow's direwolf?",
        "options": ["Ghost", "Grey Wind", "Summer", "Shaggydog"],
        "correct_answer": "Ghost",
        "difficulty": "medium"
    },
    {
        "id": "ent_261",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What is the name of Harry Potter's pet owl?",
        "options": ["Hedwig", "Errol", "Pigwidgeon", "Fawkes"],
        "correct_answer": "Hedwig",
        "difficulty": "medium"
    },
    {
        "id": "ent_262",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Star Trek, what is Mr. Spock's home planet?",
        "options": ["Vulcan", "Earth", "Romulus", "Qo'noS"],
        "correct_answer": "Vulcan",
        "difficulty": "medium"
    },
    {
        "id": "ent_263",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What year does Marty McFly travel to in Back to the Future?",
        "options": ["1955", "1985", "2015", "1885"],
        "correct_answer": "1955",
        "difficulty": "medium"
    },
    {
        "id": "ent_264",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Lord of the Rings, what is the name of the elf who joins the Fellowship?",
        "options": ["Legolas", "Elrond", "Galadriel", "Arwen"],
        "correct_answer": "Legolas",
        "difficulty": "medium"
    },
    {
        "id": "ent_265",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What is the name of the Stark family home in Game of Thrones?",
        "options": ["Winterfell", "King's Landing", "Casterly Rock", "The Eyrie"],
        "correct_answer": "Winterfell",
        "difficulty": "medium"
    },
    {
        "id": "ent_266",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Harry Potter, what position does Harry play in Quidditch?",
        "options": ["Seeker", "Keeper", "Chaser", "Beater"],
        "correct_answer": "Seeker",
        "difficulty": "medium"
    },
    {
        "id": "ent_267",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "Who directed The Lord of the Rings trilogy?",
        "options": ["Peter Jackson", "Christopher Nolan", "James Cameron", "George Lucas"],
        "correct_answer": "Peter Jackson",
        "difficulty": "medium"
    },
    {
        "id": "ent_268",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Star Wars, what is the name of the bounty hunter who captured Han Solo?",
        "options": ["Boba Fett", "Jango Fett", "Greedo", "Bossk"],
        "correct_answer": "Boba Fett",
        "difficulty": "medium"
    },
    {
        "id": "ent_269",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What is the name of the AI computer in 2001: A Space Odyssey?",
        "options": ["HAL 9000", "JARVIS", "Skynet", "VIKI"],
        "correct_answer": "HAL 9000",
        "difficulty": "medium"
    },
    {
        "id": "ent_270",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Doctor Who, what is the Doctor's home planet?",
        "options": ["Gallifrey", "Skaro", "Trenzalore", "Earth"],
        "correct_answer": "Gallifrey",
        "difficulty": "medium"
    },
    {
        "id": "ent_271",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Harry Potter, what is the name of the prison guarded by Dementors?",
        "options": ["Azkaban", "Nurmengard", "The Tower", "The Dungeon"],
        "correct_answer": "Azkaban",
        "difficulty": "medium"
    },
    {
        "id": "ent_272",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What is the name of the shire where hobbits live in Lord of the Rings?",
        "options": ["The Shire", "Hobbiton", "Bag End", "Rivendell"],
        "correct_answer": "The Shire",
        "difficulty": "medium"
    },
    {
        "id": "ent_273",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Star Trek: The Next Generation, who is the captain of the Enterprise?",
        "options": ["Jean-Luc Picard", "James T. Kirk", "Benjamin Sisko", "Kathryn Janeway"],
        "correct_answer": "Jean-Luc Picard",
        "difficulty": "medium"
    },
    {
        "id": "ent_274",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Game of Thrones, what is the motto of House Stark?",
        "options": ["Winter is Coming", "Hear Me Roar", "Fire and Blood", "Ours is the Fury"],
        "correct_answer": "Winter is Coming",
        "difficulty": "medium"
    },
    {
        "id": "ent_275",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What is the name of the desert planet in Dune?",
        "options": ["Arrakis", "Caladan", "Giedi Prime", "Kaitain"],
        "correct_answer": "Arrakis",
        "difficulty": "medium"
    },
    {
        "id": "ent_276",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Back to the Future, what is the name of Doc Brown's time-traveling train?",
        "options": ["The Time Train", "The DeLorean Train", "The Jules Verne Train", "The Steam Time Machine"],
        "correct_answer": "The Jules Verne Train",
        "difficulty": "medium"
    },
    {
        "id": "ent_277",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Harry Potter, what does the spell 'Expelliarmus' do?",
        "options": ["Disarms an opponent", "Summons objects", "Creates light", "Unlocks doors"],
        "correct_answer": "Disarms an opponent",
        "difficulty": "medium"
    },
    {
        "id": "ent_278",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What is the name of the black monolith in 2001: A Space Odyssey?",
        "options": ["The Monolith", "TMA-1", "Discovery", "Jupiter"],
        "correct_answer": "TMA-1",
        "difficulty": "medium"
    },
    {
        "id": "ent_279",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Star Wars, what is the name of the Death Star's weakness?",
        "options": ["Thermal exhaust port", "Power core", "Shield generator", "Reactor"],
        "correct_answer": "Thermal exhaust port",
        "difficulty": "medium"
    },
    {
        "id": "ent_280",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Lord of the Rings, what creature is Gollum?",
        "options": ["Hobbit (corrupted)", "Orc", "Troll", "Goblin"],
        "correct_answer": "Hobbit (corrupted)",
        "difficulty": "medium"
    },
    {
        "id": "ent_281",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "What is the name of the dragon mother in Game of Thrones?",
        "options": ["Daenerys Targaryen", "Cersei Lannister", "Arya Stark", "Sansa Stark"],
        "correct_answer": "Daenerys Targaryen",
        "difficulty": "medium"
    },
    {
        "id": "ent_282",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Interstellar, what is the name of the robot?",
        "options": ["TARS", "CASE", "HAL", "JARVIS"],
        "correct_answer": "TARS",
        "difficulty": "medium"
    },
    {
        "id": "ent_283",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "Who plays Gandalf in The Lord of the Rings films?",
        "options": ["Ian McKellen", "Christopher Lee", "Viggo Mortensen", "Sean Bean"],
        "correct_answer": "Ian McKellen",
        "difficulty": "medium"
    },

    # HARD QUESTIONS (17 total)
    {
        "id": "ent_284",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Star Wars, what is the name of Anakin Skywalker's mother?",
        "options": ["Shmi Skywalker", "Padmé Amidala", "Leia Organa", "Mon Mothma"],
        "correct_answer": "Shmi Skywalker",
        "difficulty": "hard"
    },
    {
        "id": "ent_285",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Lord of the Rings, what is the name of the language spoken by elves?",
        "options": ["Sindarin", "Quenya", "Both A and B", "Elvish"],
        "correct_answer": "Both A and B",
        "difficulty": "hard"
    },
    {
        "id": "ent_286",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Game of Thrones, what is the name of the ancestral Valyrian steel sword of House Stark?",
        "options": ["Ice", "Longclaw", "Oathkeeper", "Widow's Wail"],
        "correct_answer": "Ice",
        "difficulty": "hard"
    },
    {
        "id": "ent_287",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Harry Potter, what is the name of the potion that grants luck?",
        "options": ["Felix Felicis", "Polyjuice Potion", "Amortentia", "Veritaserum"],
        "correct_answer": "Felix Felicis",
        "difficulty": "hard"
    },
    {
        "id": "ent_288",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Star Trek, what is the Prime Directive?",
        "options": ["Non-interference with less advanced civilizations", "Always help those in need", "Explore strange new worlds", "Seek out new life"],
        "correct_answer": "Non-interference with less advanced civilizations",
        "difficulty": "hard"
    },
    {
        "id": "ent_289",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Dune, what is the name of the spice that extends life?",
        "options": ["Melange", "Spice Melange", "The Spice", "Geriatric Spice"],
        "correct_answer": "Melange",
        "difficulty": "hard"
    },
    {
        "id": "ent_290",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Back to the Future, what is Doc Brown's first name?",
        "options": ["Emmett", "Edward", "Ernest", "Elijah"],
        "correct_answer": "Emmett",
        "difficulty": "hard"
    },
    {
        "id": "ent_291",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Lord of the Rings, what is the name of the tower where Sauron resides?",
        "options": ["Barad-dûr", "Orthanc", "Minas Morgul", "Cirith Ungol"],
        "correct_answer": "Barad-dûr",
        "difficulty": "hard"
    },
    {
        "id": "ent_292",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Harry Potter, what are the three Deathly Hallows?",
        "options": ["Elder Wand, Resurrection Stone, Invisibility Cloak", "Philosopher's Stone, Sword of Gryffindor, Time Turner", "Elder Wand, Horcrux, Invisibility Cloak", "Resurrection Stone, Marauder's Map, Sorting Hat"],
        "correct_answer": "Elder Wand, Resurrection Stone, Invisibility Cloak",
        "difficulty": "hard"
    },
    {
        "id": "ent_293",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Star Wars, what is the name of the Sith homeworld?",
        "options": ["Korriban", "Mustafar", "Exegol", "Moraband"],
        "correct_answer": "Korriban",
        "difficulty": "hard"
    },
    {
        "id": "ent_294",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Game of Thrones, what is the name of the capital city of the Seven Kingdoms?",
        "options": ["King's Landing", "Winterfell", "Oldtown", "Dragonstone"],
        "correct_answer": "King's Landing",
        "difficulty": "hard"
    },
    {
        "id": "ent_295",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Doctor Who, what is the Doctor's time machine called?",
        "options": ["TARDIS", "Type 40", "Police Box", "Sonic Screwdriver"],
        "correct_answer": "TARDIS",
        "difficulty": "hard"
    },
    {
        "id": "ent_296",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In The Hobbit, what is Bilbo's last name?",
        "options": ["Baggins", "Took", "Gamgee", "Brandybuck"],
        "correct_answer": "Baggins",
        "difficulty": "hard"
    },
    {
        "id": "ent_297",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Star Trek, what is the Vulcan greeting?",
        "options": ["Live long and prosper", "Peace and long life", "May you live long", "Greetings"],
        "correct_answer": "Live long and prosper",
        "difficulty": "hard"
    },
    {
        "id": "ent_298",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Interstellar, what is the name of the planet with massive tidal waves?",
        "options": ["Miller's Planet", "Mann's Planet", "Edmund's Planet", "Cooper Station"],
        "correct_answer": "Miller's Planet",
        "difficulty": "hard"
    },
    {
        "id": "ent_299",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Lord of the Rings, what is the name of the king who returns?",
        "options": ["Aragorn", "Théoden", "Denethor", "Elrond"],
        "correct_answer": "Aragorn",
        "difficulty": "hard"
    },
    {
        "id": "ent_300",
        "category": "Entertainment",
        "subcategory": "Sci-Fi/Fantasy",
        "question": "In Harry Potter, what is the core of Harry's wand?",
        "options": ["Phoenix feather", "Dragon heartstring", "Unicorn hair", "Thestral tail hair"],
        "correct_answer": "Phoenix feather",
        "difficulty": "hard"
    }
]

def add_sci_fi_fantasy_questions():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    # Add new questions
    data['categories']['Entertainment'].extend(new_questions)

    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Added {len(new_questions)} Sci-Fi/Fantasy questions")
    print(f"   Easy: {sum(1 for q in new_questions if q['difficulty'] == 'easy')}")
    print(f"   Medium: {sum(1 for q in new_questions if q['difficulty'] == 'medium')}")
    print(f"   Hard: {sum(1 for q in new_questions if q['difficulty'] == 'hard')}")
    print(f"\n📊 Sci-Fi/Fantasy now has 75 total questions (11 → 75)")
    print(f"🎉 Entertainment category COMPLETE: 300 total questions!")

if __name__ == '__main__':
    add_sci_fi_fantasy_questions()
