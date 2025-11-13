import json

# Load database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Remove internal duplicates
ids_to_remove = [
    'bib_308',  # Duplicate of bib_252
    'bib_309',  # Duplicate of bib_257
    'bib_311',  # Duplicate of bib_273
    'bib_312',  # Duplicate of bib_281
]

original_count = len(data['categories']['Bible'])
data['categories']['Bible'] = [q for q in data['categories']['Bible'] if q['id'] not in ids_to_remove]
removed_count = original_count - len(data['categories']['Bible'])

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ Removed {removed_count} internal duplicate Bible questions")
print(f"Removed IDs: {', '.join(ids_to_remove)}")
print(f"Bible questions now: {len(data['categories']['Bible'])}")
