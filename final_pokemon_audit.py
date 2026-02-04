#!/usr/bin/env python3
"""
Final comprehensive Pokemon pack audit - manual review focus
"""

import json
from difflib import SequenceMatcher

def load_pack(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    filepath = '/home/user/fiztrivia/Fiz/Resources/Expansion Packs/expansion_pokemon.json'
    pack = load_pack(filepath)

    all_questions = pack.get('freePreviewQuestions', []) + pack.get('paidQuestions', [])

    # Manual findings from review
    auto_fix = []
    flag_for_replacement = []
    needs_verification = []

    # EXACT DUPLICATES - definitely need replacement
    flag_for_replacement.append({
        'type': 'exact_duplicate',
        'id1': 'pkm_preview_032',
        'id2': 'pkm_paid_377',
        'issue': 'Exact duplicate: "What is Ash\'s last name?"',
        'action': 'Remove pkm_paid_377'
    })

    # TRUE SEMANTIC DUPLICATES - essentially the same question
    flag_for_replacement.append({
        'type': 'semantic_duplicate',
        'id1': 'pkm_preview_014',
        'id2': 'pkm_paid_144',
        'issue': 'Q1: "Which generation introduced Mega Evolution?" vs Q2: "What generation introduced Mega Evolution?"',
        'action': 'Remove pkm_paid_144 (using Which vs What is same question)'
    })

    flag_for_replacement.append({
        'type': 'semantic_duplicate',
        'id1': 'pkm_preview_046',
        'id2': 'pkm_paid_125',
        'issue': 'Q1: "What region is Pokémon Gold/Silver set in?" vs Q2: "What region is Pokémon Gold and Silver set in?"',
        'action': 'Remove pkm_paid_125 (Gold/Silver vs Gold and Silver is same question)'
    })

    # SELF-REVEALING QUESTIONS
    needs_verification.append({
        'type': 'self_revealing',
        'id': 'pkm_paid_083',
        'issue': 'Question: "What is Ralts\' final evolution in the Gardevoir line?" - Answer: "Gardevoir"',
        'note': 'Question literally mentions Gardevoir. Should ask "What is Ralts\' final evolution?" without naming the line'
    })

    needs_verification.append({
        'type': 'self_revealing',
        'id': 'pkm_paid_354',
        'issue': 'Question: "What Pokémon does Ash\'s Charizard refuse to obey him for a while?" - Answer: "Charizard"',
        'note': 'Question already states it\'s Charizard. Poorly worded question.'
    })

    # Check for actual grammar issues
    for q in all_questions:
        # Missing question mark
        if not q['question'].endswith('?'):
            auto_fix.append({
                'id': q['id'],
                'issue': 'Missing question mark',
                'question': q['question']
            })

        # Double spaces
        if '  ' in q['question']:
            auto_fix.append({
                'id': q['id'],
                'issue': 'Double space in question',
                'question': q['question']
            })

        # Check options for double spaces
        for opt in q['options']:
            if '  ' in opt:
                auto_fix.append({
                    'id': q['id'],
                    'issue': f'Double space in option: "{opt}"',
                    'question': q['question']
                })

    # Output report
    with open('/home/user/fiztrivia/POKEMON_PACK_AUDIT_REPORT.md', 'w', encoding='utf-8') as f:
        f.write("# POKÉMON TRIVIA PACK - QA AUDIT REPORT\n\n")
        f.write(f"**Total Questions Audited:** {len(all_questions)}\n\n")
        f.write(f"**File:** `/home/user/fiztrivia/Fiz/Resources/Expansion Packs/expansion_pokemon.json`\n\n")

        f.write("---\n\n")
        f.write("## SUMMARY\n\n")
        f.write(f"- **AUTO-FIX (Grammar/Typos):** {len(auto_fix)}\n")
        f.write(f"- **FLAG FOR REPLACEMENT (Duplicates):** {len(flag_for_replacement)}\n")
        f.write(f"- **NEEDS VERIFICATION (Accuracy/Clarity):** {len(needs_verification)}\n")
        f.write(f"- **TOTAL ISSUES:** {len(auto_fix) + len(flag_for_replacement) + len(needs_verification)}\n\n")

        f.write("---\n\n")

        if auto_fix:
            f.write("## 1. AUTO-FIX: Grammar and Typo Issues\n\n")
            f.write("Clear typos and grammar errors that can be automatically fixed.\n\n")
            for i, issue in enumerate(auto_fix, 1):
                f.write(f"### {i}. ID: `{issue['id']}`\n")
                f.write(f"- **Issue:** {issue['issue']}\n")
                f.write(f"- **Question:** {issue['question']}\n\n")
        else:
            f.write("## 1. AUTO-FIX: Grammar and Typo Issues\n\n")
            f.write("✅ **No grammar or typo issues found!**\n\n")

        f.write("---\n\n")

        if flag_for_replacement:
            f.write("## 2. FLAG FOR REPLACEMENT: Duplicates\n\n")
            f.write("These are exact or true semantic duplicates that need to be replaced with new questions.\n\n")
            for i, issue in enumerate(flag_for_replacement, 1):
                f.write(f"### {i}. {issue['type'].upper()}\n")
                f.write(f"- **IDs:** `{issue['id1']}` & `{issue['id2']}`\n")
                f.write(f"- **Issue:** {issue['issue']}\n")
                f.write(f"- **Recommended Action:** {issue['action']}\n\n")
        else:
            f.write("## 2. FLAG FOR REPLACEMENT: Duplicates\n\n")
            f.write("✅ **No duplicates found!**\n\n")

        f.write("---\n\n")

        if needs_verification:
            f.write("## 3. NEEDS VERIFICATION: Accuracy and Clarity Issues\n\n")
            f.write("Questions that may be self-revealing, factually questionable, or confusingly worded.\n\n")
            for i, issue in enumerate(needs_verification, 1):
                f.write(f"### {i}. ID: `{issue['id']}`\n")
                f.write(f"- **Type:** {issue['type']}\n")
                f.write(f"- **Issue:** {issue['issue']}\n")
                if 'note' in issue:
                    f.write(f"- **Note:** {issue['note']}\n")
                f.write("\n")
        else:
            f.write("## 3. NEEDS VERIFICATION: Accuracy and Clarity Issues\n\n")
            f.write("✅ **No accuracy or clarity issues found!**\n\n")

        f.write("---\n\n")
        f.write("## AUDIT COMPLETE\n\n")
        f.write("This report identifies issues found in the Pokémon trivia pack.\n\n")
        f.write("**Note:** Template questions (e.g., 'What type does [Gym Leader X] specialize in?') are VALID when asking about different subjects and are not flagged as duplicates.\n")

    print("="*80)
    print("POKÉMON PACK AUDIT COMPLETE")
    print("="*80)
    print(f"\nTotal questions audited: {len(all_questions)}")
    print(f"\nIssues found:")
    print(f"  - AUTO-FIX: {len(auto_fix)}")
    print(f"  - FLAG FOR REPLACEMENT: {len(flag_for_replacement)}")
    print(f"  - NEEDS VERIFICATION: {len(needs_verification)}")
    print(f"  - TOTAL: {len(auto_fix) + len(flag_for_replacement) + len(needs_verification)}")
    print(f"\nReport saved to: /home/user/fiztrivia/POKEMON_PACK_AUDIT_REPORT.md")

if __name__ == '__main__':
    main()
