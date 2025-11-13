import json

# Load the questions
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# IDs to remove
ids_to_remove = [
    'sci_160', 'sci_162', 'sci_163', 'sci_165', 'sci_167', 'sci_168', 'sci_170', 'sci_172', 'sci_173',
    'spt_181',
    'foo_094', 'foo_098', 'foo_165',
    'ear_190', 'ear_192'
]

# Remove duplicates from each category
removed_count = 0
for category in data['categories']:
    original_count = len(data['categories'][category])
    data['categories'][category] = [
        q for q in data['categories'][category] 
        if q['id'] not in ids_to_remove
    ]
    removed = original_count - len(data['categories'][category])
    if removed > 0:
        print(f"{category}: Removed {removed} duplicate(s)")
        removed_count += removed

# Fix ambiguous questions - add sport names
for category in data['categories']:
    for question in data['categories'][category]:
        if question['id'] == 'spt_013':
            question['question'] = "How many players are on the field for each American football team during play?"
            print(f"Fixed spt_013: Added 'American football' to question")
        elif question['id'] == 'spt_184':
            question['question'] = "How many players are on the field for each baseball team during play?"
            print(f"Fixed spt_184: Added 'baseball' to question")

# Save the cleaned data
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"\nTotal duplicates removed: {removed_count}")

# Count final questions
total = sum(len(data['categories'][cat]) for cat in data['categories'])
print(f"Final question count: {total}")
