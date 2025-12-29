#!/usr/bin/env python3
"""Add 40 Fantasy Literature questions to reach 50 total"""
import json

new_questions = []

# Easy questions (13)
easy = [
    ("lit_034", "Who wrote 'The Lord of the Rings'?", ["J.R.R. Tolkien", "C.S. Lewis", "George R.R. Martin", "Terry Pratchett"], "J.R.R. Tolkien"),
    ("lit_035", "What is the name of the lion in 'The Chronicles of Narnia'?", ["Aslan", "Simba", "Mufasa", "Leo"], "Aslan"),
    ("lit_036", "Who wrote 'The Hobbit'?", ["J.R.R. Tolkien", "C.S. Lewis", "J.K. Rowling", "Terry Brooks"], "J.R.R. Tolkien"),
    ("lit_037", "What is the name of the wizard in 'The Lord of the Rings'?", ["Gandalf", "Merlin", "Dumbledore", "Saruman"], "Gandalf"),
    ("lit_038", "Who wrote 'The Chronicles of Narnia'?", ["C.S. Lewis", "J.R.R. Tolkien", "Philip Pullman", "Roald Dahl"], "C.S. Lewis"),
    ("lit_039", "What creature is Smaug in 'The Hobbit'?", ["Dragon", "Troll", "Goblin", "Wizard"], "Dragon"),
    ("lit_040", "Who created the Discworld series?", ["Terry Pratchett", "Neil Gaiman", "Douglas Adams", "Terry Brooks"], "Terry Pratchett"),
    ("lit_041", "What is the name of Frodo's gardener in LOTR?", ["Samwise Gamgee", "Merry Brandybuck", "Pippin Took", "Bilbo Baggins"], "Samwise Gamgee"),
    ("lit_042", "Who wrote 'A Game of Thrones'?", ["George R.R. Martin", "J.R.R. Tolkien", "Patrick Rothfuss", "Brandon Sanderson"], "George R.R. Martin"),
    ("lit_043", "What magical land is accessed through a wardrobe?", ["Narnia", "Oz", "Wonderland", "Neverland"], "Narnia"),
    ("lit_044", "Who wrote 'The Name of the Wind'?", ["Patrick Rothfuss", "Brandon Sanderson", "Patrick Rothfuss", "Terry Goodkind"], "Patrick Rothfuss"),
    ("lit_045", "What race is Legolas in LOTR?", ["Elf", "Dwarf", "Human", "Hobbit"], "Elf"),
    ("lit_046", "Who wrote 'American Gods'?", ["Neil Gaiman", "Terry Pratchett", "China Miéville", "Stephen King"], "Neil Gaiman"),
]

for q in easy:
    new_questions.append({"id": q[0], "category": "Literature", "subcategory": "Fantasy Literature", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "easy", "topic": None, "subtopic": None})

# Medium questions (14)
medium = [
    ("lit_047", "Who wrote 'The Wheel of Time' series?", ["Robert Jordan", "Brandon Sanderson", "Terry Goodkind", "Raymond E. Feist"], "Robert Jordan"),
    ("lit_048", "What is the One Ring's inscription in LOTR?", ["A ring inscription in the Black Speech", "Elvish runes", "Dwarvish text", "Ancient English"], "A ring inscription in the Black Speech"),
    ("lit_049", "Who wrote 'The Earthsea Cycle'?", ["Ursula K. Le Guin", "Anne McCaffrey", "Marion Zimmer Bradley", "Robin Hobb"], "Ursula K. Le Guin"),
    ("lit_050", "What is the capital of Westeros in 'A Song of Ice and Fire'?", ["King's Landing", "Winterfell", "Casterly Rock", "The Eyrie"], "King's Landing"),
    ("lit_051", "Who wrote 'The Stormlight Archive'?", ["Brandon Sanderson", "Patrick Rothfuss", "Joe Abercrombie", "Mark Lawrence"], "Brandon Sanderson"),
    ("lit_052", "What race are Gimli and Thorin in Tolkien's works?", ["Dwarves", "Elves", "Hobbits", "Ents"], "Dwarves"),
    ("lit_053", "Who wrote 'The Dark Tower' series?", ["Stephen King", "Dean Koontz", "Clive Barker", "Peter Straub"], "Stephen King"),
    ("lit_054", "What is the name of the school in 'The Name of the Wind'?", ["The University", "Hogwarts", "The Arcanum", "The Academy"], "The University"),
    ("lit_055", "Who wrote 'The Malazan Book of the Fallen'?", ["Steven Erikson", "Ian C. Esslemont", "Glen Cook", "R. Scott Bakker"], "Steven Erikson"),
    ("lit_056", "What is the ancient elvish city in LOTR?", ["Rivendell", "Lothlorien", "Mirkwood", "Grey Havens"], "Rivendell"),
    ("lit_057", "Who wrote 'The Kingkiller Chronicle'?", ["Patrick Rothfuss", "Brandon Sanderson", "Brent Weeks", "Peter V. Brett"], "Patrick Rothfuss"),
    ("lit_058", "What is the name of Jon Snow's direwolf?", ["Ghost", "Grey Wind", "Summer", "Nymeria"], "Ghost"),
    ("lit_059", "Who wrote 'The First Law' trilogy?", ["Joe Abercrombie", "Mark Lawrence", "Anthony Ryan", "Brian McClellan"], "Joe Abercrombie"),
    ("lit_060", "What is the ring of power called in LOTR?", ["The One Ring", "The Ring of Sauron", "The Master Ring", "The Dark Ring"], "The One Ring"),
]

