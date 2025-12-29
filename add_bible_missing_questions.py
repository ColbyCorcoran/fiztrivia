#!/usr/bin/env python3
"""Add questions to Biblical History, Biblical Theology, and Bible Languages"""
import json

# Biblical History - need 50 more (25 → 75)
# 17 easy, 17 medium, 16 hard

biblical_history = []

# Easy (17)
easy_history = [
    ("bib_328", "What sea did Moses part?", ["Red Sea", "Dead Sea", "Mediterranean Sea", "Sea of Galilee"], "Red Sea"),
    ("bib_329", "What walls fell after the Israelites marched around them?", ["Walls of Jericho", "Walls of Jerusalem", "Walls of Babylon", "Walls of Damascus"], "Walls of Jericho"),
    ("bib_330", "What garden did God create for Adam and Eve?", ["Garden of Eden", "Garden of Gethsemane", "Hanging Gardens", "Garden of Olives"], "Garden of Eden"),
    ("bib_331", "What mountain did Moses receive the Ten Commandments on?", ["Mount Sinai", "Mount Zion", "Mount Olympus", "Mount Carmel"], "Mount Sinai"),
    ("bib_332", "What city was Jesus crucified in?", ["Jerusalem", "Bethlehem", "Nazareth", "Galilee"], "Jerusalem"),
    ("bib_333", "What river was Jesus baptized in?", ["Jordan River", "Nile River", "Euphrates River", "Tigris River"], "Jordan River"),
    ("bib_334", "How many plagues did God send on Egypt?", ["10", "7", "12", "40"], "10"),
    ("bib_335", "How many days did it rain during Noah's flood?", ["40 days and 40 nights", "7 days", "30 days", "100 days"], "40 days and 40 nights"),
    ("bib_336", "What tower did people try to build to reach heaven?", ["Tower of Babel", "Tower of David", "Tower of Siloam", "Tower of Antonia"], "Tower of Babel"),
    ("bib_337", "What sea did Jesus walk on water?", ["Sea of Galilee", "Red Sea", "Dead Sea", "Mediterranean Sea"], "Sea of Galilee"),
    ("bib_338", "What city did Jonah refuse to go to?", ["Nineveh", "Babylon", "Jerusalem", "Damascus"], "Nineveh"),
    ("bib_339", "Who was the first king of Israel?", ["Saul", "David", "Solomon", "Samuel"], "Saul"),
    ("bib_340", "What king built the first temple in Jerusalem?", ["Solomon", "David", "Saul", "Hezekiah"], "Solomon"),
    ("bib_341", "What valley did David fight Goliath in?", ["Valley of Elah", "Valley of Jezreel", "Kidron Valley", "Hinnom Valley"], "Valley of Elah"),
    ("bib_342", "Where was Jesus born?", ["Bethlehem", "Nazareth", "Jerusalem", "Galilee"], "Bethlehem"),
    ("bib_343", "What hill was Jesus crucified on?", ["Golgotha (Calvary)", "Mount of Olives", "Mount Zion", "Mount Sinai"], "Golgotha (Calvary)"),
    ("bib_344", "What island was John exiled to?", ["Patmos", "Cyprus", "Crete", "Malta"], "Patmos"),
]

for q in easy_history:
    biblical_history.append({
        "id": q[0], "category": "Bible", "subcategory": "Biblical History",
        "question": q[1], "options": q[2], "correct_answer": q[3],
        "difficulty": "easy", "topic": None, "subtopic": None
    })

# Medium (17)
medium_history = [
    ("bib_345", "What year did the Babylonian exile begin?", ["586 BC", "722 BC", "605 BC", "536 BC"], "586 BC"),
    ("bib_346", "Who was the Roman governor who sentenced Jesus?", ["Pontius Pilate", "Herod Antipas", "Pilate Felix", "Festus"], "Pontius Pilate"),
    ("bib_347", "What empire conquered the Northern Kingdom of Israel?", ["Assyria", "Babylon", "Persia", "Rome"], "Assyria"),
    ("bib_348", "What year did the Northern Kingdom fall?", ["722 BC", "586 BC", "605 BC", "536 BC"], "722 BC"),
    ("bib_349", "Who was the high priest when Jesus was arrested?", ["Caiaphas", "Annas", "Eli", "Ezra"], "Caiaphas"),
    ("bib_350", "What Roman road did Paul travel on?", ["Via Appia (Appian Way)", "Via Egnatia", "Via Maris", "King's Highway"], "Via Appia (Appian Way)"),
    ("bib_351", "What council decided Gentiles didn't need circumcision?", ["Council of Jerusalem", "Council of Nicaea", "Council of Ephesus", "Council of Chalcedon"], "Council of Jerusalem"),
    ("bib_352", "Who was Caesar when Jesus was born?", ["Caesar Augustus", "Julius Caesar", "Tiberius Caesar", "Nero Caesar"], "Caesar Augustus"),
    ("bib_353", "What Persian king allowed Jews to return from exile?", ["Cyrus the Great", "Darius", "Xerxes", "Artaxerxes"], "Cyrus the Great"),
    ("bib_354", "What empire ruled during Jesus' ministry?", ["Roman Empire", "Greek Empire", "Persian Empire", "Babylonian Empire"], "Roman Empire"),
    ("bib_355", "Who rebuilt the walls of Jerusalem?", ["Nehemiah", "Ezra", "Zerubbabel", "Joshua"], "Nehemiah"),
    ("bib_356", "What sea route connected Egypt and Mesopotamia?", ["Via Maris (Way of the Sea)", "King's Highway", "Silk Road", "Incense Route"], "Via Maris (Way of the Sea)"),
    ("bib_357", "What Jewish revolt happened in 70 AD?", ["First Jewish-Roman War", "Bar Kokhba revolt", "Maccabean Revolt", "Zealot uprising"], "First Jewish-Roman War"),
    ("bib_358", "Who was the Jewish historian who wrote about first century?", ["Josephus", "Philo", "Eusebius", "Tacitus"], "Josephus"),
    ("bib_359", "What city was Paul from?", ["Tarsus", "Jerusalem", "Damascus", "Antioch"], "Tarsus"),
    ("bib_360", "What Roman emperor destroyed Jerusalem's temple?", ["Titus (under Vespasian)", "Nero", "Hadrian", "Constantine"], "Titus (under Vespasian)"),
    ("bib_361", "What mountain range is near Jerusalem?", ["Judean Hills", "Lebanon Mountains", "Mount Carmel", "Mount Hermon"], "Judean Hills"),
]

