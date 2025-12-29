#!/usr/bin/env python3
"""Add 50 Authors & Biography questions from scratch"""
import json

new_questions = []

# Easy questions (17)
easy = [
    ("lit_274", "What was Mark Twain's real name?", ["Samuel Clemens", "William Porter", "Charles Dickens", "Eric Blair"], "Samuel Clemens"),
    ("lit_275", "What was George Orwell's real name?", ["Eric Blair", "Charles Dodgson", "Mary Ann Evans", "Samuel Clemens"], "Eric Blair"),
    ("lit_276", "Which author wrote under the pen name Lewis Carroll?", ["Charles Dodgson", "Eric Blair", "Samuel Clemens", "William Porter"], "Charles Dodgson"),
    ("lit_277", "What pen name did Mary Ann Evans use?", ["George Eliot", "George Sand", "Currer Bell", "Ellis Bell"], "George Eliot"),
    ("lit_278", "Which author is known for writing while standing at a desk?", ["Ernest Hemingway", "Charles Dickens", "Victor Hugo", "Philip Roth"], "Ernest Hemingway"),
    ("lit_279", "Who won the Nobel Prize in Literature in 2016?", ["Bob Dylan", "Kazuo Ishiguro", "Louise Glück", "Annie Ernaux"], "Bob Dylan"),
    ("lit_280", "Which author created the characters Sherlock Holmes and Dr. Watson?", ["Arthur Conan Doyle", "Agatha Christie", "Edgar Allan Poe", "G.K. Chesterton"], "Arthur Conan Doyle"),
    ("lit_281", "Who wrote under the pen name 'Boz' early in their career?", ["Charles Dickens", "Mark Twain", "Oscar Wilde", "William Thackeray"], "Charles Dickens"),
    ("lit_282", "Which Brontë sister wrote under the pen name Currer Bell?", ["Charlotte Brontë", "Emily Brontë", "Anne Brontë", "Branwell Brontë"], "Charlotte Brontë"),
    ("lit_283", "Who is the best-selling fiction author of all time?", ["Agatha Christie", "William Shakespeare", "J.K. Rowling", "Stephen King"], "Agatha Christie"),
    ("lit_284", "Which author worked as a journalist before writing '1984'?", ["George Orwell", "Aldous Huxley", "Ray Bradbury", "Kurt Vonnegut"], "George Orwell"),
    ("lit_285", "Who wrote 'On Writing: A Memoir of the Craft'?", ["Stephen King", "Annie Dillard", "Anne Lamott", "William Zinsser"], "Stephen King"),
    ("lit_286", "Which author founded The Paris Review literary magazine?", ["George Plimpton", "Ernest Hemingway", "James Baldwin", "Norman Mailer"], "George Plimpton"),
    ("lit_287", "What nationality was author Franz Kafka?", ["Czech", "German", "Austrian", "Polish"], "Czech"),
    ("lit_288", "Which author served as U.S. Ambassador to Spain?", ["Washington Irving", "James Russell Lowell", "Nathaniel Hawthorne", "Henry James"], "Washington Irving"),
    ("lit_289", "Who was the first African American woman to win the Nobel Prize in Literature?", ["Toni Morrison", "Maya Angelou", "Alice Walker", "Zora Neale Hurston"], "Toni Morrison"),
    ("lit_290", "Which author wrote the essay 'Politics and the English Language'?", ["George Orwell", "Aldous Huxley", "E.M. Forster", "Virginia Woolf"], "George Orwell"),
]

for q in easy:
    new_questions.append({"id": q[0], "category": "Literature", "subcategory": "Authors & Biography", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "easy", "topic": None, "subtopic": None})

