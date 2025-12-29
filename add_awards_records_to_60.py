#!/usr/bin/env python3
"""Add 60 Awards & Records questions from scratch"""
import json

new_questions = []

# Easy questions (20)
easy = [
    ("mus_181", "Which artist has won the most Grammy Awards in history?", ["Beyoncé", "Quincy Jones", "Georg Solti", "Alison Krauss"], "Beyoncé"),
    ("mus_182", "What does a 'platinum' record certification represent in the US?", ["1 million copies sold", "500,000 copies sold", "2 million copies sold", "10 million copies sold"], "1 million copies sold"),
    ("mus_183", "Which award show features a moon man trophy?", ["MTV Video Music Awards", "Grammy Awards", "American Music Awards", "Billboard Music Awards"], "MTV Video Music Awards"),
    ("mus_184", "What is the highest certification level for album sales?", ["Diamond (10+ million)", "Platinum", "Multi-Platinum", "Gold"], "Diamond (10+ million)"),
    ("mus_185", "Which artist holds the record for most #1 hits on the Billboard Hot 100?", ["The Beatles", "Mariah Carey", "Drake", "Rihanna"], "The Beatles"),
    ("mus_186", "What is the Grammy Award for Best New Artist called?", ["Best New Artist", "Breakthrough Artist", "Rising Star", "New Talent"], "Best New Artist"),
    ("mus_187", "Which song spent the most weeks at #1 on the Billboard Hot 100?", ["Old Town Road (19 weeks)", "Despacito", "One Sweet Day", "Uptown Funk"], "Old Town Road (19 weeks)"),
    ("mus_188", "What color is a gold record certification?", ["Gold", "Silver", "Bronze", "Platinum"], "Gold"),
    ("mus_189", "Which awards show is organized by the Recording Academy?", ["Grammy Awards", "American Music Awards", "Billboard Music Awards", "MTV VMAs"], "Grammy Awards"),
    ("mus_190", "What does BMA stand for in music awards?", ["Billboard Music Awards", "British Music Awards", "Best Music Awards", "Black Music Awards"], "Billboard Music Awards"),
    ("mus_191", "Which artist has the most American Music Awards?", ["Taylor Swift", "Michael Jackson", "Whitney Houston", "Drake"], "Taylor Swift"),
    ("mus_192", "What is the UK equivalent of the Grammy Awards?", ["BRIT Awards", "Mercury Prize", "Ivor Novello Awards", "MOBO Awards"], "BRIT Awards"),
    ("mus_193", "Which album is the best-selling of all time?", ["Thriller by Michael Jackson", "Back in Black by AC/DC", "The Dark Side of the Moon by Pink Floyd", "Rumours by Fleetwood Mac"], "Thriller by Michael Jackson"),
    ("mus_194", "What does AMA stand for in music awards?", ["American Music Awards", "Artist Music Awards", "Alternative Music Awards", "Annual Music Awards"], "American Music Awards"),
    ("mus_195", "Which artist won Album of the Year at the Grammys in 2021?", ["Taylor Swift (Folklore)", "Beyoncé", "Dua Lipa", "Post Malone"], "Taylor Swift (Folklore)"),
    ("mus_196", "What certification comes before platinum?", ["Gold", "Silver", "Bronze", "Multi-Gold"], "Gold"),
    ("mus_197", "Which band has sold the most albums worldwide?", ["The Beatles", "Led Zeppelin", "Pink Floyd", "Queen"], "The Beatles"),
    ("mus_198", "What is the trophy for a Grammy Award shaped like?", ["Gramophone", "Microphone", "Music note", "Vinyl record"], "Gramophone"),
    ("mus_199", "Which artist has won the most MTV Video Music Awards?", ["Beyoncé", "Madonna", "Lady Gaga", "Taylor Swift"], "Beyoncé"),
    ("mus_200", "What award recognizes songwriting achievement?", ["Grammy for Song of the Year", "Record of the Year", "Album of the Year", "Best New Artist"], "Grammy for Song of the Year"),
]

for q in easy:
    new_questions.append({"id": q[0], "category": "Music", "subcategory": "Awards & Records", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "easy", "topic": None, "subtopic": None})

