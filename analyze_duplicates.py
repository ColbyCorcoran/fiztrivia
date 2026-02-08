#!/usr/bin/env python3
"""
Detailed duplicate question analyzer for Mario expansion pack
"""

import json

def analyze_duplicates():
    with open('/home/user/fiztrivia/Fiz/Resources/Expansion Packs/expansion_mario.json', 'r') as f:
        data = json.load(f)

    all_questions = data.get('freePreviewQuestions', []) + data.get('paidQuestions', [])

    # Group questions by text
    question_groups = {}
    for q in all_questions:
        text = q.get('question', '').strip().lower()
        if text not in question_groups:
            question_groups[text] = []
        question_groups[text].append(q)

    # Find duplicates
    duplicates = {text: questions for text, questions in question_groups.items()
                  if len(questions) > 1 and text}

    print("=" * 80)
    print("DUPLICATE QUESTIONS DETAILED ANALYSIS")
    print("=" * 80)
    print(f"\nFound {len(duplicates)} duplicate question texts\n")

    for i, (text, questions) in enumerate(duplicates.items(), 1):
        print(f"\n{'=' * 80}")
        print(f"DUPLICATE #{i}")
        print(f"{'=' * 80}")
        print(f"\nQuestion Text: {questions[0]['question']}")
        print(f"\nAppears {len(questions)} times:")

        for q in questions:
            print(f"\n  ID: {q['id']}")
            print(f"  Subtopic: {q.get('subtopic', 'N/A')}")
            print(f"  Difficulty: {q.get('difficulty', 'N/A')}")
            print(f"  Category: {q.get('category', 'N/A')}")
            print(f"  Options: {q.get('options', [])}")
            print(f"  Correct Answer: {q.get('correct_answer', 'N/A')}")

            # Check if it's in free preview
            is_free = q in data.get('freePreviewQuestions', [])
            print(f"  Type: {'FREE PREVIEW' if is_free else 'PAID'}")

    print(f"\n{'=' * 80}")
    print("SUMMARY")
    print(f"{'=' * 80}")
    print(f"\nTotal duplicates found: {len(duplicates)}")
    print(f"Total duplicate instances: {sum(len(qs) for qs in duplicates.values())}")
    print(f"\nRecommendation: Remove or modify {sum(len(qs) - 1 for qs in duplicates.values())} duplicate questions")
    print("\nSuggested IDs to remove (keep the first occurrence of each):")

    for text, questions in duplicates.items():
        # Keep first, remove rest
        for q in questions[1:]:
            print(f"  - {q['id']} (duplicate of {questions[0]['id']})")

    print()

if __name__ == '__main__':
    analyze_duplicates()
