#!/usr/bin/env python3
"""
Script to remove answer-revealing parentheses from trivia question databases.
Cleans parenthetical information from answer options and correct_answer fields.
"""

import json
import re
import sys
from pathlib import Path


def remove_parentheses(text):
    """Remove parentheses and their contents from text."""
    if not isinstance(text, str):
        return text

    # Remove anything in parentheses, including the parens and any whitespace before them
    cleaned = re.sub(r'\s*\([^)]*\)', '', text)
    return cleaned.strip()


def clean_question_file(file_path):
    """Clean parentheses from a question database file."""
    print(f"\n{'='*60}")
    print(f"Processing: {file_path}")
    print(f"{'='*60}")

    # Load the JSON file
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Get questions array (handle different structures)
    questions = []
    is_categories_format = False

    if isinstance(data, list):
        questions = data
    elif 'categories' in data:
        # Main questions.json format with categories
        is_categories_format = True
        for category_name, category_questions in data['categories'].items():
            questions.extend(category_questions)
    elif 'questions' in data:
        questions = data['questions']
    elif 'freePreviewQuestions' in data or 'paidQuestions' in data:
        # Expansion pack format
        questions = data.get('freePreviewQuestions', []) + data.get('paidQuestions', [])
    else:
        print(f"ERROR: Could not find questions in {file_path}")
        return 0

    original_count = len(questions)
    changes_made = 0
    empty_values = []

    # Process each question
    for question in questions:
        question_id = question.get('id', 'unknown')
        modified = False

        # Clean each option
        if 'options' in question:
            cleaned_options = []
            for i, opt in enumerate(question['options']):
                cleaned_opt = remove_parentheses(opt)
                if cleaned_opt != opt:
                    modified = True
                if not cleaned_opt:
                    empty_values.append(f"{question_id}: Empty option at index {i}")
                cleaned_options.append(cleaned_opt)
            question['options'] = cleaned_options

        # Clean correct answer
        if 'correct_answer' in question:
            original_answer = question['correct_answer']
            cleaned_answer = remove_parentheses(original_answer)
            if cleaned_answer != original_answer:
                modified = True
            if not cleaned_answer:
                empty_values.append(f"{question_id}: Empty correct_answer")
            question['correct_answer'] = cleaned_answer

        if modified:
            changes_made += 1

    # Write back to file with proper formatting
    if isinstance(data, list):
        output_data = questions
    elif is_categories_format:
        # Rebuild categories structure
        question_index = 0
        for category_name, category_questions in data['categories'].items():
            count = len(category_questions)
            data['categories'][category_name] = questions[question_index:question_index + count]
            question_index += count
        output_data = data
    else:
        # Preserve original structure for expansion packs
        if 'freePreviewQuestions' in data or 'paidQuestions' in data:
            free_count = len(data.get('freePreviewQuestions', []))
            data['freePreviewQuestions'] = questions[:free_count]
            data['paidQuestions'] = questions[free_count:]
        else:
            data['questions'] = questions
        output_data = data

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    # Print summary
    print(f"✓ Original question count: {original_count}")
    print(f"✓ Questions modified: {changes_made}")
    print(f"✓ Final question count: {len(questions)}")

    if empty_values:
        print(f"\n⚠️  WARNING: Found empty values after cleaning:")
        for msg in empty_values:
            print(f"  - {msg}")

    return changes_made


def main():
    """Process all question database files."""
    base_path = Path(__file__).parent / "Fiz" / "Resources"

    files_to_process = [
        ("questions.json", 99),
        ("Expansion Packs/expansion_pokemon.json", 46),
        ("Expansion Packs/expansion_harry_potter.json", 35),
        ("Expansion Packs/expansion_disney.json", 33),
        ("Expansion Packs/expansion_80s_trivia.json", 18),
        ("Expansion Packs/expansion_the_office.json", 13),
    ]

    total_changes = 0

    for file_name, expected_changes in files_to_process:
        file_path = base_path / file_name
        if not file_path.exists():
            print(f"ERROR: File not found: {file_path}")
            continue

        changes = clean_question_file(str(file_path))
        total_changes += changes

        if changes != expected_changes:
            print(f"⚠️  Expected {expected_changes} changes, but made {changes}")

    print(f"\n{'='*60}")
    print(f"TOTAL CHANGES: {total_changes}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
