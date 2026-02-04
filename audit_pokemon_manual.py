#!/usr/bin/env python3
"""
Manual QA audit for Pokémon pack - focusing on real issues only
"""

import json
import re
from difflib import SequenceMatcher

def load_pack(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def is_template_question(q1, q2):
    """Check if two questions follow the same template but ask about different subjects"""
    # Common templates that are VALID when asking about different subjects
    templates = [
        r"What (?:type|Pokemon|move|ability|item) (?:is|does) (\w+)",
        r"Who (?:is|does) (\w+)",
        r"Which (\w+)",
        r"What is (\w+)'s",
        r"In which (\w+)",
        r"How (\w+)",
    ]

    # Extract key nouns from both questions
    q1_words = set(re.findall(r'\b[A-Z][a-z]+\b', q1))
    q2_words = set(re.findall(r'\b[A-Z][a-z]+\b', q2))

    # If they share very few proper nouns, likely different subjects
    shared = q1_words & q2_words
    if len(shared) <= 1:  # At most 1 shared proper noun (like "Pokémon")
        return True

    return False

def find_real_duplicates(questions):
    """Find real duplicates, excluding template questions"""
    duplicates = []

    for i, q1 in enumerate(questions):
        for j in range(i+1, len(questions)):
            q2 = questions[j]

            similarity = SequenceMatcher(None, q1['question'].lower(), q2['question'].lower()).ratio()

            # High similarity threshold
            if similarity >= 0.90:
                # Check if it's a template question
                if not is_template_question(q1['question'], q2['question']):
                    duplicates.append({
                        'id1': q1['id'],
                        'id2': q2['id'],
                        'q1': q1['question'],
                        'q2': q2['question'],
                        'similarity': f"{similarity:.1%}"
                    })

    return duplicates

def find_real_self_revealing(questions):
    """Find questions where the answer genuinely gives away the question"""
    issues = []

    for q in questions:
        question = q['question']
        answer = q['correct_answer']

        # Skip cases where answer appearing in question is appropriate
        skip_patterns = [
            r"Who is the main character in.*" + re.escape(answer),  # "Red" in "Pokémon Red"
            r"Who is .*'s " + re.escape(answer),  # "Pikachu" in "Ash's Pikachu"
            r"What is the name of.*" + re.escape(answer),  # Name questions
            r"Which.*region.*" + re.escape(answer),  # Region names in context
            r"In.*" + re.escape(answer) + ".*Movie",  # Movie names
        ]

        # Check if answer is in question in a self-revealing way
        if answer.lower() in question.lower():
            is_legitimate = False
            for pattern in skip_patterns:
                if re.search(pattern, question, re.IGNORECASE):
                    is_legitimate = True
                    break

            if not is_legitimate:
                issues.append({
                    'id': q['id'],
                    'question': question,
                    'answer': answer
                })

    return issues

def check_specific_issues(questions):
    """Check for specific known Pokémon trivia issues"""
    issues = {
        'grammar': [],
        'accuracy': [],
        'confusing': []
    }

    for q in questions:
        question = q['question']

        # Grammar checks
        if not question.endswith('?'):
            issues['grammar'].append({'id': q['id'], 'question': question, 'issue': 'Missing ?'})

        if '  ' in question:  # Double spaces
            issues['grammar'].append({'id': q['id'], 'question': question, 'issue': 'Double space'})

        # Check options
        for opt in q['options']:
            if '  ' in opt:
                issues['grammar'].append({'id': q['id'], 'question': question, 'issue': f'Double space in option: {opt}'})

        # Common Pokémon errors
        if 'Pokemon' in question and 'Pokémon' not in question:
            issues['grammar'].append({'id': q['id'], 'question': question, 'issue': 'Missing accent: Pokémon'})

        # Check for confusing double negatives
        if re.search(r'\b(not|never|except)\b.*\b(not|never|except)\b', question, re.IGNORECASE):
            issues['confusing'].append({'id': q['id'], 'question': question, 'issue': 'Double negative'})

    return issues

def main():
    filepath = '/home/user/fiztrivia/Fiz/Resources/Expansion Packs/expansion_pokemon.json'
    pack = load_pack(filepath)

    all_questions = pack.get('freePreviewQuestions', []) + pack.get('paidQuestions', [])

    print("="*80)
    print("POKÉMON PACK - MANUAL QA AUDIT")
    print("="*80)
    print(f"Total questions: {len(all_questions)}\n")

    # Find real duplicates
    print("Checking for TRUE duplicates (excluding template questions)...")
    duplicates = find_real_duplicates(all_questions)

    # Find real self-revealing questions
    print("Checking for self-revealing questions...")
    self_revealing = find_real_self_revealing(all_questions)

    # Check specific issues
    print("Checking for grammar and accuracy issues...")
    specific_issues = check_specific_issues(all_questions)

    # Report
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    total_issues = (len(duplicates) + len(self_revealing) +
                   len(specific_issues['grammar']) +
                   len(specific_issues['accuracy']) +
                   len(specific_issues['confusing']))
    print(f"Total Issues: {total_issues}")
    print(f"  - Duplicates: {len(duplicates)}")
    print(f"  - Self-revealing: {len(self_revealing)}")
    print(f"  - Grammar: {len(specific_issues['grammar'])}")
    print(f"  - Accuracy: {len(specific_issues['accuracy'])}")
    print(f"  - Confusing: {len(specific_issues['confusing'])}")

    # Detailed output
    if duplicates:
        print("\n" + "="*80)
        print("TRUE DUPLICATES (FLAG FOR REPLACEMENT)")
        print("="*80)
        for i, dup in enumerate(duplicates, 1):
            print(f"\n{i}. IDs: {dup['id1']} & {dup['id2']} ({dup['similarity']} similar)")
            print(f"   Q1: {dup['q1']}")
            print(f"   Q2: {dup['q2']}")

    if self_revealing:
        print("\n" + "="*80)
        print("SELF-REVEALING QUESTIONS (NEEDS VERIFICATION)")
        print("="*80)
        for i, issue in enumerate(self_revealing, 1):
            print(f"\n{i}. ID: {issue['id']}")
            print(f"   Q: {issue['question']}")
            print(f"   A: {issue['answer']}")

    if specific_issues['grammar']:
        print("\n" + "="*80)
        print("GRAMMAR ISSUES (AUTO-FIX)")
        print("="*80)
        for i, issue in enumerate(specific_issues['grammar'], 1):
            print(f"\n{i}. ID: {issue['id']}")
            print(f"   Issue: {issue['issue']}")
            print(f"   Q: {issue['question']}")

    if specific_issues['confusing']:
        print("\n" + "="*80)
        print("CONFUSING WORDING (NEEDS VERIFICATION)")
        print("="*80)
        for i, issue in enumerate(specific_issues['confusing'], 1):
            print(f"\n{i}. ID: {issue['id']}")
            print(f"   Issue: {issue['issue']}")
            print(f"   Q: {issue['question']}")

    print("\n" + "="*80)

if __name__ == '__main__':
    main()
