#!/usr/bin/env python3
"""
Randomize answer positions across all questions to achieve ~25% distribution for each position (A, B, C, D)
"""
import json
import random

# Set seed for reproducibility (can be removed for true randomness)
random.seed(42)

def shuffle_question_options(question):
    """Shuffle options for a single question while maintaining correct answer"""
    options = question['options'].copy()
    correct_answer = question['correct_answer']

    # Shuffle the options
    random.shuffle(options)

    # Update the question with shuffled options
    question['options'] = options

    # Verify correct answer is still in options
    if correct_answer not in options:
        print(f"ERROR: {question['id']} - correct answer lost during shuffle!")
        return False

    return True

def main():
    # Load questions
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    print("="*80)
    print("RANDOMIZING ANSWER POSITIONS")
    print("="*80)
    print()

    total_questions = 0
    shuffled = 0
    errors = 0

    # Shuffle each category
    for category_name, questions in data['categories'].items():
        print(f"Processing {category_name}... ", end='', flush=True)

        category_shuffled = 0
        for q in questions:
            total_questions += 1
            if shuffle_question_options(q):
                category_shuffled += 1
                shuffled += 1
            else:
                errors += 1

        print(f"✓ {category_shuffled}/{len(questions)} questions shuffled")

    print()
    print(f"Total: {shuffled}/{total_questions} questions shuffled successfully")

    if errors > 0:
        print(f"⚠️  Errors: {errors} questions had issues")
        return

    # Save shuffled questions
    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print()
    print("✅ All questions shuffled and saved!")
    print()

    # Verify new distribution
    print("="*80)
    print("VERIFYING NEW DISTRIBUTION")
    print("="*80)
    print()

    position_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    category_stats = {}

    for category_name, questions in data['categories'].items():
        cat_positions = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

        for q in questions:
            correct_answer = q['correct_answer']
            options = q['options']

            try:
                position_index = options.index(correct_answer)
                position_letter = ['A', 'B', 'C', 'D'][position_index]

                position_counts[position_letter] += 1
                cat_positions[position_letter] += 1
            except ValueError:
                print(f"ERROR: {q['id']} - correct answer not found in options")

        category_stats[category_name] = cat_positions

    # Print overall distribution
    print("Overall distribution:")
    for pos in ['A', 'B', 'C', 'D']:
        count = position_counts[pos]
        percentage = (count / total_questions * 100) if total_questions > 0 else 0
        ideal = 25.0
        diff = percentage - ideal

        status = "✓" if abs(diff) < 5 else "⚠️"
        print(f"  Position {pos}: {count:4d} ({percentage:5.1f}%) [{'+'if diff > 0 else ''}{diff:+5.1f}%] {status}")

    print()

    # Print category breakdown
    print("Category breakdown:")
    for category in sorted(category_stats.keys()):
        positions = category_stats[category]
        total = sum(positions.values())

        # Check if reasonably balanced (no position > 35% or < 15%)
        percentages = {pos: (positions[pos] / total * 100) if total > 0 else 0 for pos in ['A', 'B', 'C', 'D']}
        max_pct = max(percentages.values())
        min_pct = min(percentages.values())

        if max_pct > 35 or min_pct < 15:
            status = "⚠️"
        else:
            status = "✓"

        print(f"  {category}: {status}")
        for pos in ['A', 'B', 'C', 'D']:
            print(f"    {pos}: {positions[pos]:3d} ({percentages[pos]:5.1f}%)")

    print()
    print("="*80)
    print("COMPLETE!")
    print("="*80)
    print()
    print("Answer positions have been randomized for all 3,600 questions.")
    print("Distribution should now be approximately 25% for each position A, B, C, D.")

if __name__ == "__main__":
    main()
