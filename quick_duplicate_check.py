import json
from difflib import SequenceMatcher

# Load database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Collect all questions
all_questions = []
for category in data['categories'].values():
    all_questions.extend(category)

print(f"Checking {len(all_questions)} questions for duplicates...")

# Check for exact duplicates
duplicates = []
for i, q1 in enumerate(all_questions):
    for q2 in all_questions[i+1:]:
        if q1['question'].lower().strip() == q2['question'].lower().strip():
            duplicates.append((q1['id'], q2['id'], q1['question']))

if duplicates:
    print(f"\n⚠️ Found {len(duplicates)} exact duplicate(s):")
    for dup in duplicates[:5]:  # Show first 5
        print(f"  {dup[0]} ↔ {dup[1]}: {dup[2][:60]}...")
    if len(duplicates) > 5:
        print(f"  ... and {len(duplicates) - 5} more")
else:
    print("\n✅ No exact duplicates found! Database is clean.")
    print("Ready to begin expansion.\n")
