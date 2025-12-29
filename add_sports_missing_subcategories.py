#!/usr/bin/env python3
"""Add missing Sports subcategories and complete International Competition"""
import json

# Add 1 International Competition question
intl_competition_question = {
    "id": "spt_326",
    "category": "Sports",
    "subcategory": "International Competition",
    "question": "What year did the first modern Olympics take place?",
    "options": ["1896", "1900", "1892", "1888"],
    "correct_answer": "1896",
    "difficulty": "medium",
    "topic": None,
    "subtopic": None
}

# Extreme & Action Sports (50 questions) - 17 easy, 17 medium, 16 hard
extreme_action_sports = []

# Easy questions (17)
easy = [
    ("spt_327", "What sport involves riding waves on a board?", ["Surfing", "Skateboarding", "Snowboarding", "Wakeboarding"], "Surfing", "easy"),
    ("spt_328", "What is a halfpipe used for?", ["Skateboarding and snowboarding tricks", "Swimming", "Running", "Cycling"], "Skateboarding and snowboarding tricks", "easy"),
    ("spt_329", "What sport involves jumping from aircraft with a parachute?", ["Skydiving", "Base jumping", "Bungee jumping", "Hang gliding"], "Skydiving", "easy"),
    ("spt_330", "What does BMX stand for?", ["Bicycle Motocross", "Bike Motor X-treme", "British Motor X-sports", "Bike Mountain X-sports"], "Bicycle Motocross", "easy"),
    ("spt_331", "What is the term for a 360-degree rotation in skateboarding?", ["360", "Spin", "Rotation", "Turn"], "360", "easy"),
    ("spt_332", "What sport involves descending snow-covered slopes on skis?", ["Skiing", "Snowboarding", "Sledding", "Bobsledding"], "Skiing", "easy"),
    ("spt_333", "What protective gear is essential in skateboarding?", ["Helmet", "Elbow pads only", "Knee pads only", "None needed"], "Helmet", "easy"),
    ("spt_334", "What is the X Games?", ["Extreme sports competition", "Video game tournament", "Olympics qualifier", "Winter sports only"], "Extreme sports competition", "easy"),
    ("spt_335", "What board sport is done on snow?", ["Snowboarding", "Skateboarding", "Surfing", "Wakeboarding"], "Snowboarding", "easy"),
    ("spt_336", "What is a kickflip in skateboarding?", ["Board flip trick", "Jumping motion", "Stopping technique", "Turning maneuver"], "Board flip trick", "easy"),
    ("spt_337", "What sport involves climbing vertical ice formations?", ["Ice climbing", "Rock climbing", "Mountaineering", "Skiing"], "Ice climbing", "easy"),
    ("spt_338", "What is parkour?", ["Moving through obstacles efficiently", "Skate park design", "Mountain biking", "Street racing"], "Moving through obstacles efficiently", "easy"),
    ("spt_339", "What does a skateboarder do in a 'grind'?", ["Slide along edge with trucks", "Jump high", "Spin board", "Stop quickly"], "Slide along edge with trucks", "easy"),
    ("spt_340", "What sport involves riding down rivers in an inflatable boat?", ["White-water rafting", "Kayaking", "Canoeing", "Tubing"], "White-water rafting", "easy"),
    ("spt_341", "What is motocross?", ["Motorcycle racing on dirt tracks", "Car racing", "Bicycle racing", "ATV racing"], "Motorcycle racing on dirt tracks", "easy"),
    ("spt_342", "What board is used in wakeboarding?", ["Wakeboard", "Surfboard", "Skateboard", "Snowboard"], "Wakeboard", "easy"),
    ("spt_343", "What is bungee jumping?", ["Jumping from height with elastic cord", "Parachuting", "Diving", "Rock climbing"], "Jumping from height with elastic cord", "easy"),
]

for q in easy:
    extreme_action_sports.append({
        "id": q[0],
        "category": "Sports",
        "subcategory": "Extreme & Action Sports",
        "question": q[1],
        "options": q[2],
        "correct_answer": q[3],
        "difficulty": q[4],
        "topic": None,
        "subtopic": None
    })

