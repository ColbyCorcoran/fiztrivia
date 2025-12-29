#!/usr/bin/env python3
"""Add 60 Musicians & Bands questions from scratch"""
import json

#60 questions (20 easy, 20 medium, 20 hard)
new_questions = []

# Easy questions (20)
easy = [
    ("mus_121", "Who is known as the 'King of Pop'?", ["Michael Jackson", "Prince", "Elvis Presley", "Freddie Mercury"], "Michael Jackson"),
    ("mus_122", "Which band consisted of John, Paul, George, and Ringo?", ["The Beatles", "The Rolling Stones", "The Who", "Led Zeppelin"], "The Beatles"),
    ("mus_123", "Who was the lead singer of Queen?", ["Freddie Mercury", "David Bowie", "Mick Jagger", "Robert Plant"], "Freddie Mercury"),
    ("mus_124", "Which artist is known as the 'King of Rock and Roll'?", ["Elvis Presley", "Chuck Berry", "Little Richard", "Jerry Lee Lewis"], "Elvis Presley"),
    ("mus_125", "Who is the lead vocalist of U2?", ["Bono", "The Edge", "Adam Clayton", "Larry Mullen Jr."], "Bono"),
    ("mus_126", "Which band had members Mick Jagger and Keith Richards?", ["The Rolling Stones", "The Beatles", "The Kinks", "The Yardbirds"], "The Rolling Stones"),
    ("mus_127", "Who sang 'Purple Rain'?", ["Prince", "Michael Jackson", "Stevie Wonder", "Lionel Richie"], "Prince"),
    ("mus_128", "Which band performed 'Stairway to Heaven'?", ["Led Zeppelin", "Pink Floyd", "The Who", "Deep Purple"], "Led Zeppelin"),
    ("mus_129", "Who is known as 'The Boss'?", ["Bruce Springsteen", "Bob Dylan", "Tom Petty", "Billy Joel"], "Bruce Springsteen"),
    ("mus_130", "Which band did Kurt Cobain lead?", ["Nirvana", "Pearl Jam", "Soundgarden", "Alice in Chains"], "Nirvana"),
    ("mus_131", "Who was the lead guitarist of Jimi Hendrix Experience?", ["Jimi Hendrix", "Eric Clapton", "Jimmy Page", "Jeff Beck"], "Jimi Hendrix"),
    ("mus_132", "Which band released the album 'Abbey Road'?", ["The Beatles", "The Rolling Stones", "Pink Floyd", "The Who"], "The Beatles"),
    ("mus_133", "Who is known as the 'Queen of Soul'?", ["Aretha Franklin", "Etta James", "Diana Ross", "Tina Turner"], "Aretha Franklin"),
    ("mus_134", "Which band had Axl Rose as lead singer?", ["Guns N' Roses", "Mötley Crüe", "Bon Jovi", "Def Leppard"], "Guns N' Roses"),
    ("mus_135", "Who was the frontman of The Doors?", ["Jim Morrison", "Janis Joplin", "Jimi Hendrix", "Jerry Garcia"], "Jim Morrison"),
    ("mus_136", "Which artist released the album 'Thriller'?", ["Michael Jackson", "Prince", "Madonna", "Whitney Houston"], "Michael Jackson"),
    ("mus_137", "Who founded Motown Records?", ["Berry Gordy", "Quincy Jones", "Phil Spector", "Clive Davis"], "Berry Gordy"),
    ("mus_138", "Which band performed 'Smells Like Teen Spirit'?", ["Nirvana", "Pearl Jam", "Soundgarden", "Stone Temple Pilots"], "Nirvana"),
    ("mus_139", "Who is known as 'The Godfather of Soul'?", ["James Brown", "Ray Charles", "Sam Cooke", "Otis Redding"], "James Brown"),
    ("mus_140", "Which duo consisted of Simon and Garfunkel?", ["Paul Simon and Art Garfunkel", "Hall and Oates", "The Everly Brothers", "Sam and Dave"], "Paul Simon and Art Garfunkel"),
]

for q in easy:
    new_questions.append({"id": q[0], "category": "Music", "subcategory": "Musicians & Bands", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "easy", "topic": None, "subtopic": None})

