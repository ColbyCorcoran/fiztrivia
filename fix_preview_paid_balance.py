#!/usr/bin/env python3
"""
Fix Pixar expansion pack preview/paid balance.
Convert 9 preview questions to paid to achieve 10% preview (40) and 90% paid (360).
"""

import json
import shutil
from datetime import datetime

def fix_preview_paid_balance():
    """Convert 9 preview questions to paid questions."""

    pixar_path = "Fiz/Resources/Expansion Packs/expansion_pixar.json"

    # Create backup
    backup_name = f"expansion_pixar_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    shutil.copy2(pixar_path, backup_name)
    print(f"✓ Backup created: {backup_name}\n")

    # Load Pixar pack
    with open(pixar_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("="*70)
    print("PIXAR PACK PREVIEW/PAID BALANCE FIX")
    print("="*70)

    # Show current counts
    current_preview = len(data["freePreviewQuestions"])
    current_paid = len(data["paidQuestions"])
    print(f"\nCurrent counts:")
    print(f"  Preview: {current_preview} ({current_preview/400*100:.1f}%)")
    print(f"  Paid: {current_paid} ({current_paid/400*100:.1f}%)")
    print(f"  Total: {current_preview + current_paid}")

    # Target counts
    target_preview = 40
    target_paid = 360
    questions_to_move = current_preview - target_preview

    print(f"\nTarget counts:")
    print(f"  Preview: {target_preview} (10%)")
    print(f"  Paid: {target_paid} (90%)")
    print(f"  Questions to move: {questions_to_move}")

    if questions_to_move != 9:
        print(f"\n⚠ Warning: Expected to move 9 questions, but calculated {questions_to_move}")
        response = input("Continue anyway? (yes/no): ").strip().lower()
        if response != "yes":
            print("Cancelled.")
            return

    # Find the last 9 preview questions (the ones we just converted from Disney IDs)
    # These should be pxr_preview_001 through pxr_preview_009
    preview_questions = data["freePreviewQuestions"]
    questions_to_convert = []

    # Find questions with pxr_preview_001 through pxr_preview_009
    for i, q in enumerate(preview_questions):
        if q["id"] in [f"pxr_preview_{i:03d}" for i in range(1, 10)]:
            questions_to_convert.append((i, q))

    print(f"\nFound {len(questions_to_convert)} questions to convert:")
    for idx, q in questions_to_convert:
        print(f"  {q['id']}: {q['question'][:60]}...")

    if len(questions_to_convert) != 9:
        print(f"\n✗ Error: Found {len(questions_to_convert)} questions, expected 9")
        return

    # Find highest paid ID to continue numbering
    paid_ids = [q["id"] for q in data["paidQuestions"] if q["id"].startswith("pxr_paid_")]
    paid_numbers = [int(id.split("_")[2]) for id in paid_ids]
    next_paid_number = max(paid_numbers) + 1

    print(f"\nConverting questions to paid (starting from pxr_paid_{next_paid_number}):")

    # Convert questions
    converted_questions = []
    for idx, q in sorted(questions_to_convert, reverse=True):  # Remove from end first
        old_id = q["id"]
        new_id = f"pxr_paid_{next_paid_number}"

        # Update ID
        q["id"] = new_id

        # Remove from preview questions
        data["freePreviewQuestions"].pop(idx)

        # Add to paid questions
        data["paidQuestions"].append(q)
        converted_questions.append((old_id, new_id))

        print(f"  {old_id} → {new_id}")
        next_paid_number += 1

    # Update pack metadata
    print(f"\nUpdating pack metadata:")
    old_preview_count = data["freePreviewCount"]
    data["freePreviewCount"] = 40
    print(f"  freePreviewCount: {old_preview_count} → 40")

    # Verify final counts
    final_preview = len(data["freePreviewQuestions"])
    final_paid = len(data["paidQuestions"])

    print(f"\nFinal counts:")
    print(f"  Preview: {final_preview} ({final_preview/400*100:.1f}%)")
    print(f"  Paid: {final_paid} ({final_paid/400*100:.1f}%)")
    print(f"  Total: {final_preview + final_paid}")

    if final_preview != 40 or final_paid != 360:
        print(f"\n✗ Error: Final counts don't match target!")
        return

    # Write to file
    temp_path = pixar_path + ".tmp"
    with open(temp_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    shutil.move(temp_path, pixar_path)
    print(f"\n✓ Updated: {pixar_path}")

    # Verify file is valid JSON
    with open(pixar_path, "r", encoding="utf-8") as f:
        verify_data = json.load(f)
    print(f"✓ Verified: File is valid JSON")

    print("\n" + "="*70)
    print("✓ PREVIEW/PAID BALANCE FIX COMPLETE")
    print("="*70)
    print(f"Moved {len(converted_questions)} questions from preview to paid")
    print(f"Final balance: 40 preview (10%) / 360 paid (90%)")

if __name__ == "__main__":
    try:
        fix_preview_paid_balance()
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
