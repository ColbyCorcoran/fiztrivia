#!/usr/bin/env python3
"""Add 53 Biblical Theology questions (22 → 75)"""
import json

biblical_theology = []

# Easy (18)
easy_theology = [
    ("bib_378", "What does the word 'Messiah' mean?", ["Anointed One", "Savior", "King", "Prophet"], "Anointed One"),
    ("bib_379", "What does 'Immanuel' mean?", ["God with us", "Prince of Peace", "Mighty God", "Wonderful Counselor"], "God with us"),
    ("bib_380", "What is the Great Commission?", ["Go and make disciples", "Love your neighbor", "Keep the Sabbath", "Honor your parents"], "Go and make disciples"),
    ("bib_381", "What does 'repentance' mean?", ["Turning away from sin", "Feeling sorry", "Confession only", "Baptism"], "Turning away from sin"),
    ("bib_382", "What is the greatest commandment?", ["Love the Lord your God", "Do not murder", "Keep the Sabbath", "Honor parents"], "Love the Lord your God"),
    ("bib_383", "What does 'redemption' mean?", ["Buying back/deliverance", "Forgiveness", "Salvation only", "Baptism"], "Buying back/deliverance"),
    ("bib_384", "What is the second greatest commandment?", ["Love your neighbor as yourself", "Keep the Sabbath", "Honor parents", "Do not steal"], "Love your neighbor as yourself"),
    ("bib_385", "What does 'covenant' mean?", ["Sacred agreement", "Law", "Commandment", "Promise only"], "Sacred agreement"),
    ("bib_386", "What is the fruit of the Spirit?", ["Love, joy, peace, etc.", "Faith only", "Hope only", "Charity only"], "Love, joy, peace, etc."),
    ("bib_387", "What does 'amen' mean?", ["So be it/truly", "The end", "Goodbye", "Thank you"], "So be it/truly"),
    ("bib_388", "What does 'sanctification' mean?", ["Being made holy", "Salvation", "Baptism", "Forgiveness"], "Being made holy"),
    ("bib_389", "What is the armor of God?", ["Spiritual protection equipment", "Physical armor", "Military equipment", "Church building"], "Spiritual protection equipment"),
    ("bib_390", "What does 'omnipotent' mean?", ["All-powerful", "All-knowing", "Everywhere present", "Eternal"], "All-powerful"),
    ("bib_391", "What does 'omniscient' mean?", ["All-knowing", "All-powerful", "Everywhere present", "Eternal"], "All-knowing"),
    ("bib_392", "What does 'omnipresent' mean?", ["Everywhere present", "All-knowing", "All-powerful", "Eternal"], "Everywhere present"),
    ("bib_393", "What is original sin?", ["Sin inherited from Adam", "First sin only", "Unforgivable sin", "Baptism"], "Sin inherited from Adam"),
    ("bib_394", "What does 'eternal life' refer to?", ["Life forever with God", "Long life on earth", "Reincarnation", "Resurrection only"], "Life forever with God"),
    ("bib_395", "What is the Golden Rule?", ["Treat others as you want to be treated", "Love God", "Keep commandments", "Go to church"], "Treat others as you want to be treated"),
]

for q in easy_theology:
    biblical_theology.append({
        "id": q[0], "category": "Bible", "subcategory": "Biblical Theology",
        "question": q[1], "options": q[2], "correct_answer": q[3],
        "difficulty": "easy", "topic": None, "subtopic": None
    })

# Medium (18)
medium_theology = [
    ("bib_396", "What is the theological term for God's foreknowledge?", ["Prescience", "Providence", "Predestination", "Omniscience"], "Prescience"),
    ("bib_397", "What does 'propitiation' mean?", ["Atoning sacrifice", "Prayer", "Worship", "Offering"], "Atoning sacrifice"),
    ("bib_398", "What is the theological term for Christ's return?", ["Parousia/Second Coming", "Rapture only", "Judgment", "Resurrection"], "Parousia/Second Coming"),
    ("bib_399", "What does 'eschatology' study?", ["End times/last things", "Church history", "Old Testament", "Creation"], "End times/last things"),
    ("bib_400", "What is the doctrine of the hypostatic union?", ["Christ's divine and human natures", "Trinity", "Salvation", "Church unity"], "Christ's divine and human natures"),
    ("bib_401", "What does 'soteriology' study?", ["Salvation", "God's nature", "End times", "Church"], "Salvation"),
    ("bib_402", "What is the theological term for Christ's resurrection appearance?", ["Christophany", "Theophany", "Epiphany", "Manifestation"], "Christophany"),
    ("bib_403", "What does 'ecclesiology' study?", ["The Church", "Salvation", "End times", "God's nature"], "The Church"),
    ("bib_404", "What is the doctrine of imago Dei?", ["Humans made in God's image", "Christ's image", "Trinity", "Salvation"], "Humans made in God's image"),
    ("bib_405", "What does 'pneumatology' study?", ["The Holy Spirit", "The Church", "Salvation", "Angels"], "The Holy Spirit"),
    ("bib_406", "What is the theological term for Christ's sacrifice?", ["Atonement", "Redemption only", "Salvation only", "Grace only"], "Atonement"),
    ("bib_407", "What does 'theodicy' address?", ["Problem of evil and God's justice", "End times", "Salvation", "Church doctrine"], "Problem of evil and God's justice"),
    ("bib_408", "What is the doctrine of sola scriptura?", ["Scripture alone as authority", "Faith alone", "Grace alone", "Christ alone"], "Scripture alone as authority"),
    ("bib_409", "What does 'anthropology' study in theology?", ["Doctrine of humanity", "Study of angels", "Study of Christ", "Study of salvation"], "Doctrine of humanity"),
    ("bib_410", "What is the theological term for God's undeserved favor?", ["Grace", "Mercy", "Love", "Kindness"], "Grace"),
    ("bib_411", "What does 'Christology' study?", ["Person and work of Christ", "The Church", "Salvation", "End times"], "Person and work of Christ"),
    ("bib_412", "What is the doctrine of total depravity?", ["Sin affects all of humanity", "All sins are equal", "Original sin only", "Unforgivable sin"], "Sin affects all of humanity"),
    ("bib_413", "What does 'hamartiology' study?", ["Sin", "Salvation", "Church", "End times"], "Sin"),
]

