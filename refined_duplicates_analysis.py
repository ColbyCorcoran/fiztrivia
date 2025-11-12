#!/usr/bin/env python3
"""
Refined duplicate analysis - filters out false positives.
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

def answers_are_compatible(ans1, ans2):
    """Check if two answers are the same or very similar."""
    norm1 = normalize_text(ans1)
    norm2 = normalize_text(ans2)
    return norm1 == norm2 or similarity_ratio(ans1, ans2) > 0.9

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
        'sci': range(176, 210),
        'foo': range(176, 204),
        'his': range(175, 202),
        'spt': range(190, 204),
        'bib': range(190, 205),
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

    duplicates = []

    # Find exact duplicates
    question_text_map = defaultdict(list)
    for q in questions:
        normalized = normalize_text(q['question'])
        question_text_map[normalized].append(q)

    print("\n" + "="*80)
    print("EXACT DUPLICATES")
    print("="*80)
    exact_count = 0
    for normalized_text, q_list in question_text_map.items():
        if len(q_list) > 1:
            exact_count += len(q_list) - 1
            print(f"\nDuplicate Group #{len(duplicates) + 1} (EXACT) - {len(q_list)} instances:")
            for q in sorted(q_list, key=lambda x: x['id']):
                print(f"  [{q['id']}] {q['category']} -> {q.get('subcategory', 'N/A')}")
                print(f"  Q: {q['question']}")
                print(f"  A: {q['correct_answer']}")
                print()

            keep = min(q_list, key=lambda x: x['id'])
            remove = [q for q in q_list if q['id'] != keep['id']]
            print(f"  RECOMMENDATION:")
            print(f"    KEEP: {keep['id']}")
            print(f"    REMOVE: {', '.join([q['id'] for q in remove])}")
            print()

            duplicates.append({
                'type': 'exact',
                'questions': q_list,
                'keep': keep['id'],
                'remove': [q['id'] for q in remove]
            })

    # Find semantic duplicates with stricter filtering
    print("\n" + "="*80)
    print("SEMANTIC DUPLICATES (Similar wording, same answer)")
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

            ratio = similarity_ratio(new_q['question'], other_q['question'])

            # Stricter criteria: high similarity AND same answer
            if ratio >= 0.85 and answers_are_compatible(new_q['correct_answer'], other_q['correct_answer']):
                semantic_count += 1
                print(f"\nDuplicate Group #{len(duplicates) + 1} (SEMANTIC - {ratio:.1%} similar):")
                print(f"  [{new_q['id']}] {new_q['category']} -> {new_q.get('subcategory', 'N/A')}")
                print(f"  Q: {new_q['question']}")
                print(f"  A: {new_q['correct_answer']}")
                print()
                print(f"  [{other_q['id']}] {other_q['category']} -> {other_q.get('subcategory', 'N/A')}")
                print(f"  Q: {other_q['question']}")
                print(f"  A: {other_q['correct_answer']}")
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

    # Find essential duplicates with stricter filtering
    print("\n" + "="*80)
    print("ESSENTIAL DUPLICATES (Different wording, same knowledge)")
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

            ratio = similarity_ratio(new_q['question'], other_q['question'])

            # Skip if already found
            if ratio >= 0.85:
                continue

            # Essential duplicate: 70-85% similarity AND same answer
            if ratio >= 0.70 and answers_are_compatible(new_q['correct_answer'], other_q['correct_answer']):
                essential_count += 1
                print(f"\nDuplicate Group #{len(duplicates) + 1} (ESSENTIAL - {ratio:.1%} similar):")
                print(f"  [{new_q['id']}] {new_q['category']} -> {new_q.get('subcategory', 'N/A')}")
                print(f"  Q: {new_q['question']}")
                print(f"  A: {new_q['correct_answer']}")
                print()
                print(f"  [{other_q['id']}] {other_q['category']} -> {other_q.get('subcategory', 'N/A')}")
                print(f"  Q: {other_q['question']}")
                print(f"  A: {other_q['correct_answer']}")
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
    print(f"Total duplicate groups: {len(duplicates)}")

    # List all IDs to remove
    all_to_remove = []
    for dup in duplicates:
        all_to_remove.extend(dup['remove'])

    if all_to_remove:
        print(f"\n" + "="*80)
        print("ALL QUESTION IDS TO REMOVE")
        print("="*80)

        # Group by category
        by_category = defaultdict(list)
        for qid in sorted(set(all_to_remove)):
            prefix = qid.split('_')[0]
            by_category[prefix].append(qid)

        for prefix in sorted(by_category.keys()):
            print(f"\n{prefix.upper()}:")
            for qid in by_category[prefix]:
                print(f"  {qid}")

        print(f"\n" + "-"*80)
        print(f"Total unique questions to remove: {len(set(all_to_remove))}")
        print(f"Database size: {len(questions)} -> {len(questions) - len(set(all_to_remove))} questions")
        print(f"Reduction: {len(set(all_to_remove))} questions ({len(set(all_to_remove))/len(questions)*100:.1f}%)")

    # Save to JSON for future use
    output = {
        'analysis_date': '2025-11-12',
        'total_questions': len(questions),
        'duplicates_found': len(duplicates),
        'questions_to_remove': sorted(set(all_to_remove)),
        'duplicate_groups': []
    }

    for i, dup in enumerate(duplicates, 1):
        output['duplicate_groups'].append({
            'group_number': i,
            'type': dup['type'],
            'keep': dup['keep'],
            'remove': dup['remove'],
            'questions': [
                {
                    'id': q['id'],
                    'category': q['category'],
                    'subcategory': q.get('subcategory', ''),
                    'question': q['question'],
                    'answer': q['correct_answer']
                } for q in dup['questions']
            ]
        })

    with open('/home/user/fiztrivia/duplicate_analysis_report.json', 'w') as f:
        json.dump(output, f, indent=2)

    print(f"\nDetailed report saved to: /home/user/fiztrivia/duplicate_analysis_report.json")

if __name__ == '__main__':
    main()
