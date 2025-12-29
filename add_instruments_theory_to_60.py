#!/usr/bin/env python3
"""Add 60 Instruments & Theory questions from scratch"""
import json

new_questions = []

# Easy questions (20)
easy = [
    ("mus_241", "How many strings does a standard guitar have?", ["6", "4", "5", "7"], "6"),
    ("mus_242", "What family of instruments does the violin belong to?", ["String", "Woodwind", "Brass", "Percussion"], "String"),
    ("mus_243", "How many keys are on a standard piano?", ["88", "76", "100", "61"], "88"),
    ("mus_244", "What do you call the five lines where music is written?", ["Staff or Stave", "Scale", "Chord", "Measure"], "Staff or Stave"),
    ("mus_245", "Which clef is used for higher-pitched instruments?", ["Treble clef", "Bass clef", "Alto clef", "Tenor clef"], "Treble clef"),
    ("mus_246", "How many beats are in a 4/4 time signature per measure?", ["4", "3", "2", "6"], "4"),
    ("mus_247", "What is the lowest male singing voice called?", ["Bass", "Baritone", "Tenor", "Alto"], "Bass"),
    ("mus_248", "Which family does the trumpet belong to?", ["Brass", "Woodwind", "String", "Percussion"], "Brass"),
    ("mus_249", "What are the black keys on a piano called?", ["Sharps and flats", "Naturals", "Accidentals", "Chromatics"], "Sharps and flats"),
    ("mus_250", "How many strings does a standard bass guitar have?", ["4", "5", "6", "3"], "4"),
    ("mus_251", "What is the highest female singing voice?", ["Soprano", "Alto", "Mezzo-soprano", "Contralto"], "Soprano"),
    ("mus_252", "Which percussion instrument has metal bars struck with mallets?", ["Xylophone or Glockenspiel", "Timpani", "Marimba", "Snare drum"], "Xylophone or Glockenspiel"),
    ("mus_253", "What symbol indicates to play a note louder?", ["Forte (f)", "Piano (p)", "Crescendo", "Sforzando"], "Forte (f)"),
    ("mus_254", "How many valves does a standard trumpet have?", ["3", "4", "2", "5"], "3"),
    ("mus_255", "What is a group of three notes played together called?", ["Triad or Chord", "Scale", "Arpeggio", "Harmony"], "Triad or Chord"),
    ("mus_256", "Which woodwind instrument is largest?", ["Bassoon", "Oboe", "Clarinet", "Flute"], "Bassoon"),
    ("mus_257", "What does 'piano' mean in musical dynamics?", ["Soft", "Loud", "Medium", "Very soft"], "Soft"),
    ("mus_258", "How many notes are in an octave?", ["8 (in a major scale)", "7", "12", "5"], "8 (in a major scale)"),
    ("mus_259", "What family does the saxophone belong to?", ["Woodwind", "Brass", "Percussion", "String"], "Woodwind"),
    ("mus_260", "What is the symbol that cancels a sharp or flat?", ["Natural", "Accidental", "Tie", "Slur"], "Natural"),
]

for q in easy:
    new_questions.append({"id": q[0], "category": "Music", "subcategory": "Instruments & Theory", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "easy", "topic": None, "subtopic": None})

# Medium questions (20)
medium = [
    ("mus_261", "What is the Italian term for gradually getting louder?", ["Crescendo", "Decrescendo", "Forte", "Sforzando"], "Crescendo"),
    ("mus_262", "How many semitones are in an octave?", ["12", "8", "7", "13"], "12"),
    ("mus_263", "What is the name of a chord with three notes?", ["Triad", "Tetrad", "Dyad", "Harmony"], "Triad"),
    ("mus_264", "Which instrument family does the oboe belong to?", ["Double reed woodwind", "Single reed woodwind", "Brass", "String"], "Double reed woodwind"),
    ("mus_265", "What is the term for the distance between two notes?", ["Interval", "Scale", "Chord", "Harmony"], "Interval"),
    ("mus_266", "How many strings does a standard violin have?", ["4", "5", "6", "3"], "4"),
    ("mus_267", "What is a 3/4 time signature commonly used for?", ["Waltz", "March", "Rock", "Swing"], "Waltz"),
    ("mus_268", "What does 'allegro' mean in tempo markings?", ["Fast and lively", "Slow", "Very fast", "Moderate"], "Fast and lively"),
    ("mus_269", "Which scale uses all the black keys on a piano?", ["Pentatonic scale", "Chromatic scale", "Major scale", "Minor scale"], "Pentatonic scale"),
    ("mus_270", "What is the lowest string instrument in an orchestra?", ["Double bass", "Cello", "Viola", "Bass guitar"], "Double bass"),
    ("mus_271", "What does 'staccato' mean?", ["Short and detached", "Smooth and connected", "Loud", "Soft"], "Short and detached"),
    ("mus_272", "How many lines and spaces are on a musical staff?", ["5 lines and 4 spaces", "4 lines and 5 spaces", "6 lines and 5 spaces", "5 lines and 5 spaces"], "5 lines and 4 spaces"),
    ("mus_273", "What is a series of notes played in sequence called?", ["Scale or Arpeggio", "Chord", "Harmony", "Melody"], "Scale or Arpeggio"),
    ("mus_274", "Which brass instrument has a slide instead of valves?", ["Trombone", "Trumpet", "French horn", "Tuba"], "Trombone"),
    ("mus_275", "What is the term for two half steps?", ["Whole step or Whole tone", "Semitone", "Interval", "Octave"], "Whole step or Whole tone"),
    ("mus_276", "What does 'adagio' mean in tempo?", ["Slow and stately", "Fast", "Very fast", "Moderate"], "Slow and stately"),
    ("mus_277", "How many pedals does a standard grand piano have?", ["3", "2", "4", "1"], "3"),
    ("mus_278", "What is the term for playing smoothly and connected?", ["Legato", "Staccato", "Marcato", "Tenuto"], "Legato"),
    ("mus_279", "Which woodwind instrument uses a single reed?", ["Clarinet or Saxophone", "Oboe", "Bassoon", "Flute"], "Clarinet or Saxophone"),
    ("mus_280", "What is the difference between a major and minor scale?", ["The third note (third degree)", "The fifth note", "The first note", "The seventh note"], "The third note (third degree)"),
]

