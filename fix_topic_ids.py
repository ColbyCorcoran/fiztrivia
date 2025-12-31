#!/usr/bin/env python3
"""
Fix topic field in expansion pack questions to use packId instead of packName.
"""

import json
from pathlib import Path

def fix_pack_topics(file_path):
    """Fix topic values in a pack to use packId instead of packName."""
    with open(file_path, 'r') as f:
        data = json.load(f)

    pack_id = data['packId']
    pack_name = data['packName']

    print(f"=== {pack_name} ===")
    print(f"Changing topic from '{pack_name}' to '{pack_id}'")

    fixed_count = 0

    # Fix free preview questions
    for question in data['freePreviewQuestions']:
        if question.get('topic') == pack_name:
            question['topic'] = pack_id
            fixed_count += 1

    # Fix paid questions
    for question in data['paidQuestions']:
        if question.get('topic') == pack_name:
            question['topic'] = pack_id
            fixed_count += 1

    # Write back
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Fixed {fixed_count} questions\n")

def main():
    packs_dir = Path("/Users/colbycorcoran/Documents/App Development/Fiz/Fiz/Resources/Expansion Packs")

    for pack_file in sorted(packs_dir.glob("expansion_*.json")):
        fix_pack_topics(pack_file)

    print("🎉 All expansion packs updated!")

if __name__ == "__main__":
    main()
