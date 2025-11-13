import json

# Load the questions
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# IDs to remove (28 total)
ids_to_remove = [
    # Sports (7)
    'spt_190', 'spt_192', 'spt_194', 'spt_196', 'spt_198', 'spt_200', 'spt_201',
    # History (8)
    'his_175', 'his_189', 'his_190', 'his_193', 'his_195', 'his_196', 'his_198', 'his_200',
    # Bible (5)
    'bib_190', 'bib_196', 'bib_197', 'bib_201', 'bib_203',
    # Science (5)
    'sci_179', 'sci_185', 'sci_202', 'sci_203', 'sci_204',
    # Food (3)
    'foo_176', 'foo_185', 'foo_192'
]

# Remove duplicates from each category
removed_by_category = {}
for category in data['categories']:
    original_count = len(data['categories'][category])
    data['categories'][category] = [
        q for q in data['categories'][category] 
        if q['id'] not in ids_to_remove
    ]
    removed = original_count - len(data['categories'][category])
    if removed > 0:
        removed_by_category[category] = removed
        print(f"{category}: Removed {removed} duplicate(s), now {len(data['categories'][category])} questions")

# Save the cleaned data
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"\nTotal duplicates removed: {sum(removed_by_category.values())}")

# Count final questions
total = sum(len(data['categories'][cat]) for cat in data['categories'])
print(f"Final question count: {total}")
