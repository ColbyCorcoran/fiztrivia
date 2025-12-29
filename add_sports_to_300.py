#!/usr/bin/env python3
"""
Add 140 new Sports questions to reach 300 total

Distribution:
- Team Sports: +50 (15 easy, 20 medium, 15 hard)
- Individual Sports: +60 (18 easy, 24 medium, 18 hard)
- International Competition: +30 (9 easy, 12 medium, 9 hard)
"""

import json

# IDs will be spt_161 through spt_300

new_questions = [
    # TEAM SPORTS (+50 questions)
    # Football - Easy (5)
    {"id": "spt_161", "category": "Sports", "subcategory": "Team Sports", "question": "What NFL team is known as 'America's Team'?", "options": ["Dallas Cowboys", "Green Bay Packers", "Pittsburgh Steelers", "New England Patriots"], "correct_answer": "Dallas Cowboys", "difficulty": "easy"},
    {"id": "spt_162", "category": "Sports", "subcategory": "Team Sports", "question": "How many points is a safety worth in American football?", "options": ["2", "1", "3", "6"], "correct_answer": "2", "difficulty": "easy"},
    {"id": "spt_163", "category": "Sports", "subcategory": "Team Sports", "question": "What is the name of the championship trophy in college football?", "options": ["College Football Playoff National Championship Trophy", "Heisman Trophy", "Lombardi Trophy", "Walter Camp Trophy"], "correct_answer": "College Football Playoff National Championship Trophy", "difficulty": "easy"},
    {"id": "spt_164", "category": "Sports", "subcategory": "Team Sports", "question": "Which position in football is abbreviated 'QB'?", "options": ["Quarterback", "Quick back", "Quarter blocker", "Quad back"], "correct_answer": "Quarterback", "difficulty": "easy"},
    {"id": "spt_165", "category": "Sports", "subcategory": "Team Sports", "question": "What color are the goal posts in American football?", "options": ["Yellow", "White", "Orange", "Red"], "correct_answer": "Yellow", "difficulty": "easy"},

    # Basketball - Easy (5)
    {"id": "spt_166", "category": "Sports", "subcategory": "Team Sports", "question": "How many players from one team are on a basketball court at one time?", "options": ["5", "6", "7", "4"], "correct_answer": "5", "difficulty": "easy"},
    {"id": "spt_167", "category": "Sports", "subcategory": "Team Sports", "question": "What is it called when a player scores while being fouled?", "options": ["And-one", "Free throw", "Flagrant", "Technical"], "correct_answer": "And-one", "difficulty": "easy"},
    {"id": "spt_168", "category": "Sports", "subcategory": "Team Sports", "question": "How many points is a free throw worth?", "options": ["1", "2", "3", "0"], "correct_answer": "1", "difficulty": "easy"},
    {"id": "spt_169", "category": "Sports", "subcategory": "Team Sports", "question": "Which NBA team plays in Madison Square Garden?", "options": ["New York Knicks", "Brooklyn Nets", "Boston Celtics", "Philadelphia 76ers"], "correct_answer": "New York Knicks", "difficulty": "easy"},
    {"id": "spt_170", "category": "Sports", "subcategory": "Team Sports", "question": "What violation occurs when a player takes too many steps without dribbling?", "options": ["Traveling", "Double dribble", "Palming", "Carrying"], "correct_answer": "Traveling", "difficulty": "easy"},

    # Baseball - Easy (5)
    {"id": "spt_171", "category": "Sports", "subcategory": "Team Sports", "question": "How many strikes result in a strikeout?", "options": ["3", "4", "2", "5"], "correct_answer": "3", "difficulty": "easy"},
    {"id": "spt_172", "category": "Sports", "subcategory": "Team Sports", "question": "What is the area where pitchers warm up called?", "options": ["Bullpen", "Dugout", "Mound", "Pen"], "correct_answer": "Bullpen", "difficulty": "easy"},
    {"id": "spt_173", "category": "Sports", "subcategory": "Team Sports", "question": "Which base must a runner touch to score a run?", "options": ["Home plate", "First base", "Third base", "Second base"], "correct_answer": "Home plate", "difficulty": "easy"},
    {"id": "spt_174", "category": "Sports", "subcategory": "Team Sports", "question": "What is the term for hitting the ball over the outfield fence?", "options": ["Home run", "Grand slam", "Triple", "Fly ball"], "correct_answer": "Home run", "difficulty": "easy"},
    {"id": "spt_175", "category": "Sports", "subcategory": "Team Sports", "question": "How many outs are in a half-inning?", "options": ["3", "2", "4", "6"], "correct_answer": "3", "difficulty": "easy"},

    # Football - Medium (7)
    {"id": "spt_176", "category": "Sports", "subcategory": "Team Sports", "question": "Which NFL team has the most Super Bowl appearances without a win?", "options": ["Buffalo Bills", "Minnesota Vikings", "Cincinnati Bengals", "Tennessee Titans"], "correct_answer": "Buffalo Bills", "difficulty": "medium"},
    {"id": "spt_177", "category": "Sports", "subcategory": "Team Sports", "question": "What is the NFL record for most consecutive games with a touchdown pass?", "options": ["54 (Drew Brees)", "52 (Tom Brady)", "50 (Peyton Manning)", "48 (Aaron Rodgers)"], "correct_answer": "54 (Drew Brees)", "difficulty": "medium"},
    {"id": "spt_178", "category": "Sports", "subcategory": "Team Sports", "question": "Which college football team has the most national championships?", "options": ["Yale", "Alabama", "Notre Dame", "Princeton"], "correct_answer": "Yale", "difficulty": "medium"},
    {"id": "spt_179", "category": "Sports", "subcategory": "Team Sports", "question": "What formation features 5 offensive linemen, 1 quarterback, 1 running back, and 3 wide receivers?", "options": ["Shotgun formation", "I-formation", "Wishbone", "Wildcat"], "correct_answer": "Shotgun formation", "difficulty": "medium"},
    {"id": "spt_180", "category": "Sports", "subcategory": "Team Sports", "question": "Who holds the NFL single-season rushing record?", "options": ["Eric Dickerson", "Barry Sanders", "Adrian Peterson", "O.J. Simpson"], "correct_answer": "Eric Dickerson", "difficulty": "medium"},
    {"id": "spt_181", "category": "Sports", "subcategory": "Team Sports", "question": "What is the name of the play where the quarterback throws the ball backward to another player?", "options": ["Lateral", "Screen pass", "Reverse", "Handoff"], "correct_answer": "Lateral", "difficulty": "medium"},
    {"id": "spt_182", "category": "Sports", "subcategory": "Team Sports", "question": "Which NFL team was originally named the Decatur Staleys?", "options": ["Chicago Bears", "Green Bay Packers", "Detroit Lions", "Minnesota Vikings"], "correct_answer": "Chicago Bears", "difficulty": "medium"},

    # Basketball - Medium (7)
    {"id": "spt_183", "category": "Sports", "subcategory": "Team Sports", "question": "Which player holds the NBA record for most rebounds in a single game?", "options": ["Wilt Chamberlain (55)", "Bill Russell (51)", "Dennis Rodman (34)", "Dwight Howard (30)"], "correct_answer": "Wilt Chamberlain (55)", "difficulty": "medium"},
    {"id": "spt_184", "category": "Sports", "subcategory": "Team Sports", "question": "What is the name of the defensive strategy where each player guards a specific area?", "options": ["Zone defense", "Man-to-man", "Press defense", "Box-and-one"], "correct_answer": "Zone defense", "difficulty": "medium"},
    {"id": "spt_185", "category": "Sports", "subcategory": "Team Sports", "question": "Which NBA team won the championship in 2019, their first in franchise history?", "options": ["Toronto Raptors", "Milwaukee Bucks", "Phoenix Suns", "Denver Nuggets"], "correct_answer": "Toronto Raptors", "difficulty": "medium"},
    {"id": "spt_186", "category": "Sports", "subcategory": "Team Sports", "question": "What is the width of a regulation NBA basketball rim in inches?", "options": ["18 inches", "16 inches", "20 inches", "24 inches"], "correct_answer": "18 inches", "difficulty": "medium"},
    {"id": "spt_187", "category": "Sports", "subcategory": "Team Sports", "question": "Which college has produced the most NBA #1 draft picks?", "options": ["Duke", "Kentucky", "North Carolina", "UCLA"], "correct_answer": "Duke", "difficulty": "medium"},
    {"id": "spt_188", "category": "Sports", "subcategory": "Team Sports", "question": "What is the name of the pass where the ball bounces once before reaching the receiver?", "options": ["Bounce pass", "Chest pass", "Overhead pass", "Baseball pass"], "correct_answer": "Bounce pass", "difficulty": "medium"},
    {"id": "spt_189", "category": "Sports", "subcategory": "Team Sports", "question": "How many seconds does a team have to attempt a shot in the NBA?", "options": ["24 seconds", "30 seconds", "35 seconds", "20 seconds"], "correct_answer": "24 seconds", "difficulty": "medium"},

    # Baseball - Medium (3)
    {"id": "spt_190", "category": "Sports", "subcategory": "Team Sports", "question": "What is the term for a pitch that curves away from a right-handed batter when thrown by a right-handed pitcher?", "options": ["Slider", "Curveball", "Changeup", "Sinker"], "correct_answer": "Slider", "difficulty": "medium"},
    {"id": "spt_191", "category": "Sports", "subcategory": "Team Sports", "question": "Which player holds the MLB record for most career home runs?", "options": ["Barry Bonds (762)", "Hank Aaron (755)", "Babe Ruth (714)", "Alex Rodriguez (696)"], "correct_answer": "Barry Bonds (762)", "difficulty": "medium"},
    {"id": "spt_192", "category": "Sports", "subcategory": "Team Sports", "question": "What statistic measures a pitcher's average number of earned runs per 9 innings?", "options": ["ERA (Earned Run Average)", "WHIP", "BAA", "FIP"], "correct_answer": "ERA (Earned Run Average)", "difficulty": "medium"},

    # Soccer - Medium (3)
    {"id": "spt_193", "category": "Sports", "subcategory": "Team Sports", "question": "Which English club has won the most Premier League titles?", "options": ["Manchester United", "Liverpool", "Chelsea", "Arsenal"], "correct_answer": "Manchester United", "difficulty": "medium"},
    {"id": "spt_194", "category": "Sports", "subcategory": "Team Sports", "question": "What is the name of the rule that prevents attackers from gaining unfair advantage by being ahead of defenders?", "options": ["Offside", "Penalty", "Handball", "Obstruction"], "correct_answer": "Offside", "difficulty": "medium"},
    {"id": "spt_195", "category": "Sports", "subcategory": "Team Sports", "question": "Which club has won the most UEFA Champions League titles?", "options": ["Real Madrid", "AC Milan", "Barcelona", "Bayern Munich"], "correct_answer": "Real Madrid", "difficulty": "medium"},

    # Football - Hard (5)
    {"id": "spt_196", "category": "Sports", "subcategory": "Team Sports", "question": "What is the name of the blocking technique where an offensive lineman pulls from their position to lead a run?", "options": ["Trap block", "Zone block", "Reach block", "Combo block"], "correct_answer": "Trap block", "difficulty": "hard"},
    {"id": "spt_197", "category": "Sports", "subcategory": "Team Sports", "question": "Which NFL player rushed for over 2,000 yards in a 14-game season in 1973?", "options": ["O.J. Simpson", "Jim Brown", "Walter Payton", "Earl Campbell"], "correct_answer": "O.J. Simpson", "difficulty": "hard"},
    {"id": "spt_198", "category": "Sports", "subcategory": "Team Sports", "question": "What is a 'Tampa 2' defense characterized by?", "options": ["Middle linebacker dropping deep into coverage", "Two safeties playing deep zones", "Two corners pressing receivers", "Four defensive linemen"], "correct_answer": "Middle linebacker dropping deep into coverage", "difficulty": "hard"},
    {"id": "spt_199", "category": "Sports", "subcategory": "Team Sports", "question": "Which team won the first Super Bowl in 1967?", "options": ["Green Bay Packers", "Kansas City Chiefs", "Oakland Raiders", "Dallas Cowboys"], "correct_answer": "Green Bay Packers", "difficulty": "hard"},
    {"id": "spt_200", "category": "Sports", "subcategory": "Team Sports", "question": "What is the Wonderlic test score range for NFL prospects?", "options": ["0-50", "0-100", "0-200", "0-150"], "correct_answer": "0-50", "difficulty": "hard"},

    # Basketball - Hard (5)
    {"id": "spt_201", "category": "Sports", "subcategory": "Team Sports", "question": "Which NBA team holds the record for most wins in a regular season?", "options": ["Golden State Warriors (73)", "Chicago Bulls (72)", "Los Angeles Lakers (69)", "Boston Celtics (68)"], "correct_answer": "Golden State Warriors (73)", "difficulty": "hard"},
    {"id": "spt_202", "category": "Sports", "subcategory": "Team Sports", "question": "What is the name of the statistical category that measures a player's overall contribution per 100 possessions?", "options": ["PER (Player Efficiency Rating)", "Win Shares", "VORP", "BPM"], "correct_answer": "PER (Player Efficiency Rating)", "difficulty": "hard"},
    {"id": "spt_203", "category": "Sports", "subcategory": "Team Sports", "question": "Which team drafted Kobe Bryant before trading him to the Lakers?", "options": ["Charlotte Hornets", "Vancouver Grizzlies", "Toronto Raptors", "New Jersey Nets"], "correct_answer": "Charlotte Hornets", "difficulty": "hard"},
    {"id": "spt_204", "category": "Sports", "subcategory": "Team Sports", "question": "What is the largest comeback in NBA playoff history (points)?", "options": ["31 points", "29 points", "26 points", "35 points"], "correct_answer": "31 points", "difficulty": "hard"},
    {"id": "spt_205", "category": "Sports", "subcategory": "Team Sports", "question": "Which NBA player has the highest career free throw percentage?", "options": ["Stephen Curry (90.7%)", "Steve Nash (90.4%)", "Mark Price (90.4%)", "Rick Barry (89.3%)"], "correct_answer": "Stephen Curry (90.7%)", "difficulty": "hard"},

    # Baseball - Hard (3)
    {"id": "spt_206", "category": "Sports", "subcategory": "Team Sports", "question": "What is the 'Mendoza Line' in baseball?", "options": ["A .200 batting average", "A .100 batting average", "A .250 batting average", "A .150 batting average"], "correct_answer": "A .200 batting average", "difficulty": "hard"},
    {"id": "spt_207", "category": "Sports", "subcategory": "Team Sports", "question": "Which pitcher threw a perfect game in the 1956 World Series?", "options": ["Don Larsen", "Sandy Koufax", "Bob Gibson", "Whitey Ford"], "correct_answer": "Don Larsen", "difficulty": "hard"},
    {"id": "spt_208", "category": "Sports", "subcategory": "Team Sports", "question": "What does the baseball statistic 'BABIP' stand for?", "options": ["Batting Average on Balls In Play", "Base Average Batting In Position", "Batters Against Balls In Play", "Base Awarded Batting In Park"], "correct_answer": "Batting Average on Balls In Play", "difficulty": "hard"},

    # Soccer - Hard (2)
    {"id": "spt_209", "category": "Sports", "subcategory": "Team Sports", "question": "Which player scored the 'Hand of God' goal in the 1986 World Cup?", "options": ["Diego Maradona", "Pelé", "Johan Cruyff", "Michel Platini"], "correct_answer": "Diego Maradona", "difficulty": "hard"},
    {"id": "spt_210", "category": "Sports", "subcategory": "Team Sports", "question": "What is the 'false nine' position in soccer?", "options": ["A striker who drops deep to create space", "A defensive midfielder who pushes forward", "A winger who plays centrally", "A fullback who becomes a striker"], "correct_answer": "A striker who drops deep to create space", "difficulty": "hard"},

    # INDIVIDUAL SPORTS (+60 questions)
    # Tennis - Easy (6)
    {"id": "spt_211", "category": "Sports", "subcategory": "Individual Sports", "question": "How many Grand Slam tournaments are there in tennis each year?", "options": ["4", "5", "3", "6"], "correct_answer": "4", "difficulty": "easy"},
    {"id": "spt_212", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the score called when both players have won 40 points?", "options": ["Deuce", "Advantage", "Game point", "Match point"], "correct_answer": "Deuce", "difficulty": "easy"},
    {"id": "spt_213", "category": "Sports", "subcategory": "Individual Sports", "question": "On which surface is the French Open played?", "options": ["Clay", "Grass", "Hard court", "Carpet"], "correct_answer": "Clay", "difficulty": "easy"},
    {"id": "spt_214", "category": "Sports", "subcategory": "Individual Sports", "question": "How many points is the first point in a tennis game worth?", "options": ["15", "10", "1", "5"], "correct_answer": "15", "difficulty": "easy"},
    {"id": "spt_215", "category": "Sports", "subcategory": "Individual Sports", "question": "What is it called when a player wins a point on their serve without the opponent touching the ball?", "options": ["Ace", "Winner", "Fault", "Let"], "correct_answer": "Ace", "difficulty": "easy"},
    {"id": "spt_216", "category": "Sports", "subcategory": "Individual Sports", "question": "Which Grand Slam is played on grass courts?", "options": ["Wimbledon", "US Open", "Australian Open", "French Open"], "correct_answer": "Wimbledon", "difficulty": "easy"},

    # Golf - Easy (6)
    {"id": "spt_217", "category": "Sports", "subcategory": "Individual Sports", "question": "How many holes are in a standard round of golf?", "options": ["18", "9", "27", "36"], "correct_answer": "18", "difficulty": "easy"},
    {"id": "spt_218", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the term for one stroke under par on a hole?", "options": ["Birdie", "Eagle", "Bogey", "Par"], "correct_answer": "Birdie", "difficulty": "easy"},
    {"id": "spt_219", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the device called that holds the golf ball for the first stroke?", "options": ["Tee", "Pin", "Flag", "Marker"], "correct_answer": "Tee", "difficulty": "easy"},
    {"id": "spt_220", "category": "Sports", "subcategory": "Individual Sports", "question": "What is two strokes under par called?", "options": ["Eagle", "Birdie", "Albatross", "Condor"], "correct_answer": "Eagle", "difficulty": "easy"},
    {"id": "spt_221", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the grassy area around the hole called?", "options": ["Green", "Fairway", "Rough", "Tee box"], "correct_answer": "Green", "difficulty": "easy"},
    {"id": "spt_222", "category": "Sports", "subcategory": "Individual Sports", "question": "How many major championships are there in professional golf?", "options": ["4", "3", "5", "6"], "correct_answer": "4", "difficulty": "easy"},

    # Track & Field - Easy (3)
    {"id": "spt_223", "category": "Sports", "subcategory": "Individual Sports", "question": "How many lanes are on a standard Olympic track?", "options": ["8", "6", "10", "9"], "correct_answer": "8", "difficulty": "easy"},
    {"id": "spt_224", "category": "Sports", "subcategory": "Individual Sports", "question": "What implement is thrown in the javelin event?", "options": ["Spear", "Pole", "Lance", "Rod"], "correct_answer": "Spear", "difficulty": "easy"},
    {"id": "spt_225", "category": "Sports", "subcategory": "Individual Sports", "question": "How many meters is a standard Olympic sprint track?", "options": ["400 meters", "200 meters", "500 meters", "300 meters"], "correct_answer": "400 meters", "difficulty": "easy"},

    # Swimming - Easy (3)
    {"id": "spt_226", "category": "Sports", "subcategory": "Individual Sports", "question": "Which swimming stroke is swum on the back?", "options": ["Backstroke", "Butterfly", "Breaststroke", "Freestyle"], "correct_answer": "Backstroke", "difficulty": "easy"},
    {"id": "spt_227", "category": "Sports", "subcategory": "Individual Sports", "question": "How many meters is an Olympic-sized swimming pool?", "options": ["50 meters", "25 meters", "100 meters", "75 meters"], "correct_answer": "50 meters", "difficulty": "easy"},
    {"id": "spt_228", "category": "Sports", "subcategory": "Individual Sports", "question": "What stroke involves bringing both arms forward simultaneously over the water?", "options": ["Butterfly", "Freestyle", "Backstroke", "Breaststroke"], "correct_answer": "Butterfly", "difficulty": "easy"},

    # Tennis - Medium (8)
    {"id": "spt_229", "category": "Sports", "subcategory": "Individual Sports", "question": "Who holds the record for most Grand Slam singles titles in men's tennis?", "options": ["Novak Djokovic (24)", "Rafael Nadal (22)", "Roger Federer (20)", "Pete Sampras (14)"], "correct_answer": "Novak Djokovic (24)", "difficulty": "medium"},
    {"id": "spt_230", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the fastest recorded tennis serve?", "options": ["163.7 mph (Sam Groth)", "157.2 mph (John Isner)", "149.1 mph (Andy Roddick)", "155.3 mph (Ivo Karlović)"], "correct_answer": "163.7 mph (Sam Groth)", "difficulty": "medium"},
    {"id": "spt_231", "category": "Sports", "subcategory": "Individual Sports", "question": "How many sets must a player win to claim victory in a men's Grand Slam final?", "options": ["3 out of 5", "2 out of 3", "4 out of 7", "3 out of 7"], "correct_answer": "3 out of 5", "difficulty": "medium"},
    {"id": "spt_232", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the term for winning all four Grand Slams in a calendar year?", "options": ["Calendar Grand Slam", "Golden Slam", "Career Grand Slam", "Super Slam"], "correct_answer": "Calendar Grand Slam", "difficulty": "medium"},
    {"id": "spt_233", "category": "Sports", "subcategory": "Individual Sports", "question": "Which country has won the most Davis Cup titles?", "options": ["United States", "Australia", "France", "Great Britain"], "correct_answer": "United States", "difficulty": "medium"},
    {"id": "spt_234", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the name of the line that runs parallel to the net and marks the boundary for singles play?", "options": ["Singles sideline", "Service line", "Baseline", "Center mark"], "correct_answer": "Singles sideline", "difficulty": "medium"},
    {"id": "spt_235", "category": "Sports", "subcategory": "Individual Sports", "question": "How many games must a player win to take a set, provided they lead by at least 2 games?", "options": ["6", "7", "5", "8"], "correct_answer": "6", "difficulty": "medium"},
    {"id": "spt_236", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the name of the women's team tennis competition equivalent to the Davis Cup?", "options": ["Billie Jean King Cup", "Fed Cup", "WTA Cup", "Venus Cup"], "correct_answer": "Billie Jean King Cup", "difficulty": "medium"},

    # Golf - Medium (8)
    {"id": "spt_237", "category": "Sports", "subcategory": "Individual Sports", "question": "Which golf major is traditionally played at Augusta National?", "options": ["The Masters", "US Open", "PGA Championship", "The Open Championship"], "correct_answer": "The Masters", "difficulty": "medium"},
    {"id": "spt_238", "category": "Sports", "subcategory": "Individual Sports", "question": "What is three strokes under par called?", "options": ["Albatross", "Eagle", "Condor", "Ace"], "correct_answer": "Albatross", "difficulty": "medium"},
    {"id": "spt_239", "category": "Sports", "subcategory": "Individual Sports", "question": "Which player has won the most major championships in golf history?", "options": ["Jack Nicklaus (18)", "Tiger Woods (15)", "Walter Hagen (11)", "Ben Hogan (9)"], "correct_answer": "Jack Nicklaus (18)", "difficulty": "medium"},
    {"id": "spt_240", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the term for the person who carries a player's clubs and provides advice?", "options": ["Caddie", "Coach", "Handler", "Assistant"], "correct_answer": "Caddie", "difficulty": "medium"},
    {"id": "spt_241", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the maximum number of clubs allowed in a golf bag during competition?", "options": ["14", "12", "16", "18"], "correct_answer": "14", "difficulty": "medium"},
    {"id": "spt_242", "category": "Sports", "subcategory": "Individual Sports", "question": "What is a score of one over par called?", "options": ["Bogey", "Double bogey", "Par", "Birdie"], "correct_answer": "Bogey", "difficulty": "medium"},
    {"id": "spt_243", "category": "Sports", "subcategory": "Individual Sports", "question": "Which tournament is known as 'The Old Course' and is considered the home of golf?", "options": ["St. Andrews", "Pebble Beach", "Augusta National", "Pinehurst"], "correct_answer": "St. Andrews", "difficulty": "medium"},
    {"id": "spt_244", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the team golf competition between Europe and the United States called?", "options": ["Ryder Cup", "Presidents Cup", "Walker Cup", "Solheim Cup"], "correct_answer": "Ryder Cup", "difficulty": "medium"},

    # Track & Field - Medium (4)
    {"id": "spt_245", "category": "Sports", "subcategory": "Individual Sports", "question": "Who holds the world record in the men's 100-meter dash?", "options": ["Usain Bolt (9.58s)", "Tyson Gay (9.69s)", "Yohan Blake (9.69s)", "Asafa Powell (9.72s)"], "correct_answer": "Usain Bolt (9.58s)", "difficulty": "medium"},
    {"id": "spt_246", "category": "Sports", "subcategory": "Individual Sports", "question": "How many events make up the decathlon?", "options": ["10", "7", "5", "12"], "correct_answer": "10", "difficulty": "medium"},
    {"id": "spt_247", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the name of the jumping event where athletes use a flexible pole?", "options": ["Pole vault", "High jump", "Long jump", "Triple jump"], "correct_answer": "Pole vault", "difficulty": "medium"},
    {"id": "spt_248", "category": "Sports", "subcategory": "Individual Sports", "question": "In which event do athletes run 400 meters while jumping over barriers?", "options": ["400-meter hurdles", "110-meter hurdles", "Steeplechase", "3000-meter hurdles"], "correct_answer": "400-meter hurdles", "difficulty": "medium"},

    # Swimming - Medium (4)
    {"id": "spt_249", "category": "Sports", "subcategory": "Individual Sports", "question": "Who has won the most Olympic gold medals in swimming?", "options": ["Michael Phelps (23)", "Mark Spitz (9)", "Katie Ledecky (9)", "Ryan Lochte (6)"], "correct_answer": "Michael Phelps (23)", "difficulty": "medium"},
    {"id": "spt_250", "category": "Sports", "subcategory": "Individual Sports", "question": "What swimming event combines all four strokes?", "options": ["Individual medley", "Relay medley", "Freestyle relay", "Mixed relay"], "correct_answer": "Individual medley", "difficulty": "medium"},
    {"id": "spt_251", "category": "Sports", "subcategory": "Individual Sports", "question": "How many lanes does an Olympic swimming pool have?", "options": ["8", "6", "10", "12"], "correct_answer": "8", "difficulty": "medium"},
    {"id": "spt_252", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the order of strokes in an individual medley?", "options": ["Butterfly, backstroke, breaststroke, freestyle", "Freestyle, backstroke, butterfly, breaststroke", "Backstroke, breaststroke, butterfly, freestyle", "Breaststroke, butterfly, backstroke, freestyle"], "correct_answer": "Butterfly, backstroke, breaststroke, freestyle", "difficulty": "medium"},

    # Tennis - Hard (6)
    {"id": "spt_253", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the longest tennis match in history by duration?", "options": ["11 hours 5 minutes (Isner vs Mahut, 2010)", "6 hours 36 minutes (Anderson vs Isner, 2018)", "5 hours 53 minutes (Nadal vs Djokovic, 2012)", "4 hours 54 minutes (Federer vs Roddick, 2009)"], "correct_answer": "11 hours 5 minutes (Isner vs Mahut, 2010)", "difficulty": "hard"},
    {"id": "spt_254", "category": "Sports", "subcategory": "Individual Sports", "question": "What does the ATP ranking system primarily consider?", "options": ["Points earned in tournaments over 52 weeks", "Win-loss record", "Head-to-head results", "Grand Slam performance only"], "correct_answer": "Points earned in tournaments over 52 weeks", "difficulty": "hard"},
    {"id": "spt_255", "category": "Sports", "subcategory": "Individual Sports", "question": "Which player completed the 'Golden Slam' (all four majors plus Olympic gold) in 1988?", "options": ["Steffi Graf", "Martina Navratilova", "Serena Williams", "Chris Evert"], "correct_answer": "Steffi Graf", "difficulty": "hard"},
    {"id": "spt_256", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the maximum number of challenges allowed per set in tennis (using Hawk-Eye)?", "options": ["3", "2", "4", "5"], "correct_answer": "3", "difficulty": "hard"},
    {"id": "spt_257", "category": "Sports", "subcategory": "Individual Sports", "question": "Which Grand Slam was the last to introduce a tiebreak in the final set?", "options": ["French Open (2022)", "Wimbledon (2019)", "US Open (1970)", "Australian Open (2019)"], "correct_answer": "French Open (2022)", "difficulty": "hard"},
    {"id": "spt_258", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the term for a serve that touches the net but still lands in the service box?", "options": ["Let", "Fault", "Ace", "Net serve"], "correct_answer": "Let", "difficulty": "hard"},

    # Golf - Hard (6)
    {"id": "spt_259", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the lowest score ever recorded in a major championship round?", "options": ["62", "59", "61", "63"], "correct_answer": "62", "difficulty": "hard"},
    {"id": "spt_260", "category": "Sports", "subcategory": "Individual Sports", "question": "What is a 'stimpmeter' used to measure in golf?", "options": ["Green speed", "Ball velocity", "Club head speed", "Wind speed"], "correct_answer": "Green speed", "difficulty": "hard"},
    {"id": "spt_261", "category": "Sports", "subcategory": "Individual Sports", "question": "Which golfer is known as 'The Golden Bear'?", "options": ["Jack Nicklaus", "Arnold Palmer", "Gary Player", "Tom Watson"], "correct_answer": "Jack Nicklaus", "difficulty": "hard"},
    {"id": "spt_262", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the cut line in most PGA Tour events?", "options": ["Top 70 plus ties", "Top 60 plus ties", "Top 50 plus ties", "Top 80 plus ties"], "correct_answer": "Top 70 plus ties", "difficulty": "hard"},
    {"id": "spt_263", "category": "Sports", "subcategory": "Individual Sports", "question": "What is four strokes under par on a single hole called?", "options": ["Condor", "Albatross", "Double eagle", "Ostrich"], "correct_answer": "Condor", "difficulty": "hard"},
    {"id": "spt_264", "category": "Sports", "subcategory": "Individual Sports", "question": "Which club is traditionally used for the longest shots (besides the driver)?", "options": ["3-wood", "5-wood", "Hybrid", "2-iron"], "correct_answer": "3-wood", "difficulty": "hard"},

    # Track & Field - Hard (3)
    {"id": "spt_265", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the world record for the men's marathon?", "options": ["2:00:35 (Eliud Kipchoge)", "2:01:39 (Kelvin Kiptum)", "2:02:57 (Dennis Kimetto)", "1:59:40 (Eliud Kipchoge - unofficial)"], "correct_answer": "2:00:35 (Eliud Kipchoge)", "difficulty": "hard"},
    {"id": "spt_266", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the standard weight of a men's shot put?", "options": ["16 pounds", "12 pounds", "20 pounds", "18 pounds"], "correct_answer": "16 pounds", "difficulty": "hard"},
    {"id": "spt_267", "category": "Sports", "subcategory": "Individual Sports", "question": "Which athlete holds the women's world record in the long jump?", "options": ["Galina Chistyakova (7.52m)", "Jackie Joyner-Kersee (7.49m)", "Heike Drechsler (7.48m)", "Brittney Reese (7.31m)"], "correct_answer": "Galina Chistyakova (7.52m)", "difficulty": "hard"},

    # Swimming - Hard (3)
    {"id": "spt_268", "category": "Sports", "subcategory": "Individual Sports", "question": "What is the world record for the men's 100-meter freestyle?", "options": ["46.86 seconds (Pan Zhanle)", "46.91 seconds (Caeleb Dressel)", "47.04 seconds (César Cielo)", "47.17 seconds (Kyle Chalmers)"], "correct_answer": "46.86 seconds (Pan Zhanle)", "difficulty": "hard"},
    {"id": "spt_269", "category": "Sports", "subcategory": "Individual Sports", "question": "What swimming technique involves a simultaneous two-handed touch on the wall?", "options": ["Required for butterfly and breaststroke turns", "Required for all strokes", "Required for freestyle only", "Not required for any stroke"], "correct_answer": "Required for butterfly and breaststroke turns", "difficulty": "hard"},
    {"id": "spt_270", "category": "Sports", "subcategory": "Individual Sports", "question": "How deep is an Olympic swimming pool?", "options": ["2 meters (minimum)", "3 meters", "1.5 meters", "2.5 meters"], "correct_answer": "2 meters (minimum)", "difficulty": "hard"},

    # INTERNATIONAL COMPETITION (+30 questions)
    # Olympics - Easy (5)
    {"id": "spt_271", "category": "Sports", "subcategory": "International Competition", "question": "How often are the Summer Olympics held?", "options": ["Every 4 years", "Every 2 years", "Every 5 years", "Every 3 years"], "correct_answer": "Every 4 years", "difficulty": "easy"},
    {"id": "spt_272", "category": "Sports", "subcategory": "International Competition", "question": "What are the five Olympic rings meant to represent?", "options": ["Five continents", "Five sports", "Five nations", "Five values"], "correct_answer": "Five continents", "difficulty": "easy"},
    {"id": "spt_273", "category": "Sports", "subcategory": "International Competition", "question": "What metal is the first-place Olympic medal primarily made of?", "options": ["Gold", "Silver", "Bronze", "Platinum"], "correct_answer": "Gold", "difficulty": "easy"},
    {"id": "spt_274", "category": "Sports", "subcategory": "International Competition", "question": "Where were the first modern Olympic Games held in 1896?", "options": ["Athens, Greece", "Paris, France", "London, England", "Rome, Italy"], "correct_answer": "Athens, Greece", "difficulty": "easy"},
    {"id": "spt_275", "category": "Sports", "subcategory": "International Competition", "question": "What is the Olympic motto in Latin?", "options": ["Citius, Altius, Fortius", "Carpe Diem", "E Pluribus Unum", "Veni, Vidi, Vici"], "correct_answer": "Citius, Altius, Fortius", "difficulty": "easy"},

    # World Cup - Easy (2)
    {"id": "spt_276", "category": "Sports", "subcategory": "International Competition", "question": "How often is the FIFA World Cup held?", "options": ["Every 4 years", "Every 2 years", "Every year", "Every 3 years"], "correct_answer": "Every 4 years", "difficulty": "easy"},
    {"id": "spt_277", "category": "Sports", "subcategory": "International Competition", "question": "Which country has won the most FIFA World Cups?", "options": ["Brazil", "Germany", "Argentina", "Italy"], "correct_answer": "Brazil", "difficulty": "easy"},

    # Pan American Games - Easy (1)
    {"id": "spt_278", "category": "Sports", "subcategory": "International Competition", "question": "What continent hosts the Pan American Games?", "options": ["Americas", "Europe", "Asia", "Africa"], "correct_answer": "Americas", "difficulty": "easy"},

    # Commonwealth Games - Easy (1)
    {"id": "spt_279", "category": "Sports", "subcategory": "International Competition", "question": "Which international sporting event is exclusively for Commonwealth nations?", "options": ["Commonwealth Games", "Empire Games", "British Games", "Colonial Games"], "correct_answer": "Commonwealth Games", "difficulty": "easy"},

    # Olympics - Medium (6)
    {"id": "spt_280", "category": "Sports", "subcategory": "International Competition", "question": "Which country has won the most total Olympic medals in history?", "options": ["United States", "Soviet Union", "Germany", "Great Britain"], "correct_answer": "United States", "difficulty": "medium"},
    {"id": "spt_281", "category": "Sports", "subcategory": "International Competition", "question": "What year were the first Winter Olympics held?", "options": ["1924", "1920", "1928", "1932"], "correct_answer": "1924", "difficulty": "medium"},
    {"id": "spt_282", "category": "Sports", "subcategory": "International Competition", "question": "Which city has hosted the Summer Olympics three times?", "options": ["London", "Paris", "Los Angeles", "Athens"], "correct_answer": "London", "difficulty": "medium"},
    {"id": "spt_283", "category": "Sports", "subcategory": "International Competition", "question": "How many sports were included in the 2020 Tokyo Olympics?", "options": ["33", "28", "40", "35"], "correct_answer": "33", "difficulty": "medium"},
    {"id": "spt_284", "category": "Sports", "subcategory": "International Competition", "question": "What is the name of the flame that burns throughout the Olympic Games?", "options": ["Olympic flame", "Eternal flame", "Victory flame", "Sacred flame"], "correct_answer": "Olympic flame", "difficulty": "medium"},
    {"id": "spt_285", "category": "Sports", "subcategory": "International Competition", "question": "Which athlete has won the most Olympic gold medals overall?", "options": ["Michael Phelps (23)", "Usain Bolt (8)", "Paavo Nurmi (9)", "Carl Lewis (9)"], "correct_answer": "Michael Phelps (23)", "difficulty": "medium"},

    # World Cup - Medium (3)
    {"id": "spt_286", "category": "Sports", "subcategory": "International Competition", "question": "Who is the all-time leading scorer in FIFA World Cup history?", "options": ["Miroslav Klose (16)", "Ronaldo (15)", "Gerd Müller (14)", "Just Fontaine (13)"], "correct_answer": "Miroslav Klose (16)", "difficulty": "medium"},
    {"id": "spt_287", "category": "Sports", "subcategory": "International Competition", "question": "Which country hosted the first FIFA World Cup in 1930?", "options": ["Uruguay", "Brazil", "Argentina", "Italy"], "correct_answer": "Uruguay", "difficulty": "medium"},
    {"id": "spt_288", "category": "Sports", "subcategory": "International Competition", "question": "How many teams compete in the FIFA World Cup finals?", "options": ["32", "24", "48", "16"], "correct_answer": "32", "difficulty": "medium"},

    # Other International - Medium (3)
    {"id": "spt_289", "category": "Sports", "subcategory": "International Competition", "question": "What is the international governing body for basketball?", "options": ["FIBA", "NBA", "IBF", "IBA"], "correct_answer": "FIBA", "difficulty": "medium"},
    {"id": "spt_290", "category": "Sports", "subcategory": "International Competition", "question": "Which tournament is known as the 'World Cup of Cricket'?", "options": ["ICC Cricket World Cup", "The Ashes", "IPL", "Big Bash"], "correct_answer": "ICC Cricket World Cup", "difficulty": "medium"},
    {"id": "spt_291", "category": "Sports", "subcategory": "International Competition", "question": "What is the premier international rugby union competition called?", "options": ["Rugby World Cup", "Six Nations", "The Rugby Championship", "European Rugby Cup"], "correct_answer": "Rugby World Cup", "difficulty": "medium"},

    # Olympics - Hard (5)
    {"id": "spt_292", "category": "Sports", "subcategory": "International Competition", "question": "Which Olympics were boycotted by the United States in 1980?", "options": ["Moscow", "Montreal", "Munich", "Seoul"], "correct_answer": "Moscow", "difficulty": "hard"},
    {"id": "spt_293", "category": "Sports", "subcategory": "International Competition", "question": "What is the minimum age requirement for Olympic boxing competitors?", "options": ["18", "16", "21", "17"], "correct_answer": "18", "difficulty": "hard"},
    {"id": "spt_294", "category": "Sports", "subcategory": "International Competition", "question": "Which nation has never won a Winter Olympic medal despite competing since 1924?", "options": ["Philippines", "Ecuador", "Bangladesh", "Panama"], "correct_answer": "Philippines", "difficulty": "hard"},
    {"id": "spt_295", "category": "Sports", "subcategory": "International Competition", "question": "What was the first Olympic Games to use electronic timing?", "options": ["1912 Stockholm", "1920 Antwerp", "1924 Paris", "1928 Amsterdam"], "correct_answer": "1912 Stockholm", "difficulty": "hard"},
    {"id": "spt_296", "category": "Sports", "subcategory": "International Competition", "question": "Which Summer Olympics were the first to be broadcast on television?", "options": ["1936 Berlin", "1948 London", "1952 Helsinki", "1956 Melbourne"], "correct_answer": "1936 Berlin", "difficulty": "hard"},

    # World Cup - Hard (2)
    {"id": "spt_297", "category": "Sports", "subcategory": "International Competition", "question": "Which player scored the fastest hat-trick in World Cup history?", "options": ["Fabienne Humm (Switzerland, 3 minutes)", "Carli Lloyd (USA, 13 minutes)", "Geoff Hurst (England, 1966)", "Just Fontaine (France, 1958)"], "correct_answer": "Fabienne Humm (Switzerland, 3 minutes)", "difficulty": "hard"},
    {"id": "spt_298", "category": "Sports", "subcategory": "International Competition", "question": "What is the trophy awarded to the World Cup winner called?", "options": ["FIFA World Cup Trophy", "Jules Rimet Trophy", "Golden Globe", "Victory Cup"], "correct_answer": "FIFA World Cup Trophy", "difficulty": "hard"},

    # Other International - Hard (2)
    {"id": "spt_299", "category": "Sports", "subcategory": "International Competition", "question": "Which country has won the most World Baseball Classic titles?", "options": ["Japan", "United States", "Dominican Republic", "Cuba"], "correct_answer": "Japan", "difficulty": "hard"},
    {"id": "spt_300", "category": "Sports", "subcategory": "International Competition", "question": "What is the maximum number of players on a volleyball team during international competition?", "options": ["6", "7", "5", "8"], "correct_answer": "6", "difficulty": "hard"}
]

def add_sports_questions():
    with open('Fiz/Resources/questions.json', 'r') as f:
        data = json.load(f)

    sports_questions = data['categories']['Sports']

    print(f"Current Sports questions: {len(sports_questions)}")
    print(f"Adding {len(new_questions)} new questions...")

    # Add new questions
    sports_questions.extend(new_questions)

    data['categories']['Sports'] = sports_questions

    with open('Fiz/Resources/questions.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Added {len(new_questions)} Sports questions")
    print(f"New total: {len(sports_questions)} questions")

    # Verify distribution
    from collections import defaultdict
    by_subcat = defaultdict(int)
    for q in new_questions:
        by_subcat[q['subcategory']] += 1

    print("\nDistribution of new questions:")
    for subcat, count in sorted(by_subcat.items()):
        print(f"  {subcat}: +{count}")

if __name__ == "__main__":
    add_sports_questions()
