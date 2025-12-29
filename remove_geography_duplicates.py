#!/usr/bin/env python3
"""Remove duplicate Geography questions found in final verification"""
import json

# IDs to remove (keep the lower ID in each pair)
ids_to_remove = [
    'geo_032',  # Duplicate of geo_004 (largest ocean)
    'geo_038',  # Duplicate of geo_016 (largest island)
    'geo_042'   # Duplicate of geo_019 (tallest waterfall)
]

# Note: geo_186 and geo_200 are NOT duplicates - they ask about different flags
# (Italy and Mexico) that happen to have the same colors. This is acceptable.

# Load existing data
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

geography_questions = data['categories']['Geography']
original_count = len(geography_questions)

# Remove duplicates
geography_questions = [q for q in geography_questions if q['id'] not in ids_to_remove]

data['categories']['Geography'] = geography_questions

# Save back
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

removed_count = original_count - len(geography_questions)
print(f"✅ Removed {removed_count} duplicate questions")
print(f"Geography: {original_count} → {len(geography_questions)} questions")
print(f"\nRemoved IDs: {', '.join(ids_to_remove)}")
print(f"\nNeed to add {removed_count} replacement questions to reach 300")
