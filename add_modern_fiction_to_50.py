#!/usr/bin/env python3
"""Add 50 Modern Fiction questions from scratch"""
import json

new_questions = []

# Easy questions (17)
easy = [
    ("lit_124", "Who wrote 'The Hunger Games'?", ["Suzanne Collins", "Veronica Roth", "Stephenie Meyer", "Cassandra Clare"], "Suzanne Collins"),
    ("lit_125", "Who wrote 'The Da Vinci Code'?", ["Dan Brown", "John Grisham", "Michael Crichton", "Tom Clancy"], "Dan Brown"),
    ("lit_126", "Who wrote 'The Girl with the Dragon Tattoo'?", ["Stieg Larsson", "Jo Nesbø", "Henning Mankell", "Camilla Läckberg"], "Stieg Larsson"),
    ("lit_127", "Who wrote 'The Kite Runner'?", ["Khaled Hosseini", "Jhumpa Lahiri", "Aravind Adiga", "Mohsin Hamid"], "Khaled Hosseini"),
    ("lit_128", "Who wrote 'Life of Pi'?", ["Yann Martel", "Salman Rushdie", "Arundhati Roy", "Vikram Seth"], "Yann Martel"),
    ("lit_129", "Who wrote 'The Fault in Our Stars'?", ["John Green", "Rainbow Rowell", "David Levithan", "Gayle Forman"], "John Green"),
    ("lit_130", "Who wrote 'Gone Girl'?", ["Gillian Flynn", "Paula Hawkins", "Tana French", "Ruth Ware"], "Gillian Flynn"),
    ("lit_131", "Who wrote 'The Help'?", ["Kathryn Stockett", "Sue Monk Kidd", "Jodi Picoult", "Alice Sebold"], "Kathryn Stockett"),
    ("lit_132", "Who wrote 'The Lovely Bones'?", ["Alice Sebold", "Jodi Picoult", "Kathryn Stockett", "Sue Monk Kidd"], "Alice Sebold"),
    ("lit_133", "Who wrote 'The Handmaid's Tale'?", ["Margaret Atwood", "Ursula K. Le Guin", "Octavia Butler", "Doris Lessing"], "Margaret Atwood"),
    ("lit_134", "Who wrote 'The Road'?", ["Cormac McCarthy", "Don DeLillo", "Philip Roth", "Jonathan Franzen"], "Cormac McCarthy"),
    ("lit_135", "Who wrote 'Twilight'?", ["Stephenie Meyer", "Cassandra Clare", "Suzanne Collins", "Veronica Roth"], "Stephenie Meyer"),
    ("lit_136", "Who wrote 'The Alchemist'?", ["Paulo Coelho", "Gabriel García Márquez", "Isabel Allende", "Jorge Amado"], "Paulo Coelho"),
    ("lit_137", "Who wrote 'A Thousand Splendid Suns'?", ["Khaled Hosseini", "Jhumpa Lahiri", "Aravind Adiga", "Mohsin Hamid"], "Khaled Hosseini"),
    ("lit_138", "Who wrote 'The Girl on the Train'?", ["Paula Hawkins", "Gillian Flynn", "Tana French", "Ruth Ware"], "Paula Hawkins"),
    ("lit_139", "Who wrote 'Water for Elephants'?", ["Sara Gruen", "Kathryn Stockett", "Sue Monk Kidd", "Jodi Picoult"], "Sara Gruen"),
    ("lit_140", "Who wrote 'The Book Thief'?", ["Markus Zusak", "John Boyne", "Anthony Doerr", "Geraldine Brooks"], "Markus Zusak"),
]

for q in easy:
    new_questions.append({"id": q[0], "category": "Literature", "subcategory": "Modern Fiction", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "easy", "topic": None, "subtopic": None})

# Medium questions (17)
medium = [
    ("lit_141", "Who wrote 'The Secret History'?", ["Donna Tartt", "Bret Easton Ellis", "Jay McInerney", "Jonathan Franzen"], "Donna Tartt"),
    ("lit_142", "Who wrote 'White Teeth'?", ["Zadie Smith", "Chimamanda Ngozi Adichie", "Jhumpa Lahiri", "Monica Ali"], "Zadie Smith"),
    ("lit_143", "Who wrote 'Middlesex'?", ["Jeffrey Eugenides", "Jonathan Franzen", "Michael Chabon", "Rick Moody"], "Jeffrey Eugenides"),
    ("lit_144", "Who wrote 'The Corrections'?", ["Jonathan Franzen", "Don DeLillo", "Philip Roth", "David Foster Wallace"], "Jonathan Franzen"),
    ("lit_145", "Who wrote 'Infinite Jest'?", ["David Foster Wallace", "Thomas Pynchon", "Don DeLillo", "Jonathan Franzen"], "David Foster Wallace"),
    ("lit_146", "Who wrote 'Cloud Atlas'?", ["David Mitchell", "Haruki Murakami", "Kazuo Ishiguro", "Ian McEwan"], "David Mitchell"),
    ("lit_147", "Who wrote 'Never Let Me Go'?", ["Kazuo Ishiguro", "Ian McEwan", "Julian Barnes", "Martin Amis"], "Kazuo Ishiguro"),
    ("lit_148", "Who wrote 'Atonement'?", ["Ian McEwan", "Kazuo Ishiguro", "Julian Barnes", "Graham Swift"], "Ian McEwan"),
    ("lit_149", "Who wrote 'The Amazing Adventures of Kavalier & Clay'?", ["Michael Chabon", "Jonathan Safran Foer", "Jeffrey Eugenides", "Dave Eggers"], "Michael Chabon"),
    ("lit_150", "Who wrote 'Everything Is Illuminated'?", ["Jonathan Safran Foer", "Michael Chabon", "Nicole Krauss", "Nathan Englander"], "Jonathan Safran Foer"),
    ("lit_151", "Who wrote 'The Brief Wondrous Life of Oscar Wao'?", ["Junot Díaz", "Gabriel García Márquez", "Roberto Bolaño", "Carlos Fuentes"], "Junot Díaz"),
    ("lit_152", "Who wrote '2666'?", ["Roberto Bolaño", "Gabriel García Márquez", "Mario Vargas Llosa", "Carlos Fuentes"], "Roberto Bolaño"),
    ("lit_153", "Who wrote 'The Underground Railroad'?", ["Colson Whitehead", "Ta-Nehisi Coates", "Jesmyn Ward", "Yaa Gyasi"], "Colson Whitehead"),
    ("lit_154", "Who wrote 'Half of a Yellow Sun'?", ["Chimamanda Ngozi Adichie", "Zadie Smith", "Yaa Gyasi", "NoViolet Bulawayo"], "Chimamanda Ngozi Adichie"),
    ("lit_155", "Who wrote 'The Goldfinch'?", ["Donna Tartt", "Jennifer Egan", "Ann Patchett", "Elizabeth Strout"], "Donna Tartt"),
    ("lit_156", "Who wrote 'A Visit from the Goon Squad'?", ["Jennifer Egan", "Donna Tartt", "Ann Patchett", "Alice Munro"], "Jennifer Egan"),
    ("lit_157", "Who wrote 'Norwegian Wood'?", ["Haruki Murakami", "Kazuo Ishiguro", "Yukio Mishima", "Kenzaburō Ōe"], "Haruki Murakami"),
]