# Medium questions (20)
medium = [
    ("mus_141", "Which band's original lineup included Syd Barrett?", ["Pink Floyd", "The Who", "The Kinks", "The Yardbirds"], "Pink Floyd"),
    ("mus_142", "Who was the drummer for The Beatles?", ["Ringo Starr", "Pete Best", "John Bonham", "Keith Moon"], "Ringo Starr"),
    ("mus_143", "Which guitarist played with both The Yardbirds and Cream?", ["Eric Clapton", "Jeff Beck", "Jimmy Page", "Pete Townshend"], "Eric Clapton"),
    ("mus_144", "Who replaced Brian Jones in The Rolling Stones?", ["Mick Taylor", "Ron Wood", "Bill Wyman", "Ian Stewart"], "Mick Taylor"),
    ("mus_145", "Which band did Dave Grohl join after Nirvana?", ["Foo Fighters (as founder)", "Queens of the Stone Age", "Them Crooked Vultures", "Probot"], "Foo Fighters (as founder)"),
    ("mus_146", "Who was the bassist for Led Zeppelin?", ["John Paul Jones", "John Bonham", "Jimmy Page", "Robert Plant"], "John Paul Jones"),
    ("mus_147", "Which artist is known for the album '21'?", ["Adele", "Taylor Swift", "Beyoncé", "Rihanna"], "Adele"),
    ("mus_148", "Who founded The Beach Boys?", ["Brian Wilson and family", "Mike Love", "Dennis Wilson", "Carl Wilson"], "Brian Wilson and family"),
    ("mus_149", "Which band had Debbie Harry as lead singer?", ["Blondie", "The Pretenders", "Talking Heads", "The B-52's"], "Blondie"),
    ("mus_150", "Who was the lead singer of Soundgarden?", ["Chris Cornell", "Eddie Vedder", "Layne Staley", "Kurt Cobain"], "Chris Cornell"),
    ("mus_151", "Which duo created the album 'Bridge Over Troubled Water'?", ["Simon & Garfunkel", "The Everly Brothers", "Hall & Oates", "Daryl Hall and John Oates"], "Simon & Garfunkel"),
    ("mus_152", "Who was the original lead singer of Genesis?", ["Peter Gabriel", "Phil Collins", "Tony Banks", "Steve Hackett"], "Peter Gabriel"),
    ("mus_153", "Which band featured brothers Malcolm and Angus Young?", ["AC/DC", "Van Halen", "Aerosmith", "ZZ Top"], "AC/DC"),
    ("mus_154", "Who was Tina Turner's former husband and musical partner?", ["Ike Turner", "Phil Spector", "Quincy Jones", "Berry Gordy"], "Ike Turner"),
    ("mus_155", "Which band did Sting originally perform with?", ["The Police", "Genesis", "Talking Heads", "The Clash"], "The Police"),
    ("mus_156", "Who is the lead singer of Aerosmith?", ["Steven Tyler", "Joe Perry", "Tom Hamilton", "Brad Whitford"], "Steven Tyler"),
    ("mus_157", "Which artist released the album 'Purple Rain'?", ["Prince", "Michael Jackson", "Stevie Wonder", "George Clinton"], "Prince"),
    ("mus_158", "Who founded Parliament-Funkadelic?", ["George Clinton", "Bootsy Collins", "Bernie Worrell", "James Brown"], "George Clinton"),
    ("mus_159", "Which band features brothers Liam and Noel Gallagher?", ["Oasis", "Blur", "Radiohead", "The Verve"], "Oasis"),
    ("mus_160", "Who was the keyboardist for The Doors?", ["Ray Manzarek", "John Densmore", "Robby Krieger", "Jim Morrison"], "Ray Manzarek"),
]

for q in medium:
    new_questions.append({"id": q[0], "category": "Music", "subcategory": "Musicians & Bands", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "medium", "topic": None, "subtopic": None})