for q in medium_theology:
    biblical_theology.append({
        "id": q[0], "category": "Bible", "subcategory": "Biblical Theology",
        "question": q[1], "options": q[2], "correct_answer": q[3],
        "difficulty": "medium", "topic": None, "subtopic": None
    })

# Hard (17)
hard_theology = [
    ("bib_414", "What is the doctrine of penal substitutionary atonement?", ["Christ bore punishment for sins", "Christ as example only", "Christ as teacher", "Universal salvation"], "Christ bore punishment for sins"),
    ("bib_415", "What does 'kenosis' refer to?", ["Christ's self-emptying", "Incarnation", "Atonement", "Resurrection"], "Christ's self-emptying"),
    ("bib_416", "What is the communicatio idiomatum?", ["Sharing of divine/human attributes in Christ", "Trinity", "Atonement", "Salvation"], "Sharing of divine/human attributes in Christ"),
    ("bib_417", "What is the doctrine of imputation?", ["Crediting righteousness to believers", "Original sin", "Sanctification", "Baptism"], "Crediting righteousness to believers"),
    ("bib_418", "What is Arianism?", ["Heresy denying Christ's divinity", "Monotheism", "Trinitarianism", "Gnosticism"], "Heresy denying Christ's divinity"),
    ("bib_419", "What is the economic Trinity?", ["Roles of Trinity in salvation", "Essential Trinity", "Social Trinity", "Modalism"], "Roles of Trinity in salvation"),
    ("bib_420", "What does 'perichoresis' describe?", ["Mutual indwelling of Trinity", "Incarnation", "Atonement", "Sanctification"], "Mutual indwelling of Trinity"),
    ("bib_421", "What is the doctrine of divine simplicity?", ["God has no parts", "God is one", "God is three", "God is eternal"], "God has no parts"),
    ("bib_422", "What is Pelagianism?", ["Heresy denying original sin's effect", "Salvation by works", "Denial of Trinity", "Gnosticism"], "Heresy denying original sin's effect"),
    ("bib_423", "What is the doctrine of supralapsarianism?", ["Election before the Fall", "Election after the Fall", "Universal election", "No election"], "Election before the Fall"),
    ("bib_424", "What is traducianism?", ["Soul inherited from parents", "Soul created by God", "Pre-existing soul", "No soul"], "Soul inherited from parents"),
    ("bib_425", "What is the Nestorian controversy about?", ["Two persons in Christ (heresy)", "Two natures in Christ", "One nature in Christ", "Christ's divinity"], "Two persons in Christ (heresy)"),
    ("bib_426", "What is the doctrine of irresistible grace?", ["Effectual calling of elect", "Universal call", "Resistible grace", "No grace"], "Effectual calling of elect"),
    ("bib_427", "What is monophysitism?", ["Christ has one nature (heresy)", "Christ has two natures", "Christ has no human nature", "Christ is not divine"], "Christ has one nature (heresy)"),
    ("bib_428", "What is the doctrine of eternal generation?", ["Son eternally begotten from Father", "Son created by Father", "Son adopted by Father", "Son equal to Father"], "Son eternally begotten from Father"),
    ("bib_429", "What is the Filioque controversy?", ["Spirit proceeds from Father and Son", "Spirit proceeds from Father only", "Spirit is created", "Spirit is not divine"], "Spirit proceeds from Father and Son"),
    ("bib_430", "What is creationism in soul origin?", ["God creates each soul", "Soul inherited from parents", "Pre-existing souls", "No soul"], "God creates each soul"),
]

for q in hard_theology:
    biblical_theology.append({
        "id": q[0], "category": "Bible", "subcategory": "Biblical Theology",
        "question": q[1], "options": q[2], "correct_answer": q[3],
        "difficulty": "hard", "topic": None, "subtopic": None
    })

print(f"Created {len(biblical_theology)} Biblical Theology questions")
print(f"  Easy: {len([q for q in biblical_theology if q['difficulty'] == 'easy'])}")
print(f"  Medium: {len([q for q in biblical_theology if q['difficulty'] == 'medium'])}")
print(f"  Hard: {len([q for q in biblical_theology if q['difficulty'] == 'hard'])}")

# Load and update
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

data['categories']['Bible'].extend(biblical_theology)
data['categories']['Bible'].sort(key=lambda q: int(q['id'].split('_')[1]))

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n✅ Added Biblical Theology questions")
print(f"Bible category now has {len(data['categories']['Bible'])} questions")
