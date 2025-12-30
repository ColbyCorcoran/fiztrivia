#!/usr/bin/env python3
"""
Reorganize Food category from 10 to 6 subcategories:
1. Desserts → Baking & Desserts
2. Cooking Techniques + Sauces & Condiments → Cooking
3. Famous Chefs/Restaurants → Food History
4. Dishes + Cuisines → Dishes & Cuisines
5. Keep Ingredients
6. Keep Beverages
"""
import json

def main():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    food = data['categories']['Food']

    print("Original subcategories:")
    subcats = {}
    for q in food:
        sc = q.get('subcategory', 'None')
        subcats[sc] = subcats.get(sc, 0) + 1
    for sc, count in sorted(subcats.items()):
        print(f"  {sc}: {count} questions")
    print()

    # Reorganize subcategories
    changes = 0

    for q in food:
        old_subcat = q['subcategory']

        # 1. Desserts → Baking & Desserts
        if q['subcategory'] == 'Desserts':
            q['subcategory'] = 'Baking & Desserts'
            changes += 1
        elif q['subcategory'] == 'Baking':
            q['subcategory'] = 'Baking & Desserts'
            changes += 1

        # 2. Cooking Techniques + Sauces & Condiments → Cooking
        elif q['subcategory'] == 'Cooking Techniques':
            q['subcategory'] = 'Cooking'
            changes += 1
        elif q['subcategory'] == 'Sauces & Condiments':
            q['subcategory'] = 'Cooking'
            changes += 1

        # 3. Famous Chefs/Restaurants → Food History
        elif q['subcategory'] == 'Famous Chefs/Restaurants':
            q['subcategory'] = 'Food History'
            changes += 1

        # 4. Dishes + Cuisines → Dishes & Cuisines
        elif q['subcategory'] == 'Dishes':
            q['subcategory'] = 'Dishes & Cuisines'
            changes += 1
        elif q['subcategory'] == 'Cuisines':
            q['subcategory'] = 'Dishes & Cuisines'
            changes += 1

    print(f"Made {changes} subcategory changes")
    print()

    # Count new subcategories
    new_subcats = {}
    for q in food:
        sc = q.get('subcategory', 'None')
        new_subcats[sc] = new_subcats.get(sc, 0) + 1

    print("New subcategories:")
    for sc, count in sorted(new_subcats.items()):
        print(f"  {sc}: {count} questions")
    print()

    # Sort by ID
    food.sort(key=lambda q: int(q['id'].split('_')[1]))

    # Update data
    data['categories']['Food'] = food

    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Food category reorganized from 10 to {len(new_subcats)} subcategories")
    print(f"✅ Total questions: {len(food)}")

if __name__ == "__main__":
    main()
