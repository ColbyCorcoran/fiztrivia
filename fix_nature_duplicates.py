#!/usr/bin/env python3
"""
Replace 15 duplicate Nature questions with unique ones
"""

import json

with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

nature_questions = data['categories']['Nature']

# Remove 15 duplicates
ids_to_replace = ['nat_231', 'nat_234', 'nat_235', 'nat_237', 'nat_238', 'nat_245', 'nat_255', 'nat_267', 'nat_268', 'nat_288', 'nat_291', 'nat_292', 'nat_293', 'nat_300']

nature_questions = [q for q in nature_questions if q['id'] not in ids_to_replace]

# NEW unique replacements (14 needed, one was counted twice)
replacements = [
    # Trees
    {"id": "nat_231", "category": "Nature", "subcategory": "Trees", "question": "What tree is known for producing sweet sap used in syrup production in spring?", "options": ["Sugar maple", "Black maple", "Red maple", "Silver maple"], "correct_answer": "Sugar maple", "difficulty": "easy"},
    {"id": "nat_234", "category": "Nature", "subcategory": "Trees", "question": "What is the term for trees that retain their needles year-round?", "options": ["Coniferous evergreens", "Deciduous", "Broadleaf", "Tropical"], "correct_answer": "Coniferous evergreens", "difficulty": "easy"},
    {"id": "nat_235", "category": "Nature", "subcategory": "Trees", "question": "What tropical tree produces cacao beans for chocolate?", "options": ["Cacao tree (Theobroma cacao)", "Coffee tree", "Rubber tree", "Banana tree"], "correct_answer": "Cacao tree (Theobroma cacao)", "difficulty": "easy"},
    {"id": "nat_237", "category": "Nature", "subcategory": "Trees", "question": "What tree has bark that naturally peels in papery layers?", "options": ["Birch", "Sycamore", "Eucalyptus", "All of the above"], "correct_answer": "All of the above", "difficulty": "medium"},
    {"id": "nat_238", "category": "Nature", "subcategory": "Trees", "question": "What is the state tree of California?", "options": ["Coast redwood", "Giant sequoia", "Douglas fir", "Joshua tree"], "correct_answer": "Coast redwood", "difficulty": "medium"},
    {"id": "nat_245", "category": "Nature", "subcategory": "Trees", "question": "What African tree can store thousands of gallons of water in its trunk?", "options": ["Baobab", "Acacia", "Marula", "Fever tree"], "correct_answer": "Baobab", "difficulty": "medium"},
    {"id": "nat_255", "category": "Nature", "subcategory": "Trees", "question": "What wood is traditionally used for violin bows?", "options": ["Pernambuco", "Ebony", "Rosewood", "Maple"], "correct_answer": "Pernambuco", "difficulty": "hard"},
    
    # Plants & Flowers
    {"id": "nat_267", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What aquatic plant has leaves so large they can support the weight of a small child?", "options": ["Victoria amazonica (giant water lily)", "Lotus", "Water hyacinth", "Cattail"], "correct_answer": "Victoria amazonica (giant water lily)", "difficulty": "easy"},
    {"id": "nat_268", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What flowering plant is used to make tequila?", "options": ["Blue agave", "Aloe vera", "Prickly pear", "Century plant"], "correct_answer": "Blue agave", "difficulty": "easy"},
    
    # Weather
    {"id": "nat_288", "category": "Nature", "subcategory": "Weather", "question": "What is the phenomenon where warm air traps cooler air near the surface?", "options": ["Temperature inversion", "Thermal", "Convection", "Subsidence"], "correct_answer": "Temperature inversion", "difficulty": "medium"},
    {"id": "nat_291", "category": "Nature", "subcategory": "Weather", "question": "What are wispy, high-altitude clouds made of ice crystals called?", "options": ["Cirrus", "Cumulus", "Stratus", "Nimbus"], "correct_answer": "Cirrus", "difficulty": "medium"},
    {"id": "nat_292", "category": "Nature", "subcategory": "Weather", "question": "What is the rotating column of air at the center of a tornado called?", "options": ["Vortex", "Eye", "Funnel", "Core"], "correct_answer": "Vortex", "difficulty": "medium"},
    {"id": "nat_293", "category": "Nature", "subcategory": "Weather", "question": "What is the boundary between two air masses of different temperatures called?", "options": ["Front", "Jet stream", "Pressure gradient", "Thermocline"], "correct_answer": "Front", "difficulty": "medium"},
    {"id": "nat_300", "category": "Nature", "subcategory": "Weather", "question": "What is a sudden, violent windstorm in mountainous areas called?", "options": ["Foehn wind", "Katabatic wind", "Chinook", "Williwaw"], "correct_answer": "Williwaw", "difficulty": "hard"}
]

nature_questions.extend(replacements)
data['categories']['Nature'] = nature_questions

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✓ Replaced 14 duplicate questions with unique ones")
print(f"Nature total: {len(nature_questions)} questions")
