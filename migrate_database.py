#!/usr/bin/env python3
"""
Database Migration Script: 7 Categories → 12 Categories + Topics/Subtopics
Migrates questions.json to new structure
"""

import json
import sys
from collections import defaultdict

# Marvel vs DC keywords for superhero classification
MARVEL_KEYWORDS = ['iron man', 'tony stark', 'captain america', 'steve rogers',
                   'thor', 'hulk', 'bruce banner', 'spider-man', 'peter parker',
                   'black widow', 'hawkeye', 'avengers', 'marvel', 'wakanda',
                   'black panther', 'thanos', 'infinity', 'x-men', 'wolverine',
                   'fantastic four', 'doctor strange', 'ant-man', 'guardians',
                   's.h.i.e.l.d', 'shield', 's.w.o.r.d', 'sword', 'jarvis', 'friday',
                   'morgan stark', 'peter quill', 'wanda', 'scarlet witch', 'deadpool',
                   'nova corps', 'galactus', 'daredevil', 'matt murdock', 's.s.r',
                   'bucky barnes', 'winter soldier', 'ned leeds', 'daily bugle',
                   'karen', 'edith', 'stormbreaker', 'mjolnir', 'asgard', 'natasha',
                   'clint barton', 'stephen strange', 'billy and tommy']

DC_KEYWORDS = ['batman', 'bruce wayne', 'superman', 'clark kent', 'wonder woman',
               'diana prince', 'flash', 'barry allen', 'aquaman', 'green lantern',
               'justice league', 'dc comics', 'gotham', 'metropolis', 'krypton',
               'joker', 'lex luthor', 'harley quinn', 'catwoman', 'robin',
               'batmobile', 'batcave', 'alfred', 'daily planet', 'perry white',
               'cyborg', 'victor stone', 'martian manhunter', 'shazam', 'billy batson',
               'hawkman', 'carter hall', 'zatanna', 'constantine', 'john constantine',
               'swamp thing', 'alec holland', 'lobo', 'themyscira', 'atlantis',
               'jor-el', 'lasso of truth', 'yellow lantern', 'jimmy olsen']

# Geography subcategory classification keywords
GEO_US_KEYWORDS = ['united states', 'u.s.', 'usa', 'american', 'state capital']
GEO_BORDER_KEYWORDS = ['continent', 'continents']

def classify_superhero(question):
    """Classify superhero question as Marvel or DC"""
    q_lower = question['question'].lower()
    opts_lower = ' '.join(question['options']).lower()
    ans_lower = question['correct_answer'].lower()
    full_text = f"{q_lower} {opts_lower} {ans_lower}"

    is_marvel_full = any(kw in full_text for kw in MARVEL_KEYWORDS)
    is_dc_full = any(kw in full_text for kw in DC_KEYWORDS)

    # If both or neither, use answer to decide
    if is_marvel_full and is_dc_full:
        is_marvel = any(kw in ans_lower for kw in MARVEL_KEYWORDS)
        is_dc = any(kw in ans_lower for kw in DC_KEYWORDS)
    else:
        is_marvel = is_marvel_full
        is_dc = is_dc_full

    if is_marvel and not is_dc:
        return "Marvel"
    elif is_dc and not is_marvel:
        return "DC"
    else:
        return None  # Should not happen with our keywords

def classify_geography(question):
    """Classify geography question into subcategory"""
    q_lower = question['question'].lower()

    if any(kw in q_lower for kw in GEO_US_KEYWORDS):
        return "U.S. Geography"
    elif any(kw in q_lower for kw in GEO_BORDER_KEYWORDS):
        return "Maps & Borders"
    else:
        return "World Geography"

