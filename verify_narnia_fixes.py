#!/usr/bin/env python3
"""
Quick verification script to check if Narnia pack fixes have been applied correctly
"""

import json
from collections import Counter

def verify_fixes():
    print("=" * 80)
    print("NARNIA PACK - FIX VERIFICATION")
    print("=" * 80)
    print()

    narnia_path = "/home/user/fiztrivia/Fiz/Resources/Expansion Packs/expansion_narnia.json"

    try:
        with open(narnia_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ ERROR: Could not load file: {e}")
        return

    free_q = data.get('freePreviewQuestions', [])
    paid_q = data.get('paidQuestions', [])
    all_q = free_q + paid_q

    print("1. DUPLICATE REMOVAL CHECK")
    print("-" * 80)

    removed_ids = ['nar_cre_001', 'nar_cre_005', 'nar_mag_003', 'nar_mag_004', 'nar_mag_008']
    all_ids = [q.get('id') for q in all_q]

    for rid in removed_ids:
        if rid not in all_ids:
            print(f"  ✅ {rid} - Successfully removed")
        else:
            print(f"  ❌ {rid} - STILL PRESENT (needs removal)")

    print()

    # Check for new duplicates
    print("2. DUPLICATE QUESTION TEXT CHECK")
    print("-" * 80)

    question_texts = [q.get('question', '').lower().strip() for q in all_q]
    text_counts = Counter(question_texts)
    duplicates = {text: count for text, count in text_counts.items() if count > 1 and text}

    if not duplicates:
        print("  ✅ No duplicate questions found")
    else:
        print(f"  ❌ Found {len(duplicates)} duplicate questions:")
        for text, count in list(duplicates.items())[:5]:
            print(f"    - '{text[:60]}...' ({count} times)")

    print()

    print("3. QUESTION COUNT CHECK")
    print("-" * 80)

    if len(all_q) == 400:
        print(f"  ✅ Total questions: {len(all_q)} (correct)")
    else:
        print(f"  ❌ Total questions: {len(all_q)} (expected 400)")

    if len(free_q) == 40:
        print(f"  ✅ Free preview: {len(free_q)} (correct)")
    else:
        print(f"  ❌ Free preview: {len(free_q)} (expected 40)")

    if len(paid_q) == 360:
        print(f"  ✅ Paid questions: {len(paid_q)} (correct)")
    else:
        print(f"  ❌ Paid questions: {len(paid_q)} (expected 360)")

    print()

    print("4. DIFFICULTY DISTRIBUTION CHECK")
    print("-" * 80)

    diff_counts = Counter(q.get('difficulty') for q in all_q)

    checks = [
        ('easy', 120),
        ('medium', 190),
        ('hard', 90)
    ]

    all_correct = True
    for diff, expected in checks:
        actual = diff_counts.get(diff, 0)
        if actual == expected:
            print(f"  ✅ {diff.capitalize()}: {actual}")
        else:
            print(f"  ❌ {diff.capitalize()}: {actual} (expected {expected})")
            all_correct = False

    print()

    print("5. SUBTOPIC ICONS CHECK")
    print("-" * 80)

    if 'subtopicIcons' in data:
        print(f"  ✅ subtopicIcons field present")
        icons = data['subtopicIcons']
        expected_subtopics = [
            'Books & Plot',
            'Characters',
            'Locations & Worlds',
            'Creatures & Beings',
            'Magic & Objects',
            'Themes & Symbolism'
        ]
        for st in expected_subtopics:
            if st in icons:
                print(f"    ✅ {st}: {icons[st]}")
            else:
                print(f"    ❌ {st}: MISSING")
    else:
        print(f"  ❌ subtopicIcons field NOT PRESENT")

    print()

    print("6. SUBTOPIC DISTRIBUTION CHECK")
    print("-" * 80)

    subtopic_counts = Counter(q.get('subtopic') for q in all_q)

    expected_dist = {
        'Books & Plot': 70,
        'Characters': 70,
        'Locations & Worlds': 65,
        'Creatures & Beings': 65,
        'Magic & Objects': 65,
        'Themes & Symbolism': 65
    }

    all_correct = True
    for subtopic, expected in expected_dist.items():
        actual = subtopic_counts.get(subtopic, 0)
        if actual == expected:
            print(f"  ✅ {subtopic}: {actual}")
        else:
            print(f"  ❌ {subtopic}: {actual} (expected {expected})")
            all_correct = False

    print()

    print("=" * 80)
    print("VERIFICATION SUMMARY")
    print("=" * 80)

    issues_found = []

    # Check all conditions
    if any(rid in all_ids for rid in removed_ids):
        issues_found.append("Duplicate IDs not removed")

    if duplicates:
        issues_found.append("Duplicate question text found")

    if len(all_q) != 400:
        issues_found.append("Wrong total question count")

    if 'subtopicIcons' not in data:
        issues_found.append("Missing subtopicIcons field")

    diff_check = all(diff_counts.get(d, 0) == e for d, e in checks)
    if not diff_check:
        issues_found.append("Difficulty distribution incorrect")

    if issues_found:
        print("\n❌ FIXES NOT COMPLETE")
        print("\nRemaining issues:")
        for issue in issues_found:
            print(f"  - {issue}")
    else:
        print("\n✅ ALL FIXES VERIFIED")
        print("\nThe Narnia expansion pack is now ready for launch!")

    print("=" * 80)

if __name__ == "__main__":
    verify_fixes()
