#!/usr/bin/env python3
"""Add 50 Children's Books questions from scratch"""
import json

new_questions = []

# Easy questions (17)
easy = [
    ("lit_224", "Who wrote 'Charlotte's Web'?", ["E.B. White", "Roald Dahl", "Dr. Seuss", "Beverly Cleary"], "E.B. White"),
    ("lit_225", "Who wrote 'The Cat in the Hat'?", ["Dr. Seuss", "Roald Dahl", "E.B. White", "Eric Carle"], "Dr. Seuss"),
    ("lit_226", "Who wrote 'Where the Wild Things Are'?", ["Maurice Sendak", "Dr. Seuss", "Eric Carle", "Margaret Wise Brown"], "Maurice Sendak"),
    ("lit_227", "Who wrote 'Charlie and the Chocolate Factory'?", ["Roald Dahl", "Dr. Seuss", "E.B. White", "C.S. Lewis"], "Roald Dahl"),
    ("lit_228", "Who wrote 'The Very Hungry Caterpillar'?", ["Eric Carle", "Dr. Seuss", "Maurice Sendak", "Leo Lionni"], "Eric Carle"),
    ("lit_229", "Who wrote 'Goodnight Moon'?", ["Margaret Wise Brown", "Dr. Seuss", "Maurice Sendak", "Beatrix Potter"], "Margaret Wise Brown"),
    ("lit_230", "Who created the character Peter Rabbit?", ["Beatrix Potter", "A.A. Milne", "Kenneth Grahame", "E.B. White"], "Beatrix Potter"),
    ("lit_231", "Who wrote 'Winnie-the-Pooh'?", ["A.A. Milne", "Beatrix Potter", "Kenneth Grahame", "E.B. White"], "A.A. Milne"),
    ("lit_232", "Who wrote 'Green Eggs and Ham'?", ["Dr. Seuss", "Eric Carle", "Maurice Sendak", "Margaret Wise Brown"], "Dr. Seuss"),
    ("lit_233", "Who wrote 'The Tale of Peter Rabbit'?", ["Beatrix Potter", "A.A. Milne", "Enid Blyton", "Beverly Cleary"], "Beatrix Potter"),
    ("lit_234", "Who wrote 'Matilda'?", ["Roald Dahl", "Beverly Cleary", "Judy Blume", "Louis Sachar"], "Roald Dahl"),
    ("lit_235", "Who wrote 'The Giving Tree'?", ["Shel Silverstein", "Dr. Seuss", "Maurice Sendak", "Chris Van Allsburg"], "Shel Silverstein"),
    ("lit_236", "Who wrote 'Ramona the Pest'?", ["Beverly Cleary", "Judy Blume", "Roald Dahl", "Lois Lowry"], "Beverly Cleary"),
    ("lit_237", "Who wrote 'The BFG'?", ["Roald Dahl", "C.S. Lewis", "Enid Blyton", "Michael Bond"], "Roald Dahl"),
    ("lit_238", "Who wrote 'Curious George'?", ["H.A. Rey and Margret Rey", "Dr. Seuss", "Eric Carle", "Don Freeman"], "H.A. Rey and Margret Rey"),
    ("lit_239", "Who wrote 'Make Way for Ducklings'?", ["Robert McCloskey", "Dr. Seuss", "Maurice Sendak", "Chris Van Allsburg"], "Robert McCloskey"),
    ("lit_240", "Who wrote 'Corduroy'?", ["Don Freeman", "Eric Carle", "Leo Lionni", "Ezra Jack Keats"], "Don Freeman"),
]

for q in easy:
    new_questions.append({"id": q[0], "category": "Literature", "subcategory": "Children's Books", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "easy", "topic": None, "subtopic": None})

# Medium questions (17)
medium = [
    ("lit_241", "Who wrote 'A Wrinkle in Time'?", ["Madeleine L'Engle", "Lois Lowry", "Susan Cooper", "Lloyd Alexander"], "Madeleine L'Engle"),
    ("lit_242", "Who wrote 'The Giver'?", ["Lois Lowry", "Madeleine L'Engle", "Lois Duncan", "Paula Danziger"], "Lois Lowry"),
    ("lit_243", "Who wrote 'Holes'?", ["Louis Sachar", "Jerry Spinelli", "Gary Paulsen", "S.E. Hinton"], "Louis Sachar"),
    ("lit_244", "Who wrote 'Bridge to Terabithia'?", ["Katherine Paterson", "Lois Lowry", "Judy Blume", "Paula Danziger"], "Katherine Paterson"),
    ("lit_245", "Who wrote 'The Phantom Tollbooth'?", ["Norton Juster", "Roald Dahl", "E.L. Konigsburg", "Natalie Babbitt"], "Norton Juster"),
    ("lit_246", "Who wrote 'Tuck Everlasting'?", ["Natalie Babbitt", "Katherine Paterson", "Lois Lowry", "Madeleine L'Engle"], "Natalie Babbitt"),
    ("lit_247", "Who wrote 'Where the Red Fern Grows'?", ["Wilson Rawls", "Gary Paulsen", "Fred Gipson", "Jim Kjelgaard"], "Wilson Rawls"),
    ("lit_248", "Who wrote 'Island of the Blue Dolphins'?", ["Scott O'Dell", "Gary Paulsen", "Jean Craighead George", "Wilson Rawls"], "Scott O'Dell"),
    ("lit_249", "Who wrote 'The Wind in the Willows'?", ["Kenneth Grahame", "A.A. Milne", "Beatrix Potter", "E.B. White"], "Kenneth Grahame"),
    ("lit_250", "Who wrote 'Hatchet'?", ["Gary Paulsen", "Will Hobbs", "Jean Craighead George", "Scott O'Dell"], "Gary Paulsen"),
    ("lit_251", "Who wrote 'The Secret Garden'?", ["Frances Hodgson Burnett", "Louisa May Alcott", "L.M. Montgomery", "Laura Ingalls Wilder"], "Frances Hodgson Burnett"),
    ("lit_252", "Who wrote 'Little Women'?", ["Louisa May Alcott", "Frances Hodgson Burnett", "L.M. Montgomery", "Laura Ingalls Wilder"], "Louisa May Alcott"),
    ("lit_253", "Who wrote 'Anne of Green Gables'?", ["L.M. Montgomery", "Louisa May Alcott", "Frances Hodgson Burnett", "Laura Ingalls Wilder"], "L.M. Montgomery"),
    ("lit_254", "Who wrote 'Pippi Longstocking'?", ["Astrid Lindgren", "Roald Dahl", "Enid Blyton", "E.B. White"], "Astrid Lindgren"),
    ("lit_255", "Who wrote 'The Little Prince'?", ["Antoine de Saint-Exupéry", "Roald Dahl", "E.B. White", "C.S. Lewis"], "Antoine de Saint-Exupéry"),
    ("lit_256", "Who wrote 'Harriet the Spy'?", ["Louise Fitzhugh", "Beverly Cleary", "Judy Blume", "E.L. Konigsburg"], "Louise Fitzhugh"),
    ("lit_257", "Who wrote 'From the Mixed-Up Files of Mrs. Basil E. Frankweiler'?", ["E.L. Konigsburg", "Beverly Cleary", "Judy Blume", "Louise Fitzhugh"], "E.L. Konigsburg"),
]

