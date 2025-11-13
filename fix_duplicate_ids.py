import json

# Load database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Get Bible questions
bible_questions = data['categories']['Bible']
print(f"Original Bible questions: {len(bible_questions)}")

# Remove duplicate IDs (keep first occurrence)
seen_ids = set()
unique_questions = []

for q in bible_questions:
    if q['id'] not in seen_ids:
        seen_ids.add(q['id'])
        unique_questions.append(q)
    else:
        print(f"Removing duplicate ID: {q['id']}")

data['categories']['Bible'] = unique_questions

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"\n✅ Fixed duplicate IDs")
print(f"New Bible total: {len(data['categories']['Bible'])} questions")
