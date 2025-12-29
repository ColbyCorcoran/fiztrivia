#!/usr/bin/env python3
"""Add 60 Architecture questions from scratch"""
import json

new_questions = []

# Easy questions (20)
easy = [
    ("art_181", "Who designed the Eiffel Tower?", ["Gustave Eiffel", "Charles Garnier", "Hector Guimard", "Victor Baltard"], "Gustave Eiffel"),
    ("art_182", "What famous white marble mausoleum is in India?", ["Taj Mahal", "Red Fort", "Hawa Mahal", "Golden Temple"], "Taj Mahal"),
    ("art_183", "Who designed the Sydney Opera House?", ["Jørn Utzon", "Walter Burley Griffin", "Harry Seidler", "Glenn Murcutt"], "Jørn Utzon"),
    ("art_184", "What is the tallest building in the world (as of 2024)?", ["Burj Khalifa", "Shanghai Tower", "Makkah Royal Clock Tower", "One World Trade Center"], "Burj Khalifa"),
    ("art_185", "Who designed Fallingwater?", ["Frank Lloyd Wright", "Le Corbusier", "Walter Gropius", "Ludwig Mies van der Rohe"], "Frank Lloyd Wright"),
    ("art_186", "What style are Gothic cathedrals known for?", ["Pointed arches and flying buttresses", "Rounded arches", "Flat roofs", "Onion domes"], "Pointed arches and flying buttresses"),
    ("art_187", "Who designed the Guggenheim Museum in Bilbao?", ["Frank Gehry", "Zaha Hadid", "Norman Foster", "Rem Koolhaas"], "Frank Gehry"),
    ("art_188", "What is the large amphitheater in Rome called?", ["Colosseum", "Pantheon", "Forum", "Circus Maximus"], "Colosseum"),
    ("art_189", "Who designed St. Peter's Basilica dome?", ["Michelangelo", "Bramante", "Bernini", "Raphael"], "Michelangelo"),
    ("art_190", "What architectural style has columns and pediments?", ["Classical/Greek Revival", "Gothic", "Baroque", "Art Nouveau"], "Classical/Greek Revival"),
    ("art_191", "Who designed the Glass Pyramid at the Louvre?", ["I. M. Pei", "Norman Foster", "Renzo Piano", "Richard Meier"], "I. M. Pei"),
    ("art_192", "What is the name of Barcelona's unfinished church by Gaudí?", ["Sagrada Família", "Casa Batlló", "Park Güell", "La Pedrera"], "Sagrada Família"),
    ("art_193", "What are the three Classical orders of columns?", ["Doric, Ionic, Corinthian", "Roman, Greek, Egyptian", "Gothic, Baroque, Renaissance", "Modern, Contemporary, Postmodern"], "Doric, Ionic, Corinthian"),
    ("art_194", "Who designed the Seagram Building in New York?", ["Ludwig Mies van der Rohe", "Le Corbusier", "Walter Gropius", "Philip Johnson"], "Ludwig Mies van der Rohe"),
    ("art_195", "What material is the Pantheon dome made from?", ["Concrete", "Stone", "Brick", "Wood"], "Concrete"),
    ("art_196", "Who designed the Villa Savoye?", ["Le Corbusier", "Frank Lloyd Wright", "Walter Gropius", "Ludwig Mies van der Rohe"], "Le Corbusier"),
    ("art_197", "What ancient wonder was a lighthouse?", ["Lighthouse of Alexandria", "Colossus of Rhodes", "Hanging Gardens", "Statue of Zeus"], "Lighthouse of Alexandria"),
    ("art_198", "Who designed the Chrysler Building?", ["William Van Alen", "Raymond Hood", "Cass Gilbert", "Shreve, Lamb & Harmon"], "William Van Alen"),
    ("art_199", "What architectural movement emphasized function over form?", ["Modernism/Functionalism", "Art Nouveau", "Baroque", "Gothic Revival"], "Modernism/Functionalism"),
    ("art_200", "Who designed the Barcelona Pavilion?", ["Ludwig Mies van der Rohe", "Le Corbusier", "Walter Gropius", "Antoni Gaudí"], "Ludwig Mies van der Rohe"),
]

