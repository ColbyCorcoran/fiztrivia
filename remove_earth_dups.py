import json

# Load database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Remove exact duplicates
ids_to_remove = [
    'ear_251', 'ear_256', 'ear_259', 'ear_270', 'ear_271',
    'ear_272', 'ear_277', 'ear_278', 'ear_287', 'ear_293', 'ear_300'
]

original_count = len(data['categories']['Earth'])
data['categories']['Earth'] = [q for q in data['categories']['Earth'] if q['id'] not in ids_to_remove]
removed_count = original_count - len(data['categories']['Earth'])

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ Removed {removed_count} duplicate Earth questions")
print(f"Removed IDs: {', '.join(ids_to_remove)}")
print(f"Earth questions now: {len(data['categories']['Earth'])}")
