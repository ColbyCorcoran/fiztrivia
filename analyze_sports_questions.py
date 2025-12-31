#!/usr/bin/env python3
"""
Analyze sports questions to find those missing sport names in the question text.
Focus on Team Sports, Individual Sports, and Extreme & Action Sports subcategories.
"""

import json
import re

# Common sports keywords to detect
TEAM_SPORTS = [
    'basketball', 'football', 'soccer', 'baseball', 'hockey', 'volleyball', 
    'cricket', 'rugby', 'lacrosse', 'polo', 'handball', 'american football',
    'nfl', 'nba', 'mlb', 'nhl', 'mls'
]

INDIVIDUAL_SPORTS = [
    'tennis', 'golf', 'boxing', 'wrestling', 'swimming', 'track', 'gymnastics',
    'skiing', 'skating', 'cycling', 'marathon', 'triathlon', 'archery', 'fencing',
    'judo', 'karate', 'taekwondo', 'badminton', 'squash', 'table tennis', 'bowling',
    'billiards', 'darts', 'surfing', 'rowing'
]

EXTREME_SPORTS = [
    'skateboarding', 'snowboarding', 'bmx', 'motocross', 'parkour', 'rock climbing',
    'skydiving', 'bungee', 'surfing', 'wakeboarding', 'kitesurfing', 'base jumping'
]

def has_sport_name(question_text, sport_list):
    """Check if question text contains any sport name."""
    question_lower = question_text.lower()
    
    for sport in sport_list:
        if sport.lower() in question_lower:
            return True, sport
    
    return False, None

def analyze_sports_questions(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    target_subcategories = {
        'Team Sports': TEAM_SPORTS,
        'Individual Sports': INDIVIDUAL_SPORTS,
        'Extreme & Action Sports': EXTREME_SPORTS
    }

    results = {subcat: {'with_name': [], 'without_name': []} for subcat in target_subcategories}

    sports_questions = data['categories'].get('Sports', [])

    for q in sports_questions:
        subcategory = q.get('subcategory', '')
        
        if subcategory not in target_subcategories:
            continue

        question_id = q.get('id', 'UNKNOWN')
        question_text = q.get('question', '')
        
        sport_list = target_subcategories[subcategory]
        has_name, sport_found = has_sport_name(question_text, sport_list)

        if has_name:
            results[subcategory]['with_name'].append({
                'id': question_id,
                'question': question_text,
                'sport': sport_found
            })
        else:
            results[subcategory]['without_name'].append({
                'id': question_id,
                'question': question_text,
                'options': q.get('options', [])
            })

    return results

def print_results(results):
    print("=" * 80)
    print("SPORTS QUESTIONS ANALYSIS - Missing Sport Names")
    print("=" * 80)

    for subcategory, data in results.items():
        total = len(data['with_name']) + len(data['without_name'])
        without_name_count = len(data['without_name'])
        
        print(f"\n{subcategory}:")
        print(f"  Total questions: {total}")
        print(f"  With sport name: {len(data['with_name'])}")
        print(f"  WITHOUT sport name: {without_name_count} ⚠️")

        if without_name_count > 0:
            print(f"\n  Questions needing sport names:")
            print(f"  {'-' * 76}")
            
            for i, q in enumerate(data['without_name'][:10], 1):  # Show first 10
                print(f"  {i}. {q['id']}")
                print(f"     Q: {q['question'][:70]}...")
                
                # Try to infer sport from options
                options_text = ' '.join(q['options']).lower()
                
                # Check for sport clues in options
                sport_clues = []
                if 'tennis' in options_text or 'wimbledon' in options_text or 'serve' in options_text:
                    sport_clues.append('tennis')
                if 'touchdown' in options_text or 'quarterback' in options_text:
                    sport_clues.append('football')
                if 'basket' in options_text or 'dunk' in options_text:
                    sport_clues.append('basketball')
                if 'goal' in options_text and 'net' in options_text:
                    sport_clues.append('soccer/hockey')
                
                if sport_clues:
                    print(f"     Possible sport(s): {', '.join(sport_clues)}")
                print()
            
            if without_name_count > 10:
                print(f"  ... and {without_name_count - 10} more")

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    total_without = sum(len(data['without_name']) for data in results.values())
    total_with = sum(len(data['with_name']) for data in results.values())
    total_all = total_without + total_with
    
    print(f"Total sports questions analyzed: {total_all}")
    print(f"Questions WITH sport names: {total_with} ({total_with/total_all*100:.1f}%)")
    print(f"Questions WITHOUT sport names: {total_without} ({total_without/total_all*100:.1f}%) ⚠️")

def main():
    questions_file = '/Users/colbycorcoran/Documents/App Development/Fiz/Fiz/Resources/questions.json'
    
    print("Analyzing sports questions for missing sport names...\n")
    
    results = analyze_sports_questions(questions_file)
    print_results(results)

if __name__ == '__main__':
    main()
