#!/usr/bin/env python3
"""Analyze correct answer position distribution across all questions"""
import json

def main():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    # Overall statistics
    total_questions = 0
    position_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

    # Category breakdown
    category_stats = {}

    for category_name, questions in data['categories'].items():
        cat_positions = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

        for q in questions:
            total_questions += 1

            # Find position of correct answer
            correct_answer = q['correct_answer']
            options = q['options']

            try:
                position_index = options.index(correct_answer)
                position_letter = ['A', 'B', 'C', 'D'][position_index]

                position_counts[position_letter] += 1
                cat_positions[position_letter] += 1
            except (ValueError, IndexError) as e:
                print(f"ERROR: {q['id']} - correct answer not in options: {correct_answer}")

        category_stats[category_name] = {
            'total': len(questions),
            'positions': cat_positions
        }

    # Print overall statistics
    print("="*80)
    print("OVERALL ANSWER DISTRIBUTION")
    print("="*80)
    print(f"Total questions analyzed: {total_questions}")
    print()

    print("Correct answer position:")
    for pos in ['A', 'B', 'C', 'D']:
        count = position_counts[pos]
        percentage = (count / total_questions * 100) if total_questions > 0 else 0
        ideal = 25.0
        diff = percentage - ideal
        print(f"  Position {pos}: {count:4d} questions ({percentage:5.1f}%) [{'+'if diff > 0 else ''}{diff:+5.1f}% from ideal 25%]")

    print()
    print("="*80)
    print("CATEGORY BREAKDOWN")
    print("="*80)

    for category in sorted(category_stats.keys()):
        stats = category_stats[category]
        total = stats['total']
        positions = stats['positions']

        print(f"\n{category} ({total} questions):")
        for pos in ['A', 'B', 'C', 'D']:
            count = positions[pos]
            percentage = (count / total * 100) if total > 0 else 0
            ideal = 25.0
            diff = percentage - ideal

            # Visual indicator of bias
            if abs(diff) > 10:
                indicator = "⚠️  SEVERE BIAS"
            elif abs(diff) > 5:
                indicator = "⚠️  BIAS"
            else:
                indicator = "✓"

            print(f"  {pos}: {count:3d} ({percentage:5.1f}%) [{'+'if diff > 0 else ''}{diff:+5.1f}%] {indicator}")

    print()
    print("="*80)
    print("SUMMARY")
    print("="*80)

    # Find most biased categories
    most_biased = []
    for category, stats in category_stats.items():
        total = stats['total']
        positions = stats['positions']

        # Calculate max deviation from 25%
        max_deviation = 0
        for pos in ['A', 'B', 'C', 'D']:
            percentage = (positions[pos] / total * 100) if total > 0 else 0
            deviation = abs(percentage - 25.0)
            if deviation > max_deviation:
                max_deviation = deviation

        most_biased.append((category, max_deviation))

    most_biased.sort(key=lambda x: x[1], reverse=True)

    print("\nMost biased categories (by max deviation from 25%):")
    for i, (cat, dev) in enumerate(most_biased[:5], 1):
        print(f"  {i}. {cat}: {dev:.1f}% deviation")

    print()
    overall_bias = max(abs((position_counts[pos] / total_questions * 100) - 25.0) for pos in ['A', 'B', 'C', 'D'])
    print(f"Overall database bias: {overall_bias:.1f}% (max deviation from 25%)")

    if overall_bias > 10:
        print("  Status: ⚠️  SEVERE - Needs redistribution")
    elif overall_bias > 5:
        print("  Status: ⚠️  MODERATE - Should be redistributed")
    else:
        print("  Status: ✓ ACCEPTABLE - Within 5% of ideal")

if __name__ == "__main__":
    main()
