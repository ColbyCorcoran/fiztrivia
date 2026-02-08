#!/usr/bin/env python3
"""
Fix expansion pack IDs to be sequential instead of organized by subtopic.
"""

import json
from pathlib import Path

def fix_pack_ids(file_path, prefix):
    """
    Fix IDs in an expansion pack to be sequential.

    Args:
        file_path: Path to the expansion pack JSON file
        prefix: Prefix for the IDs (e.g., 'cnd', '90s', 'mar', 'nar')
    """
    print(f"\nProcessing {file_path.name}...")

    # Read the JSON file
    with open(file_path, 'r', encoding='utf-8') as f:
        pack_data = json.load(f)

    # Create backup
    backup_path = file_path.with_suffix('.json.backup')
    with open(backup_path, 'w', encoding='utf-8') as f:
        json.dump(pack_data, f, indent=2, ensure_ascii=False)
    print(f"  Backup created: {backup_path.name}")

    # Renumber all questions sequentially
    counter = 1

    # Fix free preview questions
    if 'freePreviewQuestions' in pack_data:
        for question in pack_data['freePreviewQuestions']:
            old_id = question['id']
            new_id = f"{prefix}_{counter:03d}"
            question['id'] = new_id
            print(f"  {old_id} → {new_id}")
            counter += 1

    # Fix paid questions
    if 'paidQuestions' in pack_data:
        for question in pack_data['paidQuestions']:
            old_id = question['id']
            new_id = f"{prefix}_{counter:03d}"
            question['id'] = new_id
            print(f"  {old_id} → {new_id}")
            counter += 1

    # Write the fixed JSON back
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(pack_data, f, indent=2, ensure_ascii=False)

    total_questions = counter - 1
    print(f"  ✓ Fixed {total_questions} questions")
    print(f"  ✓ Saved to {file_path.name}")

    return total_questions

def main():
    base_path = Path("/Users/colbycorcoran/Documents/App Development/Fiz/Fiz/Resources/Expansion Packs")

    packs_to_fix = [
        ("expansion_candy.json", "cnd"),
        ("expansion_90s_trivia.json", "90s"),
        ("expansion_mario.json", "mar"),
        ("expansion_narnia.json", "nar")
    ]

    print("=" * 60)
    print("Fixing Expansion Pack IDs")
    print("=" * 60)

    for filename, prefix in packs_to_fix:
        file_path = base_path / filename
        if file_path.exists():
            total = fix_pack_ids(file_path, prefix)
        else:
            print(f"\n⚠️  File not found: {filename}")

    print("\n" + "=" * 60)
    print("✓ All packs fixed!")
    print("=" * 60)

if __name__ == "__main__":
    main()
