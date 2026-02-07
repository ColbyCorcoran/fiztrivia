#!/usr/bin/env python3
"""
Investigate specific issues found in Narnia pack audit
"""

import json
import re

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def investigate_issues():
    narnia_path = "/home/user/fiztrivia/Fiz/Resources/Expansion Packs/expansion_narnia.json"
    narnia_data = load_json(narnia_path)

    free_questions = narnia_data.get('freePreviewQuestions', [])
    paid_questions = narnia_data.get('paidQuestions', [])
    total_questions = free_questions + paid_questions

    print("=" * 80)
    print("DETAILED ISSUE INVESTIGATION")
    print("=" * 80)
    print()

    # ========================================================================
    # 1. DUPLICATE QUESTIONS
    # ========================================================================
    print("1. DUPLICATE QUESTION DETAILS")
    print("-" * 80)

    question_map = {}
    for q in total_questions:
        text = q.get('question', '').lower().strip()
        if text in question_map:
            question_map[text].append(q)
        else:
            question_map[text] = [q]

    duplicates = {text: qs for text, qs in question_map.items() if len(qs) > 1}

    for i, (text, qs) in enumerate(duplicates.items(), 1):
        print(f"\nDuplicate #{i}:")
        print(f"Question: {text}")
        for q in qs:
            print(f"  - ID: {q.get('id')}")
            print(f"    Subtopic: {q.get('subtopic')}")
            print(f"    Difficulty: {q.get('difficulty')}")
            print(f"    Correct: {q.get('correct_answer')}")

    # ========================================================================
    # 2. PROFANITY INVESTIGATION
    # ========================================================================
    print("\n\n2. PROFANITY INVESTIGATION")
    print("-" * 80)

    profanity_words = ['damn', 'hell', 'ass', 'crap', 'shit', 'fuck']

    for word in profanity_words:
        print(f"\nSearching for '{word}':")
        count = 0
        for q in total_questions:
            text = (q.get('question', '') + ' ' + ' '.join(q.get('options', []))).lower()
            if word in text:
                count += 1
                if count <= 3:  # Show first 3 examples
                    print(f"  ID: {q.get('id')}")
                    print(f"  Question: {q.get('question')[:80]}...")
                    # Find which option contains it
                    for opt in q.get('options', []):
                        if word in opt.lower():
                            print(f"  Option: {opt}")
                    print()
        if count > 0:
            print(f"  Total found: {count}")

    # ========================================================================
    # 3. SUBTOPIC ANALYSIS
    # ========================================================================
    print("\n\n3. SUBTOPIC ANALYSIS")
    print("-" * 80)

    print("\nActual subtopics used:")
    from collections import Counter
    subtopic_counts = Counter(q.get('subtopic', 'UNKNOWN') for q in total_questions)
    for subtopic, count in sorted(subtopic_counts.items()):
        print(f"  - {subtopic}: {count} questions")

    print("\n\nExpected subtopics (from original plan):")
    expected = [
        "The Lion, the Witch and the Wardrobe",
        "Prince Caspian",
        "The Voyage of the Dawn Treader",
        "The Silver Chair",
        "The Horse and His Boy",
        "The Magician's Nephew"
    ]
    for st in expected:
        print(f"  - {st}")

    print("\n\nANALYSIS:")
    print("The pack uses thematic subtopics (Characters, Locations, etc.) instead of")
    print("individual book titles. This is a DESIGN DECISION, not an error.")
    print("\nThematic approach advantages:")
    print("  + More varied gameplay experience")
    print("  + Better for players who haven't read all books")
    print("  + Avoids redundancy across books")
    print("\nBook-based approach advantages:")
    print("  + Tests knowledge of specific books")
    print("  + Follows chronological story")
    print("  + Better for book-by-book fans")

    # ========================================================================
    # 4. SUBTOPIC ICONS CHECK
    # ========================================================================
    print("\n\n4. SUBTOPIC ICONS INVESTIGATION")
    print("-" * 80)

    hp_path = "/home/user/fiztrivia/Fiz/Resources/Expansion Packs/expansion_harry_potter.json"
    hp_data = load_json(hp_path)

    print("\nHarry Potter pack structure:")
    print(f"  Has subtopicIcons: {'subtopicIcons' in hp_data}")
    if 'subtopicIcons' in hp_data:
        print(f"  subtopicIcons: {hp_data.get('subtopicIcons')}")

    print("\n\nNarnia pack structure:")
    print(f"  Has subtopicIcons: {'subtopicIcons' in narnia_data}")

    # ========================================================================
    # 5. QUESTION QUALITY SPOT CHECK
    # ========================================================================
    print("\n\n5. QUESTION QUALITY SPOT CHECK")
    print("-" * 80)

    print("\nRandom sample of questions:")
    import random
    random.seed(42)
    sample = random.sample(total_questions, min(5, len(total_questions)))

    for i, q in enumerate(sample, 1):
        print(f"\nQuestion {i}:")
        print(f"  ID: {q.get('id')}")
        print(f"  Subtopic: {q.get('subtopic')}")
        print(f"  Difficulty: {q.get('difficulty')}")
        print(f"  Q: {q.get('question')}")
        print(f"  Options: {q.get('options')}")
        print(f"  Correct: {q.get('correct_answer')}")

if __name__ == "__main__":
    investigate_issues()
