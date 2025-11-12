import json
from difflib import SequenceMatcher

# Load the database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# IDs of replacement questions
replacement_ids = [
    # Food (4)
    'foo_257', 'foo_258', 'foo_259', 'foo_260',
    # History (9)
    'his_260', 'his_261', 'his_262', 'his_263', 'his_264', 'his_265', 'his_266', 'his_267', 'his_268',
    # Sports (10)
    'spt_261', 'spt_262', 'spt_263', 'spt_264', 'spt_265', 'spt_266', 'spt_267', 'spt_268', 'spt_269', 'spt_270',
    # Science (11)
    'sci_265', 'sci_266', 'sci_267', 'sci_268', 'sci_269', 'sci_270', 'sci_271', 'sci_272', 'sci_273', 'sci_274', 'sci_275',
    # Bible (12)
    'bib_260', 'bib_261', 'bib_262', 'bib_263', 'bib_264', 'bib_265', 'bib_266', 'bib_267', 'bib_268', 'bib_269', 'bib_270', 'bib_271',
    # Earth (12)
    'ear_253', 'ear_254', 'ear_255', 'ear_256', 'ear_257', 'ear_258', 'ear_259', 'ear_260', 'ear_261', 'ear_262', 'ear_263', 'ear_264'
]

# Collect all questions
all_questions = []
for category in data['categories'].values():
    all_questions.extend(category)

# Separate replacement questions and existing questions
replacement_questions = [q for q in all_questions if q['id'] in replacement_ids]
existing_questions = [q for q in all_questions if q['id'] not in replacement_ids]

print(f"Checking {len(replacement_questions)} replacement questions against {len(existing_questions)} existing questions")

# Check for duplicates
duplicates_found = []
for repl_q in replacement_questions:
    repl_text = repl_q['question'].lower().strip()
    
    for exist_q in existing_questions:
        exist_text = exist_q['question'].lower().strip()
        
        # Check exact match
        if repl_text == exist_text:
            duplicates_found.append({
                'type': 'EXACT',
                'replacement': repl_q['id'],
                'existing': exist_q['id'],
                'question': repl_q['question'],
                'similarity': 100
            })
        else:
            # Check semantic similarity
            similarity = SequenceMatcher(None, repl_text, exist_text).ratio() * 100
            if similarity > 90:
                # Also check if answers match
                if repl_q['correct_answer'] == exist_q['correct_answer']:
                    duplicates_found.append({
                        'type': 'SEMANTIC',
                        'replacement': repl_q['id'],
                        'existing': exist_q['id'],
                        'question_new': repl_q['question'],
                        'question_old': exist_q['question'],
                        'similarity': round(similarity, 2)
                    })

if duplicates_found:
    print(f"\n⚠️ FOUND {len(duplicates_found)} DUPLICATE(S):\n")
    for dup in duplicates_found:
        print(f"{dup['type']} DUPLICATE:")
        print(f"  Replacement: {dup['replacement']}")
        print(f"  Existing: {dup['existing']}")
        if dup['type'] == 'EXACT':
            print(f"  Question: {dup['question']}")
        else:
            print(f"  New: {dup['question_new']}")
            print(f"  Old: {dup['question_old']}")
            print(f"  Similarity: {dup['similarity']}%")
        print()
else:
    print("\n✅ NO DUPLICATES FOUND! All 58 replacement questions are unique!")

print(f"\nFinal database: {len(all_questions)} total questions")
