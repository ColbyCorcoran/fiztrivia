#!/usr/bin/env python3
"""Add 52 Bible Languages questions (23 → 75)"""
import json

bible_languages = []

# Easy (17)
easy_languages = [
    ("bib_431", "What does 'Abba' mean?", ["Father/Daddy", "Lord", "Master", "King"], "Father/Daddy"),
    ("bib_432", "What does 'Hosanna' mean?", ["Save now", "Praise God", "Hallelujah", "Amen"], "Save now"),
    ("bib_433", "What does 'Rabbi' mean?", ["Teacher/Master", "Father", "Priest", "King"], "Teacher/Master"),
    ("bib_434", "What does 'Maranatha' mean?", ["Our Lord, come!", "Praise God", "Amen", "Hallelujah"], "Our Lord, come!"),
    ("bib_435", "What does 'Alleluia' mean?", ["Praise the Lord", "Thank you", "Amen", "Bless you"], "Praise the Lord"),
    ("bib_436", "What does 'Selah' likely mean?", ["Pause/Interlude", "Amen", "Forever", "Always"], "Pause/Interlude"),
    ("bib_437", "What does 'Hosanna in the highest' mean?", ["Save now in the highest", "Praise in heaven", "Glory to God", "Hallelujah forever"], "Save now in the highest"),
    ("bib_438", "What language is the word 'Abba' from?", ["Aramaic", "Hebrew", "Greek", "Latin"], "Aramaic"),
    ("bib_439", "What does 'Christ' mean in Greek?", ["Anointed One", "Savior", "King", "Lord"], "Anointed One"),
    ("bib_440", "What does 'Jehovah' mean?", ["LORD/I AM", "God", "Father", "King"], "LORD/I AM"),
    ("bib_441", "What does 'Sabbath' mean?", ["Rest", "Holy", "Seventh", "Day"], "Rest"),
    ("bib_442", "What does 'Gehenna' refer to?", ["Hell/Valley of Hinnom", "Heaven", "Purgatory", "Earth"], "Hell/Valley of Hinnom"),
    ("bib_443", "What does 'Sheol' refer to?", ["Place of the dead", "Heaven", "Hell only", "Purgatory"], "Place of the dead"),
    ("bib_444", "What does 'Golgotha' mean?", ["Place of the skull", "Hill", "Calvary", "Mountain"], "Place of the skull"),
    ("bib_445", "What does 'Bethlehem' mean?", ["House of bread", "House of God", "City of David", "Holy city"], "House of bread"),
    ("bib_446", "What does 'Jerusalem' mean?", ["City of peace/foundation of peace", "Holy city", "City of David", "God's city"], "City of peace/foundation of peace"),
    ("bib_447", "What does 'Nazareth' likely mean?", ["Branch/shoot", "Holy place", "Small town", "Galilee"], "Branch/shoot"),
]

for q in easy_languages:
    bible_languages.append({
        "id": q[0], "category": "Bible", "subcategory": "Bible Languages",
        "question": q[1], "options": q[2], "correct_answer": q[3],
        "difficulty": "easy", "topic": None, "subtopic": None
    })

# Medium (18)
medium_languages = [
    ("bib_448", "What does 'Paraclete' mean?", ["Helper/Comforter/Advocate", "Spirit", "Teacher", "Guide"], "Helper/Comforter/Advocate"),
    ("bib_449", "What does 'Gethsemane' mean?", ["Oil press", "Garden", "Olive grove", "Prayer place"], "Oil press"),
    ("bib_450", "What does 'Beelzebub' mean?", ["Lord of the flies", "Devil", "Satan", "Demon"], "Lord of the flies"),
    ("bib_451", "What does 'Mammon' refer to?", ["Wealth/riches", "Demon", "Idol", "False god"], "Wealth/riches"),
    ("bib_452", "What does 'Talitha koum' mean?", ["Little girl, arise", "Stand up", "Wake up", "Come here"], "Little girl, arise"),
    ("bib_453", "What does 'Ephphatha' mean?", ["Be opened", "Be healed", "Be blessed", "Be saved"], "Be opened"),
    ("bib_454", "What does 'Corban' mean?", ["Gift devoted to God", "Offering", "Sacrifice", "Temple tax"], "Gift devoted to God"),
    ("bib_455", "What does 'Raca' mean?", ["Empty-headed/fool", "Idiot", "Stupid", "Worthless"], "Empty-headed/fool"),
    ("bib_456", "What does 'Barabbas' mean?", ["Son of the father", "Robber", "Murderer", "Rebel"], "Son of the father"),
    ("bib_457", "What does 'Boanerges' mean?", ["Sons of thunder", "Sons of light", "Sons of God", "Disciples"], "Sons of thunder"),
    ("bib_458", "What does 'Cephas' mean?", ["Rock/Peter", "Stone", "Foundation", "Disciple"], "Rock/Peter"),
    ("bib_459", "What does 'Eli, Eli, lema sabachthani' mean?", ["My God, my God, why have you forsaken me?", "Father, forgive them", "It is finished", "Into your hands"], "My God, my God, why have you forsaken me?"),
    ("bib_460", "What does 'Tetragrammaton' refer to?", ["YHWH (God's name)", "Trinity", "Holy", "Lord"], "YHWH (God's name)"),
    ("bib_461", "What does 'Torah' mean?", ["Law/instruction", "Commandments", "Books", "Scripture"], "Law/instruction"),
    ("bib_462", "What does 'Nevi'im' refer to?", ["Prophets", "Writings", "Law", "Psalms"], "Prophets"),
    ("bib_463", "What does 'Ketuvim' refer to?", ["Writings", "Prophets", "Law", "History"], "Writings"),
    ("bib_464", "What does 'Tanakh' stand for?", ["Torah, Nevi'im, Ketuvim", "Old Testament", "Hebrew Bible", "Jewish Scripture"], "Torah, Nevi'im, Ketuvim"),
    ("bib_465", "What does 'Septuagint' mean?", ["Seventy (Greek OT translation)", "Seven", "Seventh", "Sacred"], "Seventy (Greek OT translation)"),
]

