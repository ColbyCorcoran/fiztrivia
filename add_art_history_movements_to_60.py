#!/usr/bin/env python3
"""Add 60 Art History & Movements questions from scratch"""
import json

new_questions = []

# Easy questions (20)
easy = [
    ("art_061", "Which art movement is characterized by small brush strokes and light?", ["Impressionism", "Cubism", "Surrealism", "Abstract Expressionism"], "Impressionism"),
    ("art_062", "Which movement featured melting clocks and dreamlike imagery?", ["Surrealism", "Cubism", "Dadaism", "Futurism"], "Surrealism"),
    ("art_063", "Which movement broke objects into geometric shapes?", ["Cubism", "Impressionism", "Fauvism", "Expressionism"], "Cubism"),
    ("art_064", "What does 'Renaissance' mean?", ["Rebirth", "Enlightenment", "Revolution", "Discovery"], "Rebirth"),
    ("art_065", "Which movement used bright, wild colors and was named after 'wild beasts'?", ["Fauvism", "Cubism", "Expressionism", "Surrealism"], "Fauvism"),
    ("art_066", "What art period came before the Renaissance?", ["Medieval/Gothic", "Baroque", "Rococo", "Neoclassical"], "Medieval/Gothic"),
    ("art_067", "Which movement featured drip painting and large canvases?", ["Abstract Expressionism", "Cubism", "Pop Art", "Minimalism"], "Abstract Expressionism"),
    ("art_068", "Which movement used everyday objects like soup cans as art subjects?", ["Pop Art", "Dadaism", "Surrealism", "Minimalism"], "Pop Art"),
    ("art_069", "What period is Michelangelo associated with?", ["Renaissance", "Baroque", "Medieval", "Neoclassical"], "Renaissance"),
    ("art_070", "Which movement rejected traditional art and embraced absurdity?", ["Dadaism", "Surrealism", "Futurism", "Constructivism"], "Dadaism"),
    ("art_071", "What art period followed the Renaissance?", ["Baroque", "Rococo", "Neoclassical", "Romantic"], "Baroque"),
    ("art_072", "Which movement focused on depicting modern life and leisure activities?", ["Impressionism", "Realism", "Romanticism", "Neoclassicism"], "Impressionism"),
    ("art_073", "What does 'art nouveau' mean in English?", ["New art", "Modern art", "Young art", "Fresh art"], "New art"),
    ("art_074", "Which movement emphasized emotion over reason?", ["Romanticism", "Neoclassicism", "Realism", "Naturalism"], "Romanticism"),
    ("art_075", "What period features ornate decoration and drama?", ["Baroque", "Renaissance", "Gothic", "Rococo"], "Baroque"),
    ("art_076", "Which movement tried to depict reality exactly as it appears?", ["Realism", "Romanticism", "Impressionism", "Symbolism"], "Realism"),
    ("art_077", "What century was the Renaissance?", ["14th-17th century", "12th-14th century", "18th-19th century", "10th-12th century"], "14th-17th century"),
    ("art_078", "Which movement featured simplified forms and primary colors?", ["De Stijl", "Bauhaus", "Constructivism", "Suprematism"], "De Stijl"),
    ("art_079", "What period emphasized reason and classical ideals?", ["Neoclassicism", "Romanticism", "Baroque", "Rococo"], "Neoclassicism"),
    ("art_080", "Which movement emphasized speed, technology, and motion?", ["Futurism", "Cubism", "Constructivism", "Dadaism"], "Futurism"),
]

for q in easy:
    new_questions.append({"id": q[0], "category": "Art", "subcategory": "Art History & Movements", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "easy", "topic": None, "subtopic": None})

