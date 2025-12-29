#!/usr/bin/env python3
"""Add 60 Sculpture questions from scratch"""
import json

new_questions = []

# Easy questions (20)
easy = [
    ("art_121", "Who sculpted 'David' during the Renaissance?", ["Michelangelo", "Donatello", "Leonardo da Vinci", "Bernini"], "Michelangelo"),
    ("art_122", "Who sculpted 'The Thinker'?", ["Auguste Rodin", "Camille Claudel", "Antoine Bourdelle", "Aristide Maillol"], "Auguste Rodin"),
    ("art_123", "What famous statue stands in New York Harbor?", ["Statue of Liberty", "David", "Christ the Redeemer", "The Thinker"], "Statue of Liberty"),
    ("art_124", "Who designed the Statue of Liberty?", ["Frédéric Auguste Bartholdi", "Gustave Eiffel", "Auguste Rodin", "Jean-Antoine Houdon"], "Frédéric Auguste Bartholdi"),
    ("art_125", "What material is the Statue of Liberty primarily made of?", ["Copper", "Bronze", "Iron", "Steel"], "Copper"),
    ("art_126", "Who sculpted 'The Kiss'?", ["Auguste Rodin", "Antonio Canova", "Constantin Brâncuși", "Camille Claudel"], "Auguste Rodin"),
    ("art_127", "What ancient Greek statue is missing its arms?", ["Venus de Milo", "Nike of Samothrace", "Laocoön", "Aphrodite of Knidos"], "Venus de Milo"),
    ("art_128", "Who sculpted 'The Gates of Hell'?", ["Auguste Rodin", "Lorenzo Ghiberti", "Andrea Pisano", "Donatello"], "Auguste Rodin"),
    ("art_129", "What is the famous Christ statue in Rio de Janeiro called?", ["Christ the Redeemer", "Christ the King", "Sacred Heart", "Cristo Rey"], "Christ the Redeemer"),
    ("art_130", "Who created the famous Mount Rushmore sculptures?", ["Gutzon Borglum", "Augustus Saint-Gaudens", "Daniel Chester French", "Lorado Taft"], "Gutzon Borglum"),
    ("art_131", "What is the study of carving or engraving called?", ["Glyptics", "Casting", "Modeling", "Assemblage"], "Glyptics"),
    ("art_132", "Who sculpted the Pietà in St. Peter's Basilica?", ["Michelangelo", "Bernini", "Donatello", "Giambologna"], "Michelangelo"),
    ("art_133", "What material did ancient Greeks primarily use for sculpture?", ["Marble", "Bronze", "Clay", "Wood"], "Marble"),
    ("art_134", "Who created the 'Balloon Dog' sculptures?", ["Jeff Koons", "Damien Hirst", "Takashi Murakami", "Anish Kapoor"], "Jeff Koons"),
    ("art_135", "What is bronze primarily made of?", ["Copper and tin", "Iron and carbon", "Copper and zinc", "Gold and silver"], "Copper and tin"),
    ("art_136", "Who sculpted 'The Little Mermaid' in Copenhagen?", ["Edvard Eriksen", "Bertel Thorvaldsen", "Bjørn Nørgaard", "Jens Adolf Jerichau"], "Edvard Eriksen"),
    ("art_137", "What process uses wax that is melted away?", ["Lost-wax casting", "Sand casting", "Die casting", "Investment casting"], "Lost-wax casting"),
    ("art_138", "Who created mobiles (moving sculptures)?", ["Alexander Calder", "Jean Tinguely", "Naum Gabo", "László Moholy-Nagy"], "Alexander Calder"),
    ("art_139", "What famous Egyptian sculpture has a lion's body?", ["Great Sphinx of Giza", "Nefertiti Bust", "Rosetta Stone", "Abu Simbel"], "Great Sphinx of Giza"),
    ("art_140", "Who sculpted the lions in London's Trafalgar Square?", ["Edwin Landseer", "John Flaxman", "Francis Chantrey", "Richard Westmacott"], "Edwin Landseer"),
]

for q in easy:
    new_questions.append({"id": q[0], "category": "Art", "subcategory": "Sculpture", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "easy", "topic": None, "subtopic": None})

