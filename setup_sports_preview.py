#!/usr/bin/env python3
"""
Set up free preview (first 50 questions) and paid questions (remaining 450).
"""

import json

def main():
    # Read the draft sports file
    with open('/home/user/fiztrivia/Fiz/Resources/Expansion Packs/draft_sports.json', 'r') as f:
        data = json.load(f)

    # All questions are currently in paidQuestions
    all_questions = data['paidQuestions']

    # Split: first 50 are free preview, rest are paid
    free_preview = all_questions[:50]
    paid = all_questions[50:]

    print(f"Total questions: {len(all_questions)}")
    print(f"Free preview: {len(free_preview)} (spt_001 to spt_050)")
    print(f"Paid: {len(paid)} (spt_051 to spt_500)")

    # Count difficulty for free preview
    free_difficulty = {"easy": 0, "medium": 0, "hard": 0}
    for q in free_preview:
        free_difficulty[q['difficulty']] += 1

    # Count difficulty for paid
    paid_difficulty = {"easy": 0, "medium": 0, "hard": 0}
    for q in paid:
        paid_difficulty[q['difficulty']] += 1

    print(f"\nFree preview difficulty:")
    print(f"  Easy: {free_difficulty['easy']}")
    print(f"  Medium: {free_difficulty['medium']}")
    print(f"  Hard: {free_difficulty['hard']}")

    print(f"\nPaid difficulty:")
    print(f"  Easy: {paid_difficulty['easy']}")
    print(f"  Medium: {paid_difficulty['medium']}")
    print(f"  Hard: {paid_difficulty['hard']}")

    # Total difficulty (should match 500 questions)
    total_difficulty = {
        "easy": free_difficulty['easy'] + paid_difficulty['easy'],
        "medium": free_difficulty['medium'] + paid_difficulty['medium'],
        "hard": free_difficulty['hard'] + paid_difficulty['hard']
    }

    # Update the data structure
    data['freePreviewQuestions'] = free_preview
    data['paidQuestions'] = paid
    data['questionCount'] = len(all_questions)
    data['freePreviewCount'] = len(free_preview)
    data['difficulty'] = total_difficulty

    # Save the updated file
    with open('/home/user/fiztrivia/Fiz/Resources/Expansion Packs/draft_sports.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("\n✅ Successfully set up free preview and paid questions!")
    print(f"\nPack metadata updated:")
    print(f"  questionCount: {data['questionCount']}")
    print(f"  freePreviewCount: {data['freePreviewCount']}")
    print(f"  difficulty: {data['difficulty']}")


if __name__ == '__main__':
    main()
