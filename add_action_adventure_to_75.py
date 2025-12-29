#!/usr/bin/env python3
"""Add 55 Action/Adventure questions to reach 75 total (ent_052 to ent_106)"""
import json

new_questions = [
    # EASY QUESTIONS (18 total)
    {
        "id": "ent_052",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of Indiana Jones' signature weapon?",
        "options": ["Whip", "Sword", "Gun", "Lasso"],
        "correct_answer": "Whip",
        "difficulty": "easy"
    },
    {
        "id": "ent_053",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What color pill does Neo take in The Matrix?",
        "options": ["Red", "Blue", "Green", "Yellow"],
        "correct_answer": "Red",
        "difficulty": "easy"
    },
    {
        "id": "ent_054",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of the theme park in Jurassic Park?",
        "options": ["Jurassic Park", "Dino World", "Dinosaur Island", "Prehistoric Park"],
        "correct_answer": "Jurassic Park",
        "difficulty": "easy"
    },
    {
        "id": "ent_055",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is James Bond's code number?",
        "options": ["007", "006", "001", "008"],
        "correct_answer": "007",
        "difficulty": "easy"
    },
    {
        "id": "ent_056",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of the ship in Pirates of the Caribbean?",
        "options": ["The Black Pearl", "The Flying Dutchman", "The Queen Anne's Revenge", "The Jolly Roger"],
        "correct_answer": "The Black Pearl",
        "difficulty": "easy"
    },
    {
        "id": "ent_057",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "Who plays Ethan Hunt in the Mission: Impossible series?",
        "options": ["Tom Cruise", "Brad Pitt", "Matt Damon", "Tom Hardy"],
        "correct_answer": "Tom Cruise",
        "difficulty": "easy"
    },
    {
        "id": "ent_058",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of the killer shark in Jaws?",
        "options": ["Bruce", "Jaws", "Chomper", "Big Blue"],
        "correct_answer": "Bruce",
        "difficulty": "easy"
    },
    {
        "id": "ent_059",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "Who is the villain in Die Hard?",
        "options": ["Hans Gruber", "Simon Gruber", "John McClane", "Karl Vreski"],
        "correct_answer": "Hans Gruber",
        "difficulty": "easy"
    },
    {
        "id": "ent_060",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of the cyborg assassin in The Terminator?",
        "options": ["T-800", "T-1000", "T-X", "T-3000"],
        "correct_answer": "T-800",
        "difficulty": "easy"
    },
    {
        "id": "ent_061",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "Who plays John Wick?",
        "options": ["Keanu Reeves", "Jason Statham", "Liam Neeson", "Dwayne Johnson"],
        "correct_answer": "Keanu Reeves",
        "difficulty": "easy"
    },
    {
        "id": "ent_062",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of the Hulk's alter ego?",
        "options": ["Bruce Banner", "Tony Stark", "Steve Rogers", "Peter Parker"],
        "correct_answer": "Bruce Banner",
        "difficulty": "easy"
    },
    {
        "id": "ent_063",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is Superman's weakness?",
        "options": ["Kryptonite", "Magic", "Red sun radiation", "Lead"],
        "correct_answer": "Kryptonite",
        "difficulty": "easy"
    },
    {
        "id": "ent_064",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "Who is the main villain in Avengers: Endgame?",
        "options": ["Thanos", "Loki", "Ultron", "Red Skull"],
        "correct_answer": "Thanos",
        "difficulty": "easy"
    },
    {
        "id": "ent_065",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of Thor's hammer?",
        "options": ["Mjolnir", "Stormbreaker", "Gungnir", "Jarnbjorn"],
        "correct_answer": "Mjolnir",
        "difficulty": "easy"
    },
    {
        "id": "ent_066",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "Who is Spider-Man's love interest in the original trilogy?",
        "options": ["Mary Jane Watson", "Gwen Stacy", "Felicia Hardy", "Betty Brant"],
        "correct_answer": "Mary Jane Watson",
        "difficulty": "easy"
    },
    {
        "id": "ent_067",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of Captain Jack Sparrow's ship?",
        "options": ["Black Pearl", "Flying Dutchman", "Queen Anne's Revenge", "Silent Mary"],
        "correct_answer": "Black Pearl",
        "difficulty": "easy"
    },
    {
        "id": "ent_068",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "Who plays Jason Bourne in the Bourne series?",
        "options": ["Matt Damon", "Jeremy Renner", "Brad Pitt", "George Clooney"],
        "correct_answer": "Matt Damon",
        "difficulty": "easy"
    },
    {
        "id": "ent_069",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What vehicle does Dominic Toretto drive in The Fast and the Furious?",
        "options": ["Dodge Charger", "Nissan Skyline", "Toyota Supra", "Mazda RX-7"],
        "correct_answer": "Dodge Charger",
        "difficulty": "easy"
    },

    # MEDIUM QUESTIONS (22 total)
    {
        "id": "ent_070",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "In which film does Indiana Jones search for the Holy Grail?",
        "options": ["Indiana Jones and the Last Crusade", "Raiders of the Lost Ark", "Indiana Jones and the Temple of Doom", "Indiana Jones and the Kingdom of the Crystal Skull"],
        "correct_answer": "Indiana Jones and the Last Crusade",
        "difficulty": "medium"
    },
    {
        "id": "ent_071",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of the artificial intelligence system in The Matrix?",
        "options": ["The Architect", "The Oracle", "Agent Smith", "The Machines"],
        "correct_answer": "The Architect",
        "difficulty": "medium"
    },
    {
        "id": "ent_072",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of the island where Jurassic Park is located?",
        "options": ["Isla Nublar", "Isla Sorna", "Isla Muerta", "Isla Pena"],
        "correct_answer": "Isla Nublar",
        "difficulty": "medium"
    },
    {
        "id": "ent_073",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "Who is the first actor to play James Bond in a film?",
        "options": ["Sean Connery", "Roger Moore", "Pierce Brosnan", "Daniel Craig"],
        "correct_answer": "Sean Connery",
        "difficulty": "medium"
    },
    {
        "id": "ent_074",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of the cursed pirate captain in Pirates of the Caribbean?",
        "options": ["Captain Barbossa", "Davy Jones", "Captain Salazar", "Blackbeard"],
        "correct_answer": "Captain Barbossa",
        "difficulty": "medium"
    },
    {
        "id": "ent_075",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "In which city does Die Hard take place?",
        "options": ["Los Angeles", "New York", "Chicago", "San Francisco"],
        "correct_answer": "Los Angeles",
        "difficulty": "medium"
    },
    {
        "id": "ent_076",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of the resistance leader in The Terminator series?",
        "options": ["John Connor", "Kyle Reese", "Sarah Connor", "Marcus Wright"],
        "correct_answer": "John Connor",
        "difficulty": "medium"
    },
    {
        "id": "ent_077",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What was John Wick's job before retirement?",
        "options": ["Assassin", "Bounty Hunter", "Private Detective", "Bodyguard"],
        "correct_answer": "Assassin",
        "difficulty": "medium"
    },
    {
        "id": "ent_078",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of the mineral that weakens Superman?",
        "options": ["Kryptonite", "Adamantium", "Vibranium", "Promethium"],
        "correct_answer": "Kryptonite",
        "difficulty": "medium"
    },
    {
        "id": "ent_079",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of Black Panther's kingdom?",
        "options": ["Wakanda", "Genosha", "Latveria", "Atlantis"],
        "correct_answer": "Wakanda",
        "difficulty": "medium"
    },
    {
        "id": "ent_080",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "In which Avengers film does the team first assemble?",
        "options": ["The Avengers (2012)", "Avengers: Age of Ultron", "Captain America: Civil War", "Avengers: Infinity War"],
        "correct_answer": "The Avengers (2012)",
        "difficulty": "medium"
    },
    {
        "id": "ent_081",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of Wonder Woman's home island?",
        "options": ["Themyscira", "Paradise Island", "Olympus", "Amazon Isle"],
        "correct_answer": "Themyscira",
        "difficulty": "medium"
    },
    {
        "id": "ent_082",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "Who created the character of Batman?",
        "options": ["Bob Kane and Bill Finger", "Stan Lee and Jack Kirby", "Jerry Siegel and Joe Shuster", "Jim Lee and Frank Miller"],
        "correct_answer": "Bob Kane and Bill Finger",
        "difficulty": "medium"
    },
    {
        "id": "ent_083",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of the high-tech suit Tony Stark wears?",
        "options": ["Iron Man suit", "War Machine", "Iron Patriot", "Rescue"],
        "correct_answer": "Iron Man suit",
        "difficulty": "medium"
    },
    {
        "id": "ent_084",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What year was the first Mad Max film released?",
        "options": ["1979", "1981", "1985", "1977"],
        "correct_answer": "1979",
        "difficulty": "medium"
    },
    {
        "id": "ent_085",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "Who directed the original Alien film?",
        "options": ["Ridley Scott", "James Cameron", "David Fincher", "Jean-Pierre Jeunet"],
        "correct_answer": "Ridley Scott",
        "difficulty": "medium"
    },
    {
        "id": "ent_086",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of the villainous organization in Mission: Impossible?",
        "options": ["The Syndicate", "SPECTRE", "HYDRA", "The Collective"],
        "correct_answer": "The Syndicate",
        "difficulty": "medium"
    },
    {
        "id": "ent_087",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "In which country does most of Skyfall take place?",
        "options": ["Scotland", "England", "Turkey", "China"],
        "correct_answer": "Scotland",
        "difficulty": "medium"
    },
    {
        "id": "ent_088",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of the company that creates dinosaurs in Jurassic Park?",
        "options": ["InGen", "Biosyn", "Mantah Corp", "Masrani Global"],
        "correct_answer": "InGen",
        "difficulty": "medium"
    },
    {
        "id": "ent_089",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "Who plays Ellen Ripley in the Alien franchise?",
        "options": ["Sigourney Weaver", "Linda Hamilton", "Jamie Lee Curtis", "Carrie Fisher"],
        "correct_answer": "Sigourney Weaver",
        "difficulty": "medium"
    },
    {
        "id": "ent_090",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of the virtual training program in The Matrix?",
        "options": ["The Construct", "The Dojo", "The Simulation", "The Grid"],
        "correct_answer": "The Construct",
        "difficulty": "medium"
    },
    {
        "id": "ent_091",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "Who is the main antagonist in John Wick: Chapter 3?",
        "options": ["The High Table", "Viggo Tarasov", "Santino D'Antonio", "Iosef Tarasov"],
        "correct_answer": "The High Table",
        "difficulty": "medium"
    },

    # HARD QUESTIONS (15 total)
    {
        "id": "ent_092",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of Indiana Jones' father?",
        "options": ["Henry Jones Sr.", "Marcus Brody", "Sallah", "Walter Donovan"],
        "correct_answer": "Henry Jones Sr.",
        "difficulty": "hard"
    },
    {
        "id": "ent_093",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "In The Matrix, what is the name of the ship captained by Morpheus?",
        "options": ["Nebuchadnezzar", "Logos", "Mjolnir", "Osiris"],
        "correct_answer": "Nebuchadnezzar",
        "difficulty": "hard"
    },
    {
        "id": "ent_094",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of the mathematician who first predicted chaos theory in Jurassic Park?",
        "options": ["Dr. Ian Malcolm", "Dr. Alan Grant", "Dr. Ellie Sattler", "Dr. Henry Wu"],
        "correct_answer": "Dr. Ian Malcolm",
        "difficulty": "hard"
    },
    {
        "id": "ent_095",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What was the code name for James Bond's first mission as 007?",
        "options": ["Casino Royale", "Dr. No", "From Russia with Love", "Goldfinger"],
        "correct_answer": "Casino Royale",
        "difficulty": "hard"
    },
    {
        "id": "ent_096",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of the goddess imprisoned in Davy Jones' heart in Pirates of the Caribbean?",
        "options": ["Calypso", "Tia Dalma", "Circe", "Medusa"],
        "correct_answer": "Calypso",
        "difficulty": "hard"
    },
    {
        "id": "ent_097",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of the building where Die Hard takes place?",
        "options": ["Nakatomi Plaza", "Willis Tower", "Empire State Building", "Chrysler Building"],
        "correct_answer": "Nakatomi Plaza",
        "difficulty": "hard"
    },
    {
        "id": "ent_098",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "In The Terminator, what year does Kyle Reese travel from?",
        "options": ["2029", "2027", "2018", "2035"],
        "correct_answer": "2029",
        "difficulty": "hard"
    },
    {
        "id": "ent_099",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What was the name of John Wick's wife?",
        "options": ["Helen", "Sarah", "Maria", "Anna"],
        "correct_answer": "Helen",
        "difficulty": "hard"
    },
    {
        "id": "ent_100",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of the planet Superman is from?",
        "options": ["Krypton", "Oa", "Thanagar", "Rann"],
        "correct_answer": "Krypton",
        "difficulty": "hard"
    },
    {
        "id": "ent_101",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "In Avengers: Endgame, what is the name of the quantum realm device?",
        "options": ["Quantum Tunnel", "Quantum Bridge", "Quantum Portal", "Quantum Gate"],
        "correct_answer": "Quantum Tunnel",
        "difficulty": "hard"
    },
    {
        "id": "ent_102",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the real name of the Joker's girlfriend Harley Quinn?",
        "options": ["Harleen Quinzel", "Holly Quinn", "Harper Quinzel", "Harriet Quinn"],
        "correct_answer": "Harleen Quinzel",
        "difficulty": "hard"
    },
    {
        "id": "ent_103",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of the desert wasteland in Mad Max: Fury Road?",
        "options": ["The Wasteland", "The Citadel", "Bullet Farm", "Gas Town"],
        "correct_answer": "The Wasteland",
        "difficulty": "hard"
    },
    {
        "id": "ent_104",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "In Alien, what is the name of the spaceship where the crew encounters the xenomorph?",
        "options": ["Nostromo", "Sulaco", "Prometheus", "Covenant"],
        "correct_answer": "Nostromo",
        "difficulty": "hard"
    },
    {
        "id": "ent_105",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "What is the name of Jason Bourne's real identity?",
        "options": ["David Webb", "John Michael Kane", "Richard Chamberlain", "Paul Greengrass"],
        "correct_answer": "David Webb",
        "difficulty": "hard"
    },
    {
        "id": "ent_106",
        "category": "Entertainment",
        "subcategory": "Action/Adventure",
        "question": "In The Fast and the Furious, what is the name of Brian O'Conner's FBI handler?",
        "options": ["Special Agent Bilkins", "Agent Hobbs", "Agent Shaw", "Agent Stasiak"],
        "correct_answer": "Special Agent Bilkins",
        "difficulty": "hard"
    }
]

def add_action_adventure_questions():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    # Add new questions
    data['categories']['Entertainment'].extend(new_questions)

    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Added {len(new_questions)} Action/Adventure questions")
    print(f"   Easy: {sum(1 for q in new_questions if q['difficulty'] == 'easy')}")
    print(f"   Medium: {sum(1 for q in new_questions if q['difficulty'] == 'medium')}")
    print(f"   Hard: {sum(1 for q in new_questions if q['difficulty'] == 'hard')}")
    print(f"\n📊 Action/Adventure now has 75 total questions (20 → 75)")

if __name__ == '__main__':
    add_action_adventure_questions()
