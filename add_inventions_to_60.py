#!/usr/bin/env python3
"""Add 60 Inventions questions from scratch"""
import json

new_questions = []

# Easy questions (20)
easy = [
    ("tec_264", "Who is credited with inventing the light bulb?", ["Thomas Edison", "Nikola Tesla", "Benjamin Franklin", "Alexander Graham Bell"], "Thomas Edison"),
    ("tec_265", "Who invented the telephone?", ["Alexander Graham Bell", "Thomas Edison", "Guglielmo Marconi", "Samuel Morse"], "Alexander Graham Bell"),
    ("tec_266", "Who invented the printing press?", ["Johannes Gutenberg", "Benjamin Franklin", "William Caxton", "Johann Fust"], "Johannes Gutenberg"),
    ("tec_267", "Who is credited with inventing the World Wide Web?", ["Tim Berners-Lee", "Bill Gates", "Steve Jobs", "Vint Cerf"], "Tim Berners-Lee"),
    ("tec_268", "Who invented the airplane?", ["Wright Brothers", "Charles Lindbergh", "Amelia Earhart", "Leonardo da Vinci"], "Wright Brothers"),
    ("tec_269", "Who invented the steam engine (improved version)?", ["James Watt", "George Stephenson", "Robert Fulton", "Thomas Newcomen"], "James Watt"),
    ("tec_270", "Who invented the theory of evolution by natural selection?", ["Charles Darwin", "Gregor Mendel", "Louis Pasteur", "Alfred Wallace"], "Charles Darwin"),
    ("tec_271", "Who invented the telegraph?", ["Samuel Morse", "Alexander Graham Bell", "Thomas Edison", "Nikola Tesla"], "Samuel Morse"),
    ("tec_272", "Who invented the radio?", ["Guglielmo Marconi", "Nikola Tesla", "Heinrich Hertz", "Lee de Forest"], "Guglielmo Marconi"),
    ("tec_273", "Who discovered penicillin?", ["Alexander Fleming", "Louis Pasteur", "Jonas Salk", "Edward Jenner"], "Alexander Fleming"),
    ("tec_274", "Who invented the automobile (first practical car)?", ["Karl Benz", "Henry Ford", "Gottlieb Daimler", "Rudolf Diesel"], "Karl Benz"),
    ("tec_275", "Who invented dynamite?", ["Alfred Nobel", "Albert Einstein", "Marie Curie", "Dmitri Mendeleev"], "Alfred Nobel"),
    ("tec_276", "Who invented the phonograph?", ["Thomas Edison", "Alexander Graham Bell", "Emile Berliner", "Guglielmo Marconi"], "Thomas Edison"),
    ("tec_277", "Who invented the first successful vaccine (smallpox)?", ["Edward Jenner", "Louis Pasteur", "Jonas Salk", "Alexander Fleming"], "Edward Jenner"),
    ("tec_278", "Who invented the mechanical television?", ["John Logie Baird", "Philo Farnsworth", "Vladimir Zworykin", "Charles Jenkins"], "John Logie Baird"),
    ("tec_279", "Who invented the safety elevator?", ["Elisha Otis", "Alexander Miles", "Werner von Siemens", "Frank Sprague"], "Elisha Otis"),
    ("tec_280", "Who invented the cotton gin?", ["Eli Whitney", "Cyrus McCormick", "John Deere", "James Hargreaves"], "Eli Whitney"),
    ("tec_281", "Who invented vulcanized rubber?", ["Charles Goodyear", "John Dunlop", "Benjamin Franklin", "Thomas Hancock"], "Charles Goodyear"),
    ("tec_282", "Who invented the sewing machine?", ["Elias Howe", "Isaac Singer", "Barthélemy Thimonnier", "Walter Hunt"], "Elias Howe"),
    ("tec_283", "Who invented the Kodak camera?", ["George Eastman", "Louis Daguerre", "Joseph Niepce", "William Fox"], "George Eastman"),
]

