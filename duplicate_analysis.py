#!/usr/bin/env python3
"""
Analyze questions.json for duplicates:
- Exact duplicates (identical text)
- Semantic duplicates (same meaning, different wording)
- Essential duplicates (testing same knowledge)
"""

import json
from collections import defaultdict
from difflib import SequenceMatcher
import re

def normalize_text(text):
    """Normalize text for comparison by removing extra spaces and lowercasing"""
    return re.sub(r'\s+', ' ', text.lower().strip())

def similarity_ratio(text1, text2):
    """Calculate similarity ratio between two strings"""
    return SequenceMatcher(None, normalize_text(text1), normalize_text(text2)).ratio()

def extract_core_concept(question):
    """Extract the core concept being asked about"""
    # Remove question marks, common question words
    normalized = normalize_text(question)
    # Remove common question starters
    for starter in ['what is', 'what was', 'what are', 'what were',
                    'which', 'who is', 'who was', 'who were',
                    'when did', 'when was', 'where is', 'where was',
                    'how many', 'how much', 'in which']:
        if normalized.startswith(starter):
            normalized = normalized[len(starter):].strip()
    return normalized

def analyze_duplicates(json_path):
    """Analyze questions for all types of duplicates"""

    # Load questions
    with open(json_path, 'r') as f:
        data = json.load(f)

    # Flatten all questions
    all_questions = []
    for category, questions in data['categories'].items():
        all_questions.extend(questions)

    print(f"Analyzing {len(all_questions)} questions...")
    print("=" * 80)

    # Track duplicates
    exact_duplicates = defaultdict(list)
    semantic_duplicates = []
    essential_duplicates = []

    # Build indices for efficient comparison
    question_text_index = defaultdict(list)
    answer_index = defaultdict(list)

    for q in all_questions:
        # Index by normalized question text
        normalized = normalize_text(q['question'])
        question_text_index[normalized].append(q)

        # Index by correct answer
        answer_index[normalize_text(q['correct_answer'])].append(q)

    # 1. Find EXACT DUPLICATES
    print("\n### 1. EXACT DUPLICATES ###\n")
    exact_count = 0
    for normalized_text, questions in question_text_index.items():
        if len(questions) > 1:
            exact_count += len(questions) - 1
            print(f"Found {len(questions)} exact duplicates:")
            for q in questions:
                print(f"  - {q['id']} ({q['category']} / {q['subcategory']})")
                print(f"    Question: {q['question']}")
                print(f"    Answer: {q['correct_answer']}")
                print(f"    Difficulty: {q['difficulty']}")
            print(f"  RECOMMENDATION: Keep {questions[0]['id']}, remove others")
            print()

    if exact_count == 0:
        print("No exact duplicates found.\n")
    else:
        print(f"Total exact duplicate questions: {exact_count}\n")

    # 2. Find SEMANTIC DUPLICATES (high similarity, not exact)
    print("\n### 2. SEMANTIC DUPLICATES ###\n")
    print("(Questions with different wording but very similar meaning)\n")

    semantic_count = 0
    checked_pairs = set()

    for i, q1 in enumerate(all_questions):
        for q2 in all_questions[i+1:]:
            pair_key = tuple(sorted([q1['id'], q2['id']]))
            if pair_key in checked_pairs:
                continue
            checked_pairs.add(pair_key)

            # Skip if already found as exact duplicate
            if normalize_text(q1['question']) == normalize_text(q2['question']):
                continue

            # Calculate similarity
            similarity = similarity_ratio(q1['question'], q2['question'])

            # High similarity threshold (80-95%) indicates semantic duplicates
            if similarity >= 0.80 and similarity < 1.0:
                # Also check if they have the same answer
                same_answer = normalize_text(q1['correct_answer']) == normalize_text(q2['correct_answer'])

                semantic_count += 1
                print(f"Semantic duplicate pair (similarity: {similarity:.1%}):")
                print(f"  {q1['id']} ({q1['category']} / {q1['subcategory']})")
                print(f"    Q: {q1['question']}")
                print(f"    A: {q1['correct_answer']}")
                print(f"    Difficulty: {q1['difficulty']}")
                print(f"  {q2['id']} ({q2['category']} / {q2['subcategory']})")
                print(f"    Q: {q2['question']}")
                print(f"    A: {q2['correct_answer']}")
                print(f"    Difficulty: {q2['difficulty']}")

                if same_answer:
                    print(f"  Same answer: YES")
                    print(f"  RECOMMENDATION: These likely ask the same thing - review and keep one")
                else:
                    print(f"  Same answer: NO")
                    print(f"  RECOMMENDATION: Review carefully - similar wording but different facts")
                print()

    if semantic_count == 0:
        print("No semantic duplicates found.\n")
    else:
        print(f"Total semantic duplicate pairs: {semantic_count}\n")

    # 3. Find ESSENTIAL DUPLICATES (same answer, potentially same knowledge)
    print("\n### 3. ESSENTIAL DUPLICATES ###\n")
    print("(Questions with same answer that might test the same knowledge)\n")

    essential_count = 0
    for answer, questions in answer_index.items():
        if len(questions) > 1:
            # Group by category to identify potential duplicates
            # Questions with same answer in same category are more suspicious

            for i, q1 in enumerate(questions):
                for q2 in questions[i+1:]:
                    # Skip if already caught as exact or semantic
                    if normalize_text(q1['question']) == normalize_text(q2['question']):
                        continue

                    similarity = similarity_ratio(q1['question'], q2['question'])
                    if similarity >= 0.80:  # Already caught in semantic
                        continue

                    # Check if they're testing similar concepts
                    # Lower similarity (30-50%) but same answer and category might indicate essential duplicates
                    if similarity >= 0.30 and q1['category'] == q2['category']:
                        essential_count += 1
                        print(f"Potential essential duplicate (similarity: {similarity:.1%}):")
                        print(f"  {q1['id']} ({q1['category']} / {q1['subcategory']})")
                        print(f"    Q: {q1['question']}")
                        print(f"    Difficulty: {q1['difficulty']}")
                        print(f"  {q2['id']} ({q2['category']} / {q2['subcategory']})")
                        print(f"    Q: {q2['question']}")
                        print(f"    Difficulty: {q2['difficulty']}")
                        print(f"  Shared answer: {q1['correct_answer']}")
                        print(f"  RECOMMENDATION: Review if both test the same core knowledge")
                        print()

    if essential_count == 0:
        print("No essential duplicates found with medium similarity.\n")
    else:
        print(f"Total potential essential duplicate pairs: {essential_count}\n")

    # 4. SUMMARY STATISTICS
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total questions analyzed: {len(all_questions)}")
    print(f"Exact duplicate questions: {exact_count}")
    print(f"Semantic duplicate pairs: {semantic_count}")
    print(f"Essential duplicate pairs: {essential_count}")
    print(f"Total issues found: {exact_count + semantic_count + essential_count}")

    # Additional analysis: Questions by category
    print("\n### Questions by Category ###")
    for category, questions in data['categories'].items():
        print(f"{category}: {len(questions)} questions")

    # Find recently added questions (high ID numbers)
    print("\n### Recently Added Questions (check for duplicates) ###")
    recent_thresholds = {
        'foo': 65, 'ear': 189, 'bib': 172, 'spt': 170, 'sci': 160, 'ent': 200, 'his': 170
    }

    for prefix, threshold in recent_thresholds.items():
        recent = [q for q in all_questions if q['id'].startswith(prefix) and
                  int(q['id'].split('_')[1]) >= threshold]
        if recent:
            print(f"\n{prefix.upper()} questions >= {prefix}_{threshold:03d}: {len(recent)} questions")
            for q in sorted(recent, key=lambda x: x['id']):
                print(f"  {q['id']}: {q['question'][:70]}...")

if __name__ == "__main__":
    analyze_duplicates('/home/user/fiztrivia/Fiz/Resources/questions.json')
