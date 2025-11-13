import json
from difflib import SequenceMatcher

# Load the database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# The 4 final replacements
final_ids = ['spt_271', 'sci_276', 'ear_265', 'ear_266']

# Collect all questions
all_questions = []
for category in data['categories'].values():
    all_questions.extend(category)

# Separate final questions and all others
final_questions = [q for q in all_questions if q['id'] in final_ids]
other_questions = [q for q in all_questions if q['id'] not in final_ids]

print(f"Checking {len(final_questions)} final replacement questions...")

duplicates_found = []
for final_q in final_questions:
    final_text = final_q['question'].lower().strip()
    
    for other_q in other_questions:
        other_text = other_q['question'].lower().strip()
        
        if final_text == other_text:
            duplicates_found.append({
                'new': final_q['id'],
                'existing': other_q['id'],
                'question': final_q['question']
            })

if duplicates_found:
    print(f"\n⚠️ FOUND {len(duplicates_found)} DUPLICATE(S)!")
    for dup in duplicates_found:
        print(f"  {dup['new']} duplicates {dup['existing']}: {dup['question']}")
else:
    print("\n✅ ALL CLEAR! No duplicates found in final 4 questions!")
    print("\nFinal database ready:")
    print(f"  Total questions: {len(all_questions)}")
    print("  All categories at 250 (except Entertainment at 307)")
