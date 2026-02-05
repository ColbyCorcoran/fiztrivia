#!/usr/bin/env python3
import json
import re
from collections import defaultdict

def audit_pack(filepath, pack_name):
    print(f"\n{'='*60}")
    print(f"{pack_name} PACK AUDIT")
    print(f"{'='*60}\n")

    with open(filepath, 'r') as f:
        data = json.load(f)

    all_questions = data.get('freePreviewQuestions', []) + data.get('paidQuestions', [])
    total = len(all_questions)

    print(f"Total questions: {total}\n")

    # Check for exact duplicates
    question_texts = defaultdict(list)
    for q in all_questions:
        question_texts[q['question'].lower().strip()].append(q['id'])

    exact_dupes = {k: v for k, v in question_texts.items() if len(v) > 1}

    # Check for self-revealing
    self_revealing = []
    for q in all_questions:
        question = q['question'].lower()
        answer = q['correct_answer'].lower()

        # Check if answer words appear in question
        answer_words = set(answer.split())
        question_words = set(question.split())

        # Remove common words
        common = {'a', 'an', 'the', 'is', 'are', 'was', 'were', 'in', 'on', 'at', 'to', 'for', 'of', 'and', 'or'}
        answer_words -= common
        question_words -= common

        # Check for significant overlap
        overlap = answer_words & question_words
        if overlap and len(overlap) >= 1:
            # Check if it's actually revealing (not just common terms)
            significant_overlap = [w for w in overlap if len(w) > 4 or w in answer]
            if significant_overlap:
                self_revealing.append({
                    'id': q['id'],
                    'question': q['question'],
                    'answer': q['correct_answer'],
                    'overlap': significant_overlap
                })

    # Report
    print(f"EXACT DUPLICATES: {len(exact_dupes)}")
    if exact_dupes:
        for question, ids in list(exact_dupes.items())[:5]:
            print(f"  - {ids}: '{question[:60]}...'")

    print(f"\nSELF-REVEALING: {len(self_revealing)}")
    for item in self_revealing[:10]:
        print(f"  - {item['id']}: Q: '{item['question'][:60]}...' → A: '{item['answer']}'")
        print(f"    Overlap: {item['overlap']}")

    print(f"\nTOTAL ISSUES: {len(exact_dupes) + len(self_revealing)}")
    print(f"Quality Score: {((total - len(exact_dupes) - len(self_revealing)) / total * 100):.1f}%")

    return {
        'total': total,
        'exact_dupes': len(exact_dupes),
        'self_revealing': len(self_revealing)
    }

# Audit Star Wars
sw_stats = audit_pack(
    '/home/user/fiztrivia/Fiz/Resources/Expansion Packs/expansion_star_wars.json',
    'STAR WARS'
)

# Audit The Office
office_stats = audit_pack(
    '/home/user/fiztrivia/Fiz/Resources/Expansion Packs/expansion_the_office.json',
    'THE OFFICE'
)

print(f"\n{'='*60}")
print("SUMMARY OF REMAINING PACKS")
print(f"{'='*60}")
print(f"Star Wars: {sw_stats['exact_dupes'] + sw_stats['self_revealing']} issues ({(sw_stats['exact_dupes'] + sw_stats['self_revealing'])/sw_stats['total']*100:.1f}%)")
print(f"The Office: {office_stats['exact_dupes'] + office_stats['self_revealing']} issues ({(office_stats['exact_dupes'] + office_stats['self_revealing'])/office_stats['total']*100:.1f}%)")
