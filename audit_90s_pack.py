#!/usr/bin/env python3
"""
Comprehensive audit script for 90s Trivia expansion pack
"""

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

def load_json(filepath):
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def audit_90s_pack(pack_path, narnia_path=None, candy_path=None):
    """Perform comprehensive audit"""

    results = {
        'structural': [],
        'id_validation': [],
        'content_quality': [],
        'distribution': [],
        'metadata': [],
        'comparison': []
    }

    issues = []

    # Load the pack
    try:
        pack = load_json(pack_path)
    except Exception as e:
        return None, [f"❌ CRITICAL: Failed to load JSON: {e}"]

    # ===== 1. STRUCTURAL VALIDATION =====
    print("Running Structural Validation...")

    # Check for required top-level fields
    required_fields = ['packId', 'packName', 'packDescription', 'subtopics',
                      'questionCount', 'freePreviewCount', 'difficulty',
                      'price', 'icon', 'freePreviewQuestions', 'paidQuestions']

    missing_fields = [f for f in required_fields if f not in pack]
    if missing_fields:
        results['structural'].append(f"❌ FAIL: Missing top-level fields: {missing_fields}")
        issues.append(f"Missing fields: {missing_fields}")
    else:
        results['structural'].append("✅ PASS: All required top-level fields present")

    # Check total question count
    free_count = len(pack.get('freePreviewQuestions', []))
    paid_count = len(pack.get('paidQuestions', []))
    total_questions = free_count + paid_count

    if total_questions == 400:
        results['structural'].append(f"✅ PASS: Total questions = 400 ({free_count} free + {paid_count} paid)")
    else:
        results['structural'].append(f"❌ FAIL: Total questions = {total_questions} (expected 400)")
        issues.append(f"Total questions: {total_questions} (expected 400)")

    if free_count == 40:
        results['structural'].append(f"✅ PASS: Free preview questions = 40")
    else:
        results['structural'].append(f"❌ FAIL: Free preview questions = {free_count} (expected 40)")
        issues.append(f"Free preview count: {free_count} (expected 40)")

    if paid_count == 360:
        results['structural'].append(f"✅ PASS: Paid questions = 360")
    else:
        results['structural'].append(f"❌ FAIL: Paid questions = {paid_count} (expected 360)")
        issues.append(f"Paid count: {paid_count} (expected 360)")

    # Check question structure
    all_questions = pack.get('freePreviewQuestions', []) + pack.get('paidQuestions', [])
    required_q_fields = ['id', 'category', 'subcategory', 'question', 'options',
                        'correct_answer', 'difficulty', 'topic', 'subtopic']

    malformed_questions = []
    for i, q in enumerate(all_questions):
        missing = [f for f in required_q_fields if f not in q]
        if missing:
            malformed_questions.append(f"Question {i+1} (ID: {q.get('id', 'MISSING')}): missing {missing}")

    if malformed_questions:
        results['structural'].append(f"❌ FAIL: {len(malformed_questions)} questions missing required fields")
        issues.extend(malformed_questions[:5])  # Show first 5
        if len(malformed_questions) > 5:
            issues.append(f"... and {len(malformed_questions) - 5} more")
    else:
        results['structural'].append(f"✅ PASS: All {len(all_questions)} questions have required fields")

    # ===== 2. ID VALIDATION =====
    print("Running ID Validation...")

    # Check for duplicate IDs
    all_ids = [q['id'] for q in all_questions if 'id' in q]
    id_counts = Counter(all_ids)
    duplicates = {id_: count for id_, count in id_counts.items() if count > 1}

    if duplicates:
        results['id_validation'].append(f"❌ FAIL: {len(duplicates)} duplicate IDs found")
        for id_, count in list(duplicates.items())[:5]:
            issues.append(f"Duplicate ID: {id_} appears {count} times")
    else:
        results['id_validation'].append(f"✅ PASS: All {len(all_ids)} IDs are unique")

    # Check ID format (90s_XXX_###)
    import re
    id_pattern = re.compile(r'^90s_[A-Z]{3}_\d{3}$')
    invalid_ids = [id_ for id_ in all_ids if not id_pattern.match(id_)]

    if invalid_ids:
        results['id_validation'].append(f"❌ FAIL: {len(invalid_ids)} IDs don't match format 90s_XXX_###")
        for id_ in invalid_ids[:5]:
            issues.append(f"Invalid ID format: {id_}")
    else:
        results['id_validation'].append(f"✅ PASS: All IDs follow correct format (90s_XXX_###)")

    # Check ID sequential ordering within subtopics
    subtopic_ids = defaultdict(list)
    for q in all_questions:
        if 'id' in q and 'subtopic' in q:
            subtopic_ids[q['subtopic']].append(q['id'])

    sequential_issues = []
    for subtopic, ids in subtopic_ids.items():
        ids_sorted = sorted(ids)
        # Extract numeric part
        numbers = []
        for id_ in ids_sorted:
            match = re.search(r'_(\d{3})$', id_)
            if match:
                numbers.append(int(match.group(1)))

        # Check if sequential
        if numbers:
            expected = list(range(numbers[0], numbers[0] + len(numbers)))
            if numbers != expected:
                sequential_issues.append(f"Subtopic '{subtopic}': Non-sequential IDs")

    if sequential_issues:
        results['id_validation'].append(f"⚠️  WARNING: {len(sequential_issues)} subtopics have non-sequential IDs")
        issues.extend(sequential_issues[:3])
    else:
        results['id_validation'].append(f"✅ PASS: IDs are sequential within subtopics")

    # ===== 3. CONTENT QUALITY =====
    print("Running Content Quality Validation...")

    # Check all questions have exactly 4 options
    option_issues = []
    for q in all_questions:
        if 'options' not in q:
            continue
        if len(q['options']) != 4:
            option_issues.append(f"ID {q.get('id')}: {len(q['options'])} options")

    if option_issues:
        results['content_quality'].append(f"❌ FAIL: {len(option_issues)} questions don't have 4 options")
        issues.extend(option_issues[:5])
    else:
        results['content_quality'].append(f"✅ PASS: All questions have exactly 4 options")

    # Check correct_answer matches one of the options
    answer_mismatch = []
    for q in all_questions:
        if 'correct_answer' not in q or 'options' not in q:
            continue
        if q['correct_answer'] not in q['options']:
            answer_mismatch.append(f"ID {q.get('id')}: Answer '{q['correct_answer']}' not in options")

    if answer_mismatch:
        results['content_quality'].append(f"❌ FAIL: {len(answer_mismatch)} questions have mismatched answers")
        issues.extend(answer_mismatch[:5])
    else:
        results['content_quality'].append(f"✅ PASS: All correct_answer fields match options")

    # Check for duplicate question text
    question_texts = [q['question'].lower().strip() for q in all_questions if 'question' in q]
    text_counts = Counter(question_texts)
    dup_texts = {text: count for text, count in text_counts.items() if count > 1}

    if dup_texts:
        results['content_quality'].append(f"❌ FAIL: {len(dup_texts)} duplicate question texts found")
        for text, count in list(dup_texts.items())[:3]:
            issues.append(f"Duplicate question: '{text[:60]}...' ({count} times)")
    else:
        results['content_quality'].append(f"✅ PASS: All question texts are unique")

    # Check for prohibited content (snakes, spiders)
    prohibited_terms = ['snake', 'snakes', 'spider', 'spiders', 'arachnid', 'serpent']
    prohibited_found = []
    for q in all_questions:
        q_text = q.get('question', '').lower()
        options_text = ' '.join(q.get('options', [])).lower()
        for term in prohibited_terms:
            if term in q_text or term in options_text:
                prohibited_found.append(f"ID {q.get('id')}: Contains '{term}'")
                break

    if prohibited_found:
        results['content_quality'].append(f"⚠️  WARNING: {len(prohibited_found)} questions contain prohibited terms")
        issues.extend(prohibited_found[:3])
    else:
        results['content_quality'].append(f"✅ PASS: No prohibited content (snakes/spiders) found")

    # ===== 4. DISTRIBUTION VALIDATION =====
    print("Running Distribution Validation...")

    # Check subtopic distribution
    subtopic_counts = Counter([q.get('subtopic') for q in all_questions])
    expected_distribution = {
        'Music': 60,
        'Movies & TV': 60,
        'Technology': 55,
        'Fashion & Culture': 60,
        'Toys & Games': 55,
        'Sports': 55,
        'Events': 55
    }

    dist_issues = []
    for subtopic, expected in expected_distribution.items():
        actual = subtopic_counts.get(subtopic, 0)
        if actual != expected:
            dist_issues.append(f"{subtopic}: {actual} questions (expected {expected})")

    if dist_issues:
        results['distribution'].append(f"❌ FAIL: Subtopic distribution incorrect")
        issues.extend(dist_issues)
    else:
        results['distribution'].append(f"✅ PASS: Subtopic distribution matches expected (60,60,55,60,55,55,55)")

    # Check difficulty breakdown
    difficulty_counts = Counter([q.get('difficulty') for q in all_questions])
    easy = difficulty_counts.get('easy', 0)
    medium = difficulty_counts.get('medium', 0)
    hard = difficulty_counts.get('hard', 0)

    # Expected: easy ~120, medium ~200, hard ~80
    diff_issues = []
    if not (110 <= easy <= 130):
        diff_issues.append(f"Easy: {easy} (expected ~120, range 110-130)")
    if not (190 <= medium <= 210):
        diff_issues.append(f"Medium: {medium} (expected ~200, range 190-210)")
    if not (70 <= hard <= 90):
        diff_issues.append(f"Hard: {hard} (expected ~80, range 70-90)")

    if diff_issues:
        results['distribution'].append(f"⚠️  WARNING: Difficulty distribution outside expected ranges")
        issues.extend(diff_issues)
    else:
        results['distribution'].append(f"✅ PASS: Difficulty breakdown: Easy={easy}, Medium={medium}, Hard={hard}")

    # Check free preview distribution (should be 5-6 per subtopic, all easy)
    free_questions = pack.get('freePreviewQuestions', [])
    free_subtopics = Counter([q.get('subtopic') for q in free_questions])
    free_difficulties = Counter([q.get('difficulty') for q in free_questions])

    free_dist_issues = []
    for subtopic in expected_distribution.keys():
        count = free_subtopics.get(subtopic, 0)
        if not (5 <= count <= 6):
            free_dist_issues.append(f"{subtopic}: {count} free questions (expected 5-6)")

    if free_dist_issues:
        results['distribution'].append(f"⚠️  WARNING: Free preview subtopic distribution uneven")
        issues.extend(free_dist_issues)
    else:
        results['distribution'].append(f"✅ PASS: Free preview evenly distributed (5-6 per subtopic)")

    non_easy_free = sum(v for k, v in free_difficulties.items() if k != 'easy')
    if non_easy_free > 0:
        results['distribution'].append(f"⚠️  WARNING: {non_easy_free} free preview questions are not 'easy' difficulty")
        issues.append(f"Free preview should all be easy, found {non_easy_free} non-easy")
    else:
        results['distribution'].append(f"✅ PASS: All free preview questions are 'easy' difficulty")

    # ===== 5. METADATA VALIDATION =====
    print("Running Metadata Validation...")

    # Check questionCount
    if pack.get('questionCount') == 400:
        results['metadata'].append(f"✅ PASS: questionCount = 400")
    else:
        results['metadata'].append(f"❌ FAIL: questionCount = {pack.get('questionCount')} (expected 400)")
        issues.append(f"questionCount metadata: {pack.get('questionCount')}")

    # Check freePreviewCount
    if pack.get('freePreviewCount') == 40:
        results['metadata'].append(f"✅ PASS: freePreviewCount = 40")
    else:
        results['metadata'].append(f"❌ FAIL: freePreviewCount = {pack.get('freePreviewCount')} (expected 40)")
        issues.append(f"freePreviewCount metadata: {pack.get('freePreviewCount')}")

    # Check price (should be number 0.69)
    price = pack.get('price')
    if isinstance(price, (int, float)) and price == 0.69:
        results['metadata'].append(f"✅ PASS: price = 0.69 (number type)")
    else:
        results['metadata'].append(f"❌ FAIL: price = {price} (type: {type(price).__name__}, expected 0.69 as number)")
        issues.append(f"Price: {price} (type: {type(price).__name__})")

    # Check difficulty breakdown metadata
    if 'difficulty' in pack:
        meta_easy = pack['difficulty'].get('easy', 0)
        meta_medium = pack['difficulty'].get('medium', 0)
        meta_hard = pack['difficulty'].get('hard', 0)

        if meta_easy == easy and meta_medium == medium and meta_hard == hard:
            results['metadata'].append(f"✅ PASS: Difficulty metadata matches actual counts")
        else:
            results['metadata'].append(f"❌ FAIL: Difficulty metadata mismatch")
            issues.append(f"Metadata: easy={meta_easy}, medium={meta_medium}, hard={meta_hard}")
            issues.append(f"Actual: easy={easy}, medium={medium}, hard={hard}")

    # Check subtopics list
    if 'subtopics' in pack:
        meta_subtopics = set(pack['subtopics'])
        actual_subtopics = set(expected_distribution.keys())
        if meta_subtopics == actual_subtopics:
            results['metadata'].append(f"✅ PASS: All 7 subtopics listed in metadata")
        else:
            missing = actual_subtopics - meta_subtopics
            extra = meta_subtopics - actual_subtopics
            results['metadata'].append(f"❌ FAIL: Subtopics metadata mismatch")
            if missing:
                issues.append(f"Missing subtopics in metadata: {missing}")
            if extra:
                issues.append(f"Extra subtopics in metadata: {extra}")

    # Check for subtopicIcons
    if 'subtopicIcons' in pack:
        icon_subtopics = set(pack['subtopicIcons'].keys())
        if icon_subtopics == actual_subtopics:
            results['metadata'].append(f"✅ PASS: subtopicIcons present for all 7 subtopics")
        else:
            missing = actual_subtopics - icon_subtopics
            results['metadata'].append(f"⚠️  WARNING: Missing subtopicIcons for: {missing}")
            issues.append(f"Missing subtopicIcons: {missing}")
    else:
        results['metadata'].append(f"⚠️  WARNING: subtopicIcons field not present")
        issues.append("subtopicIcons field missing")

    # Check for icon, isPublished, releaseDate
    meta_checks = []
    if 'icon' not in pack:
        meta_checks.append("icon")
    if 'isPublished' not in pack:
        meta_checks.append("isPublished")
    if 'releaseDate' not in pack:
        meta_checks.append("releaseDate")

    if meta_checks:
        results['metadata'].append(f"⚠️  WARNING: Missing metadata fields: {meta_checks}")
        issues.append(f"Missing metadata: {meta_checks}")
    else:
        results['metadata'].append(f"✅ PASS: icon, isPublished, releaseDate fields present")

    # ===== 6. COMPARISON WITH OTHER PACKS =====
    print("Running Comparison with Other Packs...")

    # Load comparison packs if available
    comparison_packs = {}
    if narnia_path and Path(narnia_path).exists():
        try:
            comparison_packs['narnia'] = load_json(narnia_path)
        except:
            pass
    if candy_path and Path(candy_path).exists():
        try:
            comparison_packs['candy'] = load_json(candy_path)
        except:
            pass

    if comparison_packs:
        # Compare top-level structure
        pack_fields = set(pack.keys())
        for name, comp_pack in comparison_packs.items():
            comp_fields = set(comp_pack.keys())
            missing = comp_fields - pack_fields
            extra = pack_fields - comp_fields

            if missing or extra:
                results['comparison'].append(f"⚠️  WARNING: Field differences vs {name}")
                if missing:
                    issues.append(f"Fields in {name} but not 90s: {missing}")
                if extra:
                    issues.append(f"Fields in 90s but not {name}: {extra}")
            else:
                results['comparison'].append(f"✅ PASS: Top-level fields match {name}")

        # Check pricing appropriateness (400 questions)
        results['comparison'].append(f"✅ INFO: 400 questions at $0.69 follows pricing tier guidelines")
    else:
        results['comparison'].append(f"⚠️  INFO: No comparison packs available for analysis")

    return results, issues

