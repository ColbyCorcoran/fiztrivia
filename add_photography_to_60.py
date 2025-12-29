#!/usr/bin/env python3
"""Add 60 Photography questions from scratch"""
import json

new_questions = []

# Easy questions (20)
easy = [
    ("art_241", "What does 'SLR' stand for in cameras?", ["Single-Lens Reflex", "Standard Light Recorder", "Simple Lens Reflector", "Special Light Refractor"], "Single-Lens Reflex"),
    ("art_242", "What does 'ISO' measure in photography?", ["Light sensitivity", "Shutter speed", "Aperture size", "Focal length"], "Light sensitivity"),
    ("art_243", "What is the opening that controls light in a camera called?", ["Aperture", "Shutter", "Lens", "Sensor"], "Aperture"),
    ("art_244", "Who invented the first practical photographic process?", ["Louis Daguerre", "William Fox Talbot", "Nicéphore Niépce", "George Eastman"], "Louis Daguerre"),
    ("art_245", "What does 'f-stop' refer to?", ["Aperture size", "Shutter speed", "ISO setting", "White balance"], "Aperture size"),
    ("art_246", "What type of photography captures very small subjects up close?", ["Macro photography", "Landscape photography", "Portrait photography", "Street photography"], "Macro photography"),
    ("art_247", "What famous photograph shows a sailor kissing a nurse in Times Square?", ["V-J Day in Times Square", "Migrant Mother", "Afghan Girl", "Tank Man"], "V-J Day in Times Square"),
    ("art_248", "What does 'DSLR' stand for?", ["Digital Single-Lens Reflex", "Digital Standard Light Recorder", "Direct Single-Lens Reflector", "Digital Simple Lens Refractor"], "Digital Single-Lens Reflex"),
    ("art_249", "Who photographed 'Migrant Mother'?", ["Dorothea Lange", "Walker Evans", "Margaret Bourke-White", "Gordon Parks"], "Dorothea Lange"),
    ("art_250", "What is the rule that divides a frame into nine parts?", ["Rule of thirds", "Golden ratio", "Rule of fifths", "Symmetry rule"], "Rule of thirds"),
    ("art_251", "What type of lens makes objects appear closer?", ["Telephoto lens", "Wide-angle lens", "Fish-eye lens", "Macro lens"], "Telephoto lens"),
    ("art_252", "Who photographed 'Afghan Girl' for National Geographic?", ["Steve McCurry", "Annie Leibovitz", "Sebastião Salgado", "James Nachtwey"], "Steve McCurry"),
    ("art_253", "What does RAW format preserve in digital photography?", ["All original data without compression", "Compressed image data", "Only color information", "Only brightness data"], "All original data without compression"),
    ("art_254", "What is the art of taking self-portraits called?", ["Self-portraiture/Selfie", "Auto-photography", "Mirror photography", "Solo imaging"], "Self-portraiture/Selfie"),
    ("art_255", "Who founded Magnum Photos agency?", ["Robert Capa and others", "Henri Cartier-Bresson alone", "Steve McCurry", "Sebastião Salgado"], "Robert Capa and others"),
    ("art_256", "What company created the first mass-market camera?", ["Kodak", "Canon", "Nikon", "Leica"], "Kodak"),
    ("art_257", "What is the speed at which the shutter opens and closes called?", ["Shutter speed", "Aperture", "ISO", "Exposure"], "Shutter speed"),
    ("art_258", "What type of photography captures celestial objects?", ["Astrophotography", "Aerial photography", "Underwater photography", "Night photography"], "Astrophotography"),
    ("art_259", "Who is known for black and white landscape photography of Yosemite?", ["Ansel Adams", "Edward Weston", "Minor White", "Paul Strand"], "Ansel Adams"),
    ("art_260", "What is the term for blurry background in photos?", ["Bokeh", "Vignette", "Grain", "Noise"], "Bokeh"),
]

for q in easy:
    new_questions.append({"id": q[0], "category": "Art", "subcategory": "Photography", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "easy", "topic": None, "subtopic": None})