for q in medium:
    new_questions.append({"id": q[0], "category": "Literature", "subcategory": "Children's Books", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "medium", "topic": None, "subtopic": None})

# Hard questions (16)
hard = [
    ("lit_258", "Who wrote 'The Outsiders'?", ["S.E. Hinton", "Judy Blume", "Paul Zindel", "Robert Cormier"], "S.E. Hinton"),
    ("lit_259", "Who wrote 'A Light in the Attic'?", ["Shel Silverstein", "Jack Prelutsky", "Roald Dahl", "Dr. Seuss"], "Shel Silverstein"),
    ("lit_260", "Who wrote 'The Egypt Game'?", ["Zilpha Keatley Snyder", "E.L. Konigsburg", "Beverly Cleary", "Lois Lowry"], "Zilpha Keatley Snyder"),
    ("lit_261", "Who wrote 'My Side of the Mountain'?", ["Jean Craighead George", "Gary Paulsen", "Scott O'Dell", "Wilson Rawls"], "Jean Craighead George"),
    ("lit_262", "Who wrote 'Maniac Magee'?", ["Jerry Spinelli", "Louis Sachar", "Gary Paulsen", "Paul Zindel"], "Jerry Spinelli"),
    ("lit_263", "Who wrote 'The Chocolate War'?", ["Robert Cormier", "S.E. Hinton", "Paul Zindel", "Jerry Spinelli"], "Robert Cormier"),
    ("lit_264", "Who wrote 'Roll of Thunder, Hear My Cry'?", ["Mildred D. Taylor", "Virginia Hamilton", "Katherine Paterson", "Lois Lowry"], "Mildred D. Taylor"),
    ("lit_265", "Who wrote 'The Dark Is Rising' sequence?", ["Susan Cooper", "Lloyd Alexander", "Madeleine L'Engle", "Ursula K. Le Guin"], "Susan Cooper"),
    ("lit_266", "Who wrote 'The Black Cauldron' series?", ["Lloyd Alexander", "Susan Cooper", "Patricia C. Wrede", "Robin McKinley"], "Lloyd Alexander"),
    ("lit_267", "Who wrote 'The Hero and the Crown'?", ["Robin McKinley", "Tamora Pierce", "Patricia C. Wrede", "Susan Cooper"], "Robin McKinley"),
    ("lit_268", "Who wrote 'Are You There God? It's Me, Margaret'?", ["Judy Blume", "Beverly Clearly", "Paula Danziger", "Lois Duncan"], "Judy Blume"),
    ("lit_269", "Who wrote 'The True Confessions of Charlotte Doyle'?", ["Avi", "Gary Paulsen", "Scott O'Dell", "Karen Hesse"], "Avi"),
    ("lit_270", "Who wrote 'Out of the Dust'?", ["Karen Hesse", "Sharon Creech", "Patricia MacLachlan", "Cynthia Rylant"], "Karen Hesse"),
    ("lit_271", "Who wrote 'Walk Two Moons'?", ["Sharon Creech", "Karen Hesse", "Patricia MacLachlan", "Cynthia Voigt"], "Sharon Creech"),
    ("lit_272", "Who wrote 'The Westing Game'?", ["Ellen Raskin", "E.L. Konigsburg", "Zilpha Keatley Snyder", "Natalie Babbitt"], "Ellen Raskin"),
    ("lit_273", "Who wrote 'The View from Saturday'?", ["E.L. Konigsburg", "Sharon Creech", "Karen Hesse", "Avi"], "E.L. Konigsburg"),
]

for q in hard:
    new_questions.append({"id": q[0], "category": "Literature", "subcategory": "Children's Books", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "hard", "topic": None, "subtopic": None})

# Load, add, sort, save
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

data['categories']['Literature'].extend(new_questions)
data['categories']['Literature'].sort(key=lambda q: int(q['id'].split('_')[1]))

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added 50 Children's Books questions")
print(f"Literature now has {len(data['categories']['Literature'])} total questions")
print(f"Added: 17 easy, 17 medium, 16 hard")