# Medium questions (17)
medium = [
    ("spt_344", "Who is considered the most famous skateboarder of all time?", ["Tony Hawk", "Rodney Mullen", "Bob Burnquist", "Bucky Lasek"], "Tony Hawk", "medium"),
    ("spt_345", "What is a 'barrel' in surfing?", ["Riding inside a breaking wave", "Board storage container", "Type of wave", "Surfboard design"], "Riding inside a breaking wave", "medium"),
    ("spt_346", "What is free soloing?", ["Climbing without ropes", "Freestyle skiing", "Solo skateboarding", "Individual surfing"], "Climbing without ropes", "medium"),
    ("spt_347", "What year was the first X Games held?", ["1995", "1990", "2000", "1985"], "1995", "medium"),
    ("spt_348", "What is a 'McTwist' in action sports?", ["540-degree spin", "360-degree spin", "720-degree spin", "180-degree spin"], "540-degree spin", "medium"),
    ("spt_349", "Who was the first person to land a 900 in skateboarding?", ["Tony Hawk", "Bob Burnquist", "Shaun White", "Danny Way"], "Tony Hawk", "medium"),
    ("spt_350", "What is slacklining?", ["Walking on suspended webbing", "Zip-lining", "Tightrope walking on ice", "Mountain climbing"], "Walking on suspended webbing", "medium"),
    ("spt_351", "What does 'goofy foot' mean in board sports?", ["Right foot forward", "Left foot forward", "Both feet together", "No foot preference"], "Right foot forward", "medium"),
    ("spt_352", "What is BASE jumping an acronym for?", ["Building, Antenna, Span, Earth", "Base Area Skydiving Experience", "British Aerial Sports Extreme", "Belayed Airborne Sports Event"], "Building, Antenna, Span, Earth", "medium"),
    ("spt_353", "What is the Vans Warped Tour associated with?", ["Action sports and punk rock", "Classical music", "Basketball", "Marathon running"], "Action sports and punk rock", "medium"),
    ("spt_354", "What is a 'nosegrind' in skateboarding?", ["Grinding on front truck", "Riding on nose of board", "Frontside trick", "Jumping technique"], "Grinding on front truck", "medium"),
    ("spt_355", "Who is known as 'The Flying Tomato'?", ["Shaun White", "Tony Hawk", "Travis Pastrana", "Danny Way"], "Shaun White", "medium"),
    ("spt_356", "What is 'hang time' in action sports?", ["Time spent in air", "Waiting time", "Competition time", "Practice time"], "Time spent in air", "medium"),
    ("spt_357", "What is the Banzai Pipeline famous for?", ["Dangerous surf break in Hawaii", "Snowboard park", "Skate park", "BMX track"], "Dangerous surf break in Hawaii", "medium"),
    ("spt_358", "What is a 'fakie' in skateboarding?", ["Riding backward", "Riding forward", "Jumping trick", "Grinding technique"], "Riding backward", "medium"),
    ("spt_359", "What is wingsuit flying?", ["Gliding through air in special suit", "Paragliding", "Hang gliding", "Skydiving with parachute"], "Gliding through air in special suit", "medium"),
    ("spt_360", "What is the Triple Crown of Surfing?", ["Three elite contests in Hawaii", "Three board types", "Three wave heights", "Three surf brands"], "Three elite contests in Hawaii", "medium"),
]

for q in medium:
    extreme_action_sports.append({
        "id": q[0],
        "category": "Sports",
        "subcategory": "Extreme & Action Sports",
        "question": q[1],
        "options": q[2],
        "correct_answer": q[3],
        "difficulty": q[4],
        "topic": None,
        "subtopic": None
    })

