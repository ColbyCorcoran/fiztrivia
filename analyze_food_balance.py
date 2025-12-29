#!/usr/bin/env python3
"""
Analyze Food category balance across subcategories and difficulties
"""

import json
from collections import defaultdict

def analyze_food():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    food_questions = data['categories']['Food']

    print("=" * 80)
    print("FOOD CATEGORY ANALYSIS")
    print("=" * 80)
    print(f"\nTotal Food Questions: {len(food_questions)}")
    print(f"Target: 300 questions")
    print(f"Need to add: {300 - len(food_questions)} questions")

    # Analyze by subcategory
    by_subcat = defaultdict(list)
    for q in food_questions:
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
    for q in food_questions:
        all_diff_counts[q['difficulty']] += 1

    total = len(food_questions)
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

    # Ideal: 30 questions per subcategory (300 / 10 = 30)
    target_per_subcat = 30

    print(f"\nTarget per subcategory: {target_per_subcat} questions")
    print()

    for stats in sorted(subcat_stats, key=lambda x: x['total']):
        current = stats['total']
        need = target_per_subcat - current

        if need > 0:
            # Calculate difficulty distribution for this subcategory
            # Maintain similar ratios
            current_easy_pct = stats['easy'] / current if current > 0 else 0.33
            current_medium_pct = stats['medium'] / current if current > 0 else 0.40
            current_hard_pct = stats['hard'] / current if current > 0 else 0.27

            # Round to maintain current distribution
            add_easy = int(need * current_easy_pct)
            add_medium = int(need * current_medium_pct)
            add_hard = need - add_easy - add_medium

            print(f"{stats['name']:25s} {current:3d} → {target_per_subcat:3d} (need +{need})")
            print(f"  Add: {add_easy} easy, {add_medium} medium, {add_hard} hard")
        else:
            print(f"{stats['name']:25s} {current:3d} → Already at/above target")

    print("\n" + "=" * 80)
    print("SAMPLE QUESTION TYPES TO ADD")
    print("=" * 80)

    suggestions = {
        'Baking': [
            'Bread types and techniques',
            'Pastry and dough methods',
            'Cake decorating',
            'Cookie varieties'
        ],
        'Beverages': [
            'Coffee and tea varieties',
            'Wine and spirits',
            'Soft drinks history',
            'Cocktail recipes'
        ],
        'Cooking Techniques': [
            'Knife skills',
            'Cooking methods (sauté, braise, etc.)',
            'Food preparation',
            'Kitchen equipment'
        ],
        'Cuisines': [
            'Regional specialties',
            'National dishes',
            'Cultural food traditions',
            'Cooking styles'
        ],
        'Desserts': [
            'Classic desserts',
            'International sweets',
            'Frozen desserts',
            'Candy and confections'
        ],
        'Dishes': [
            'Main courses',
            'Side dishes',
            'Breakfast foods',
            'Appetizers'
        ],
        'Famous Chefs/Restaurants': [
            'Celebrity chefs',
            'Michelin-starred restaurants',
            'Culinary pioneers',
            'Food TV personalities'
        ],
        'Food History': [
            'Food origins',
            'Culinary innovations',
            'Historical dishes',
            'Food movements'
        ],
        'Ingredients': [
            'Herbs and spices',
            'Vegetables and fruits',
            'Proteins and meats',
            'Grains and legumes'
        ],
        'Sauces & Condiments': [
            'Mother sauces',
            'Regional sauces',
            'Condiment varieties',
            'Flavor enhancers'
        ]
    }

    for subcat in sorted(suggestions.keys()):
        print(f"\n{subcat}:")
        for topic in suggestions[subcat]:
            print(f"  • {topic}")

    print("\n" + "=" * 80)

if __name__ == "__main__":
    analyze_food()
