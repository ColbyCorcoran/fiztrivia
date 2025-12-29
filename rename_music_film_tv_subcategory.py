#!/usr/bin/env python3
"""Rename Film & TV subcategory to Music in Film & TV"""
import json

with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

music_questions = data['categories']['Music']

renamed_count = 0
for q in music_questions:
    if q['subcategory'] == 'Film & TV':
        q['subcategory'] = 'Music in Film & TV'
        renamed_count += 1

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Renamed {renamed_count} questions from 'Film & TV' to 'Music in Film & TV'")
