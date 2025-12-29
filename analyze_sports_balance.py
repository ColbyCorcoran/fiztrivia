#!/usr/bin/env python3
"""
Analyze Sports category balance across subcategories and difficulties
"""

import json
from collections import defaultdict

def analyze_sports():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    sports_questions = data['categories']['Sports']

    print("=" * 80)
    print("SPORTS CATEGORY ANALYSIS")
    print("=" * 80)
    print(f"\nTotal Sports Questions: {len(sports_questions)}")
    print(f"Target: 300 questions")
    print(f"Need to add: {300 - len(sports_questions)} questions")

    # Analyze by subcategory
    by_subcat = defaultdict(list)
    for q in sports_questions:
        by_subcat[q['subcategory']].append(q)

    print("\n" + "=" * 80)
    print("SUBCATEGORY BREAKDOWN")
    print("=" * 80)

    subcat_stats = []
    for subcat in sorted(by_subcat.keys()):
        questions = by_subcat[subcat]

        # Difficulty counts
        diff_counts = defaultdict(int)
        for q in questions:
            diff_counts[q['difficulty']] += 1

        stats = {
            'name': subcat,
            'total': len(questions),
            'easy': diff_counts['easy'],
            'medium': diff_counts['medium'],
            'hard': diff_counts['hard']
        }
        subcat_stats.append(stats)

        print(f"\n{subcat}: {len(questions)} questions")
        print(f"  Easy:   {diff_counts['easy']:3d} ({diff_counts['easy']/len(questions)*100:.1f}%)")
        print(f"  Medium: {diff_counts['medium']:3d} ({diff_counts['medium']/len(questions)*100:.1f}%)")
        print(f"  Hard:   {diff_counts['hard']:3d} ({diff_counts['hard']/len(questions)*100:.1f}%)")

    # Overall difficulty distribution
    print("\n" + "=" * 80)
    print("OVERALL DIFFICULTY DISTRIBUTION")
    print("=" * 80)

    all_diff_counts = defaultdict(int)
    for q in sports_questions:
        all_diff_counts[q['difficulty']] += 1

    total = len(sports_questions)
    print(f"\nTotal: {total} questions")
    print(f"Easy:   {all_diff_counts['easy']:3d} ({all_diff_counts['easy']/total*100:.1f}%)")
    print(f"Medium: {all_diff_counts['medium']:3d} ({all_diff_counts['medium']/total*100:.1f}%)")
    print(f"Hard:   {all_diff_counts['hard']:3d} ({all_diff_counts['hard']/total*100:.1f}%)")

    # Calculate recommended distribution for 300 questions
    print("\n" + "=" * 80)
    print("RECOMMENDED DISTRIBUTION TO REACH 300")
    print("=" * 80)

    target_total = 300
    need_to_add = target_total - total

    # Proposed subcategory targets (based on natural sports coverage)
    # Team Sports is largest (football, basketball, baseball, soccer, hockey, etc.)
    # Individual Sports (tennis, golf, boxing, track & field, swimming, etc.)
    # International Competition (Olympics, World Cup, etc.)

    targets = {
        'Team Sports': 150,  # 100 → 150 (+50)
        'Individual Sports': 100,  # 40 → 100 (+60)
        'International Competition': 50  # 20 → 50 (+30)
    }

    print(f"\nProposed subcategory distribution for 300 total:")
    total_to_add = 0
    for subcat, target in targets.items():
        current = next(s['total'] for s in subcat_stats if s['name'] == subcat)
        need = target - current
        total_to_add += need
        print(f"  {subcat:30s} {current:3d} → {target:3d} (+{need})")

    print(f"\nTotal to add: {total_to_add} questions")

    # Difficulty targets for new questions (emphasize medium/hard)
    target_easy_pct = 0.30  # 30% easy
    target_medium_pct = 0.40  # 40% medium
    target_hard_pct = 0.30  # 30% hard

    print("\n" + "=" * 80)
    print("RECOMMENDED DIFFICULTY DISTRIBUTION FOR NEW QUESTIONS")
    print("=" * 80)

    for subcat, target in targets.items():
        current = next(s['total'] for s in subcat_stats if s['name'] == subcat)
        need = target - current

        if need > 0:
            add_easy = int(need * target_easy_pct)
            add_medium = int(need * target_medium_pct)
            add_hard = need - add_easy - add_medium

            print(f"\n{subcat} (+{need} total):")
            print(f"  Easy:   {add_easy}")
            print(f"  Medium: {add_medium}")
            print(f"  Hard:   {add_hard}")

    print("\n" + "=" * 80)

if __name__ == "__main__":
    analyze_sports()