# Medium questions (20)
medium = [
    ("art_261", "Who photographed 'The Steerage' in 1907?", ["Alfred Stieglitz", "Edward Steichen", "Paul Strand", "Alvin Langdon Coburn"], "Alfred Stieglitz"),
    ("art_262", "What year was the first photograph taken?", ["1826 or 1827", "1839", "1850", "1800"], "1826 or 1827"),
    ("art_263", "Who invented the calotype process?", ["William Fox Talbot", "Louis Daguerre", "Nicéphore Niépce", "George Eastman"], "William Fox Talbot"),
    ("art_264", "What is Henri Cartier-Bresson's famous concept?", ["The decisive moment", "The golden hour", "Straight photography", "Pictorialism"], "The decisive moment"),
    ("art_265", "Who photographed 'Moonrise, Hernandez, New Mexico'?", ["Ansel Adams", "Edward Weston", "Minor White", "Imogen Cunningham"], "Ansel Adams"),
    ("art_266", "What does 'bokeh' come from?", ["Japanese word for blur", "German lens term", "French artistic term", "Latin for light"], "Japanese word for blur"),
    ("art_267", "Who founded the Photo-Secession movement?", ["Alfred Stieglitz", "Edward Steichen", "Gertrude Käsebier", "Clarence H. White"], "Alfred Stieglitz"),
    ("art_268", "What is the Zone System developed by Ansel Adams?", ["Technique for exposure and development", "Composition method", "Lens selection guide", "Camera focusing system"], "Technique for exposure and development"),
    ("art_269", "Who photographed nudes including 'Nude, 1936'?", ["Edward Weston", "Man Ray", "Helmut Newton", "Robert Mapplethorpe"], "Edward Weston"),
    ("art_270", "What war photographer co-founded Magnum Photos?", ["Robert Capa", "Henri Cartier-Bresson", "David Seymour", "George Rodger"], "Robert Capa"),
    ("art_271", "Who created surrealist photographs like 'Le Violon d'Ingres'?", ["Man Ray", "László Moholy-Nagy", "André Kertész", "Brassaï"], "Man Ray"),
    ("art_272", "What is the first permanent photograph called?", ["View from the Window at Le Gras", "The Steerage", "Boulevard du Temple", "The Horse in Motion"], "View from the Window at Le Gras"),
    ("art_273", "Who photographed the construction of the Empire State Building?", ["Lewis Hine", "Margaret Bourke-White", "Berenice Abbott", "Walker Evans"], "Lewis Hine"),
    ("art_274", "What movement emphasized photography as fine art?", ["Pictorialism", "Straight photography", "New Objectivity", "Surrealism"], "Pictorialism"),
    ("art_275", "Who photographed 'Tank Man' during Tiananmen Square?", ["Jeff Widener (and others)", "James Nachtwey", "Don McCullin", "Larry Burrows"], "Jeff Widener (and others)"),
    ("art_276", "What is the name for very long exposure photography?", ["Long exposure/Bulb mode", "Time-lapse", "HDR", "Bracketing"], "Long exposure/Bulb mode"),
    ("art_277", "Who created the 'Family of Man' exhibition?", ["Edward Steichen", "Alfred Stieglitz", "John Szarkowski", "Beaumont Newhall"], "Edward Steichen"),
    ("art_278", "What camera company created the first 35mm camera?", ["Leica", "Nikon", "Canon", "Kodak"], "Leica"),
    ("art_279", "Who photographed Paris streets at night?", ["Brassaï", "Henri Cartier-Bresson", "Robert Doisneau", "Eugène Atget"], "Brassaï"),
    ("art_280", "What is the process of lightening parts of a print called?", ["Dodging", "Burning", "Bleaching", "Washing"], "Dodging"),
]

for q in medium:
    new_questions.append({"id": q[0], "category": "Art", "subcategory": "Photography", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "medium", "topic": None, "subtopic": None})

