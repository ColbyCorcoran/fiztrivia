#!/usr/bin/env python3
"""Add 60 Famous Painters questions from scratch"""
import json

new_questions = []

# Easy questions (20)
easy = [
    ("art_001", "Who painted the Mona Lisa?", ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"], "Leonardo da Vinci"),
    ("art_002", "Who painted 'Starry Night'?", ["Vincent van Gogh", "Claude Monet", "Pablo Picasso", "Salvador Dalí"], "Vincent van Gogh"),
    ("art_003", "Who painted the ceiling of the Sistine Chapel?", ["Michelangelo", "Leonardo da Vinci", "Raphael", "Donatello"], "Michelangelo"),
    ("art_004", "Who is famous for his melting clocks painting 'The Persistence of Memory'?", ["Salvador Dalí", "Pablo Picasso", "René Magritte", "Joan Miró"], "Salvador Dalí"),
    ("art_005", "Who painted 'The Scream'?", ["Edvard Munch", "Vincent van Gogh", "Paul Gauguin", "Henri Matisse"], "Edvard Munch"),
    ("art_006", "Who painted 'Guernica'?", ["Pablo Picasso", "Salvador Dalí", "Joan Miró", "Georges Braque"], "Pablo Picasso"),
    ("art_007", "Who cut off part of his own ear?", ["Vincent van Gogh", "Paul Gauguin", "Henri de Toulouse-Lautrec", "Édouard Manet"], "Vincent van Gogh"),
    ("art_008", "Who painted 'The Last Supper'?", ["Leonardo da Vinci", "Michelangelo", "Raphael", "Caravaggio"], "Leonardo da Vinci"),
    ("art_009", "Who painted 'Girl with a Pearl Earring'?", ["Johannes Vermeer", "Rembrandt", "Frans Hals", "Jan Steen"], "Johannes Vermeer"),
    ("art_010", "Who painted numerous water lily paintings?", ["Claude Monet", "Pierre-Auguste Renoir", "Edgar Degas", "Camille Pissarro"], "Claude Monet"),
    ("art_011", "Who painted 'The Birth of Venus'?", ["Sandro Botticelli", "Leonardo da Vinci", "Raphael", "Titian"], "Sandro Botticelli"),
    ("art_012", "Who is known for his Campbell's Soup Cans artwork?", ["Andy Warhol", "Roy Lichtenstein", "Jackson Pollock", "Keith Haring"], "Andy Warhol"),
    ("art_013", "Who painted 'American Gothic'?", ["Grant Wood", "Edward Hopper", "Norman Rockwell", "Andrew Wyeth"], "Grant Wood"),
    ("art_014", "Who was a famous Mexican painter known for her self-portraits?", ["Frida Kahlo", "Diego Rivera", "Leonora Carrington", "Rufino Tamayo"], "Frida Kahlo"),
    ("art_015", "Who painted 'The Night Watch'?", ["Rembrandt", "Johannes Vermeer", "Frans Hals", "Pieter Bruegel"], "Rembrandt"),
    ("art_016", "Who is known for drip painting technique?", ["Jackson Pollock", "Willem de Kooning", "Mark Rothko", "Franz Kline"], "Jackson Pollock"),
    ("art_017", "Who painted 'The Kiss'?", ["Gustav Klimt", "Edvard Munch", "Egon Schiele", "Oskar Kokoschka"], "Gustav Klimt"),
    ("art_018", "Who painted 'Las Meninas'?", ["Diego Velázquez", "Francisco Goya", "El Greco", "Bartolomé Murillo"], "Diego Velázquez"),
    ("art_019", "Who created the sculpture 'David' (Renaissance)?", ["Michelangelo", "Donatello", "Leonardo da Vinci", "Bernini"], "Michelangelo"),
    ("art_020", "Who painted 'The Creation of Adam'?", ["Michelangelo", "Leonardo da Vinci", "Raphael", "Titian"], "Michelangelo"),
]

for q in easy:
    new_questions.append({"id": q[0], "category": "Art", "subcategory": "Famous Painters", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "easy", "topic": None, "subtopic": None})

# Medium questions (20)
medium = [
    ("art_021", "Who painted 'The Garden of Earthly Delights'?", ["Hieronymus Bosch", "Pieter Bruegel", "Jan van Eyck", "Albrecht Dürer"], "Hieronymus Bosch"),
    ("art_022", "Who was Frida Kahlo's husband, also a famous muralist?", ["Diego Rivera", "David Alfaro Siqueiros", "José Clemente Orozco", "Rufino Tamayo"], "Diego Rivera"),
    ("art_023", "Who painted 'Christina's World'?", ["Andrew Wyeth", "Edward Hopper", "Grant Wood", "Thomas Hart Benton"], "Andrew Wyeth"),
    ("art_024", "Who painted 'The School of Athens'?", ["Raphael", "Michelangelo", "Leonardo da Vinci", "Botticelli"], "Raphael"),
    ("art_025", "Who painted 'Impression, Sunrise' which gave Impressionism its name?", ["Claude Monet", "Pierre-Auguste Renoir", "Edgar Degas", "Camille Pissarro"], "Claude Monet"),
    ("art_026", "Who painted 'The Great Wave off Kanagawa'?", ["Katsushika Hokusai", "Utagawa Hiroshige", "Kitagawa Utamaro", "Ando Hiroshige"], "Katsushika Hokusai"),
    ("art_027", "Who painted 'Nighthawks'?", ["Edward Hopper", "Grant Wood", "Andrew Wyeth", "Georgia O'Keeffe"], "Edward Hopper"),
    ("art_028", "Who painted 'The Arnolfini Portrait'?", ["Jan van Eyck", "Rogier van der Weyden", "Hans Memling", "Hieronymus Bosch"], "Jan van Eyck"),
    ("art_029", "Who painted 'Olympia' which caused scandal in 1865?", ["Édouard Manet", "Gustave Courbet", "Edgar Degas", "Paul Cézanne"], "Édouard Manet"),
    ("art_030", "Who painted 'A Sunday Afternoon on the Island of La Grande Jatte'?", ["Georges Seurat", "Paul Signac", "Camille Pissarro", "Claude Monet"], "Georges Seurat"),
    ("art_031", "Who painted 'The Swing'?", ["Jean-Honoré Fragonard", "François Boucher", "Antoine Watteau", "Nicolas Poussin"], "Jean-Honoré Fragonard"),
    ("art_032", "Who painted 'Where Do We Come From? What Are We? Where Are We Going?'?", ["Paul Gauguin", "Vincent van Gogh", "Paul Cézanne", "Henri Rousseau"], "Paul Gauguin"),
    ("art_033", "Who painted 'The Raft of the Medusa'?", ["Théodore Géricault", "Eugène Delacroix", "Jacques-Louis David", "Jean-Auguste-Dominique Ingres"], "Théodore Géricault"),
    ("art_034", "Who is known for painting ballet dancers?", ["Edgar Degas", "Pierre-Auguste Renoir", "Mary Cassatt", "Berthe Morisot"], "Edgar Degas"),
    ("art_035", "Who painted 'The Third of May 1808'?", ["Francisco Goya", "Diego Velázquez", "El Greco", "Francisco de Zurbarán"], "Francisco Goya"),
    ("art_036", "Who painted 'The Son of Man' featuring a man with a green apple?", ["René Magritte", "Salvador Dalí", "Max Ernst", "Giorgio de Chirico"], "René Magritte"),
    ("art_037", "Who painted 'The Hay Wain'?", ["John Constable", "J.M.W. Turner", "Thomas Gainsborough", "Joshua Reynolds"], "John Constable"),
    ("art_038", "Who painted 'Liberty Leading the People'?", ["Eugène Delacroix", "Théodore Géricault", "Jacques-Louis David", "Jean-François Millet"], "Eugène Delacroix"),
    ("art_039", "Who painted 'The Fighting Temeraire'?", ["J.M.W. Turner", "John Constable", "William Blake", "Thomas Lawrence"], "J.M.W. Turner"),
    ("art_040", "Who painted 'The Card Players'?", ["Paul Cézanne", "Vincent van Gogh", "Paul Gauguin", "Henri de Toulouse-Lautrec"], "Paul Cézanne"),
]

for q in medium:
    new_questions.append({"id": q[0], "category": "Art", "subcategory": "Famous Painters", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "medium", "topic": None, "subtopic": None})

# Hard questions (20)
hard = [
    ("art_041", "Who painted 'The Ambassadors' featuring a distorted skull?", ["Hans Holbein the Younger", "Albrecht Dürer", "Lucas Cranach", "Hans Memling"], "Hans Holbein the Younger"),
    ("art_042", "Who painted 'Las Hilanderas' (The Spinners)?", ["Diego Velázquez", "Francisco Goya", "Bartolomé Murillo", "José de Ribera"], "Diego Velázquez"),
    ("art_043", "Who painted 'The Hunters in the Snow'?", ["Pieter Bruegel the Elder", "Hieronymus Bosch", "Jan van Eyck", "Pieter Bruegel the Younger"], "Pieter Bruegel the Elder"),
    ("art_044", "Who painted 'The Blind Leading the Blind'?", ["Pieter Bruegel the Elder", "Hieronymus Bosch", "Jan Steen", "Frans Hals"], "Pieter Bruegel the Elder"),
    ("art_045", "Who painted 'The Death of Marat'?", ["Jacques-Louis David", "Eugène Delacroix", "Jean-Auguste-Dominique Ingres", "Théodore Géricault"], "Jacques-Louis David"),
    ("art_046", "Who painted 'The Turkish Bath'?", ["Jean-Auguste-Dominique Ingres", "Jacques-Louis David", "Eugène Delacroix", "Théodore Chassériau"], "Jean-Auguste-Dominique Ingres"),
    ("art_047", "Who painted 'The Apotheosis of Homer'?", ["Jean-Auguste-Dominique Ingres", "Jacques-Louis David", "Nicolas Poussin", "Charles Le Brun"], "Jean-Auguste-Dominique Ingres"),
    ("art_048", "Who painted 'The Oxbow'?", ["Thomas Cole", "Frederic Edwin Church", "Albert Bierstadt", "Asher Brown Durand"], "Thomas Cole"),
    ("art_049", "Who painted 'Watson and the Shark'?", ["John Singleton Copley", "Benjamin West", "Gilbert Stuart", "Charles Willson Peale"], "John Singleton Copley"),
    ("art_050", "Who painted 'The Resurrection' fresco in Sansepolcro?", ["Piero della Francesca", "Masaccio", "Fra Angelico", "Paolo Uccello"], "Piero della Francesca"),
    ("art_051", "Who painted 'The Flagellation of Christ' with perfect linear perspective?", ["Piero della Francesca", "Masaccio", "Paolo Uccello", "Andrea Mantegna"], "Piero della Francesca"),
    ("art_052", "Who painted 'The Rokeby Venus'?", ["Diego Velázquez", "Titian", "Giorgione", "Peter Paul Rubens"], "Diego Velázquez"),
    ("art_053", "Who painted 'The Tempest' (La Tempesta)?", ["Giorgione", "Titian", "Tintoretto", "Veronese"], "Giorgione"),
    ("art_054", "Who painted 'The Tribute Money' fresco?", ["Masaccio", "Giotto", "Fra Angelico", "Piero della Francesca"], "Masaccio"),
    ("art_055", "Who painted 'The Nightmare'?", ["Henry Fuseli", "William Blake", "John Henry Fuseli", "James Barry"], "Henry Fuseli"),
    ("art_056", "Who painted 'The Naked Maja' and 'The Clothed Maja'?", ["Francisco Goya", "Diego Velázquez", "El Greco", "Bartolomé Murillo"], "Francisco Goya"),
    ("art_057", "Who painted 'The Fall of Icarus' (attributed)?", ["Pieter Bruegel the Elder", "Hieronymus Bosch", "Jan van Eyck", "Rogier van der Weyden"], "Pieter Bruegel the Elder"),
    ("art_058", "Who painted 'Saturn Devouring His Son'?", ["Francisco Goya", "Peter Paul Rubens", "Caravaggio", "José de Ribera"], "Francisco Goya"),
    ("art_059", "Who painted 'The Conspiracy of Claudius Civilis'?", ["Rembrandt", "Frans Hals", "Johannes Vermeer", "Jan Steen"], "Rembrandt"),
    ("art_060", "Who painted 'The Sleeping Gypsy'?", ["Henri Rousseau", "Paul Gauguin", "Henri Matisse", "André Derain"], "Henri Rousseau"),
]

for q in hard:
    new_questions.append({"id": q[0], "category": "Art", "subcategory": "Famous Painters", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "hard", "topic": None, "subtopic": None})

# Load, add, sort, save
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Create Art category if it doesn't exist
if 'Art' not in data['categories']:
    data['categories']['Art'] = []

data['categories']['Art'].extend(new_questions)
data['categories']['Art'].sort(key=lambda q: int(q['id'].split('_')[1]))

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added 60 Famous Painters questions")
print(f"Art now has {len(data['categories']['Art'])} total questions")
print(f"Added: 20 easy, 20 medium, 20 hard")
