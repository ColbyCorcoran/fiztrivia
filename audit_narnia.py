#!/usr/bin/env python3
"""
Comprehensive audit script for Narnia expansion pack
"""

import json
import re
from collections import Counter, defaultdict

def load_json(filepath):
    """Load and parse JSON file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ FAIL: Could not load {filepath}: {e}")
        return None

def audit_narnia_pack():
    """Perform comprehensive audit of Narnia expansion pack"""

    print("=" * 80)
    print("NARNIA EXPANSION PACK AUDIT REPORT")
    print("=" * 80)
    print()

    # Load the pack
    narnia_path = "/home/user/fiztrivia/Fiz/Resources/Expansion Packs/expansion_narnia.json"
    harry_potter_path = "/home/user/fiztrivia/Fiz/Resources/Expansion Packs/expansion_harry_potter.json"

    narnia_data = load_json(narnia_path)
    if not narnia_data:
        return

    harry_potter_data = load_json(harry_potter_path)

    issues = []
    passed_checks = []
    failed_checks = []

    # ========================================================================
    # 1. STRUCTURAL VALIDATION
    # ========================================================================
    print("1. STRUCTURAL VALIDATION")
    print("-" * 80)

    # Check for free and paid questions
    free_questions = narnia_data.get('freePreviewQuestions', [])
    paid_questions = narnia_data.get('paidQuestions', [])
    total_questions = free_questions + paid_questions

    # 1.1 Question count
    expected_total = 400
    expected_free = 40
    expected_paid = 360

    actual_total = len(total_questions)
    actual_free = len(free_questions)
    actual_paid = len(paid_questions)

    if actual_total == expected_total:
        passed_checks.append("Total question count: 400")
        print(f"✅ PASS: Total questions = {actual_total} (expected {expected_total})")
    else:
        failed_checks.append(f"Total question count: {actual_total} (expected {expected_total})")
        print(f"❌ FAIL: Total questions = {actual_total} (expected {expected_total})")
        issues.append(f"Wrong total question count: {actual_total} instead of {expected_total}")

    if actual_free == expected_free:
        passed_checks.append("Free preview count: 40")
        print(f"✅ PASS: Free preview questions = {actual_free} (expected {expected_free})")
    else:
        failed_checks.append(f"Free preview count: {actual_free} (expected {expected_free})")
        print(f"❌ FAIL: Free preview questions = {actual_free} (expected {expected_free})")
        issues.append(f"Wrong free preview count: {actual_free} instead of {expected_free}")

    if actual_paid == expected_paid:
        passed_checks.append("Paid question count: 360")
        print(f"✅ PASS: Paid questions = {actual_paid} (expected {expected_paid})")
    else:
        failed_checks.append(f"Paid question count: {actual_paid} (expected {expected_paid})")
        print(f"❌ FAIL: Paid questions = {actual_paid} (expected {expected_paid})")
        issues.append(f"Wrong paid question count: {actual_paid} instead of {expected_paid}")

    # 1.2 Required fields in each question
    print("\n1.2 Required Fields Check:")
    required_fields = ['id', 'category', 'subcategory', 'question', 'options', 'correct_answer', 'difficulty', 'topic', 'subtopic']
    missing_fields_count = 0

    for i, q in enumerate(total_questions):
        missing = [f for f in required_fields if f not in q]
        if missing:
            missing_fields_count += 1
            if missing_fields_count <= 5:  # Show first 5
                issues.append(f"Question {i+1} (ID: {q.get('id', 'UNKNOWN')}) missing fields: {missing}")

    if missing_fields_count == 0:
        passed_checks.append("All required fields present")
        print(f"✅ PASS: All questions have required fields")
    else:
        failed_checks.append(f"Missing fields in {missing_fields_count} questions")
        print(f"❌ FAIL: {missing_fields_count} questions missing required fields")

    # 1.3 Pack metadata
    print("\n1.3 Pack Metadata:")
    metadata_fields = ['packId', 'packName', 'packDescription', 'subtopics', 'questionCount',
                       'freePreviewCount', 'difficulty', 'price', 'icon', 'isPublished', 'releaseDate']

    metadata_complete = True
    for field in metadata_fields:
        if field not in narnia_data:
            metadata_complete = False
            issues.append(f"Missing metadata field: {field}")
            print(f"❌ Missing: {field}")

    if metadata_complete:
        passed_checks.append("Pack metadata complete")
        print(f"✅ PASS: All metadata fields present")
    else:
        failed_checks.append("Incomplete pack metadata")

    print()

    # ========================================================================
    # 2. ID VALIDATION
    # ========================================================================
    print("2. ID VALIDATION")
    print("-" * 80)

    # 2.1 ID uniqueness
    all_ids = [q.get('id', '') for q in total_questions]
    id_counts = Counter(all_ids)
    duplicates = {id: count for id, count in id_counts.items() if count > 1}

    if not duplicates:
        passed_checks.append("All IDs unique")
        print(f"✅ PASS: All {len(all_ids)} IDs are unique")
    else:
        failed_checks.append(f"{len(duplicates)} duplicate IDs")
        print(f"❌ FAIL: Found {len(duplicates)} duplicate IDs:")
        for id, count in list(duplicates.items())[:10]:  # Show first 10
            print(f"  - {id}: {count} occurrences")
            issues.append(f"Duplicate ID: {id} ({count} times)")

    # 2.2 ID format validation
    print("\n2.2 ID Format Check:")
    id_pattern = re.compile(r'^nar_[a-z]+_\d{3}$')
    invalid_format_count = 0

    for q in total_questions:
        id = q.get('id', '')
        if not id_pattern.match(id):
            invalid_format_count += 1
            if invalid_format_count <= 5:  # Show first 5
                issues.append(f"Invalid ID format: {id}")

    if invalid_format_count == 0:
        passed_checks.append("All IDs follow correct format")
        print(f"✅ PASS: All IDs follow format nar_XXX_###")
    else:
        failed_checks.append(f"{invalid_format_count} IDs with wrong format")
        print(f"❌ FAIL: {invalid_format_count} IDs don't follow format nar_XXX_###")

    # 2.3 ID sequential check by subtopic
    print("\n2.3 ID Sequential Check by Subtopic:")
    subtopic_ids = defaultdict(list)
    for q in total_questions:
        subtopic = q.get('subtopic', 'UNKNOWN')
        id = q.get('id', '')
        if id:
            # Extract the number part
            match = re.search(r'_(\d{3})$', id)
            if match:
                subtopic_ids[subtopic].append((id, int(match.group(1))))

    sequential_issues = 0
    for subtopic, id_list in sorted(subtopic_ids.items()):
        id_list.sort(key=lambda x: x[1])
        numbers = [num for _, num in id_list]
        expected = list(range(1, len(numbers) + 1))
        if numbers != expected:
            sequential_issues += 1
            issues.append(f"Subtopic '{subtopic}' IDs not sequential: {numbers[:10]}...")

    if sequential_issues == 0:
        passed_checks.append("IDs sequential within subtopics")
        print(f"✅ PASS: IDs are sequential within each subtopic")
    else:
        failed_checks.append(f"{sequential_issues} subtopics with non-sequential IDs")
        print(f"❌ FAIL: {sequential_issues} subtopics have non-sequential IDs")

    print()

    # ========================================================================
    # 3. CONTENT QUALITY
    # ========================================================================
    print("3. CONTENT QUALITY")
    print("-" * 80)

    # 3.1 Options count
    wrong_options_count = 0
    for q in total_questions:
        options = q.get('options', [])
        if len(options) != 4:
            wrong_options_count += 1
            if wrong_options_count <= 5:
                issues.append(f"Question {q.get('id')} has {len(options)} options (expected 4)")

    if wrong_options_count == 0:
        passed_checks.append("All questions have 4 options")
        print(f"✅ PASS: All questions have exactly 4 options")
    else:
        failed_checks.append(f"{wrong_options_count} questions with wrong option count")
        print(f"❌ FAIL: {wrong_options_count} questions don't have 4 options")

    # 3.2 correct_answer field
    missing_answer_count = 0
    for q in total_questions:
        if 'correct_answer' not in q or not q['correct_answer']:
            missing_answer_count += 1
            if missing_answer_count <= 5:
                issues.append(f"Question {q.get('id')} missing correct_answer")

    if missing_answer_count == 0:
        passed_checks.append("All questions have correct_answer")
        print(f"✅ PASS: All questions have correct_answer field")
    else:
        failed_checks.append(f"{missing_answer_count} questions missing correct_answer")
        print(f"❌ FAIL: {missing_answer_count} questions missing correct_answer")

    # 3.3 correct_answer matches options
    mismatch_count = 0
    for q in total_questions:
        correct = q.get('correct_answer', '')
        options = q.get('options', [])
        if correct and correct not in options:
            mismatch_count += 1
            if mismatch_count <= 5:
                issues.append(f"Question {q.get('id')}: correct_answer '{correct}' not in options")

    if mismatch_count == 0:
        passed_checks.append("All correct_answers match options")
        print(f"✅ PASS: All correct_answers match one of the options")
    else:
        failed_checks.append(f"{mismatch_count} questions with mismatched answers")
        print(f"❌ FAIL: {mismatch_count} questions have correct_answer not in options")

    # 3.4 Duplicate question text
    print("\n3.4 Duplicate Question Text Check:")
    question_texts = [q.get('question', '').lower().strip() for q in total_questions]
    text_counts = Counter(question_texts)
    dup_texts = {text: count for text, count in text_counts.items() if count > 1 and text}

    if not dup_texts:
        passed_checks.append("No duplicate question text")
        print(f"✅ PASS: No duplicate question text found")
    else:
        failed_checks.append(f"{len(dup_texts)} duplicate question texts")
        print(f"❌ FAIL: Found {len(dup_texts)} duplicate question texts:")
        for text, count in list(dup_texts.items())[:5]:
            print(f"  - '{text[:60]}...' ({count} times)")
            issues.append(f"Duplicate question: {text[:60]}... ({count} times)")

    # 3.5 Prohibited content
    print("\n3.5 Prohibited Content Check:")
    prohibited_words = ['snake', 'snakes', 'spider', 'spiders']
    prohibited_found = []

    for q in total_questions:
        text = (q.get('question', '') + ' ' + ' '.join(q.get('options', []))).lower()
        for word in prohibited_words:
            if word in text:
                prohibited_found.append((q.get('id'), word))
                if len(prohibited_found) <= 5:
                    issues.append(f"Question {q.get('id')} contains prohibited word: {word}")

    if not prohibited_found:
        passed_checks.append("No prohibited content")
        print(f"✅ PASS: No prohibited content (snakes/spiders) found")
    else:
        failed_checks.append(f"{len(prohibited_found)} instances of prohibited content")
        print(f"❌ FAIL: Found {len(prohibited_found)} instances of prohibited content")

    # 3.6 Family-friendly check (basic profanity)
    print("\n3.6 Family-Friendly Language Check:")
    # Basic check for common profanity
    profanity_words = ['damn', 'hell', 'ass', 'crap', 'shit', 'fuck']
    profanity_found = []

    for q in total_questions:
        text = (q.get('question', '') + ' ' + ' '.join(q.get('options', []))).lower()
        for word in profanity_words:
            if word in text:
                profanity_found.append((q.get('id'), word))
                if len(profanity_found) <= 5:
                    issues.append(f"Question {q.get('id')} contains profanity: {word}")

    if not profanity_found:
        passed_checks.append("Family-friendly language")
        print(f"✅ PASS: No profanity detected")
    else:
        failed_checks.append(f"{len(profanity_found)} instances of profanity")
        print(f"❌ FAIL: Found {len(profanity_found)} instances of profanity")

    print()

    # ========================================================================
    # 4. DISTRIBUTION VALIDATION
    # ========================================================================
    print("4. DISTRIBUTION VALIDATION")
    print("-" * 80)

    # 4.1 Subtopic distribution
    print("4.1 Subtopic Distribution:")
    expected_distribution = {
        "The Lion, the Witch and the Wardrobe": 70,
        "Prince Caspian": 70,
        "The Voyage of the Dawn Treader": 65,
        "The Silver Chair": 65,
        "The Horse and His Boy": 65,
        "The Magician's Nephew": 65
    }

    subtopic_counts = Counter(q.get('subtopic', 'UNKNOWN') for q in total_questions)
    distribution_correct = True

    for subtopic, expected in expected_distribution.items():
        actual = subtopic_counts.get(subtopic, 0)
        if actual == expected:
            print(f"  ✅ {subtopic}: {actual} (expected {expected})")
        else:
            print(f"  ❌ {subtopic}: {actual} (expected {expected})")
            distribution_correct = False
            issues.append(f"Subtopic '{subtopic}' has {actual} questions (expected {expected})")

    # Check for unknown subtopics
    for subtopic, count in subtopic_counts.items():
        if subtopic not in expected_distribution:
            print(f"  ❌ Unknown subtopic: {subtopic} ({count} questions)")
            distribution_correct = False
            issues.append(f"Unknown subtopic: {subtopic}")

    if distribution_correct:
        passed_checks.append("Subtopic distribution correct")
    else:
        failed_checks.append("Subtopic distribution incorrect")

    # 4.2 Difficulty breakdown
    print("\n4.2 Difficulty Breakdown:")
    expected_difficulty = {
        "easy": 120,
        "medium": 190,
        "hard": 90
    }

    difficulty_counts = Counter(q.get('difficulty', 'UNKNOWN') for q in total_questions)
    difficulty_correct = True

    for diff, expected in expected_difficulty.items():
        actual = difficulty_counts.get(diff, 0)
        if actual == expected:
            print(f"  ✅ {diff.capitalize()}: {actual} (expected {expected})")
        else:
            print(f"  ❌ {diff.capitalize()}: {actual} (expected {expected})")
            difficulty_correct = False
            issues.append(f"Difficulty '{diff}' has {actual} questions (expected {expected})")

    if difficulty_correct:
        passed_checks.append("Difficulty distribution correct")
    else:
        failed_checks.append("Difficulty distribution incorrect")

    # 4.3 Free preview distribution
    print("\n4.3 Free Preview Distribution:")
    free_subtopics = Counter(q.get('subtopic', 'UNKNOWN') for q in free_questions)
    print(f"  Total free preview: {len(free_questions)}")
    for subtopic, count in sorted(free_subtopics.items()):
        print(f"    - {subtopic}: {count}")

    # Check if reasonably distributed (should be ~6-7 per subtopic)
    if len(free_subtopics) == 6 and all(5 <= count <= 8 for count in free_subtopics.values()):
        passed_checks.append("Free preview well distributed")
        print(f"  ✅ PASS: Free preview distributed across all subtopics")
    else:
        failed_checks.append("Free preview distribution uneven")
        print(f"  ⚠️  WARNING: Free preview distribution may be uneven")

    print()

    # ========================================================================
    # 5. METADATA VALIDATION
    # ========================================================================
    print("5. METADATA VALIDATION")
    print("-" * 80)

    # 5.1 questionCount
    metadata_qcount = narnia_data.get('questionCount', 0)
    if metadata_qcount == 400:
        passed_checks.append("Metadata questionCount correct")
        print(f"✅ PASS: questionCount = {metadata_qcount}")
    else:
        failed_checks.append(f"Metadata questionCount wrong: {metadata_qcount}")
        print(f"❌ FAIL: questionCount = {metadata_qcount} (expected 400)")
        issues.append(f"Metadata questionCount is {metadata_qcount}, should be 400")

    # 5.2 freePreviewCount
    metadata_free = narnia_data.get('freePreviewCount', 0)
    if metadata_free == 40:
        passed_checks.append("Metadata freePreviewCount correct")
        print(f"✅ PASS: freePreviewCount = {metadata_free}")
    else:
        failed_checks.append(f"Metadata freePreviewCount wrong: {metadata_free}")
        print(f"❌ FAIL: freePreviewCount = {metadata_free} (expected 40)")
        issues.append(f"Metadata freePreviewCount is {metadata_free}, should be 40")

    # 5.3 price
    price = narnia_data.get('price')
    if price == 2.99:
        passed_checks.append("Price correct (2.99)")
        print(f"✅ PASS: price = {price} (number)")
    elif price == "2.99":
        failed_checks.append("Price is string, should be number")
        print(f"❌ FAIL: price = '{price}' (string, should be number 2.99)")
        issues.append("Price field is a string, should be number 2.99")
    else:
        failed_checks.append(f"Price wrong: {price}")
        print(f"❌ FAIL: price = {price} (expected 2.99)")
        issues.append(f"Price is {price}, should be 2.99 for 400 questions")

    # 5.4 difficulty metadata
    print("\n5.4 Difficulty Metadata:")
    metadata_diff = narnia_data.get('difficulty', {})
    if metadata_diff == expected_difficulty:
        passed_checks.append("Difficulty metadata matches actual")
        print(f"✅ PASS: Difficulty metadata matches actual counts")
    else:
        failed_checks.append("Difficulty metadata mismatch")
        print(f"❌ FAIL: Difficulty metadata doesn't match:")
        print(f"  Metadata: {metadata_diff}")
        print(f"  Actual: {dict(difficulty_counts)}")
        issues.append(f"Difficulty metadata mismatch: {metadata_diff} vs actual {dict(difficulty_counts)}")

    # 5.5 subtopics list
    print("\n5.5 Subtopics List:")
    metadata_subtopics = narnia_data.get('subtopics', [])
    if len(metadata_subtopics) == 6:
        passed_checks.append("6 subtopics in metadata")
        print(f"✅ PASS: {len(metadata_subtopics)} subtopics listed")
        for st in metadata_subtopics:
            print(f"  - {st}")
    else:
        failed_checks.append(f"Wrong subtopic count: {len(metadata_subtopics)}")
        print(f"❌ FAIL: {len(metadata_subtopics)} subtopics (expected 6)")
        issues.append(f"Metadata has {len(metadata_subtopics)} subtopics, expected 6")

    # 5.6 Other metadata fields
    print("\n5.6 Other Metadata:")
    pack_id = narnia_data.get('packId', '')
    if pack_id == 'com.fiz.pack.narnia':
        passed_checks.append("PackId correct")
        print(f"✅ PASS: packId = {pack_id}")
    else:
        failed_checks.append(f"PackId wrong: {pack_id}")
        print(f"❌ FAIL: packId = {pack_id} (expected com.fiz.pack.narnia)")

    icon = narnia_data.get('icon', '')
    is_published = narnia_data.get('isPublished')
    release_date = narnia_data.get('releaseDate', '')

    print(f"  icon: {icon}")
    print(f"  isPublished: {is_published}")
    print(f"  releaseDate: {release_date}")

    print()

    # ========================================================================
    # 6. COMPARISON WITH OTHER PACKS
    # ========================================================================
    print("6. COMPARISON WITH OTHER PACKS")
    print("-" * 80)

    if harry_potter_data:
        # Compare structure
        hp_keys = set(harry_potter_data.keys())
        narnia_keys = set(narnia_data.keys())

        if hp_keys == narnia_keys:
            passed_checks.append("Pack structure matches Harry Potter")
            print(f"✅ PASS: Pack structure matches Harry Potter reference")
        else:
            missing_in_narnia = hp_keys - narnia_keys
            extra_in_narnia = narnia_keys - hp_keys
            if missing_in_narnia:
                failed_checks.append(f"Missing keys: {missing_in_narnia}")
                print(f"❌ FAIL: Missing keys: {missing_in_narnia}")
                issues.append(f"Missing metadata keys compared to HP: {missing_in_narnia}")
            if extra_in_narnia:
                print(f"ℹ️  Extra keys in Narnia: {extra_in_narnia}")

        # Check question field consistency
        if harry_potter_data.get('freePreviewQuestions'):
            hp_question = harry_potter_data['freePreviewQuestions'][0]
            narnia_question = total_questions[0] if total_questions else {}

            hp_fields = set(hp_question.keys())
            narnia_fields = set(narnia_question.keys())

            if hp_fields == narnia_fields:
                passed_checks.append("Question fields match Harry Potter")
                print(f"✅ PASS: Question fields consistent with Harry Potter")
            else:
                print(f"⚠️  WARNING: Question fields differ from Harry Potter")
                print(f"  Missing: {hp_fields - narnia_fields}")
                print(f"  Extra: {narnia_fields - hp_fields}")
    else:
        print("⚠️  WARNING: Could not load Harry Potter pack for comparison")

    # Pricing validation
    print("\n6.1 Pricing Validation:")
    if price == 2.99 and actual_total == 400:
        passed_checks.append("Pricing appropriate for question count")
        print(f"✅ PASS: $2.99 is appropriate for 400 questions (300-400q range)")
    else:
        print(f"⚠️  Review pricing: ${price} for {actual_total} questions")

    print()

    # ========================================================================
    # FINAL REPORT
    # ========================================================================
    print("=" * 80)
    print("AUDIT SUMMARY")
    print("=" * 80)
    print()

    total_checks = len(passed_checks) + len(failed_checks)
    pass_rate = (len(passed_checks) / total_checks * 100) if total_checks > 0 else 0

    print(f"Total Checks: {total_checks}")
    print(f"Passed: {len(passed_checks)} ✅")
    print(f"Failed: {len(failed_checks)} ❌")
    print(f"Score: {pass_rate:.1f}%")
    print()

    if failed_checks:
        print("FAILED CHECKS:")
        print("-" * 80)
        for check in failed_checks:
            print(f"  ❌ {check}")
        print()

    if issues:
        print("ISSUES FOUND:")
        print("-" * 80)
        for i, issue in enumerate(issues[:20], 1):  # Show first 20
            print(f"{i}. {issue}")
        if len(issues) > 20:
            print(f"... and {len(issues) - 20} more issues")
        print()

    # Recommendations
    print("RECOMMENDATIONS:")
    print("-" * 80)

    if failed_checks:
        print("Critical fixes needed:")
        if any("duplicate" in check.lower() for check in failed_checks):
            print("  - Remove duplicate IDs and question text")
        if any("format" in check.lower() for check in failed_checks):
            print("  - Fix ID formatting to match nar_XXX_### pattern")
        if any("distribution" in check.lower() for check in failed_checks):
            print("  - Rebalance question distribution across subtopics/difficulties")
        if any("metadata" in check.lower() for check in failed_checks):
            print("  - Update pack metadata to match actual counts")
        if any("answer" in check.lower() for check in failed_checks):
            print("  - Fix correct_answer mismatches with options")
        if any("options" in check.lower() for check in failed_checks):
            print("  - Ensure all questions have exactly 4 options")
    else:
        print("  ✅ No critical issues found!")

    print()

    # Final verdict
    print("=" * 80)
    print("FINAL VERDICT")
    print("=" * 80)

    critical_failures = [
        check for check in failed_checks
        if any(keyword in check.lower() for keyword in ['duplicate', 'missing', 'mismatch', 'total question count'])
    ]

    if not failed_checks:
        print("✅ LAUNCH READY")
        print("\nThe Narnia expansion pack passes all quality checks and is ready for launch!")
    elif not critical_failures and pass_rate >= 90:
        print("⚠️  LAUNCH READY (with minor warnings)")
        print("\nThe pack is functionally ready but has minor issues that should be addressed in future updates.")
    else:
        print("❌ NEEDS FIXES")
        print(f"\nThe pack has {len(failed_checks)} failed checks that must be addressed before launch.")
        print("Focus on critical issues first, then address warnings.")

    print("=" * 80)

if __name__ == "__main__":
    audit_narnia_pack()
