#!/usr/bin/env python3
"""
Analyze Pokémon questions to determine if they're more game or entertainment focused
"""

import json

def analyze_pokemon_questions():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    entertainment = data['categories']['Entertainment']

    pokemon_questions = [q for q in entertainment if q.get('subcategory') == 'Pokémon']

    print(f"Total Pokémon questions: {len(pokemon_questions)}\n")
    print("=" * 80)

    # Sample different difficulty levels
    for difficulty in ['easy', 'medium', 'hard']:
        diff_questions = [q for q in pokemon_questions if q['difficulty'] == difficulty]
        print(f"\n{difficulty.upper()} Questions ({len(diff_questions)} total):")
        print("-" * 80)

        # Show first 5 of each difficulty
        for i, q in enumerate(diff_questions[:5], 1):
            print(f"{i}. [{q['id']}] {q['question']}")

    # Look for game-specific keywords
    game_keywords = ['game', 'generation', 'region', 'version', 'console', 'release']
    anime_keywords = ['ash', 'episode', 'series', 'show', 'anime', 'episode']

    game_count = 0
    anime_count = 0
    general_count = 0

    for q in pokemon_questions:
        question_lower = q['question'].lower()
        is_game = any(keyword in question_lower for keyword in game_keywords)
        is_anime = any(keyword in question_lower for keyword in anime_keywords)

        if is_game:
            game_count += 1
        elif is_anime:
            anime_count += 1
        else:
            general_count += 1

    print("\n" + "=" * 80)
    print("KEYWORD ANALYSIS:")
    print(f"  Game-specific keywords: {game_count} questions")
    print(f"  Anime-specific keywords: {anime_count} questions")
    print(f"  General (either/both): {general_count} questions")
    print("=" * 80)

if __name__ == "__main__":
    analyze_pokemon_questions()
