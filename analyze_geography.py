#!/usr/bin/env python3
"""
Analyze Geography questions and propose distribution across 5 subcategories
"""

import json

def analyze_geography_questions():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    earth = data['categories']['Earth']
    geo_questions = [q for q in earth if q.get('subcategory') == 'Geography']

    print(f"Total Geography questions: {len(geo_questions)}\n")
    print("=" * 80)
    print("ALL GEOGRAPHY QUESTIONS:")
    print("=" * 80)

    # Proposed subcategories
    us_geo = []
    world_geo = []
    flags = []
    landmarks = []
    maps_borders = []
    unclear = []

    # Keywords for classification
    us_keywords = ['united states', 'u.s.', 'usa', 'american', 'california', 'texas',
                   'new york', 'florida', 'state capital', 'state']
    flag_keywords = ['flag', 'colors', 'stripe', 'star on']
    landmark_keywords = ['tower', 'monument', 'statue', 'building', 'bridge', 'temple',
                         'palace', 'cathedral', 'pyramid']
    border_keywords = ['border', 'boundary', 'continent', 'hemisphere']

    for i, q in enumerate(geo_questions, 1):
        question_lower = q['question'].lower()

        # Try to classify
        category = None
        if any(keyword in question_lower for keyword in flag_keywords):
            category = "FLAGS"
            flags.append(q)
        elif any(keyword in question_lower for keyword in us_keywords):
            category = "U.S. GEOGRAPHY"
            us_geo.append(q)
        elif any(keyword in question_lower for keyword in landmark_keywords):
            category = "LANDMARKS & MONUMENTS"
            landmarks.append(q)
        elif any(keyword in question_lower for keyword in border_keywords):
            category = "MAPS & BORDERS"
            maps_borders.append(q)
        else:
            category = "WORLD GEOGRAPHY (default)"
            world_geo.append(q)

        print(f"\n{i}. [{q['id']}] [{category}]")
        print(f"   Difficulty: {q['difficulty']}")
        print(f"   Q: {q['question']}")
        print(f"   A: {q['correct_answer']}")

    print("\n" + "=" * 80)
    print("PROPOSED DISTRIBUTION:")
    print("=" * 80)
    print(f"U.S. Geography: {len(us_geo)} questions")
    print(f"World Geography: {len(world_geo)} questions")
    print(f"Flags: {len(flags)} questions")
    print(f"Landmarks & Monuments: {len(landmarks)} questions")
    print(f"Maps & Borders: {len(maps_borders)} questions")
    print(f"\nTotal: {len(geo_questions)} questions")

if __name__ == "__main__":
    analyze_geography_questions()
