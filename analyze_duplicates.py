#!/usr/bin/env python3
"""
Analyze questions.json for duplicate questions.
Finds exact duplicates, semantic duplicates, and essential duplicates.
"""

import json
import re
from collections import defaultdict
from difflib import SequenceMatcher

def normalize_text(text):
    """Normalize text for comparison by removing punctuation and extra spaces."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def similarity_ratio(text1, text2):
    """Calculate similarity ratio between two texts."""
    return SequenceMatcher(None, normalize_text(text1), normalize_text(text2)).ratio()

def are_semantically_similar(q1, q2, threshold=0.85):
    """Check if two questions are semantically similar."""
    return similarity_ratio(q1, q2) >= threshold

def are_essentially_same(q1_data, q2_data):
    """Check if two questions test the same knowledge."""
    # If questions are very similar and have same correct answer
    if similarity_ratio(q1_data['question'], q2_data['question']) >= 0.7:
        if q1_data['correct_answer'] == q2_data['correct_answer']:
            return True
    return False

def main():
    # Load questions
    with open('/home/user/fiztrivia/Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    # Flatten questions from categories
    questions = []
    for category, category_questions in data['categories'].items():
        questions.extend(category_questions)

    print(f"Total questions in database: {len(questions)}")

    # Define newly added question ranges
    new_ranges = {
        'sci': range(176, 210),  # sci_176 to sci_209
        'foo': range(176, 204),  # foo_176 to foo_203
        'his': range(175, 202),  # his_175 to his_201
        'spt': range(190, 204),  # spt_190 to spt_203
        'bib': range(190, 205),  # bib_190 to bib_204
    }

    # Identify new questions
    new_questions = []
    for q in questions:
        q_id = q['id']
        prefix = q_id.split('_')[0]
        try:
            number = int(q_id.split('_')[1])
            if prefix in new_ranges and number in new_ranges[prefix]:
                new_questions.append(q)
        except:
            pass

    print(f"New questions to check: {len(new_questions)}")

    # Find duplicates
    duplicates = []

    # Track exact duplicates
    question_text_map = defaultdict(list)
    for q in questions:
        normalized = normalize_text(q['question'])
        question_text_map[normalized].append(q)

    # Find exact duplicates
    print("\n" + "="*80)
    print("EXACT DUPLICATES")
    print("="*80)
    exact_count = 0
    for normalized_text, q_list in question_text_map.items():
        if len(q_list) > 1:
            exact_count += len(q_list) - 1
            print(f"\nDuplicate Group (EXACT) - {len(q_list)} instances:")
            for q in sorted(q_list, key=lambda x: x['id']):
                print(f"  ID: {q['id']}")
                print(f"  Category: {q['category']} -> {q.get('subcategory', 'N/A')}")
                print(f"  Question: {q['question']}")
                print(f"  Answer: {q['correct_answer']}")
                print()

            # Recommendation
            keep = min(q_list, key=lambda x: x['id'])
            remove = [q for q in q_list if q['id'] != keep['id']]
            print(f"  RECOMMENDATION:")
            print(f"    KEEP: {keep['id']}")
            print(f"    REMOVE: {', '.join([q['id'] for q in remove])}")
            print()

            duplicates.append({
                'type': 'exact',
                'count': len(q_list),
                'questions': q_list,
                'keep': keep['id'],
                'remove': [q['id'] for q in remove]
            })

    # Find semantic duplicates (checking new questions against all)
    print("\n" + "="*80)
    print("SEMANTIC DUPLICATES (Very similar wording, 85%+ match)")
    print("="*80)
    semantic_count = 0
    checked_pairs = set()

    for new_q in new_questions:
        for other_q in questions:
            if new_q['id'] == other_q['id']:
                continue

            pair = tuple(sorted([new_q['id'], other_q['id']]))
            if pair in checked_pairs:
                continue
            checked_pairs.add(pair)

            # Skip if already found as exact duplicate
            if normalize_text(new_q['question']) == normalize_text(other_q['question']):
                continue

            if are_semantically_similar(new_q['question'], other_q['question'], threshold=0.85):
                semantic_count += 1
                ratio = similarity_ratio(new_q['question'], other_q['question'])
                print(f"\nSemantic Duplicate (Similarity: {ratio:.1%}):")
                print(f"  ID 1: {new_q['id']}")
                print(f"  Category: {new_q['category']} -> {new_q.get('subcategory', 'N/A')}")
                print(f"  Question: {new_q['question']}")
                print(f"  Answer: {new_q['correct_answer']}")
                print()
                print(f"  ID 2: {other_q['id']}")
                print(f"  Category: {other_q['category']} -> {other_q.get('subcategory', 'N/A')}")
                print(f"  Question: {other_q['question']}")
                print(f"  Answer: {other_q['correct_answer']}")
                print()

                keep = min([new_q, other_q], key=lambda x: x['id'])
                remove = new_q if keep['id'] == other_q['id'] else other_q
                print(f"  RECOMMENDATION:")
                print(f"    KEEP: {keep['id']}")
                print(f"    REMOVE: {remove['id']}")
                print()

                duplicates.append({
                    'type': 'semantic',
                    'similarity': ratio,
                    'questions': [new_q, other_q],
                    'keep': keep['id'],
                    'remove': [remove['id']]
                })

    # Find essential duplicates (testing same knowledge, 70-85% match)
    print("\n" + "="*80)
    print("ESSENTIAL DUPLICATES (Same knowledge, different wording, 70-85% match)")
    print("="*80)
    essential_count = 0
    checked_pairs = set()

    for new_q in new_questions:
        for other_q in questions:
            if new_q['id'] == other_q['id']:
                continue

            pair = tuple(sorted([new_q['id'], other_q['id']]))
            if pair in checked_pairs:
                continue
            checked_pairs.add(pair)

            # Skip if already found as exact or semantic duplicate
            ratio = similarity_ratio(new_q['question'], other_q['question'])
            if ratio >= 0.85:
                continue

            if ratio >= 0.70 and new_q['correct_answer'] == other_q['correct_answer']:
                essential_count += 1
                print(f"\nEssential Duplicate (Similarity: {ratio:.1%}):")
                print(f"  ID 1: {new_q['id']}")
                print(f"  Category: {new_q['category']} -> {new_q.get('subcategory', 'N/A')}")
                print(f"  Question: {new_q['question']}")
                print(f"  Answer: {new_q['correct_answer']}")
                print()
                print(f"  ID 2: {other_q['id']}")
                print(f"  Category: {other_q['category']} -> {other_q.get('subcategory', 'N/A')}")
                print(f"  Question: {other_q['question']}")
                print(f"  Answer: {other_q['correct_answer']}")
                print()

                keep = min([new_q, other_q], key=lambda x: x['id'])
                remove = new_q if keep['id'] == other_q['id'] else other_q
                print(f"  RECOMMENDATION:")
                print(f"    KEEP: {keep['id']}")
                print(f"    REMOVE: {remove['id']}")
                print()

                duplicates.append({
                    'type': 'essential',
                    'similarity': ratio,
                    'questions': [new_q, other_q],
                    'keep': keep['id'],
                    'remove': [remove['id']]
                })

    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total questions analyzed: {len(questions)}")
    print(f"New questions checked: {len(new_questions)}")
    print(f"Exact duplicates found: {exact_count}")
    print(f"Semantic duplicates found: {semantic_count}")
    print(f"Essential duplicates found: {essential_count}")
    print(f"Total duplicate instances: {exact_count + semantic_count + essential_count}")

    # List all IDs to remove
    all_to_remove = []
    for dup in duplicates:
        all_to_remove.extend(dup['remove'])

    if all_to_remove:
        print(f"\n" + "="*80)
        print("ALL QUESTION IDS TO REMOVE")
        print("="*80)
        for qid in sorted(set(all_to_remove)):
            print(f"  {qid}")
        print(f"\nTotal unique questions to remove: {len(set(all_to_remove))}")
        print(f"Database would go from {len(questions)} to {len(questions) - len(set(all_to_remove))} questions")

if __name__ == '__main__':
    main()
