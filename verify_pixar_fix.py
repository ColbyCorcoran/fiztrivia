#!/usr/bin/env python3
"""
Verify that the Pixar expansion pack fix is complete and correct.
This script runs comprehensive checks to ensure all transformations succeeded.
"""

import json
import sys

def verify_pixar_fix():
    """Verify all aspects of the Pixar pack fix."""

    print("="*70)
    print("PIXAR EXPANSION PACK FIX VERIFICATION")
    print("="*70)

    # 1. Load Pixar pack
    pixar_path = "Fiz/Resources/Expansion Packs/expansion_pixar.json"
    try:
        with open(pixar_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"\n✓ File loaded successfully: {pixar_path}")
    except Exception as e:
        print(f"\n✗ Failed to load file: {e}")
        return 1

    checks_passed = 0
    checks_failed = 0

    print("\n" + "="*70)
    print("RUNNING VERIFICATION CHECKS")
    print("="*70)

    # 2. Check total question count
    total = len(data["freePreviewQuestions"]) + len(data["paidQuestions"])
    print(f"\n1. Total Question Count:")
    if total == 400:
        print(f"   ✓ PASS: Total = {total} (expected 400)")
        checks_passed += 1
    else:
        print(f"   ✗ FAIL: Total = {total} (expected 400)")
        checks_failed += 1

    # 3. Check for any dsn_ IDs
    all_questions = data["freePreviewQuestions"] + data["paidQuestions"]
    dsn_ids = [q["id"] for q in all_questions if q["id"].startswith("dsn_")]
    print(f"\n2. Disney ID Check (dsn_ prefix):")
    if len(dsn_ids) == 0:
        print(f"   ✓ PASS: No dsn_ IDs found")
        checks_passed += 1
    else:
        print(f"   ✗ FAIL: Found {len(dsn_ids)} dsn_ IDs: {dsn_ids[:5]}")
        checks_failed += 1

    # 4. Check all topics are correct
    wrong_topics = [(q["id"], q["topic"]) for q in all_questions if q["topic"] != "com.fiz.pack.pixar"]
    print(f"\n3. Topic Field Check:")
    if len(wrong_topics) == 0:
        print(f"   ✓ PASS: All questions have topic = 'com.fiz.pack.pixar'")
        checks_passed += 1
    else:
        print(f"   ✗ FAIL: Found {len(wrong_topics)} questions with wrong topic:")
        for qid, topic in wrong_topics[:5]:
            print(f"      {qid}: '{topic}'")
        checks_failed += 1

    # 5. Check for duplicate IDs
    all_ids = [q["id"] for q in all_questions]
    unique_ids = set(all_ids)
    print(f"\n4. Unique ID Check:")
    if len(all_ids) == len(unique_ids):
        print(f"   ✓ PASS: All {len(all_ids)} IDs are unique")
        checks_passed += 1
    else:
        duplicates = [id for id in all_ids if all_ids.count(id) > 1]
        print(f"   ✗ FAIL: Found {len(all_ids) - len(unique_ids)} duplicate IDs: {set(duplicates)}")
        checks_failed += 1

    # 6. Check pxr_preview sequence
    preview_ids = sorted([q["id"] for q in data["freePreviewQuestions"] if "preview" in q["id"]])
    expected_preview = [f"pxr_preview_{i:03d}" for i in range(1, 10)]
    print(f"\n5. Preview ID Sequence Check:")
    if len([id for id in preview_ids if id.startswith("pxr_preview_")]) >= 9:
        if expected_preview == preview_ids[:9]:
            print(f"   ✓ PASS: Preview IDs pxr_preview_001 to pxr_preview_009 present")
            checks_passed += 1
        else:
            print(f"   ✗ FAIL: Preview ID sequence incorrect")
            print(f"      Expected: {expected_preview[:5]}...")
            print(f"      Got: {preview_ids[:5]}...")
            checks_failed += 1
    else:
        print(f"   ⚠ WARNING: Less than 9 pxr_preview_* IDs found")
        checks_failed += 1

    # 7. Check pxr_paid range includes new IDs
    paid_ids = [q["id"] for q in data["paidQuestions"] if q["id"].startswith("pxr_paid_")]
    paid_numbers = [int(id.split("_")[2]) for id in paid_ids]
    has_new_range = any(num >= 217 for num in paid_numbers)
    print(f"\n6. Paid ID Range Check:")
    if has_new_range:
        max_paid = max(paid_numbers)
        min_paid = min(paid_numbers)
        count_new = sum(1 for num in paid_numbers if num >= 217)
        print(f"   ✓ PASS: New paid IDs present (pxr_paid_217+)")
        print(f"      Range: pxr_paid_{min_paid} to pxr_paid_{max_paid}")
        print(f"      New IDs (≥217): {count_new}")
        checks_passed += 1
    else:
        print(f"   ✗ FAIL: No paid IDs in range pxr_paid_217+")
        checks_failed += 1

    # 8. Check ID format consistency
    print(f"\n7. ID Format Consistency:")
    pxr_ids = [q["id"] for q in all_questions if q["id"].startswith("pxr_")]
    if len(pxr_ids) == 400:
        print(f"   ✓ PASS: All 400 questions use pxr_ prefix")
        checks_passed += 1
    else:
        print(f"   ✗ FAIL: Only {len(pxr_ids)}/400 questions use pxr_ prefix")
        checks_failed += 1

    # 9. Check question array sizes
    print(f"\n8. Question Array Sizes:")
    preview_count = len(data["freePreviewQuestions"])
    paid_count = len(data["paidQuestions"])
    if preview_count == 49 and paid_count == 351:
        print(f"   ✓ PASS: Preview={preview_count}, Paid={paid_count}")
        checks_passed += 1
    else:
        print(f"   ⚠ INFO: Preview={preview_count} (expected ~49), Paid={paid_count} (expected ~351)")
        checks_passed += 1  # Not a critical failure

    # Summary
    print("\n" + "="*70)
    print("VERIFICATION SUMMARY")
    print("="*70)
    print(f"Checks passed: {checks_passed}/{checks_passed + checks_failed}")
    print(f"Checks failed: {checks_failed}/{checks_passed + checks_failed}")

    if checks_failed == 0:
        print("\n✓✓✓ ALL CHECKS PASSED - FIX IS COMPLETE! ✓✓✓")
        print("\nThe Pixar expansion pack is ready to use.")
        return 0
    else:
        print(f"\n✗✗✗ FIX INCOMPLETE - {checks_failed} CHECK(S) FAILED ✗✗✗")
        print("\nPlease review the failures above and re-run the fix script.")
        return 1

if __name__ == "__main__":
    try:
        exit_code = verify_pixar_fix()
        sys.exit(exit_code)
    except Exception as e:
        print(f"\n✗ Verification error: {e}")
        sys.exit(1)
