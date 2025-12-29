#!/usr/bin/env python3
"""Analyze Sports questions and categorize by sport topic"""
import json
import re

def identify_sport_topic(question_text, options_text, answer_text):
    """Identify which sport a question is about based on keywords"""
    combined = f"{question_text} {options_text} {answer_text}".lower()

    # Team sports keywords
    if any(word in combined for word in ['soccer', 'goal keeper', 'penalty kick', 'world cup', 'fifa', 'pitch ']):
        return 'Soccer'
    if any(word in combined for word in ['touchdown', 'quarterback', 'nfl', 'super bowl', 'gridiron', 'linebacker', 'fumble', 'field goal', 'down ', 'yards']):
        return 'Football'
    if any(word in combined for word in ['basketball', 'nba', 'dunk', 'layup', 'three-point', 'rebound', 'hoop', 'court ']):
        return 'Basketball'
    if any(word in combined for word in ['baseball', 'mlb', 'pitcher', 'batter', 'home run', 'inning', 'strike', 'bases', 'diamond', 'catcher']):
        return 'Baseball'
    if any(word in combined for word in ['hockey', 'nhl', 'puck', 'ice rink', 'goalie mask', 'zamboni', 'stanley cup', 'hat trick']):
        return 'Hockey'
    if any(word in combined for word in ['volleyball', 'spike', 'serve', 'net height']):
        return 'Volleyball'
    if any(word in combined for word in ['rugby', 'scrum', 'try line']):
        return 'Rugby'
    if any(word in combined for word in ['cricket', 'wicket', 'bowler', 'batsman']):
        return 'Cricket'

    # Individual sports keywords
    if any(word in combined for word in ['tennis', 'wimbledon', 'grand slam', 'ace', 'deuce', 'love', 'court', 'serve', 'racket']):
        return 'Tennis'
    if any(word in combined for word in ['golf', 'birdie', 'bogey', 'par', 'hole', 'tee', 'putt', 'fairway', 'green', 'masters', 'pga']):
        return 'Golf'
    if any(word in combined for word in ['swimming', 'freestyle', 'butterfly', 'backstroke', 'pool', 'lap']):
        return 'Swimming'
    if any(word in combined for word in ['boxing', 'knockout', 'ring', 'round', 'punch', 'heavyweight']):
        return 'Boxing'
    if any(word in combined for word in ['track', 'sprint', 'relay', 'hurdles', 'marathon', 'meter dash']):
        return 'Track & Field'
    if any(word in combined for word in ['gymnastics', 'vault', 'beam', 'floor exercise', 'parallel bars']):
        return 'Gymnastics'
    if any(word in combined for word in ['wrestling', 'pin', 'takedown', 'mat ']):
        return 'Wrestling'

    # Extreme/Action sports
    if any(word in combined for word in ['skateboard', 'halfpipe', 'ollie', 'kickflip']):
        return 'Skateboarding'
    if any(word in combined for word in ['surfing', 'wave', 'board']):
        return 'Surfing'
    if any(word in combined for word in ['snowboard', 'ski', 'slope', 'slalom']):
        return 'Winter Sports'

    return None

def main():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    sports = data['categories']['Sports']

    # Analyze each subcategory
    for subcat in ['Team Sports', 'Individual Sports', 'International Competition']:
        questions = [q for q in sports if q.get('subcategory') == subcat]
        print(f"\n{'='*80}")
        print(f"{subcat}: {len(questions)} questions")
        print('='*80)

        # Count by identified topic
        topics = {}
        for q in questions:
            options_text = ' '.join(q['options'])
            topic = identify_sport_topic(q['question'], options_text, q['correct_answer'])
            if topic not in topics:
                topics[topic] = []
            topics[topic].append(q['id'])

        print(f"\nQuestions by topic:")
        for topic in sorted(topics.keys(), key=lambda x: (x is None, x)):
            count = len(topics[topic])
            print(f"  {topic or 'General/Other'}: {count} questions")
            if count <= 10:
                print(f"    IDs: {', '.join(topics[topic])}")

if __name__ == "__main__":
    main()
