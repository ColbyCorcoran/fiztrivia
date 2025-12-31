#!/usr/bin/env python3
"""
Validate and fix incorrect sport topics in questions.
Detects mismatches between question content and assigned topic.
"""

import json
import re

# Sport-specific keywords to detect the correct sport
SPORT_KEYWORDS = {
    'Football': [
        'touchdown', 'quarterback', 'downs', 'field goal', 'snap', 'nfl',
        'super bowl', 'offensive line', 'linebacker', 'end zone', 'fumble'
    ],
    'Basketball': [
        'basket', 'dunk', 'three-point', 'rebound', 'nba', 'foul shot',
        'court (basketball)', 'layup', 'free throw'
    ],
    'Tennis': [
        'wimbledon', 'serve', 'deuce', 'love', 'grand slam (tennis)',
        'court (tennis)', 'baseline', 'volley', 'ace', 'tiebreak', 'french open',
        'us open (tennis)', 'australian open'
    ],
    'Baseball': [
        'strike', 'batter', 'pitcher', 'inning', 'mlb', 'home run',
        'bases', 'outfield', 'diamond'
    ],
    'Golf': [
        'hole', 'par', 'birdie', 'eagle', 'bogey', 'green (golf)',
        'fairway', 'putt', 'tee', 'caddy', 'bunker'
    ],
    'Soccer': [
        'goal (soccer)', 'world cup', 'fifa', 'penalty kick', 'offside',
        'midfielder', 'goalkeeper'
    ],
    'Hockey': [
        'puck', 'rink', 'nhl', 'hat trick', 'icing', 'penalty box'
    ],
    'Boxing': [
        'round (boxing)', 'knockout', 'jab', 'uppercut', 'ring (boxing)',
        'heavyweight', 'referee (boxing)'
    ]
}

def detect_sport_from_content(question_text, options_text):
    """Detect which sport based on question and options content."""
    combined_text = (question_text + ' ' + options_text).lower()
    
    matches = {}
    
    for sport, keywords in SPORT_KEYWORDS.items():
        match_count = 0
        for keyword in keywords:
            if keyword.lower() in combined_text:
                match_count += 1
        
        if match_count > 0:
            matches[sport] = match_count
    
    if not matches:
        return None
    
    # Return sport with most keyword matches
    return max(matches, key=matches.get)

def validate_sport_topics(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    target_subcategories = ['Team Sports', 'Individual Sports', 'Extreme & Action Sports']
    
    mismatches = []
    
    sports_questions = data['categories'].get('Sports', [])
    
    for q in sports_questions:
        subcategory = q.get('subcategory', '')
        
        if subcategory not in target_subcategories:
            continue
        
        question_id = q.get('id', 'UNKNOWN')
        question_text = q.get('question', '')
        options = q.get('options', [])
        options_text = ' '.join(options)
        assigned_topic = q.get('topic')
        
        if not assigned_topic:
            continue  # Skip questions asking to identify sport
        
        # Detect sport from content
        detected_sport = detect_sport_from_content(question_text, options_text)
        
        if detected_sport and detected_sport != assigned_topic:
            mismatches.append({
                'id': question_id,
                'question': question_text,
                'options': options,
                'assigned_topic': assigned_topic,
                'detected_topic': detected_sport
            })
    
    return mismatches

def print_mismatches(mismatches):
    print("=" * 80)
    print("SPORT TOPIC VALIDATION - Mismatches Found")
    print("=" * 80)
    
    if not mismatches:
        print("\n✅ No mismatches found - all topics are correct!")
        return
    
    print(f"\n⚠️  Found {len(mismatches)} questions with incorrect topics:\n")
    
    for i, m in enumerate(mismatches, 1):
        print(f"{i}. {m['id']}")
        print(f"   Question: {m['question']}")
        print(f"   Options: {m['options']}")
        print(f"   ASSIGNED topic: {m['assigned_topic']} ❌")
        print(f"   DETECTED topic: {m['detected_topic']} ✅")
        print()

def main():
    questions_file = '/Users/colbycorcoran/Documents/App Development/Fiz/Fiz/Resources/questions.json'
    
    print("Validating sport topics in questions...\n")
    
    mismatches = validate_sport_topics(questions_file)
    print_mismatches(mismatches)
    
    print("\n" + "=" * 80)
    print(f"Total mismatches: {len(mismatches)}")
    print("=" * 80)

if __name__ == '__main__':
    main()
