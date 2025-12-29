#!/usr/bin/env python3
"""
Move topic questions to expansion packs
Keep 10 questions per non-sports topic, 20 per sports topic in base game
"""

import json
import random
from collections import defaultdict

# Set seed for reproducibility
random.seed(42)

def select_questions_to_keep(questions, count):
    """
    Select questions to keep in base game, aiming for difficulty variety
    """
    # Group by difficulty
    by_difficulty = defaultdict(list)
    for q in questions:
        by_difficulty[q['difficulty']].append(q)

    kept = []

    # Try to get a mix: ~40% easy, ~30% medium, ~30% hard
    target_easy = int(count * 0.4)
    target_medium = int(count * 0.3)
    target_hard = count - target_easy - target_medium

    # Shuffle each difficulty group
    for diff in by_difficulty:
        random.shuffle(by_difficulty[diff])

    # Take from each difficulty
    kept.extend(by_difficulty['easy'][:target_easy])
    kept.extend(by_difficulty['medium'][:target_medium])
    kept.extend(by_difficulty['hard'][:target_hard])

    # If we don't have enough, take more from whatever is available
    while len(kept) < count:
        for diff in ['easy', 'medium', 'hard']:
            if len(by_difficulty[diff]) > 0:
                # Find questions we haven't taken yet
                for q in by_difficulty[diff]:
                    if q not in kept:
                        kept.append(q)
                        if len(kept) >= count:
                            break
            if len(kept) >= count:
                break

    return kept[:count]

