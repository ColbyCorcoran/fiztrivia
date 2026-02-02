#!/usr/bin/env python3
"""
Fix Pixar expansion pack ID and topic issues.
This script transforms all questions with Disney IDs to use correct Pixar IDs.
"""

import json
import shutil
from datetime import datetime
import sys

def fix_pixar_ids(dry_run=False):
    """Transform all questions with Disney IDs to use correct Pixar IDs."""

    pixar_path = "Fiz/Resources/Expansion Packs/expansion_pixar.json"

    # 1. Load Pixar pack
    print(f"Loading {pixar_path}...")
    with open(pixar_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 2. Create ID mappings
    preview_counter = 1
    paid_counter = 217  # Continue from existing pxr_paid_216
    id_mapping = {}
    changes_made = 0

    print("\n" + "="*70)
    print("TRANSFORMING IDS")
    print("="*70 + "\n")

    # 3. Fix preview questions
    print("Preview Questions:")
    for q in data["freePreviewQuestions"]:
        if q["id"].startswith("dsn_"):
            old_id = q["id"]
            new_id = f"pxr_preview_{preview_counter:03d}"
            id_mapping[old_id] = new_id

            if not dry_run:
                q["id"] = new_id
                q["topic"] = "com.fiz.pack.pixar"

            preview_counter += 1
            changes_made += 1
            print(f"  {old_id:20s} → {new_id}")

    # 4. Fix paid questions
    print("\nPaid Questions:")
    for q in data["paidQuestions"]:
        if q["id"].startswith("dsn_"):
            old_id = q["id"]
            new_id = f"pxr_paid_{paid_counter}"
            id_mapping[old_id] = new_id

            if not dry_run:
                q["id"] = new_id
                q["topic"] = "com.fiz.pack.pixar"

            paid_counter += 1
            changes_made += 1
            print(f"  {old_id:20s} → {new_id}")

    print("\n" + "="*70)
    print(f"Total changes: {changes_made}")
    print("="*70)

    # 5. Write to file (if not dry run)
    if not dry_run:
        # Create backup first
        backup_name = f"expansion_pixar_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        shutil.copy2(pixar_path, backup_name)
        print(f"\n✓ Backup created: {backup_name}")

        # Write to temp file first
        temp_path = pixar_path + ".tmp"
        with open(temp_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        # Atomic rename
        shutil.move(temp_path, pixar_path)
        print(f"✓ Updated: {pixar_path}")

        # Verify file was written correctly
        with open(pixar_path, "r", encoding="utf-8") as f:
            verify_data = json.load(f)
        print(f"✓ Verified: File is valid JSON")

        # Count results
        all_questions = verify_data["freePreviewQuestions"] + verify_data["paidQuestions"]
        dsn_count = sum(1 for q in all_questions if q["id"].startswith("dsn_"))
        pxr_count = sum(1 for q in all_questions if q["id"].startswith("pxr_"))
        print(f"\n📊 Final counts:")
        print(f"   Questions with pxr_ IDs: {pxr_count}")
        print(f"   Questions with dsn_ IDs: {dsn_count}")

        if dsn_count == 0:
            print(f"\n✓ SUCCESS: All Disney IDs have been converted!")
        else:
            print(f"\n⚠ WARNING: {dsn_count} Disney IDs remain")

    else:
        print("\n[DRY RUN - No changes made]")

    return id_mapping

def main():
    """Main entry point with interactive confirmation."""

    print("="*70)
    print("PIXAR EXPANSION PACK ID FIX")
    print("="*70)

    # Run dry run first
    print("\n=== DRY RUN ===\n")
    try:
        id_mapping = fix_pixar_ids(dry_run=True)
        print(f"\nDry run complete. Would transform {len(id_mapping)} questions.")
    except Exception as e:
        print(f"\n✗ Error during dry run: {e}")
        return 1

    # Ask for confirmation
    print("\n" + "="*70)
    response = input("\nApply changes? (yes/no): ").strip().lower()

    if response != "yes":
        print("Cancelled. No changes made.")
        return 0

    # Apply actual changes
    print("\n=== APPLYING CHANGES ===\n")
    try:
        id_mapping = fix_pixar_ids(dry_run=False)
        print(f"\n✓ Successfully transformed {len(id_mapping)} questions!")
        return 0
    except Exception as e:
        print(f"\n✗ Error applying changes: {e}")
        print("The backup file can be used to restore the original.")
        return 1

if __name__ == "__main__":
    exit(main())