# Medium questions (20)
medium = [
    ("art_141", "Who sculpted 'Ecstasy of Saint Teresa'?", ["Gian Lorenzo Bernini", "Alessandro Algardi", "Francesco Borromini", "Pietro da Cortona"], "Gian Lorenzo Bernini"),
    ("art_142", "What is the tallest statue in the world (as of 2024)?", ["Statue of Unity (India)", "Spring Temple Buddha (China)", "Statue of Liberty (USA)", "Christ the Redeemer (Brazil)"], "Statue of Unity (India)"),
    ("art_143", "Who created 'Bird in Space'?", ["Constantin Brâncuși", "Jean Arp", "Barbara Hepworth", "Henry Moore"], "Constantin Brâncuși"),
    ("art_144", "Who sculpted 'The Burghers of Calais'?", ["Auguste Rodin", "Camille Claudel", "Antoine Bourdelle", "Charles Despiau"], "Auguste Rodin"),
    ("art_145", "What is the name of Michelangelo's unfinished sculptures that appear to emerge from stone?", ["Prisoners/Slaves", "David", "Pietà", "Moses"], "Prisoners/Slaves"),
    ("art_146", "Who created the 'Unique Forms of Continuity in Space'?", ["Umberto Boccioni", "Giacomo Balla", "Carlo Carrà", "Gino Severini"], "Umberto Boccioni"),
    ("art_147", "Which sculptor created works with holes, like 'Reclining Figure'?", ["Henry Moore", "Barbara Hepworth", "Jean Arp", "Naum Gabo"], "Henry Moore"),
    ("art_148", "Who sculpted the 'Manneken Pis' in Brussels?", ["Jérôme Duquesnoy", "François Duquesnoy", "Artus Quellinus", "Lucas Faydherbe"], "Jérôme Duquesnoy"),
    ("art_149", "What sculpture technique involves building up material?", ["Modeling/Additive", "Carving/Subtractive", "Casting", "Assemblage"], "Modeling/Additive"),
    ("art_150", "Who created 'L.O.V.E.' (the raised middle finger sculpture in Milan)?", ["Maurizio Cattelan", "Piero Manzoni", "Michelangelo Pistoletto", "Jannis Kounellis"], "Maurizio Cattelan"),
    ("art_151", "Which sculptor worked primarily with marble and created 'Psyche Revived by Cupid's Kiss'?", ["Antonio Canova", "Bertel Thorvaldsen", "Jean-Antoine Houdon", "Étienne Maurice Falconet"], "Antonio Canova"),
    ("art_152", "Who created 'Cloud Gate' (The Bean) in Chicago?", ["Anish Kapoor", "Richard Serra", "Jeff Koons", "Claes Oldenburg"], "Anish Kapoor"),
    ("art_153", "What is the process of creating a sculpture by removing material called?", ["Carving/Subtractive", "Modeling/Additive", "Casting", "Welding"], "Carving/Subtractive"),
    ("art_154", "Who sculpted 'The Age of Bronze'?", ["Auguste Rodin", "Camille Claudel", "Antoine Bourdelle", "Émile Antoine Bourdelle"], "Auguste Rodin"),
    ("art_155", "Which ancient sculpture depicts a father and sons being attacked?", ["Laocoön and His Sons", "The Farnese Bull", "Hercules and Antaeus", "The Rape of the Sabines"], "Laocoön and His Sons"),
    ("art_156", "Who created the bronze doors called 'Gates of Paradise'?", ["Lorenzo Ghiberti", "Andrea Pisano", "Donatello", "Luca della Robbia"], "Lorenzo Ghiberti"),
    ("art_157", "Who sculpted 'The Rape of Proserpina'?", ["Gian Lorenzo Bernini", "Antonio Canova", "Giambologna", "Alessandro Algardi"], "Gian Lorenzo Bernini"),
    ("art_158", "Which sculptor created 'Spiral Jetty' in Utah's Great Salt Lake?", ["Robert Smithson", "Michael Heizer", "Walter De Maria", "Nancy Holt"], "Robert Smithson"),
    ("art_159", "Who created 'Puppy', a giant flower-covered dog sculpture?", ["Jeff Koons", "Claes Oldenburg", "Takashi Murakami", "Damien Hirst"], "Jeff Koons"),
    ("art_160", "What sculpture depicts Winged Victory?", ["Nike of Samothrace", "Venus de Milo", "Athena Parthenos", "Apollo Belvedere"], "Nike of Samothrace"),
]

for q in medium:
    new_questions.append({"id": q[0], "category": "Art", "subcategory": "Sculpture", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "medium", "topic": None, "subtopic": None})