# Medium questions (20)
medium = [
    ("art_081", "Where did the Renaissance begin?", ["Florence, Italy", "Rome, Italy", "Paris, France", "Venice, Italy"], "Florence, Italy"),
    ("art_082", "Which movement used dots of pure color (pointillism)?", ["Neo-Impressionism", "Impressionism", "Fauvism", "Divisionism"], "Neo-Impressionism"),
    ("art_083", "Who founded the Bauhaus school?", ["Walter Gropius", "Le Corbusier", "Ludwig Mies van der Rohe", "Frank Lloyd Wright"], "Walter Gropius"),
    ("art_084", "What year did the Impressionist movement begin (first exhibition)?", ["1874", "1880", "1865", "1890"], "1874"),
    ("art_085", "Which movement preceded Impressionism in France?", ["Realism", "Romanticism", "Neoclassicism", "Symbolism"], "Realism"),
    ("art_086", "What does 'Rococo' art typically depict?", ["Playful, ornate aristocratic life", "Religious scenes", "Heroic battles", "Working-class struggles"], "Playful, ornate aristocratic life"),
    ("art_087", "Which movement was founded by André Breton?", ["Surrealism", "Dadaism", "Futurism", "Cubism"], "Surrealism"),
    ("art_088", "What was the Ashcan School known for depicting?", ["Gritty urban American life", "Abstract forms", "European landscapes", "Religious imagery"], "Gritty urban American life"),
    ("art_089", "Which Russian art movement featured geometric abstraction?", ["Constructivism", "Suprematism", "Futurism", "Rayonism"], "Constructivism"),
    ("art_090", "What movement did Gustave Courbet lead?", ["Realism", "Impressionism", "Romanticism", "Naturalism"], "Realism"),
    ("art_091", "Which movement featured artists like Rothko and Newman?", ["Color Field painting", "Abstract Expressionism", "Pop Art", "Minimalism"], "Color Field painting"),
    ("art_092", "What art movement emerged in 1960s Britain and America celebrating popular culture?", ["Pop Art", "Op Art", "Minimalism", "Conceptual Art"], "Pop Art"),
    ("art_093", "Which Pre-Raphaelite Brotherhood founder painted 'Ophelia'?", ["John Everett Millais", "Dante Gabriel Rossetti", "William Holman Hunt", "Ford Madox Brown"], "John Everett Millais"),
    ("art_094", "What movement did Kazimir Malevich found?", ["Suprematism", "Constructivism", "Rayonism", "Cubo-Futurism"], "Suprematism"),
    ("art_095", "Which movement emphasized the unconscious mind and dreams?", ["Surrealism", "Symbolism", "Expressionism", "Dadaism"], "Surrealism"),
    ("art_096", "What was the Barbizon School known for?", ["Landscape painting", "Portraiture", "Still life", "Historical scenes"], "Landscape painting"),
    ("art_097", "Which movement featured Kandinsky and Marc?", ["Der Blaue Reiter (The Blue Rider)", "Die Brücke (The Bridge)", "Bauhaus", "Expressionism"], "Der Blaue Reiter (The Blue Rider)"),
    ("art_098", "What Italian movement rejected the past and celebrated modernity?", ["Futurism", "Metaphysical painting", "Arte Povera", "Novecento Italiano"], "Futurism"),
    ("art_099", "Which movement was characterized by optical illusions?", ["Op Art", "Pop Art", "Kinetic Art", "Minimalism"], "Op Art"),
    ("art_100", "What movement did Giorgio de Chirico pioneer?", ["Metaphysical painting", "Surrealism", "Futurism", "Arte Povera"], "Metaphysical painting"),
]

for q in medium:
    new_questions.append({"id": q[0], "category": "Art", "subcategory": "Art History & Movements", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "medium", "topic": None, "subtopic": None})

