#!/usr/bin/env python3
"""Add 50 Video Games questions to reach 60 total"""
import json

new_questions = []

# Easy questions (17)
easy = [
    ("tec_034", "What is the name of Nintendo's iconic plumber?", ["Mario", "Luigi", "Wario", "Waluigi"], "Mario"),
    ("tec_035", "Which company created the PlayStation?", ["Sony", "Microsoft", "Nintendo", "Sega"], "Sony"),
    ("tec_036", "What is the name of Link's fairy companion in 'The Legend of Zelda: Ocarina of Time'?", ["Navi", "Tael", "Tatl", "Midna"], "Navi"),
    ("tec_037", "Which game features a blocky world made entirely of cubes?", ["Minecraft", "Roblox", "Terraria", "Fortnite"], "Minecraft"),
    ("tec_038", "What color is Sonic the Hedgehog?", ["Blue", "Red", "Green", "Yellow"], "Blue"),
    ("tec_039", "Which game series features Master Chief?", ["Halo", "Call of Duty", "Destiny", "Titanfall"], "Halo"),
    ("tec_040", "What is the maximum number of players in a standard Fortnite Battle Royale match?", ["100", "50", "150", "200"], "100"),
    ("tec_041", "Which company makes the Xbox?", ["Microsoft", "Sony", "Nintendo", "Sega"], "Microsoft"),
    ("tec_042", "What is Mario's profession?", ["Plumber", "Carpenter", "Doctor", "Chef"], "Plumber"),
    ("tec_043", "Which game involves catching creatures and battling them?", ["Pokémon", "Digimon", "Monster Hunter", "Yo-kai Watch"], "Pokémon"),
    ("tec_044", "What is the name of the princess Mario typically rescues?", ["Princess Peach", "Princess Daisy", "Princess Rosalina", "Princess Zelda"], "Princess Peach"),
    ("tec_045", "Which battle royale game features building mechanics?", ["Fortnite", "PUBG", "Apex Legends", "Warzone"], "Fortnite"),
    ("tec_046", "What company created Pac-Man?", ["Namco", "Atari", "Nintendo", "Sega"], "Namco"),
    ("tec_047", "Which game series is known for the phrase 'Finish Him'?", ["Mortal Kombat", "Street Fighter", "Tekken", "Soul Calibur"], "Mortal Kombat"),
    ("tec_048", "What is the currency called in Roblox?", ["Robux", "V-Bucks", "Coins", "Gems"], "Robux"),
    ("tec_049", "Which Nintendo console was released in 2017?", ["Nintendo Switch", "Wii U", "3DS", "Nintendo DS"], "Nintendo Switch"),
    ("tec_050", "What type of animal is Crash Bandicoot?", ["Bandicoot", "Fox", "Hedgehog", "Raccoon"], "Bandicoot"),
]

for q in easy:
    new_questions.append({"id": q[0], "category": "Technology", "subcategory": "Video Games", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "easy", "topic": None, "subtopic": None})

# Medium questions (17)
medium = [
    ("tec_051", "What year was the original Nintendo Entertainment System (NES) released in North America?", ["1985", "1983", "1987", "1990"], "1985"),
    ("tec_052", "Which game popularized the battle royale genre?", ["PlayerUnknown's Battlegrounds (PUBG)", "Fortnite", "Apex Legends", "H1Z1"], "PlayerUnknown's Battlegrounds (PUBG)"),
    ("tec_053", "What is the name of the main character in 'The Legend of Zelda' series?", ["Link", "Zelda", "Ganondorf", "Epona"], "Link"),
    ("tec_054", "Which company developed 'The Witcher 3: Wild Hunt'?", ["CD Projekt Red", "BioWare", "Bethesda", "Ubisoft"], "CD Projekt Red"),
    ("tec_055", "What was the first commercially successful video game?", ["Pong", "Space Invaders", "Pac-Man", "Asteroids"], "Pong"),
    ("tec_056", "Which game engine is used by 'Fortnite' and 'Gears of War'?", ["Unreal Engine", "Unity", "CryEngine", "Frostbite"], "Unreal Engine"),
    ("tec_057", "What is the best-selling video game of all time?", ["Minecraft", "Grand Theft Auto V", "Tetris", "Wii Sports"], "Minecraft"),
    ("tec_058", "Which Valve game introduced the Steam platform?", ["Half-Life 2", "Counter-Strike", "Portal", "Team Fortress 2"], "Half-Life 2"),
    ("tec_059", "What year did the original PlayStation release in Japan?", ["1994", "1995", "1996", "1997"], "1994"),
    ("tec_060", "Which game features the character Kratos?", ["God of War", "Devil May Cry", "Dante's Inferno", "Darksiders"], "God of War"),
    ("tec_061", "What is the name of the protagonist in the 'Half-Life' series?", ["Gordon Freeman", "Adrian Shephard", "Barney Calhoun", "Alyx Vance"], "Gordon Freeman"),
    ("tec_062", "Which fighting game series features Ryu and Ken?", ["Street Fighter", "Mortal Kombat", "Tekken", "King of Fighters"], "Street Fighter"),
    ("tec_063", "What does 'RPG' stand for in gaming?", ["Role-Playing Game", "Rocket Propelled Grenade", "Real Player Game", "Random Play Generator"], "Role-Playing Game"),
    ("tec_064", "Which game series is known for its tagline 'War. War never changes.'?", ["Fallout", "Call of Duty", "Battlefield", "Medal of Honor"], "Fallout"),
    ("tec_065", "What was Sega's mascot before Sonic?", ["Alex Kidd", "Ristar", "Vectorman", "Ecco the Dolphin"], "Alex Kidd"),
    ("tec_066", "Which game won Game of the Year at The Game Awards 2023?", ["Baldur's Gate 3", "The Legend of Zelda: Tears of the Kingdom", "Spider-Man 2", "Alan Wake 2"], "Baldur's Gate 3"),
    ("tec_067", "What company created League of Legends?", ["Riot Games", "Blizzard Entertainment", "Valve", "Epic Games"], "Riot Games"),
]

