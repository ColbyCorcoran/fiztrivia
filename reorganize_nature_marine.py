#!/usr/bin/env python3
"""
Reorganize Nature category to add "Oceans & Marine Life" subcategory
Move marine-related questions from Animals & Wildlife to the new subcategory
"""

import json

# Marine-related keywords to identify questions
marine_keywords = [
    'ocean', 'sea', 'marine', 'whale', 'dolphin', 'shark', 'fish',
    'coral', 'reef', 'squid', 'octopus', 'jellyfish', 'seal',
    'penguin', 'orca', 'starfish', 'seahorse', 'crab', 'lobster',
    'turtle', 'walrus', 'eel', 'ray', 'salmon', 'tuna', 'clownfish',
    'nautilus', 'shrimp', 'krill', 'plankton', 'kelp', 'seaweed',
    'tide', 'wave', 'saltwater', 'aquatic', 'underwater'
]

def is_marine_question(question_text):
    """Check if a question is marine-related"""
    text_lower = question_text.lower()
    return any(keyword in text_lower for keyword in marine_keywords)

def reorganize_nature():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    nature_questions = data['categories']['Nature']

    print("=" * 80)
    print("REORGANIZING NATURE CATEGORY")
    print("=" * 80)
    print(f"\nTotal Nature questions: {len(nature_questions)}")

    # Separate questions by current subcategory
    animals_wildlife = [q for q in nature_questions if q['subcategory'] == 'Animals & Wildlife']
    plants_flowers = [q for q in nature_questions if q['subcategory'] == 'Plants & Flowers']
    trees = [q for q in nature_questions if q['subcategory'] == 'Trees']
    weather = [q for q in nature_questions if q['subcategory'] == 'Weather']

    print(f"\nCurrent distribution:")
    print(f"  Animals & Wildlife: {len(animals_wildlife)}")
    print(f"  Plants & Flowers: {len(plants_flowers)}")
    print(f"  Trees: {len(trees)}")
    print(f"  Weather: {len(weather)}")

    # Identify marine questions in Animals & Wildlife
    marine_questions = []
    non_marine_animals = []

    for q in animals_wildlife:
        if is_marine_question(q['question']):
            # Change subcategory to Oceans & Marine Life
            q['subcategory'] = 'Oceans & Marine Life'
            marine_questions.append(q)
            print(f"\n  Moving to marine: {q['question'][:70]}...")
        else:
            non_marine_animals.append(q)

    print(f"\n" + "=" * 80)
    print(f"MOVED {len(marine_questions)} questions to 'Oceans & Marine Life'")
    print("=" * 80)

    # Rebuild nature_questions with new organization
    reorganized = non_marine_animals + plants_flowers + trees + weather + marine_questions

    print(f"\nNew distribution:")
    print(f"  Animals & Wildlife: {len(non_marine_animals)}")
    print(f"  Plants & Flowers: {len(plants_flowers)}")
    print(f"  Trees: {len(trees)}")
    print(f"  Weather: {len(weather)}")
    print(f"  Oceans & Marine Life: {len(marine_questions)}")
    print(f"\nTotal: {len(reorganized)} questions")

    # Update database
    data['categories']['Nature'] = reorganized

    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("\n✓ Nature category reorganized")
    print(f"\nTarget for 300 total with 5 subcategories: 60 each")
    print(f"\nQuestions needed to reach 60 per subcategory:")
    print(f"  Animals & Wildlife: {60 - len(non_marine_animals)} ({len(non_marine_animals)} → 60)")
    print(f"  Plants & Flowers: {60 - len(plants_flowers)} ({len(plants_flowers)} → 60)")
    print(f"  Trees: {60 - len(trees)} ({len(trees)} → 60)")
    print(f"  Weather: {60 - len(weather)} ({len(weather)} → 60)")
    print(f"  Oceans & Marine Life: {60 - len(marine_questions)} ({len(marine_questions)} → 60)")

if __name__ == "__main__":
    reorganize_nature()
