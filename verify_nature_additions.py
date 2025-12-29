#!/usr/bin/env python3
"""
Verify the 70 new Nature questions don't duplicate existing questions
"""

import json
from difflib import SequenceMatcher

def similarity_ratio(str1, str2):
    """Calculate similarity ratio between two strings"""
    return SequenceMatcher(None, str1.lower(), str2.lower()).ratio()

def check_duplicates():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    nature_questions = data['categories']['Nature']

    # New question IDs (nat_231 to nat_300)
    new_question_ids = [f"nat_{i:03d}" for i in range(231, 301)]

    new_questions = [q for q in nature_questions if q['id'] in new_question_ids]
    existing_questions = [q for q in nature_questions if q['id'] not in new_question_ids]

    print("=" * 80)
    print("DUPLICATE CHECK FOR NEW NATURE QUESTIONS")
    print("=" * 80)
    print(f"\nNew questions to check: {len(new_questions)}")
    print(f"Existing questions to compare against: {len(existing_questions)}")
    print()

    found_issues = False

    for new_q in new_questions:
        new_text = new_q['question']
        new_id = new_q['id']
        new_answer = new_q['correct_answer']

        for existing_q in existing_questions:
            existing_text = existing_q['question']
            existing_id = existing_q['id']
            existing_answer = existing_q['correct_answer']

            similarity = similarity_ratio(new_text, existing_text)

            # Check for exact duplicates (100%)
            if similarity == 1.0:
                print(f"❌ EXACT DUPLICATE FOUND!")
                print(f"   New: [{new_id}] {new_text}")
                print(f"   Existing: [{existing_id}] {existing_text}")
                print()
                found_issues = True

            # Check for semantic duplicates (>90% similar with same answer)
            elif similarity > 0.90 and new_answer == existing_answer:
                print(f"⚠️  SEMANTIC DUPLICATE ({similarity*100:.1f}% similar, same answer)")
                print(f"   New: [{new_id}] {new_text}")
                print(f"   Existing: [{existing_id}] {existing_text}")
                print(f"   Answer: {new_answer}")
                print()
                found_issues = True

            # Check for essential duplicates (70-90% similar with same answer)
            elif similarity > 0.70 and new_answer == existing_answer:
                print(f"⚠️  POTENTIAL DUPLICATE ({similarity*100:.1f}% similar, same answer)")
                print(f"   New: [{new_id}] {new_text}")
                print(f"   Existing: [{existing_id}] {existing_text}")
                print(f"   Answer: {new_answer}")
                print()
                found_issues = True

    if not found_issues:
        print("✅ NO DUPLICATES FOUND!")
        print("\nAll 70 new Nature questions are unique.")
        print("No exact, semantic, or essential duplicates detected.")
    else:
        print("=" * 80)
        print("⚠️  DUPLICATES DETECTED - REVIEW REQUIRED")
        print("=" * 80)

    print()

if __name__ == "__main__":
    check_duplicates()
