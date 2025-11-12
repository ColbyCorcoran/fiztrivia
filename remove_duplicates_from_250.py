import json

# Load the questions
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# All duplicate IDs to remove
ids_to_remove = [
    # Sports (10)
    'spt_213', 'spt_227', 'spt_229', 'spt_237', 'spt_239', 'spt_245', 'spt_247', 'spt_250', 'spt_252', 'spt_253',
    # Bible (12)
    'bib_215', 'bib_216', 'bib_218', 'bib_222', 'bib_226', 'bib_230', 'bib_239', 'bib_240', 'bib_248', 'bib_250', 'bib_255', 'bib_259',
    # History (9)
    'his_211', 'his_216', 'his_221', 'his_223', 'his_226', 'his_243', 'his_251', 'his_252', 'his_254',
    # Science (11)
    'sci_216', 'sci_233', 'sci_236', 'sci_237', 'sci_241', 'sci_242', 'sci_243', 'sci_246', 'sci_254', 'sci_256', 'sci_260',
    # Food (4)
    'foo_207', 'foo_208', 'foo_209', 'foo_255',
    # Earth (10)
    'ear_212', 'ear_222', 'ear_224', 'ear_229', 'ear_234', 'ear_236', 'ear_237', 'ear_242', 'ear_243', 'ear_244',
    # Special cases - remove one from each pair
    'ear_245',  # Keep sci_248
    'ear_233'   # Keep ear_207
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

# Show what each category needs
print("\nQuestions needed to reach 250:")
for category in ['Bible', 'Earth', 'Food', 'History', 'Science', 'Sports']:
    count = len(data['categories'][category])
    needed = 250 - count
    if needed > 0:
        print(f"  {category}: {count} → need {needed} more")
