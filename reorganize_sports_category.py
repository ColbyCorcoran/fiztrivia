#!/usr/bin/env python3
"""
Reorganize Sports category:
1. Reduce Team Sports from 152 to 50 (move 102 to expansion)
2. Reduce Individual Sports from 99 to 50 (move 49 to expansion)
3. Add topic tags to sport-specific questions
4. Keep International Competition at 49 (will add 1 more manually)
"""
import json

def identify_sport_topic(question_text, options_text, answer_text):
    """Identify which sport a question is about based on keywords"""
    combined = f"{question_text} {options_text} {answer_text}".lower()

    # Team sports (priority order for Team Sports subcategory)
    if any(word in combined for word in ['soccer', 'goal keeper', 'penalty kick', 'world cup', 'fifa', 'pitch ']):
        return 'Soccer'
    if any(word in combined for word in ['touchdown', 'quarterback', 'nfl', 'super bowl', 'gridiron', 'linebacker', 'fumble', 'field goal', 'down ', 'yards', 'american football']):
        return 'Football'
    if any(word in combined for word in ['basketball', 'nba', 'dunk', 'layup', 'three-point', 'rebound', 'hoop', 'court ']):
        return 'Basketball'
    if any(word in combined for word in ['baseball', 'mlb', 'pitcher', 'batter', 'home run', 'inning', 'strike', 'bases', 'diamond', 'catcher']):
        return 'Baseball'
    if any(word in combined for word in ['hockey', 'nhl', 'puck', 'ice rink', 'goalie mask', 'zamboni', 'stanley cup', 'hat trick']):
        return 'Hockey'
    if any(word in combined for word in ['volleyball', 'spike', 'volleyball']):
        return 'Volleyball'
    if any(word in combined for word in ['rugby', 'scrum', 'try line']):
        return 'Rugby'
    if any(word in combined for word in ['cricket', 'wicket', 'bowler', 'batsman']):
        return 'Cricket'

    # Individual sports (priority order for Individual Sports subcategory)
    if any(word in combined for word in ['tennis', 'wimbledon', 'grand slam', 'ace', 'deuce', 'love', 'racket']):
        return 'Tennis'
    if any(word in combined for word in ['golf', 'birdie', 'bogey', 'par', 'hole', 'tee', 'putt', 'fairway', 'green', 'masters', 'pga']):
        return 'Golf'
    if any(word in combined for word in ['swimming', 'freestyle', 'butterfly', 'backstroke', 'pool', 'lap', 'swimmer']):
        return 'Swimming'
    if any(word in combined for word in ['boxing', 'knockout', 'ring', 'round', 'punch', 'heavyweight', 'boxer']):
        return 'Boxing'
    if any(word in combined for word in ['track', 'sprint', 'relay', 'hurdles', 'marathon', 'meter dash', '100-meter', '200-meter']):
        return 'Track & Field'
    if any(word in combined for word in ['gymnastics', 'vault', 'beam', 'floor exercise', 'parallel bars']):
        return 'Gymnastics'
    if any(word in combined for word in ['wrestling', 'pin', 'takedown', 'mat ']):
        return 'Wrestling'

    return None

def main():
    # Load questions
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    sports = data['categories']['Sports']

    # Separate by subcategory
    team_sports = [q for q in sports if q.get('subcategory') == 'Team Sports']
    individual_sports = [q for q in sports if q.get('subcategory') == 'Individual Sports']
    intl_competition = [q for q in sports if q.get('subcategory') == 'International Competition']

    print(f"Original counts:")
    print(f"  Team Sports: {len(team_sports)}")
    print(f"  Individual Sports: {len(individual_sports)}")
    print(f"  International Competition: {len(intl_competition)}")
    print()

    # Process Team Sports - keep 50, prioritize sport-specific
    team_sports_tagged = []
    for q in team_sports:
        options_text = ' '.join(q['options'])
        topic = identify_sport_topic(q['question'], options_text, q['correct_answer'])
        if topic:
            q['topic'] = topic
        team_sports_tagged.append((q, topic))

    # Sort: sport-specific first, then general
    team_sports_tagged.sort(key=lambda x: (x[1] is None, x[0]['id']))

    # Keep first 50
    team_sports_keep = [q for q, _ in team_sports_tagged[:50]]
    team_sports_expansion = [q for q, _ in team_sports_tagged[50:]]

    print(f"Team Sports:")
    print(f"  Keeping: {len(team_sports_keep)}")
    print(f"  Moving to expansion: {len(team_sports_expansion)}")

    # Count topics in kept questions
    topics_kept = {}
    for q in team_sports_keep:
        topic = q.get('topic', 'General')
        topics_kept[topic] = topics_kept.get(topic, 0) + 1
    print(f"  Topics kept: {dict(sorted(topics_kept.items()))}")
    print()

    # Process Individual Sports - keep 50, prioritize sport-specific
    individual_sports_tagged = []
    for q in individual_sports:
        options_text = ' '.join(q['options'])
        topic = identify_sport_topic(q['question'], options_text, q['correct_answer'])
        if topic:
            q['topic'] = topic
        individual_sports_tagged.append((q, topic))

    # Sort: sport-specific first, then general
    individual_sports_tagged.sort(key=lambda x: (x[1] is None, x[0]['id']))

    # Keep first 50
    individual_sports_keep = [q for q, _ in individual_sports_tagged[:50]]
    individual_sports_expansion = [q for q, _ in individual_sports_tagged[50:]]

    print(f"Individual Sports:")
    print(f"  Keeping: {len(individual_sports_keep)}")
    print(f"  Moving to expansion: {len(individual_sports_expansion)}")

    # Count topics in kept questions
    topics_kept = {}
    for q in individual_sports_keep:
        topic = q.get('topic', 'General')
        topics_kept[topic] = topics_kept.get(topic, 0) + 1
    print(f"  Topics kept: {dict(sorted(topics_kept.items()))}")
    print()

    # Update main questions file
    new_sports = team_sports_keep + individual_sports_keep + intl_competition
    new_sports.sort(key=lambda q: int(q['id'].split('_')[1]))

    data['categories']['Sports'] = new_sports

    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Updated main questions file")
    print(f"   New Sports total: {len(new_sports)} questions")
    print(f"   Team Sports: {len(team_sports_keep)}")
    print(f"   Individual Sports: {len(individual_sports_keep)}")
    print(f"   International Competition: {len(intl_competition)}")

    # Create expansion pack file
    expansion_pack = {
        "Team Sports": team_sports_expansion,
        "Individual Sports": individual_sports_expansion
    }

    with open('Fiz/Resources/sports_expansion_pack.json', 'w') as f:
        json.dump(expansion_pack, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Created expansion pack file")
    print(f"   Team Sports expansion: {len(team_sports_expansion)} questions")
    print(f"   Individual Sports expansion: {len(individual_sports_expansion)} questions")
    print(f"   Total in expansion: {len(team_sports_expansion) + len(individual_sports_expansion)} questions")

if __name__ == "__main__":
    main()
