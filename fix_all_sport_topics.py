#!/usr/bin/env python3
"""
Fix ALL incorrect sport topics based on comprehensive analysis.
"""

import json

# Complete corrections based on thorough analysis
TOPIC_CORRECTIONS = {
    'spt_103': 'Golf',      # "hole in one stroke"
    'spt_106': 'Golf',      # "the green in golf"
    'spt_115': 'Golf',      # "fairway in golf"
    'spt_117': 'Tennis',    # "Wimbledon surface"
    'spt_123': 'Tennis',    # "US Open surface"
    'spt_125': 'Tennis',    # "tennis court made of"
    'spt_127': 'Tennis',    # "US Open tennis tournament"
    'spt_133': 'Tennis',    # "bagel in tennis"
    'spt_138': 'Tennis',    # "baseline and service line"
    'spt_213': 'Tennis',    # "French Open surface"
}

def fix_sport_topics(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    fixed_count = 0
    sports_questions = data['categories'].get('Sports', [])
    
    for q in sports_questions:
        question_id = q.get('id', 'UNKNOWN')
        
        if question_id in TOPIC_CORRECTIONS:
            old_topic = q.get('topic')
            new_topic = TOPIC_CORRECTIONS[question_id]
            
            print(f"✓ {question_id}: {old_topic} → {new_topic}")
            
            q['topic'] = new_topic
            fixed_count += 1
    
    # Write fixed data
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    return fixed_count

def main():
    questions_file = '/Users/colbycorcoran/Documents/App Development/Fiz/Fiz/Resources/questions.json'
    
    print("Fixing sport topics...\n")
    fixed = fix_sport_topics(questions_file)
    print(f"\n✅ Fixed {fixed} topics")

if __name__ == '__main__':
    main()