for q in easy:
    new_questions.append({"id": q[0], "category": "Technology", "subcategory": "Inventions", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "easy", "topic": None, "subtopic": None})

# Medium questions (20)
medium = [
    ("tec_284", "What year was the first airplane flight by the Wright Brothers?", ["1903", "1900", "1905", "1910"], "1903"),
    ("tec_285", "Who invented the transistor?", ["Bardeen, Brattain, and Shockley", "Jack Kilby", "Robert Noyce", "Gordon Moore"], "Bardeen, Brattain, and Shockley"),
    ("tec_286", "Who invented the microwave oven?", ["Percy Spencer", "John Gorrie", "Willis Carrier", "Clarence Birdseye"], "Percy Spencer"),
    ("tec_287", "What year was the first commercial computer UNIVAC introduced?", ["1951", "1946", "1955", "1960"], "1951"),
    ("tec_288", "Who invented the first electronic computer ENIAC?", ["Eckert and Mauchly", "Alan Turing", "John von Neumann", "Konrad Zuse"], "Eckert and Mauchly"),
    ("tec_289", "Who invented the integrated circuit (microchip)?", ["Jack Kilby and Robert Noyce", "Gordon Moore", "William Shockley", "John Bardeen"], "Jack Kilby and Robert Noyce"),
    ("tec_290", "What year was the first telephone patent filed?", ["1876", "1875", "1880", "1870"], "1876"),
    ("tec_291", "Who invented the battery (voltaic pile)?", ["Alessandro Volta", "Benjamin Franklin", "Michael Faraday", "Luigi Galvani"], "Alessandro Volta"),
    ("tec_292", "Who invented the diesel engine?", ["Rudolf Diesel", "Karl Benz", "Gottlieb Daimler", "Nicolaus Otto"], "Rudolf Diesel"),
    ("tec_293", "Who invented the laser?", ["Theodore Maiman", "Charles Townes", "Arthur Schawlow", "Gordon Gould"], "Theodore Maiman"),
    ("tec_294", "What year did Alexander Fleming discover penicillin?", ["1928", "1920", "1935", "1945"], "1928"),
    ("tec_295", "Who invented the first practical refrigerator?", ["Jacob Perkins", "John Gorrie", "Carl von Linde", "Willis Carrier"], "Jacob Perkins"),
    ("tec_296", "Who invented the barcode?", ["Norman Woodland and Bernard Silver", "George Laurer", "David Collins", "Alan Haberman"], "Norman Woodland and Bernard Silver"),
    ("tec_297", "Who invented the X-ray machine?", ["Wilhelm Röntgen", "Marie Curie", "Henri Becquerel", "Ernest Rutherford"], "Wilhelm Röntgen"),
    ("tec_298", "What year was the first successful airplane flight?", ["1903", "1900", "1905", "1910"], "1903"),
    ("tec_299", "Who invented the pneumatic tire?", ["John Dunlop", "Charles Goodyear", "Robert Thomson", "André Michelin"], "John Dunlop"),
    ("tec_300", "Who invented the Polaroid camera?", ["Edwin Land", "George Eastman", "Louis Daguerre", "Harold Edgerton"], "Edwin Land"),
    ("tec_301", "Who invented the jet engine?", ["Frank Whittle and Hans von Ohain", "Igor Sikorsky", "Charles Lindbergh", "Wernher von Braun"], "Frank Whittle and Hans von Ohain"),
    ("tec_302", "Who invented the ballpoint pen?", ["László Bíró", "Lewis Waterman", "George Parker", "John Loud"], "László Bíró"),
    ("tec_303", "Who invented the incandescent light bulb (commercial version)?", ["Thomas Edison", "Joseph Swan", "Humphry Davy", "Warren de la Rue"], "Thomas Edison"),
]

for q in medium:
    new_questions.append({"id": q[0], "category": "Technology", "subcategory": "Inventions", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "medium", "topic": None, "subtopic": None})