for q in medium:
    new_questions.append({"id": q[0], "category": "Music", "subcategory": "Instruments & Theory", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "medium", "topic": None, "subtopic": None})

# Hard questions (20)
hard = [
    ("mus_281", "What is the interval of a perfect fifth in semitones?", ["7 semitones", "5 semitones", "8 semitones", "6 semitones"], "7 semitones"),
    ("mus_282", "Which mode is built on the first degree of the major scale?", ["Ionian", "Dorian", "Phrygian", "Lydian"], "Ionian"),
    ("mus_283", "What is a diminished seventh chord?", ["A chord with a minor third, diminished fifth, and diminished seventh", "A chord with major intervals", "A sus4 chord", "An augmented chord"], "A chord with a minor third, diminished fifth, and diminished seventh"),
    ("mus_284", "Who invented the modern piano?", ["Bartolomeo Cristofori", "Johann Sebastian Bach", "Antonio Stradivari", "Ludwig van Beethoven"], "Bartolomeo Cristofori"),
    ("mus_285", "What is the circle of fifths used for?", ["Understanding key relationships", "Tuning instruments", "Reading sheet music", "Counting beats"], "Understanding key relationships"),
    ("mus_286", "What is the Phrygian mode's characteristic?", ["Lowered second scale degree", "Raised fourth", "Lowered seventh", "Raised sixth"], "Lowered second scale degree"),
    ("mus_287", "How many positions are there on a trombone?", ["7", "5", "6", "8"], "7"),
    ("mus_288", "What is a tritone interval?", ["Augmented fourth or diminished fifth (6 semitones)", "Perfect fifth", "Major third", "Minor sixth"], "Augmented fourth or diminished fifth (6 semitones)"),
    ("mus_289", "Which family of violins were made by Antonio Stradivari?", ["Violin family (violin, viola, cello)", "Guitars", "Lutes", "Harpsichords"], "Violin family (violin, viola, cello)"),
    ("mus_290", "What is the Locrian mode built on?", ["Seventh degree of major scale", "First degree", "Fourth degree", "Fifth degree"], "Seventh degree of major scale"),
    ("mus_291", "What does a fermata symbol indicate?", ["Hold the note longer than its value", "Play softer", "Repeat", "Play staccato"], "Hold the note longer than its value"),
    ("mus_292", "What is the interval between C and F#?", ["Augmented fourth/Tritone", "Perfect fourth", "Perfect fifth", "Major third"], "Augmented fourth/Tritone"),
    ("mus_293", "Which temperament system divides the octave into 12 equal parts?", ["Equal temperament", "Just intonation", "Pythagorean tuning", "Meantone temperament"], "Equal temperament"),
    ("mus_294", "What is the dominant seventh chord in the key of C major?", ["G7", "C7", "F7", "D7"], "G7"),
    ("mus_295", "What technique involves playing notes of a chord in sequence?", ["Arpeggio", "Glissando", "Tremolo", "Vibrato"], "Arpeggio"),
    ("mus_296", "What is the enharmonic equivalent of C#?", ["Db", "D", "B", "C"], "Db"),
    ("mus_297", "Which interval is considered the most consonant?", ["Perfect fifth or octave", "Minor second", "Tritone", "Major seventh"], "Perfect fifth or octave"),
    ("mus_298", "What is a cadenza in classical music?", ["A virtuosic solo passage", "A chord progression", "A type of scale", "A dance form"], "A virtuosic solo passage"),
    ("mus_299", "What is the Mixolydian mode's characteristic?", ["Lowered seventh scale degree", "Raised fourth", "Lowered third", "Raised sixth"], "Lowered seventh scale degree"),
    ("mus_300", "What is the term for the simultaneous sounding of two or more independent melodic lines?", ["Counterpoint or Polyphony", "Harmony", "Monophony", "Homophony"], "Counterpoint or Polyphony"),
]

for q in hard:
    new_questions.append({"id": q[0], "category": "Music", "subcategory": "Instruments & Theory", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "hard", "topic": None, "subtopic": None})

# Load, add, sort, save
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

data['categories']['Music'].extend(new_questions)
data['categories']['Music'].sort(key=lambda q: int(q['id'].split('_')[1]))

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added 60 Instruments & Theory questions")
print(f"Music now has {len(data['categories']['Music'])} total questions")
print(f"Added: 20 easy, 20 medium, 20 hard")
