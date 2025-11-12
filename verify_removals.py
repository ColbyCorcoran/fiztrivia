import json

# Load the questions
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# IDs we tried to remove
ids_to_remove = [
    'sci_160', 'sci_162', 'sci_163', 'sci_165', 'sci_167', 'sci_168', 'sci_170', 'sci_172', 'sci_173',
    'spt_181',
    'foo_094', 'foo_098', 'foo_165',
    'ear_190', 'ear_192'
]

# Check which ones are still in the database
all_ids = []
for category in data['categories']:
    for question in data['categories'][category]:
        all_ids.append(question['id'])

still_present = [id for id in ids_to_remove if id in all_ids]
if still_present:
    print(f"IDs that are still in database: {still_present}")
else:
    print("All duplicate IDs successfully removed")

# Check if any of the IDs were never there
never_present = [id for id in ids_to_remove if id not in all_ids]
if never_present:
    print(f"IDs that were never in database: {never_present}")