# Hard questions (20)
hard = [
    ("art_281", "Who created 'Pepper No. 30' in 1930?", ["Edward Weston", "Ansel Adams", "Paul Strand", "Imogen Cunningham"], "Edward Weston"),
    ("art_282", "What is the Daguerreotype process based on?", ["Silver-plated copper", "Paper negatives", "Glass plates", "Film emulsion"], "Silver-plated copper"),
    ("art_283", "Who photographed 'Dunes, Oceano' series?", ["Edward Weston", "Ansel Adams", "Minor White", "Brett Weston"], "Edward Weston"),
    ("art_284", "What photography movement did August Sander represent?", ["New Objectivity (Neue Sachlichkeit)", "Pictorialism", "Surrealism", "Constructivism"], "New Objectivity (Neue Sachlichkeit)"),
    ("art_285", "Who created 'The Americans' photo book?", ["Robert Frank", "Walker Evans", "Garry Winogrand", "Lee Friedlander"], "Robert Frank"),
    ("art_286", "What is the wet collodion process?", ["Glass plate negative process", "Paper negative process", "Metal plate process", "Film development process"], "Glass plate negative process"),
    ("art_287", "Who photographed 'Identical Twins, Roselle, New Jersey'?", ["Diane Arbus", "Mary Ellen Mark", "Sally Mann", "Nan Goldin"], "Diane Arbus"),
    ("art_288", "What movement did Paul Strand's 'Abstraction, Porch Shadows' represent?", ["Straight photography/Modernism", "Pictorialism", "Surrealism", "Documentary"], "Straight photography/Modernism"),
    ("art_289", "Who created photograms without a camera?", ["Man Ray and László Moholy-Nagy", "Alfred Stieglitz", "Edward Steichen", "Ansel Adams"], "Man Ray and László Moholy-Nagy"),
    ("art_290", "What is the platinum print process known for?", ["Archival permanence and tonal range", "Fast processing", "Color accuracy", "Low cost"], "Archival permanence and tonal range"),
    ("art_291", "Who photographed 'Hands, Rebecca, New Mexico, 1957'?", ["Paul Strand", "Ansel Adams", "Edward Weston", "Minor White"], "Paul Strand"),
    ("art_292", "What is the term for combining multiple negatives?", ["Composite/Combination printing", "Double exposure", "Solarization", "Photomontage"], "Composite/Combination printing"),
    ("art_293", "Who created 'The Pond-Moonlight' (1904)?", ["Edward Steichen", "Alfred Stieglitz", "Gertrude Käsebier", "Clarence H. White"], "Edward Steichen"),
    ("art_294", "What is the Sabattier effect?", ["Partial reversal/Solarization", "Double exposure", "Color shift", "Grain increase"], "Partial reversal/Solarization"),
    ("art_295", "Who photographed 'Cotton Mill Girl' (1908)?", ["Lewis Hine", "Jacob Riis", "Walker Evans", "Dorothea Lange"], "Lewis Hine"),
    ("art_296", "What camera did Ansel Adams primarily use?", ["Large format view camera", "35mm Leica", "Medium format Hasselblad", "Twin-lens reflex"], "Large format view camera"),
    ("art_297", "Who created the 'Equivalents' cloud photographs?", ["Alfred Stieglitz", "Minor White", "Ansel Adams", "Edward Weston"], "Alfred Stieglitz"),
    ("art_298", "What is the gum bichromate process?", ["Pigment printing process", "Silver-based process", "Digital process", "Instant film process"], "Pigment printing process"),
    ("art_299", "Who photographed 'Paris de Nuit' in the 1930s?", ["Brassaï", "André Kertész", "Robert Doisneau", "Henri Cartier-Bresson"], "Brassaï"),
    ("art_300", "What is the cyanotype process known for?", ["Blue color/blueprint process", "Red color", "Black and white", "Color photography"], "Blue color/blueprint process"),
]

for q in hard:
    new_questions.append({"id": q[0], "category": "Art", "subcategory": "Photography", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "hard", "topic": None, "subtopic": None})

# Load, add, sort, save
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

data['categories']['Art'].extend(new_questions)
data['categories']['Art'].sort(key=lambda q: int(q['id'].split('_')[1]))

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added 60 Photography questions")
print(f"Art now has {len(data['categories']['Art'])} total questions")
print(f"Added: 20 easy, 20 medium, 20 hard")
