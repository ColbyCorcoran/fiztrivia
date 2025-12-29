#!/usr/bin/env python3
"""Add 39 Music in Film & TV questions to reach 60 total"""
import json

# 39 new Music in Film & TV questions (13 easy, 13 medium, 13 hard)
new_questions = [
    # EASY (13 questions)
    {
        "id": "mus_022",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "What song does Celine Dion sing in Titanic?",
        "options": ["My Heart Will Go On", "Because You Loved Me", "The Power of Love", "All By Myself"],
        "correct_answer": "My Heart Will Go On",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_023",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Which band performed 'Eye of the Tiger' from Rocky III?",
        "options": ["Survivor", "Journey", "Foreigner", "Boston"],
        "correct_answer": "Survivor",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_024",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who sang 'I Will Always Love You' in The Bodyguard?",
        "options": ["Whitney Houston", "Mariah Carey", "Celine Dion", "Diana Ross"],
        "correct_answer": "Whitney Houston",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_025",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "What TV show features the theme song 'I'll Be There for You'?",
        "options": ["Friends", "Seinfeld", "How I Met Your Mother", "The Big Bang Theory"],
        "correct_answer": "Friends",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_026",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who sang 'Let It Go' from Frozen?",
        "options": ["Idina Menzel", "Kristen Bell", "Demi Lovato", "Lea Michele"],
        "correct_answer": "Idina Menzel",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_027",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "What is the theme song of The Fresh Prince of Bel-Air?",
        "options": ["The Fresh Prince of Bel-Air theme", "Getting Jiggy wit It", "Summertime", "Men in Black"],
        "correct_answer": "The Fresh Prince of Bel-Air theme",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_028",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who performed 'Shallow' in A Star Is Born?",
        "options": ["Lady Gaga and Bradley Cooper", "Adele", "Taylor Swift", "Beyoncé"],
        "correct_answer": "Lady Gaga and Bradley Cooper",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_029",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "What song plays during the pottery scene in Ghost?",
        "options": ["Unchained Melody", "My Heart Will Go On", "I Will Always Love You", "The Power of Love"],
        "correct_answer": "Unchained Melody",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_030",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who sang the theme song for Skyfall?",
        "options": ["Adele", "Sam Smith", "Billie Eilish", "Alicia Keys"],
        "correct_answer": "Adele",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_031",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "What song does Elton John perform in The Lion King?",
        "options": ["Can You Feel the Love Tonight", "Your Song", "Rocket Man", "Tiny Dancer"],
        "correct_answer": "Can You Feel the Love Tonight",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_032",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who performed '(I've Had) The Time of My Life' from Dirty Dancing?",
        "options": ["Bill Medley and Jennifer Warnes", "Patrick Swayze and Jennifer Grey", "Lionel Richie and Diana Ross", "Kenny Loggins"],
        "correct_answer": "Bill Medley and Jennifer Warnes",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_033",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "What TV show features the Rembrandts' 'I'll Be There for You'?",
        "options": ["Friends", "Seinfeld", "Frasier", "Cheers"],
        "correct_answer": "Friends",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_034",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who composed the theme for Game of Thrones?",
        "options": ["Ramin Djawadi", "Bear McCreary", "Hans Zimmer", "Howard Shore"],
        "correct_answer": "Ramin Djawadi",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    },

    # MEDIUM (13 questions)
    {
        "id": "mus_035",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who composed the score for Schindler's List?",
        "options": ["John Williams", "Hans Zimmer", "Ennio Morricone", "Alexandre Desplat"],
        "correct_answer": "John Williams",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_036",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "What is the name of the theme song from Cheers?",
        "options": ["Where Everybody Knows Your Name", "Making Your Way", "Boston Blues", "Friendly Faces"],
        "correct_answer": "Where Everybody Knows Your Name",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_037",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who composed the music for Interstellar?",
        "options": ["Hans Zimmer", "John Williams", "Thomas Newman", "James Newton Howard"],
        "correct_answer": "Hans Zimmer",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_038",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Which composer scored the Harry Potter films?",
        "options": ["John Williams (first three), then others", "Hans Zimmer", "Howard Shore", "James Horner"],
        "correct_answer": "John Williams (first three), then others",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_039",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who wrote the score for The Social Network?",
        "options": ["Trent Reznor and Atticus Ross", "Hans Zimmer", "Alexandre Desplat", "Thomas Newman"],
        "correct_answer": "Trent Reznor and Atticus Ross",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_040",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "What song won an Oscar for Best Original Song from 8 Mile?",
        "options": ["Lose Yourself", "Till I Collapse", "Without Me", "The Real Slim Shady"],
        "correct_answer": "Lose Yourself",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_041",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who composed the music for The Godfather?",
        "options": ["Nino Rota", "Ennio Morricone", "John Williams", "Bernard Herrmann"],
        "correct_answer": "Nino Rota",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_042",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Which TV show features 'Woke Up This Morning' by Alabama 3?",
        "options": ["The Sopranos", "Breaking Bad", "The Wire", "Mad Men"],
        "correct_answer": "The Sopranos",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_043",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who composed the memorable score for Psycho?",
        "options": ["Bernard Herrmann", "Alfred Newman", "Franz Waxman", "Miklós Rózsa"],
        "correct_answer": "Bernard Herrmann",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_044",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "What TV show uses Gary Portnoy's 'Where Everybody Knows Your Name'?",
        "options": ["Cheers", "Frasier", "Wings", "The Norm Show"],
        "correct_answer": "Cheers",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_045",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who composed the music for Pirates of the Caribbean?",
        "options": ["Hans Zimmer and Klaus Badelt", "John Williams", "James Newton Howard", "Danny Elfman"],
        "correct_answer": "Hans Zimmer and Klaus Badelt",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_046",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "What is the theme song of M*A*S*H called?",
        "options": ["Suicide Is Painless", "Goodbye Farewell and Amen", "War and Peace", "Korean Blues"],
        "correct_answer": "Suicide Is Painless",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_047",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who composed the score for The Mission?",
        "options": ["Ennio Morricone", "John Williams", "Hans Zimmer", "Gabriel Yared"],
        "correct_answer": "Ennio Morricone",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },

    # HARD (13 questions)
    {
        "id": "mus_048",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who composed the distinctive score for The Good, the Bad and the Ugly?",
        "options": ["Ennio Morricone", "Nino Rota", "Dmitri Tiomkin", "Elmer Bernstein"],
        "correct_answer": "Ennio Morricone",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_049",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who composed the music for Blade Runner?",
        "options": ["Vangelis", "Jean-Michel Jarre", "Tangerine Dream", "Klaus Schulze"],
        "correct_answer": "Vangelis",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_050",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Which composer wrote the score for Lawrence of Arabia?",
        "options": ["Maurice Jarre", "Dimitri Tiomkin", "Miklós Rózsa", "Bernard Herrmann"],
        "correct_answer": "Maurice Jarre",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_051",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who composed the jazz-influenced score for Anatomy of a Murder?",
        "options": ["Duke Ellington", "Miles Davis", "Dave Brubeck", "John Coltrane"],
        "correct_answer": "Duke Ellington",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_052",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who wrote the electronic score for Tron (1982)?",
        "options": ["Wendy Carlos", "Vangelis", "Giorgio Moroder", "Jean-Michel Jarre"],
        "correct_answer": "Wendy Carlos",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_053",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who composed the minimalist score for The Hours?",
        "options": ["Philip Glass", "Steve Reich", "Michael Nyman", "Arvo Pärt"],
        "correct_answer": "Philip Glass",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_054",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Which composer scored There Will Be Blood?",
        "options": ["Jonny Greenwood", "Thom Yorke", "Trent Reznor", "Nick Cave"],
        "correct_answer": "Jonny Greenwood",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_055",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who composed the music for Vertigo?",
        "options": ["Bernard Herrmann", "Alfred Newman", "Franz Waxman", "Miklós Rózsa"],
        "correct_answer": "Bernard Herrmann",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_056",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who wrote the score for Brokeback Mountain?",
        "options": ["Gustavo Santaolalla", "Alexandre Desplat", "Thomas Newman", "Carter Burwell"],
        "correct_answer": "Gustavo Santaolalla",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_057",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who composed the avant-garde score for Under the Skin?",
        "options": ["Mica Levi", "Jóhann Jóhannsson", "Ben Salisbury", "Geoff Barrow"],
        "correct_answer": "Mica Levi",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_058",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who composed the score for The Last Emperor?",
        "options": ["Ryuichi Sakamoto, David Byrne, and Cong Su", "Tan Dun", "Toru Takemitsu", "Joe Hisaishi"],
        "correct_answer": "Ryuichi Sakamoto, David Byrne, and Cong Su",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_059",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "What is the name of the Coen Brothers' composer who scored Fargo and No Country for Old Men?",
        "options": ["Carter Burwell", "Thomas Newman", "Alexandre Desplat", "Howard Shore"],
        "correct_answer": "Carter Burwell",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    },
    {
        "id": "mus_060",
        "category": "Music",
        "subcategory": "Music in Film & TV",
        "question": "Who composed the haunting score for The Shining?",
        "options": ["Wendy Carlos and Rachel Elkind (adapted classical)", "Bernard Herrmann", "Jerry Goldsmith", "John Carpenter"],
        "correct_answer": "Wendy Carlos and Rachel Elkind (adapted classical)",
        "difficulty": "hard",
        "topic": None,
        "subtopic": None
    }
]

# Load existing data
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Add new questions
data['categories']['Music'].extend(new_questions)

# Sort by ID to maintain order
data['categories']['Music'].sort(key=lambda q: int(q['id'].split('_')[1]))

# Save back
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Added 39 Music in Film & TV questions")
print(f"Music now has {len(data['categories']['Music'])} total questions")

# Count Music in Film & TV
film_tv = [q for q in data['categories']['Music'] if q['subcategory'] == 'Music in Film & TV']
print(f"Music in Film & TV: {len(film_tv)} questions")

# Count by difficulty
easy = len([q for q in new_questions if q['difficulty'] == 'easy'])
medium = len([q for q in new_questions if q['difficulty'] == 'medium'])
hard = len([q for q in new_questions if q['difficulty'] == 'hard'])
print(f"Added: {easy} easy, {medium} medium, {hard} hard")
