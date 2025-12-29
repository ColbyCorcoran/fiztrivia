#!/usr/bin/env python3
"""Replace 3 duplicate Literature questions"""
import json

replacements = {
    # Replace lit_302 (duplicate of lit_289 - both about Toni Morrison)
    "lit_302": {
        "id": "lit_302",
        "category": "Literature",
        "subcategory": "Authors & Biography",
        "question": "Which American author won the first Pulitzer Prize for Fiction?",
        "options": ["Edith Wharton", "Willa Cather", "Sinclair Lewis", "Ernest Hemingway"],
        "correct_answer": "Edith Wharton",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },

    # Replace lit_192 (duplicate of lit_101 - both ask who wrote Paradise Lost)
    "lit_192": {
        "id": "lit_192",
        "category": "Literature",
        "subcategory": "Poetry",
        "question": "Who wrote 'The Faerie Queene', an allegorical epic poem?",
        "options": ["Edmund Spenser", "Christopher Marlowe", "Philip Sidney", "Ben Jonson"],
        "correct_answer": "Edmund Spenser",
        "difficulty": "medium",
        "topic": None,
        "subtopic": None
    },

    # Replace lit_233 (duplicate of lit_230 - both about Peter Rabbit/Beatrix Potter)
    "lit_233": {
        "id": "lit_233",
        "category": "Literature",
        "subcategory": "Children's Books",
        "question": "Who wrote 'James and the Giant Peach'?",
        "options": ["Roald Dahl", "E.B. White", "Beverly Cleary", "Judy Blume"],
        "correct_answer": "Roald Dahl",
        "difficulty": "easy",
        "topic": None,
        "subtopic": None
    }
}

def main():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    literature = data['categories']['Literature']

    replaced_count = 0
    for i, q in enumerate(literature):
        if q['id'] in replacements:
            old_question = q['question']
            literature[i] = replacements[q['id']]
            replaced_count += 1
            print(f"✅ Replaced {q['id']}:")
            print(f"   OLD: {old_question}")
            print(f"   NEW: {replacements[q['id']]['question']}")
            print()

    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Replaced {replaced_count} questions")

if __name__ == "__main__":
    main()