# Medium questions (17)
medium = [
    ("lit_291", "Which Romantic poet drowned at age 29 in the Gulf of Spezia?", ["Percy Bysshe Shelley", "John Keats", "Lord Byron", "Samuel Taylor Coleridge"], "Percy Bysshe Shelley"),
    ("lit_292", "What was O. Henry's real name?", ["William Sydney Porter", "Samuel Clemens", "Eric Blair", "Theodore Geisel"], "William Sydney Porter"),
    ("lit_293", "Which author was a licensed pilot on Mississippi riverboats?", ["Mark Twain", "Herman Melville", "Jack London", "Ernest Hemingway"], "Mark Twain"),
    ("lit_294", "Who wrote under the collective pen name 'Ellery Queen' with their cousin?", ["Frederic Dannay and Manfred Lee", "Erle Stanley Gardner", "Dashiell Hammett", "Raymond Chandler"], "Frederic Dannay and Manfred Lee"),
    ("lit_295", "Which author served as an ambulance driver in World War I?", ["Ernest Hemingway", "F. Scott Fitzgerald", "John Dos Passos", "E.E. Cummings"], "Ernest Hemingway"),
    ("lit_296", "What pen name did Charlotte Brontë's sister Emily use?", ["Ellis Bell", "Currer Bell", "Acton Bell", "George Eliot"], "Ellis Bell"),
    ("lit_297", "Which Beat Generation writer worked as a fire lookout?", ["Jack Kerouac", "Allen Ginsberg", "Gary Snyder", "Lawrence Ferlinghetti"], "Jack Kerouac"),
    ("lit_298", "Who won the Pulitzer Prize four times for drama?", ["Eugene O'Neill", "Tennessee Williams", "Arthur Miller", "Edward Albee"], "Eugene O'Neill"),
    ("lit_299", "Which author's middle name was Conan, not a pen name?", ["Arthur Conan Doyle", "Arthur Conan", "Conan O'Brien", "Robert E. Howard"], "Arthur Conan Doyle"),
    ("lit_300", "What was Dr. Seuss's real name?", ["Theodor Seuss Geisel", "Theodore Geisel Seuss", "Seuss Theodore Geisel", "Theodor Geisel"], "Theodor Seuss Geisel"),
    ("lit_301", "Which author declined the Nobel Prize in Literature in 1964?", ["Jean-Paul Sartre", "Albert Camus", "Boris Pasternak", "Aleksandr Solzhenitsyn"], "Jean-Paul Sartre"),
    ("lit_302", "Who was the first American-born woman to win the Nobel Prize in Literature?", ["Toni Morrison", "Pearl S. Buck", "Sinclair Lewis", "Eugene O'Neill"], "Toni Morrison"),
    ("lit_303", "Which author worked as a customs inspector while writing poetry?", ["Geoffrey Chaucer", "William Wordsworth", "Herman Melville", "Wallace Stevens"], "Geoffrey Chaucer"),
    ("lit_304", "What literary movement was founded by André Breton in 1924?", ["Surrealism", "Dadaism", "Futurism", "Expressionism"], "Surrealism"),
    ("lit_305", "Which author duo wrote as 'Nicci French'?", ["Nicci Gerrard and Sean French", "Nicci Harris and David French", "Nicole French and Sean Gerrard", "Nicola French"], "Nicci Gerrard and Sean French"),
    ("lit_306", "Who was the youngest recipient of the Nobel Prize in Literature?", ["Rudyard Kipling", "Albert Camus", "Bob Dylan", "Toni Morrison"], "Rudyard Kipling"),
    ("lit_307", "Which Harlem Renaissance writer worked as Langston Hughes's secretary?", ["Zora Neale Hurston", "Nella Larsen", "Jessie Fauset", "Dorothy West"], "Zora Neale Hurston"),
]

for q in medium:
    new_questions.append({"id": q[0], "category": "Literature", "subcategory": "Authors & Biography", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "medium", "topic": None, "subtopic": None})

