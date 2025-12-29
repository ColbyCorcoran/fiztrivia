#!/usr/bin/env python3
"""Add 60 Music History & Eras questions from scratch"""
import json

# Define all 60 questions (20 easy, 20 medium, 20 hard)
new_questions = []

# Easy questions (20)
easy_questions = [
    ("mus_061", "What decade is often called the 'Golden Age of Rock and Roll'?", ["1950s", "1960s", "1970s", "1980s"], "1950s"),
    ("mus_062", "Which era of classical music did Mozart compose in?", ["Classical", "Baroque", "Romantic", "Modern"], "Classical"),
    ("mus_063", "What music genre originated in New Orleans in the early 1900s?", ["Jazz", "Blues", "Country", "Rock"], "Jazz"),
    ("mus_064", "Which decade saw the rise of disco music?", ["1970s", "1960s", "1980s", "1990s"], "1970s"),
    ("mus_065", "What era of classical music did Johann Sebastian Bach compose in?", ["Baroque", "Classical", "Romantic", "Renaissance"], "Baroque"),
    ("mus_066", "Which decade is known for grunge music?", ["1990s", "1980s", "2000s", "1970s"], "1990s"),
    ("mus_067", "What genre emerged in the Bronx in the 1970s?", ["Hip-hop", "Punk", "New Wave", "Disco"], "Hip-hop"),
    ("mus_068", "Which classical era focused on emotional expression?", ["Romantic", "Baroque", "Classical", "Modern"], "Romantic"),
    ("mus_069", "What decade saw the British Invasion?", ["1960s", "1950s", "1970s", "1980s"], "1960s"),
    ("mus_070", "Which musical movement started in Jamaica in the late 1960s?", ["Reggae", "Ska", "Dub", "Calypso"], "Reggae"),
    ("mus_071", "What decade is known for punk rock?", ["1970s", "1960s", "1980s", "1990s"], "1970s"),
    ("mus_072", "Which era saw the development of the symphony orchestra?", ["Classical", "Baroque", "Romantic", "Renaissance"], "Classical"),
    ("mus_073", "What decade saw the rise of MTV and music videos?", ["1980s", "1970s", "1990s", "2000s"], "1980s"),
    ("mus_074", "Which genre developed in the Mississippi Delta?", ["Blues", "Jazz", "Gospel", "Country"], "Blues"),
    ("mus_075", "What decade saw the Woodstock festival?", ["1960s", "1950s", "1970s", "1980s"], "1960s"),
    ("mus_076", "Which musical era preceded the Baroque period?", ["Renaissance", "Medieval", "Classical", "Romantic"], "Renaissance"),
    ("mus_077", "What decade is known for the Seattle grunge scene?", ["1990s", "1980s", "2000s", "1970s"], "1990s"),
    ("mus_078", "Which genre combines elements of blues, gospel, and jazz?", ["Soul", "Funk", "Disco", "R&B"], "Soul"),
    ("mus_079", "What decade saw the birth of rock and roll?", ["1950s", "1940s", "1960s", "1970s"], "1950s"),
    ("mus_080", "Which classical composer is known for the Romantic era?", ["Beethoven (late period)", "Mozart", "Bach", "Vivaldi"], "Beethoven (late period)"),
]

for q_data in easy_questions:
    new_questions.append({
        "id": q_data[0],
        "category": "Music",
        "subcategory": "Music History & Eras",
        "question": q_data[1],
        "options": q_data[2],
        "correct_answer": q_data[3],
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    })

# Medium questions (20)
medium_questions = [
    ("mus_081", "What musical movement emerged in response to disco in the late 1970s?", ["Punk rock", "New Wave", "Grunge", "Alternative rock"], "Punk rock"),
    ("mus_082", "Which decade saw the development of bebop jazz?", ["1940s", "1930s", "1950s", "1960s"], "1940s"),
    ("mus_083", "What era is characterized by ornate musical decoration and figured bass?", ["Baroque", "Classical", "Romantic", "Renaissance"], "Baroque"),
    ("mus_084", "Which musical movement began in Detroit in the 1960s?", ["Motown", "Memphis Soul", "Chicago Blues", "Philadelphia Soul"], "Motown"),
    ("mus_085", "What decade saw the rise of electronic dance music (EDM)?", ["2000s-2010s", "1990s", "1980s", "2020s"], "2000s-2010s"),
    ("mus_086", "Which jazz era featured Miles Davis' 'Kind of Blue'?", ["Cool jazz/Modal jazz (late 1950s)", "Bebop", "Swing", "Free jazz"], "Cool jazz/Modal jazz (late 1950s)"),
    ("mus_087", "What musical movement emphasized simplicity and repetition?", ["Minimalism", "Impressionism", "Expressionism", "Serialism"], "Minimalism"),
    ("mus_088", "Which decade saw the birth of techno music in Detroit?", ["1980s", "1970s", "1990s", "2000s"], "1980s"),
    ("mus_089", "What era in classical music featured composers like Debussy?", ["Impressionism", "Romanticism", "Modernism", "Expressionism"], "Impressionism"),
    ("mus_090", "Which musical movement emerged in the UK in the late 1970s?", ["New Wave", "Britpop", "Shoegaze", "Trip-hop"], "New Wave"),
    ("mus_091", "What decade saw the golden age of swing music?", ["1930s-1940s", "1920s", "1950s", "1940s-1950s"], "1930s-1940s"),
    ("mus_092", "Which genre emerged from Jamaican ska and rocksteady?", ["Reggae", "Dub", "Dancehall", "Ragga"], "Reggae"),
    ("mus_093", "What musical era featured the development of opera?", ["Baroque", "Renaissance", "Classical", "Romantic"], "Baroque"),
    ("mus_094", "Which decade saw the rise of alternative rock?", ["1990s", "1980s", "2000s", "1970s"], "1990s"),
    ("mus_095", "What genre developed in Chicago in the 1980s?", ["House music", "Techno", "Garage", "Trance"], "House music"),
    ("mus_096", "Which classical period emphasized balance and clarity?", ["Classical (1750-1820)", "Baroque", "Romantic", "Modern"], "Classical (1750-1820)"),
    ("mus_097", "What decade saw the British punk movement?", ["1970s", "1960s", "1980s", "1990s"], "1970s"),
    ("mus_098", "Which genre combined punk and reggae?", ["Ska punk/Two-tone", "Punk funk", "Post-punk", "No wave"], "Ska punk/Two-tone"),
    ("mus_099", "What musical movement emphasized emotional intensity and nationalism?", ["Romanticism", "Impressionism", "Expressionism", "Nationalism"], "Romanticism"),
    ("mus_100", "Which decade saw the development of trip-hop?", ["1990s", "1980s", "2000s", "2010s"], "1990s"),
]

