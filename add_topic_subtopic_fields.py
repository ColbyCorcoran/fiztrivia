#!/usr/bin/env python3
"""Add topic and subtopic fields to all questions missing them"""
import json

with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

print("=== ADDING TOPIC/SUBTOPIC FIELDS ===\n")

total_updated = 0
category_updates = {}

for category_name, questions in data['categories'].items():
    updated_count = 0

    for q in questions:
        if 'topic' not in q or 'subtopic' not in q:
            # Add both fields with null values
            q['topic'] = None
            q['subtopic'] = None
            updated_count += 1
            total_updated += 1

    if updated_count > 0:
        category_updates[category_name] = updated_count
        print(f"{category_name}: Added fields to {updated_count} questions")

# Write back to file
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n✅ Total questions updated: {total_updated}")
print("\nAll questions now have topic and subtopic fields (set to null for later tagging)")

