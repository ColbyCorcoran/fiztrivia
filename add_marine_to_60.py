#!/usr/bin/env python3
"""
Add 44 new Oceans & Marine Life questions to reach 60 total

Distribution:
- Easy: 13 questions (30%)
- Medium: 18 questions (40%)
- Hard: 13 questions (30%)
"""

import json

# IDs will be nat_301 through nat_344

new_questions = [
    # EASY (13 questions)
    {"id": "nat_301", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What is the largest ocean on Earth?", "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], "correct_answer": "Pacific Ocean", "difficulty": "easy"},
    {"id": "nat_302", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What is the largest mammal in the ocean?", "options": ["Blue whale", "Humpback whale", "Orca", "Sperm whale"], "correct_answer": "Blue whale", "difficulty": "easy"},
    {"id": "nat_303", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What type of fish is Nemo from the movie Finding Nemo?", "options": ["Clownfish", "Angelfish", "Tang", "Butterflyfish"], "correct_answer": "Clownfish", "difficulty": "easy"},
    {"id": "nat_304", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What do whales breathe through on top of their heads?", "options": ["Blowhole", "Gills", "Nostrils", "Spiracle"], "correct_answer": "Blowhole", "difficulty": "easy"},
    {"id": "nat_305", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What is a baby seal called?", "options": ["Pup", "Calf", "Kit", "Cub"], "correct_answer": "Pup", "difficulty": "easy"},
    {"id": "nat_306", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What color is a polar bear's skin underneath its fur?", "options": ["Black", "White", "Pink", "Brown"], "correct_answer": "Black", "difficulty": "easy"},
    {"id": "nat_307", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What do sea turtles use to navigate during migration?", "options": ["Earth's magnetic field", "Stars", "Sun position", "Ocean currents only"], "correct_answer": "Earth's magnetic field", "difficulty": "easy"},
    {"id": "nat_308", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What is the hard outer structure of coral made from?", "options": ["Calcium carbonate", "Silica", "Chitin", "Keratin"], "correct_answer": "Calcium carbonate", "difficulty": "easy"},
    {"id": "nat_309", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "How many arms does a typical starfish have?", "options": ["5", "6", "8", "4"], "correct_answer": "5", "difficulty": "easy"},
    {"id": "nat_310", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What do jellyfish lack that most animals have?", "options": ["Brain", "Heart", "Stomach", "All of the above"], "correct_answer": "All of the above", "difficulty": "easy"},
    {"id": "nat_311", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What is the fastest fish in the ocean?", "options": ["Sailfish", "Marlin", "Tuna", "Swordfish"], "correct_answer": "Sailfish", "difficulty": "easy"},
    {"id": "nat_312", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What marine animal has three hearts?", "options": ["Octopus", "Squid", "Cuttlefish", "Nautilus"], "correct_answer": "Octopus", "difficulty": "easy"},
    {"id": "nat_313", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What is the Great Barrier Reef primarily made of?", "options": ["Coral", "Rock", "Sand", "Shells"], "correct_answer": "Coral", "difficulty": "easy"},

    # MEDIUM (18 questions)
    {"id": "nat_314", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What percentage of Earth's surface is covered by oceans?", "options": ["71%", "60%", "80%", "50%"], "correct_answer": "71%", "difficulty": "medium"},
    {"id": "nat_315", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What is the deepest part of the ocean called?", "options": ["Mariana Trench", "Tonga Trench", "Philippine Trench", "Puerto Rico Trench"], "correct_answer": "Mariana Trench", "difficulty": "medium"},
    {"id": "nat_316", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What ocean current helps warm Western Europe's climate?", "options": ["Gulf Stream", "Kuroshio Current", "California Current", "Humboldt Current"], "correct_answer": "Gulf Stream", "difficulty": "medium"},
    {"id": "nat_317", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What is the study of oceans called?", "options": ["Oceanography", "Marine biology", "Hydrology", "Limnology"], "correct_answer": "Oceanography", "difficulty": "medium"},
    {"id": "nat_318", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What marine mammal is known for using tools to open shellfish?", "options": ["Sea otter", "Seal", "Walrus", "Sea lion"], "correct_answer": "Sea otter", "difficulty": "medium"},
    {"id": "nat_319", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What is bioluminescence in marine animals?", "options": ["Production of light through chemical reactions", "Reflection of sunlight", "Absorption of light", "Camouflage ability"], "correct_answer": "Production of light through chemical reactions", "difficulty": "medium"},
    {"id": "nat_320", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "Which whale species is known for its complex songs?", "options": ["Humpback whale", "Blue whale", "Gray whale", "Minke whale"], "correct_answer": "Humpback whale", "difficulty": "medium"},
    {"id": "nat_321", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What is the symbiotic relationship between clownfish and sea anemones called?", "options": ["Mutualism", "Commensalism", "Parasitism", "Competition"], "correct_answer": "Mutualism", "difficulty": "medium"},
    {"id": "nat_322", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What type of whale is an orca actually classified as?", "options": ["Dolphin", "Porpoise", "Baleen whale", "Seal"], "correct_answer": "Dolphin", "difficulty": "medium"},
    {"id": "nat_323", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What is the most venomous marine creature?", "options": ["Box jellyfish", "Blue-ringed octopus", "Stonefish", "Cone snail"], "correct_answer": "Box jellyfish", "difficulty": "medium"},
    {"id": "nat_324", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "How do dolphins primarily communicate?", "options": ["Echolocation clicks and whistles", "Body language only", "Color changes", "Chemical signals"], "correct_answer": "Echolocation clicks and whistles", "difficulty": "medium"},
    {"id": "nat_325", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What is the largest species of ray?", "options": ["Manta ray", "Stingray", "Eagle ray", "Electric ray"], "correct_answer": "Manta ray", "difficulty": "medium"},
    {"id": "nat_326", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What marine animal has the largest eyes in the animal kingdom?", "options": ["Giant squid", "Blue whale", "Great white shark", "Whale shark"], "correct_answer": "Giant squid", "difficulty": "medium"},
    {"id": "nat_327", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What is the average depth of the ocean?", "options": ["3,688 meters", "2,000 meters", "5,000 meters", "1,500 meters"], "correct_answer": "3,688 meters", "difficulty": "medium"},
    {"id": "nat_328", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What do manatees primarily eat?", "options": ["Seagrass and aquatic plants", "Fish", "Plankton", "Crustaceans"], "correct_answer": "Seagrass and aquatic plants", "difficulty": "medium"},
    {"id": "nat_329", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "Which male marine animal becomes pregnant and gives birth?", "options": ["Seahorse", "Pipefish", "Sea dragon", "All of the above"], "correct_answer": "All of the above", "difficulty": "medium"},
    {"id": "nat_330", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What is the zone of the ocean that receives sunlight called?", "options": ["Epipelagic zone", "Mesopelagic zone", "Bathypelagic zone", "Abyssopelagic zone"], "correct_answer": "Epipelagic zone", "difficulty": "medium"},
    {"id": "nat_331", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What causes ocean tides?", "options": ["Gravitational pull of the moon and sun", "Wind", "Earth's rotation only", "Ocean currents"], "correct_answer": "Gravitational pull of the moon and sun", "difficulty": "medium"},

    # HARD (13 questions)
    {"id": "nat_332", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What is the scientific name for a killer whale?", "options": ["Orcinus orca", "Delphinapterus leucas", "Physeter macrocephalus", "Balaenoptera musculus"], "correct_answer": "Orcinus orca", "difficulty": "hard"},
    {"id": "nat_333", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What depth does the hadal zone begin at in the ocean?", "options": ["6,000 meters", "4,000 meters", "8,000 meters", "10,000 meters"], "correct_answer": "6,000 meters", "difficulty": "hard"},
    {"id": "nat_334", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What is the phenomenon called when coral expels its symbiotic algae due to stress?", "options": ["Coral bleaching", "Coral spawning", "Coral degradation", "Coral mortality"], "correct_answer": "Coral bleaching", "difficulty": "hard"},
    {"id": "nat_335", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What whale species has the longest migration route?", "options": ["Gray whale", "Humpback whale", "Blue whale", "Minke whale"], "correct_answer": "Gray whale", "difficulty": "hard"},
    {"id": "nat_336", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What is the term for the tiny organisms that drift in ocean currents and form the base of the marine food web?", "options": ["Plankton", "Krill", "Algae", "Bacteria"], "correct_answer": "Plankton", "difficulty": "hard"},
    {"id": "nat_337", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What unique hunting technique do humpback whales use involving bubbles?", "options": ["Bubble net feeding", "Bubble screen feeding", "Bubble trap feeding", "Bubble circle feeding"], "correct_answer": "Bubble net feeding", "difficulty": "hard"},
    {"id": "nat_338", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What is the largest bony fish in the ocean?", "options": ["Ocean sunfish (Mola mola)", "Swordfish", "Marlin", "Tuna"], "correct_answer": "Ocean sunfish (Mola mola)", "difficulty": "hard"},
    {"id": "nat_339", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "Which ocean trench is the deepest point on Earth?", "options": ["Challenger Deep in the Mariana Trench", "Tonga Trench", "Philippine Trench", "Kermadec Trench"], "correct_answer": "Challenger Deep in the Mariana Trench", "difficulty": "hard"},
    {"id": "nat_340", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What is the lifespan of a Greenland shark, one of the longest-living vertebrates?", "options": ["400+ years", "200 years", "100 years", "50 years"], "correct_answer": "400+ years", "difficulty": "hard"},
    {"id": "nat_341", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What marine animal has a beak similar to a parrot and is known for its intelligence?", "options": ["Octopus", "Squid", "Cuttlefish", "All of the above"], "correct_answer": "All of the above", "difficulty": "hard"},
    {"id": "nat_342", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What is the only mammal that spends its entire life in the ocean without ever coming to land?", "options": ["Cetaceans (whales, dolphins, porpoises)", "Seals", "Sea otters", "Manatees"], "correct_answer": "Cetaceans (whales, dolphins, porpoises)", "difficulty": "hard"},
    {"id": "nat_343", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What is the process called when nutrients from deep ocean waters rise to the surface?", "options": ["Upwelling", "Downwelling", "Thermocline", "Halocline"], "correct_answer": "Upwelling", "difficulty": "hard"},
    {"id": "nat_344", "category": "Nature", "subcategory": "Oceans & Marine Life", "question": "What whale species is known for its spiral tusk and is called the 'unicorn of the sea'?", "options": ["Narwhal", "Beluga", "Bowhead whale", "Orca"], "correct_answer": "Narwhal", "difficulty": "hard"}
]

def add_marine_questions():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    nature_questions = data['categories']['Nature']

    print(f"Current Nature questions: {len(nature_questions)}")
    print(f"Adding {len(new_questions)} new Oceans & Marine Life questions...")

    # Add new questions
    nature_questions.extend(new_questions)

    data['categories']['Nature'] = nature_questions

    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Added {len(new_questions)} Oceans & Marine Life questions")
    print(f"New total: {len(nature_questions)} Nature questions")

    # Verify distribution
    from collections import defaultdict
    by_subcat = defaultdict(int)
    for q in nature_questions:
        by_subcat[q['subcategory']] += 1

    print("\nNature subcategory distribution:")
    for subcat in sorted(by_subcat.keys()):
        print(f"  {subcat}: {by_subcat[subcat]}")

if __name__ == "__main__":
    add_marine_questions()
