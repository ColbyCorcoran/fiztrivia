#!/usr/bin/env python3
"""
Balance answer option distribution in expansion pack files.
Shuffles options so correct answers are evenly distributed across slots A, B, C, D.
Preserves compound answers ("all of the above", "both X and Y") in slot D.
"""

import json
import random
import re
from datetime import datetime
from collections import Counter

def should_be_in_slot_d(answer_text):
    """Check if answer should stay in slot D (compound answers)."""
    patterns = [
        r'all of the above',
        r'both [A-D] and [A-D]',
        r'none of the above',
        r'all of these',
    ]
    
    for pattern in patterns:
        if re.search(pattern, answer_text, re.IGNORECASE):
            return True
    return False

def balance_pack(json_file, output_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    pack_name = data.get('packName', 'Unknown')

    # Target distribution: try to get close to 25% for each slot
    target_per_slot = {}
    balanced_count = 0
    skipped_count = 0
    fixed_missing = 0

    for section_name in ['freePreviewQuestions', 'paidQuestions']:
        questions = data.get(section_name, [])
        
        # Calculate target counts for this section
        total_questions = len(questions)
        target_per_slot = {
            'A': total_questions // 4,
            'B': total_questions // 4,
            'C': total_questions // 4,
            'D': total_questions // 4
        }
        
        # Give remainder to slots in order
        remainder = total_questions % 4
        for i, slot in enumerate(['A', 'B', 'C', 'D']):
            if i < remainder:
                target_per_slot[slot] += 1

        # Track current distribution
        current_counts = Counter()

        # Process each question
        for q in questions:
            options = q.get('options', [])
            correct_answer = q.get('correct_answer', '')
            
            if not options:
                continue
                
            # Check if correct answer is missing
            if not correct_answer or correct_answer not in options:
                # Try to infer from first option if it looks like the correct answer
                if options and len(options) > 0:
                    q['correct_answer'] = options[0]
                    correct_answer = options[0]
                    fixed_missing += 1
                    print(f"  Fixed missing answer for {q.get('id', 'UNKNOWN')}: set to '{correct_answer}'")
                else:
                    print(f"  ⚠️  Skipping {q.get('id', 'UNKNOWN')}: no options available")
                    continue

            # Check if this should stay in slot D
            if should_be_in_slot_d(correct_answer):
                # Ensure it's in slot D
                try:
                    current_index = options.index(correct_answer)
                    if current_index != 3:
                        options_copy = [opt for opt in options if opt != correct_answer]
                        options_copy.append(correct_answer)
                        q['options'] = options_copy
                        balanced_count += 1
                except ValueError:
                    pass
                current_counts['D'] += 1
                skipped_count += 1
                continue

            # Find least-used slot that needs more answers
            available_slots = [slot for slot, count in current_counts.items() 
                              if count < target_per_slot[slot]]
            
            if not available_slots:
                # All slots at target, just pick randomly
                target_slot = random.choice(['A', 'B', 'C', 'D'])
            else:
                # Pick from slots that need more
                target_slot = random.choice(available_slots)
            
            target_index = ['A', 'B', 'C', 'D'].index(target_slot)

            # Shuffle options to put correct answer in target slot
            try:
                current_index = options.index(correct_answer)
                
                if current_index != target_index:
                    # Create new option order
                    options_copy = options.copy()
                    
                    # Remove correct answer from current position
                    options_copy.remove(correct_answer)
                    
                    # Insert at target position
                    options_copy.insert(target_index, correct_answer)
                    
                    # Update the question
                    q['options'] = options_copy
                    balanced_count += 1
                
                current_counts[target_slot] += 1
                
            except ValueError:
                print(f"  ⚠️  Warning: Correct answer not found for {q.get('id', 'UNKNOWN')}")

    # Write balanced data
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return pack_name, balanced_count, skipped_count, fixed_missing

def main():
    expansion_files = [
        '/Users/colbycorcoran/Documents/App Development/Fiz/Fiz/Resources/Expansion Packs/expansion_harry_potter.json',
        '/Users/colbycorcoran/Documents/App Development/Fiz/Fiz/Resources/Expansion Packs/expansion_pokemon.json',
        '/Users/colbycorcoran/Documents/App Development/Fiz/Fiz/Resources/Expansion Packs/expansion_80s_trivia.json',
        '/Users/colbycorcoran/Documents/App Development/Fiz/Fiz/Resources/Expansion Packs/expansion_disney.json',
        '/Users/colbycorcoran/Documents/App Development/Fiz/Fiz/Resources/Expansion Packs/expansion_the_office.json',
    ]

    print("Balancing answer distributions in expansion packs...")
    print("=" * 80)

    all_results = []

    for file_path in expansion_files:
        try:
            # Create backup
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = file_path.replace('.json', f'_backup_{timestamp}.json')
            
            import shutil
            shutil.copy(file_path, backup_file)
            print(f"\n✅ Backup created: {backup_file}")

            # Balance the pack
            pack_name, balanced, skipped, fixed = balance_pack(file_path, file_path)
            all_results.append((pack_name, balanced, skipped, fixed))
            
            print(f"\n{pack_name}:")
            print(f"  - Balanced: {balanced} questions")
            print(f"  - Skipped (compound answers): {skipped} questions")
            if fixed > 0:
                print(f"  - Fixed missing answers: {fixed} questions")
            
        except FileNotFoundError:
            print(f"\n⚠️  File not found: {file_path}")
        except Exception as e:
            print(f"\n❌  Error processing {file_path}: {e}")
            import traceback
            traceback.print_exc()

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    for pack_name, balanced, skipped, fixed in all_results:
        print(f"{pack_name:30s} - Balanced: {balanced:4d}, Skipped: {skipped:2d}, Fixed: {fixed:2d}")

    print("\nRe-analyzing distributions...")

if __name__ == '__main__':
    main()