for q_data in medium_questions:
    new_questions.append({
        "id": q_data[0],
        "category": "Music",
        "subcategory": "Music History & Eras",
        "question": q_data[1],
        "options": q_data[2],
        "correct_answer": q_data[3],
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    })

# Hard questions (20)
hard_questions = [
    ("mus_101", "Which compositional technique did Arnold Schoenberg develop?", ["Twelve-tone technique", "Serialism", "Minimalism", "Chance music"], "Twelve-tone technique"),
    ("mus_102", "What year is generally considered the start of the Baroque period?", ["1600", "1550", "1650", "1700"], "1600"),
    ("mus_103", "Which movement emphasized atonality and dissonance in the early 20th century?", ["Second Viennese School", "Impressionism", "Minimalism", "Futurism"], "Second Viennese School"),
    ("mus_104", "What decade saw the development of free jazz?", ["1960s", "1950s", "1970s", "1940s"], "1960s"),
    ("mus_105", "Which musical movement was led by Karlheinz Stockhausen?", ["Electronic/Musique concrète", "Minimalism", "Serialism", "Chance music"], "Electronic/Musique concrète"),
    ("mus_106", "What era featured the development of the concerto grosso?", ["Baroque", "Classical", "Renaissance", "Romantic"], "Baroque"),
    ("mus_107", "Which decade saw the Canterbury scene in progressive rock?", ["1970s", "1960s", "1980s", "1990s"], "1970s"),
    ("mus_108", "What musical movement emphasized indeterminacy and chance?", ["Aleatoric music (John Cage)", "Minimalism", "Serialism", "Expressionism"], "Aleatoric music (John Cage)"),
    ("mus_109", "Which genre emerged from the UK's early 1990s rave scene?", ["Jungle/Drum and bass", "Dubstep", "Grime", "UK Garage"], "Jungle/Drum and bass"),
    ("mus_110", "What year did bebop jazz emerge?", ["1940s (around 1945)", "1930s", "1950s", "1960s"], "1940s (around 1945)"),
    ("mus_111", "Which movement featured prepared piano and extended techniques?", ["Experimental music (John Cage era)", "Minimalism", "Impressionism", "Serialism"], "Experimental music (John Cage era)"),
    ("mus_112", "What decade saw the development of krautrock in Germany?", ["1970s", "1960s", "1980s", "1990s"], "1970s"),
    ("mus_113", "Which classical technique uses all 12 chromatic pitches equally?", ["Serialism/Dodecaphony", "Atonality", "Bitonality", "Polytonality"], "Serialism/Dodecaphony"),
    ("mus_114", "What musical movement featured Terry Riley and Steve Reich?", ["Minimalism", "Serialism", "Experimental", "Postmodernism"], "Minimalism"),
    ("mus_115", "Which decade saw the Madchester scene?", ["Late 1980s-early 1990s", "1980s", "1990s", "2000s"], "Late 1980s-early 1990s"),
    ("mus_116", "What era featured the development of the basso continuo?", ["Baroque", "Renaissance", "Classical", "Medieval"], "Baroque"),
    ("mus_117", "Which movement emphasized whole-tone scales and exotic sounds?", ["Impressionism (Debussy)", "Romanticism", "Expressionism", "Modernism"], "Impressionism (Debussy)"),
    ("mus_118", "What decade saw the development of no wave in New York?", ["Late 1970s", "Early 1980s", "Late 1960s", "Early 1970s"], "Late 1970s"),
    ("mus_119", "Which genre emerged from UK garage in the early 2000s?", ["Dubstep", "Grime", "Bassline", "2-step"], "Dubstep"),
    ("mus_120", "What musical philosophy emphasized total serialism?", ["Integral serialism (Boulez)", "Twelve-tone technique", "Minimalism", "Aleatoric music"], "Integral serialism (Boulez)"),
]

for q_data in hard_questions:
    new_questions.append({
        "id": q_data[0],
        "category": "Music",
        "subcategory": "Music History & Eras",
        "question": q_data[1],
        "options": q_data[2],
        "correct_answer": q_data[3],
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    })

# Load existing data
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Add new questions
data['categories']['Music'].extend(new_questions)

# Sort by ID
data['categories']['Music'].sort(key=lambda q: int(q['id'].split('_')[1]))

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added 60 Music History & Eras questions")
print(f"Music now has {len(data['categories']['Music'])} total questions")
print(f"Added: 20 easy, 20 medium, 20 hard")
