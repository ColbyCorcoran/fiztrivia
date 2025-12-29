#!/usr/bin/env python3
"""Add 58 U.S. Geography questions to reach 60 total"""
import json

# 58 new U.S. Geography questions (19 easy, 20 medium, 19 hard)
new_questions = [
    # EASY (19 questions)
    {
        "id": "geo_123",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the largest state in the United States by land area?",
        "options": ["Alaska", "Texas", "California", "Montana"],
        "correct_answer": "Alaska",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_124",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which river is the longest in the United States?",
        "options": ["Missouri River", "Mississippi River", "Yukon River", "Rio Grande"],
        "correct_answer": "Missouri River",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_125",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the capital of California?",
        "options": ["Sacramento", "Los Angeles", "San Francisco", "San Diego"],
        "correct_answer": "Sacramento",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_126",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "How many states make up the United States?",
        "options": ["50", "48", "52", "51"],
        "correct_answer": "50",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_127",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which ocean is on the West Coast of the United States?",
        "options": ["Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", "Indian Ocean"],
        "correct_answer": "Pacific Ocean",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_128",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the smallest state in the United States?",
        "options": ["Rhode Island", "Delaware", "Connecticut", "Hawaii"],
        "correct_answer": "Rhode Island",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_129",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which mountain range runs along the eastern United States?",
        "options": ["Appalachian Mountains", "Rocky Mountains", "Sierra Nevada", "Cascade Range"],
        "correct_answer": "Appalachian Mountains",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_130",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the capital of Texas?",
        "options": ["Austin", "Houston", "Dallas", "San Antonio"],
        "correct_answer": "Austin",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_131",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which Great Lake is entirely within the United States?",
        "options": ["Lake Michigan", "Lake Superior", "Lake Huron", "Lake Erie"],
        "correct_answer": "Lake Michigan",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_132",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the capital of New York?",
        "options": ["Albany", "New York City", "Buffalo", "Rochester"],
        "correct_answer": "Albany",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_133",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which state is known as the \"Sunshine State\"?",
        "options": ["Florida", "California", "Arizona", "Hawaii"],
        "correct_answer": "Florida",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_134",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the highest mountain in the United States?",
        "options": ["Denali", "Mount Whitney", "Mount Rainier", "Pikes Peak"],
        "correct_answer": "Denali",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_135",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which state is home to the Grand Canyon?",
        "options": ["Arizona", "Utah", "Colorado", "Nevada"],
        "correct_answer": "Arizona",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_136",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the capital of Florida?",
        "options": ["Tallahassee", "Miami", "Orlando", "Tampa"],
        "correct_answer": "Tallahassee",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_137",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which state is known as the \"Golden State\"?",
        "options": ["California", "Nevada", "Colorado", "Wyoming"],
        "correct_answer": "California",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_138",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What river forms much of the border between the United States and Mexico?",
        "options": ["Rio Grande", "Colorado River", "Pecos River", "Gila River"],
        "correct_answer": "Rio Grande",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_139",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which state are the Hawaiian Islands part of?",
        "options": ["Hawaii", "Pacific Territory", "American Samoa", "Guam"],
        "correct_answer": "Hawaii",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_140",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the largest city in the United States by population?",
        "options": ["New York City", "Los Angeles", "Chicago", "Houston"],
        "correct_answer": "New York City",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_141",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which state is Mount Rushmore located in?",
        "options": ["South Dakota", "North Dakota", "Wyoming", "Montana"],
        "correct_answer": "South Dakota",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },

    # MEDIUM (20 questions)
    {
        "id": "geo_142",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the only state that borders just one other state?",
        "options": ["Maine", "Alaska", "Florida", "Washington"],
        "correct_answer": "Maine",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_143",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which state has the longest coastline?",
        "options": ["Alaska", "Florida", "California", "Maine"],
        "correct_answer": "Alaska",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_144",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the deepest lake in the United States?",
        "options": ["Crater Lake", "Lake Tahoe", "Lake Superior", "Great Salt Lake"],
        "correct_answer": "Crater Lake",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_145",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which state is known as the \"Cornhusker State\"?",
        "options": ["Nebraska", "Iowa", "Kansas", "Illinois"],
        "correct_answer": "Nebraska",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_146",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the capital of Colorado?",
        "options": ["Denver", "Boulder", "Colorado Springs", "Aurora"],
        "correct_answer": "Denver",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_147",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which U.S. state has the most active volcanoes?",
        "options": ["Alaska", "Hawaii", "Washington", "California"],
        "correct_answer": "Alaska",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_148",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the lowest point in the United States?",
        "options": ["Death Valley", "Salton Sea", "New Orleans", "Badwater Basin"],
        "correct_answer": "Death Valley",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_149",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which state contains Yellowstone National Park primarily?",
        "options": ["Wyoming", "Montana", "Idaho", "Utah"],
        "correct_answer": "Wyoming",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_150",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the capital of Massachusetts?",
        "options": ["Boston", "Cambridge", "Worcester", "Springfield"],
        "correct_answer": "Boston",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_151",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which state is the largest producer of maple syrup?",
        "options": ["Vermont", "Maine", "New Hampshire", "New York"],
        "correct_answer": "Vermont",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_152",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the most populous city in Texas?",
        "options": ["Houston", "Dallas", "Austin", "San Antonio"],
        "correct_answer": "Houston",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_153",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which state has the nickname \"The Last Frontier\"?",
        "options": ["Alaska", "Montana", "Wyoming", "Idaho"],
        "correct_answer": "Alaska",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_154",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the capital of Oregon?",
        "options": ["Salem", "Portland", "Eugene", "Bend"],
        "correct_answer": "Salem",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_155",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which state contains the geographic center of the contiguous United States?",
        "options": ["Kansas", "Nebraska", "South Dakota", "Oklahoma"],
        "correct_answer": "Kansas",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_156",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the largest desert in the United States?",
        "options": ["Mojave Desert", "Sonoran Desert", "Chihuahuan Desert", "Great Basin Desert"],
        "correct_answer": "Great Basin Desert",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_157",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which state is home to Acadia National Park?",
        "options": ["Maine", "Vermont", "New Hampshire", "Massachusetts"],
        "correct_answer": "Maine",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_158",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the capital of Nevada?",
        "options": ["Carson City", "Las Vegas", "Reno", "Henderson"],
        "correct_answer": "Carson City",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_159",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which state is known as the \"Pelican State\"?",
        "options": ["Louisiana", "Mississippi", "Alabama", "Georgia"],
        "correct_answer": "Louisiana",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_160",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What major river flows through the Grand Canyon?",
        "options": ["Colorado River", "Green River", "San Juan River", "Little Colorado River"],
        "correct_answer": "Colorado River",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_161",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which state has the most counties?",
        "options": ["Texas", "Georgia", "Virginia", "Kentucky"],
        "correct_answer": "Texas",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },

    # HARD (19 questions)
    {
        "id": "geo_162",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the capital of South Dakota?",
        "options": ["Pierre", "Sioux Falls", "Rapid City", "Aberdeen"],
        "correct_answer": "Pierre",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_163",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which state contains the most extensive cave system in the world?",
        "options": ["Kentucky", "Tennessee", "West Virginia", "Missouri"],
        "correct_answer": "Kentucky",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_164",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the capital of Vermont?",
        "options": ["Montpelier", "Burlington", "Rutland", "Bennington"],
        "correct_answer": "Montpelier",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_165",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which U.S. state has the highest mean elevation?",
        "options": ["Colorado", "Wyoming", "Utah", "Montana"],
        "correct_answer": "Colorado",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_166",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the only state capital that has three words in its name?",
        "options": ["Salt Lake City", "Oklahoma City", "Jefferson City", "Baton Rouge"],
        "correct_answer": "Salt Lake City",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_167",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which state is Point Barrow, the northernmost point in the United States, located in?",
        "options": ["Alaska", "Washington", "Maine", "Minnesota"],
        "correct_answer": "Alaska",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_168",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the capital of New Hampshire?",
        "options": ["Concord", "Manchester", "Nashua", "Portsmouth"],
        "correct_answer": "Concord",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_169",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which state contains the most fourteeners (mountains over 14,000 feet)?",
        "options": ["Colorado", "California", "Alaska", "Wyoming"],
        "correct_answer": "Colorado",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_170",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the westernmost point of the continental United States?",
        "options": ["Cape Alava, Washington", "Point Arena, California", "Cape Flattery, Washington", "Point Conception, California"],
        "correct_answer": "Cape Alava, Washington",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_171",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the capital of Delaware?",
        "options": ["Dover", "Wilmington", "Newark", "Lewes"],
        "correct_answer": "Dover",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_172",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which state borders the most other states?",
        "options": ["Tennessee and Missouri (tied at 8)", "Kentucky", "Colorado", "Arkansas"],
        "correct_answer": "Tennessee and Missouri (tied at 8)",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_173",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the least populous state capital?",
        "options": ["Montpelier, Vermont", "Pierre, South Dakota", "Augusta, Maine", "Juneau, Alaska"],
        "correct_answer": "Montpelier, Vermont",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_174",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which state contains the geographic center of the entire United States (including Alaska and Hawaii)?",
        "options": ["South Dakota", "Kansas", "Nebraska", "Wyoming"],
        "correct_answer": "South Dakota",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_175",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the capital of West Virginia?",
        "options": ["Charleston", "Huntington", "Morgantown", "Wheeling"],
        "correct_answer": "Charleston",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_176",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which U.S. state has the most national parks?",
        "options": ["California", "Alaska", "Utah", "Colorado"],
        "correct_answer": "California",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_177",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the only U.S. state whose name is one syllable?",
        "options": ["Maine", "Iowa", "Ohio", "Utah"],
        "correct_answer": "Maine",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_178",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "Which state has the highest percentage of its land covered by water?",
        "options": ["Michigan", "Alaska", "Florida", "Louisiana"],
        "correct_answer": "Michigan",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_179",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the southernmost point of the continental United States?",
        "options": ["Key West, Florida", "Cape Sable, Florida", "South Point, Florida", "Ballast Key, Florida"],
        "correct_answer": "Ballast Key, Florida",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_180",
        "category": "Geography",
        "subcategory": "U.S. Geography",
        "question": "What is the capital of Wyoming?",
        "options": ["Cheyenne", "Casper", "Laramie", "Jackson"],
        "correct_answer": "Cheyenne",
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

print("✅ Added 58 U.S. Geography questions")
print(f"Geography now has {len(data['categories']['Geography'])} total questions")

# Count U.S. Geography
us_geo = [q for q in data['categories']['Geography'] if q['subcategory'] == 'U.S. Geography']
print(f"U.S. Geography: {len(us_geo)} questions")

# Count by difficulty
easy = len([q for q in new_questions if q['difficulty'] == 'easy'])
medium = len([q for q in new_questions if q['difficulty'] == 'medium'])
hard = len([q for q in new_questions if q['difficulty'] == 'hard'])
print(f"Added: {easy} easy, {medium} medium, {hard} hard")
