#!/usr/bin/env python3
"""
More refined check: identify questions that are truly about Biblical times
(before ~100 AD) vs. legitimate post-Biblical church history
"""

import json

def check_timeline():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    history = data['categories']['History']
    church_history = [q for q in history if q.get('subcategory') == 'Church History']

    print("=" * 80)
    print("REFINED CHURCH HISTORY TIMELINE CHECK")
    print("=" * 80)
    print()
    print("Biblical Period: Creation through ~90-100 AD (Book of Revelation)")
    print("Church History: ~100 AD onwards")
    print()
    print("=" * 80)

    # Questions that are LIKELY about Biblical times (need to move to Bible)
    biblical_era = [
        'his_073',  # Apostle to the Gentiles (Paul during Acts)
        'his_075',  # First four books of NT (Gospels - part of Bible itself)
    ]

    # Questions that are POST-BIBLICAL and appropriate for Church History
    post_biblical = [
        'his_080', 'his_098', 'his_278',  # Constantine 313 AD
        'his_100', 'his_113', 'his_121', 'his_128', 'his_281',  # Nicaea 325 AD
        'his_269',  # First pope (church structure question, not Biblical narrative)
        'his_272',  # Easter (church tradition, not Biblical event)
        'his_276',  # Wycliffe 1380s
        'his_087', 'his_103', 'his_104', 'his_119', 'his_126', 'his_277',  # Reformers (1500s+)
    ]

    print("\n⚠️  POTENTIALLY PROBLEMATIC (Biblical-era content):\n")
    
    for q in church_history:
        if q['id'] in biblical_era:
            print(f"[{q['id']}] {q['question']}")
            print(f"   Answer: {q.get('correct_answer')}")
            print(f"   >>> This appears to be about Biblical times")
            print(f"   >>> Should likely be in BIBLE category\n")

    print("=" * 80)
    print("✅ POST-BIBLICAL QUESTIONS (appropriate for Church History):")
    print("=" * 80)
    print()
    print(f"Found {len(post_biblical)} questions about legitimate church history")
    print("(early church councils, Constantine, church structure, reformers, etc.)")
    print()
    print("These are CORRECT in Church History because they occurred after")
    print("the Biblical period ended (~100 AD).")
    print()

    # Show a few examples
    examples = [
        'his_080',  # Constantine
        'his_128',  # Nicaea
        'his_104',  # Wycliffe
    ]

    print("Examples of appropriate Church History questions:")
    for q in church_history:
        if q['id'] in examples:
            print(f"  • [{q['id']}] {q['question'][:60]}...")

    print("\n" + "=" * 80)
    print(f"\nSUMMARY: Found {len(biblical_era)} questions that should move to Bible category")
    print("=" * 80)

if __name__ == "__main__":
    check_timeline()
