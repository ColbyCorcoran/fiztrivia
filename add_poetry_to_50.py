#!/usr/bin/env python3
"""Add 50 Poetry questions from scratch"""
import json

new_questions = []

# Easy questions (17)
easy = [
    ("lit_174", "Who wrote 'The Raven'?", ["Edgar Allan Poe", "Robert Frost", "Emily Dickinson", "Walt Whitman"], "Edgar Allan Poe"),
    ("lit_175", "Who wrote 'The Road Not Taken'?", ["Robert Frost", "Carl Sandburg", "Langston Hughes", "E.E. Cummings"], "Robert Frost"),
    ("lit_176", "How many lines are in a sonnet?", ["14", "10", "12", "16"], "14"),
    ("lit_177", "Who wrote 'I Wandered Lonely as a Cloud' (Daffodils)?", ["William Wordsworth", "Samuel Taylor Coleridge", "Lord Byron", "Percy Shelley"], "William Wordsworth"),
    ("lit_178", "What is a haiku?", ["A three-line Japanese poem", "A four-line poem", "A narrative poem", "An epic poem"], "A three-line Japanese poem"),
    ("lit_179", "Who wrote 'Leaves of Grass'?", ["Walt Whitman", "Emily Dickinson", "Henry Wadsworth Longfellow", "Edgar Allan Poe"], "Walt Whitman"),
    ("lit_180", "What is a limerick?", ["A five-line humorous poem", "A fourteen-line poem", "A three-line poem", "An epic poem"], "A five-line humorous poem"),
    ("lit_181", "Who wrote 'Howl'?", ["Allen Ginsberg", "Jack Kerouac", "Lawrence Ferlinghetti", "Gregory Corso"], "Allen Ginsberg"),
    ("lit_182", "Who is known as the national poet of Scotland?", ["Robert Burns", "Sir Walter Scott", "Robert Louis Stevenson", "Hugh MacDiarmid"], "Robert Burns"),
    ("lit_183", "Who wrote 'The Waste Land'?", ["T.S. Eliot", "Ezra Pound", "W.H. Auden", "Wallace Stevens"], "T.S. Eliot"),
    ("lit_184", "What is blank verse?", ["Unrhymed iambic pentameter", "Free verse", "Rhymed couplets", "Sonnets"], "Unrhymed iambic pentameter"),
    ("lit_185", "Who wrote 'Do Not Go Gentle into That Good Night'?", ["Dylan Thomas", "W.H. Auden", "Ted Hughes", "Philip Larkin"], "Dylan Thomas"),
    ("lit_186", "How many syllables are in a traditional haiku?", ["17 (5-7-5)", "15", "12", "21"], "17 (5-7-5)"),
    ("lit_187", "Who wrote 'If—'?", ["Rudyard Kipling", "Robert Frost", "W.B. Yeats", "T.S. Eliot"], "Rudyard Kipling"),
    ("lit_188", "What is free verse?", ["Poetry without regular meter or rhyme", "Rhyming poetry", "Sonnets", "Haiku"], "Poetry without regular meter or rhyme"),
    ("lit_189", "Who wrote 'The Love Song of J. Alfred Prufrock'?", ["T.S. Eliot", "Ezra Pound", "W.H. Auden", "Robert Frost"], "T.S. Eliot"),
    ("lit_190", "What is an epic poem?", ["A long narrative poem", "A short lyric poem", "A humorous poem", "A love poem"], "A long narrative poem"),
]

for q in easy:
    new_questions.append({"id": q[0], "category": "Literature", "subcategory": "Poetry", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "easy", "topic": None, "subtopic": None})

# Medium questions (17)
medium = [
    ("lit_191", "Who wrote 'Ode to a Nightingale'?", ["John Keats", "Percy Shelley", "Lord Byron", "William Wordsworth"], "John Keats"),
    ("lit_192", "Who wrote 'Paradise Lost' in blank verse?", ["John Milton", "William Blake", "Alexander Pope", "John Donne"], "John Milton"),
    ("lit_193", "Who wrote 'The Rime of the Ancient Mariner'?", ["Samuel Taylor Coleridge", "William Wordsworth", "Robert Southey", "Lord Byron"], "Samuel Taylor Coleridge"),
    ("lit_194", "What is a villanelle?", ["A 19-line poem with specific rhyme scheme", "A sonnet variation", "A Japanese poem form", "A four-line stanza"], "A 19-line poem with specific rhyme scheme"),
    ("lit_195", "Who wrote 'Ozymandias'?", ["Percy Bysshe Shelley", "John Keats", "Lord Byron", "William Wordsworth"], "Percy Bysshe Shelley"),
    ("lit_196", "Who wrote 'The Second Coming'?", ["W.B. Yeats", "T.S. Eliot", "Ezra Pound", "W.H. Auden"], "W.B. Yeats"),
    ("lit_197", "What is iambic pentameter?", ["Five iambs (unstressed-stressed) per line", "Five stressed syllables", "Ten syllables with no pattern", "Four beats per line"], "Five iambs (unstressed-stressed) per line"),
    ("lit_198", "Who wrote 'Kubla Khan'?", ["Samuel Taylor Coleridge", "William Wordsworth", "John Keats", "Percy Shelley"], "Samuel Taylor Coleridge"),
    ("lit_199", "Who wrote 'Annabel Lee'?", ["Edgar Allan Poe", "Emily Dickinson", "Walt Whitman", "Henry Wadsworth Longfellow"], "Edgar Allan Poe"),
    ("lit_200", "What is a sestina?", ["A 39-line poem with six-line stanzas", "A fourteen-line poem", "A narrative poem", "A Japanese poem"], "A 39-line poem with six-line stanzas"),
    ("lit_201", "Who wrote 'The Hollow Men'?", ["T.S. Eliot", "Ezra Pound", "W.H. Auden", "Wallace Stevens"], "T.S. Eliot"),
    ("lit_202", "Who wrote 'Invictus'?", ["William Ernest Henley", "Rudyard Kipling", "Alfred Lord Tennyson", "Robert Browning"], "William Ernest Henley"),
    ("lit_203", "What is an ode?", ["A lyric poem addressing a subject", "A humorous poem", "A narrative poem", "A Japanese poem"], "A lyric poem addressing a subject"),
    ("lit_204", "Who wrote 'Stopping by Woods on a Snowy Evening'?", ["Robert Frost", "Carl Sandburg", "Wallace Stevens", "E.E. Cummings"], "Robert Frost"),
    ("lit_205", "Who wrote 'The Charge of the Light Brigade'?", ["Alfred Lord Tennyson", "Robert Browning", "Matthew Arnold", "Gerard Manley Hopkins"], "Alfred Lord Tennyson"),
    ("lit_206", "What is alliteration?", ["Repetition of initial consonant sounds", "Repetition of vowel sounds", "Rhyming words", "Meter pattern"], "Repetition of initial consonant sounds"),
    ("lit_207", "Who wrote 'Funeral Blues' (Stop All the Clocks)?", ["W.H. Auden", "T.S. Eliot", "Dylan Thomas", "Philip Larkin"], "W.H. Auden"),
]

