#!/usr/bin/env python3
"""Add 50 Classic Literature questions from scratch"""
import json

new_questions = []

# Easy questions (17)
easy = [
    ("lit_074", "Who wrote 'Romeo and Juliet'?", ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"], "William Shakespeare"),
    ("lit_075", "Who wrote 'Pride and Prejudice'?", ["Jane Austen", "Charlotte Brontë", "Emily Brontë", "George Eliot"], "Jane Austen"),
    ("lit_076", "Who wrote 'A Tale of Two Cities'?", ["Charles Dickens", "Victor Hugo", "Alexandre Dumas", "Thomas Hardy"], "Charles Dickens"),
    ("lit_077", "Who wrote 'The Adventures of Tom Sawyer'?", ["Mark Twain", "Jack London", "Herman Melville", "Nathaniel Hawthorne"], "Mark Twain"),
    ("lit_078", "Who wrote 'Moby-Dick'?", ["Herman Melville", "Mark Twain", "Ernest Hemingway", "John Steinbeck"], "Herman Melville"),
    ("lit_079", "Who wrote 'Great Expectations'?", ["Charles Dickens", "Thomas Hardy", "George Eliot", "Anthony Trollope"], "Charles Dickens"),
    ("lit_080", "Who wrote 'Wuthering Heights'?", ["Emily Brontë", "Charlotte Brontë", "Jane Austen", "George Eliot"], "Emily Brontë"),
    ("lit_081", "Who wrote 'Jane Eyre'?", ["Charlotte Brontë", "Emily Brontë", "Jane Austen", "Elizabeth Gaskell"], "Charlotte Brontë"),
    ("lit_082", "Who wrote 'The Great Gatsby'?", ["F. Scott Fitzgerald", "Ernest Hemingway", "John Steinbeck", "William Faulkner"], "F. Scott Fitzgerald"),
    ("lit_083", "Who wrote 'To Kill a Mockingbird'?", ["Harper Lee", "John Steinbeck", "Truman Capote", "Flannery O'Connor"], "Harper Lee"),
    ("lit_084", "Who wrote 'Hamlet'?", ["William Shakespeare", "Christopher Marlowe", "Ben Jonson", "John Milton"], "William Shakespeare"),
    ("lit_085", "Who wrote '1984'?", ["George Orwell", "Aldous Huxley", "Ray Bradbury", "Arthur C. Clarke"], "George Orwell"),
    ("lit_086", "Who wrote 'The Picture of Dorian Gray'?", ["Oscar Wilde", "Robert Louis Stevenson", "Bram Stoker", "H.G. Wells"], "Oscar Wilde"),
    ("lit_087", "Who wrote 'Frankenstein'?", ["Mary Shelley", "Bram Stoker", "Edgar Allan Poe", "H.G. Wells"], "Mary Shelley"),
    ("lit_088", "Who wrote 'Dracula'?", ["Bram Stoker", "Mary Shelley", "Robert Louis Stevenson", "H.G. Wells"], "Bram Stoker"),
    ("lit_089", "Who wrote 'The Scarlet Letter'?", ["Nathaniel Hawthorne", "Herman Melville", "Edgar Allan Poe", "Washington Irving"], "Nathaniel Hawthorne"),
    ("lit_090", "Who wrote 'The Odyssey'?", ["Homer", "Virgil", "Ovid", "Sophocles"], "Homer"),
]

for q in easy:
    new_questions.append({"id": q[0], "category": "Literature", "subcategory": "Classic Literature", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "easy", "topic": None, "subtopic": None})

# Medium questions (17)
medium = [
    ("lit_091", "What city is the setting for 'A Tale of Two Cities'?", ["London and Paris", "London and Dublin", "Paris and Rome", "New York and Boston"], "London and Paris"),
    ("lit_092", "Who wrote 'Crime and Punishment'?", ["Fyodor Dostoevsky", "Leo Tolstoy", "Anton Chekhov", "Ivan Turgenev"], "Fyodor Dostoevsky"),
    ("lit_093", "Who wrote 'Anna Karenina'?", ["Leo Tolstoy", "Fyodor Dostoevsky", "Ivan Turgenev", "Nikolai Gogol"], "Leo Tolstoy"),
    ("lit_094", "Who wrote 'Les Misérables'?", ["Victor Hugo", "Alexandre Dumas", "Gustave Flaubert", "Émile Zola"], "Victor Hugo"),
    ("lit_095", "Who wrote 'The Count of Monte Cristo'?", ["Alexandre Dumas", "Victor Hugo", "Honoré de Balzac", "Guy de Maupassant"], "Alexandre Dumas"),
    ("lit_096", "What is the name of the whale in 'Moby-Dick'?", ["Moby Dick", "Leviathan", "The White Whale", "Ahab"], "Moby Dick"),
    ("lit_097", "Who wrote 'Madame Bovary'?", ["Gustave Flaubert", "Victor Hugo", "Émile Zola", "Guy de Maupassant"], "Gustave Flaubert"),
    ("lit_098", "Who wrote 'The Brothers Karamazov'?", ["Fyodor Dostoevsky", "Leo Tolstoy", "Anton Chekhov", "Maxim Gorky"], "Fyodor Dostoevsky"),
    ("lit_099", "Who wrote 'Don Quixote'?", ["Miguel de Cervantes", "Lope de Vega", "Federico García Lorca", "Pedro Calderón"], "Miguel de Cervantes"),
    ("lit_100", "Who wrote 'The Canterbury Tales'?", ["Geoffrey Chaucer", "William Langland", "John Gower", "Thomas Malory"], "Geoffrey Chaucer"),
    ("lit_101", "Who wrote 'Paradise Lost'?", ["John Milton", "William Blake", "Alexander Pope", "John Donne"], "John Milton"),
    ("lit_102", "Who wrote 'Gulliver's Travels'?", ["Jonathan Swift", "Daniel Defoe", "Henry Fielding", "Laurence Sterne"], "Jonathan Swift"),
    ("lit_103", "Who wrote 'Candide'?", ["Voltaire", "Jean-Jacques Rousseau", "Denis Diderot", "Montesquieu"], "Voltaire"),
    ("lit_104", "Who wrote 'The Hunchback of Notre-Dame'?", ["Victor Hugo", "Alexandre Dumas", "Gustave Flaubert", "Honoré de Balzac"], "Victor Hugo"),
    ("lit_105", "Who wrote 'Vanity Fair'?", ["William Makepeace Thackeray", "Charles Dickens", "Anthony Trollope", "George Eliot"], "William Makepeace Thackeray"),
    ("lit_106", "Who wrote 'Middlemarch'?", ["George Eliot", "Jane Austen", "Charlotte Brontë", "Elizabeth Gaskell"], "George Eliot"),
    ("lit_107", "Who wrote 'The Iliad'?", ["Homer", "Virgil", "Hesiod", "Sophocles"], "Homer"),
]

for q in medium:
    new_questions.append({"id": q[0], "category": "Literature", "subcategory": "Classic Literature", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "medium", "topic": None, "subtopic": None})

# Hard questions (16)
hard = [
    ("lit_108", "Who wrote 'The Divine Comedy'?", ["Dante Alighieri", "Petrarch", "Boccaccio", "Ariosto"], "Dante Alighieri"),
    ("lit_109", "Who wrote 'War and Peace'?", ["Leo Tolstoy", "Fyodor Dostoevsky", "Ivan Turgenev", "Anton Chekhov"], "Leo Tolstoy"),
    ("lit_110", "Who wrote 'Ulysses'?", ["James Joyce", "Samuel Beckett", "W.B. Yeats", "Oscar Wilde"], "James Joyce"),
    ("lit_111", "Who wrote 'In Search of Lost Time' (Remembrance of Things Past)?", ["Marcel Proust", "André Gide", "Albert Camus", "Jean-Paul Sartre"], "Marcel Proust"),
    ("lit_112", "Who wrote 'The Aeneid'?", ["Virgil", "Homer", "Ovid", "Horace"], "Virgil"),
    ("lit_113", "Who wrote 'Oedipus Rex'?", ["Sophocles", "Euripides", "Aeschylus", "Aristophanes"], "Sophocles"),
    ("lit_114", "Who wrote 'The Metamorphoses'?", ["Ovid", "Virgil", "Homer", "Horace"], "Ovid"),
    ("lit_115", "Who wrote 'One Hundred Years of Solitude'?", ["Gabriel García Márquez", "Jorge Luis Borges", "Pablo Neruda", "Octavio Paz"], "Gabriel García Márquez"),
    ("lit_116", "Who wrote 'The Master and Margarita'?", ["Mikhail Bulgakov", "Boris Pasternak", "Vladimir Nabokov", "Alexander Solzhenitsyn"], "Mikhail Bulgakov"),
    ("lit_117", "Who wrote 'The Trial'?", ["Franz Kafka", "Hermann Hesse", "Thomas Mann", "Robert Musil"], "Franz Kafka"),
    ("lit_118", "Who wrote 'The Sound and the Fury'?", ["William Faulkner", "Ernest Hemingway", "John Steinbeck", "F. Scott Fitzgerald"], "William Faulkner"),
    ("lit_119", "Who wrote 'Absalom, Absalom!'?", ["William Faulkner", "Thomas Wolfe", "Sinclair Lewis", "Theodore Dreiser"], "William Faulkner"),
    ("lit_120", "Who wrote 'The Grapes of Wrath'?", ["John Steinbeck", "William Faulkner", "Ernest Hemingway", "Sinclair Lewis"], "John Steinbeck"),
    ("lit_121", "Who wrote 'Beloved'?", ["Toni Morrison", "Alice Walker", "Maya Angelou", "Zora Neale Hurston"], "Toni Morrison"),
    ("lit_122", "Who wrote 'Invisible Man'?", ["Ralph Ellison", "Richard Wright", "James Baldwin", "Langston Hughes"], "Ralph Ellison"),
    ("lit_123", "Who wrote 'Catch-22'?", ["Joseph Heller", "Kurt Vonnegut", "Thomas Pynchon", "Norman Mailer"], "Joseph Heller"),
]

for q in hard:
    new_questions.append({"id": q[0], "category": "Literature", "subcategory": "Classic Literature", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "hard", "topic": None, "subtopic": None})

# Load, add, sort, save
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

data['categories']['Literature'].extend(new_questions)
data['categories']['Literature'].sort(key=lambda q: int(q['id'].split('_')[1]))

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added 50 Classic Literature questions")
print(f"Literature now has {len(data['categories']['Literature'])} total questions")
print(f"Added: 17 easy, 17 medium, 16 hard")