for q in medium_languages:
    bible_languages.append({
        "id": q[0], "category": "Bible", "subcategory": "Bible Languages",
        "question": q[1], "options": q[2], "correct_answer": q[3],
        "difficulty": "medium", "topic": None, "subtopic": None
    })

# Hard (17)
hard_languages = [
    ("bib_466", "What does 'hesed' mean in Hebrew?", ["Steadfast love/loving-kindness", "Grace", "Mercy", "Love"], "Steadfast love/loving-kindness"),
    ("bib_467", "What does 'ruach' mean in Hebrew?", ["Spirit/wind/breath", "Soul", "Life", "Power"], "Spirit/wind/breath"),
    ("bib_468", "What does 'nephesh' mean in Hebrew?", ["Soul/life/being", "Spirit", "Body", "Heart"], "Soul/life/being"),
    ("bib_469", "What does 'tsedaqah' mean in Hebrew?", ["Righteousness/justice", "Mercy", "Grace", "Love"], "Righteousness/justice"),
    ("bib_470", "What does 'charis' mean in Greek?", ["Grace/favor", "Love", "Mercy", "Kindness"], "Grace/favor"),
    ("bib_471", "What does 'agape' mean in Greek?", ["Unconditional love", "Friendship", "Romantic love", "Family love"], "Unconditional love"),
    ("bib_472", "What does 'philia' mean in Greek?", ["Friendship/brotherly love", "Romantic love", "Unconditional love", "Family love"], "Friendship/brotherly love"),
    ("bib_473", "What does 'eros' mean in Greek?", ["Romantic love", "Unconditional love", "Friendship", "Family love"], "Romantic love"),
    ("bib_474", "What does 'pistis' mean in Greek?", ["Faith/trust", "Hope", "Love", "Belief"], "Faith/trust"),
    ("bib_475", "What does 'elpis' mean in Greek?", ["Hope", "Faith", "Love", "Joy"], "Hope"),
    ("bib_476", "What does 'dikaiosune' mean in Greek?", ["Righteousness", "Justice", "Holiness", "Goodness"], "Righteousness"),
    ("bib_477", "What does 'koinonia' mean in Greek?", ["Fellowship/communion", "Church", "Community", "Gathering"], "Fellowship/communion"),
    ("bib_478", "What does 'metanoia' mean in Greek?", ["Repentance/change of mind", "Confession", "Sorrow", "Turning"], "Repentance/change of mind"),
    ("bib_479", "What does 'apokalypsis' mean in Greek?", ["Revelation/unveiling", "End times", "Judgment", "Vision"], "Revelation/unveiling"),
    ("bib_480", "What does 'doxa' mean in Greek?", ["Glory/honor", "Praise", "Worship", "Majesty"], "Glory/honor"),
    ("bib_481", "What does 'hilasmos' mean in Greek?", ["Propitiation/atoning sacrifice", "Sacrifice", "Offering", "Atonement"], "Propitiation/atoning sacrifice"),
    ("bib_482", "What does 'parousia' mean in Greek?", ["Presence/coming/arrival", "Second coming", "Return", "Appearance"], "Presence/coming/arrival"),
]

for q in hard_languages:
    bible_languages.append({
        "id": q[0], "category": "Bible", "subcategory": "Bible Languages",
        "question": q[1], "options": q[2], "correct_answer": q[3],
        "difficulty": "hard", "topic": None, "subtopic": None
    })

print(f"Created {len(bible_languages)} Bible Languages questions")
print(f"  Easy: {len([q for q in bible_languages if q['difficulty'] == 'easy'])}")
print(f"  Medium: {len([q for q in bible_languages if q['difficulty'] == 'medium'])}")
print(f"  Hard: {len([q for q in bible_languages if q['difficulty'] == 'hard'])}")

# Load and update
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

data['categories']['Bible'].extend(bible_languages)
data['categories']['Bible'].sort(key=lambda q: int(q['id'].split('_')[1]))

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n✅ Added Bible Languages questions")
print(f"Bible category now has {len(data['categories']['Bible'])} questions")
