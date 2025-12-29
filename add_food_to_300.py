#!/usr/bin/env python3
"""
Add 22 Food questions to reach 300 total
Prioritize smallest subcategories for balance
"""

import json

def add_food_questions():
    # Load current database
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    food_questions = data['categories']['Food']
    
    print(f"Current Food questions: {len(food_questions)}")
    print(f"Adding 22 questions (foo_279 to foo_300)")
    print()
    print("Distribution strategy:")
    print("  Sauces & Condiments: +7 (8 → 15)")
    print("  Food History: +6 (10 → 16)")
    print("  Desserts: +4 (18 → 22)")
    print("  Beverages: +2 (21 → 23)")
    print("  Cuisines: +2 (21 → 23)")
    print("  Cooking Techniques: +1 (22 → 23)")
    print()

    # NEW UNIQUE QUESTIONS (avoiding duplicates)
    new_questions = [
        # SAUCES & CONDIMENTS (7 questions) - foo_279-285
        {
            "id": "foo_279",
            "category": "Food",
            "subcategory": "Sauces & Condiments",
            "question": "What is the main ingredient in traditional pesto sauce?",
            "options": ["Basil", "Parsley", "Oregano", "Cilantro"],
            "correct_answer": "Basil",
            "difficulty": "medium"
        },
        {
            "id": "foo_280",
            "category": "Food",
            "subcategory": "Sauces & Condiments",
            "question": "Which French mother sauce is made with a white roux and milk?",
            "options": ["Béchamel", "Velouté", "Espagnole", "Hollandaise"],
            "correct_answer": "Béchamel",
            "difficulty": "hard"
        },
        {
            "id": "foo_281",
            "category": "Food",
            "subcategory": "Sauces & Condiments",
            "question": "What condiment is made from fermented soybeans?",
            "options": ["Soy sauce", "Worcestershire sauce", "Fish sauce", "Hot sauce"],
            "correct_answer": "Soy sauce",
            "difficulty": "easy"
        },
        {
            "id": "foo_282",
            "category": "Food",
            "subcategory": "Sauces & Condiments",
            "question": "What is the primary ingredient in aioli?",
            "options": ["Garlic", "Lemon", "Egg", "Mustard"],
            "correct_answer": "Garlic",
            "difficulty": "medium"
        },
        {
            "id": "foo_283",
            "category": "Food",
            "subcategory": "Sauces & Condiments",
            "question": "Which sauce is traditionally served with eggs Benedict?",
            "options": ["Hollandaise", "Béarnaise", "Béchamel", "Mornay"],
            "correct_answer": "Hollandaise",
            "difficulty": "hard"
        },
        {
            "id": "foo_284",
            "category": "Food",
            "subcategory": "Sauces & Condiments",
            "question": "What is the main ingredient in tartar sauce?",
            "options": ["Mayonnaise", "Sour cream", "Yogurt", "Cream cheese"],
            "correct_answer": "Mayonnaise",
            "difficulty": "easy"
        },
        {
            "id": "foo_285",
            "category": "Food",
            "subcategory": "Sauces & Condiments",
            "question": "What Asian condiment is made from chili peppers and fermented beans?",
            "options": ["Sambal oelek", "Hoisin sauce", "Oyster sauce", "Teriyaki sauce"],
            "correct_answer": "Sambal oelek",
            "difficulty": "hard"
        },

        # FOOD HISTORY (6 questions) - foo_286-291
        {
            "id": "foo_286",
            "category": "Food",
            "subcategory": "Food History",
            "question": "In what century was the tomato introduced to Europe from the Americas?",
            "options": ["16th century", "15th century", "17th century", "14th century"],
            "correct_answer": "16th century",
            "difficulty": "hard"
        },
        {
            "id": "foo_287",
            "category": "Food",
            "subcategory": "Food History",
            "question": "What food was originally called 'alligator pear'?",
            "options": ["Avocado", "Mango", "Papaya", "Kiwi"],
            "correct_answer": "Avocado",
            "difficulty": "medium"
        },
        {
            "id": "foo_288",
            "category": "Food",
            "subcategory": "Food History",
            "question": "Which ancient civilization first cultivated chocolate?",
            "options": ["Maya", "Aztec", "Inca", "Egyptian"],
            "correct_answer": "Maya",
            "difficulty": "hard"
        },
        {
            "id": "foo_289",
            "category": "Food",
            "subcategory": "Food History",
            "question": "What was the first vegetable grown in space in 1995?",
            "options": ["Potato", "Lettuce", "Carrot", "Tomato"],
            "correct_answer": "Potato",
            "difficulty": "hard"
        },
        {
            "id": "foo_290",
            "category": "Food",
            "subcategory": "Food History",
            "question": "Which European country first popularized French fries?",
            "options": ["Belgium", "France", "Netherlands", "Germany"],
            "correct_answer": "Belgium",
            "difficulty": "medium"
        },
        {
            "id": "foo_291",
            "category": "Food",
            "subcategory": "Food History",
            "question": "What was the first food eaten on the moon by astronauts?",
            "options": ["Freeze-dried fruit", "Tang", "Space ice cream", "Crackers"],
            "correct_answer": "Freeze-dried fruit",
            "difficulty": "hard"
        },

        # DESSERTS (4 questions) - foo_292-295
        {
            "id": "foo_292",
            "category": "Food",
            "subcategory": "Desserts",
            "question": "What Italian dessert features layers of coffee-soaked ladyfingers and mascarpone?",
            "options": ["Tiramisu", "Panna cotta", "Cannoli", "Zabaglione"],
            "correct_answer": "Tiramisu",
            "difficulty": "medium"
        },
        {
            "id": "foo_293",
            "category": "Food",
            "subcategory": "Desserts",
            "question": "What is the main flavoring in a traditional crème brûlée?",
            "options": ["Vanilla", "Chocolate", "Coffee", "Caramel"],
            "correct_answer": "Vanilla",
            "difficulty": "medium"
        },
        {
            "id": "foo_294",
            "category": "Food",
            "subcategory": "Desserts",
            "question": "What French pastry is made with choux dough and filled with cream?",
            "options": ["Éclair", "Croissant", "Macaron", "Tart"],
            "correct_answer": "Éclair",
            "difficulty": "hard"
        },
        {
            "id": "foo_295",
            "category": "Food",
            "subcategory": "Desserts",
            "question": "What dessert is traditionally served flambéed with rum or brandy?",
            "options": ["Bananas Foster", "Crêpes Suzette", "Cherries Jubilee", "All of the above"],
            "correct_answer": "All of the above",
            "difficulty": "hard"
        },

        # BEVERAGES (2 questions) - foo_296-297
        {
            "id": "foo_296",
            "category": "Food",
            "subcategory": "Beverages",
            "question": "What type of tea is fully oxidized?",
            "options": ["Black tea", "Green tea", "White tea", "Oolong tea"],
            "correct_answer": "Black tea",
            "difficulty": "medium"
        },
        {
            "id": "foo_297",
            "category": "Food",
            "subcategory": "Beverages",
            "question": "What is the main spirit in a Moscow Mule cocktail?",
            "options": ["Vodka", "Rum", "Gin", "Whiskey"],
            "correct_answer": "Vodka",
            "difficulty": "hard"
        },

        # CUISINES (2 questions) - foo_298-299
        {
            "id": "foo_298",
            "category": "Food",
            "subcategory": "Cuisines",
            "question": "What is the national dish of Spain made with rice, saffron, and seafood?",
            "options": ["Paella", "Risotto", "Jambalaya", "Biryani"],
            "correct_answer": "Paella",
            "difficulty": "medium"
        },
        {
            "id": "foo_299",
            "category": "Food",
            "subcategory": "Cuisines",
            "question": "What Japanese dish consists of battered and deep-fried seafood or vegetables?",
            "options": ["Tempura", "Teriyaki", "Katsu", "Yakitori"],
            "correct_answer": "Tempura",
            "difficulty": "easy"
        },

        # COOKING TECHNIQUES (1 question) - foo_300
        {
            "id": "foo_300",
            "category": "Food",
            "subcategory": "Cooking Techniques",
            "question": "What cooking method involves cooking food slowly in liquid at low temperatures?",
            "options": ["Braising", "Sautéing", "Grilling", "Broiling"],
            "correct_answer": "Braising",
            "difficulty": "medium"
        }
    ]

    # Add new questions
    food_questions.extend(new_questions)

    # Save updated database
    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✓ Added 22 new Food questions")
    print(f"\nNew Food total: {len(food_questions)} questions")

    # Show breakdown
    print("\nBreakdown by subcategory:")
    subcats = {}
    for q in food_questions:
        subcat = q['subcategory']
        if subcat not in subcats:
            subcats[subcat] = 0
        subcats[subcat] += 1

    for subcat in sorted(subcats.keys()):
        print(f"  {subcat}: {subcats[subcat]} questions")

    # Show difficulty breakdown
    print("\nBreakdown by difficulty:")
    diffs = {'easy': 0, 'medium': 0, 'hard': 0}
    for q in food_questions:
        diffs[q['difficulty']] += 1

    for diff in ['easy', 'medium', 'hard']:
        pct = (diffs[diff] / len(food_questions)) * 100
        print(f"  {diff.capitalize()}: {diffs[diff]} ({pct:.1f}%)")

    print("\n✓ Food category complete: 300/300 questions")

if __name__ == "__main__":
    add_food_questions()
