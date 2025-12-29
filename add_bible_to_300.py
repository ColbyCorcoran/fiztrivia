#!/usr/bin/env python3
"""
Add 34 Bible questions to reach 300 total
Prioritize smallest subcategories: Bible Trivia, Bible Languages, Biblical History, Biblical Theology
Emphasize easy and medium questions
"""

import json

# Load database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

print(f"Current Bible questions: {len(data['categories']['Bible'])}")
print(f"Adding 34 questions (bib_267 to bib_300)")
print()
print("Distribution strategy:")
print("  Bible Trivia: +15 (3 → 18)")
print("  Bible Languages: +10 (13 → 23)")
print("  Biblical History: +5 (20 → 25)")
print("  Biblical Theology: +4 (18 → 22)")
print()
print("Difficulty emphasis: +25 easy, +9 medium (already have enough hard)")
print()

# 34 new Bible questions (bib_267 to bib_300)
new_questions = [
    # BIBLE TRIVIA (15 questions: 10 easy, 5 medium)
    {
        "id": "bib_267",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "How many books are in the New Testament?",
        "options": ["27", "39", "66", "24"],
        "correct_answer": "27",
        "difficulty": "easy"
    },
    {
        "id": "bib_268",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "How many books are in the Old Testament?",
        "options": ["39", "27", "66", "46"],
        "correct_answer": "39",
        "difficulty": "easy"
    },
    {
        "id": "bib_269",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "How many days and nights did it rain during the flood?",
        "options": ["40", "7", "100", "365"],
        "correct_answer": "40",
        "difficulty": "easy"
    },
    {
        "id": "bib_270",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "How many disciples did Jesus have?",
        "options": ["12", "10", "7", "24"],
        "correct_answer": "12",
        "difficulty": "easy"
    },
    {
        "id": "bib_271",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "What is the shortest book in the Bible by number of verses?",
        "options": ["2 John", "3 John", "Obadiah", "Jude"],
        "correct_answer": "2 John",
        "difficulty": "medium"
    },
    {
        "id": "bib_272",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "What is the longest book in the Bible by number of chapters?",
        "options": ["Psalms", "Genesis", "Isaiah", "Jeremiah"],
        "correct_answer": "Psalms",
        "difficulty": "easy"
    },
    {
        "id": "bib_273",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "How many commandments did God give to Moses?",
        "options": ["10", "7", "12", "613"],
        "correct_answer": "10",
        "difficulty": "easy"
    },
    {
        "id": "bib_274",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "How many plagues did God send upon Egypt?",
        "options": ["10", "7", "12", "40"],
        "correct_answer": "10",
        "difficulty": "easy"
    },
    {
        "id": "bib_275",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "How many sons did Jacob have?",
        "options": ["12", "10", "7", "13"],
        "correct_answer": "12",
        "difficulty": "medium"
    },
    {
        "id": "bib_276",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "How many chapters are in the book of Revelation?",
        "options": ["22", "12", "28", "40"],
        "correct_answer": "22",
        "difficulty": "medium"
    },
    {
        "id": "bib_277",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "What is the middle book of the Bible?",
        "options": ["Psalms", "Proverbs", "Micah", "Romans"],
        "correct_answer": "Psalms",
        "difficulty": "medium"
    },
    {
        "id": "bib_278",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "How many people were on Noah's ark?",
        "options": ["8", "6", "10", "12"],
        "correct_answer": "8",
        "difficulty": "easy"
    },
    {
        "id": "bib_279",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "How many books of the Bible are named after women?",
        "options": ["2", "1", "3", "4"],
        "correct_answer": "2",
        "difficulty": "medium"
    },
    {
        "id": "bib_280",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "How many Gospels are in the New Testament?",
        "options": ["4", "3", "5", "7"],
        "correct_answer": "4",
        "difficulty": "easy"
    },
    {
        "id": "bib_281",
        "category": "Bible",
        "subcategory": "Bible Trivia",
        "question": "How many years did the Israelites wander in the wilderness?",
        "options": ["40", "30", "70", "400"],
        "correct_answer": "40",
        "difficulty": "easy"
    },

    # BIBLE LANGUAGES (10 questions: 7 easy, 3 medium)
    {
        "id": "bib_282",
        "category": "Bible",
        "subcategory": "Bible Languages",
        "question": "What language was most of the Old Testament originally written in?",
        "options": ["Hebrew", "Greek", "Aramaic", "Latin"],
        "correct_answer": "Hebrew",
        "difficulty": "easy"
    },
    {
        "id": "bib_283",
        "category": "Bible",
        "subcategory": "Bible Languages",
        "question": "What language was most of the New Testament originally written in?",
        "options": ["Greek", "Hebrew", "Aramaic", "Latin"],
        "correct_answer": "Greek",
        "difficulty": "easy"
    },
    {
        "id": "bib_284",
        "category": "Bible",
        "subcategory": "Bible Languages",
        "question": "What does 'Amen' mean?",
        "options": ["So be it", "Praise God", "Holy", "Forever"],
        "correct_answer": "So be it",
        "difficulty": "easy"
    },
    {
        "id": "bib_285",
        "category": "Bible",
        "subcategory": "Bible Languages",
        "question": "What does 'Hallelujah' mean?",
        "options": ["Praise the Lord", "God is good", "Blessed be", "Holy is He"],
        "correct_answer": "Praise the Lord",
        "difficulty": "easy"
    },
    {
        "id": "bib_286",
        "category": "Bible",
        "subcategory": "Bible Languages",
        "question": "What does the name 'Jesus' mean?",
        "options": ["The Lord saves", "Son of God", "Messiah", "King of kings"],
        "correct_answer": "The Lord saves",
        "difficulty": "medium"
    },
    {
        "id": "bib_287",
        "category": "Bible",
        "subcategory": "Bible Languages",
        "question": "What does 'Emmanuel' mean?",
        "options": ["God with us", "Mighty God", "Prince of Peace", "Wonderful Counselor"],
        "correct_answer": "God with us",
        "difficulty": "easy"
    },
    {
        "id": "bib_288",
        "category": "Bible",
        "subcategory": "Bible Languages",
        "question": "What does 'Messiah' mean?",
        "options": ["Anointed One", "Savior", "King", "Lord"],
        "correct_answer": "Anointed One",
        "difficulty": "medium"
    },
    {
        "id": "bib_289",
        "category": "Bible",
        "subcategory": "Bible Languages",
        "question": "What does 'Sabbath' mean?",
        "options": ["Rest", "Worship", "Holy", "Seventh"],
        "correct_answer": "Rest",
        "difficulty": "easy"
    },
    {
        "id": "bib_290",
        "category": "Bible",
        "subcategory": "Bible Languages",
        "question": "What does 'Selah' mean in the Psalms?",
        "options": ["Pause/Reflect", "Sing", "Praise", "Forever"],
        "correct_answer": "Pause/Reflect",
        "difficulty": "medium"
    },
    {
        "id": "bib_291",
        "category": "Bible",
        "subcategory": "Bible Languages",
        "question": "What does 'Hosanna' mean?",
        "options": ["Save now", "Praise God", "Holy", "King"],
        "correct_answer": "Save now",
        "difficulty": "easy"
    },

    # BIBLICAL HISTORY (5 questions: 4 easy, 1 medium)
    {
        "id": "bib_292",
        "category": "Bible",
        "subcategory": "Biblical History",
        "question": "What empire conquered Judah and destroyed the temple in 586 BC?",
        "options": ["Babylonian", "Assyrian", "Persian", "Greek"],
        "correct_answer": "Babylonian",
        "difficulty": "easy"
    },
    {
        "id": "bib_293",
        "category": "Bible",
        "subcategory": "Biblical History",
        "question": "What empire conquered the Northern Kingdom of Israel in 722 BC?",
        "options": ["Assyrian", "Babylonian", "Persian", "Egyptian"],
        "correct_answer": "Assyrian",
        "difficulty": "medium"
    },
    {
        "id": "bib_294",
        "category": "Bible",
        "subcategory": "Biblical History",
        "question": "What empire allowed the Jews to return from exile?",
        "options": ["Persian", "Babylonian", "Greek", "Roman"],
        "correct_answer": "Persian",
        "difficulty": "easy"
    },
    {
        "id": "bib_295",
        "category": "Bible",
        "subcategory": "Biblical History",
        "question": "What empire ruled over Israel during the time of Jesus?",
        "options": ["Roman", "Greek", "Persian", "Babylonian"],
        "correct_answer": "Roman",
        "difficulty": "easy"
    },
    {
        "id": "bib_296",
        "category": "Bible",
        "subcategory": "Biblical History",
        "question": "What city was the capital of the United Kingdom under David and Solomon?",
        "options": ["Jerusalem", "Samaria", "Bethlehem", "Hebron"],
        "correct_answer": "Jerusalem",
        "difficulty": "easy"
    },

    # BIBLICAL THEOLOGY (4 questions: 4 easy)
    {
        "id": "bib_297",
        "category": "Bible",
        "subcategory": "Biblical Theology",
        "question": "What is the Great Commandment according to Jesus?",
        "options": ["Love God and love your neighbor", "Do not kill", "Keep the Sabbath", "Honor your parents"],
        "correct_answer": "Love God and love your neighbor",
        "difficulty": "easy"
    },
    {
        "id": "bib_298",
        "category": "Bible",
        "subcategory": "Biblical Theology",
        "question": "What does justification by faith mean?",
        "options": ["Being made right with God through faith", "Works-based salvation", "Baptismal regeneration", "Penance for sins"],
        "correct_answer": "Being made right with God through faith",
        "difficulty": "easy"
    },
    {
        "id": "bib_299",
        "category": "Bible",
        "subcategory": "Biblical Theology",
        "question": "What is grace according to the Bible?",
        "options": ["Unmerited favor from God", "Earned blessing", "Good works", "Religious rituals"],
        "correct_answer": "Unmerited favor from God",
        "difficulty": "easy"
    },
    {
        "id": "bib_300",
        "category": "Bible",
        "subcategory": "Biblical Theology",
        "question": "What does it mean to be born again?",
        "options": ["Spiritual rebirth through faith in Christ", "Physical rebirth", "Baptism only", "Good deeds"],
        "correct_answer": "Spiritual rebirth through faith in Christ",
        "difficulty": "easy"
    }
]

# Add new questions
data['categories']['Bible'].extend(new_questions)

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✓ Added {len(new_questions)} new Bible questions")
print(f"\nNew Bible total: {len(data['categories']['Bible'])} questions")

# Show breakdown
print("\nBreakdown by subcategory:")
subcats = {}
for q in data['categories']['Bible']:
    subcat = q['subcategory']
    if subcat not in subcats:
        subcats[subcat] = 0
    subcats[subcat] += 1

for subcat in sorted(subcats.keys()):
    print(f"  {subcat}: {subcats[subcat]} questions")

# Show difficulty breakdown
print("\nBreakdown by difficulty:")
diffs = {'easy': 0, 'medium': 0, 'hard': 0}
for q in data['categories']['Bible']:
    diffs[q['difficulty']] += 1

for diff in ['easy', 'medium', 'hard']:
    pct = (diffs[diff] / len(data['categories']['Bible'])) * 100
    print(f"  {diff.capitalize()}: {diffs[diff]} ({pct:.1f}%)")

print("\n✓ Bible category complete: 300/300 questions")
