#!/usr/bin/env python3
"""
Marvel MCU Expansion Pack Quality Assurance Audit
Checks for duplicates, grammar issues, self-revealing answers, and accuracy problems
"""

import json
import re
from collections import defaultdict
from difflib import SequenceMatcher

def load_questions(file_path):
    """Load questions from JSON file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get('freePreviewQuestions', []) + data.get('paidQuestions', [])

def check_exact_duplicates(questions):
    """Find exact duplicate questions"""
    duplicates = []
    seen = {}

    for q in questions:
        question_text = q['question'].strip().lower()
        if question_text in seen:
            duplicates.append({
                'type': 'exact_duplicate',
                'question1_id': seen[question_text],
                'question2_id': q['id'],
                'question': q['question']
            })
        else:
            seen[question_text] = q['id']

    return duplicates

def similarity_ratio(str1, str2):
    """Calculate similarity between two strings"""
    return SequenceMatcher(None, str1.lower(), str2.lower()).ratio()

def check_semantic_duplicates(questions, threshold=0.7):
    """Find questions that are very similar (semantic duplicates)"""
    duplicates = []

    for i, q1 in enumerate(questions):
        for q2 in questions[i+1:]:
            ratio = similarity_ratio(q1['question'], q2['question'])
            if ratio >= threshold:
                # Check if they're asking about the same subject
                duplicates.append({
                    'type': 'semantic_duplicate',
                    'similarity': f"{ratio:.0%}",
                    'question1_id': q1['id'],
                    'question1': q1['question'],
                    'question2_id': q2['id'],
                    'question2': q2['question']
                })

    return duplicates

def check_grammar_and_typos(questions):
    """Check for common grammar issues and typos"""
    issues = []

    # Common patterns to check
    patterns = {
        r'\b(a)\s+([aeiou])': 'Should use "an" before vowel',
        r'\b(an)\s+([^aeiou\s])': 'Should use "a" before consonant',
        r'\s{2,}': 'Multiple spaces',
        r'[.!?]{2,}': 'Multiple punctuation marks',
        r'\b(teh|hte|adn|nad)\b': 'Common typo',
        r'^[a-z]': 'Question should start with capital letter',
        r'[^?.]$': 'Question should end with punctuation',
    }

    for q in questions:
        question_text = q['question']

        # Check patterns
        for pattern, description in patterns.items():
            if re.search(pattern, question_text):
                issues.append({
                    'type': 'grammar',
                    'id': q['id'],
                    'question': question_text,
                    'issue': description
                })

        # Check options
        for opt in q['options']:
            if opt.strip() != opt:
                issues.append({
                    'type': 'whitespace',
                    'id': q['id'],
                    'question': question_text,
                    'issue': f'Option has leading/trailing whitespace: "{opt}"'
                })

    return issues

def check_self_revealing(questions):
    """Check if answer appears in question text"""
    issues = []

    for q in questions:
        question_lower = q['question'].lower()
        correct_lower = q['correct_answer'].lower()

        # Check if the exact answer appears in the question
        if correct_lower in question_lower:
            # Make sure it's not a coincidence (e.g., "in Iron Man" vs "Iron Man")
            # Check if it's a substantial match
            if len(correct_lower) > 5 or correct_lower == question_lower:
                issues.append({
                    'type': 'self_revealing',
                    'id': q['id'],
                    'question': q['question'],
                    'answer': q['correct_answer']
                })

    return issues

def check_confusing_wording(questions):
    """Check for potentially confusing questions"""
    issues = []

    confusing_patterns = [
        (r'\bnot\b.*\bnot\b', 'Double negative'),
        (r'\b(which of these|which one|what one)\b.*\b(is not|isn\'t|aren\'t)\b', 'Negative question'),
    ]

    for q in questions:
        question_text = q['question']

        for pattern, description in confusing_patterns:
            if re.search(pattern, question_text, re.IGNORECASE):
                issues.append({
                    'type': 'confusing',
                    'id': q['id'],
                    'question': question_text,
                    'issue': description
                })

    return issues

def manual_review_needed(questions):
    """Flag questions that need manual review for accuracy"""
    review_needed = []

    # Look for questions with specific patterns that might need verification
    review_patterns = [
        (r'\b(first|last|only|never|always)\b', 'Absolute claim - verify accuracy'),
        (r'\b\d{4}\b', 'Specific year mentioned - verify date'),
        (r'\b(how many|number of)\b', 'Numeric fact - verify accuracy'),
    ]

    for q in questions:
        question_text = q['question']

        for pattern, reason in review_patterns:
            if re.search(pattern, question_text, re.IGNORECASE):
                review_needed.append({
                    'type': 'needs_verification',
                    'id': q['id'],
                    'question': question_text,
                    'answer': q['correct_answer'],
                    'reason': reason
                })
                break  # Only flag once per question

    return review_needed

def generate_report(questions):
    """Generate comprehensive QA report"""

    print("=" * 80)
    print("MARVEL MCU EXPANSION PACK - QUALITY ASSURANCE AUDIT REPORT")
    print("=" * 80)
    print(f"\nTotal Questions: {len(questions)}\n")

    # 1. Exact Duplicates
    exact_dupes = check_exact_duplicates(questions)
    if exact_dupes:
        print("\n" + "=" * 80)
        print("🚨 FLAG FOR REPLACEMENT: EXACT DUPLICATES")
        print("=" * 80)
        for d in exact_dupes:
            print(f"\n❌ {d['question1_id']} and {d['question2_id']}")
            print(f"   Question: {d['question']}")
    else:
        print("\n✅ No exact duplicates found")

    # 2. Semantic Duplicates
    semantic_dupes = check_semantic_duplicates(questions, threshold=0.75)
    if semantic_dupes:
        print("\n" + "=" * 80)
        print("🚨 FLAG FOR REPLACEMENT: SEMANTIC DUPLICATES (75%+ similar)")
        print("=" * 80)
        for d in semantic_dupes:
            print(f"\n❌ {d['question1_id']} vs {d['question2_id']} ({d['similarity']} similar)")
            print(f"   Q1: {d['question1']}")
            print(f"   Q2: {d['question2']}")
    else:
        print("\n✅ No semantic duplicates found (75%+ threshold)")

    # 3. Grammar and Typos
    grammar_issues = check_grammar_and_typos(questions)
    if grammar_issues:
        print("\n" + "=" * 80)
        print("🔧 AUTO-FIX: GRAMMAR & TYPOS")
        print("=" * 80)
        for issue in grammar_issues:
            print(f"\n⚠️  {issue['id']}")
            print(f"   Question: {issue['question']}")
            print(f"   Issue: {issue['issue']}")
    else:
        print("\n✅ No grammar or typo issues found")

    # 4. Self-Revealing Answers
    self_revealing = check_self_revealing(questions)
    if self_revealing:
        print("\n" + "=" * 80)
        print("🚨 FLAG FOR REPLACEMENT: SELF-REVEALING ANSWERS")
        print("=" * 80)
        for issue in self_revealing:
            print(f"\n❌ {issue['id']}")
            print(f"   Question: {issue['question']}")
            print(f"   Answer: {issue['answer']}")
    else:
        print("\n✅ No self-revealing answers found")

    # 5. Confusing Wording
    confusing = check_confusing_wording(questions)
    if confusing:
        print("\n" + "=" * 80)
        print("⚠️  NEEDS VERIFICATION: CONFUSING WORDING")
        print("=" * 80)
        for issue in confusing:
            print(f"\n⚠️  {issue['id']}")
            print(f"   Question: {issue['question']}")
            print(f"   Issue: {issue['issue']}")
    else:
        print("\n✅ No confusing wording found")

    # 6. Manual Review for Accuracy
    review = manual_review_needed(questions)
    if review:
        print("\n" + "=" * 80)
        print("📋 NEEDS VERIFICATION: FACTUAL ACCURACY (Sample)")
        print("=" * 80)
        print("(Showing first 20 questions that contain absolute claims or specific facts)")
        for issue in review[:20]:
            print(f"\n⚠️  {issue['id']}")
            print(f"   Question: {issue['question']}")
            print(f"   Answer: {issue['answer']}")
            print(f"   Reason: {issue['reason']}")

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Exact Duplicates: {len(exact_dupes)}")
    print(f"Semantic Duplicates (75%+): {len(semantic_dupes)}")
    print(f"Grammar/Typo Issues: {len(grammar_issues)}")
    print(f"Self-Revealing Answers: {len(self_revealing)}")
    print(f"Confusing Wording: {len(confusing)}")
    print(f"Questions Needing Verification: {len(review)}")
    print("=" * 80)

    return {
        'exact_duplicates': exact_dupes,
        'semantic_duplicates': semantic_dupes,
        'grammar_issues': grammar_issues,
        'self_revealing': self_revealing,
        'confusing': confusing,
        'needs_verification': review
    }

if __name__ == "__main__":
    file_path = "/home/user/fiztrivia/Fiz/Resources/Expansion Packs/expansion_marvel.json"
    questions = load_questions(file_path)
    results = generate_report(questions)
