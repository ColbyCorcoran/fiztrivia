#!/usr/bin/env python3
"""
Verify and audit Pixar expansion pack ID issues.
This script identifies questions with incorrect Disney IDs and creates a backup.
"""

import json
from datetime import datetime
import shutil
import os

def verify_pixar_issues():
    """Audit the Pixar pack for questions with incorrect Disney IDs."""

    pixar_path = "Fiz/Resources/Expansion Packs/expansion_pixar.json"

    # 1. Create timestamped backup
    backup_name = f"expansion_pixar_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    shutil.copy2(pixar_path, backup_name)
    print(f"✓ Backup created: {backup_name}\n")

    # 2. Load and analyze Pixar pack
    with open(pixar_path, "r", encoding="utf-8") as f:
        pixar_data = json.load(f)

    # 3. Find all questions with dsn_ IDs
    problems = []
    for q in pixar_data["freePreviewQuestions"]:
        if q["id"].startswith("dsn_"):
            problems.append(("preview", q))

    for q in pixar_data["paidQuestions"]:
        if q["id"].startswith("dsn_"):
            problems.append(("paid", q))

    # 4. Generate report
    preview_count = sum(1 for t, q in problems if t == "preview")
    paid_count = sum(1 for t, q in problems if t == "paid")

    print("="*70)
    print("PIXAR EXPANSION PACK ID AUDIT")
    print("="*70)
    print(f"\n📊 Found {len(problems)} questions with incorrect Disney IDs:")
    print(f"   - Preview questions: {preview_count}")
    print(f"   - Paid questions: {paid_count}")

    # 5. Display sample problems
    print(f"\n📝 Sample Problems (showing first 10):\n")
    for i, (qtype, q) in enumerate(problems[:10], 1):
        print(f"{i}. [{qtype.upper()}] {q['id']}")
        print(f"   Question: {q['question'][:60]}...")
        print(f"   Topic: {q['topic']} (should be: com.fiz.pack.pixar)")
        print(f"   Subtopic: {q['subtopic']}")
        print()

    # 6. Analyze current Pixar ID distribution
    all_questions = pixar_data["freePreviewQuestions"] + pixar_data["paidQuestions"]
    pxr_ids = [q["id"] for q in all_questions if q["id"].startswith("pxr_")]
    dsn_ids = [q["id"] for q in all_questions if q["id"].startswith("dsn_")]

    print("="*70)
    print("CURRENT ID DISTRIBUTION")
    print("="*70)
    print(f"Total questions: {len(all_questions)}")
    print(f"Questions with pxr_ IDs: {len(pxr_ids)}")
    print(f"Questions with dsn_ IDs: {len(dsn_ids)}")

    # Find highest numbered pxr_paid ID
    pxr_paid_ids = [q["id"] for q in all_questions if q["id"].startswith("pxr_paid_")]
    if pxr_paid_ids:
        pxr_paid_numbers = [int(id.split("_")[2]) for id in pxr_paid_ids]
        highest_pxr_paid = max(pxr_paid_numbers)
        print(f"Highest pxr_paid_ ID: pxr_paid_{highest_pxr_paid}")

    # 7. Proposed ID mapping
    print("\n" + "="*70)
    print("PROPOSED ID CHANGES")
    print("="*70)
    print(f"\nPreview questions will be renamed:")
    print(f"  dsn_preview_* → pxr_preview_001 through pxr_preview_{preview_count:03d}")
    print(f"\nPaid questions will be renamed:")
    print(f"  dsn_paid_* → pxr_paid_217 through pxr_paid_{216 + paid_count}")
    print(f"\nAll {len(problems)} questions will have topic updated:")
    print(f"  'Disney' → 'com.fiz.pack.pixar'")

    print("\n" + "="*70)
    print("✓ VERIFICATION COMPLETE")
    print("="*70)
    print(f"Backup: {backup_name}")
    print("Ready to proceed with fix_pixar_ids.py")

    return len(problems)

if __name__ == "__main__":
    try:
        problem_count = verify_pixar_issues()
        print(f"\n✓ Found {problem_count} questions to fix")
        exit(0)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        exit(1)
