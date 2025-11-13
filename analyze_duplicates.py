#!/usr/bin/env python3
"""
Analyze questions.json for duplicate questions.
Focus on newly added questions and cross-check against all existing questions.
"""

import json
from collections import defaultdict
from difflib import SequenceMatcher

# Define newly added question ranges
NEW_QUESTION_RANGES = {
    'bib': (210, 259),
    'ear': (207, 252),
    'foo': (207, 256),
    'his': (210, 259),
    'sci': (215, 264),
    'spt': (211, 260)
}

def is_new_question(question_id):
    """Check if a question ID is in the newly added ranges."""
    prefix = question_id.split('_')[0]
    if prefix not in NEW_QUESTION_RANGES:
        return False

    try:
        num = int(question_id.split('_')[1])
        start, end = NEW_QUESTION_RANGES[prefix]
        return start <= num <= end
    except:
        return False

def normalize_text(text):
    """Normalize text for comparison."""
    return text.lower().strip().replace('?', '').replace('.', '').replace(',', '')

def similarity_ratio(text1, text2):
    """Calculate similarity ratio between two texts."""
    return SequenceMatcher(None, normalize_text(text1), normalize_text(text2)).ratio()

def main():
    # Load questions
    with open('/home/user/fiztrivia/Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    # Extract all questions from the nested structure
    all_questions = []
    for category, questions_list in data['categories'].items():
        all_questions.extend(questions_list)

    print(f"Total questions in database: {len(all_questions)}")

    # Separate new and existing questions
    new_questions = [q for q in all_questions if is_new_question(q['id'])]
    existing_questions = [q for q in all_questions if not is_new_question(q['id'])]

    print(f"New questions: {len(new_questions)}")
    print(f"Existing questions: {len(existing_questions)}")
    print()

    # Track duplicates
    exact_duplicates = []
    semantic_duplicates = []
    essential_duplicates = []

    # 1. Check for exact duplicate text
    print("=" * 80)
    print("CHECKING FOR EXACT DUPLICATES")
    print("=" * 80)

    question_text_map = defaultdict(list)
    for q in all_questions:
        normalized = normalize_text(q['question'])
        question_text_map[normalized].append(q)

    for text, qs in question_text_map.items():
        if len(qs) > 1:
            # Check if any involve new questions
            has_new = any(is_new_question(q['id']) for q in qs)
            if has_new:
                exact_duplicates.append(qs)
                print(f"\nEXACT DUPLICATE GROUP (involves new questions):")
                for q in qs:
                    new_marker = " [NEW]" if is_new_question(q['id']) else ""
                    print(f"  - {q['id']}{new_marker}: {q['question']}")
                    print(f"    Category: {q['category']}, Subcategory: {q.get('subcategory', 'N/A')}")

    if not exact_duplicates:
        print("\nNo exact duplicates found involving new questions.")

    # 2. Check for semantic duplicates (high similarity but not exact)
    print("\n" + "=" * 80)
    print("CHECKING FOR SEMANTIC DUPLICATES (>90% similar)")
    print("=" * 80)

    # Check new questions against all questions
    checked_pairs = set()
    for new_q in new_questions:
        for other_q in all_questions:
            if new_q['id'] == other_q['id']:
                continue

            # Create a consistent pair identifier
            pair_id = tuple(sorted([new_q['id'], other_q['id']]))
            if pair_id in checked_pairs:
                continue
            checked_pairs.add(pair_id)

            similarity = similarity_ratio(new_q['question'], other_q['question'])

            # High similarity but not exact match
            if 0.90 < similarity < 1.0:
                semantic_duplicates.append((new_q, other_q))
                print(f"\nSEMANTIC DUPLICATE PAIR (>90% similar):")
                print(f"  - {new_q['id']} [NEW]: {new_q['question']}")
                print(f"    Category: {new_q['category']}, Subcategory: {new_q.get('subcategory', 'N/A')}")
                print(f"  - {other_q['id']}: {other_q['question']}")
                print(f"    Category: {other_q['category']}, Subcategory: {other_q.get('subcategory', 'N/A')}")
                print(f"    Similarity: {similarity:.2%}")

    if not semantic_duplicates:
        print("\nNo semantic duplicates found involving new questions.")

    # 3. Check for essential duplicates (same correct answer + similar topic)
    print("\n" + "=" * 80)
    print("CHECKING FOR ESSENTIAL DUPLICATES (same answer, similar question)")
    print("=" * 80)

    # Group by correct answer
    answer_groups = defaultdict(list)
    for q in all_questions:
        answer_groups[normalize_text(q['correct_answer'])].append(q)

    # For each answer group, check if questions are asking the same thing
    checked_essential_pairs = set()
    for answer, qs in answer_groups.items():
        if len(qs) > 1:
            # Check pairs within this answer group
            for i, q1 in enumerate(qs):
                for q2 in qs[i+1:]:
                    # Only check if at least one is new
                    if not (is_new_question(q1['id']) or is_new_question(q2['id'])):
                        continue

                    # Create a consistent pair identifier
                    pair_id = tuple(sorted([q1['id'], q2['id']]))
                    if pair_id in checked_essential_pairs:
                        continue
                    checked_essential_pairs.add(pair_id)

                    similarity = similarity_ratio(q1['question'], q2['question'])

                    # If they have same answer and question is >70% similar
                    if similarity > 0.70 and similarity < 0.90:  # Not already caught as semantic
                        essential_duplicates.append((q1, q2))
                        print(f"\nESSENTIAL DUPLICATE PAIR (same answer, similar question):")
                        new_marker1 = " [NEW]" if is_new_question(q1['id']) else ""
                        new_marker2 = " [NEW]" if is_new_question(q2['id']) else ""
                        print(f"  - {q1['id']}{new_marker1}: {q1['question']}")
                        print(f"    Answer: {q1['correct_answer']}")
                        print(f"    Category: {q1['category']}, Subcategory: {q1.get('subcategory', 'N/A')}")
                        print(f"  - {q2['id']}{new_marker2}: {q2['question']}")
                        print(f"    Answer: {q2['correct_answer']}")
                        print(f"    Category: {q2['category']}, Subcategory: {q2.get('subcategory', 'N/A')}")
                        print(f"    Similarity: {similarity:.2%}")

    if not essential_duplicates:
        print("\nNo essential duplicates found involving new questions.")

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total questions analyzed: {len(all_questions)}")
    print(f"New questions analyzed: {len(new_questions)}")
    print(f"Exact duplicate groups found: {len(exact_duplicates)}")
    print(f"Semantic duplicate pairs found: {len(semantic_duplicates)}")
    print(f"Essential duplicate pairs found: {len(essential_duplicates)}")

    total_duplicates = len(exact_duplicates) + len(semantic_duplicates) + len(essential_duplicates)

    if total_duplicates == 0:
        print("\n" + "=" * 80)
        print("✓ ZERO DUPLICATES FOUND")
        print("=" * 80)
        print("All 296 new questions are unique and do not duplicate anything in the")
        print("existing question database. The database is clean!")
    else:
        print(f"\nTotal duplicate issues found: {total_duplicates}")
        print("Review the details above to identify which questions need attention.")

if __name__ == '__main__':
    main()
