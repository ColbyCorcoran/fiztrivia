#!/usr/bin/env python3
"""Add 55 Maps & Borders questions to reach 60 total"""
import json

# 55 new Maps & Borders questions (18 easy, 19 medium, 18 hard)
new_questions = [
    # EASY (18 questions)
    {
        "id": "geo_068",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What imaginary line divides the Earth into Northern and Southern hemispheres?",
        "options": ["Equator", "Prime Meridian", "Tropic of Cancer", "International Date Line"],
        "correct_answer": "Equator",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_069",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What is the line of longitude at 0 degrees called?",
        "options": ["Prime Meridian", "Equator", "Tropic of Capricorn", "Arctic Circle"],
        "correct_answer": "Prime Meridian",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_070",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which country shares the longest border with the United States?",
        "options": ["Canada", "Mexico", "Russia", "Cuba"],
        "correct_answer": "Canada",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_071",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "How many countries border France?",
        "options": ["8", "6", "5", "10"],
        "correct_answer": "8",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_072",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What line of latitude is located at 23.5 degrees north?",
        "options": ["Tropic of Cancer", "Tropic of Capricorn", "Arctic Circle", "Antarctic Circle"],
        "correct_answer": "Tropic of Cancer",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_073",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which two countries share the Iberian Peninsula?",
        "options": ["Spain and Portugal", "France and Spain", "Italy and France", "Greece and Turkey"],
        "correct_answer": "Spain and Portugal",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_074",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What is the name of the line that divides North and South Korea?",
        "options": ["38th Parallel", "Mason-Dixon Line", "49th Parallel", "Maginot Line"],
        "correct_answer": "38th Parallel",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_075",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which ocean borders Africa's western coast?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Southern Ocean"],
        "correct_answer": "Atlantic Ocean",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_076",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "How many time zones does China officially use?",
        "options": ["1", "5", "3", "7"],
        "correct_answer": "1",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_077",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which continent is divided by the equator almost in half?",
        "options": ["Africa", "South America", "Asia", "Australia"],
        "correct_answer": "Africa",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_078",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What do the letters 'GMT' stand for in time zones?",
        "options": ["Greenwich Mean Time", "Global Meridian Time", "General Mean Time", "Geographic Median Time"],
        "correct_answer": "Greenwich Mean Time",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_079",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which river forms part of the border between Mexico and the United States?",
        "options": ["Rio Grande", "Colorado River", "Mississippi River", "Columbia River"],
        "correct_answer": "Rio Grande",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_080",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What is the southernmost point of mainland Africa called?",
        "options": ["Cape Agulhas", "Cape of Good Hope", "Cape Town", "Cape Verde"],
        "correct_answer": "Cape Agulhas",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_081",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which sea separates Europe from Africa at its narrowest point?",
        "options": ["Mediterranean Sea", "Red Sea", "Black Sea", "Adriatic Sea"],
        "correct_answer": "Mediterranean Sea",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_082",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "How many countries does Brazil border?",
        "options": ["10", "8", "6", "12"],
        "correct_answer": "10",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_083",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What line of latitude is at 23.5 degrees south?",
        "options": ["Tropic of Capricorn", "Tropic of Cancer", "Antarctic Circle", "Equator"],
        "correct_answer": "Tropic of Capricorn",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_084",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which peninsula do Italy, Greece, and the Balkans form part of?",
        "options": ["Southern Europe", "Mediterranean Region", "Balkans", "None - they are separate peninsulas"],
        "correct_answer": "None - they are separate peninsulas",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_085",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which body of water separates Alaska from Russia?",
        "options": ["Bering Strait", "Bering Sea", "Arctic Ocean", "Pacific Ocean"],
        "correct_answer": "Bering Strait",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },

    # MEDIUM (19 questions)
    {
        "id": "geo_086",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which country has borders with both the Atlantic and Indian Oceans?",
        "options": ["South Africa", "Australia", "Brazil", "Indonesia"],
        "correct_answer": "South Africa",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_087",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What is the only country that borders both the Caspian Sea and the Persian Gulf?",
        "options": ["Iran", "Azerbaijan", "Turkmenistan", "Russia"],
        "correct_answer": "Iran",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_088",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which European country is divided into 26 cantons?",
        "options": ["Switzerland", "Belgium", "Netherlands", "Austria"],
        "correct_answer": "Switzerland",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_089",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What is the name of the boundary line between India and Pakistan?",
        "options": ["Radcliffe Line", "McMahon Line", "Durand Line", "Line of Control"],
        "correct_answer": "Radcliffe Line",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_090",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which country has the most neighboring countries?",
        "options": ["China", "Russia", "Brazil", "Germany"],
        "correct_answer": "China",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_091",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What is the boundary between Europe and Asia called in the Ural region?",
        "options": ["Ural-Caucasus Line", "Continental Divide", "Eurasian Border", "Silk Road"],
        "correct_answer": "Ural-Caucasus Line",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_092",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which two countries are separated by the Strait of Dover?",
        "options": ["England and France", "Spain and Morocco", "Denmark and Sweden", "Italy and Tunisia"],
        "correct_answer": "England and France",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_093",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What is the Arctic Circle's approximate latitude?",
        "options": ["66.5°N", "60°N", "70°N", "75°N"],
        "correct_answer": "66.5°N",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_094",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which African country is completely surrounded by South Africa?",
        "options": ["Lesotho", "Swaziland", "Botswana", "Zimbabwe"],
        "correct_answer": "Lesotho",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_095",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What is the shortest distance between Africa and Europe?",
        "options": ["14 kilometers", "30 kilometers", "50 kilometers", "8 kilometers"],
        "correct_answer": "14 kilometers",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_096",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which two South American countries do not border Brazil?",
        "options": ["Chile and Ecuador", "Argentina and Peru", "Colombia and Venezuela", "Bolivia and Paraguay"],
        "correct_answer": "Chile and Ecuador",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_097",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What body of water separates Saudi Arabia from Africa?",
        "options": ["Red Sea", "Persian Gulf", "Arabian Sea", "Gulf of Aden"],
        "correct_answer": "Red Sea",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_098",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which country has land borders with 14 different nations?",
        "options": ["Russia", "China", "Brazil", "India"],
        "correct_answer": "Russia",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_099",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What is the line of latitude at approximately 66.5 degrees south called?",
        "options": ["Antarctic Circle", "Tropic of Capricorn", "South Polar Circle", "Southern Boundary"],
        "correct_answer": "Antarctic Circle",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_100",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which country is bordered by both the Black Sea and the Mediterranean Sea?",
        "options": ["Turkey", "Greece", "Bulgaria", "Romania"],
        "correct_answer": "Turkey",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_101",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What mountain range forms a natural border between France and Spain?",
        "options": ["Pyrenees", "Alps", "Sierra Nevada", "Cantabrian Mountains"],
        "correct_answer": "Pyrenees",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_102",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which continent is crossed by all lines of longitude?",
        "options": ["Antarctica", "Africa", "Asia", "South America"],
        "correct_answer": "Antarctica",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_103",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What is the border between Afghanistan and Pakistan called?",
        "options": ["Durand Line", "Radcliffe Line", "McMahon Line", "Line of Control"],
        "correct_answer": "Durand Line",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_104",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which sea connects to the Atlantic Ocean through the Strait of Gibraltar?",
        "options": ["Mediterranean Sea", "Adriatic Sea", "Aegean Sea", "Black Sea"],
        "correct_answer": "Mediterranean Sea",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },

    # HARD (18 questions)
    {
        "id": "geo_105",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What is the only tripoint where three continents meet?",
        "options": ["Suez (Africa, Asia, and by extension Europe)", "Bering Strait", "Sinai Peninsula", "There is no such point"],
        "correct_answer": "There is no such point",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_106",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which country has the most international land borders?",
        "options": ["China and Russia (tied at 14)", "Brazil", "Germany", "India"],
        "correct_answer": "China and Russia (tied at 14)",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_107",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What is the Four Corners region in the United States?",
        "options": ["Where Utah, Colorado, Arizona, and New Mexico meet", "Where four Great Lakes meet", "Where four state capitals align", "Where the Mississippi divides four states"],
        "correct_answer": "Where Utah, Colorado, Arizona, and New Mexico meet",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_108",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which European microstate is an enclave within Italy?",
        "options": ["San Marino and Vatican City", "Monaco", "Liechtenstein", "Andorra"],
        "correct_answer": "San Marino and Vatican City",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_109",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What is the name of the artificial border created between North and South Vietnam?",
        "options": ["17th Parallel", "38th Parallel", "DMZ Line", "Ben Hai River"],
        "correct_answer": "17th Parallel",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_110",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which two countries share the world's longest international border?",
        "options": ["Canada and United States", "Russia and Kazakhstan", "Chile and Argentina", "China and Russia"],
        "correct_answer": "Canada and United States",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_111",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What is unique about the border between Zambia and Zimbabwe?",
        "options": ["Victoria Falls is on it", "It's the shortest international border", "It follows a straight line", "It changes with the seasons"],
        "correct_answer": "Victoria Falls is on it",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_112",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which strait separates the North and South Islands of New Zealand?",
        "options": ["Cook Strait", "Bass Strait", "Torres Strait", "Foveaux Strait"],
        "correct_answer": "Cook Strait",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_113",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What is the McMahon Line?",
        "options": ["Border between India and China", "Antarctic territorial claim", "Arctic boundary", "Equatorial reference line"],
        "correct_answer": "Border between India and China",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_114",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which country has a quadripoint with Namibia, Zambia, Zimbabwe, and Botswana?",
        "options": ["None - it's a near-quadripoint", "South Africa", "Angola", "Mozambique"],
        "correct_answer": "None - it's a near-quadripoint",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_115",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What is the Oder-Neisse Line?",
        "options": ["Border between Germany and Poland", "Border between Russia and Finland", "Demarcation line in Korea", "Division of Austria-Hungary"],
        "correct_answer": "Border between Germany and Poland",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_116",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which body of water separates Tasmania from mainland Australia?",
        "options": ["Bass Strait", "Cook Strait", "Torres Strait", "Tasman Sea"],
        "correct_answer": "Bass Strait",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_117",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What is the name of the maritime boundary concept at 200 nautical miles?",
        "options": ["Exclusive Economic Zone (EEZ)", "Continental Shelf", "Territorial Waters", "High Seas Boundary"],
        "correct_answer": "Exclusive Economic Zone (EEZ)",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_118",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which South American country has coastlines on both the Pacific Ocean and the Caribbean Sea?",
        "options": ["Colombia", "Panama", "Venezuela", "Ecuador"],
        "correct_answer": "Colombia",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_119",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What is the Wakhan Corridor?",
        "options": ["Narrow strip of Afghanistan between Tajikistan and Pakistan", "Border between India and Nepal", "Passage through the Himalayas", "Trade route in Central Asia"],
        "correct_answer": "Narrow strip of Afghanistan between Tajikistan and Pakistan",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_120",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which two oceans does the Drake Passage connect?",
        "options": ["Atlantic and Pacific", "Pacific and Southern", "Atlantic and Southern", "Indian and Pacific"],
        "correct_answer": "Atlantic and Pacific",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_121",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "What is the Line of Actual Control (LAC)?",
        "options": ["De facto border between India and China", "Korean DMZ", "Cyprus Green Line", "Israeli West Bank barrier"],
        "correct_answer": "De facto border between India and China",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_122",
        "category": "Geography",
        "subcategory": "Maps & Borders",
        "question": "Which country controls both sides of the Bosphorus Strait?",
        "options": ["Turkey", "Greece", "Bulgaria", "Russia"],
        "correct_answer": "Turkey",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    }
]

# Load existing data
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Add new questions
data['categories']['Geography'].extend(new_questions)

# Sort by ID to maintain order
data['categories']['Geography'].sort(key=lambda q: int(q['id'].split('_')[1]))

# Save back
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Added 55 Maps & Borders questions")
print(f"Geography now has {len(data['categories']['Geography'])} total questions")

# Count Maps & Borders
maps_borders = [q for q in data['categories']['Geography'] if q['subcategory'] == 'Maps & Borders']
print(f"Maps & Borders: {len(maps_borders)} questions")

# Count by difficulty
easy = len([q for q in new_questions if q['difficulty'] == 'easy'])
medium = len([q for q in new_questions if q['difficulty'] == 'medium'])
hard = len([q for q in new_questions if q['difficulty'] == 'hard'])
print(f"Added: {easy} easy, {medium} medium, {hard} hard")
