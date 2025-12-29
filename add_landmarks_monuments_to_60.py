#!/usr/bin/env python3
"""Add 60 Landmarks & Monuments questions from scratch"""
import json

# 60 Landmarks & Monuments questions (20 easy, 20 medium, 20 hard)
new_questions = [
    # EASY (20 questions)
    {
        "id": "geo_241",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which famous statue stands in New York Harbor?",
        "options": ["Statue of Liberty", "Lincoln Memorial", "Christ the Redeemer", "Statue of David"],
        "correct_answer": "Statue of Liberty",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_242",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "In which country is the Eiffel Tower located?",
        "options": ["France", "Italy", "Spain", "Belgium"],
        "correct_answer": "France",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_243",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "What ancient wonder is located in Egypt?",
        "options": ["Great Pyramid of Giza", "Hanging Gardens", "Colossus of Rhodes", "Lighthouse of Alexandria"],
        "correct_answer": "Great Pyramid of Giza",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_244",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which famous tower is in Pisa, Italy?",
        "options": ["Leaning Tower of Pisa", "Tower of London", "CN Tower", "Space Needle"],
        "correct_answer": "Leaning Tower of Pisa",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_245",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Where is the Great Wall located?",
        "options": ["China", "Japan", "Korea", "Mongolia"],
        "correct_answer": "China",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_246",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which monument overlooks Rio de Janeiro?",
        "options": ["Christ the Redeemer", "Statue of Liberty", "Big Ben", "Eiffel Tower"],
        "correct_answer": "Christ the Redeemer",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_247",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "What is the famous clock tower in London called?",
        "options": ["Big Ben", "Liberty Bell", "Peace Tower", "Campanile"],
        "correct_answer": "Big Ben",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_248",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which ancient amphitheater is in Rome?",
        "options": ["Colosseum", "Parthenon", "Forum", "Pantheon"],
        "correct_answer": "Colosseum",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_249",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Where is the Taj Mahal located?",
        "options": ["India", "Pakistan", "Bangladesh", "Nepal"],
        "correct_answer": "India",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_250",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which bridge is famous in San Francisco?",
        "options": ["Golden Gate Bridge", "Brooklyn Bridge", "London Bridge", "Sydney Harbour Bridge"],
        "correct_answer": "Golden Gate Bridge",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_251",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Where is the Sydney Opera House located?",
        "options": ["Australia", "New Zealand", "Singapore", "Malaysia"],
        "correct_answer": "Australia",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_252",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which ancient temple complex is in Cambodia?",
        "options": ["Angkor Wat", "Borobudur", "Prambanan", "Shwedagon"],
        "correct_answer": "Angkor Wat",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_253",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "What is the name of the palace in Versailles?",
        "options": ["Palace of Versailles", "Louvre Palace", "Buckingham Palace", "Schönbrunn Palace"],
        "correct_answer": "Palace of Versailles",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_254",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Where are the carved faces of Mount Rushmore?",
        "options": ["South Dakota", "North Dakota", "Wyoming", "Montana"],
        "correct_answer": "South Dakota",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_255",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which famous fountain is in Rome?",
        "options": ["Trevi Fountain", "Fontana di Trevi", "Fountain of Neptune", "Fountain of Four Rivers"],
        "correct_answer": "Trevi Fountain",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_256",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Where is Machu Picchu located?",
        "options": ["Peru", "Mexico", "Brazil", "Chile"],
        "correct_answer": "Peru",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_257",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which famous cathedral is in Paris?",
        "options": ["Notre-Dame", "Sagrada Familia", "St. Peter's Basilica", "Westminster Abbey"],
        "correct_answer": "Notre-Dame",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_258",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "What is the tallest building in the world (as of 2025)?",
        "options": ["Burj Khalifa", "Shanghai Tower", "Taipei 101", "One World Trade Center"],
        "correct_answer": "Burj Khalifa",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_259",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Where is Stonehenge located?",
        "options": ["England", "Ireland", "Scotland", "Wales"],
        "correct_answer": "England",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_260",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which ancient city carved into rock is in Jordan?",
        "options": ["Petra", "Jerusalem", "Damascus", "Palmyra"],
        "correct_answer": "Petra",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },

    # MEDIUM (20 questions)
    {
        "id": "geo_261",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which monument was a gift from France to the United States?",
        "options": ["Statue of Liberty", "Washington Monument", "Liberty Bell", "Lincoln Memorial"],
        "correct_answer": "Statue of Liberty",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_262",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "What does 'Machu Picchu' mean in Quechua?",
        "options": ["Old Peak", "Lost City", "Sky City", "Sacred Mountain"],
        "correct_answer": "Old Peak",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_263",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which city is the Acropolis located in?",
        "options": ["Athens", "Rome", "Istanbul", "Cairo"],
        "correct_answer": "Athens",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_264",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "What year was the Eiffel Tower completed?",
        "options": ["1889", "1876", "1901", "1855"],
        "correct_answer": "1889",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_265",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which emperor built the Taj Mahal?",
        "options": ["Shah Jahan", "Akbar", "Aurangzeb", "Babur"],
        "correct_answer": "Shah Jahan",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_266",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Where is the Gateway Arch located?",
        "options": ["St. Louis, Missouri", "Chicago, Illinois", "Seattle, Washington", "Denver, Colorado"],
        "correct_answer": "St. Louis, Missouri",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_267",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which Spanish architect designed the Sagrada Familia?",
        "options": ["Antoni Gaudí", "Santiago Calatrava", "Rafael Moneo", "Ricardo Bofill"],
        "correct_answer": "Antoni Gaudí",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_268",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "What is the name of the mausoleum in Moscow's Red Square?",
        "options": ["Lenin's Mausoleum", "Kremlin", "St. Basil's Cathedral", "GUM"],
        "correct_answer": "Lenin's Mausoleum",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_269",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which city is home to the Space Needle?",
        "options": ["Seattle", "Portland", "Vancouver", "San Francisco"],
        "correct_answer": "Seattle",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_270",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "What is the largest religious monument in the world?",
        "options": ["Angkor Wat", "St. Peter's Basilica", "Hagia Sophia", "Blue Mosque"],
        "correct_answer": "Angkor Wat",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_271",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Where is the Brandenburg Gate located?",
        "options": ["Berlin", "Munich", "Hamburg", "Frankfurt"],
        "correct_answer": "Berlin",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_272",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which monument honors Abraham Lincoln in Washington D.C.?",
        "options": ["Lincoln Memorial", "Washington Monument", "Jefferson Memorial", "Capitol Building"],
        "correct_answer": "Lincoln Memorial",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_273",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "What city is the CN Tower in?",
        "options": ["Toronto", "Montreal", "Vancouver", "Calgary"],
        "correct_answer": "Toronto",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_274",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which temple is carved into the side of a mountain in Abu Simbel?",
        "options": ["Temple of Ramesses II", "Temple of Karnak", "Temple of Luxor", "Temple of Hatshepsut"],
        "correct_answer": "Temple of Ramesses II",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_275",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Where is the Christ the Redeemer statue's home city?",
        "options": ["Rio de Janeiro", "São Paulo", "Brasília", "Salvador"],
        "correct_answer": "Rio de Janeiro",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_276",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "What is the official residence of the British monarch in London?",
        "options": ["Buckingham Palace", "Westminster Palace", "Windsor Castle", "Kensington Palace"],
        "correct_answer": "Buckingham Palace",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_277",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which monument was built as a victory arch by Napoleon?",
        "options": ["Arc de Triomphe", "Arch of Constantine", "Brandenburg Gate", "Marble Arch"],
        "correct_answer": "Arc de Triomphe",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_278",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Where is the Forbidden City located?",
        "options": ["Beijing", "Shanghai", "Xi'an", "Nanjing"],
        "correct_answer": "Beijing",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_279",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which monument is the tallest in the United States?",
        "options": ["Gateway Arch", "Washington Monument", "Statue of Liberty", "San Jacinto Monument"],
        "correct_answer": "Gateway Arch",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_280",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "What ancient wonder is the only one still standing?",
        "options": ["Great Pyramid of Giza", "Colossus of Rhodes", "Hanging Gardens of Babylon", "Lighthouse of Alexandria"],
        "correct_answer": "Great Pyramid of Giza",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },

    # HARD (20 questions)
    {
        "id": "geo_281",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which monument features the inscription 'Give me your tired, your poor'?",
        "options": ["Statue of Liberty", "Ellis Island", "Lincoln Memorial", "Liberty Bell"],
        "correct_answer": "Statue of Liberty",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_282",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "What is the name of the ancient Incan city ruins near Cusco, Peru?",
        "options": ["Machu Picchu", "Sacsayhuamán", "Ollantaytambo", "Pisac"],
        "correct_answer": "Machu Picchu",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_283",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which monument in India was built by Emperor Ashoka?",
        "options": ["Sanchi Stupa", "Taj Mahal", "Qutub Minar", "Red Fort"],
        "correct_answer": "Sanchi Stupa",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_284",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "What is the name of the temple complex in Kyoto with thousands of red torii gates?",
        "options": ["Fushimi Inari Taisha", "Kinkaku-ji", "Kiyomizu-dera", "Ryoan-ji"],
        "correct_answer": "Fushimi Inari Taisha",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_285",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which ancient city in Turkey is known for its rock-cut architecture?",
        "options": ["Cappadocia", "Ephesus", "Troy", "Pergamon"],
        "correct_answer": "Cappadocia",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_286",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "What is the name of the massive bell in Westminster?",
        "options": ["Great Bell (Big Ben is the tower)", "Liberty Bell", "Tsar Bell", "Sigismund Bell"],
        "correct_answer": "Great Bell (Big Ben is the tower)",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_287",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which Chilean monument consists of massive stone statues?",
        "options": ["Easter Island Moai", "Cristo Redentor de los Andes", "La Portada", "Torres del Paine"],
        "correct_answer": "Easter Island Moai",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_288",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "What is the name of the giant Buddha statue in Afghanistan destroyed in 2001?",
        "options": ["Buddhas of Bamiyan", "Leshan Giant Buddha", "Ushiku Daibutsu", "Tian Tan Buddha"],
        "correct_answer": "Buddhas of Bamiyan",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_289",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which monument in Turkey was originally a Byzantine cathedral?",
        "options": ["Hagia Sophia", "Blue Mosque", "Topkapi Palace", "Galata Tower"],
        "correct_answer": "Hagia Sophia",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_290",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "What is the name of the prehistoric monument in Malta?",
        "options": ["Ħaġar Qim", "Stonehenge", "Newgrange", "Carnac"],
        "correct_answer": "Ħaġar Qim",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_291",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which monument in Brazil was voted one of the New Seven Wonders?",
        "options": ["Christ the Redeemer", "Iguazu Falls", "Sugarloaf Mountain", "Amazon Theatre"],
        "correct_answer": "Christ the Redeemer",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_292",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "What is the name of the terracotta army's burial site in China?",
        "options": ["Mausoleum of Qin Shi Huang", "Ming Tombs", "Shaolin Temple", "Summer Palace"],
        "correct_answer": "Mausoleum of Qin Shi Huang",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_293",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which monument in India is known as the 'Victory Tower'?",
        "options": ["Qutub Minar", "Charminar", "India Gate", "Gateway of India"],
        "correct_answer": "Qutub Minar",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_294",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "What is the name of the ancient amphitheater in Verona?",
        "options": ["Arena di Verona", "Colosseum", "Theatre of Marcellus", "Teatro Romano"],
        "correct_answer": "Arena di Verona",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_295",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which monument in Mexico is a pre-Columbian pyramid?",
        "options": ["Pyramid of the Sun", "El Castillo", "Pyramid of Cholula", "All of the above"],
        "correct_answer": "All of the above",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_296",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "What is the name of the ancient city in Yemen known for unique architecture?",
        "options": ["Shibam", "Sana'a", "Aden", "Tarim"],
        "correct_answer": "Shibam",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_297",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which monument was designed by Maya Lin?",
        "options": ["Vietnam Veterans Memorial", "Korean War Memorial", "Lincoln Memorial", "World War II Memorial"],
        "correct_answer": "Vietnam Veterans Memorial",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_298",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "What is the name of the temple complex in Bagan, Myanmar?",
        "options": ["Thousands of pagodas (no single name)", "Shwedagon Pagoda", "Ananda Temple", "Dhammayangyi Temple"],
        "correct_answer": "Thousands of pagodas (no single name)",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_299",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "Which monument in Ethiopia is a collection of rock-hewn churches?",
        "options": ["Lalibela", "Axum", "Gondar", "Tiya"],
        "correct_answer": "Lalibela",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "geo_300",
        "category": "Geography",
        "subcategory": "Landmarks & Monuments",
        "question": "What is the name of the ancient library in Turkey (now ruins)?",
        "options": ["Library of Celsus", "Library of Alexandria", "Library of Pergamon", "Library of Constantinople"],
        "correct_answer": "Library of Celsus",
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

print("✅ Added 60 Landmarks & Monuments questions")
print(f"Geography now has {len(data['categories']['Geography'])} total questions")

# Count Landmarks & Monuments
landmarks = [q for q in data['categories']['Geography'] if q['subcategory'] == 'Landmarks & Monuments']
print(f"Landmarks & Monuments: {len(landmarks)} questions")

# Count by difficulty
easy = len([q for q in new_questions if q['difficulty'] == 'easy'])
medium = len([q for q in new_questions if q['difficulty'] == 'medium'])
hard = len([q for q in new_questions if q['difficulty'] == 'hard'])
print(f"Added: {easy} easy, {medium} medium, {hard} hard")
