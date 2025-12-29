#!/usr/bin/env python3
"""Add 65 Animation questions to reach 75 total (ent_107 to ent_171)"""
import json

new_questions = [
    # EASY QUESTIONS (22 total)
    {
        "id": "ent_107",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of Simba's father in The Lion King?",
        "options": ["Mufasa", "Scar", "Rafiki", "Zazu"],
        "correct_answer": "Mufasa",
        "difficulty": "easy"
    },
    {
        "id": "ent_108",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is Elsa's power in Frozen?",
        "options": ["Ice and snow", "Fire", "Lightning", "Water"],
        "correct_answer": "Ice and snow",
        "difficulty": "easy"
    },
    {
        "id": "ent_109",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the ogre in Shrek?",
        "options": ["Shrek", "Donkey", "Fiona", "Farquaad"],
        "correct_answer": "Shrek",
        "difficulty": "easy"
    },
    {
        "id": "ent_110",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the demigod in Moana?",
        "options": ["Maui", "Tamatoa", "Tui", "Sina"],
        "correct_answer": "Maui",
        "difficulty": "easy"
    },
    {
        "id": "ent_111",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What does Aladdin use to fly?",
        "options": ["Magic carpet", "Magic lamp", "Flying carpet", "Genie"],
        "correct_answer": "Magic carpet",
        "difficulty": "easy"
    },
    {
        "id": "ent_112",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the villain in The Little Mermaid?",
        "options": ["Ursula", "Maleficent", "Cruella", "Jafar"],
        "correct_answer": "Ursula",
        "difficulty": "easy"
    },
    {
        "id": "ent_113",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the panda in Kung Fu Panda?",
        "options": ["Po", "Shifu", "Tigress", "Tai Lung"],
        "correct_answer": "Po",
        "difficulty": "easy"
    },
    {
        "id": "ent_114",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the dragon in How to Train Your Dragon?",
        "options": ["Toothless", "Hiccup", "Astrid", "Stormfly"],
        "correct_answer": "Toothless",
        "difficulty": "easy"
    },
    {
        "id": "ent_115",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "Who is the villain in Despicable Me?",
        "options": ["Vector", "Gru", "El Macho", "Balthazar Bratt"],
        "correct_answer": "Vector",
        "difficulty": "easy"
    },
    {
        "id": "ent_116",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What color are the Minions?",
        "options": ["Yellow", "Blue", "Green", "Orange"],
        "correct_answer": "Yellow",
        "difficulty": "easy"
    },
    {
        "id": "ent_117",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the princess in Beauty and the Beast?",
        "options": ["Belle", "Ariel", "Jasmine", "Rapunzel"],
        "correct_answer": "Belle",
        "difficulty": "easy"
    },
    {
        "id": "ent_118",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What animal is Remy in Ratatouille?",
        "options": ["Rat", "Mouse", "Chef", "Cat"],
        "correct_answer": "Rat",
        "difficulty": "easy"
    },
    {
        "id": "ent_119",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the house that floats in Up?",
        "options": ["Carl's house", "Ellie's house", "Paradise Falls house", "Balloon house"],
        "correct_answer": "Carl's house",
        "difficulty": "easy"
    },
    {
        "id": "ent_120",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the cowboy in Toy Story?",
        "options": ["Woody", "Buzz", "Rex", "Andy"],
        "correct_answer": "Woody",
        "difficulty": "easy"
    },
    {
        "id": "ent_121",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the princess with long magical hair?",
        "options": ["Rapunzel", "Elsa", "Anna", "Merida"],
        "correct_answer": "Rapunzel",
        "difficulty": "easy"
    },
    {
        "id": "ent_122",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What type of animal is Bambi?",
        "options": ["Deer", "Rabbit", "Fox", "Bear"],
        "correct_answer": "Deer",
        "difficulty": "easy"
    },
    {
        "id": "ent_123",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the forgetful fish in Finding Nemo?",
        "options": ["Dory", "Nemo", "Marlin", "Bruce"],
        "correct_answer": "Dory",
        "difficulty": "easy"
    },
    {
        "id": "ent_124",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the race car in Cars?",
        "options": ["Lightning McQueen", "Mater", "Sally", "Doc Hudson"],
        "correct_answer": "Lightning McQueen",
        "difficulty": "easy"
    },
    {
        "id": "ent_125",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "Who is the villain in Tangled?",
        "options": ["Mother Gothel", "Maleficent", "Ursula", "Cruella"],
        "correct_answer": "Mother Gothel",
        "difficulty": "easy"
    },
    {
        "id": "ent_126",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the elephant with big ears?",
        "options": ["Dumbo", "Jumbo", "Ellie", "Horton"],
        "correct_answer": "Dumbo",
        "difficulty": "easy"
    },
    {
        "id": "ent_127",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the chef in Ratatouille that Remy helps?",
        "options": ["Linguini", "Colette", "Skinner", "Gusteau"],
        "correct_answer": "Linguini",
        "difficulty": "easy"
    },
    {
        "id": "ent_128",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of Mulan's dragon companion?",
        "options": ["Mushu", "Khan", "Cri-Kee", "Yao"],
        "correct_answer": "Mushu",
        "difficulty": "easy"
    },

    # MEDIUM QUESTIONS (26 total)
    {
        "id": "ent_129",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Spirited Away, what is the name of the bathhouse owner?",
        "options": ["Yubaba", "Zeniba", "Haku", "No-Face"],
        "correct_answer": "Yubaba",
        "difficulty": "medium"
    },
    {
        "id": "ent_130",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What year was the first Toy Story film released?",
        "options": ["1995", "1998", "1993", "2000"],
        "correct_answer": "1995",
        "difficulty": "medium"
    },
    {
        "id": "ent_131",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Frozen, what is the name of Kristoff's reindeer?",
        "options": ["Sven", "Olaf", "Hans", "Marshmallow"],
        "correct_answer": "Sven",
        "difficulty": "medium"
    },
    {
        "id": "ent_132",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the island in Moana?",
        "options": ["Motunui", "Te Fiti", "Lalotai", "Maui"],
        "correct_answer": "Motunui",
        "difficulty": "medium"
    },
    {
        "id": "ent_133",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In The Lion King, who is Simba's uncle?",
        "options": ["Scar", "Mufasa", "Rafiki", "Zazu"],
        "correct_answer": "Scar",
        "difficulty": "medium"
    },
    {
        "id": "ent_134",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the restaurant in Ratatouille?",
        "options": ["Gusteau's", "La Ratatouille", "Ego's", "The French Laundry"],
        "correct_answer": "Gusteau's",
        "difficulty": "medium"
    },
    {
        "id": "ent_135",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Shrek, what is the name of Lord Farquaad's kingdom?",
        "options": ["Duloc", "Far Far Away", "Camelot", "Shrekshire"],
        "correct_answer": "Duloc",
        "difficulty": "medium"
    },
    {
        "id": "ent_136",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "Who directed Spirited Away?",
        "options": ["Hayao Miyazaki", "Isao Takahata", "Mamoru Hosoda", "Makoto Shinkai"],
        "correct_answer": "Hayao Miyazaki",
        "difficulty": "medium"
    },
    {
        "id": "ent_137",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Up, what is the name of the boy scout?",
        "options": ["Russell", "Kevin", "Carl", "Charles"],
        "correct_answer": "Russell",
        "difficulty": "medium"
    },
    {
        "id": "ent_138",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the chef that Linguini admires in Ratatouille?",
        "options": ["Auguste Gusteau", "Anton Ego", "Chef Skinner", "Colette Tatou"],
        "correct_answer": "Auguste Gusteau",
        "difficulty": "medium"
    },
    {
        "id": "ent_139",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Kung Fu Panda, what is the name of Po's master?",
        "options": ["Master Shifu", "Master Oogway", "Tai Lung", "Tigress"],
        "correct_answer": "Master Shifu",
        "difficulty": "medium"
    },
    {
        "id": "ent_140",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the city in Big Hero 6?",
        "options": ["San Fransokyo", "Tokyo", "San Francisco", "Neo Tokyo"],
        "correct_answer": "San Fransokyo",
        "difficulty": "medium"
    },
    {
        "id": "ent_141",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In How to Train Your Dragon, what is Hiccup's last name?",
        "options": ["Haddock", "Hofferson", "Jorgenson", "Ingerman"],
        "correct_answer": "Haddock",
        "difficulty": "medium"
    },
    {
        "id": "ent_142",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the villain in Aladdin?",
        "options": ["Jafar", "Iago", "Razoul", "Cassim"],
        "correct_answer": "Jafar",
        "difficulty": "medium"
    },
    {
        "id": "ent_143",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Wall-E, what is the name of the plant that Wall-E finds?",
        "options": ["A seedling", "An orchid", "A fern", "A rose"],
        "correct_answer": "A seedling",
        "difficulty": "medium"
    },
    {
        "id": "ent_144",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the kingdom in Tangled?",
        "options": ["Corona", "Arendelle", "DunBroch", "Agrabah"],
        "correct_answer": "Corona",
        "difficulty": "medium"
    },
    {
        "id": "ent_145",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Coco, what is the name of Miguel's idol?",
        "options": ["Ernesto de la Cruz", "Héctor", "Chicharrón", "Papá Julio"],
        "correct_answer": "Ernesto de la Cruz",
        "difficulty": "medium"
    },
    {
        "id": "ent_146",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What studio produced Spirited Away?",
        "options": ["Studio Ghibli", "Toei Animation", "Madhouse", "Kyoto Animation"],
        "correct_answer": "Studio Ghibli",
        "difficulty": "medium"
    },
    {
        "id": "ent_147",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In The Incredibles, what is Dash's superpower?",
        "options": ["Super speed", "Super strength", "Invisibility", "Elasticity"],
        "correct_answer": "Super speed",
        "difficulty": "medium"
    },
    {
        "id": "ent_148",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the villain in Sleeping Beauty?",
        "options": ["Maleficent", "Ursula", "Cruella", "Queen Grimhilde"],
        "correct_answer": "Maleficent",
        "difficulty": "medium"
    },
    {
        "id": "ent_149",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Zootopia, what is Judy Hopps' job?",
        "options": ["Police officer", "Meter maid", "Detective", "Mayor"],
        "correct_answer": "Police officer",
        "difficulty": "medium"
    },
    {
        "id": "ent_150",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the demigod's hook in Moana?",
        "options": ["Maui's fishhook", "The Heart of Te Fiti", "Tamatoa's treasure", "The Ocean's Gift"],
        "correct_answer": "Maui's fishhook",
        "difficulty": "medium"
    },
    {
        "id": "ent_151",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Mulan, what is the name of the matchmaker's assistant?",
        "options": ["Grandmother Fa", "The Emperor", "Chi-Fu", "None of the above"],
        "correct_answer": "None of the above",
        "difficulty": "medium"
    },
    {
        "id": "ent_152",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What year did Frozen win the Academy Award for Best Animated Feature?",
        "options": ["2014", "2013", "2015", "2012"],
        "correct_answer": "2014",
        "difficulty": "medium"
    },
    {
        "id": "ent_153",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Spider-Man: Into the Spider-Verse, what is Miles Morales' superhero name?",
        "options": ["Spider-Man", "Kid Arachnid", "Spin", "Web-Slinger"],
        "correct_answer": "Spider-Man",
        "difficulty": "medium"
    },
    {
        "id": "ent_154",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the food critic in Ratatouille?",
        "options": ["Anton Ego", "Auguste Gusteau", "Chef Skinner", "Colette"],
        "correct_answer": "Anton Ego",
        "difficulty": "medium"
    },

    # HARD QUESTIONS (17 total)
    {
        "id": "ent_155",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Spirited Away, what is Chihiro's new name given by Yubaba?",
        "options": ["Sen", "Lin", "Kamaji", "Boh"],
        "correct_answer": "Sen",
        "difficulty": "hard"
    },
    {
        "id": "ent_156",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the villain in Kung Fu Panda 2?",
        "options": ["Lord Shen", "Tai Lung", "Kai", "Master Shifu"],
        "correct_answer": "Lord Shen",
        "difficulty": "hard"
    },
    {
        "id": "ent_157",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In The Lion King, what does 'Hakuna Matata' mean?",
        "options": ["No worries", "Circle of life", "Be prepared", "Long live the king"],
        "correct_answer": "No worries",
        "difficulty": "hard"
    },
    {
        "id": "ent_158",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the kingdom in Frozen?",
        "options": ["Arendelle", "Corona", "DunBroch", "Atlantica"],
        "correct_answer": "Arendelle",
        "difficulty": "hard"
    },
    {
        "id": "ent_159",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Up, what is the name of the bird that Russell befriends?",
        "options": ["Kevin", "Russell", "Doug", "Alpha"],
        "correct_answer": "Kevin",
        "difficulty": "hard"
    },
    {
        "id": "ent_160",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the crab who collects treasures in Moana?",
        "options": ["Tamatoa", "Maui", "Heihei", "Pua"],
        "correct_answer": "Tamatoa",
        "difficulty": "hard"
    },
    {
        "id": "ent_161",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In How to Train Your Dragon, what type of dragon is Toothless?",
        "options": ["Night Fury", "Deadly Nadder", "Gronckle", "Monstrous Nightmare"],
        "correct_answer": "Night Fury",
        "difficulty": "hard"
    },
    {
        "id": "ent_162",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the emotion headquarters in Inside Out?",
        "options": ["Headquarters", "Mind Palace", "Brain Center", "Emotion Station"],
        "correct_answer": "Headquarters",
        "difficulty": "hard"
    },
    {
        "id": "ent_163",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Coco, what instrument does Miguel play?",
        "options": ["Guitar", "Violin", "Trumpet", "Piano"],
        "correct_answer": "Guitar",
        "difficulty": "hard"
    },
    {
        "id": "ent_164",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the ant colony's princess in A Bug's Life?",
        "options": ["Atta", "Dot", "Rosie", "Gypsy"],
        "correct_answer": "Atta",
        "difficulty": "hard"
    },
    {
        "id": "ent_165",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Zootopia, what is the name of the disease affecting predators?",
        "options": ["Night Howler serum", "Savage syndrome", "Wild disease", "Predator plague"],
        "correct_answer": "Night Howler serum",
        "difficulty": "hard"
    },
    {
        "id": "ent_166",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the first Pixar short film?",
        "options": ["The Adventures of André and Wally B.", "Luxo Jr.", "Tin Toy", "Knick Knack"],
        "correct_answer": "The Adventures of André and Wally B.",
        "difficulty": "hard"
    },
    {
        "id": "ent_167",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Tangled, what is Flynn Rider's real name?",
        "options": ["Eugene Fitzherbert", "Eugene Rider", "Flynn Eugene", "Eugene Flynn"],
        "correct_answer": "Eugene Fitzherbert",
        "difficulty": "hard"
    },
    {
        "id": "ent_168",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the villain in Big Hero 6?",
        "options": ["Yokai", "Callaghan", "Krei", "Tadashi"],
        "correct_answer": "Yokai",
        "difficulty": "hard"
    },
    {
        "id": "ent_169",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In Ratatouille, what is the name of the motto 'Anyone Can Cook' associated with?",
        "options": ["Auguste Gusteau", "Anton Ego", "Chef Skinner", "Colette"],
        "correct_answer": "Auguste Gusteau",
        "difficulty": "hard"
    },
    {
        "id": "ent_170",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "What is the name of the villain in The Emperor's New Groove?",
        "options": ["Yzma", "Kronk", "Pacha", "Kuzco"],
        "correct_answer": "Yzma",
        "difficulty": "hard"
    },
    {
        "id": "ent_171",
        "category": "Entertainment",
        "subcategory": "Animation",
        "question": "In My Neighbor Totoro, what vegetables do Satsuki and Mei grow?",
        "options": ["Corn", "Cucumbers", "Tomatoes", "Radishes"],
        "correct_answer": "Corn",
        "difficulty": "hard"
    }
]

def add_animation_questions():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    # Add new questions
    data['categories']['Entertainment'].extend(new_questions)

    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Added {len(new_questions)} Animation questions")
    print(f"   Easy: {sum(1 for q in new_questions if q['difficulty'] == 'easy')}")
    print(f"   Medium: {sum(1 for q in new_questions if q['difficulty'] == 'medium')}")
    print(f"   Hard: {sum(1 for q in new_questions if q['difficulty'] == 'hard')}")
    print(f"\n📊 Animation now has 75 total questions (10 → 75)")

if __name__ == '__main__':
    add_animation_questions()