# Hard questions (20)
hard = [
    ("tec_304", "Who invented the first mechanical computer (Analytical Engine)?", ["Charles Babbage", "Ada Lovelace", "Alan Turing", "John von Neumann"], "Charles Babbage"),
    ("tec_305", "What year was the transistor invented at Bell Labs?", ["1947", "1945", "1950", "1952"], "1947"),
    ("tec_306", "Who invented the hovercraft?", ["Christopher Cockerell", "Igor Sikorsky", "Howard Hughes", "Barnes Wallis"], "Christopher Cockerell"),
    ("tec_307", "Who invented the first programmable computer (Z3)?", ["Konrad Zuse", "Alan Turing", "John von Neumann", "Claude Shannon"], "Konrad Zuse"),
    ("tec_308", "What year was the integrated circuit patented?", ["1959", "1955", "1960", "1965"], "1959"),
    ("tec_309", "Who invented the electron microscope?", ["Ernst Ruska and Max Knoll", "Wilhelm Röntgen", "Robert Hooke", "Antonie van Leeuwenhoek"], "Ernst Ruska and Max Knoll"),
    ("tec_310", "Who invented the polio vaccine?", ["Jonas Salk", "Albert Sabin", "Edward Jenner", "Louis Pasteur"], "Jonas Salk"),
    ("tec_311", "What year was the World Wide Web invented?", ["1989", "1991", "1985", "1993"], "1989"),
    ("tec_312", "Who invented the television (electronic version)?", ["Philo Farnsworth", "John Logie Baird", "Vladimir Zworykin", "Charles Jenkins"], "Philo Farnsworth"),
    ("tec_313", "Who invented the cyclotron particle accelerator?", ["Ernest Lawrence", "Robert Oppenheimer", "Enrico Fermi", "J. Robert Van de Graaff"], "Ernest Lawrence"),
    ("tec_314", "Who invented the Turing machine concept?", ["Alan Turing", "John von Neumann", "Claude Shannon", "Alonzo Church"], "Alan Turing"),
    ("tec_315", "What year did the first satellite Sputnik launch?", ["1957", "1955", "1960", "1961"], "1957"),
    ("tec_316", "Who invented the first successful helicopter?", ["Igor Sikorsky", "Paul Cornu", "Louis Breguet", "Juan de la Cierva"], "Igor Sikorsky"),
    ("tec_317", "Who invented the scanning tunneling microscope?", ["Gerd Binnig and Heinrich Rohrer", "Ernst Ruska", "Richard Feynman", "Max Knoll"], "Gerd Binnig and Heinrich Rohrer"),
    ("tec_318", "What year was the first heart transplant performed?", ["1967", "1965", "1970", "1972"], "1967"),
    ("tec_319", "Who invented the first programmable loom (Jacquard loom)?", ["Joseph Marie Jacquard", "Eli Whitney", "James Hargreaves", "Samuel Crompton"], "Joseph Marie Jacquard"),
    ("tec_320", "Who invented fiber optics for telecommunications?", ["Charles Kao", "Theodore Maiman", "Gordon Gould", "Robert Noyce"], "Charles Kao"),
    ("tec_321", "What year was the first synthetic plastic (Bakelite) created?", ["1907", "1900", "1910", "1920"], "1907"),
    ("tec_322", "Who invented the MRI scanner?", ["Raymond Damadian", "Paul Lauterbur", "Peter Mansfield", "Felix Bloch"], "Raymond Damadian"),
    ("tec_323", "Who invented the first practical typewriter?", ["Christopher Latham Sholes", "Charles Thurber", "Pellegrino Turri", "William Burt"], "Christopher Latham Sholes"),
]

for q in hard:
    new_questions.append({"id": q[0], "category": "Technology", "subcategory": "Inventions", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "hard", "topic": None, "subtopic": None})

# Load, add, sort, save
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

data['categories']['Technology'].extend(new_questions)
data['categories']['Technology'].sort(key=lambda q: int(q['id'].split('_')[1]))

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added 60 Inventions questions")
print(f"Technology now has {len(data['categories']['Technology'])} total questions")
print(f"Added: 20 easy, 20 medium, 20 hard")