# Hard questions (20)
hard = [
    ("mus_161", "Which guitarist replaced Mick Taylor in The Rolling Stones?", ["Ron Wood", "Mick Ronson", "Keith Richards", "Brian Jones"], "Ron Wood"),
    ("mus_162", "Who was the original drummer for The Who?", ["Keith Moon", "Kenney Jones", "Pete Townshend", "John Entwistle"], "Keith Moon"),
    ("mus_163", "Which bassist was a founding member of both The Yardbirds and Led Zeppelin?", ["None - different bassists", "John Paul Jones", "Paul Samwell-Smith", "Chris Dreja"], "None - different bassists"),
    ("mus_164", "Who produced The Beatles' album 'Sgt. Pepper's Lonely Hearts Club Band'?", ["George Martin", "Phil Spector", "Brian Epstein", "Glyn Johns"], "George Martin"),
    ("mus_165", "Which artist founded Paisley Park Records?", ["Prince", "Janet Jackson", "The Time", "Sheila E."], "Prince"),
    ("mus_166", "Who was the original lead guitarist of Guns N' Roses?", ["Slash", "Izzy Stradlin", "Tracii Guns", "Gilby Clarke"], "Slash"),
    ("mus_167", "Which keyboardist co-founded Pink Floyd?", ["Rick Wright", "Roger Waters", "David Gilmour", "Syd Barrett"], "Rick Wright"),
    ("mus_168", "Who was the drummer for Cream?", ["Ginger Baker", "Mitch Mitchell", "John Bonham", "Keith Moon"], "Ginger Baker"),
    ("mus_169", "Which saxophonist played with The E Street Band?", ["Clarence Clemons", "David Sanborn", "Kenny G", "Lenny Pickett"], "Clarence Clemons"),
    ("mus_170", "Who was the original bassist for Metallica?", ["Cliff Burton", "Jason Newsted", "Robert Trujillo", "Ron McGovney"], "Cliff Burton"),
    ("mus_171", "Which artist founded Death Row Records with Suge Knight?", ["Dr. Dre", "Tupac Shakur", "Snoop Dogg", "The D.O.C."], "Dr. Dre"),
    ("mus_172", "Who was the original singer of Journey before Steve Perry?", ["Gregg Rolie", "Robert Fleischman", "Steve Augeri", "Jeff Scott Soto"], "Gregg Rolie"),
    ("mus_173", "Which guitarist co-founded The Velvet Underground?", ["Sterling Morrison and Lou Reed", "John Cale", "Maureen Tucker", "Nico"], "Sterling Morrison and Lou Reed"),
    ("mus_174", "Who was the drummer for The Jimi Hendrix Experience?", ["Mitch Mitchell", "Buddy Miles", "Ginger Baker", "Keith Moon"], "Mitch Mitchell"),
    ("mus_175", "Which bassist founded The Smiths with Morrissey?", ["Johnny Marr (guitarist), Andy Rourke was bassist", "Mike Joyce", "Craig Gannon", "Andy Rourke"], "Johnny Marr (guitarist), Andy Rourke was bassist"),
    ("mus_176", "Who produced My Bloody Valentine's 'Loveless'?", ["Kevin Shields", "Alan Moulder", "Flood", "Brian Eno"], "Kevin Shields"),
    ("mus_177", "Which drummer founded The Strawbs before joining Yes?", ["Bill Bruford", "Alan White", "Tony Kaye", "Rick Wakeman"], "Bill Bruford"),
    ("mus_178", "Who was the original bassist for The Sex Pistols?", ["Glen Matlock", "Sid Vicious", "Paul Cook", "Steve Jones"], "Glen Matlock"),
    ("mus_179", "Which guitarist played on David Bowie's 'Ziggy Stardust'?", ["Mick Ronson", "Carlos Alomar", "Reeves Gabrels", "Earl Slick"], "Mick Ronson"),
    ("mus_180", "Who was the keyboardist for The Band?", ["Garth Hudson", "Richard Manuel", "Levon Helm", "Robbie Robertson"], "Garth Hudson"),
]

for q in hard:
    new_questions.append({"id": q[0], "category": "Music", "subcategory": "Musicians & Bands", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "hard", "topic": None, "subtopic": None})

# Load, add, sort, save
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

data['categories']['Music'].extend(new_questions)
data['categories']['Music'].sort(key=lambda q: int(q['id'].split('_')[1]))

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added 60 Musicians & Bands questions")
print(f"Music now has {len(data['categories']['Music'])} total questions")
print(f"Added: 20 easy, 20 medium, 20 hard")
