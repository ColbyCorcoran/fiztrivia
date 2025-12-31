#!/usr/bin/env python3
"""
Add sport names to questions where needed.
Only adds to questions with a 'topic' field (questions ABOUT a sport).
Skips questions with topic=null (questions asking to IDENTIFY a sport).
"""

import json
import re
from datetime import datetime

def has_sport_name_in_question(question_text, sport_name):
    """Check if sport name is already in the question."""
    if not sport_name:
        return True  # No sport to add
    
    question_lower = question_text.lower()
    sport_lower = sport_name.lower()
    
    # Check for the sport name or common variations
    if sport_lower in question_lower:
        return True
    
    # Check for sport-specific terms that make it obvious
    sport_terms = {
        'Football': ['touchdown', 'quarterback', 'nfl', 'super bowl'],
        'Basketball': ['basket', 'nba', 'dunk', 'three-point'],
        'Tennis': ['wimbledon', 'grand slam', 'serve', 'court (tennis)'],
        'Baseball': ['mlb', 'pitcher', 'batter', 'inning'],
        'Golf': ['par', 'birdie', 'hole', 'putt'],
        'Soccer': ['goal', 'world cup', 'fifa'],
        'Hockey': ['nhl', 'puck', 'rink'],
    }
    
    if sport_name in sport_terms:
        for term in sport_terms[sport_name]:
            if term in question_lower:
                return True
    
    return False

def add_sport_name_to_question(question_text, sport_name):
    """Add sport name to question in a natural way."""
    if not sport_name:
        return question_text
    
    question_text = question_text.strip()
    
    # Pattern 1: "What is..." → "In [sport], what is..."
    if question_text.lower().startswith('what is '):
        return f"In {sport_name.lower()}, what is {question_text[8:]}"
    
    # Pattern 2: "What are..." → "In [sport], what are..."
    if question_text.lower().startswith('what are '):
        return f"In {sport_name.lower()}, what are {question_text[9:]}"
    
    # Pattern 3: "How many..." → "In [sport], how many..."
    if question_text.lower().startswith('how many '):
        return f"In {sport_name.lower()}, how many {question_text[9:]}"
    
    # Pattern 4: "Which..." → "In [sport], which..."
    if question_text.lower().startswith('which '):
        return f"In {sport_name.lower()}, which {question_text[6:]}"
    
    # Pattern 5: "What does..." → "In [sport], what does..."
    if question_text.lower().startswith('what does '):
        return f"In {sport_name.lower()}, what does {question_text[10:]}"
    
    # Pattern 6: "When..." → "In [sport], when..."
    if question_text.lower().startswith('when '):
        return f"In {sport_name.lower()}, when {question_text[5:]}"
    
    # Default: Add to beginning
    return f"In {sport_name.lower()}, {question_text[0].lower()}{question_text[1:]}"

def process_sports_questions(json_file, output_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    target_subcategories = ['Team Sports', 'Individual Sports', 'Extreme & Action Sports']
    
    modified_count = 0
    skipped_no_topic = 0
    skipped_has_name = 0
    
    sports_questions = data['categories'].get('Sports', [])
    
    for q in sports_questions:
        subcategory = q.get('subcategory', '')
        
        if subcategory not in target_subcategories:
            continue
        
        question_id = q.get('id', 'UNKNOWN')
        question_text = q.get('question', '')
        sport_name = q.get('topic')
        
        # Skip if no topic (question is asking to identify the sport)
        if not sport_name:
            skipped_no_topic += 1
            continue
        
        # Skip if sport name already in question
        if has_sport_name_in_question(question_text, sport_name):
            skipped_has_name += 1
            continue
        
        # Add sport name
        new_question = add_sport_name_to_question(question_text, sport_name)
        
        print(f"{question_id} ({sport_name}):")
        print(f"  OLD: {question_text}")
        print(f"  NEW: {new_question}")
        print()
        
        q['question'] = new_question
        modified_count += 1
    
    # Write modified data
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    return modified_count, skipped_no_topic, skipped_has_name

def main():
    questions_file = '/Users/colbycorcoran/Documents/App Development/Fiz/Fiz/Resources/questions.json'
    
    # Create backup
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = questions_file.replace('.json', f'_backup_{timestamp}.json')
    
    import shutil
    shutil.copy(questions_file, backup_file)
    print(f"✅ Backup created: {backup_file}\n")
    
    print("Adding sport names to questions...\n")
    print("=" * 80)
    
    modified, skipped_no_topic, skipped_has_name = process_sports_questions(
        questions_file, questions_file
    )
    
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Modified: {modified} questions")
    print(f"Skipped (no topic - asking to identify sport): {skipped_no_topic} questions")
    print(f"Skipped (sport name already present): {skipped_has_name} questions")
    print(f"\nTotal processed: {modified + skipped_no_topic + skipped_has_name}")

if __name__ == '__main__':
    main()