for q in medium:
    new_questions.append({"id": q[0], "category": "Technology", "subcategory": "Video Games", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "medium", "topic": None, "subtopic": None})

# Hard questions (16)
hard = [
    ("tec_068", "What was the code name for the Nintendo 64 during development?", ["Project Reality", "Dolphin", "Revolution", "Cafe"], "Project Reality"),
    ("tec_069", "Which game designer created Metal Gear Solid?", ["Hideo Kojima", "Shigeru Miyamoto", "Satoru Iwata", "Hideki Kamiya"], "Hideo Kojima"),
    ("tec_070", "What year did the video game crash of North America occur?", ["1983", "1980", "1985", "1982"], "1983"),
    ("tec_071", "Which indie game was created by Toby Fox?", ["Undertale", "Celeste", "Hollow Knight", "Stardew Valley"], "Undertale"),
    ("tec_072", "What is the name of the AI companion in 'Portal'?", ["GLaDOS", "Wheatley", "Cave Johnson", "Chell"], "GLaDOS"),
    ("tec_073", "Which game holds the record for most expensive game ever made?", ["Star Citizen (in development)", "Grand Theft Auto V", "Cyberpunk 2077", "Red Dead Redemption 2"], "Star Citizen (in development)"),
    ("tec_074", "What was the first game to feature a named playable female character?", ["Ms. Pac-Man", "Metroid", "Tomb Raider", "Resident Evil"], "Ms. Pac-Man"),
    ("tec_075", "Which game engine powers 'The Elder Scrolls V: Skyrim'?", ["Creation Engine", "Gamebryo", "Unreal Engine", "Unity"], "Creation Engine"),
    ("tec_076", "What is the maximum level in the original 'Pac-Man'?", ["256 (due to kill screen)", "255", "999", "Infinite"], "256 (due to kill screen)"),
    ("tec_077", "Which game was the first to use motion capture technology?", ["Prince of Persia (1989)", "Mortal Kombat", "Virtua Fighter", "Alone in the Dark"], "Prince of Persia (1989)"),
    ("tec_078", "What does 'FPS' stand for in gaming (both meanings)?", ["First-Person Shooter and Frames Per Second", "First Player Start", "Full Performance System", "Fast Paced Strategy"], "First-Person Shooter and Frames Per Second"),
    ("tec_079", "Which game creator is known as the 'father of video games'?", ["Ralph Baer", "Nolan Bushnell", "Shigeru Miyamoto", "Sid Meier"], "Ralph Baer"),
    ("tec_080", "What was the first video game played in space?", ["Tetris", "Pong", "Game Boy games", "Space Invaders"], "Tetris"),
    ("tec_081", "Which game series popularized the 'New Game Plus' feature?", ["Chrono Trigger", "Final Fantasy VII", "The Legend of Zelda", "Super Mario Bros."], "Chrono Trigger"),
    ("tec_082", "What is the Konami Code?", ["Up, Up, Down, Down, Left, Right, Left, Right, B, A", "Up, Down, Left, Right, A, B", "A, B, A, B, Up, Down", "Left, Right, Up, Down, Start"], "Up, Up, Down, Down, Left, Right, Left, Right, B, A"),
    ("tec_083", "Which game featured the first true open world?", ["Elite (1984)", "Grand Theft Auto III", "The Legend of Zelda", "Ultima"], "Elite (1984)"),
]

for q in hard:
    new_questions.append({"id": q[0], "category": "Technology", "subcategory": "Video Games", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "hard", "topic": None, "subtopic": None})

# Load, add, sort, save
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

data['categories']['Technology'].extend(new_questions)
data['categories']['Technology'].sort(key=lambda q: int(q['id'].split('_')[1]))

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added 50 Video Games questions")
print(f"Technology now has {len(data['categories']['Technology'])} total questions")
print(f"Added: 17 easy, 17 medium, 16 hard")
