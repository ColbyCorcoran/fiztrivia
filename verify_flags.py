#!/usr/bin/env python3
"""Verify new Flags questions for duplicates"""
import json
from difflib import SequenceMatcher

def similarity_ratio(str1, str2):
    return SequenceMatcher(None, str1.lower(), str2.lower()).ratio()

def check_duplicates():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    all_questions = []
    for category in data['categories'].values():
        all_questions.extend(category)

    # Get the new Flags questions (geo_181 to geo_240)
    new_questions = [q for q in all_questions if q['id'] >= 'geo_181' and q['id'] <= 'geo_240']
    existing_questions = [q for q in all_questions if q['id'] < 'geo_181' or q['id'] > 'geo_240']

    print(f"Checking {len(new_questions)} new Flags questions against {len(existing_questions)} existing questions...\n")

    duplicates_found = []

    for new_q in new_questions:
        for exist_q in existing_questions:
            ratio = similarity_ratio(new_q['question'], exist_q['question'])

            # Check for exact duplicates (100%)
            if ratio == 1.0:
                duplicates_found.append({
                    'new_id': new_q['id'],
                    'new_question': new_q['question'],
                    'existing_id': exist_q['id'],
                    'existing_question': exist_q['question'],
                    'similarity': ratio,
                    'type': 'EXACT'
                })
            # Check for semantic duplicates (>90% similar with same answer)
            elif ratio > 0.90 and new_q['correct_answer'].lower() == exist_q['correct_answer'].lower():
                duplicates_found.append({
                    'new_id': new_q['id'],
                    'new_question': new_q['question'],
                    'existing_id': exist_q['id'],
                    'existing_question': exist_q['question'],
                    'similarity': ratio,
                    'type': 'SEMANTIC'
                })
            # Check for potential duplicates (>70% similar with same answer)
            elif ratio > 0.70 and new_q['correct_answer'].lower() == exist_q['correct_answer'].lower():
                duplicates_found.append({
                    'new_id': new_q['id'],
                    'new_question': new_q['question'],
                    'existing_id': exist_q['id'],
                    'existing_question': exist_q['question'],
                    'similarity': ratio,
                    'type': 'POTENTIAL'
                })

    if duplicates_found:
        print(f"❌ Found {len(duplicates_found)} duplicates:\n")
        for dup in duplicates_found:
            print(f"[{dup['type']}] {dup['similarity']:.1%} similar")
            print(f"  NEW {dup['new_id']}: {dup['new_question']}")
            print(f"  EXISTING {dup['existing_id']}: {dup['existing_question']}\n")
    else:
        print("✅ No duplicates found! All questions are unique.")

    return duplicates_found

if __name__ == '__main__':
    check_duplicates()