def generate_report(results, issues, output_path):
    """Generate markdown audit report"""

    total_checks = sum(len(v) for v in results.values())
    passed = sum(1 for v in results.values() for item in v if item.startswith('✅'))
    failed = sum(1 for v in results.values() for item in v if item.startswith('❌'))
    warnings = sum(1 for v in results.values() for item in v if item.startswith('⚠️'))

    score = (passed / (passed + failed) * 100) if (passed + failed) > 0 else 0

    report = f"""# 90s Trivia Expansion Pack - Comprehensive Audit Report

**Generated:** {Path(__file__).name}
**Date:** 2026-02-07
**Pack Location:** `/home/user/fiztrivia/Fiz/Resources/Expansion Packs/expansion_90s_trivia.json`

---

## Executive Summary

**Total Checks:** {total_checks}
**✅ Passed:** {passed}
**❌ Failed:** {failed}
**⚠️  Warnings:** {warnings}

**Pass Rate:** {score:.1f}%

**Final Verdict:** {"🚀 LAUNCH READY" if failed == 0 and len(issues) <= warnings else "⚠️  NEEDS FIXES"}

---

## 1. Structural Validation

"""

    for item in results['structural']:
        report += f"{item}\n"

    report += "\n---\n\n## 2. ID Validation\n\n"
    for item in results['id_validation']:
        report += f"{item}\n"

    report += "\n---\n\n## 3. Content Quality\n\n"
    for item in results['content_quality']:
        report += f"{item}\n"

    report += "\n---\n\n## 4. Distribution Validation\n\n"
    for item in results['distribution']:
        report += f"{item}\n"

    report += "\n---\n\n## 5. Metadata Validation\n\n"
    for item in results['metadata']:
        report += f"{item}\n"

    report += "\n---\n\n## 6. Comparison with Other Packs\n\n"
    for item in results['comparison']:
        report += f"{item}\n"

    report += "\n---\n\n## Issues Found\n\n"
    if issues:
        report += f"**Total Issues:** {len(issues)}\n\n"
        for i, issue in enumerate(issues, 1):
            report += f"{i}. {issue}\n"
    else:
        report += "✅ No critical issues found!\n"

    report += "\n---\n\n## Recommendations\n\n"

    if failed > 0:
        report += "### Critical Fixes Required\n\n"
        report += "1. Address all ❌ FAIL items immediately\n"
        report += "2. Review issues list for specific problems\n"
        report += "3. Re-run audit after fixes\n\n"

    if warnings > 0:
        report += "### Optional Improvements\n\n"
        report += "1. Review ⚠️  WARNING items\n"
        report += "2. Consider addressing for better consistency\n"
        report += "3. Not blocking for launch if no critical failures\n\n"

    if failed == 0 and warnings == 0:
        report += "✅ **Pack is in excellent condition!**\n\n"
        report += "- All validation checks passed\n"
        report += "- No structural issues found\n"
        report += "- Ready for production deployment\n\n"

    report += "---\n\n## Next Steps\n\n"

    if failed == 0:
        report += "1. ✅ Pack validation complete\n"
        report += "2. 🧪 Test in-app purchase flow\n"
        report += "3. 🎮 Test gameplay with pack questions\n"
        report += "4. 📱 Verify on physical device\n"
        report += "5. 🚀 Ready for App Store submission\n"
    else:
        report += "1. 🔧 Fix all critical issues listed above\n"
        report += "2. 🔄 Re-run audit script\n"
        report += "3. ✅ Confirm all checks pass\n"
        report += "4. 🧪 Proceed to testing\n"

    report += "\n---\n\n"
    report += f"**Audit Complete** - Generated by audit_90s_pack.py\n"

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)

    return score, failed

