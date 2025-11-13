import json

# Load database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# IDs to remove (duplicates found)
ids_to_remove = [
    'bib_252',  # Duplicate of bib_212
    'bib_254',  # Duplicate of bib_092
    'bib_257',  # Duplicate of bib_206
    'bib_263',  # Duplicate of bib_205
    'bib_264',  # Duplicate of bib_046
    'bib_266',  # Duplicate of bib_047
    'bib_268',  # Duplicate of bib_102
    'bib_273',  # Duplicate of bib_202
    'bib_275',  # Duplicate of bib_140
    'bib_281',  # Duplicate of bib_079
    'bib_284',  # Duplicate of bib_174
    'bib_298',  # Duplicate of bib_208
]

# Remove duplicates
original_count = len(data['categories']['Bible'])
data['categories']['Bible'] = [q for q in data['categories']['Bible'] if q['id'] not in ids_to_remove]
removed_count = original_count - len(data['categories']['Bible'])

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ Removed {removed_count} duplicate Bible questions")
print(f"Removed IDs: {', '.join(ids_to_remove)}")
print(f"Bible questions now: {len(data['categories']['Bible'])}")
