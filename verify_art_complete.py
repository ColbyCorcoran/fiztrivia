#!/usr/bin/env python3
"""Comprehensive duplicate verification for all 300 Art questions"""
import json
from difflib import SequenceMatcher

def similarity(a, b):
    """Calculate similarity ratio between two strings"""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def main():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    art = data['categories']['Art']

    print(f"Total Art questions: {len(art)}")
    print()

    # Count by subcategory
    subcategories = {}
    for q in art:
        subcat = q['subcategory']
        subcategories[subcat] = subcategories.get(subcat, 0) + 1

    print("By subcategory:")
    for subcat, count in sorted(subcategories.items()):
        print(f"  {subcat}: {count} questions")
    print()

    # Count by difficulty
    difficulties = {}
    for q in art:
        diff = q['difficulty']
        difficulties[diff] = difficulties.get(diff, 0) + 1

    print("By difficulty:")
    for diff, count in sorted(difficulties.items()):
        print(f"  {diff}: {count} questions")
    print()

    # Check for duplicates
    duplicates_exact = []
    duplicates_semantic = []
    duplicates_essential = []

    for i, q1 in enumerate(art):
        for j, q2 in enumerate(art[i+1:], i+1):
            sim = similarity(q1['question'], q2['question'])

            if sim == 1.0:
                # Exact duplicate
                duplicates_exact.append((q1['id'], q2['id'], q1['question'], q2['question']))
            elif sim > 0.9:
                # Semantic duplicate (very similar, likely same question)
                if q1['correct_answer'] == q2['correct_answer']:
                    duplicates_semantic.append((q1['id'], q2['id'], f"{sim:.2%}", q1['question'], q2['question']))
            elif sim > 0.7:
                # Essential duplicate (testing same knowledge)
                if q1['correct_answer'] == q2['correct_answer']:
                    duplicates_essential.append((q1['id'], q2['id'], f"{sim:.2%}", q1['question'], q2['question']))

    # Report results
    if duplicates_exact:
        print(f"❌ Found {len(duplicates_exact)} EXACT duplicates:")
        for id1, id2, q1, q2 in duplicates_exact:
            print(f"  {id1} = {id2}")
            print(f"    '{q1}'")
        print()
    else:
        print("✅ No exact duplicates found")
        print()

    if duplicates_semantic:
        print(f"⚠️  Found {len(duplicates_semantic)} SEMANTIC duplicates (>90% similar):")
        for id1, id2, sim, q1, q2 in duplicates_semantic:
            print(f"  {id1} ~ {id2} ({sim})")
            print(f"    '{q1}'")
            print(f"    '{q2}'")
        print()
    else:
        print("✅ No semantic duplicates found")
        print()

    if duplicates_essential:
        print(f"⚠️  Found {len(duplicates_essential)} ESSENTIAL duplicates (70-90% similar):")
        for id1, id2, sim, q1, q2 in duplicates_essential:
            print(f"  {id1} ~ {id2} ({sim})")
            print(f"    '{q1}'")
            print(f"    '{q2}'")
        print()
    else:
        print("✅ No essential duplicates found")
        print()

    if not (duplicates_exact or duplicates_semantic or duplicates_essential):
        print("🎉 All 300 Art questions are unique!")
        return 0
    else:
        total_dups = len(duplicates_exact) + len(duplicates_semantic) + len(duplicates_essential)
        print(f"Total duplicates found: {total_dups}")
        return total_dups

if __name__ == "__main__":
    exit(main())