for q in medium:
    new_questions.append({"id": q[0], "category": "Literature", "subcategory": "Poetry", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "medium", "topic": None, "subtopic": None})

# Hard questions (16)
hard = [
    ("lit_208", "Who wrote 'The Cantos'?", ["Ezra Pound", "T.S. Eliot", "Wallace Stevens", "Hart Crane"], "Ezra Pound"),
    ("lit_209", "Who wrote 'The Bridge'?", ["Hart Crane", "Wallace Stevens", "William Carlos Williams", "Ezra Pound"], "Hart Crane"),
    ("lit_210", "Who wrote 'Paterson'?", ["William Carlos Williams", "Wallace Stevens", "Hart Crane", "Marianne Moore"], "William Carlos Williams"),
    ("lit_211", "Who wrote 'The Dream Songs'?", ["John Berryman", "Robert Lowell", "Sylvia Plath", "Anne Sexton"], "John Berryman"),
    ("lit_212", "Who wrote 'Ariel'?", ["Sylvia Plath", "Anne Sexton", "Adrienne Rich", "Elizabeth Bishop"], "Sylvia Plath"),
    ("lit_213", "Who wrote 'Life Studies'?", ["Robert Lowell", "John Berryman", "Theodore Roethke", "Delmore Schwartz"], "Robert Lowell"),
    ("lit_214", "Who wrote 'The Duino Elegies'?", ["Rainer Maria Rilke", "Paul Celan", "Georg Trakl", "Stefan George"], "Rainer Maria Rilke"),
    ("lit_215", "Who wrote 'The Four Quartets'?", ["T.S. Eliot", "Ezra Pound", "W.H. Auden", "Wallace Stevens"], "T.S. Eliot"),
    ("lit_216", "Who wrote 'Harmonium'?", ["Wallace Stevens", "Hart Crane", "William Carlos Williams", "Ezra Pound"], "Wallace Stevens"),
    ("lit_217", "Who wrote 'North'?", ["Seamus Heaney", "Ted Hughes", "Philip Larkin", "Thom Gunn"], "Seamus Heaney"),
    ("lit_218", "Who wrote 'The Whitsun Weddings'?", ["Philip Larkin", "Ted Hughes", "Thom Gunn", "Seamus Heaney"], "Philip Larkin"),
    ("lit_219", "Who wrote 'Crow'?", ["Ted Hughes", "Seamus Heaney", "Philip Larkin", "Geoffrey Hill"], "Ted Hughes"),
    ("lit_220", "Who wrote 'The Wild Iris'?", ["Louise Glück", "Jorie Graham", "Rita Dove", "Sharon Olds"], "Louise Glück"),
    ("lit_221", "Who wrote 'The Collected Poems' and won the Nobel Prize in 1995?", ["Seamus Heaney", "Derek Walcott", "Joseph Brodsky", "Wisława Szymborska"], "Seamus Heaney"),
    ("lit_222", "Who wrote 'Omeros'?", ["Derek Walcott", "Seamus Heaney", "V.S. Naipaul", "Kamau Brathwaite"], "Derek Walcott"),
    ("lit_223", "Who wrote 'The Changing Light at Sandover'?", ["James Merrill", "John Ashbery", "A.R. Ammons", "Mark Strand"], "James Merrill"),
]

for q in hard:
    new_questions.append({"id": q[0], "category": "Literature", "subcategory": "Poetry", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "hard", "topic": None, "subtopic": None})

# Load, add, sort, save
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

data['categories']['Literature'].extend(new_questions)
data['categories']['Literature'].sort(key=lambda q: int(q['id'].split('_')[1]))

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added 50 Poetry questions")
print(f"Literature now has {len(data['categories']['Literature'])} total questions")
print(f"Added: 17 easy, 17 medium, 16 hard")
