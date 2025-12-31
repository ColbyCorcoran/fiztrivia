#!/usr/bin/env python3
"""
Fix incorrect sport topics in questions.
"""

import json
from datetime import datetime

# Manual corrections for known mismatches
TOPIC_CORRECTIONS = {
    'spt_103': 'Golf',  # hole in one
    'spt_106': 'Golf',  # the green in golf
    'spt_115': 'Golf',  # fairway in golf
    'spt_117': 'Tennis',  # Wimbledon surface
    'spt_123': 'Tennis',  # US Open surface
    'spt_127': 'Tennis',  # US Open tennis
    'spt_133': 'Tennis',  # bagel in tennis
    'spt_138': 'Tennis',  # baseline and service line
    'spt_213': 'Tennis',  # French Open surface
}

def fix_sport_topics(json_file, output_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    fixed_count = 0
    sports_questions = data['categories'].get('Sports', [])
    
    for q in sports_questions:
        question_id = q.get('id', 'UNKNOWN')
        
        if question_id in TOPIC_CORRECTIONS:
            old_topic = q.get('topic')
            new_topic = TOPIC_CORRECTIONS[question_id]
            
            print(f"{question_id}: {old_topic} → {new_topic}")
            print(f"  Q: {q['question'][:70]}...")
            print()
            
            q['topic'] = new_topic
            fixed_count += 1
    
    # Write fixed data
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    return fixed_count

def main():
    questions_file = '/Users/colbycorcoran/Documents/App Development/Fiz/Fiz/Resources/questions.json'
    
    print("Fixing incorrect sport topics...\n")
    print("=" * 80)
    
    fixed = fix_sport_topics(questions_file, questions_file)
    
    print("=" * 80)
    print(f"Total topics fixed: {fixed}")

if __name__ == '__main__':
    main()
