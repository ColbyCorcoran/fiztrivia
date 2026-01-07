#!/usr/bin/env python3
"""
Assign appropriate subtopics to base game questions from expansion packs.
This ensures questions appear correctly on the wheel in Single Topic Mode.
"""

import json

# Define subtopic mappings for each question
SUBTOPIC_ASSIGNMENTS = {
    # Harry Potter questions
    "lit_001": "Characters",  # Harry's owl (Hedwig)
    "lit_004": "Spells & Magic",  # Disarming spell (Expelliarmus)
    "lit_007": "Wizarding World",  # Time-Turner
    "lit_009": "Characters",  # Harry's parents
    "lit_011": "Hogwarts",  # Quidditch position
    "lit_016": "Wizarding World",  # Basilisk fang for diary
    "lit_024": "Characters",  # Hermione's middle name
    "lit_025": "Characters",  # Ron's rat (Scabbers)
    "lit_030": "Spells & Magic",  # Patronus charm
    "lit_033": "Books & Plot",  # Tales of Beedle the Bard

    # Pokémon questions
    "tec_001": "Pokémon Species",  # First in Pokédex (Bulbasaur)
    "tec_002": "Types & Evolution",  # Pikachu's type
    "tec_005": "Games",  # Item to catch Pokémon (Pokéball)
    "tec_009": "Pokémon Species",  # Legendary Fire (Moltres)
    "tec_010": "Types & Evolution",  # Magikarp evolution
    "tec_012": "Types & Evolution",  # Psyduck's type
    "tec_014": "Pokémon Species",  # Virtual Pokémon (Porygon)
    "tec_024": "Pokémon Species",  # Sleep song (Jigglypuff)
    "tec_032": "Types & Evolution",  # Gengar's type
    "tec_033": "Types & Evolution",  # Alakazam's type

    # The Office questions
    "ent_031": "Trivia",  # Company name (Dunder Mifflin)
    "ent_032": "Episodes",  # Stapler in Jello
    "ent_033": "Characters",  # Dwight's farm (Beets)
    "ent_034": "Characters",  # Jim's last name (Halpert)
    "ent_035": "Characters",  # Kevin's favorite food (Chili)
    "ent_036": "Episodes",  # Michael hits Meredith
    "ent_037": "Characters",  # Creed's job title
    "ent_038": "Episodes",  # The Injury episode (George Foreman Grill)
    "ent_039": "Characters",  # Angela's cat (Sprinkles)
    "ent_040": "Characters",  # Stamford manager (Josh Porter)
}


def assign_subtopics(questions_path: str):
    """Assign subtopics to base game questions."""

    # Load questions database
    with open(questions_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Track assignments
    assigned = 0

    # Iterate through all categories and questions
    for category_name, questions in data['categories'].items():
        for question in questions:
            question_id = question.get('id')

            # Check if this question needs a subtopic assigned
            if question_id in SUBTOPIC_ASSIGNMENTS:
                # Verify it has a topic but no subtopic
                if question.get('topic') and not question.get('subtopic'):
                    question['subtopic'] = SUBTOPIC_ASSIGNMENTS[question_id]
                    assigned += 1
                    print(f"✓ Assigned '{question['subtopic']}' to {question_id}: {question['question'][:50]}...")

    # Save updated database
    with open(questions_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Successfully assigned {assigned} subtopics!")
    return assigned


if __name__ == "__main__":
    questions_path = "/Users/colbycorcoran/Documents/App Development/Fiz/Fiz/Resources/questions.json"
    assigned = assign_subtopics(questions_path)

    if assigned == len(SUBTOPIC_ASSIGNMENTS):
        print(f"✅ All {len(SUBTOPIC_ASSIGNMENTS)} questions successfully assigned subtopics!")
    else:
        print(f"⚠️  Warning: Expected {len(SUBTOPIC_ASSIGNMENTS)} assignments, but only assigned {assigned}")
