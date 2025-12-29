#!/usr/bin/env python3
"""
Analyze History category balance across subcategories and difficulties
"""

import json
from collections import defaultdict

def analyze_history():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    history_questions = data['categories']['History']

    print("=" * 80)
    print("HISTORY CATEGORY ANALYSIS")
    print("=" * 80)
    print(f"\nTotal History Questions: {len(history_questions)}")
    print(f"Target: 300 questions")
    print(f"Need to add: {300 - len(history_questions)} questions")

    # Analyze by subcategory
    by_subcat = defaultdict(list)
    for q in history_questions:
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
    for q in history_questions:
        all_diff_counts[q['difficulty']] += 1

    total = len(history_questions)
    print(f"\nTotal: {total} questions")
    print(f"Easy:   {all_diff_counts['easy']:3d} ({all_diff_counts['easy']/total*100:.1f}%)")
    print(f"Medium: {all_diff_counts['medium']:3d} ({all_diff_counts['medium']/total*100:.1f}%)")
    print(f"Hard:   {all_diff_counts['hard']:3d} ({all_diff_counts['hard']/total*100:.1f}%)")

    # Calculate ideal distribution for 300 questions
    print("\n" + "=" * 80)
    print("RECOMMENDED ADDITIONS TO REACH 300")
    print("=" * 80)

    target_total = 300
    need_to_add = target_total - total

    # Target: ~33% easy, ~40% medium, ~27% hard
    target_easy = int(target_total * 0.33)
    target_medium = int(target_total * 0.40)
    target_hard = target_total - target_easy - target_medium

    need_easy = max(0, target_easy - all_diff_counts['easy'])
    need_medium = max(0, target_medium - all_diff_counts['medium'])
    need_hard = max(0, target_hard - all_diff_counts['hard'])

    print(f"\nTo reach 300 with balanced difficulty:")
    print(f"  Target Easy:   {target_easy} (currently {all_diff_counts['easy']}) → Need +{need_easy}")
    print(f"  Target Medium: {target_medium} (currently {all_diff_counts['medium']}) → Need +{need_medium}")
    print(f"  Target Hard:   {target_hard} (currently {all_diff_counts['hard']}) → Need +{need_hard}")

    # Calculate per-subcategory recommendations
    print("\n" + "=" * 80)
    print("SUBCATEGORY BALANCE RECOMMENDATIONS")
    print("=" * 80)

    # Ideal: 75 questions per subcategory (300 / 4 = 75)
    target_per_subcat = 75

    print(f"\nTarget per subcategory: {target_per_subcat} questions")
    print()

    for stats in sorted(subcat_stats, key=lambda x: x['total']):
        current = stats['total']
        need = target_per_subcat - current

        if need > 0:
            current_easy_pct = stats['easy'] / current if current > 0 else 0.33
            current_medium_pct = stats['medium'] / current if current > 0 else 0.40
            current_hard_pct = stats['hard'] / current if current > 0 else 0.27

            add_easy = int(need * current_easy_pct)
            add_medium = int(need * current_medium_pct)
            add_hard = need - add_easy - add_medium

            print(f"{stats['name']:20s} {current:3d} → {target_per_subcat:3d} (need +{need})")
            print(f"  Add: {add_easy} easy, {add_medium} medium, {add_hard} hard")
        else:
            print(f"{stats['name']:20s} {current:3d} → Already at/above target")

    print("\n" + "=" * 80)

if __name__ == "__main__":
    analyze_history()
