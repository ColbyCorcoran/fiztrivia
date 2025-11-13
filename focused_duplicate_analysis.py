#!/usr/bin/env python3
"""
Focused duplicate analysis - find TRUE duplicates
"""

import json
from collections import defaultdict
from difflib import SequenceMatcher
import re

def normalize_text(text):
    """Normalize text for comparison"""
    return re.sub(r'\s+', ' ', text.lower().strip())

def similarity_ratio(text1, text2):
    """Calculate similarity ratio"""
    return SequenceMatcher(None, normalize_text(text1), normalize_text(text2)).ratio()

def load_questions(json_path):
    """Load all questions from JSON"""
    with open(json_path, 'r') as f:
        data = json.load(f)
    all_questions = []
    for category, questions in data['categories'].items():
        all_questions.extend(questions)
    return all_questions, data['categories']

def find_exact_duplicates(questions):
    """Find questions with identical text"""
    question_text_index = defaultdict(list)
    for q in questions:
        normalized = normalize_text(q['question'])
        question_text_index[normalized].append(q)

    duplicates = []
    for normalized_text, qs in question_text_index.items():
        if len(qs) > 1:
            duplicates.append(qs)

    return duplicates

def find_true_semantic_duplicates(questions):
    """Find questions that are truly the same (90%+ similarity, same answer)"""
    true_duplicates = []
    checked_pairs = set()

    for i, q1 in enumerate(questions):
        for q2 in questions[i+1:]:
            pair_key = tuple(sorted([q1['id'], q2['id']]))
            if pair_key in checked_pairs:
                continue
            checked_pairs.add(pair_key)

            # Skip exact duplicates (already caught)
            if normalize_text(q1['question']) == normalize_text(q2['question']):
                continue

            # Calculate similarity
            similarity = similarity_ratio(q1['question'], q2['question'])
            same_answer = normalize_text(q1['correct_answer']) == normalize_text(q2['correct_answer'])

            # High similarity (90%+) AND same answer = likely true duplicate
            if similarity >= 0.90 and same_answer:
                true_duplicates.append((q1, q2, similarity))

    return true_duplicates

def main():
    questions, categories = load_questions('/home/user/fiztrivia/Fiz/Resources/questions.json')

    print("="*80)
    print("DUPLICATE ANALYSIS REPORT")
    print("="*80)
    print(f"\nTotal questions: {len(questions)}")

    # Category breakdown
    print("\nQuestions by category:")
    for cat, qs in categories.items():
        print(f"  {cat}: {len(qs)}")

    # 1. EXACT DUPLICATES
    print("\n" + "="*80)
    print("1. EXACT DUPLICATES")
    print("="*80)
    exact_dupes = find_exact_duplicates(questions)

    if exact_dupes:
        for group in exact_dupes:
            print(f"\nFound {len(group)} exact duplicates:")
            for q in group:
                print(f"  ID: {q['id']}")
                print(f"  Category: {q['category']} / {q['subcategory']}")
                print(f"  Question: {q['question']}")
                print(f"  Answer: {q['correct_answer']}")
                print(f"  Difficulty: {q['difficulty']}")
                print()

            # Recommendation
            keep = group[0]
            remove = [q['id'] for q in group[1:]]
            print(f"  RECOMMENDATION: Keep {keep['id']}, remove {', '.join(remove)}")
            print()
    else:
        print("\nNo exact duplicates found.")

    # Count
    exact_count = sum(len(group) - 1 for group in exact_dupes)
    print(f"\nTotal exact duplicate questions to remove: {exact_count}")

    # 2. TRUE SEMANTIC DUPLICATES
    print("\n" + "="*80)
    print("2. TRUE SEMANTIC DUPLICATES (90%+ similarity, same answer)")
    print("="*80)

    semantic_dupes = find_true_semantic_duplicates(questions)

    if semantic_dupes:
        for q1, q2, sim in semantic_dupes:
            print(f"\nSemantic duplicate (similarity: {sim:.1%}):")
            print(f"  [{q1['id']}] {q1['category']} / {q1['subcategory']}")
            print(f"    Q: {q1['question']}")
            print(f"    A: {q1['correct_answer']}")
            print(f"    Difficulty: {q1['difficulty']}")
            print(f"  [{q2['id']}] {q2['category']} / {q2['subcategory']}")
            print(f"    Q: {q2['question']}")
            print(f"    A: {q2['correct_answer']}")
            print(f"    Difficulty: {q2['difficulty']}")
            print(f"  RECOMMENDATION: Review and keep one - these are likely asking the same thing")
            print()
    else:
        print("\nNo true semantic duplicates found.")

    print(f"\nTotal semantic duplicate pairs: {len(semantic_dupes)}")

    # 3. RECENTLY ADDED QUESTIONS
    print("\n" + "="*80)
    print("3. RECENTLY ADDED QUESTIONS (potential duplicates)")
    print("="*80)

    recent_thresholds = {
        'foo': 64,  # Original count was 64
        'ear': 189,
        'sci': 160,
        'spt': 170,
        'bib': 142
    }

    for prefix, threshold in recent_thresholds.items():
        recent = [q for q in questions if q['id'].startswith(prefix)]
        if recent:
            max_id = max(int(q['id'].split('_')[1]) for q in recent)
            if max_id > threshold:
                print(f"\n{prefix.upper()} category: {len(recent)} total, highest ID: {prefix}_{max_id:03d}")
                new_questions = [q for q in recent if int(q['id'].split('_')[1]) > threshold]
                if new_questions:
                    print(f"  New questions added (>{prefix}_{threshold:03d}): {len(new_questions)}")
                    for q in sorted(new_questions, key=lambda x: x['id']):
                        print(f"    {q['id']}: {q['question'][:60]}...")

    # SUMMARY
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total questions analyzed: {len(questions)}")
    print(f"Exact duplicates found: {exact_count} questions to remove")
    print(f"Semantic duplicates found: {len(semantic_dupes)} pairs to review")
    print(f"Total issues: {exact_count + len(semantic_dupes)}")

    if exact_count > 0:
        print(f"\nACTION REQUIRED: Remove {exact_count} exact duplicate questions")
    if len(semantic_dupes) > 0:
        print(f"ACTION REQUIRED: Review {len(semantic_dupes)} semantic duplicate pairs")

if __name__ == "__main__":
    main()