# Hard questions (20)
hard = [
    ("art_161", "Who sculpted 'The Walking Man' (L'Homme qui marche)?", ["Alberto Giacometti", "Auguste Rodin", "Henry Moore", "Constantin Brâncuși"], "Alberto Giacometti"),
    ("art_162", "Which sculptor created 'Tilted Arc' that was controversially removed?", ["Richard Serra", "Carl Andre", "Donald Judd", "Dan Flavin"], "Richard Serra"),
    ("art_163", "Who created 'Fountain', the famous urinal artwork?", ["Marcel Duchamp", "Man Ray", "Francis Picabia", "Hans Arp"], "Marcel Duchamp"),
    ("art_164", "What is the term for a sculpture that is the negative space?", ["Counter-relief or void", "Assemblage", "Bas-relief", "High relief"], "Counter-relief or void"),
    ("art_165", "Who sculpted 'Charging Bull' on Wall Street?", ["Arturo Di Modica", "Kristen Visbal", "Auguste Rodin", "Jeff Koons"], "Arturo Di Modica"),
    ("art_166", "Which sculptor created 'Column of the Infinite'?", ["Constantin Brâncuși", "Naum Gabo", "Antoine Pevsner", "Vladimir Tatlin"], "Constantin Brâncuși"),
    ("art_167", "Who created 'One and Three Chairs' (conceptual sculpture)?", ["Joseph Kosuth", "Sol LeWitt", "Lawrence Weiner", "Robert Morris"], "Joseph Kosuth"),
    ("art_168", "Which sculptor created kinetic sculptures powered by water?", ["Jean Tinguely", "Alexander Calder", "Naum Gabo", "George Rickey"], "Jean Tinguely"),
    ("art_169", "Who sculpted 'The Veiled Virgin'?", ["Giovanni Strazza", "Antonio Corradini", "Giuseppe Sanmartino", "Antonio Canova"], "Giovanni Strazza"),
    ("art_170", "Which minimalist sculptor created 'Equivalent VIII' (the bricks)?", ["Carl Andre", "Donald Judd", "Dan Flavin", "Robert Morris"], "Carl Andre"),
    ("art_171", "Who created 'Sky Mirror' in Nottingham and New York?", ["Anish Kapoor", "Richard Serra", "Jeff Koons", "Antony Gormley"], "Anish Kapoor"),
    ("art_172", "Which sculptor created 'Angel of the North' in England?", ["Antony Gormley", "Henry Moore", "Barbara Hepworth", "Anthony Caro"], "Antony Gormley"),
    ("art_173", "Who sculpted 'The Veiled Christ' with translucent marble veil?", ["Giuseppe Sanmartino", "Antonio Corradini", "Giovanni Strazza", "Antonio Canova"], "Giuseppe Sanmartino"),
    ("art_174", "Which sculptor created 'The Monument to Balzac'?", ["Auguste Rodin", "Antoine Bourdelle", "Aristide Maillol", "Charles Despiau"], "Auguste Rodin"),
    ("art_175", "Who created 'Merzbau', an evolving sculptural installation?", ["Kurt Schwitters", "Marcel Duchamp", "Hans Arp", "Max Ernst"], "Kurt Schwitters"),
    ("art_176", "Which sculptor created 'Double Negative' by removing 240,000 tons of rock?", ["Michael Heizer", "Robert Smithson", "Walter De Maria", "Nancy Holt"], "Michael Heizer"),
    ("art_177", "Who created 'House' (a concrete cast of a Victorian house's interior)?", ["Rachel Whiteread", "Anish Kapoor", "Antony Gormley", "Cornelia Parker"], "Rachel Whiteread"),
    ("art_178", "Which sculptor created 'The Physical Impossibility of Death'?", ["Damien Hirst", "Jeff Koons", "Maurizio Cattelan", "Takashi Murakami"], "Damien Hirst"),
    ("art_179", "Who created 'The Spire' (Monument of Light) in Dublin?", ["Ian Ritchie", "Norman Foster", "Richard Rogers", "Santiago Calatrava"], "Ian Ritchie"),
    ("art_180", "Which sculptor created 'The Lightning Field' in New Mexico?", ["Walter De Maria", "Robert Smithson", "Michael Heizer", "Nancy Holt"], "Walter De Maria"),
]

for q in hard:
    new_questions.append({"id": q[0], "category": "Art", "subcategory": "Sculpture", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "hard", "topic": None, "subtopic": None})

# Load, add, sort, save
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

data['categories']['Art'].extend(new_questions)
data['categories']['Art'].sort(key=lambda q: int(q['id'].split('_')[1]))

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added 60 Sculpture questions")
print(f"Art now has {len(data['categories']['Art'])} total questions")
print(f"Added: 20 easy, 20 medium, 20 hard")
