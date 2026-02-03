#!/usr/bin/env python3
"""
Fix sports questions that need proper context.
"""

import json

def main():
    # Read the draft sports file
    with open('/home/user/fiztrivia/Fiz/Resources/Expansion Packs/draft_sports.json', 'r') as f:
        data = json.load(f)

    # Map of question IDs to their fixes
    fixes = {
        'spt_015': {
            'old': 'What does RBI stand for?',
            'new': 'In baseball, what does RBI stand for?'
        },
        'spt_036': {
            'old': 'Which team drafted Michael Jordan?',
            'new': 'Which NBA team drafted Michael Jordan?'
        },
        'spt_042': {
            'old': "Which player is known as 'The Greek Freak'?",
            'new': "Which NBA player is known as 'The Greek Freak'?"
        },
        'spt_071': {
            'old': 'What is it called when a player uses their head to play the ball?',
            'new': 'In soccer, what is it called when a player uses their head to play the ball?'
        },
        'spt_177': {
            'old': 'What is the standard starting score in a game of 501?',
            'new': 'In darts, what is the standard starting score in a game of 501?'
        },
        'spt_311': {
            'old': 'What eight points of contact are used?',
            'new': 'In Muay Thai, what eight points of contact are used?'
        }
    }

    # Apply fixes to both free preview and paid questions
    fixed_count = 0
    for question_list in [data['freePreviewQuestions'], data['paidQuestions']]:
        for q in question_list:
            if q['id'] in fixes:
                fix = fixes[q['id']]
                if q['question'] == fix['old']:
                    q['question'] = fix['new']
                    fixed_count += 1
                    print(f"✓ Fixed {q['id']}:")
                    print(f"  Old: {fix['old']}")
                    print(f"  New: {fix['new']}")
                    print()

    # Save the updated file
    with open('/home/user/fiztrivia/Fiz/Resources/Expansion Packs/draft_sports.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("=" * 80)
    print(f"✅ Successfully fixed {fixed_count} questions!")
    print("=" * 80)

if __name__ == '__main__':
    main()