# Medium questions (20)
medium = [
    ("mus_201", "Who was the first woman to win the Grammy for Album of the Year twice?", ["Taylor Swift", "Adele", "Beyoncé", "Alison Krauss"], "Taylor Swift"),
    ("mus_202", "Which album won the first-ever Grammy for Album of the Year in 1959?", ["The Music from Peter Gunn by Henry Mancini", "Frank Sinatra's album", "Ella Fitzgerald's album", "Nat King Cole's album"], "The Music from Peter Gunn by Henry Mancini"),
    ("mus_203", "How many Grammy Awards has Quincy Jones won?", ["28", "32", "25", "30"], "28"),
    ("mus_204", "Which artist refused their Grammy Award in 1991?", ["Sinéad O'Connor", "Prince", "Public Enemy", "Bob Dylan"], "Sinéad O'Connor"),
    ("mus_205", "What was the first rap album to win a Grammy?", ["DJ Jazzy Jeff & The Fresh Prince - 'He's the DJ, I'm the Rapper'", "Run-DMC's 'Raising Hell'", "Public Enemy's album", "N.W.A's album"], "DJ Jazzy Jeff & The Fresh Prince - 'He's the DJ, I'm the Rapper'"),
    ("mus_206", "Which artist has the most platinum-certified albums?", ["Garth Brooks or The Beatles (tied)", "Elvis Presley", "Led Zeppelin", "Michael Jackson"], "Garth Brooks or The Beatles (tied)"),
    ("mus_207", "Who is the youngest person to win a Grammy Award?", ["Leah Peasall (8 years old)", "Blue Ivy Carter", "Stevie Wonder", "LeAnn Rimes"], "Leah Peasall (8 years old)"),
    ("mus_208", "Which song holds the record for most weeks on the Billboard Hot 100?", ["Radioactive by Imagine Dragons (87 weeks)", "Blinding Lights", "Shape of You", "Uptown Funk"], "Radioactive by Imagine Dragons (87 weeks)"),
    ("mus_209", "Who won the most Grammys in a single night?", ["Beyoncé and Michael Jackson (tied at 8)", "Santana", "Adele", "U2"], "Beyoncé and Michael Jackson (tied at 8)"),
    ("mus_210", "Which album spent the most consecutive weeks at #1 on Billboard?", ["West Side Story soundtrack (54 weeks)", "Thriller", "Rumours", "21 by Adele"], "West Side Story soundtrack (54 weeks)"),
    ("mus_211", "Who was the first hip-hop artist to win a Grammy?", ["DJ Jazzy Jeff & The Fresh Prince", "Run-DMC", "LL Cool J", "Public Enemy"], "DJ Jazzy Jeff & The Fresh Prince"),
    ("mus_212", "Which artist has spent the most cumulative weeks at #1 on Billboard Hot 100?", ["Mariah Carey", "The Beatles", "Drake", "Rihanna"], "Mariah Carey"),
    ("mus_213", "What was the first music video to win a Grammy?", ["No specific 'first' - category added in 1982", "Thriller", "Money for Nothing", "Take On Me"], "No specific 'first' - category added in 1982"),
    ("mus_214", "Which artist has the most Billboard Hot 100 entries?", ["Drake", "Lil Wayne", "Elvis Presley", "The Glee Cast"], "Drake"),
    ("mus_215", "Who won the first Grammy for Best Rap Solo Performance?", ["LL Cool J", "MC Hammer", "Tupac", "Dr. Dre"], "LL Cool J"),
    ("mus_216", "Which album won Album of the Year at the 2020 Grammys?", ["When We All Fall Asleep, Where Do We Go? by Billie Eilish", "Thank U, Next by Ariana Grande", "Norman F---ing Rockwell! by Lana Del Rey", "i,i by Bon Iver"], "When We All Fall Asleep, Where Do We Go? by Billie Eilish"),
    ("mus_217", "Who has won the most Country Music Association Awards?", ["George Strait", "Alan Jackson", "Brooks & Dunn", "Garth Brooks"], "George Strait"),
    ("mus_218", "Which song won Record of the Year at the 1985 Grammys?", ["What's Love Got to Do with It by Tina Turner", "When Doves Cry", "Against All Odds", "Time After Time"], "What's Love Got to Do with It by Tina Turner"),
    ("mus_219", "Who is the most-awarded artist at the Billboard Music Awards?", ["Drake", "Taylor Swift", "The Weeknd", "Justin Bieber"], "Drake"),
    ("mus_220", "Which artist won the first MTV Video Music Award for Video of the Year?", ["The Cars - 'You Might Think'", "Michael Jackson - Thriller", "Madonna - Like a Virgin", "Prince - When Doves Cry"], "The Cars - 'You Might Think'"),
]

for q in medium:
    new_questions.append({"id": q[0], "category": "Music", "subcategory": "Awards & Records", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "medium", "topic": None, "subtopic": None})