for q in easy:
    new_questions.append({"id": q[0], "category": "Art", "subcategory": "Architecture", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "easy", "topic": None, "subtopic": None})

# Medium questions (20)
medium = [
    ("art_201", "What year was the Eiffel Tower completed?", ["1889", "1878", "1900", "1885"], "1889"),
    ("art_202", "Who designed the Woolworth Building?", ["Cass Gilbert", "William Van Alen", "Raymond Hood", "Louis Sullivan"], "Cass Gilbert"),
    ("art_203", "What is Frank Lloyd Wright's architectural philosophy called?", ["Organic architecture", "Brutalism", "Deconstructivism", "High-tech"], "Organic architecture"),
    ("art_204", "Who designed the Pompidou Centre in Paris?", ["Renzo Piano and Richard Rogers", "Norman Foster", "I. M. Pei", "Jean Nouvel"], "Renzo Piano and Richard Rogers"),
    ("art_205", "What is the Islamic architectural feature with geometric patterns called?", ["Muqarnas/Arabesque", "Mosaic", "Fresco", "Inlay"], "Muqarnas/Arabesque"),
    ("art_206", "Who designed Brasília, Brazil's capital?", ["Oscar Niemeyer", "Lúcio Costa", "Roberto Burle Marx", "Affonso Eduardo Reidy"], "Oscar Niemeyer"),
    ("art_207", "What architectural movement featured exposed concrete?", ["Brutalism", "Modernism", "Postmodernism", "Deconstructivism"], "Brutalism"),
    ("art_208", "Who designed the Farnsworth House?", ["Ludwig Mies van der Rohe", "Philip Johnson", "Le Corbusier", "Richard Neutra"], "Ludwig Mies van der Rohe"),
    ("art_209", "What is the oculus in the Pantheon?", ["Opening in the dome", "Entrance hall", "Supporting column", "Decorative frieze"], "Opening in the dome"),
    ("art_210", "Who designed the Shard in London?", ["Renzo Piano", "Norman Foster", "Zaha Hadid", "Richard Rogers"], "Renzo Piano"),
    ("art_211", "What style is characterized by ornate natural forms?", ["Art Nouveau", "Art Deco", "Bauhaus", "Brutalism"], "Art Nouveau"),
    ("art_212", "Who designed the Getty Center in Los Angeles?", ["Richard Meier", "I. M. Pei", "Frank Gehry", "Thom Mayne"], "Richard Meier"),
    ("art_213", "What is a flying buttress used for?", ["Supporting walls from outside", "Decoration", "Water drainage", "Bell tower support"], "Supporting walls from outside"),
    ("art_214", "Who designed the CCTV Headquarters in Beijing?", ["Rem Koolhaas (OMA)", "Zaha Hadid", "Norman Foster", "Herzog & de Meuron"], "Rem Koolhaas (OMA)"),
    ("art_215", "What is the name of Gaudí's wavy apartment building?", ["Casa Milà (La Pedrera)", "Casa Batlló", "Casa Vicens", "Palau Güell"], "Casa Milà (La Pedrera)"),
    ("art_216", "Who designed the TWA Flight Center at JFK?", ["Eero Saarinen", "SOM", "I. M. Pei", "Paul Rudolph"], "Eero Saarinen"),
    ("art_217", "What is Louis Sullivan famous for saying?", ["Form follows function", "Less is more", "Architecture is frozen music", "God is in the details"], "Form follows function"),
    ("art_218", "Who designed the Einstein Tower in Potsdam?", ["Erich Mendelsohn", "Bruno Taut", "Walter Gropius", "Hans Poelzig"], "Erich Mendelsohn"),
    ("art_219", "What is the architectural term for a half-circular recess?", ["Apse", "Nave", "Transept", "Clerestory"], "Apse"),
    ("art_220", "Who designed the Vitra Design Museum?", ["Frank Gehry", "Zaha Hadid", "Rem Koolhaas", "Peter Eisenman"], "Frank Gehry"),
]

for q in medium:
    new_questions.append({"id": q[0], "category": "Art", "subcategory": "Architecture", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "medium", "topic": None, "subtopic": None})

