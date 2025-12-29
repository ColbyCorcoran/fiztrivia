#!/usr/bin/env python3
"""
Analyze Superhero questions to classify as Marvel vs DC
"""

import json

def analyze_superhero_questions():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    entertainment = data['categories']['Entertainment']
    superhero_questions = [q for q in entertainment if q.get('subcategory') == 'Superheroes']

    print(f"Total Superhero questions: {len(superhero_questions)}\n")
    print("=" * 80)
    print("ANALYZING SUPERHERO QUESTIONS FOR MARVEL vs DC")
    print("=" * 80)

    # Keywords for classification
    marvel_keywords = ['iron man', 'tony stark', 'captain america', 'steve rogers',
                       'thor', 'hulk', 'bruce banner', 'spider-man', 'peter parker',
                       'black widow', 'hawkeye', 'avengers', 'marvel', 'wakanda',
                       'black panther', 'thanos', 'infinity', 'x-men', 'wolverine',
                       'fantastic four', 'doctor strange', 'ant-man', 'guardians',
                       's.h.i.e.l.d', 'shield', 's.w.o.r.d', 'sword', 'jarvis', 'friday',
                       'morgan stark', 'peter quill', 'wanda', 'scarlet witch', 'deadpool',
                       'nova corps', 'galactus', 'daredevil', 'matt murdock', 's.s.r',
                       'bucky barnes', 'winter soldier', 'ned leeds', 'daily bugle',
                       'karen', 'edith', 'stormbreaker', 'mjolnir', 'asgard', 'natasha',
                       'clint barton', 'stephen strange', 'billy and tommy']

    dc_keywords = ['batman', 'bruce wayne', 'superman', 'clark kent', 'wonder woman',
                   'diana prince', 'flash', 'barry allen', 'aquaman', 'green lantern',
                   'justice league', 'dc comics', 'gotham', 'metropolis', 'krypton',
                   'joker', 'lex luthor', 'harley quinn', 'catwoman', 'robin',
                   'batmobile', 'batcave', 'alfred', 'daily planet', 'perry white',
                   'cyborg', 'victor stone', 'martian manhunter', 'shazam', 'billy batson',
                   'hawkman', 'carter hall', 'zatanna', 'constantine', 'john constantine',
                   'swamp thing', 'alec holland', 'lobo', 'themyscira', 'atlantis',
                   'jor-el', 'lasso of truth', 'yellow lantern', 'jimmy olsen']

    marvel_questions = []
    dc_questions = []
    unclear_questions = []

    for q in superhero_questions:
        question_lower = q['question'].lower()
        options_lower = ' '.join(q['options']).lower()
        answer_lower = q['correct_answer'].lower()
        full_text = f"{question_lower} {options_lower} {answer_lower}"

        # Check keywords in full text
        is_marvel_full = any(keyword in full_text for keyword in marvel_keywords)
        is_dc_full = any(keyword in full_text for keyword in dc_keywords)

        # If both or neither, use answer to decide
        if is_marvel_full and is_dc_full:
            # Trick question - use answer
            is_marvel = any(keyword in answer_lower for keyword in marvel_keywords)
            is_dc = any(keyword in answer_lower for keyword in dc_keywords)
        else:
            is_marvel = is_marvel_full
            is_dc = is_dc_full

        if is_marvel and not is_dc:
            marvel_questions.append(q)
            classification = "MARVEL"
        elif is_dc and not is_marvel:
            dc_questions.append(q)
            classification = "DC"
        else:
            # Still unclear - needs manual review
            unclear_questions.append(q)
            classification = "UNCLEAR"

        print(f"\n[{q['id']}] [{classification}]")
        print(f"Q: {q['question']}")
        print(f"A: {q['correct_answer']}")

    print("\n" + "=" * 80)
    print("CLASSIFICATION SUMMARY:")
    print("=" * 80)
    print(f"Marvel: {len(marvel_questions)} questions")
    print(f"DC: {len(dc_questions)} questions")
    print(f"Unclear: {len(unclear_questions)} questions")
    print(f"Total: {len(superhero_questions)} questions")

    if unclear_questions:
        print("\n" + "=" * 80)
        print("UNCLEAR QUESTIONS NEEDING MANUAL REVIEW:")
        print("=" * 80)
        for q in unclear_questions:
            print(f"\n[{q['id']}] {q['question']}")
            print(f"Options: {', '.join(q['options'])}")
            print(f"Answer: {q['correct_answer']}")

if __name__ == "__main__":
    analyze_superhero_questions()