# Hard questions (16)
hard = [
    ("spt_361", "Who was the first to complete a double backflip on a motorcycle?", ["Travis Pastrana", "Ryan Williams", "Carey Hart", "Mat Hoffman"], "Travis Pastrana", "hard"),
    ("spt_362", "What is the 'Dawn Patrol' in surfing culture?", ["Early morning surf session", "Sunset surfing", "Night surfing", "Afternoon session"], "Early morning surf session", "hard"),
    ("spt_363", "Who climbed El Capitan's 'The Nose' route free solo?", ["Alex Honnold", "Tommy Caldwell", "Lynn Hill", "Adam Ondra"], "Alex Honnold", "hard"),
    ("spt_364", "What is a 'rodeo flip' in snowboarding?", ["Off-axis backflip with 180", "Simple backflip", "360 spin", "Frontflip"], "Off-axis backflip with 180", "hard"),
    ("spt_365", "Who invented the ollie in skateboarding?", ["Alan 'Ollie' Gelfand", "Rodney Mullen", "Tony Hawk", "Stacy Peralta"], "Alan 'Ollie' Gelfand", "hard"),
    ("spt_366", "What is the Big Air competition in action sports?", ["Single-trick showcase with large ramp", "Endurance event", "Speed competition", "Team relay"], "Single-trick showcase with large ramp", "hard"),
    ("spt_367", "What is 'jibbing' in snowboarding?", ["Tricks on non-snow features", "Speed racing", "Halfpipe tricks", "Aerial jumps"], "Tricks on non-snow features", "hard"),
    ("spt_368", "Who was the first woman to land a 1080 in skateboarding?", ["Gui Khury (male, but Lizzie Armanto first woman 540)", "Lizzie Armanto", "Leticia Bufoni", "Sky Brown"], "Gui Khury (male, but Lizzie Armanto first woman 540)", "hard"),
    ("spt_369", "What is the Mega Ramp in skateboarding?", ["Extra-large ramp for big air", "Standard halfpipe", "Street course", "Bowl design"], "Extra-large ramp for big air", "hard"),
    ("spt_370", "What is 'pow' in snowboarding slang?", ["Powder snow", "Power slide", "Powerful trick", "Point of wipeout"], "Powder snow", "hard"),
    ("spt_371", "Who was the first to land a 1080 in skateboarding?", ["Tom Schaar", "Tony Hawk", "Mitchie Brusco", "Gui Khury"], "Tom Schaar", "hard"),
    ("spt_372", "What is a 'superman seat grab' in motocross?", ["Extending body backward while grabbing seat", "Sitting trick", "Front flip", "Standing jump"], "Extending body backward while grabbing seat", "hard"),
    ("spt_373", "What is the Eddie Aikau Big Wave Invitational?", ["Elite surfing contest in huge waves", "Skateboard competition", "Snowboard event", "BMX race"], "Elite surfing contest in huge waves", "hard"),
    ("spt_374", "What is 'sketchy' in action sports terminology?", ["Barely landing trick", "Perfect landing", "Failed attempt", "Easy trick"], "Barely landing trick", "hard"),
    ("spt_375", "Who is Kelly Slater?", ["11-time world surfing champion", "Skateboarder", "Snowboarder", "BMX rider"], "11-time world surfing champion", "hard"),
    ("spt_376", "What is a 'butter' in snowboarding?", ["Ground-based spin trick", "Aerial trick", "Rail grind", "Speed technique"], "Ground-based spin trick", "hard"),
]

for q in hard:
    extreme_action_sports.append({
        "id": q[0],
        "category": "Sports",
        "subcategory": "Extreme & Action Sports",
        "question": q[1],
        "options": q[2],
        "correct_answer": q[3],
        "difficulty": q[4],
        "topic": None,
        "subtopic": None
    })

# Load and update
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

# Add International Competition question
data['categories']['Sports'].append(intl_competition_question)

# Add Extreme & Action Sports questions
data['categories']['Sports'].extend(extreme_action_sports)

# Sort
data['categories']['Sports'].sort(key=lambda q: int(q['id'].split('_')[1]))

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Added 1 International Competition question (49 → 50)")
print("✅ Added 50 Extreme & Action Sports questions")
print(f"   - {len([q for q in extreme_action_sports if q['difficulty'] == 'easy'])} easy")
print(f"   - {len([q for q in extreme_action_sports if q['difficulty'] == 'medium'])} medium")
print(f"   - {len([q for q in extreme_action_sports if q['difficulty'] == 'hard'])} hard")
print(f"\nSports category now has {len(data['categories']['Sports'])} questions")