for q in medium:
    new_questions.append({"id": q[0], "category": "Literature", "subcategory": "Modern Fiction", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "medium", "topic": None, "subtopic": None})

# Hard questions (16)
hard = [
    ("lit_158", "Who wrote 'Gravity's Rainbow'?", ["Thomas Pynchon", "Don DeLillo", "David Foster Wallace", "William Gaddis"], "Thomas Pynchon"),
    ("lit_159", "Who wrote 'Underworld'?", ["Don DeLillo", "Thomas Pynchon", "Philip Roth", "Cormac McCarthy"], "Don DeLillo"),
    ("lit_160", "Who wrote 'American Pastoral'?", ["Philip Roth", "Don DeLillo", "Saul Bellow", "John Updike"], "Philip Roth"),
    ("lit_161", "Who wrote 'Blood Meridian'?", ["Cormac McCarthy", "Don DeLillo", "Philip Roth", "Thomas Pynchon"], "Cormac McCarthy"),
    ("lit_162", "Who wrote 'The Recognitions'?", ["William Gaddis", "Thomas Pynchon", "Don DeLillo", "David Foster Wallace"], "William Gaddis"),
    ("lit_163", "Who wrote 'The Wind-Up Bird Chronicle'?", ["Haruki Murakami", "Kenzaburō Ōe", "Yukio Mishima", "Jun'ichirō Tanizaki"], "Haruki Murakami"),
    ("lit_164", "Who wrote 'The Satanic Verses'?", ["Salman Rushdie", "V.S. Naipaul", "Arundhati Roy", "Vikram Seth"], "Salman Rushdie"),
    ("lit_165", "Who wrote 'Disgrace'?", ["J.M. Coetzee", "Nadine Gordimer", "Doris Lessing", "Alan Paton"], "J.M. Coetzee"),
    ("lit_166", "Who wrote 'The Remains of the Day'?", ["Kazuo Ishiguro", "Ian McEwan", "Julian Barnes", "Graham Swift"], "Kazuo Ishiguro"),
    ("lit_167", "Who wrote 'The Blind Assassin'?", ["Margaret Atwood", "Alice Munro", "Carol Shields", "Anne Michaels"], "Margaret Atwood"),
    ("lit_168", "Who wrote 'The God of Small Things'?", ["Arundhati Roy", "Jhumpa Lahiri", "Kiran Desai", "Anita Desai"], "Arundhati Roy"),
    ("lit_169", "Who wrote 'Austerlitz'?", ["W.G. Sebald", "Thomas Bernhard", "Peter Handke", "Elfriede Jelinek"], "W.G. Sebald"),
    ("lit_170", "Who wrote 'The Savage Detectives'?", ["Roberto Bolaño", "Carlos Fuentes", "Mario Vargas Llosa", "Julio Cortázar"], "Roberto Bolaño"),
    ("lit_171", "Who wrote 'The Inheritance of Loss'?", ["Kiran Desai", "Arundhati Roy", "Jhumpa Lahiri", "Anita Desai"], "Kiran Desai"),
    ("lit_172", "Who wrote 'Wolf Hall'?", ["Hilary Mantel", "Eleanor Catton", "Zadie Smith", "Sarah Waters"], "Hilary Mantel"),
    ("lit_173", "Who wrote 'The Luminaries'?", ["Eleanor Catton", "Hilary Mantel", "Kate Atkinson", "Sarah Waters"], "Eleanor Catton"),
]

for q in hard:
    new_questions.append({"id": q[0], "category": "Literature", "subcategory": "Modern Fiction", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "hard", "topic": None, "subtopic": None})

# Load, add, sort, save
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

data['categories']['Literature'].extend(new_questions)
data['categories']['Literature'].sort(key=lambda q: int(q['id'].split('_')[1]))

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added 50 Modern Fiction questions")
print(f"Literature now has {len(data['categories']['Literature'])} total questions")
print(f"Added: 17 easy, 17 medium, 16 hard")
