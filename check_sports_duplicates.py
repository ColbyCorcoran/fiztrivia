import json
from difflib import SequenceMatcher

# Load database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Get all Sports questions
sports_questions = data['categories']['Sports']

# Get newly added questions (spt_251 to spt_300)
new_question_ids = [f"spt_{i:03d}" for i in range(251, 301)]
new_questions = [q for q in sports_questions if q['id'] in new_question_ids]

print(f"Checking {len(new_questions)} newly added Sports questions against {len(sports_questions) - len(new_questions)} existing questions...\n")

# Check for duplicates
duplicates_found = []

for new_q in new_questions:
    for existing_q in sports_questions:
        if new_q['id'] == existing_q['id']:
            continue
        if existing_q['id'] in new_question_ids:
            continue

        # Check similarity
        ratio = SequenceMatcher(None, new_q['question'].lower(), existing_q['question'].lower()).ratio()

        if ratio > 0.90:  # Semantic duplicate threshold
            duplicates_found.append({
                'new_id': new_q['id'],
                'existing_id': existing_q['id'],
                'similarity': ratio,
                'new_question': new_q['question'],
                'existing_question': existing_q['question']
            })

if duplicates_found:
    print(f"⚠️ Found {len(duplicates_found)} potential duplicate(s):\n")
    for dup in duplicates_found:
        print(f"  {dup['new_id']} ↔ {dup['existing_id']} ({dup['similarity']:.1%} similar)")
        print(f"    New: {dup['new_question'][:70]}...")
        print(f"    Existing: {dup['existing_question'][:70]}...")
        print()
else:
    print("✅ No duplicates found! All new Sports questions are unique.")
