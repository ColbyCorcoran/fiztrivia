#!/usr/bin/env python3
"""
Auto-categorize sports questions into 6 general subtopics.
"""

import json

def categorize_sports_question(question_text, options_text="", answer_text=""):
    """
    Categorize a sports question based on keywords and content.

    Subtopics:
    1. Rules & Gameplay - rules, scoring, positions, gameplay mechanics
    2. Players & Teams - specific players, teams, records
    3. Championships & Tournaments - major events, tournaments, championships
    4. History & Records - historical facts, years, milestones, all-time records
    5. Equipment & Terminology - equipment, terms, definitions
    6. Trivia & Facts - general knowledge, catch-all
    """

    full_text = (question_text + " " + options_text + " " + answer_text).lower()

    # Championships & Tournaments (check first - specific events)
    championship_keywords = [
        'super bowl', 'world series', 'nba finals', 'stanley cup',
        'world cup', 'olympics', 'olympic', 'grand slam', 'majors',
        'championship', 'tournament', 'hosted', 'fifa'
    ]
    if any(keyword in full_text for keyword in championship_keywords):
        return "Championships & Tournaments"

    # History & Records (check before Players & Teams to catch record-holders)
    history_keywords = [
        'year was', 'when was', 'first', 'introduced', 'history',
        'holds the record', 'most career', 'most points in', 'most rebounds',
        'most assists', 'most touchdown', 'all time', 'most decorated'
    ]
    if any(keyword in full_text for keyword in history_keywords):
        return "History & Records"

    # Players & Teams
    players_teams_keywords = [
        'which player', 'which team', 'who holds', 'who has',
        'which country', 'team is known as', 'player is known as',
        'team did', 'drafted', "'s team", 'play for'
    ]
    if any(keyword in full_text for keyword in players_teams_keywords):
        return "Players & Teams"

    # Equipment & Terminology
    equipment_keywords = [
        'what is a', 'what is the', 'what does', 'what do',
        'called when', 'term for', 'diameter', 'distance',
        'thickness', 'height of', 'width of', 'use to',
        'what are the', 'represent', 'surface', 'line'
    ]
    # Check for specific equipment/terminology patterns
    if any(keyword in full_text for keyword in equipment_keywords):
        # But exclude if it's about records or players
        if not any(word in full_text for word in ['who holds', 'which player', 'most career', 'record for']):
            return "Equipment & Terminology"

    # Rules & Gameplay
    rules_keywords = [
        'how many', 'how long', 'worth in', 'points is',
        'fouls', 'foul out', 'periods', 'halves',
        'shot clock', 'advance', 'regulation', 'position',
        'substitutions', 'stoppage time', 'power play', 'icing',
        'sack', 'double-double'
    ]
    if any(keyword in full_text for keyword in rules_keywords):
        return "Rules & Gameplay"

    # Default to Trivia & Facts
    return "Trivia & Facts"


def main():
    # Read the draft sports file
    with open('/home/user/fiztrivia/Fiz/Resources/Expansion Packs/draft_sports.json', 'r') as f:
        data = json.load(f)

    # Categorize each question
    categorized_count = {
        "Rules & Gameplay": 0,
        "Players & Teams": 0,
        "Championships & Tournaments": 0,
        "History & Records": 0,
        "Equipment & Terminology": 0,
        "Trivia & Facts": 0
    }

    for question in data['paidQuestions']:
        options_text = " ".join(question['options'])
        subtopic = categorize_sports_question(
            question['question'],
            options_text,
            question['correct_answer']
        )
        question['subtopic'] = subtopic
        categorized_count[subtopic] += 1

    # Save the updated file
    with open('/home/user/fiztrivia/Fiz/Resources/Expansion Packs/draft_sports.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("✅ Successfully categorized 80 sports questions!")
    print("\nDistribution across subtopics:")
    for subtopic, count in categorized_count.items():
        print(f"  {subtopic}: {count}")
    print(f"\nTotal: {sum(categorized_count.values())}")


if __name__ == '__main__':
    main()