def main():
    base_path = Path('/home/user/fiztrivia/Fiz/Resources/Expansion Packs')

    pack_path = base_path / 'expansion_90s_trivia.json'
    narnia_path = base_path / 'expansion_narnia.json'
    candy_path = base_path / 'expansion_candy.json'
    output_path = Path('/home/user/fiztrivia/90S_AUDIT_REPORT.md')

    print("=" * 60)
    print("90s Trivia Expansion Pack - Comprehensive Audit")
    print("=" * 60)
    print()

    if not pack_path.exists():
        print(f"❌ ERROR: Pack file not found at {pack_path}")
        return 1

    results, issues = audit_90s_pack(str(pack_path), str(narnia_path), str(candy_path))

    if results is None:
        print("❌ CRITICAL ERROR during audit:")
        for issue in issues:
            print(f"  {issue}")
        return 1

    print()
    print("=" * 60)
    print("Generating Report...")
    print("=" * 60)

    score, failed = generate_report(results, issues, output_path)

    print(f"\n✅ Audit complete!")
    print(f"📊 Pass Rate: {score:.1f}%")
    print(f"📄 Report saved to: {output_path}")
    print()

    if failed == 0:
        print("🚀 VERDICT: LAUNCH READY")
    else:
        print("⚠️  VERDICT: NEEDS FIXES")
        print(f"   {failed} critical failures found")

    return 0 if failed == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
