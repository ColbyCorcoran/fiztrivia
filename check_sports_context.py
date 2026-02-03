#!/usr/bin/env python3
"""
Check sports questions for proper context.
Flag questions that may need sport context added or have redundant context.
"""

import json
import re

def get_sport_from_question(question_text, options_text=""):
    """
    Try to identify which sport a question is about based on keywords.
    Returns the sport name if clearly identified, None otherwise.
    """
    text = (question_text + " " + options_text).lower()

    # Sport-specific keywords that make the sport obvious
    sport_keywords = {
        'basketball': ['basketball', 'nba', 'hoop', 'dunk', 'layup', 'rebound', 'alley-oop', 'slam dunk'],
        'football': ['football', 'nfl', 'super bowl', 'touchdown', 'quarterback', 'linebacker', 'end zone'],
        'baseball': ['baseball', 'mlb', 'world series', 'pitcher', 'batter', 'home run', 'strike', 'innings', 'diamond', 'bases'],
        'soccer': ['soccer', 'fifa', 'world cup', 'goalkeeper', 'penalty kick', 'offside', 'stoppage time'],
        'hockey': ['hockey', 'nhl', 'stanley cup', 'puck', 'ice rink', 'goaltender', 'face-off', 'icing', 'power play'],
        'tennis': ['tennis', 'grand slam', 'wimbledon', 'us open', 'french open', 'australian open', 'racket', 'serve', 'deuce', 'love'],
        'golf': ['golf', 'pga', 'masters', 'birdie', 'eagle', 'bogey', 'albatross', 'tee shot', 'fairway', 'green', 'putter'],
        'boxing': ['boxing', 'heavyweight', 'knockout', 'uppercut', 'jab', 'ring'],
        'swimming': ['swimming', 'freestyle', 'backstroke', 'breaststroke', 'butterfly', 'pool', 'lane'],
        'gymnastics': ['gymnastics', 'vault', 'beam', 'uneven bars', 'floor exercise', 'pommel horse'],
        'cricket': ['cricket', 'wicket', 'bowler', 'batsman', 'over', 'test match'],
        'volleyball': ['volleyball', 'spike', 'set', 'dig', 'net'],
        'rugby': ['rugby', 'scrum', 'try', 'conversion', 'lineout'],
        'mma': ['mma', 'ufc', 'octagon', 'submission', 'tapout'],
        'f1': ['formula 1', 'formula one', 'f1', 'grand prix', 'pole position', 'pit stop'],
        'nascar': ['nascar', 'daytona', 'stock car'],
        'olympics': ['olympics', 'olympic', 'gold medal', 'silver medal', 'bronze medal']
    }

    for sport, keywords in sport_keywords.items():
        if any(keyword in text for keyword in keywords):
            return sport

    return None

def needs_context(question_text, options_text, correct_answer):
    """
    Determine if a question needs sport context added.
    Returns (needs_context: bool, reason: str, suggested_sport: str)
    """
    text = question_text.lower()
    full_text = (question_text + " " + options_text + " " + correct_answer).lower()

    # Check if sport is already identified in the question
    identified_sport = get_sport_from_question(question_text, options_text)

    if identified_sport:
        return (False, f"Sport clearly identified: {identified_sport}", identified_sport)

    # Generic terms that could apply to multiple sports and need context
    ambiguous_patterns = [
        (r'^what is (it called|the term)', 'Generic "what is" question'),
        (r'^how many (points|players|fouls)', 'Generic counting question'),
        (r'^what does \w+ stand for', 'Acronym question'),
        (r'(score|scoring|point)', 'Scoring question'),
        (r'^which (player|team|country)', 'Generic player/team question'),
        (r'(championship|tournament|cup|trophy)', 'Generic championship question'),
        (r'(regulation|standard|official)', 'Rules question'),
        (r'(surface|court|field|rink)', 'Playing surface question'),
    ]

    for pattern, reason in ambiguous_patterns:
        if re.search(pattern, text):
            # This might need context
            # But check if there are any sport-specific terms in options or answer
            if not get_sport_from_question(full_text):
                return (True, reason, None)

    return (False, "Question appears clear", None)

