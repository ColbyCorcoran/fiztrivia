#!/usr/bin/env python3
"""
Check all Church History questions to ensure they're post-Biblical
"""

import json

def check_church_history():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    history = data['categories']['History']
    church_history = [q for q in history if q.get('subcategory') == 'Church History']

    print("=" * 80)
    print("CHURCH HISTORY TIMELINE VERIFICATION")
    print("=" * 80)
    print(f"\nTotal Church History questions: {len(church_history)}")
    print("\nChecking for Biblical-era questions (should be in Bible category)...\n")

    # Keywords/phrases that might indicate Biblical times
    biblical_indicators = [
        'jesus', 'christ', 'apostle', 'disciple', 'peter', 'paul', 'john',
        'gospel', 'acts', 'testament', '325 ad', '313 ad', 'constantine',
        'nicaea', 'nicea', 'arian', 'early church'
    ]

    potential_issues = []

    for q in church_history:
        question_lower = q['question'].lower()
        answer_lower = q.get('correct_answer', '').lower()
        
        # Check for Biblical-era indicators
        found_indicators = []
        for indicator in biblical_indicators:
            if indicator in question_lower or indicator in answer_lower:
                found_indicators.append(indicator)
        
        if found_indicators:
            potential_issues.append({
                'id': q['id'],
                'question': q['question'],
                'answer': q.get('correct_answer'),
                'indicators': found_indicators
            })

    if potential_issues:
        print(f"⚠️  Found {len(potential_issues)} questions that may reference Biblical times:\n")
        for issue in potential_issues:
            print(f"[{issue['id']}] {issue['question']}")
            print(f"   Answer: {issue['answer']}")
            print(f"   Indicators: {', '.join(issue['indicators'])}")
            print()
    else:
        print("✅ No Biblical-era questions found in Church History!")
        print("All Church History questions appear to be post-Biblical.")

    print("=" * 80)
    print("\nNOTE: Church History should start after the Biblical period ends.")
    print("      Biblical period: Creation through ~90 AD (Book of Revelation)")
    print("      Church History: ~100 AD onwards")
    print()
    print("Questions about early church councils (Nicaea 325 AD), early church")
    print("fathers, and the spread of Christianity ARE appropriate for Church")
    print("History as they occurred after the Biblical canon was completed.")
    print("=" * 80)

if __name__ == "__main__":
    check_church_history()