def move_to_expansions():
    """Main migration function"""

    print("=" * 80)
    print("MOVING QUESTIONS TO EXPANSION PACKS")
    print("=" * 80)

    # Load current database
    print("\nLoading questions.json...")
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    categories = data['categories']

    # Initialize expansion packs structure
    expansion_packs = {}

    # Track stats
    stats = {
        'total_moved': 0,
        'by_pack': {}
    }

    # Category ID counters for expansion questions
    expansion_counters = {
        'Entertainment': 301,
        'Literature': 301,
        'Technology': 301,
        'Sports': 301
    }

    # ========================================
    # ENTERTAINMENT
    # ========================================
    print("\n[1/4] Processing Entertainment topics...")
    ent_topics = {
        'Pixar': 10,
        'Star Wars': 10,
        'Marvel': 10,
        'DC': 10,
        'The Office': 10
    }

    for topic_name, keep_count in ent_topics.items():
        # Get all questions for this topic
        topic_questions = [q for q in categories['Entertainment'] if q.get('topic') == topic_name]

        print(f"  {topic_name}: {len(topic_questions)} total, keeping {keep_count}")

        if len(topic_questions) > keep_count:
            # Select questions to keep
            kept = select_questions_to_keep(topic_questions, keep_count)
            kept_ids = set(q['id'] for q in kept)

            # Questions to move
            to_move = [q for q in topic_questions if q['id'] not in kept_ids]

            # Create expansion pack
            expansion_pack_name = topic_name.lower().replace(' ', '_')
            expansion_packs[expansion_pack_name] = []

            # Renumber expansion questions
            for q in to_move:
                new_q = q.copy()
                new_q['id'] = f"ent_{expansion_counters['Entertainment']:03d}"
                expansion_counters['Entertainment'] += 1
                expansion_packs[expansion_pack_name].append(new_q)

            # Update base game (remove moved questions)
            categories['Entertainment'] = [
                q for q in categories['Entertainment']
                if not (q.get('topic') == topic_name and q['id'] not in kept_ids)
            ]

            stats['total_moved'] += len(to_move)
            stats['by_pack'][expansion_pack_name] = len(to_move)
            print(f"    Moved {len(to_move)} to expansion ({expansion_pack_name})")

    # ========================================
    # LITERATURE
    # ========================================
    print("\n[2/4] Processing Literature topics...")
    lit_questions = categories['Literature']
    harry_potter = [q for q in lit_questions if q.get('topic') == 'Harry Potter']

    print(f"  Harry Potter: {len(harry_potter)} total, keeping 10")

    if len(harry_potter) > 10:
        kept = select_questions_to_keep(harry_potter, 10)
        kept_ids = set(q['id'] for q in kept)
        to_move = [q for q in harry_potter if q['id'] not in kept_ids]

        # Create expansion pack
        expansion_packs['harry_potter'] = []
        for q in to_move:
            new_q = q.copy()
            new_q['id'] = f"lit_{expansion_counters['Literature']:03d}"
            expansion_counters['Literature'] += 1
            expansion_packs['harry_potter'].append(new_q)

        # Update base game
        categories['Literature'] = [q for q in lit_questions if q['id'] in kept_ids]

        stats['total_moved'] += len(to_move)
        stats['by_pack']['harry_potter'] = len(to_move)
        print(f"    Moved {len(to_move)} to expansion (harry_potter)")

    # ========================================
    # TECHNOLOGY
    # ========================================
    print("\n[3/4] Processing Technology topics...")
    tech_questions = categories['Technology']
    pokemon = [q for q in tech_questions if q.get('topic') == 'Pokémon']

    print(f"  Pokémon: {len(pokemon)} total, keeping 10")

    if len(pokemon) > 10:
        kept = select_questions_to_keep(pokemon, 10)
        kept_ids = set(q['id'] for q in kept)
        to_move = [q for q in pokemon if q['id'] not in kept_ids]

        # Create expansion pack
        expansion_packs['pokemon'] = []
        for q in to_move:
            new_q = q.copy()
            new_q['id'] = f"tec_{expansion_counters['Technology']:03d}"
            expansion_counters['Technology'] += 1
            expansion_packs['pokemon'].append(new_q)

        # Update base game
        categories['Technology'] = [q for q in tech_questions if q['id'] in kept_ids]

        stats['total_moved'] += len(to_move)
        stats['by_pack']['pokemon'] = len(to_move)
        print(f"    Moved {len(to_move)} to expansion (pokemon)")

    # ========================================
    # SPORTS
    # ========================================
    print("\n[4/4] Processing Sports topics...")
    sports_topics = {
        'American Football': 20,
        'Baseball': 20,
        'Basketball': 20,
        'Golf': 20,
        'Hockey': 20,
        'Olympics': 20,
        'Soccer': 20,
        'Tennis': 20
    }

    expansion_packs['sports'] = {}

    for topic_name, keep_count in sports_topics.items():
        topic_questions = [q for q in categories['Sports'] if q.get('topic') == topic_name]

        print(f"  {topic_name}: {len(topic_questions)} total, keeping {keep_count}")

        if len(topic_questions) > keep_count:
            kept = select_questions_to_keep(topic_questions, keep_count)
            kept_ids = set(q['id'] for q in kept)
            to_move = [q for q in topic_questions if q['id'] not in kept_ids]

            # Create sport-specific expansion
            sport_key = topic_name.lower().replace(' ', '_')
            expansion_packs['sports'][sport_key] = []

            for q in to_move:
                new_q = q.copy()
                new_q['id'] = f"spt_{expansion_counters['Sports']:03d}"
                expansion_counters['Sports'] += 1
                expansion_packs['sports'][sport_key].append(new_q)

            # Update base game
            categories['Sports'] = [
                q for q in categories['Sports']
                if not (q.get('topic') == topic_name and q['id'] not in kept_ids)
            ]

            moved_count = len(to_move)
            stats['total_moved'] += moved_count
            if 'sports' not in stats['by_pack']:
                stats['by_pack']['sports'] = 0
            stats['by_pack']['sports'] += moved_count
            print(f"    Moved {moved_count} to expansion (sports/{sport_key})")
        elif len(topic_questions) == keep_count:
            print(f"    Already at target, keeping all {keep_count}")
        else:
            print(f"    Only {len(topic_questions)} available, keeping all")

    # ========================================
    # SAVE FILES
    # ========================================
    print("\n" + "=" * 80)
    print("SAVING FILES")
    print("=" * 80)

    # Save updated base game
    output_data = {'categories': categories}
    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    print("✓ Saved questions.json (base game)")

    # Save expansion packs
    expansion_data = {'expansion_packs': expansion_packs}
    with open('Fiz/Resources/questions_expansions.json', 'w') as f:
        json.dump(expansion_data, f, indent=2, ensure_ascii=False)
    print("✓ Saved questions_expansions.json")

    # ========================================
    # STATISTICS
    # ========================================
    print("\n" + "=" * 80)
    print("MIGRATION STATISTICS")
    print("=" * 80)

    base_game_total = sum(len(qs) for qs in categories.values())

    print(f"\nBase game questions: {base_game_total}")
    print(f"Expansion questions: {stats['total_moved']}")
    print(f"Total preserved: {base_game_total + stats['total_moved']}")

    print("\nQuestions per category (base game):")
    for cat_name in sorted(categories.keys()):
        count = len(categories[cat_name])
        print(f"  {cat_name:20s} {count:4d} questions")

    print("\nExpansion packs created:")
    for pack_name, count in sorted(stats['by_pack'].items()):
        print(f"  {pack_name:30s} {count:3d} questions")

    print("\n" + "=" * 80)
    print("✓ Migration complete!")
    print("=" * 80)

    return stats

if __name__ == "__main__":
    stats = move_to_expansions()