# Hard questions (20)
hard = [
    ("art_221", "Who designed the Schröder House in Utrecht?", ["Gerrit Rietveld", "Theo van Doesburg", "J.J.P. Oud", "Mart Stam"], "Gerrit Rietveld"),
    ("art_222", "What is Andrea Palladio's most famous villa?", ["Villa Rotonda (La Rotonda)", "Villa Barbaro", "Villa Emo", "Villa Foscari"], "Villa Rotonda (La Rotonda)"),
    ("art_223", "Who designed the Vanna Venturi House?", ["Robert Venturi", "Michael Graves", "Charles Moore", "Philip Johnson"], "Robert Venturi"),
    ("art_224", "What is the architectural term for the triangular section above columns?", ["Pediment", "Entablature", "Frieze", "Cornice"], "Pediment"),
    ("art_225", "Who designed the Jewish Museum in Berlin?", ["Daniel Libeskind", "Peter Eisenman", "Zaha Hadid", "Frank Gehry"], "Daniel Libeskind"),
    ("art_226", "What is the term for Islamic pointed arches?", ["Ogee arch", "Horseshoe arch", "Tudor arch", "Lancet arch"], "Ogee arch"),
    ("art_227", "Who designed the Bibliothèque Sainte-Geneviève?", ["Henri Labrouste", "Charles Garnier", "Victor Baltard", "Eugène Viollet-le-Duc"], "Henri Labrouste"),
    ("art_228", "What architectural movement did Peter Eisenman belong to?", ["Deconstructivism", "Postmodernism", "High-tech", "Metabolism"], "Deconstructivism"),
    ("art_229", "Who designed the Kimbell Art Museum?", ["Louis Kahn", "Paul Rudolph", "I. M. Pei", "Philip Johnson"], "Louis Kahn"),
    ("art_230", "What is the term for interlocking timber construction?", ["Mortise and tenon", "Post and beam", "Balloon frame", "Platform frame"], "Mortise and tenon"),
    ("art_231", "Who designed the AT&T Building (now Sony Tower)?", ["Philip Johnson", "Michael Graves", "Robert Venturi", "Charles Moore"], "Philip Johnson"),
    ("art_232", "What Japanese architectural movement emphasized organic metabolism?", ["Metabolism", "Modernism", "Brutalism", "High-tech"], "Metabolism"),
    ("art_233", "Who designed the Ronchamp chapel?", ["Le Corbusier", "Oscar Niemeyer", "Alvar Aalto", "Eero Saarinen"], "Le Corbusier"),
    ("art_234", "What is the term for a vaulted semicircular ceiling?", ["Barrel vault", "Groin vault", "Rib vault", "Fan vault"], "Barrel vault"),
    ("art_235", "Who designed the Nationalgalerie in Berlin?", ["Ludwig Mies van der Rohe", "Walter Gropius", "Hans Scharoun", "Egon Eiermann"], "Ludwig Mies van der Rohe"),
    ("art_236", "What is the term for decorative openwork stonework?", ["Tracery", "Quatrefoil", "Finial", "Crocket"], "Tracery"),
    ("art_237", "Who designed the Nakagin Capsule Tower?", ["Kisho Kurokawa", "Kenzo Tange", "Arata Isozaki", "Fumihiko Maki"], "Kisho Kurokawa"),
    ("art_238", "What is the architectural term for a projecting window bay?", ["Oriel window", "Bay window", "Clerestory", "Dormer"], "Oriel window"),
    ("art_239", "Who designed the Yoyogi National Gymnasium?", ["Kenzo Tange", "Kisho Kurokawa", "Arata Isozaki", "Fumihiko Maki"], "Kenzo Tange"),
    ("art_240", "What is the term for upward curve of a roof in Asian architecture?", ["Upsweep/Upturned eaves", "Pagoda", "Hip roof", "Gable roof"], "Upsweep/Upturned eaves"),
]

for q in hard:
    new_questions.append({"id": q[0], "category": "Art", "subcategory": "Architecture", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "hard", "topic": None, "subtopic": None})

# Load, add, sort, save
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

data['categories']['Art'].extend(new_questions)
data['categories']['Art'].sort(key=lambda q: int(q['id'].split('_')[1]))

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added 60 Architecture questions")
print(f"Art now has {len(data['categories']['Art'])} total questions")
print(f"Added: 20 easy, 20 medium, 20 hard")