# Hard questions (20)
hard = [
    ("art_101", "Which Mannerist painter created elongated figures like 'View of Toledo'?", ["El Greco", "Parmigianino", "Pontormo", "Bronzino"], "El Greco"),
    ("art_102", "What year was the Armory Show in New York introducing modern art?", ["1913", "1910", "1920", "1905"], "1913"),
    ("art_103", "Which movement featured Umberto Boccioni's 'Unique Forms of Continuity in Space'?", ["Futurism", "Cubism", "Constructivism", "Vorticism"], "Futurism"),
    ("art_104", "Who wrote the 'Futurist Manifesto' in 1909?", ["Filippo Tommaso Marinetti", "Umberto Boccioni", "Giacomo Balla", "Carlo Carrà"], "Filippo Tommaso Marinetti"),
    ("art_105", "Which Fauvist artist painted 'The Joy of Life'?", ["Henri Matisse", "André Derain", "Maurice de Vlaminck", "Raoul Dufy"], "Henri Matisse"),
    ("art_106", "What German Expressionist group was founded in Dresden in 1905?", ["Die Brücke (The Bridge)", "Der Blaue Reiter", "Neue Sachlichkeit", "November Group"], "Die Brücke (The Bridge)"),
    ("art_107", "Which movement featured Christo and Jeanne-Claude's wrapped buildings?", ["Environmental Art/Land Art", "Conceptual Art", "Installation Art", "Performance Art"], "Environmental Art/Land Art"),
    ("art_108", "Who painted 'Black Square', a key Suprematist work?", ["Kazimir Malevich", "El Lissitzky", "Alexander Rodchenko", "Vladimir Tatlin"], "Kazimir Malevich"),
    ("art_109", "Which art movement was centered at Black Mountain College?", ["Abstract Expressionism", "Color Field", "Pop Art", "Minimalism"], "Abstract Expressionism"),
    ("art_110", "What movement did Theo van Doesburg co-found?", ["De Stijl", "Bauhaus", "Constructivism", "Suprematism"], "De Stijl"),
    ("art_111", "Which Symbolist painter created 'The Isle of the Dead'?", ["Arnold Böcklin", "Gustave Moreau", "Odilon Redon", "Pierre Puvis de Chavannes"], "Arnold Böcklin"),
    ("art_112", "What year did the Salon des Refusés first exhibit rejected works?", ["1863", "1874", "1855", "1880"], "1863"),
    ("art_113", "Which movement featured Carl Andre's floor sculptures?", ["Minimalism", "Conceptual Art", "Post-Minimalism", "Process Art"], "Minimalism"),
    ("art_114", "Who founded Orphism (Orphic Cubism)?", ["Robert Delaunay", "Sonia Delaunay", "Francis Picabia", "Fernand Léger"], "Robert Delaunay"),
    ("art_115", "Which movement featured Yves Klein's monochrome blue paintings?", ["Nouveau Réalisme", "Zero Group", "Fluxus", "Arte Povera"], "Nouveau Réalisme"),
    ("art_116", "What was the Neue Sachlichkeit movement in English?", ["New Objectivity", "New Realism", "New Vision", "New Clarity"], "New Objectivity"),
    ("art_117", "Which movement did Piet Mondrian help establish?", ["De Stijl", "Bauhaus", "Suprematism", "Constructivism"], "De Stijl"),
    ("art_118", "Who wrote 'Concerning the Spiritual in Art'?", ["Wassily Kandinsky", "Piet Mondrian", "Kazimir Malevich", "Paul Klee"], "Wassily Kandinsky"),
    ("art_119", "Which Viennese Secessionist designed the Secession Building?", ["Joseph Maria Olbrich", "Gustav Klimt", "Otto Wagner", "Josef Hoffmann"], "Joseph Maria Olbrich"),
    ("art_120", "What movement featured Hans Arp's organic abstract forms?", ["Dadaism and later Surrealism", "Cubism", "Futurism", "Constructivism"], "Dadaism and later Surrealism"),
]

for q in hard:
    new_questions.append({"id": q[0], "category": "Art", "subcategory": "Art History & Movements", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "hard", "topic": None, "subtopic": None})

# Load, add, sort, save
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

data['categories']['Art'].extend(new_questions)
data['categories']['Art'].sort(key=lambda q: int(q['id'].split('_')[1]))

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added 60 Art History & Movements questions")
print(f"Art now has {len(data['categories']['Art'])} total questions")
print(f"Added: 20 easy, 20 medium, 20 hard")