def has_redundant_context(question_text):
    """
    Check if question has redundant sport context.
    E.g., "In basketball, how many players are on a basketball court?"
    """
    text = question_text.lower()

    # Check for "In [sport], ..." at the beginning
    sport_prefix = re.match(r'^in (basketball|football|baseball|soccer|tennis|golf|hockey|swimming|cricket|rugby|volleyball|boxing|mma|formula 1|nascar)', text)
    if sport_prefix:
        sport = sport_prefix.group(1)
        # Check if the sport is mentioned again later in the question
        rest_of_question = text[sport_prefix.end():]
        if sport in rest_of_question or get_sport_from_question(rest_of_question):
            return (True, f"Sport '{sport}' mentioned in prefix and again in question")

    return (False, "")

def main():
    # Read the draft sports file
    with open('/home/user/fiztrivia/Fiz/Resources/Expansion Packs/draft_sports.json', 'r') as f:
        data = json.load(f)

    all_questions = data['freePreviewQuestions'] + data['paidQuestions']

    needs_context_list = []
    redundant_context_list = []

    print("Analyzing 500 sports questions for context issues...\n")

    for q in all_questions:
        question_id = q['id']
        question_text = q['question']
        options_text = " ".join(q['options'])
        correct_answer = q['correct_answer']

        # Check if needs context
        needs, reason, sport = needs_context(question_text, options_text, correct_answer)
        if needs:
            needs_context_list.append({
                'id': question_id,
                'question': question_text,
                'reason': reason,
                'options': q['options'],
                'answer': correct_answer,
                'subcategory': q['subcategory']
            })

        # Check for redundant context
        redundant, redundant_reason = has_redundant_context(question_text)
        if redundant:
            redundant_context_list.append({
                'id': question_id,
                'question': question_text,
                'reason': redundant_reason
            })

    print(f"=" * 80)
    print(f"CONTEXT ANALYSIS RESULTS")
    print(f"=" * 80)
    print(f"\nTotal questions analyzed: {len(all_questions)}")
    print(f"Questions that MAY NEED context: {len(needs_context_list)}")
    print(f"Questions with REDUNDANT context: {len(redundant_context_list)}")

    if needs_context_list:
        print(f"\n{'=' * 80}")
        print(f"QUESTIONS THAT MAY NEED SPORT CONTEXT:")
        print(f"{'=' * 80}\n")

        for item in needs_context_list[:50]:  # Show first 50
            print(f"ID: {item['id']}")
            print(f"Subcategory: {item['subcategory']}")
            print(f"Question: {item['question']}")
            print(f"Options: {', '.join(item['options'])}")
            print(f"Answer: {item['answer']}")
            print(f"Reason: {item['reason']}")
            print(f"-" * 80)

        if len(needs_context_list) > 50:
            print(f"\n... and {len(needs_context_list) - 50} more")

    if redundant_context_list:
        print(f"\n{'=' * 80}")
        print(f"QUESTIONS WITH REDUNDANT CONTEXT:")
        print(f"{'=' * 80}\n")

        for item in redundant_context_list:
            print(f"ID: {item['id']}")
            print(f"Question: {item['question']}")
            print(f"Reason: {item['reason']}")
            print(f"-" * 80)

    # Save detailed report to file
    report = {
        'total_questions': len(all_questions),
        'needs_context_count': len(needs_context_list),
        'redundant_context_count': len(redundant_context_list),
        'needs_context': needs_context_list,
        'redundant_context': redundant_context_list
    }

    with open('/home/user/fiztrivia/sports_context_report.json', 'w') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"\n{'=' * 80}")
    print(f"Full report saved to: sports_context_report.json")
    print(f"{'=' * 80}")

if __name__ == '__main__':
    main()
