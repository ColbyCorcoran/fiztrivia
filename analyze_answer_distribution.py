#!/usr/bin/env python3
"""
Analyze answer option distribution in expansion pack files.
Shows how often each option slot (A, B, C, D) is the correct answer.
"""

import json
from collections import Counter

def analyze_expansion_pack(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    pack_name = data.get('packName', 'Unknown')

    # Combine all questions (free preview + paid)
    all_questions = data.get('freePreviewQuestions', []) + data.get('paidQuestions', [])

    total = len(all_questions)
    slot_counts = Counter()

    for q in all_questions:
        options = q.get('options', [])
        correct_answer = q.get('correct_answer', '')

        if not options or not correct_answer:
            continue

        try:
            correct_index = options.index(correct_answer)
            slot_letter = ['A', 'B', 'C', 'D'][correct_index]
            slot_counts[slot_letter] += 1
        except (ValueError, IndexError):
            print(f"⚠️  Warning: Correct answer not found for question {q.get('id', 'UNKNOWN')}")

    return pack_name, total, slot_counts

def print_distribution(pack_name, total, slot_counts):
    print(f"\n{'=' * 80}")
    print(f"Pack: {pack_name}")
    print(f"Total Questions: {total}")
    print(f"{'=' * 80}")

    if total == 0:
        print("No questions found!")
        return

    for slot in ['A', 'B', 'C', 'D']:
        count = slot_counts.get(slot, 0)
        percentage = (count / total * 100) if total > 0 else 0

        # Color code based on how far from ideal (25%)
        status = ""
        if percentage > 40:
            status = " ⚠️  TOO HIGH!"
        elif percentage < 15:
            status = " ⚠️  TOO LOW!"
        elif percentage > 30:
            status = " ⚠️  High"
        elif percentage < 20:
            status = " ⚠️  Low"
        else:
            status = " ✅"

        bar_length = int(percentage / 2)  # Scale to 50 chars max
        bar = '█' * bar_length

        print(f"  Slot {slot}: {count:4d} ({percentage:5.1f}%) {bar}{status}")

    print(f"{'=' * 80}")

def main():
    expansion_files = [
        '/Users/colbycorcoran/Documents/App Development/Fiz/Fiz/Resources/Expansion Packs/expansion_harry_potter.json',
        '/Users/colbycorcoran/Documents/App Development/Fiz/Fiz/Resources/Expansion Packs/expansion_pokemon.json',
        '/Users/colbycorcoran/Documents/App Development/Fiz/Fiz/Resources/Expansion Packs/expansion_80s_trivia.json',
        '/Users/colbycorcoran/Documents/App Development/Fiz/Fiz/Resources/Expansion Packs/expansion_disney.json',
        '/Users/colbycorcoran/Documents/App Development/Fiz/Fiz/Resources/Expansion Packs/expansion_the_office.json',
    ]

    print("Analyzing answer option distribution in expansion packs...")

    all_results = []

    for file_path in expansion_files:
        try:
            pack_name, total, slot_counts = analyze_expansion_pack(file_path)
            all_results.append((pack_name, total, slot_counts))
            print_distribution(pack_name, total, slot_counts)
        except FileNotFoundError:
            print(f"\n⚠️  File not found: {file_path}")
        except Exception as e:
            print(f"\n❌  Error processing {file_path}: {e}")

    # Summary
    print(f"\n{'=' * 80}")
    print("SUMMARY")
    print(f"{'=' * 80}")

    for pack_name, total, slot_counts in all_results:
        slot_a_pct = (slot_counts.get('A', 0) / total * 100) if total > 0 else 0
        status = "✅ Balanced" if 20 <= slot_a_pct <= 30 else "⚠️  NEEDS BALANCING"
        print(f"{pack_name:30s} - Total: {total:4d} - Slot A: {slot_a_pct:5.1f}% {status}")

if __name__ == '__main__':
    main()
