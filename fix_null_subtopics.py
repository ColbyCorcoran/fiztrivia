#!/usr/bin/env python3
"""
Fix null subtopics in expansion packs by intelligently assigning based on question content.
"""

import json
import re
from pathlib import Path

# Define keyword patterns for each pack's subtopics
SUBTOPIC_KEYWORDS = {
    "Harry Potter": {
        "Characters": ["harry", "hermione", "ron", "dumbledore", "snape", "voldemort", "character", "who is", "whose"],
        "Spells & Magic": ["spell", "curse", "charm", "jinx", "hex", "wand", "magic", "potion"],
        "Hogwarts": ["hogwarts", "house", "gryffindor", "slytherin", "ravenclaw", "hufflepuff", "school", "classroom"],
        "Books & Plot": ["book", "chapter", "story", "plot", "happened", "event", "year"],
        "Movies": ["movie", "film", "actor", "actress", "played", "scene"],
        "Magical Creatures": ["creature", "dragon", "phoenix", "hippogriff", "basilisk", "animal", "beast"],
        "Wizarding World": ["ministry", "quidditch", "muggle", "wizard", "witch", "world", "society"]
    },
    "Pokémon": {
        "Pokémon Species": ["pikachu", "charizard", "bulbasaur", "squirtle", "eevee", "pokémon", "species", "type"],
        "Games": ["game", "version", "red", "blue", "gold", "silver", "ruby", "sapphire", "diamond", "pearl"],
        "Moves & Abilities": ["move", "attack", "ability", "damage", "power", "effect"],
        "Trainers & Characters": ["ash", "trainer", "gym", "leader", "champion", "character", "who"],
        "Anime & Movies": ["anime", "episode", "series", "movie", "show"],
        "Types & Evolution": ["type", "evolve", "evolution", "stage", "form"],
        "Regions & Locations": ["region", "city", "town", "route", "location", "where", "kanto", "johto"]
    },
    "The Office": {
        "Characters": ["michael", "jim", "pam", "dwight", "andy", "angela", "kevin", "character", "who"],
        "Episodes": ["episode", "season", "titled", "called"],
        "Quotes": ["said", "quote", "line", "famous"],
        "Relationships": ["relationship", "dating", "married", "couple", "love"],
        "Locations": ["office", "building", "scranton", "location", "where"],
        "Trivia": ["company", "business", "work", "job", "event"]
    }
}

def classify_question(question_text, subtopics_keywords):
    """Classify a question into the most likely subtopic based on keywords."""
    question_lower = question_text.lower()

    scores = {}
    for subtopic, keywords in subtopics_keywords.items():
        score = sum(1 for keyword in keywords if keyword in question_lower)
        if score > 0:
            scores[subtopic] = score

    if scores:
        # Return subtopic with highest score
        return max(scores, key=scores.get)

    # Default to first subtopic if no matches
    return list(subtopics_keywords.keys())[0]

def fix_pack(file_path):
    """Fix null subtopics in a pack."""
    with open(file_path, 'r') as f:
        data = json.load(f)

    pack_name = data['packName']

    if pack_name not in SUBTOPIC_KEYWORDS:
        print(f"⚠️  No keywords defined for {pack_name}, skipping...")
        return

    keywords = SUBTOPIC_KEYWORDS[pack_name]
    fixed_count = 0

    # Fix free preview questions
    for question in data['freePreviewQuestions']:
        if question.get('subtopic') is None:
            new_subtopic = classify_question(question['question'], keywords)
            question['subtopic'] = new_subtopic
            fixed_count += 1
            print(f"  {question['id']}: → {new_subtopic}")

    # Fix paid questions
    for question in data['paidQuestions']:
        if question.get('subtopic') is None:
            new_subtopic = classify_question(question['question'], keywords)
            question['subtopic'] = new_subtopic
            fixed_count += 1

    if fixed_count > 0:
        # Write back
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✅ {pack_name}: Fixed {fixed_count} null subtopics\n")
    else:
        print(f"✅ {pack_name}: No null subtopics found\n")

def main():
    packs_dir = Path("/Users/colbycorcoran/Documents/App Development/Fiz/Fiz/Resources/Expansion Packs")

    for pack_file in sorted(packs_dir.glob("expansion_*.json")):
        print(f"=== Processing {pack_file.name} ===")
        fix_pack(pack_file)

if __name__ == "__main__":
    main()
