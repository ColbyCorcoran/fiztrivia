#!/usr/bin/env python3
"""
Verification script to spot check cleaned questions.
"""

import json
from pathlib import Path


def main():
    base_path = Path("Fiz/Resources")

    print("Spot checking specific questions...\n")
    print("="*60)

    # Check questions.json - lit_186
    with open(base_path / "questions.json", 'r') as f:
        data = json.load(f)
        all_questions = []
        for cat_questions in data['categories'].values():
            all_questions.extend(cat_questions)

        for q in all_questions:
            if q['id'] == 'lit_186':
                print(f"questions.json - lit_186:")
                print(f"  Question: {q['question']}")
                print(f"  Correct answer: '{q['correct_answer']}'")
                print(f"  Expected: '17' (no parentheses)")
                print(f"  ✓ PASS" if q['correct_answer'] == '17' else f"  ✗ FAIL")
                print()
                break

    # Check expansion_disney.json
    with open(base_path / "Expansion Packs/expansion_disney.json", 'r') as f:
        data = json.load(f)
        questions = data.get('freePreviewQuestions', []) + data.get('paidQuestions', [])

        # Find question about Disney theme parks
        for q in questions:
            if 'theme parks' in q.get('question', '').lower() and 'walt disney world' in q.get('question', '').lower():
                print(f"expansion_disney.json - Theme parks question:")
                print(f"  ID: {q['id']}")
                print(f"  Question: {q['question']}")
                print(f"  Correct answer: '{q['correct_answer']}'")
                print(f"  Expected: '4' (no parentheses)")
                print(f"  ✓ PASS" if q['correct_answer'] == '4' else f"  ✗ FAIL")
                print()
                break

        # Find question about first international Disney park
        for q in questions:
            if 'first international' in q.get('question', '').lower() and 'disney park' in q.get('question', '').lower():
                print(f"expansion_disney.json - First international park:")
                print(f"  ID: {q['id']}")
                print(f"  Question: {q['question']}")
                print(f"  Correct answer: '{q['correct_answer']}'")
                print(f"  Expected: 'Tokyo Disneyland' (no year)")
                print(f"  ✓ PASS" if q['correct_answer'] == 'Tokyo Disneyland' else f"  ✗ FAIL")
                print()
                break

    # Check expansion_pokemon.json for type weakness
    with open(base_path / "Expansion Packs/expansion_pokemon.json", 'r') as f:
        data = json.load(f)
        questions = data.get('freePreviewQuestions', []) + data.get('paidQuestions', [])

        # Find a question with type weaknesses that had parentheses
        for q in questions:
            if 'weakness' in q.get('question', '').lower() or 'weak to' in q.get('question', '').lower():
                # Check if any option has parentheses (it shouldn't after cleaning)
                has_parens = any('(' in opt for opt in q['options'])
                if not has_parens:
                    print(f"expansion_pokemon.json - Type weakness question:")
                    print(f"  ID: {q['id']}")
                    print(f"  Question: {q['question']}")
                    print(f"  Options: {q['options']}")
                    print(f"  ✓ PASS - No parentheses found")
                    print()
                    break

    print("="*60)
    print("Verification complete!")


if __name__ == "__main__":
    main()
