#!/usr/bin/env python3
"""
Remove Oceans & Marine Life subcategory from Nature:
1. Move 16 original marine questions back to Animals & Wildlife
2. Delete 44 newly created marine questions
3. Remove Oceans & Marine Life as a subcategory
"""

import json

# The 16 original question IDs that were moved from Animals & Wildlife
ORIGINAL_MARINE_IDS = [
    'nat_012', 'nat_016', 'nat_041', 'nat_042', 'nat_066', 'nat_087',
    'nat_093', 'nat_135', 'nat_154', 'nat_158', 'nat_169', 'nat_189',
    'nat_193', 'nat_195', 'nat_199', 'nat_221'
]

def remove_marine_subcategory():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    nature_questions = data['categories']['Nature']

    print("=" * 80)
    print("REMOVING OCEANS & MARINE LIFE SUBCATEGORY")
    print("=" * 80)
    print(f"\nCurrent Nature total: {len(nature_questions)} questions\n")

    # Count current distribution
    subcats = {}
    for q in nature_questions:
        subcat = q['subcategory']
        if subcat not in subcats:
            subcats[subcat] = 0
        subcats[subcat] += 1

    print("Current distribution:")
    for subcat, count in sorted(subcats.items()):
        print(f"  {subcat}: {count}")

    # Process questions
    questions_to_keep = []
    moved_back = 0
    deleted = 0

    for q in nature_questions:
        if q['subcategory'] == 'Oceans & Marine Life':
            if q['id'] in ORIGINAL_MARINE_IDS:
                # Move back to Animals & Wildlife
                q['subcategory'] = 'Animals & Wildlife'
                questions_to_keep.append(q)
                moved_back += 1
                print(f"  Moving back: {q['id']} - {q['question'][:60]}...")
            else:
                # Delete (newly created marine questions)
                deleted += 1
                print(f"  Deleting: {q['id']} - {q['question'][:60]}...")
        else:
            # Keep all non-marine questions
            questions_to_keep.append(q)

    print(f"\n" + "=" * 80)
    print(f"SUMMARY")
    print("=" * 80)
    print(f"Moved back to Animals & Wildlife: {moved_back}")
    print(f"Deleted: {deleted}")
    print(f"Original count: {len(nature_questions)}")
    print(f"New count: {len(questions_to_keep)}")
    print(f"Net change: {len(questions_to_keep) - len(nature_questions)}")

    # Count new distribution
    new_subcats = {}
    for q in questions_to_keep:
        subcat = q['subcategory']
        if subcat not in new_subcats:
            new_subcats[subcat] = 0
        new_subcats[subcat] += 1

    print(f"\nNew distribution:")
    for subcat, count in sorted(new_subcats.items()):
        print(f"  {subcat}: {count}")

    # Update database
    data['categories']['Nature'] = questions_to_keep

    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("\n✓ Oceans & Marine Life subcategory removed")
    print(f"✓ Nature now has {len(questions_to_keep)} questions")

if __name__ == "__main__":
    remove_marine_subcategory()