for q in medium_history:
    biblical_history.append({
        "id": q[0], "category": "Bible", "subcategory": "Biblical History",
        "question": q[1], "options": q[2], "correct_answer": q[3],
        "difficulty": "medium", "topic": None, "subtopic": None
    })

# Hard (16)
hard_history = [
    ("bib_362", "What year did Constantine legalize Christianity?", ["313 AD (Edict of Milan)", "325 AD", "380 AD", "300 AD"], "313 AD (Edict of Milan)"),
    ("bib_363", "Who was the last judge of Israel?", ["Samuel", "Eli", "Gideon", "Samson"], "Samuel"),
    ("bib_364", "What Hasmonean dynasty leader rededicated the temple?", ["Judas Maccabeus", "Simon Maccabeus", "John Hyrcanus", "Alexander Jannaeus"], "Judas Maccabeus"),
    ("bib_365", "What year was the Septuagint translated?", ["3rd-2nd century BC", "1st century BC", "1st century AD", "2nd century AD"], "3rd-2nd century BC"),
    ("bib_366", "Who was the Nabatean king mentioned in 2 Corinthians?", ["Aretas IV", "Herod the Great", "Agrippa", "Antipater"], "Aretas IV"),
    ("bib_367", "What Roman province was Judea part of?", ["Syria", "Asia", "Macedonia", "Galatia"], "Syria"),
    ("bib_368", "Who was the Idumean father of Herod the Great?", ["Antipater", "Herod Antipas", "Philip", "Archelaus"], "Antipater"),
    ("bib_369", "What year did the Dead Sea Scrolls originate?", ["3rd century BC - 1st century AD", "1st century AD only", "2nd century AD", "Before 500 BC"], "3rd century BC - 1st century AD"),
    ("bib_370", "Who was the Roman prefect after Pontius Pilate?", ["Marullus", "Felix", "Festus", "Fadus"], "Marullus"),
    ("bib_371", "What Jewish sect lived at Qumran?", ["Essenes", "Pharisees", "Sadducees", "Zealots"], "Essenes"),
    ("bib_372", "What year did Herod's temple construction begin?", ["20 BC", "37 BC", "4 BC", "10 BC"], "20 BC"),
    ("bib_373", "Who was the Herodian tetrarch of Galilee during Jesus' ministry?", ["Herod Antipas", "Philip", "Archelaus", "Herod the Great"], "Herod Antipas"),
    ("bib_374", "What revolt led by Simon bar Kokhba occurred when?", ["132-135 AD", "70 AD", "66-73 AD", "115 AD"], "132-135 AD"),
    ("bib_375", "Who was the procurator who sent Paul to Rome?", ["Porcius Festus", "Felix", "Pontius Pilate", "Fadus"], "Porcius Festus"),
    ("bib_376", "What synagogue inscription mentions Theodotos?", ["Theodotos inscription (Jerusalem)", "Delos inscription", "Sardis inscription", "Ostia inscription"], "Theodotos inscription (Jerusalem)"),
    ("bib_377", "What year did Rome make Judea a province?", ["6 AD", "4 BC", "70 AD", "63 BC"], "6 AD"),
]

for q in hard_history:
    biblical_history.append({
        "id": q[0], "category": "Bible", "subcategory": "Biblical History",
        "question": q[1], "options": q[2], "correct_answer": q[3],
        "difficulty": "hard", "topic": None, "subtopic": None
    })

print(f"Created {len(biblical_history)} Biblical History questions")
print(f"  Easy: {len([q for q in biblical_history if q['difficulty'] == 'easy'])}")
print(f"  Medium: {len([q for q in biblical_history if q['difficulty'] == 'medium'])}")
print(f"  Hard: {len([q for q in biblical_history if q['difficulty'] == 'hard'])}")

# Load and update
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

data['categories']['Bible'].extend(biblical_history)
data['categories']['Bible'].sort(key=lambda q: int(q['id'].split('_')[1]))

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n✅ Added Biblical History questions")
print(f"Bible category now has {len(data['categories']['Bible'])} questions")
