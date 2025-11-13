import json

# Load the backup
with open('Fiz/Resources/questions_backup_20251112_214451.json', 'r') as f:
    data = json.load(f)

# IDs we tried to remove
ids_to_remove = [
    'sci_160', 'sci_162', 'sci_163', 'sci_165', 'sci_167', 'sci_168', 'sci_170', 'sci_172', 'sci_173',
    'spt_181',
    'foo_094', 'foo_098', 'foo_165',
    'ear_190', 'ear_192'
]

# Check which ones existed in the backup
all_ids = []
for category in data['categories']:
    for question in data['categories'][category]:
        all_ids.append(question['id'])

existed = [id for id in ids_to_remove if id in all_ids]
print(f"IDs that existed in backup: {existed}")
print(f"Count: {len(existed)}")

did_not_exist = [id for id in ids_to_remove if id not in all_ids]
if did_not_exist:
    print(f"\nIDs that did NOT exist in original: {did_not_exist}")
    print(f"Count: {len(did_not_exist)}")
