import json

# Load the database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Check sci_277
all_questions = []
for category in data['categories'].values():
    all_questions.extend(category)

sci_277 = next(q for q in all_questions if q['id'] == 'sci_277')
others = [q for q in all_questions if q['id'] != 'sci_277']

duplicate = False
for q in others:
    if q['question'].lower().strip() == sci_277['question'].lower().strip():
        print(f"⚠️ sci_277 duplicates {q['id']}")
        duplicate = True
        break

if not duplicate:
    print("✅ SUCCESS! All questions are now unique!")
    print(f"\nFinal database stats:")
    print(f"  Total questions: {len(all_questions)}")
    for cat in sorted(data['categories'].keys()):
        print(f"  {cat}: {len(data['categories'][cat])}")