# Hard questions (16)
hard = [
    ("lit_308", "Which modernist writer worked as a bank clerk for Lloyd's Bank?", ["T.S. Eliot", "Ezra Pound", "James Joyce", "Virginia Woolf"], "T.S. Eliot"),
    ("lit_309", "What was the pen name of Aurore Dupin, French novelist?", ["George Sand", "George Eliot", "Colette", "Simone de Beauvoir"], "George Sand"),
    ("lit_310", "Which author was expelled from West Point for deliberately neglecting duties?", ["Edgar Allan Poe", "Herman Melville", "Ambrose Bierce", "Stephen Crane"], "Edgar Allan Poe"),
    ("lit_311", "Who wrote under the heteronym 'Alberto Caeiro'?", ["Fernando Pessoa", "Jorge Luis Borges", "Octavio Paz", "Pablo Neruda"], "Fernando Pessoa"),
    ("lit_312", "Which Existentialist author worked in the French Resistance?", ["Albert Camus", "Jean-Paul Sartre", "Simone de Beauvoir", "André Malraux"], "Albert Camus"),
    ("lit_313", "What was Isak Dinesen's real name?", ["Karen Blixen", "Sigrid Undset", "Selma Lagerlöf", "Astrid Lindgren"], "Karen Blixen"),
    ("lit_314", "Which author founded the literary movement 'Imagism'?", ["Ezra Pound", "T.S. Eliot", "H.D. (Hilda Doolittle)", "Amy Lowell"], "Ezra Pound"),
    ("lit_315", "Who was the first woman to win the Neustadt International Prize for Literature?", ["Elizabeth Bishop", "Gabriela Mistral", "Octavio Paz", "Czesław Miłosz"], "Elizabeth Bishop"),
    ("lit_316", "Which author wrote under at least 72 different heteronyms?", ["Fernando Pessoa", "Jorge Luis Borges", "Italo Calvino", "Umberto Eco"], "Fernando Pessoa"),
    ("lit_317", "What was the pen name of Aleksey Maksimovich Peshkov?", ["Maxim Gorky", "Anton Chekhov", "Ivan Turgenev", "Nikolai Gogol"], "Maxim Gorky"),
    ("lit_318", "Which Oulipo member wrote 'Life: A User's Manual'?", ["Georges Perec", "Italo Calvino", "Raymond Queneau", "Jacques Roubaud"], "Georges Perec"),
    ("lit_319", "Who was the first Latin American to win the Nobel Prize in Literature?", ["Gabriela Mistral", "Pablo Neruda", "Gabriel García Márquez", "Octavio Paz"], "Gabriela Mistral"),
    ("lit_320", "Which Victorian author worked as an opium addict and ran a household with Dante Gabriel Rossetti?", ["Algernon Charles Swinburne", "Christina Rossetti", "Elizabeth Siddal", "William Morris"], "Algernon Charles Swinburne"),
    ("lit_321", "What was George Sand's relationship to Frédéric Chopin?", ["Romantic partner", "Sister", "Patron", "Student"], "Romantic partner"),
    ("lit_322", "Which author founded the literary theory of 'Carnivalization'?", ["Mikhail Bakhtin", "Viktor Shklovsky", "Roman Jakobson", "Vladimir Propp"], "Mikhail Bakhtin"),
    ("lit_323", "Who wrote the 'Oulipo' constraint novel 'A Void' without using the letter 'e'?", ["Georges Perec", "Raymond Queneau", "Italo Calvino", "Jacques Roubaud"], "Georges Perec"),
]

for q in hard:
    new_questions.append({"id": q[0], "category": "Literature", "subcategory": "Authors & Biography", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "hard", "topic": None, "subtopic": None})

# Load, add, sort, save
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

data['categories']['Literature'].extend(new_questions)
data['categories']['Literature'].sort(key=lambda q: int(q['id'].split('_')[1]))

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added 50 Authors & Biography questions")
print(f"Literature now has {len(data['categories']['Literature'])} total questions")
print(f"Added: 17 easy, 17 medium, 16 hard")