for q in medium:
    new_questions.append({"id": q[0], "category": "Literature", "subcategory": "Fantasy Literature", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "medium", "topic": None, "subtopic": None})

# Hard questions (13)
hard = [
    ("lit_061", "Who completed 'The Wheel of Time' after Robert Jordan's death?", ["Brandon Sanderson", "Harriet McDougal", "Tom Doherty", "Brandon Sanderson"], "Brandon Sanderson"),
    ("lit_062", "What is the name of the magic system in Brandon Sanderson's Mistborn?", ["Allomancy", "Feruchemy", "Hemalurgy", "All of the above"], "All of the above"),
    ("lit_063", "Who wrote 'The Black Company'?", ["Glen Cook", "Steven Erikson", "Joe Abercrombie", "R. Scott Bakker"], "Glen Cook"),
    ("lit_064", "What is the ancient language in 'The Inheritance Cycle'?", ["The Ancient Language", "Elvish", "Dragon tongue", "Old Speech"], "The Ancient Language"),
    ("lit_065", "Who wrote 'The Book of the New Sun'?", ["Gene Wolfe", "Jack Vance", "M. John Harrison", "China Miéville"], "Gene Wolfe"),
    ("lit_066", "What is the world called in 'The Wheel of Time'?", ["The World", "Randland", "The Westlands", "Tar Valon"], "The World"),
    ("lit_067", "Who wrote 'Gormenghast'?", ["Mervyn Peake", "Michael Moorcock", "Fritz Leiber", "Lord Dunsany"], "Mervyn Peake"),
    ("lit_068", "What is Kvothe's true name in 'The Kingkiller Chronicle'?", ["Kvothe (his calling name)", "Kote", "Maedre", "All are names he uses"], "All are names he uses"),
    ("lit_069", "Who wrote 'The Dying Earth'?", ["Jack Vance", "Gene Wolfe", "Clark Ashton Smith", "Fritz Leiber"], "Jack Vance"),
    ("lit_070", "What is the capital city in Robert Jordan's 'Wheel of Time'?", ["Tar Valon (Aes Sedai)", "Caemlyn", "Cairhien", "Tear"], "Tar Valon (Aes Sedai)"),
    ("lit_071", "Who wrote 'The Broken Empire' trilogy?", ["Mark Lawrence", "Joe Abercrombie", "Anthony Ryan", "Brian McClellan"], "Mark Lawrence"),
    ("lit_072", "What is the magic system called in Patrick Rothfuss's work?", ["Sympathy", "Naming", "Both sympathy and naming", "Alar"], "Both sympathy and naming"),
    ("lit_073", "Who wrote 'The Prince of Nothing' trilogy?", ["R. Scott Bakker", "Steven Erikson", "Glen Cook", "Mark Lawrence"], "R. Scott Bakker"),
]

for q in hard:
    new_questions.append({"id": q[0], "category": "Literature", "subcategory": "Fantasy Literature", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "hard", "topic": None, "subtopic": None})

# Load, add, sort, save
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

data['categories']['Literature'].extend(new_questions)
data['categories']['Literature'].sort(key=lambda q: int(q['id'].split('_')[1]))

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added 40 Fantasy Literature questions")
print(f"Literature now has {len(data['categories']['Literature'])} total questions")

fantasy = [q for q in data['categories']['Literature'] if q['subcategory'] == 'Fantasy Literature']
print(f"Fantasy Literature: {len(fantasy)} questions")
print(f"Added: 13 easy, 14 medium, 13 hard")
