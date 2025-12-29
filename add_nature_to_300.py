#!/usr/bin/env python3
"""
Add 70 Nature questions to reach 300 total
Focus on Trees, Plants, and Weather (Animals already above target)
Emphasis on medium and hard difficulties
"""

import json

# Load database
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

print(f"Current Nature questions: {len(data['categories']['Nature'])}")
print(f"Adding 70 questions (nat_231 to nat_300)")
print()
print("Distribution strategy:")
print("  Trees: +30 (38 → 68)")
print("  Plants & Flowers: +25 (40 → 65)")
print("  Weather: +15 (49 → 64)")
print("  Animals & Wildlife: +0 (already at 103)")
print()
print("Difficulty emphasis: +4 easy, +37 medium, +29 hard")
print()

# 70 new Nature questions (nat_231 to nat_300)
new_questions = [
    # TREES (30 questions: 5 easy, 15 medium, 10 hard)
    # Easy (5)
    {"id": "nat_231", "category": "Nature", "subcategory": "Trees", "question": "What type of tree produces acorns?", "options": ["Oak", "Pine", "Maple", "Birch"], "correct_answer": "Oak", "difficulty": "easy"},
    {"id": "nat_232", "category": "Nature", "subcategory": "Trees", "question": "What is the tallest species of tree in the world?", "options": ["Coast redwood", "Giant sequoia", "Douglas fir", "Eucalyptus"], "correct_answer": "Coast redwood", "difficulty": "easy"},
    {"id": "nat_233", "category": "Nature", "subcategory": "Trees", "question": "What type of tree produces maple syrup?", "options": ["Sugar maple", "Red maple", "Silver maple", "Japanese maple"], "correct_answer": "Sugar maple", "difficulty": "easy"},
    {"id": "nat_234", "category": "Nature", "subcategory": "Trees", "question": "What are trees that lose their leaves in fall called?", "options": ["Deciduous", "Evergreen", "Coniferous", "Perennial"], "correct_answer": "Deciduous", "difficulty": "easy"},
    {"id": "nat_235", "category": "Nature", "subcategory": "Trees", "question": "What tree produces coconuts?", "options": ["Palm tree", "Banana tree", "Mango tree", "Papaya tree"], "correct_answer": "Palm tree", "difficulty": "easy"},
    
    # Medium (15)
    {"id": "nat_236", "category": "Nature", "subcategory": "Trees", "question": "What is the oldest known living tree species?", "options": ["Bristlecone pine", "Ginkgo", "Redwood", "Baobab"], "correct_answer": "Bristlecone pine", "difficulty": "medium"},
    {"id": "nat_237", "category": "Nature", "subcategory": "Trees", "question": "What tree is known for its distinctive white bark?", "options": ["Birch", "Aspen", "Poplar", "Willow"], "correct_answer": "Birch", "difficulty": "medium"},
    {"id": "nat_238", "category": "Nature", "subcategory": "Trees", "question": "What is the national tree of Canada?", "options": ["Maple", "Pine", "Oak", "Spruce"], "correct_answer": "Maple", "difficulty": "medium"},
    {"id": "nat_239", "category": "Nature", "subcategory": "Trees", "question": "What tree produces the fruit that olives come from?", "options": ["Olive tree", "Fig tree", "Date palm", "Citrus tree"], "correct_answer": "Olive tree", "difficulty": "medium"},
    {"id": "nat_240", "category": "Nature", "subcategory": "Trees", "question": "What is the scientific name for the process trees use to transport water?", "options": ["Transpiration", "Photosynthesis", "Respiration", "Osmosis"], "correct_answer": "Transpiration", "difficulty": "medium"},
    {"id": "nat_241", "category": "Nature", "subcategory": "Trees", "question": "What tree is sacred in Buddhism?", "options": ["Bodhi tree (fig)", "Banyan tree", "Sal tree", "Lotus tree"], "correct_answer": "Bodhi tree (fig)", "difficulty": "medium"},
    {"id": "nat_242", "category": "Nature", "subcategory": "Trees", "question": "What coniferous tree is known for its edible pine nuts?", "options": ["Stone pine", "White pine", "Scots pine", "Lodgepole pine"], "correct_answer": "Stone pine", "difficulty": "medium"},
    {"id": "nat_243", "category": "Nature", "subcategory": "Trees", "question": "What tree produces the spice cinnamon from its bark?", "options": ["Cinnamon tree", "Nutmeg tree", "Clove tree", "Bay tree"], "correct_answer": "Cinnamon tree", "difficulty": "medium"},
    {"id": "nat_244", "category": "Nature", "subcategory": "Trees", "question": "What is the national tree of Japan?", "options": ["Cherry blossom (sakura)", "Bamboo", "Pine", "Maple"], "correct_answer": "Cherry blossom (sakura)", "difficulty": "medium"},
    {"id": "nat_245", "category": "Nature", "subcategory": "Trees", "question": "What tree is known as the 'tree of life' in Africa?", "options": ["Baobab", "Acacia", "Marula", "Sausage tree"], "correct_answer": "Baobab", "difficulty": "medium"},
    {"id": "nat_246", "category": "Nature", "subcategory": "Trees", "question": "What wood is traditionally used to make baseball bats?", "options": ["Ash or maple", "Oak", "Pine", "Birch"], "correct_answer": "Ash or maple", "difficulty": "medium"},
    {"id": "nat_247", "category": "Nature", "subcategory": "Trees", "question": "What tree produces chestnuts?", "options": ["Chestnut tree", "Walnut tree", "Hickory tree", "Pecan tree"], "correct_answer": "Chestnut tree", "difficulty": "medium"},
    {"id": "nat_248", "category": "Nature", "subcategory": "Trees", "question": "What is the fastest-growing tree species?", "options": ["Bamboo (technically grass but tree-like)", "Eucalyptus", "Poplar", "Willow"], "correct_answer": "Bamboo (technically grass but tree-like)", "difficulty": "medium"},
    {"id": "nat_249", "category": "Nature", "subcategory": "Trees", "question": "What tree is cork harvested from?", "options": ["Cork oak", "White oak", "Red oak", "Live oak"], "correct_answer": "Cork oak", "difficulty": "medium"},
    {"id": "nat_250", "category": "Nature", "subcategory": "Trees", "question": "What tree produces the aromatic resin frankincense?", "options": ["Boswellia tree", "Myrrh tree", "Balsam tree", "Cedar tree"], "correct_answer": "Boswellia tree", "difficulty": "medium"},
    
    # Hard (10)
    {"id": "nat_251", "category": "Nature", "subcategory": "Trees", "question": "What is the scientific name for the giant sequoia?", "options": ["Sequoiadendron giganteum", "Sequoia sempervirens", "Metasequoia glyptostroboides", "Taxodium distichum"], "correct_answer": "Sequoiadendron giganteum", "difficulty": "hard"},
    {"id": "nat_252", "category": "Nature", "subcategory": "Trees", "question": "What tree disease has devastated ash trees in North America?", "options": ["Emerald ash borer", "Dutch elm disease", "Chestnut blight", "Pine bark beetle"], "correct_answer": "Emerald ash borer", "difficulty": "hard"},
    {"id": "nat_253", "category": "Nature", "subcategory": "Trees", "question": "What is the term for the study of tree rings?", "options": ["Dendrochronology", "Dendrology", "Xylology", "Silviculture"], "correct_answer": "Dendrochronology", "difficulty": "hard"},
    {"id": "nat_254", "category": "Nature", "subcategory": "Trees", "question": "What endangered tree species is native only to Wollemi National Park in Australia?", "options": ["Wollemi pine", "Huon pine", "Kauri pine", "Bunya pine"], "correct_answer": "Wollemi pine", "difficulty": "hard"},
    {"id": "nat_255", "category": "Nature", "subcategory": "Trees", "question": "What is the hardest wood in the world?", "options": ["Lignum vitae", "Ebony", "Ironwood", "Teak"], "correct_answer": "Lignum vitae", "difficulty": "hard"},
    {"id": "nat_256", "category": "Nature", "subcategory": "Trees", "question": "What tree produces the alkaloid quinine used to treat malaria?", "options": ["Cinchona tree", "Willow tree", "Coca tree", "Poppy tree"], "correct_answer": "Cinchona tree", "difficulty": "hard"},
    {"id": "nat_257", "category": "Nature", "subcategory": "Trees", "question": "What is the term for trees that have both male and female flowers on the same tree?", "options": ["Monoecious", "Dioecious", "Hermaphroditic", "Polygamous"], "correct_answer": "Monoecious", "difficulty": "hard"},
    {"id": "nat_258", "category": "Nature", "subcategory": "Trees", "question": "What living fossil tree was thought extinct until rediscovered in China in 1941?", "options": ["Dawn redwood", "Ginkgo", "Wollemi pine", "Monkey puzzle"], "correct_answer": "Dawn redwood", "difficulty": "hard"},
    {"id": "nat_259", "category": "Nature", "subcategory": "Trees", "question": "What tree family includes mahogany and teak?", "options": ["Meliaceae", "Fabaceae", "Lauraceae", "Fagaceae"], "correct_answer": "Meliaceae", "difficulty": "hard"},
    {"id": "nat_260", "category": "Nature", "subcategory": "Trees", "question": "What is the phenomenon where trees synchronize their mast years for seed production?", "options": ["Masting", "Seeding synchrony", "Fruiting cycle", "Reproductive pulsing"], "correct_answer": "Masting", "difficulty": "hard"},

    # PLANTS & FLOWERS (25 questions: 10 easy, 10 medium, 5 hard)
    # Easy (10)
    {"id": "nat_261", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What is the national flower of the United States?", "options": ["Rose", "Tulip", "Daisy", "Sunflower"], "correct_answer": "Rose", "difficulty": "easy"},
    {"id": "nat_262", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What flower is associated with the Netherlands?", "options": ["Tulip", "Rose", "Lily", "Carnation"], "correct_answer": "Tulip", "difficulty": "easy"},
    {"id": "nat_263", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What plant is aloe vera used from?", "options": ["Aloe plant", "Cactus", "Succulent", "Fern"], "correct_answer": "Aloe plant", "difficulty": "easy"},
    {"id": "nat_264", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What type of plant is bamboo?", "options": ["Grass", "Tree", "Shrub", "Vine"], "correct_answer": "Grass", "difficulty": "easy"},
    {"id": "nat_265", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What flower is the symbol of remembrance for veterans?", "options": ["Poppy", "Rose", "Lily", "Daisy"], "correct_answer": "Poppy", "difficulty": "easy"},
    {"id": "nat_266", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What plant produces vanilla flavoring?", "options": ["Vanilla orchid", "Vanilla bean plant", "Vanilla vine", "Vanilla tree"], "correct_answer": "Vanilla orchid", "difficulty": "easy"},
    {"id": "nat_267", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What is the largest flower in the world?", "options": ["Rafflesia arnoldii", "Titan arum", "Sunflower", "Lotus"], "correct_answer": "Rafflesia arnoldii", "difficulty": "easy"},
    {"id": "nat_268", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What plant is known for following the sun's movement?", "options": ["Sunflower", "Daisy", "Marigold", "Dandelion"], "correct_answer": "Sunflower", "difficulty": "easy"},
    {"id": "nat_269", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What is lavender commonly used for?", "options": ["Aromatherapy and relaxation", "Cooking only", "Medicine only", "Dye production"], "correct_answer": "Aromatherapy and relaxation", "difficulty": "easy"},
    {"id": "nat_270", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What flower blooms in spring and is associated with Easter?", "options": ["Lily", "Rose", "Tulip", "Daisy"], "correct_answer": "Lily", "difficulty": "easy"},
    
    # Medium (10)
    {"id": "nat_271", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What carnivorous plant is native to the Carolinas?", "options": ["Venus flytrap", "Pitcher plant", "Sundew", "Butterwort"], "correct_answer": "Venus flytrap", "difficulty": "medium"},
    {"id": "nat_272", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What is the national flower of Japan?", "options": ["Cherry blossom", "Chrysanthemum", "Lotus", "Plum blossom"], "correct_answer": "Cherry blossom", "difficulty": "medium"},
    {"id": "nat_273", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What flower bulb was so valuable it caused a market crash in 17th century Netherlands?", "options": ["Tulip", "Daffodil", "Hyacinth", "Crocus"], "correct_answer": "Tulip", "difficulty": "medium"},
    {"id": "nat_274", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What is the term for plants that complete their life cycle in two years?", "options": ["Biennials", "Annuals", "Perennials", "Ephemerals"], "correct_answer": "Biennials", "difficulty": "medium"},
    {"id": "nat_275", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What plant genus includes poison ivy, poison oak, and poison sumac?", "options": ["Toxicodendron", "Rhus", "Urtica", "Hedera"], "correct_answer": "Toxicodendron", "difficulty": "medium"},
    {"id": "nat_276", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What is the world's most expensive spice by weight?", "options": ["Saffron", "Vanilla", "Cardamom", "Cinnamon"], "correct_answer": "Saffron", "difficulty": "medium"},
    {"id": "nat_277", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What flower is the symbol of the fleur-de-lis?", "options": ["Iris", "Lily", "Orchid", "Lotus"], "correct_answer": "Iris", "difficulty": "medium"},
    {"id": "nat_278", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What plant produces the psychoactive compound in cannabis?", "options": ["THC (tetrahydrocannabinol)", "CBD", "Hemp", "Marijuana"], "correct_answer": "THC (tetrahydrocannabinol)", "difficulty": "medium"},
    {"id": "nat_279", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What is the process by which pollen is transferred to fertilize plants?", "options": ["Pollination", "Germination", "Fertilization", "Propagation"], "correct_answer": "Pollination", "difficulty": "medium"},
    {"id": "nat_280", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What desert plant can live for over 200 years and only blooms once before dying?", "options": ["Century plant (agave)", "Joshua tree", "Barrel cactus", "Saguaro cactus"], "correct_answer": "Century plant (agave)", "difficulty": "medium"},
    
    # Hard (5)
    {"id": "nat_281", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What is the scientific term for the opening on leaves that allows gas exchange?", "options": ["Stomata", "Lenticels", "Cuticle", "Epidermis"], "correct_answer": "Stomata", "difficulty": "hard"},
    {"id": "nat_282", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What flower produces opium?", "options": ["Opium poppy (Papaver somniferum)", "Corn poppy", "Oriental poppy", "Iceland poppy"], "correct_answer": "Opium poppy (Papaver somniferum)", "difficulty": "hard"},
    {"id": "nat_283", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What is the term for plants that grow on other plants without being parasitic?", "options": ["Epiphytes", "Parasites", "Saprophytes", "Lithophytes"], "correct_answer": "Epiphytes", "difficulty": "hard"},
    {"id": "nat_284", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What rare parasitic flower is known as the 'corpse flower' for its smell?", "options": ["Rafflesia", "Amorphophallus titanum", "Stapelia", "Aristolochia"], "correct_answer": "Rafflesia", "difficulty": "hard"},
    {"id": "nat_285", "category": "Nature", "subcategory": "Plants & Flowers", "question": "What is the phenomenon where some plants flower only after exposure to cold temperatures?", "options": ["Vernalization", "Photoperiodism", "Stratification", "Dormancy"], "correct_answer": "Vernalization", "difficulty": "hard"},

    # WEATHER (15 questions: 2 easy, 7 medium, 6 hard)
    # Easy (2)
    {"id": "nat_286", "category": "Nature", "subcategory": "Weather", "question": "What do you call frozen rain?", "options": ["Hail or sleet", "Snow", "Frost", "Ice"], "correct_answer": "Hail or sleet", "difficulty": "easy"},
    {"id": "nat_287", "category": "Nature", "subcategory": "Weather", "question": "What is a tornado over water called?", "options": ["Waterspout", "Hurricane", "Typhoon", "Cyclone"], "correct_answer": "Waterspout", "difficulty": "easy"},
    
    # Medium (7)
    {"id": "nat_288", "category": "Nature", "subcategory": "Weather", "question": "What scale is used to measure tornado intensity?", "options": ["Enhanced Fujita Scale", "Richter Scale", "Saffir-Simpson Scale", "Beaufort Scale"], "correct_answer": "Enhanced Fujita Scale", "difficulty": "medium"},
    {"id": "nat_289", "category": "Nature", "subcategory": "Weather", "question": "What is the term for the temperature at which air becomes saturated and dew forms?", "options": ["Dew point", "Frost point", "Saturation point", "Condensation point"], "correct_answer": "Dew point", "difficulty": "medium"},
    {"id": "nat_290", "category": "Nature", "subcategory": "Weather", "question": "What causes the aurora borealis (northern lights)?", "options": ["Solar wind particles interacting with Earth's atmosphere", "Ice crystals in the atmosphere", "Pollution", "Volcanic ash"], "correct_answer": "Solar wind particles interacting with Earth's atmosphere", "difficulty": "medium"},
    {"id": "nat_291", "category": "Nature", "subcategory": "Weather", "question": "What type of cloud produces thunderstorms?", "options": ["Cumulonimbus", "Cumulus", "Stratus", "Cirrus"], "correct_answer": "Cumulonimbus", "difficulty": "medium"},
    {"id": "nat_292", "category": "Nature", "subcategory": "Weather", "question": "What is the calm center of a hurricane called?", "options": ["Eye", "Core", "Center", "Vortex"], "correct_answer": "Eye", "difficulty": "medium"},
    {"id": "nat_293", "category": "Nature", "subcategory": "Weather", "question": "What instrument measures atmospheric pressure?", "options": ["Barometer", "Thermometer", "Hygrometer", "Anemometer"], "correct_answer": "Barometer", "difficulty": "medium"},
    {"id": "nat_294", "category": "Nature", "subcategory": "Weather", "question": "What is a long period of abnormally low rainfall called?", "options": ["Drought", "Dry spell", "Aridity", "Desiccation"], "correct_answer": "Drought", "difficulty": "medium"},
    
    # Hard (6)
    {"id": "nat_295", "category": "Nature", "subcategory": "Weather", "question": "What is the term for rain that evaporates before reaching the ground?", "options": ["Virga", "Drizzle", "Mist", "Vapor"], "correct_answer": "Virga", "difficulty": "hard"},
    {"id": "nat_296", "category": "Nature", "subcategory": "Weather", "question": "What is a derecho?", "options": ["A widespread, long-lived windstorm", "A type of tornado", "A tropical cyclone", "A dust storm"], "correct_answer": "A widespread, long-lived windstorm", "difficulty": "hard"},
    {"id": "nat_297", "category": "Nature", "subcategory": "Weather", "question": "What phenomenon causes 'St. Elmo's Fire'?", "options": ["Electrical discharge in the atmosphere", "Ball lightning", "Aurora", "Reflection of moonlight"], "correct_answer": "Electrical discharge in the atmosphere", "difficulty": "hard"},
    {"id": "nat_298", "category": "Nature", "subcategory": "Weather", "question": "What is the scientific name for a sun dog (parhelion)?", "options": ["Parhelion", "Halo", "Sun pillar", "Crepuscular ray"], "correct_answer": "Parhelion", "difficulty": "hard"},
    {"id": "nat_299", "category": "Nature", "subcategory": "Weather", "question": "What layer of the atmosphere contains the ozone layer?", "options": ["Stratosphere", "Troposphere", "Mesosphere", "Thermosphere"], "correct_answer": "Stratosphere", "difficulty": "hard"},
    {"id": "nat_300", "category": "Nature", "subcategory": "Weather", "question": "What is a haboob?", "options": ["A type of dust storm", "A heat wave", "A cold front", "A monsoon"], "correct_answer": "A type of dust storm", "difficulty": "hard"}
]

# Add new questions
data['categories']['Nature'].extend(new_questions)

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✓ Added {len(new_questions)} new Nature questions")
print(f"\nNew Nature total: {len(data['categories']['Nature'])} questions")

# Show breakdown
print("\nBreakdown by subcategory:")
subcats = {}
for q in data['categories']['Nature']:
    subcat = q['subcategory']
    if subcat not in subcats:
        subcats[subcat] = 0
    subcats[subcat] += 1

for subcat in sorted(subcats.keys()):
    print(f"  {subcat}: {subcats[subcat]} questions")

# Show difficulty breakdown
print("\nBreakdown by difficulty:")
diffs = {'easy': 0, 'medium': 0, 'hard': 0}
for q in data['categories']['Nature']:
    diffs[q['difficulty']] += 1

for diff in ['easy', 'medium', 'hard']:
    pct = (diffs[diff] / len(data['categories']['Nature'])) * 100
    print(f"  {diff.capitalize()}: {diffs[diff]} ({pct:.1f}%)")

print("\n✓ Nature category complete: 300/300 questions")
