#!/usr/bin/env python3
"""Add 60 Flags questions from scratch"""
import json

# 60 Flags questions (20 easy, 20 medium, 20 hard)
new_questions = [
    # EASY (20 questions)
    {
        "id": "geo_181",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag features a red maple leaf?",
        "options": ["Canada", "Switzerland", "Japan", "Denmark"],
        "correct_answer": "Canada",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_182",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What colors are on the flag of the United States?",
        "options": ["Red, white, and blue", "Red, white, and green", "Blue, yellow, and white", "Red, blue, and yellow"],
        "correct_answer": "Red, white, and blue",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_183",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag is a solid green rectangle?",
        "options": ["Libya (historically)", "Ireland", "Saudi Arabia", "Pakistan"],
        "correct_answer": "Libya (historically)",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_184",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What color is the circle on Japan's flag?",
        "options": ["Red", "White", "Yellow", "Blue"],
        "correct_answer": "Red",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_185",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag features stars and stripes?",
        "options": ["United States", "Australia", "Brazil", "Chile"],
        "correct_answer": "United States",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_186",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What colors are on the flag of Italy?",
        "options": ["Green, white, and red", "Blue, white, and red", "Green, yellow, and red", "Red, white, and blue"],
        "correct_answer": "Green, white, and red",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_187",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag is a white cross on a red background?",
        "options": ["Switzerland", "Denmark", "England", "Sweden"],
        "correct_answer": "Switzerland",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_188",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What colors are on the flag of France?",
        "options": ["Blue, white, and red", "Red, white, and green", "Blue, yellow, and red", "Green, white, and red"],
        "correct_answer": "Blue, white, and red",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_189",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag features a Union Jack in the corner?",
        "options": ["Australia", "United States", "Ireland", "South Africa"],
        "correct_answer": "Australia",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_190",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What colors are on the flag of Germany?",
        "options": ["Black, red, and yellow", "Black, white, and red", "Blue, white, and red", "Green, white, and red"],
        "correct_answer": "Black, red, and yellow",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_191",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag features a red circle on a green background?",
        "options": ["Bangladesh", "Japan", "Pakistan", "Morocco"],
        "correct_answer": "Bangladesh",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_192",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What colors are on the flag of Ireland?",
        "options": ["Green, white, and orange", "Green, white, and red", "Blue, white, and green", "Green, yellow, and white"],
        "correct_answer": "Green, white, and orange",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_193",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag has horizontal stripes of red, white, and blue from top to bottom?",
        "options": ["Netherlands", "France", "Russia", "United Kingdom"],
        "correct_answer": "Netherlands",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_194",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What symbol is on the flag of Canada?",
        "options": ["Maple leaf", "Eagle", "Star", "Lion"],
        "correct_answer": "Maple leaf",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_195",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag features a yellow sun with rays?",
        "options": ["Argentina", "Brazil", "Mexico", "Colombia"],
        "correct_answer": "Argentina",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_196",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What colors are on the flag of Spain?",
        "options": ["Red and yellow", "Red and white", "Blue and yellow", "Green and red"],
        "correct_answer": "Red and yellow",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_197",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag is red with a yellow star?",
        "options": ["Vietnam", "China", "Turkey", "Morocco"],
        "correct_answer": "Vietnam",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_198",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What shape is on the flag of Israel?",
        "options": ["Star of David", "Crescent moon", "Cross", "Circle"],
        "correct_answer": "Star of David",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_199",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag features a white crescent and star on a red background?",
        "options": ["Turkey", "Pakistan", "Tunisia", "Algeria"],
        "correct_answer": "Turkey",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_200",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What colors are on the flag of Mexico?",
        "options": ["Green, white, and red", "Red, white, and blue", "Green, yellow, and red", "Blue, white, and green"],
        "correct_answer": "Green, white, and red",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },

    # MEDIUM (20 questions)
    {
        "id": "geo_201",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag features the Southern Cross constellation?",
        "options": ["Australia and New Zealand", "Chile", "Brazil", "Argentina"],
        "correct_answer": "Australia and New Zealand",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_202",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What animal is on the flag of Wales?",
        "options": ["Dragon", "Lion", "Eagle", "Unicorn"],
        "correct_answer": "Dragon",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_203",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag has 50 stars representing its states?",
        "options": ["United States", "Brazil", "Australia", "European Union"],
        "correct_answer": "United States",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_204",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What colors are on the flag of Brazil?",
        "options": ["Green, yellow, blue, and white", "Green, yellow, and red", "Blue, white, and green", "Yellow, green, and red"],
        "correct_answer": "Green, yellow, blue, and white",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_205",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which two countries have flags that are nearly identical but with colors inverted?",
        "options": ["Poland and Indonesia/Monaco", "France and Netherlands", "Italy and Ireland", "Russia and Slovenia"],
        "correct_answer": "Poland and Indonesia/Monaco",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_206",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What symbol is at the center of the Mexican flag?",
        "options": ["Eagle eating a snake", "Sun", "Star", "Cross"],
        "correct_answer": "Eagle eating a snake",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_207",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which Nordic country's flag is blue with a yellow cross?",
        "options": ["Sweden", "Norway", "Denmark", "Finland"],
        "correct_answer": "Sweden",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_208",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What is unique about Nepal's flag shape?",
        "options": ["It's not rectangular", "It's circular", "It's triangular", "It's hexagonal"],
        "correct_answer": "It's not rectangular",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_209",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag features a cedar tree?",
        "options": ["Lebanon", "Syria", "Jordan", "Iraq"],
        "correct_answer": "Lebanon",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_210",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What colors are on the flag of South Africa?",
        "options": ["Red, green, blue, yellow, black, and white", "Red, green, and yellow", "Blue, yellow, and green", "Red, white, and blue"],
        "correct_answer": "Red, green, blue, yellow, black, and white",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_211",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag shows a wheel (chakra) in the center?",
        "options": ["India", "Pakistan", "Bangladesh", "Sri Lanka"],
        "correct_answer": "India",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_212",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What appears on the flag of Cambodia?",
        "options": ["Angkor Wat temple", "Dragon", "Lotus flower", "Elephant"],
        "correct_answer": "Angkor Wat temple",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_213",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag features a dragon?",
        "options": ["Bhutan and Wales", "China", "Vietnam", "Thailand"],
        "correct_answer": "Bhutan and Wales",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_214",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What colors are on the flag of Jamaica?",
        "options": ["Green, yellow, and black", "Red, yellow, and green", "Blue, yellow, and black", "Green, red, and yellow"],
        "correct_answer": "Green, yellow, and black",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_215",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag has the most colors?",
        "options": ["Belize", "South Africa", "Brazil", "Mexico"],
        "correct_answer": "Belize",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_216",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What is on the flag of Portugal?",
        "options": ["Armillary sphere and shield", "Cross", "Star", "Crown"],
        "correct_answer": "Armillary sphere and shield",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_217",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag is white with a red circle, similar to Japan, but with text?",
        "options": ["Bangladesh", "South Korea", "Singapore", "Philippines"],
        "correct_answer": "Bangladesh",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_218",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What symbol appears on the flag of Sri Lanka?",
        "options": ["Lion", "Elephant", "Tiger", "Peacock"],
        "correct_answer": "Lion",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_219",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag features a yin-yang symbol?",
        "options": ["South Korea", "North Korea", "Mongolia", "Taiwan"],
        "correct_answer": "South Korea",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_220",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What appears on the flag of Kenya?",
        "options": ["Shield and spears", "Lion", "Elephant", "Tree"],
        "correct_answer": "Shield and spears",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },

    # HARD (20 questions)
    {
        "id": "geo_221",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag has a building depicted on it?",
        "options": ["Afghanistan and Cambodia", "India", "China", "Thailand"],
        "correct_answer": "Afghanistan and Cambodia",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_222",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What is the only national flag that is not rectangular or square?",
        "options": ["Nepal", "Switzerland", "Vatican City", "Monaco"],
        "correct_answer": "Nepal",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_223",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag features a firearm (rifle)?",
        "options": ["Mozambique", "Guatemala", "Zimbabwe", "Haiti"],
        "correct_answer": "Mozambique",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_224",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What is on the flag of Turkmenistan?",
        "options": ["Carpet patterns", "Yurt", "Horse", "Eagle"],
        "correct_answer": "Carpet patterns",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_225",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which two countries have square flags?",
        "options": ["Switzerland and Vatican City", "Nepal and Bhutan", "Monaco and Liechtenstein", "San Marino and Andorra"],
        "correct_answer": "Switzerland and Vatican City",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_226",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What do the 27 stars on the Brazilian flag represent?",
        "options": ["States and Federal District", "Cities", "Heroes", "Provinces"],
        "correct_answer": "States and Federal District",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_227",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag has different designs on each side?",
        "options": ["Paraguay", "Moldova", "Saudi Arabia", "Iraq"],
        "correct_answer": "Paraguay",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_228",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What is depicted on the flag of Cyprus?",
        "options": ["Map of the island", "Olive branches", "Ancient ship", "Temple"],
        "correct_answer": "Map of the island",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_229",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag features the Dharmachakra wheel?",
        "options": ["India", "Tibet", "Mongolia", "Bhutan"],
        "correct_answer": "India",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_230",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What appears on the flag of Belize?",
        "options": ["People and tools in a circle", "Jaguar", "Mayan temple", "Parrot"],
        "correct_answer": "People and tools in a circle",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_231",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag shows a book on it?",
        "options": ["Afghanistan", "Pakistan", "Iran", "Saudi Arabia"],
        "correct_answer": "Afghanistan",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_232",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What is unique about the flag of Dominica?",
        "options": ["Purple color (rare for flags)", "Circular shape", "Holographic elements", "Changes seasonally"],
        "correct_answer": "Purple color (rare for flags)",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_233",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag features a bird of paradise?",
        "options": ["Papua New Guinea", "Madagascar", "Fiji", "Solomon Islands"],
        "correct_answer": "Papua New Guinea",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_234",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What do the colors on the Pan-African flag represent?",
        "options": ["Red (blood), Black (people), Green (land)", "Freedom, Unity, Progress", "Past, Present, Future", "Faith, Hope, Charity"],
        "correct_answer": "Red (blood), Black (people), Green (land)",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_235",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag has the phrase 'Ordem e Progresso' (Order and Progress)?",
        "options": ["Brazil", "Portugal", "Angola", "Mozambique"],
        "correct_answer": "Brazil",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_236",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What celestial bodies appear on Nepal's flag?",
        "options": ["Sun and moon", "Stars", "Comet", "None"],
        "correct_answer": "Sun and moon",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_237",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag features a trident?",
        "options": ["Barbados", "Ukraine", "Malta", "Cyprus"],
        "correct_answer": "Barbados",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_238",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What is on the flag of Kiribati?",
        "options": ["Frigate bird over the sun and ocean", "Palm tree", "Canoe", "Fish"],
        "correct_answer": "Frigate bird over the sun and ocean",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_239",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "Which country's flag shows mountains and a sun?",
        "options": ["Nepal and Afghanistan", "Bhutan", "Tajikistan", "Kyrgyzstan"],
        "correct_answer": "Nepal and Afghanistan",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_240",
        "category": "Geography",
        "subcategory": "Flags",
        "question": "What appears on the flag of Albania?",
        "options": ["Double-headed eagle", "Single eagle", "Lion", "Dragon"],
        "correct_answer": "Double-headed eagle",
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

print("✅ Added 60 Flags questions")
print(f"Geography now has {len(data['categories']['Geography'])} total questions")

# Count Flags
flags = [q for q in data['categories']['Geography'] if q['subcategory'] == 'Flags']
print(f"Flags: {len(flags)} questions")

# Count by difficulty
easy = len([q for q in new_questions if q['difficulty'] == 'easy'])
medium = len([q for q in new_questions if q['difficulty'] == 'medium'])
hard = len([q for q in new_questions if q['difficulty'] == 'hard'])
print(f"Added: {easy} easy, {medium} medium, {hard} hard")
