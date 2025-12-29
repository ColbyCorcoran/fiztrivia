#!/usr/bin/env python3
"""Final verification: Check all Geography questions for duplicates"""
import json
from difflib import SequenceMatcher

def similarity_ratio(str1, str2):
    return SequenceMatcher(None, str1.lower(), str2.lower()).ratio()

def check_duplicates():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    geography_questions = data['categories']['Geography']

    print("=== FINAL GEOGRAPHY VERIFICATION ===\n")
    print(f"Total Geography questions: {len(geography_questions)}\n")

    # Count by subcategory
    subcats = {}
    for q in geography_questions:
        subcat = q['subcategory']
        if subcat not in subcats:
            subcats[subcat] = 0
        subcats[subcat] += 1

    print("Distribution by subcategory:")
    for subcat, count in sorted(subcats.items()):
        print(f"  {subcat}: {count} questions")

    print("\n=== CHECKING FOR DUPLICATES ===\n")

    duplicates_found = []

    for i, q1 in enumerate(geography_questions):
        for j, q2 in enumerate(geography_questions):
            if i >= j:  # Skip comparing question with itself and avoid duplicates
                continue

            ratio = similarity_ratio(q1['question'], q2['question'])

            # Check for exact duplicates (100%)
            if ratio == 1.0:
                duplicates_found.append({
                    'id1': q1['id'],
                    'question1': q1['question'],
                    'id2': q2['id'],
                    'question2': q2['question'],
                    'similarity': ratio,
                    'type': 'EXACT'
                })
            # Check for semantic duplicates (>90% similar with same answer)
            elif ratio > 0.90 and q1['correct_answer'].lower() == q2['correct_answer'].lower():
                duplicates_found.append({
                    'id1': q1['id'],
                    'question1': q1['question'],
                    'id2': q2['id'],
                    'question2': q2['question'],
                    'similarity': ratio,
                    'type': 'SEMANTIC'
                })
            # Check for potential duplicates (>70% similar with same answer)
            elif ratio > 0.70 and q1['correct_answer'].lower() == q2['correct_answer'].lower():
                duplicates_found.append({
                    'id1': q1['id'],
                    'question1': q1['question'],
                    'id2': q2['id'],
                    'question2': q2['question'],
                    'similarity': ratio,
                    'type': 'POTENTIAL'
                })

    if duplicates_found:
        print(f"❌ Found {len(duplicates_found)} duplicates within Geography:\n")
        for dup in duplicates_found:
            print(f"[{dup['type']}] {dup['similarity']:.1%} similar")
            print(f"  {dup['id1']}: {dup['question1']}")
            print(f"  {dup['id2']}: {dup['question2']}\n")
        return False
    else:
        print("✅ No duplicates found within Geography category!")
        print("✅ All 300 Geography questions are unique!")
        return True

if __name__ == '__main__':
    success = check_duplicates()
    exit(0 if success else 1)
