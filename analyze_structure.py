#!/usr/bin/env python3
"""
Analyze the structure of questions.json database
"""

import json
from collections import defaultdict

def analyze_database(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    categories = data['categories']

    # Overall stats
    total_questions = sum(len(questions) for questions in categories.values())

    print("=" * 80)
    print("QUESTIONS DATABASE STRUCTURE ANALYSIS")
    print("=" * 80)
    print(f"\nTotal Questions: {total_questions}")
    print(f"Total Categories: {len(categories)}")
    print()

    # Analyze each category
    for category_name in sorted(categories.keys()):
        questions = categories[category_name]
        print(f"\n{'=' * 80}")
        print(f"CATEGORY: {category_name}")
        print(f"{'=' * 80}")
        print(f"Total Questions: {len(questions)}")

        # Subcategory breakdown
        subcategories = defaultdict(list)
        difficulty_counts = defaultdict(int)

        for q in questions:
            subcategories[q['subcategory']].append(q)
            difficulty_counts[q['difficulty']] += 1

        print(f"\nSubcategories ({len(subcategories)}):")
        for subcat in sorted(subcategories.keys()):
            count = len(subcategories[subcat])
            # Get difficulty breakdown for this subcategory
            subcat_diff = defaultdict(int)
            for q in subcategories[subcat]:
                subcat_diff[q['difficulty']] += 1

            diff_str = f"easy: {subcat_diff['easy']}, medium: {subcat_diff['medium']}, hard: {subcat_diff['hard']}"
            print(f"  • {subcat}: {count} questions ({diff_str})")

        print(f"\nDifficulty Distribution:")
        print(f"  • Easy: {difficulty_counts['easy']}")
        print(f"  • Medium: {difficulty_counts['medium']}")
        print(f"  • Hard: {difficulty_counts['hard']}")

        # ID range
        ids = [q['id'] for q in questions]
        print(f"\nID Range: {min(ids)} to {max(ids)}")

    print("\n" + "=" * 80)
    print("SUMMARY BY CATEGORY")
    print("=" * 80)

    summary = []
    for category_name in sorted(categories.keys()):
        questions = categories[category_name]
        subcats = set(q['subcategory'] for q in questions)
        summary.append({
            'category': category_name,
            'count': len(questions),
            'subcategories': len(subcats)
        })

    for item in sorted(summary, key=lambda x: x['count'], reverse=True):
        print(f"{item['category']:20s} {item['count']:4d} questions, {item['subcategories']:2d} subcategories")

    print("\n" + "=" * 80)

if __name__ == "__main__":
    analyze_database("Fiz/Resources/questions.json")
