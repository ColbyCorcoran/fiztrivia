#!/usr/bin/env python3
"""
Reorganize Bible category:
1. Merge Old Testament + New Testament + Bible Trivia → Bible Trivia (75 questions)
2. Expand Biblical History: 25 → 75 (+50)
3. Expand Biblical Theology: 22 → 75 (+53)
4. Expand Bible Languages: 23 → 75 (+52)
"""
import json

def main():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    bible = data['categories']['Bible']

    # Separate by subcategory
    old_testament = [q for q in bible if q.get('subcategory') == 'Old Testament']
    new_testament = [q for q in bible if q.get('subcategory') == 'New Testament']
    bible_trivia = [q for q in bible if q.get('subcategory') == 'Bible Trivia']
    biblical_history = [q for q in bible if q.get('subcategory') == 'Biblical History']
    biblical_theology = [q for q in bible if q.get('subcategory') == 'Biblical Theology']
    bible_languages = [q for q in bible if q.get('subcategory') == 'Bible Languages']

    print("Current counts:")
    print(f"  Old Testament: {len(old_testament)}")
    print(f"  New Testament: {len(new_testament)}")
    print(f"  Bible Trivia: {len(bible_trivia)}")
    print(f"  Biblical History: {len(biblical_history)}")
    print(f"  Biblical Theology: {len(biblical_theology)}")
    print(f"  Bible Languages: {len(bible_languages)}")
    print()

    # Merge Old Testament, New Testament, Bible Trivia
    merged_trivia = old_testament + new_testament + bible_trivia
    print(f"Merged trivia total: {len(merged_trivia)} questions")

    # Change all to "Bible Trivia" subcategory
    for q in merged_trivia:
        q['subcategory'] = 'Bible Trivia'

    # Sort by difficulty to get diverse mix, then take first 75
    easy = [q for q in merged_trivia if q['difficulty'] == 'easy']
    medium = [q for q in merged_trivia if q['difficulty'] == 'medium']
    hard = [q for q in merged_trivia if q['difficulty'] == 'hard']

    # Take proportional amounts (roughly 1/3 each)
    bible_trivia_keep = easy[:25] + medium[:25] + hard[:25]
    bible_trivia_expansion = [q for q in merged_trivia if q not in bible_trivia_keep]

    print(f"\nBible Trivia:")
    print(f"  Keeping: {len(bible_trivia_keep)}")
    print(f"  Moving to expansion: {len(bible_trivia_expansion)}")

    # Count by difficulty
    diffs = {}
    for q in bible_trivia_keep:
        d = q['difficulty']
        diffs[d] = diffs.get(d, 0) + 1
    print(f"  Difficulty kept: {diffs}")
    print()

    # Keep other subcategories as-is (will add more questions later)
    new_bible = bible_trivia_keep + biblical_history + biblical_theology + bible_languages
    new_bible.sort(key=lambda q: int(q['id'].split('_')[1]))

    data['categories']['Bible'] = new_bible

    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Updated main questions file")
    print(f"   New Bible total: {len(new_bible)} questions")
    print(f"   Bible Trivia: {len(bible_trivia_keep)}")
    print(f"   Biblical History: {len(biblical_history)}")
    print(f"   Biblical Theology: {len(biblical_theology)}")
    print(f"   Bible Languages: {len(bible_languages)}")

    # Create expansion pack
    expansion_pack = {
        "Bible Trivia": bible_trivia_expansion
    }

    with open('Fiz/Resources/bible_expansion_pack.json', 'w') as f:
        json.dump(expansion_pack, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Created expansion pack file")
    print(f"   Bible Trivia expansion: {len(bible_trivia_expansion)} questions")

if __name__ == "__main__":
    main()
