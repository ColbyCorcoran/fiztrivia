#!/usr/bin/env python3
"""
Remove duplicate questions from questions.json based on the duplicate IDs list.
Keeps the question with the lower ID number, removes the higher one.
"""

import json
import shutil
from datetime import datetime
from pathlib import Path

# File paths
DUPLICATES_FILE = Path.home() / "Library/Mobile Documents/com~apple~CloudDocs/Downloads/exact_duplicate_question_ids.json"
QUESTIONS_FILE = Path("Fiz/Resources/questions.json")
BACKUP_FILE = Path(f"Fiz/Resources/questions_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")

def main():
    # Load duplicate IDs
    print(f"Loading duplicates from: {DUPLICATES_FILE}")
    with open(DUPLICATES_FILE, 'r', encoding='utf-8') as f:
        duplicates = json.load(f)

    # Determine which IDs to remove (keep lower ID, remove higher)
    ids_to_remove = set()
    for question_text, id_list in duplicates.items():
        if len(id_list) == 2:
            # Keep the lower ID (first in list), remove the higher one
            ids_to_remove.add(id_list[1])
            print(f"Will remove: {id_list[1]} (keeping {id_list[0]})")

    print(f"\nTotal duplicate IDs to remove: {len(ids_to_remove)}")

    # Load questions
    print(f"\nLoading questions from: {QUESTIONS_FILE}")
    with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
        questions_data = json.load(f)

    # Count original questions
    original_count = sum(len(questions) for questions in questions_data['categories'].values())
    print(f"Original question count: {original_count}")

    # Create backup
    print(f"\nCreating backup: {BACKUP_FILE}")
    shutil.copy2(QUESTIONS_FILE, BACKUP_FILE)

    # Remove duplicates from each category
    removed_count = 0
    for category_name, questions_list in questions_data['categories'].items():
        original_len = len(questions_list)
        filtered = [q for q in questions_list if q['id'] not in ids_to_remove]
        questions_data['categories'][category_name] = filtered
        removed_from_category = original_len - len(filtered)
        if removed_from_category > 0:
            print(f"  Removed {removed_from_category} duplicate(s) from {category_name}")
        removed_count += removed_from_category

    final_count = sum(len(questions) for questions in questions_data['categories'].values())

    print(f"\nQuestions removed: {removed_count}")
    print(f"Final question count: {final_count}")

    # Verify all duplicates were found and removed
    if removed_count != len(ids_to_remove):
        print(f"\nWARNING: Expected to remove {len(ids_to_remove)} duplicates, but removed {removed_count}")
        # Find which IDs weren't found
        all_remaining_ids = set()
        for questions_list in questions_data['categories'].values():
            for q in questions_list:
                all_remaining_ids.add(q['id'])

        still_present = ids_to_remove & all_remaining_ids
        if still_present:
            print(f"IDs still present: {still_present}")

    # Save updated questions
    print(f"\nSaving updated questions to: {QUESTIONS_FILE}")
    with open(QUESTIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(questions_data, f, indent=2, ensure_ascii=False)

    print("\n✅ Done! Duplicates removed successfully.")
    print(f"   Backup saved: {BACKUP_FILE}")

    # Show which IDs were kept vs removed
    print("\nSummary of removed duplicates:")
    for question_text, id_list in duplicates.items():
        if len(id_list) == 2:
            print(f"  '{question_text[:60]}...'")
            print(f"    ✓ Kept: {id_list[0]}")
            print(f"    ✗ Removed: {id_list[1]}")

if __name__ == "__main__":
    main()