# Hard questions (20)
hard = [
    ("mus_221", "Which conductor won the most Grammy Awards?", ["Georg Solti (31)", "Leonard Bernstein", "Pierre Boulez", "Herbert von Karajan"], "Georg Solti (31)"),
    ("mus_222", "What was the first album to be certified diamond (10x platinum)?", ["Thriller by Michael Jackson", "Eagles: Their Greatest Hits", "Led Zeppelin IV", "The Wall by Pink Floyd"], "Thriller by Michael Jackson"),
    ("mus_223", "Who won the Grammy for Best New Artist in 1965?", ["The Beatles", "Bob Dylan", "The Beach Boys", "The Supremes"], "The Beatles"),
    ("mus_224", "Which artist has the longest-running #1 album on Billboard?", ["West Side Story soundtrack", "Thriller", "Rumours", "21"], "West Side Story soundtrack"),
    ("mus_225", "Who was the first woman to win Producer of the Year at the Grammys?", ["Lauren Christy (as part of The Matrix in 2004)", "Linda Perry", "Sylvia Massy", "Sheryl Crow"], "Lauren Christy (as part of The Matrix in 2004)"),
    ("mus_226", "Which album won the Mercury Prize in 1992 (the first year)?", ["Screamadelica by Primal Scream", "Blue Lines by Massive Attack", "Leisure by Blur", "Shepherd Moons by Enya"], "Screamadelica by Primal Scream"),
    ("mus_227", "Who has the most consecutive #1 debuts on the Billboard 200?", ["DMX or Drake (depending on criteria)", "Jay-Z", "Eminem", "Kanye West"], "DMX or Drake (depending on criteria)"),
    ("mus_228", "Which artist won the Polar Music Prize first?", ["Paul McCartney", "Bob Dylan", "Sting", "Peter Gabriel"], "Paul McCartney"),
    ("mus_229", "What was the first song to debut at #1 on the Billboard Hot 100?", ["You Are Not Alone by Michael Jackson", "Fantasy by Mariah Carey", "I'll Be Missing You", "Candle in the Wind 1997"], "You Are Not Alone by Michael Jackson"),
    ("mus_230", "Who won the most MTV Europe Music Awards?", ["Justin Bieber", "Lady Gaga", "Eminem", "Taylor Swift"], "Justin Bieber"),
    ("mus_231", "Which classical album sold the most copies?", ["The Three Tenors in Concert", "Switched-On Bach", "Vivaldi's Four Seasons", "Carmina Burana"], "The Three Tenors in Concert"),
    ("mus_232", "Who was the first Latin artist to win Album of the Year at the Grammys?", ["Carlos Santana (Supernatural)", "Gloria Estefan", "Ricky Martin", "Marc Anthony"], "Carlos Santana (Supernatural)"),
    ("mus_233", "Which artist has the most Diamond-certified singles?", ["Bruno Mars", "Katy Perry", "Rihanna", "Ed Sheeran"], "Bruno Mars"),
    ("mus_234", "Who won the first Grammy for Best Hard Rock/Metal Performance?", ["Jethro Tull", "Metallica", "AC/DC", "Guns N' Roses"], "Jethro Tull"),
    ("mus_235", "Which album spent the most total weeks on the Billboard 200?", ["The Dark Side of the Moon by Pink Floyd", "Rumours", "Legend by Bob Marley", "Thriller"], "The Dark Side of the Moon by Pink Floyd"),
    ("mus_236", "Who was the youngest Album of the Year Grammy winner?", ["Taylor Swift (20 years old)", "Billie Eilish", "Stevie Wonder", "Alanis Morissette"], "Taylor Swift (20 years old)"),
    ("mus_237", "Which artist has the most simultaneous Billboard Hot 100 entries?", ["Drake (27 songs)", "The Beatles", "Lil Wayne", "Taylor Swift"], "Drake (27 songs)"),
    ("mus_238", "Who won the first Grammy for Best Electronic/Dance Album?", ["Daft Punk (Alive 2007)", "The Chemical Brothers", "Moby", "Fatboy Slim"], "Daft Punk (Alive 2007)"),
    ("mus_239", "Which song has been certified the highest by the RIAA?", ["White Christmas by Bing Crosby", "Candle in the Wind 1997", "Thriller", "Shape of You"], "White Christmas by Bing Crosby"),
    ("mus_240", "Who has won the most Brit Awards?", ["Robbie Williams", "Arctic Monkeys", "Coldplay", "Adele"], "Robbie Williams"),
]

for q in hard:
    new_questions.append({"id": q[0], "category": "Music", "subcategory": "Awards & Records", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "hard", "topic": None, "subtopic": None})

# Load, add, sort, save
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

data['categories']['Music'].extend(new_questions)
data['categories']['Music'].sort(key=lambda q: int(q['id'].split('_')[1]))

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added 60 Awards & Records questions")
print(f"Music now has {len(data['categories']['Music'])} total questions")
print(f"Added: 20 easy, 20 medium, 20 hard")
