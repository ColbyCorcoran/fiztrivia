#!/usr/bin/env python3
"""Replace 1 duplicate Technology question"""
import json

replacement = {
    # Replace tec_298 (duplicate of tec_284 - both about Wright Brothers first flight)
    "tec_298": {
        "id": "tec_298",
        "category": "Technology",
        "subcategory": "Inventions",
        "question": "Who invented the first practical parachute design?",
        "options": ["Louis-Sébastien Lenormand", "Leonardo da Vinci", "André-Jacques Garnerin", "Faust Vrančić"],
        "correct_answer": "Louis-Sébastien Lenormand",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    }
}

def main():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    technology = data['categories']['Technology']

    replaced_count = 0
    for i, q in enumerate(technology):
        if q['id'] in replacement:
            old_question = q['question']
            technology[i] = replacement[q['id']]
            replaced_count += 1
            print(f"✅ Replaced {q['id']}:")
            print(f"   OLD: {old_question}")
            print(f"   NEW: {replacement[q['id']]['question']}")
            print()

    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Replaced {replaced_count} question(s)")

if __name__ == "__main__":
    main()
