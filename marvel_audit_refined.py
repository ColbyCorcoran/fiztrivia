#!/usr/bin/env python3
"""
Refined Marvel MCU Pack Audit - Filtering out false positives
"""

import json

def load_questions(file_path):
    """Load questions from JSON file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get('freePreviewQuestions', []) + data.get('paidQuestions', [])

def find_question_by_id(questions, qid):
    """Find a question by ID"""
    for q in questions:
        if q['id'] == qid:
            return q
    return None

def analyze_true_semantic_duplicates(questions):
    """
    Identify TRUE semantic duplicates - questions about the same subject,
    not just similar structure about different subjects.
    """

    true_duplicates = []

    # Based on the initial scan, here are pairs that look like TRUE duplicates
    # (asking about the same subject in different ways)

    suspicious_pairs = [
        # Questions that might be asking about the same thing
        ("mcu_011", "mcu_163"),  # Tony Stark's daughter vs father - 93% similar
        ("mcu_010", "mcu_019"),  # AI that replaces JARVIS vs AI that helps Spider-Man
        ("mcu_024", "mcu_028"),  # X-Men's school vs X-Men's leader - 87% similar
        ("mcu_023", "mcu_025"),  # Spider-Man's newspaper vs love interest - 82% similar
        ("mcu_033", "mcu_268"),  # Peter Quill's celestial father vs mother - 79% similar
        ("mcu_327", "mcu_337"),  # Deadpool release vs Deadpool 2 release - 97% similar (DIFFERENT MOVIES - NOT duplicate)
        ("mcu_225", "mcu_229"),  # Who created the Eternals vs who directed Eternals - 81% similar
        ("mcu_274", "mcu_291"),  # Who adopts Rocket vs who voices Rocket - 85% similar
        ("mcu_380", "mcu_434", "mcu_494"),  # Original trilogy actor questions
        ("mcu_404", "mcu_410", "mcu_416"),  # Storm family superhero names
        ("mcu_427", "mcu_433"),  # Amazing Spider-Man 1 vs 2 - 98% similar (DIFFERENT MOVIES)
    ]

    # Review self-revealing answers more carefully
    self_revealing = [
        "mcu_082",  # Avengers initiative
        "mcu_214",  # Red Room
        "mcu_228",  # Cosmic energy
        "mcu_348",  # Teleportation
        "mcu_354",  # Sonic scream
        "mcu_367",  # Days of Future Past
        "mcu_418",  # Subterranea
    ]

    # Check each self-revealing question
    print("=" * 80)
    print("SELF-REVEALING ANSWERS - DETAILED REVIEW")
    print("=" * 80)
    for qid in self_revealing:
        q = find_question_by_id(questions, qid)
        if q:
            print(f"\n{qid}:")
            print(f"  Q: {q['question']}")
            print(f"  A: {q['correct_answer']}")
            print(f"  Options: {', '.join(q['options'])}")

    # Look for actual semantic duplicates
    print("\n" + "=" * 80)
    print("TRUE SEMANTIC DUPLICATES - MANUAL REVIEW")
    print("=" * 80)

    # Tony Stark family
    q1 = find_question_by_id(questions, "mcu_011")
    q2 = find_question_by_id(questions, "mcu_163")
    print(f"\nmcu_011 vs mcu_163:")
    print(f"  Q1: {q1['question']}")
    print(f"  Q2: {q2['question']}")
    print(f"  VERDICT: Different subjects (daughter vs father) - NOT a duplicate")

    # Peter Quill family
    q1 = find_question_by_id(questions, "mcu_033")
    q2 = find_question_by_id(questions, "mcu_268")
    print(f"\nmcu_033 vs mcu_268:")
    print(f"  Q1: {q1['question']}")
    print(f"  Q2: {q2['question']}")
    print(f"  VERDICT: Different subjects (father vs mother) - NOT a duplicate")

    # Eternals creator vs director
    q1 = find_question_by_id(questions, "mcu_225")
    q2 = find_question_by_id(questions, "mcu_229")
    print(f"\nmcu_225 vs mcu_229:")
    print(f"  Q1: {q1['question']}")
    print(f"  Q2: {q2['question']}")
    print(f"  VERDICT: Different questions (created comic vs directed film) - NOT a duplicate")

    # Rocket
    q1 = find_question_by_id(questions, "mcu_274")
    q2 = find_question_by_id(questions, "mcu_291")
    print(f"\nmcu_274 vs mcu_291:")
    print(f"  Q1: {q1['question']}")
    print(f"  Q2: {q2['question']}")
    print(f"  VERDICT: Different questions (adopts vs voices) - NOT a duplicate")

    # Check for any questions about the same character/topic
    print("\n" + "=" * 80)
    print("SCANNING FOR QUESTIONS ABOUT IDENTICAL TOPICS")
    print("=" * 80)

    # Group questions by key subjects
    subject_map = {}
    for q in questions:
        question_lower = q['question'].lower()

        # Extract potential subjects
        if 'tony stark' in question_lower and 'father' in question_lower:
            key = 'tony_stark_father'
        elif 'tony stark' in question_lower and 'daughter' in question_lower:
            key = 'tony_stark_daughter'
        elif 's.h.i.e.l.d' in question_lower or 'shield' in question_lower:
            key = 'shield'
        elif 'deadpool' in question_lower and 'year' in question_lower and '2' not in question_lower:
            key = 'deadpool_year'
        elif 'deadpool 2' in question_lower and 'year' in question_lower:
            key = 'deadpool2_year'
        elif 'spider-man 2' in question_lower and 'year' in question_lower:
            key = 'spiderman2_year'
        elif 'spider-man 3' in question_lower and 'year' in question_lower:
            key = 'spiderman3_year'
        else:
            continue

        if key not in subject_map:
            subject_map[key] = []
        subject_map[key].append(q)

    # Check for duplicates in same subject
    for subject, qs in subject_map.items():
        if len(qs) > 1:
            print(f"\n{subject.upper()} - {len(qs)} questions:")
            for q in qs:
                print(f"  {q['id']}: {q['question']}")

if __name__ == "__main__":
    file_path = "/home/user/fiztrivia/Fiz/Resources/Expansion Packs/expansion_marvel.json"
    questions = load_questions(file_path)
    analyze_true_semantic_duplicates(questions)
