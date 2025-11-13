import json

# Load database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Remove the higher ID duplicates
ids_to_remove = ['sci_210', 'sci_214']

data['categories']['Science'] = [
    q for q in data['categories']['Science']
    if q['id'] not in ids_to_remove
]

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Removed {len(ids_to_remove)} duplicate questions")
print(f"Science: now {len(data['categories']['Science'])} questions")
print(f"Total: {sum(len(data['categories'][cat]) for cat in data['categories'])} questions")