def migrate_database(input_file, output_file):
    """Main migration function"""

    print("=" * 80)
    print("DATABASE MIGRATION: 7 → 12 Categories + Topics/Subtopics")
    print("=" * 80)

    # Load current database
    print(f"\nLoading {input_file}...")
    with open(input_file, 'r') as f:
        data = json.load(f)

    old_categories = data['categories']
    new_categories = defaultdict(list)

    # Track statistics
    stats = {
        'total_questions': 0,
        'id_changes': 0,
        'topics_assigned': 0,
        'category_migrations': defaultdict(int)
    }

    # ID counters for new categories
    lit_counter = 1
    mus_counter = 1
    tec_counter = 1
    geo_counter = 1
    nat_counter = 1

    print("\nProcessing questions...")

    # ========================================
    # ENTERTAINMENT CATEGORY
    # ========================================
    print("\n[1/7] Processing Entertainment...")
    for q in old_categories['Entertainment']:
        stats['total_questions'] += 1
        old_subcat = q['subcategory']
        old_id = q['id']

        # Harry Potter → Literature
        if old_subcat == 'Harry Potter':
            q['id'] = f"lit_{lit_counter:03d}"
            q['category'] = 'Literature'
            q['subcategory'] = 'Fantasy Literature'
            q['topic'] = 'Harry Potter'
            q['subtopic'] = None
            new_categories['Literature'].append(q)
            stats['id_changes'] += 1
            stats['topics_assigned'] += 1
            stats['category_migrations']['Entertainment → Literature'] += 1
            lit_counter += 1

        # Film Score Composers → Music
        elif old_subcat == 'Film Score Composers':
            q['id'] = f"mus_{mus_counter:03d}"
            q['category'] = 'Music'
            q['subcategory'] = 'Film & TV'
            q['topic'] = None  # NO TOPIC per user instructions
            q['subtopic'] = None
            new_categories['Music'].append(q)
            stats['id_changes'] += 1
            stats['category_migrations']['Entertainment → Music'] += 1
            mus_counter += 1

        # Pokémon → Technology
        elif old_subcat == 'Pokémon':
            q['id'] = f"tec_{tec_counter:03d}"
            q['category'] = 'Technology'
            q['subcategory'] = 'Video Games'
            q['topic'] = 'Pokémon'
            q['subtopic'] = None
            new_categories['Technology'].append(q)
            stats['id_changes'] += 1
            stats['topics_assigned'] += 1
            stats['category_migrations']['Entertainment → Technology'] += 1
            tec_counter += 1

        # Pixar → Animation
        elif old_subcat == 'Pixar':
            q['subcategory'] = 'Animation'
            q['topic'] = 'Pixar'
            q['subtopic'] = None
            new_categories['Entertainment'].append(q)
            stats['topics_assigned'] += 1

        # Star Wars → Sci-Fi/Fantasy
        elif old_subcat == 'Star Wars':
            q['subcategory'] = 'Sci-Fi/Fantasy'
            q['topic'] = 'Star Wars'
            q['subtopic'] = None
            new_categories['Entertainment'].append(q)
            stats['topics_assigned'] += 1

        # Film → Sci-Fi/Fantasy (NO TOPIC)
        elif old_subcat == 'Film':
            q['subcategory'] = 'Sci-Fi/Fantasy'
            q['topic'] = None  # NO TOPIC per user instructions
            q['subtopic'] = None
            new_categories['Entertainment'].append(q)

        # Superheroes → Action/Adventure with Marvel/DC topics
        elif old_subcat == 'Superheroes':
            q['subcategory'] = 'Action/Adventure'
            topic = classify_superhero(q)
            q['topic'] = topic
            q['subtopic'] = None
            new_categories['Entertainment'].append(q)
            if topic:
                stats['topics_assigned'] += 1

        # The Office → Drama/Comedy
        elif old_subcat == 'The Office':
            q['subcategory'] = 'Drama/Comedy'
            q['topic'] = 'The Office'
            q['subtopic'] = None
            new_categories['Entertainment'].append(q)
            stats['topics_assigned'] += 1

        else:
            print(f"WARNING: Unknown Entertainment subcategory: {old_subcat} [{old_id}]")
            q['topic'] = None
            q['subtopic'] = None
            new_categories['Entertainment'].append(q)

    # ========================================
    # EARTH → NATURE + GEOGRAPHY
    # ========================================
    print("[2/7] Processing Earth → Nature + Geography...")
    for q in old_categories['Earth']:
        stats['total_questions'] += 1
        old_subcat = q['subcategory']

        # Geography → Geography category
        if old_subcat == 'Geography':
            q['id'] = f"geo_{geo_counter:03d}"
            q['category'] = 'Geography'
            q['subcategory'] = classify_geography(q)
            q['topic'] = None  # NO TOPIC per user instructions
            q['subtopic'] = None
            new_categories['Geography'].append(q)
            stats['id_changes'] += 1
            stats['category_migrations']['Earth → Geography'] += 1
            geo_counter += 1

        # Everything else → Nature
        else:
            q['id'] = f"nat_{nat_counter:03d}"
            q['category'] = 'Nature'

            # Update subcategory names
            if old_subcat == 'Animals':
                q['subcategory'] = 'Animals & Wildlife'
            elif old_subcat == 'Plants':
                q['subcategory'] = 'Plants & Flowers'
            # Trees and Weather stay the same

            q['topic'] = None  # NO TOPIC per user instructions
            q['subtopic'] = None
            new_categories['Nature'].append(q)
            stats['id_changes'] += 1
            stats['category_migrations']['Earth → Nature'] += 1
            nat_counter += 1

    # ========================================
    # SPORTS - Reorganize subcategories
    # ========================================
    print("[3/7] Processing Sports...")
    sport_mapping = {
        'American Football': ('Team Sports', 'American Football'),
        'Baseball': ('Team Sports', 'Baseball'),
        'Basketball': ('Team Sports', 'Basketball'),
        'Hockey': ('Team Sports', 'Hockey'),
        'Soccer': ('Team Sports', 'Soccer'),
        'Tennis': ('Individual Sports', 'Tennis'),
        'Golf': ('Individual Sports', 'Golf'),
        'Olympics': ('International Competition', 'Olympics')
    }

    for q in old_categories['Sports']:
        stats['total_questions'] += 1
        old_subcat = q['subcategory']

        if old_subcat in sport_mapping:
            new_subcat, topic = sport_mapping[old_subcat]
            q['subcategory'] = new_subcat
            q['topic'] = topic
            q['subtopic'] = None
            stats['topics_assigned'] += 1
        else:
            print(f"WARNING: Unknown Sports subcategory: {old_subcat} [{q['id']}]")
            q['topic'] = None
            q['subtopic'] = None

        new_categories['Sports'].append(q)

    # ========================================
    # SCIENCE - No changes, just add topic/subtopic fields
    # ========================================
    print("[4/7] Processing Science...")
    for q in old_categories['Science']:
        stats['total_questions'] += 1
        q['topic'] = None  # NO TOPIC per user instructions
        q['subtopic'] = None
        new_categories['Science'].append(q)

    # ========================================
    # HISTORY - No changes, just add topic/subtopic fields
    # ========================================
    print("[5/7] Processing History...")
    for q in old_categories['History']:
        stats['total_questions'] += 1
        q['topic'] = None  # NO TOPIC per user instructions
        q['subtopic'] = None
        new_categories['History'].append(q)

    # ========================================
    # BIBLE - No changes, just add topic/subtopic fields
    # ========================================
    print("[6/7] Processing Bible...")
    for q in old_categories['Bible']:
        stats['total_questions'] += 1

        # Rename "Biblical Languages" to "Bible Languages"
        if q['subcategory'] == 'Biblical Languages':
            q['subcategory'] = 'Bible Languages'

        q['topic'] = None  # NO TOPIC per user instructions
        q['subtopic'] = None
        new_categories['Bible'].append(q)

    # ========================================
    # FOOD - No changes, just add topic/subtopic fields
    # ========================================
    print("[7/7] Processing Food...")
    for q in old_categories['Food']:
        stats['total_questions'] += 1
        q['topic'] = None  # NO TOPIC per user instructions
        q['subtopic'] = None
        new_categories['Food'].append(q)

    # ========================================
    # CREATE ART CATEGORY (EMPTY)
    # ========================================
    new_categories['Art'] = []

    # ========================================
    # VALIDATE & SAVE
    # ========================================
    print("\n" + "=" * 80)
    print("VALIDATION")
    print("=" * 80)

    # Sort categories
    category_order = ['Entertainment', 'Literature', 'Music', 'Technology', 'Art',
                      'Geography', 'Sports', 'Science', 'Nature', 'History', 'Bible', 'Food']

    sorted_categories = {cat: new_categories[cat] for cat in category_order}

    # Count questions per category
    print("\nQuestions per category:")
    total_new = 0
    for cat in category_order:
        count = len(sorted_categories[cat])
        total_new += count
        print(f"  {cat:20s} {count:4d} questions")

    print(f"\nTotal questions: {total_new}")
    print(f"Expected: {stats['total_questions']}")

    if total_new != stats['total_questions']:
        print(f"ERROR: Question count mismatch! {total_new} != {stats['total_questions']}")
        sys.exit(1)

    # Check for duplicate IDs
    all_ids = []
    for questions in sorted_categories.values():
        for q in questions:
            all_ids.append(q['id'])

    if len(all_ids) != len(set(all_ids)):
        print("ERROR: Duplicate IDs found!")
        sys.exit(1)

    print(f"\n✓ No duplicate IDs")
    print(f"✓ All {total_new} questions accounted for")

    # Print migration statistics
    print("\n" + "=" * 80)
    print("MIGRATION STATISTICS")
    print("=" * 80)
    print(f"Total questions processed: {stats['total_questions']}")
    print(f"ID changes: {stats['id_changes']}")
    print(f"Topics assigned: {stats['topics_assigned']}")
    print(f"Questions without topics: {stats['total_questions'] - stats['topics_assigned']}")

    print("\nCategory migrations:")
    for migration, count in sorted(stats['category_migrations'].items()):
        print(f"  {migration}: {count} questions")

    # Save new database
    output_data = {'categories': sorted_categories}

    print(f"\n" + "=" * 80)
    print(f"Saving to {output_file}...")
    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print("✓ Migration complete!")
    print("=" * 80)

    return stats

if __name__ == "__main__":
    input_file = "Fiz/Resources/questions.json"
    output_file = "Fiz/Resources/questions.json"

    # Confirm before overwriting
    print("\nWARNING: This will overwrite questions.json")
    print("A backup should already exist: questions_backup_20251228_211602.json")
    response = input("\nProceed with migration? (yes/no): ")

    if response.lower() != 'yes':
        print("Migration cancelled.")
        sys.exit(0)

    stats = migrate_database(input_file, output_file)
