#!/usr/bin/env python3
"""
Comprehensive audit script for Mario "Italian Brothers Plumbing" expansion pack
"""

import json
import sys
from collections import Counter, defaultdict
from datetime import datetime

def load_json(filepath):
    """Load and parse JSON file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ CRITICAL ERROR: Failed to load JSON: {e}")
        sys.exit(1)

def validate_structure(data):
    """Validate basic structure and question counts"""
    results = []
    passed = 0
    failed = 0

    # Check metadata fields
    required_meta = ['packId', 'packName', 'packDescription', 'subtopics', 'subtopicIcons',
                     'questionCount', 'freePreviewCount', 'difficulty', 'price', 'icon',
                     'isPublished', 'releaseDate', 'freePreviewQuestions', 'paidQuestions']

    missing_fields = [f for f in required_meta if f not in data]
    if missing_fields:
        results.append(f"❌ Missing metadata fields: {', '.join(missing_fields)}")
        failed += 1
    else:
        results.append("✅ All required metadata fields present")
        passed += 1

    # Check question counts
    free_count = len(data.get('freePreviewQuestions', []))
    paid_count = len(data.get('paidQuestions', []))
    total_count = free_count + paid_count

    if free_count == 50:
        results.append(f"✅ Free preview questions: {free_count} (correct)")
        passed += 1
    else:
        results.append(f"❌ Free preview questions: {free_count} (expected 50)")
        failed += 1

    if paid_count == 450:
        results.append(f"✅ Paid questions: {paid_count} (correct)")
        passed += 1
    else:
        results.append(f"❌ Paid questions: {paid_count} (expected 450)")
        failed += 1

    if total_count == 500:
        results.append(f"✅ Total questions: {total_count} (correct)")
        passed += 1
    else:
        results.append(f"❌ Total questions: {total_count} (expected 500)")
        failed += 1

    # Check metadata counts match
    if data.get('questionCount') == 500:
        results.append(f"✅ Metadata questionCount: {data['questionCount']} (correct)")
        passed += 1
    else:
        results.append(f"❌ Metadata questionCount: {data.get('questionCount')} (expected 500)")
        failed += 1

    if data.get('freePreviewCount') == 50:
        results.append(f"✅ Metadata freePreviewCount: {data['freePreviewCount']} (correct)")
        passed += 1
    else:
        results.append(f"❌ Metadata freePreviewCount: {data.get('freePreviewCount')} (expected 50)")
        failed += 1

    return results, passed, failed

def validate_ids(data):
    """Validate question IDs"""
    results = []
    passed = 0
    failed = 0
    issues = []

    all_questions = data.get('freePreviewQuestions', []) + data.get('paidQuestions', [])
    all_ids = [q.get('id') for q in all_questions]

    # Check for duplicates
    id_counts = Counter(all_ids)
    duplicates = [id for id, count in id_counts.items() if count > 1]

    if duplicates:
        results.append(f"❌ Duplicate IDs found: {len(duplicates)} duplicates")
        for dup_id in duplicates:
            issues.append(f"  - {dup_id} appears {id_counts[dup_id]} times")
        failed += 1
    else:
        results.append(f"✅ All {len(all_ids)} IDs are unique")
        passed += 1

    # Check ID format (mar_XXX_###)
    invalid_format = []
    for q in all_questions:
        qid = q.get('id', '')
        if not qid.startswith('mar_'):
            invalid_format.append(f"{qid} - doesn't start with 'mar_'")
        elif '_' not in qid[4:]:
            invalid_format.append(f"{qid} - missing subtopic separator")

    if invalid_format:
        results.append(f"❌ Invalid ID format: {len(invalid_format)} issues")
        issues.extend([f"  - {issue}" for issue in invalid_format[:10]])
        if len(invalid_format) > 10:
            issues.append(f"  ... and {len(invalid_format) - 10} more")
        failed += 1
    else:
        results.append(f"✅ All IDs follow correct format (mar_XXX_###)")
        passed += 1

    # Check subtopic ID groupings
    subtopic_prefixes = {
        'Characters': 'mar_char_',
        'Games & Gameplay': 'mar_game_',
        'Power-ups & Items': 'mar_pow_',  # Using 'pow' abbreviation
        'Locations & Worlds': 'mar_loc_',
        'Enemies & Bosses': 'mar_ene_',  # Using 'ene' abbreviation
        'Music & Sound': 'mar_mus_',
        'Trivia & History': 'mar_tri_'  # Using 'tri' abbreviation
    }

    subtopic_mismatches = []
    for q in all_questions:
        qid = q.get('id', '')
        subtopic = q.get('subtopic', '')
        expected_prefix = subtopic_prefixes.get(subtopic, '')

        if expected_prefix and not qid.startswith(expected_prefix):
            subtopic_mismatches.append(f"{qid} - has subtopic '{subtopic}' but doesn't match prefix {expected_prefix}")

    if subtopic_mismatches:
        results.append(f"❌ ID/subtopic mismatches: {len(subtopic_mismatches)} issues")
        issues.extend([f"  - {issue}" for issue in subtopic_mismatches[:10]])
        if len(subtopic_mismatches) > 10:
            issues.append(f"  ... and {len(subtopic_mismatches) - 10} more")
        failed += 1
    else:
        results.append(f"✅ All IDs match their subtopic prefixes")
        passed += 1

    return results, passed, failed, issues

def validate_content(data):
    """Validate question content quality"""
    results = []
    passed = 0
    failed = 0
    issues = []

    all_questions = data.get('freePreviewQuestions', []) + data.get('paidQuestions', [])

    # Check required fields in each question
    required_fields = ['id', 'category', 'subcategory', 'question', 'options',
                      'correct_answer', 'difficulty', 'topic', 'subtopic']

    missing_fields_count = 0
    for i, q in enumerate(all_questions):
        missing = [f for f in required_fields if f not in q]
        if missing:
            missing_fields_count += 1
            if missing_fields_count <= 5:
                issues.append(f"  - Question {i+1} ({q.get('id', 'NO_ID')}): missing {', '.join(missing)}")

    if missing_fields_count > 0:
        results.append(f"❌ Questions with missing fields: {missing_fields_count}")
        if missing_fields_count > 5:
            issues.append(f"  ... and {missing_fields_count - 5} more questions")
        failed += 1
    else:
        results.append(f"✅ All questions have required fields")
        passed += 1

    # Check options count (must be exactly 4)
    invalid_options = []
    for q in all_questions:
        options = q.get('options', [])
        if len(options) != 4:
            invalid_options.append(f"{q.get('id')} - has {len(options)} options")

    if invalid_options:
        results.append(f"❌ Questions with != 4 options: {len(invalid_options)}")
        issues.extend([f"  - {issue}" for issue in invalid_options[:10]])
        if len(invalid_options) > 10:
            issues.append(f"  ... and {len(invalid_options) - 10} more")
        failed += 1
    else:
        results.append(f"✅ All questions have exactly 4 options")
        passed += 1

    # Check correct_answer matches an option
    mismatched_answers = []
    for q in all_questions:
        correct = q.get('correct_answer')
        options = q.get('options', [])
        if correct not in options:
            mismatched_answers.append(f"{q.get('id')} - correct_answer '{correct}' not in options")

    if mismatched_answers:
        results.append(f"❌ Correct answer mismatches: {len(mismatched_answers)}")
        issues.extend([f"  - {issue}" for issue in mismatched_answers[:10]])
        if len(mismatched_answers) > 10:
            issues.append(f"  ... and {len(mismatched_answers) - 10} more")
        failed += 1
    else:
        results.append(f"✅ All correct_answers match their options")
        passed += 1

    # Check for duplicate question text
    question_texts = [q.get('question', '').strip().lower() for q in all_questions]
    text_counts = Counter(question_texts)
    duplicates = [text for text, count in text_counts.items() if count > 1 and text]

    if duplicates:
        results.append(f"❌ Duplicate question texts: {len(duplicates)}")
        for dup_text in duplicates[:5]:
            matching_ids = [q.get('id') for q in all_questions if q.get('question', '').strip().lower() == dup_text]
            issues.append(f"  - '{dup_text[:60]}...' appears in: {', '.join(matching_ids)}")
        if len(duplicates) > 5:
            issues.append(f"  ... and {len(duplicates) - 5} more duplicates")
        failed += 1
    else:
        results.append(f"✅ No duplicate question texts found")
        passed += 1

    # Check for prohibited content (snakes, spiders)
    prohibited_terms = ['snake', 'spider', 'serpent', 'arachnid']
    prohibited_found = []
    for q in all_questions:
        question_lower = q.get('question', '').lower()
        options_lower = ' '.join(q.get('options', [])).lower()
        full_text = question_lower + ' ' + options_lower

        for term in prohibited_terms:
            if term in full_text:
                prohibited_found.append(f"{q.get('id')} - contains '{term}'")

    if prohibited_found:
        results.append(f"❌ Prohibited content found: {len(prohibited_found)} instances")
        issues.extend([f"  - {issue}" for issue in prohibited_found[:10]])
        if len(prohibited_found) > 10:
            issues.append(f"  ... and {len(prohibited_found) - 10} more")
        failed += 1
    else:
        results.append(f"✅ No prohibited content (snakes, spiders) found")
        passed += 1

    # Check topic field consistency
    wrong_topic = []
    for q in all_questions:
        topic = q.get('topic')
        if topic != 'com.fiz.pack.mario':
            wrong_topic.append(f"{q.get('id')} - has topic '{topic}'")

    if wrong_topic:
        results.append(f"❌ Wrong topic field: {len(wrong_topic)} questions")
        issues.extend([f"  - {issue}" for issue in wrong_topic[:10]])
        if len(wrong_topic) > 10:
            issues.append(f"  ... and {len(wrong_topic) - 10} more")
        failed += 1
    else:
        results.append(f"✅ All questions have correct topic field")
        passed += 1

    return results, passed, failed, issues

def validate_distribution(data):
    """Validate subtopic and difficulty distribution"""
    results = []
    passed = 0
    failed = 0
    issues = []

    all_questions = data.get('freePreviewQuestions', []) + data.get('paidQuestions', [])
    free_questions = data.get('freePreviewQuestions', [])

    # Subtopic distribution (7 subtopics: 70, 70, 70, 75, 75, 70, 70 = 500)
    expected_distribution = {
        'Characters': 70,
        'Games & Gameplay': 70,
        'Power-ups & Items': 70,
        'Locations & Worlds': 75,
        'Enemies & Bosses': 75,
        'Music & Sound': 70,
        'Trivia & History': 70
    }

    subtopic_counts = Counter(q.get('subtopic') for q in all_questions)

    distribution_correct = True
    for subtopic, expected in expected_distribution.items():
        actual = subtopic_counts.get(subtopic, 0)
        if actual != expected:
            distribution_correct = False
            issues.append(f"  - {subtopic}: {actual} questions (expected {expected})")

    if distribution_correct:
        results.append(f"✅ Subtopic distribution correct (70,70,70,75,75,70,70)")
        passed += 1
    else:
        results.append(f"❌ Subtopic distribution incorrect:")
        failed += 1

    # Show actual distribution
    results.append(f"   Actual distribution:")
    for subtopic in expected_distribution.keys():
        count = subtopic_counts.get(subtopic, 0)
        results.append(f"   - {subtopic}: {count}")

    # Difficulty distribution (easy ~150, medium ~250, hard ~100)
    difficulty_counts = Counter(q.get('difficulty') for q in all_questions)

    easy_count = difficulty_counts.get('easy', 0)
    medium_count = difficulty_counts.get('medium', 0)
    hard_count = difficulty_counts.get('hard', 0)

    results.append(f"   Difficulty distribution:")
    results.append(f"   - Easy: {easy_count} (target ~150)")
    results.append(f"   - Medium: {medium_count} (target ~250)")
    results.append(f"   - Hard: {hard_count} (target ~100)")

    # Check if within reasonable range (±20)
    difficulty_ok = (130 <= easy_count <= 170 and
                    230 <= medium_count <= 270 and
                    80 <= hard_count <= 120)

    if difficulty_ok:
        results.append(f"✅ Difficulty distribution within acceptable range")
        passed += 1
    else:
        results.append(f"❌ Difficulty distribution outside acceptable range")
        failed += 1

    # Check metadata difficulty matches actual
    meta_difficulty = data.get('difficulty', {})
    meta_easy = meta_difficulty.get('easy', 0)
    meta_medium = meta_difficulty.get('medium', 0)
    meta_hard = meta_difficulty.get('hard', 0)

    if (meta_easy == easy_count and meta_medium == medium_count and meta_hard == hard_count):
        results.append(f"✅ Metadata difficulty counts match actual counts")
        passed += 1
    else:
        results.append(f"❌ Metadata difficulty mismatch:")
        issues.append(f"  - Metadata: easy={meta_easy}, medium={meta_medium}, hard={meta_hard}")
        issues.append(f"  - Actual: easy={easy_count}, medium={medium_count}, hard={hard_count}")
        failed += 1

    # Free preview distribution (7-8 per subtopic, all easy)
    free_subtopics = Counter(q.get('subtopic') for q in free_questions)
    free_difficulties = Counter(q.get('difficulty') for q in free_questions)

    results.append(f"   Free preview by subtopic:")
    free_distribution_ok = True
    for subtopic in expected_distribution.keys():
        count = free_subtopics.get(subtopic, 0)
        results.append(f"   - {subtopic}: {count} (target 7-8)")
        if count < 7 or count > 8:
            free_distribution_ok = False

    if free_distribution_ok:
        results.append(f"✅ Free preview subtopic distribution correct (7-8 each)")
        passed += 1
    else:
        results.append(f"❌ Free preview subtopic distribution incorrect")
        failed += 1

    # Check all free previews are easy
    non_easy_free = [q.get('id') for q in free_questions if q.get('difficulty') != 'easy']
    if non_easy_free:
        results.append(f"❌ Free preview has {len(non_easy_free)} non-easy questions:")
        issues.extend([f"  - {qid}" for qid in non_easy_free[:10]])
        if len(non_easy_free) > 10:
            issues.append(f"  ... and {len(non_easy_free) - 10} more")
        failed += 1
    else:
        results.append(f"✅ All free preview questions are easy difficulty")
        passed += 1

    return results, passed, failed, issues

def validate_metadata(data):
    """Validate pack metadata"""
    results = []
    passed = 0
    failed = 0
    issues = []

    # Check packId
    if data.get('packId') == 'com.fiz.pack.mario':
        results.append(f"✅ packId correct: {data['packId']}")
        passed += 1
    else:
        results.append(f"❌ packId incorrect: {data.get('packId')} (expected com.fiz.pack.mario)")
        failed += 1

    # Check price (should be 0.99 as number for 500 questions)
    price = data.get('price')
    if isinstance(price, (int, float)) and price == 0.99:
        results.append(f"✅ Price correct: ${price} (number type)")
        passed += 1
    elif isinstance(price, str):
        results.append(f"❌ Price is string: '{price}' (should be number 0.99)")
        failed += 1
    else:
        results.append(f"❌ Price incorrect: {price} (expected 0.99)")
        failed += 1

    # Check subtopics list
    expected_subtopics = ['Characters', 'Games & Gameplay', 'Power-ups & Items',
                         'Locations & Worlds', 'Enemies & Bosses', 'Music & Sound',
                         'Trivia & History']
    actual_subtopics = data.get('subtopics', [])

    if actual_subtopics == expected_subtopics:
        results.append(f"✅ All 7 subtopics listed correctly")
        passed += 1
    else:
        results.append(f"❌ Subtopics list incorrect")
        issues.append(f"  - Expected: {expected_subtopics}")
        issues.append(f"  - Actual: {actual_subtopics}")
        failed += 1

    # Check subtopicIcons
    subtopic_icons = data.get('subtopicIcons', {})
    if len(subtopic_icons) == 7:
        results.append(f"✅ Icons present for all 7 subtopics")
        passed += 1
    else:
        results.append(f"❌ Icons present for {len(subtopic_icons)} subtopics (expected 7)")
        missing_icons = [s for s in expected_subtopics if s not in subtopic_icons]
        if missing_icons:
            issues.append(f"  - Missing icons for: {', '.join(missing_icons)}")
        failed += 1

    # Check other required fields
    if 'icon' in data:
        results.append(f"✅ Pack icon present: {data['icon']}")
        passed += 1
    else:
        results.append(f"❌ Pack icon missing")
        failed += 1

    if 'isPublished' in data:
        results.append(f"✅ isPublished field present: {data['isPublished']}")
        passed += 1
    else:
        results.append(f"❌ isPublished field missing")
        failed += 1

    if 'releaseDate' in data:
        results.append(f"✅ releaseDate field present: {data['releaseDate']}")
        passed += 1
    else:
        results.append(f"❌ releaseDate field missing")
        failed += 1

    return results, passed, failed, issues

def generate_report(data, output_file):
    """Generate comprehensive audit report"""

    report_lines = []
    report_lines.append("# Mario \"Italian Brothers Plumbing\" Expansion Pack - Audit Report")
    report_lines.append(f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append(f"**Pack:** {data.get('packName', 'Unknown')}")
    report_lines.append(f"**Pack ID:** {data.get('packId', 'Unknown')}")
    report_lines.append("\n---\n")

    total_passed = 0
    total_failed = 0
    all_issues = []

    # 1. Structural Validation
    report_lines.append("## 1. Structural Validation\n")
    results, passed, failed = validate_structure(data)
    report_lines.extend(results)
    total_passed += passed
    total_failed += failed
    report_lines.append("")

    # 2. ID Validation
    report_lines.append("## 2. ID Validation\n")
    results, passed, failed, issues = validate_ids(data)
    report_lines.extend(results)
    if issues:
        all_issues.extend(issues)
    total_passed += passed
    total_failed += failed
    report_lines.append("")

    # 3. Content Quality
    report_lines.append("## 3. Content Quality\n")
    results, passed, failed, issues = validate_content(data)
    report_lines.extend(results)
    if issues:
        all_issues.extend(issues)
    total_passed += passed
    total_failed += failed
    report_lines.append("")

    # 4. Distribution Validation
    report_lines.append("## 4. Distribution Validation\n")
    results, passed, failed, issues = validate_distribution(data)
    report_lines.extend(results)
    if issues:
        all_issues.extend(issues)
    total_passed += passed
    total_failed += failed
    report_lines.append("")

    # 5. Metadata Validation
    report_lines.append("## 5. Metadata Validation\n")
    results, passed, failed, issues = validate_metadata(data)
    report_lines.extend(results)
    if issues:
        all_issues.extend(issues)
    total_passed += passed
    total_failed += failed
    report_lines.append("")

    # Summary
    total_checks = total_passed + total_failed
    score = (total_passed / total_checks * 100) if total_checks > 0 else 0

    report_lines.append("---\n")
    report_lines.append("## Summary\n")
    report_lines.append(f"**Total Checks:** {total_checks}")
    report_lines.append(f"**Passed:** ✅ {total_passed}")
    report_lines.append(f"**Failed:** ❌ {total_failed}")
    report_lines.append(f"**Score:** {score:.1f}%")
    report_lines.append("")

    # Issues
    if all_issues:
        report_lines.append("## Issues Found\n")
        report_lines.extend(all_issues)
        report_lines.append("")

    # Recommendations
    report_lines.append("## Recommendations\n")
    if total_failed == 0:
        report_lines.append("✅ No issues found! Pack is ready for launch.")
    else:
        report_lines.append("The following issues should be addressed before launch:")
        if total_failed > 0:
            report_lines.append(f"- {total_failed} validation checks failed")
        if all_issues:
            report_lines.append(f"- {len(all_issues)} specific issues documented above")
    report_lines.append("")

    # Final Verdict
    report_lines.append("## Final Verdict\n")
    if score >= 95 and total_failed <= 2:
        report_lines.append("**Status:** 🟢 LAUNCH READY")
        report_lines.append("\nThe pack meets all critical requirements with minor or no issues.")
    elif score >= 85:
        report_lines.append("**Status:** 🟡 NEEDS MINOR FIXES")
        report_lines.append("\nThe pack has some issues that should be fixed before launch.")
    else:
        report_lines.append("**Status:** 🔴 NEEDS MAJOR FIXES")
        report_lines.append("\nThe pack has significant issues that must be fixed before launch.")

    # Write report
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))

    print(f"\n✅ Audit report generated: {output_file}")
    print(f"Score: {score:.1f}% ({total_passed}/{total_checks} checks passed)")

    return score >= 95 and total_failed <= 2

def main():
    mario_pack_path = '/home/user/fiztrivia/Fiz/Resources/Expansion Packs/expansion_mario.json'
    output_path = '/home/user/fiztrivia/MARIO_AUDIT_REPORT.md'

    print("🔍 Starting Mario Expansion Pack Audit...")
    print(f"Reading: {mario_pack_path}")

    data = load_json(mario_pack_path)
    print(f"✅ JSON loaded successfully")

    print("📊 Running validation checks...")
    success = generate_report(data, output_path)

    if success:
        print("\n🎉 AUDIT PASSED - Pack is launch ready!")
        return 0
    else:
        print("\n⚠️  AUDIT FAILED - Issues need to be fixed")
        return 1

if __name__ == '__main__':
    sys.exit(main())
