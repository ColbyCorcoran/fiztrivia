#!/usr/bin/env python3
"""Add Sports History & Records and Athletes & Biography subcategories"""
import json

# Sports History & Records (50 questions) - 17 easy, 17 medium, 16 hard
history_records = []

# Easy questions (17)
easy_history = [
    ("spt_377", "Who holds the record for most Olympic gold medals?", ["Michael Phelps", "Usain Bolt", "Carl Lewis", "Mark Spitz"], "Michael Phelps", "easy"),
    ("spt_378", "What year did Jackie Robinson break baseball's color barrier?", ["1947", "1945", "1950", "1942"], "1947", "easy"),
    ("spt_379", "Who was the first athlete to run a mile in under 4 minutes?", ["Roger Bannister", "Paavo Nurmi", "Jesse Owens", "Emil Zátopek"], "Roger Bannister", "easy"),
    ("spt_380", "What year were the first modern Olympics held?", ["1896", "1900", "1892", "1888"], "1896", "easy"),
    ("spt_381", "Who hit the most home runs in MLB history?", ["Barry Bonds", "Hank Aaron", "Babe Ruth", "Alex Rodriguez"], "Barry Bonds", "easy"),
    ("spt_382", "What team won the first Super Bowl?", ["Green Bay Packers", "Kansas City Chiefs", "Dallas Cowboys", "New York Jets"], "Green Bay Packers", "easy"),
    ("spt_383", "Who was known as 'The Greatest' in boxing?", ["Muhammad Ali", "Mike Tyson", "Joe Louis", "Sugar Ray Robinson"], "Muhammad Ali", "easy"),
    ("spt_384", "What year did Title IX pass, advancing women's sports?", ["1972", "1965", "1980", "1975"], "1972", "easy"),
    ("spt_385", "Who was the first Black athlete to play in the NBA?", ["Earl Lloyd", "Chuck Cooper", "Nathaniel Clifton", "Bill Russell"], "Earl Lloyd", "easy"),
    ("spt_386", "What is the longest tennis match ever played?", ["11 hours 5 minutes (Isner-Mahut)", "8 hours", "6 hours", "4 hours"], "11 hours 5 minutes (Isner-Mahut)", "easy"),
    ("spt_387", "Who was the first gymnast to score a perfect 10?", ["Nadia Comăneci", "Olga Korbut", "Mary Lou Retton", "Simone Biles"], "Nadia Comăneci", "easy"),
    ("spt_388", "What year did basketball allow professionals in Olympics?", ["1992", "1988", "1996", "1984"], "1992", "easy"),
    ("spt_389", "Who scored 100 points in a single NBA game?", ["Wilt Chamberlain", "Kobe Bryant", "Michael Jordan", "LeBron James"], "Wilt Chamberlain", "easy"),
    ("spt_390", "What is the oldest continuous sporting event?", ["Kentucky Derby", "Wimbledon", "Boston Marathon", "America's Cup"], "Kentucky Derby", "easy"),
    ("spt_391", "Who was the first woman to run the Boston Marathon?", ["Kathrine Switzer", "Joan Benoit", "Grete Waitz", "Nina Kuscsik"], "Kathrine Switzer", "easy"),
    ("spt_392", "What year was the first World Cup held?", ["1930", "1928", "1932", "1926"], "1930", "easy"),
    ("spt_393", "Who holds the NFL career touchdown record?", ["Jerry Rice", "Emmitt Smith", "LaDainian Tomlinson", "Tom Brady"], "Jerry Rice", "easy"),
]

for q in easy_history:
    history_records.append({
        "id": q[0],
        "category": "Sports",
        "subcategory": "Sports History & Records",
        "question": q[1],
        "options": q[2],
        "correct_answer": q[3],
        "difficulty": q[4],
        "topic": None,
        "subtopic": None
    })

# Medium questions (17)
medium_history = [
    ("spt_394", "What team ended the longest championship drought in sports history in 2016?", ["Chicago Cubs (108 years)", "Boston Red Sox", "Cleveland Indians", "Philadelphia Eagles"], "Chicago Cubs (108 years)", "medium"),
    ("spt_395", "Who was the first athlete to earn $1 million per year?", ["Nolan Ryan", "Muhammad Ali", "Pelé", "Joe Namath"], "Nolan Ryan", "medium"),
    ("spt_396", "What year did the shot clock start in basketball?", ["1954", "1950", "1960", "1945"], "1954", "medium"),
    ("spt_397", "Who was the youngest heavyweight boxing champion?", ["Mike Tyson", "Muhammad Ali", "Floyd Patterson", "Evander Holyfield"], "Mike Tyson", "medium"),
    ("spt_398", "What is Babe Ruth's famous 'called shot' game?", ["1932 World Series", "1927 World Series", "1923 World Series", "1930 World Series"], "1932 World Series", "medium"),
    ("spt_399", "What year did the three-point line debut in the NBA?", ["1979", "1975", "1982", "1977"], "1979", "medium"),
    ("spt_400", "Who was the first European to win NBA MVP?", ["Dirk Nowitzki", "Tony Parker", "Pau Gasol", "Giannis Antetokounmpo"], "Dirk Nowitzki", "medium"),
    ("spt_401", "What sport was banned in England from 1457 to 1502?", ["Golf", "Tennis", "Football", "Cricket"], "Golf", "medium"),
    ("spt_402", "Who was the first baseball player to have their number retired?", ["Lou Gehrig", "Babe Ruth", "Jackie Robinson", "Joe DiMaggio"], "Lou Gehrig", "medium"),
    ("spt_403", "What year did the NFL and AFL merge?", ["1970", "1966", "1975", "1968"], "1970", "medium"),
    ("spt_404", "Who was the first woman to coach an NBA team?", ["Becky Hammon", "Nancy Lieberman", "Cheryl Reeve", "Geno Auriemma"], "Becky Hammon", "medium"),
    ("spt_405", "What is the 'Miracle on Ice'?", ["1980 US Olympic hockey win over USSR", "1960 US hockey gold", "1998 Czech hockey gold", "2002 Canadian hockey gold"], "1980 US Olympic hockey win over USSR", "medium"),
    ("spt_406", "What year did instant replay debut in NFL?", ["1986", "1980", "1990", "1975"], "1986", "medium"),
    ("spt_407", "Who broke Babe Ruth's single-season home run record first?", ["Roger Maris", "Hank Aaron", "Mark McGwire", "Barry Bonds"], "Roger Maris", "medium"),
    ("spt_408", "What is the Fosbury Flop?", ["High jump technique revolution", "Gymnastics move", "Pole vault technique", "Diving style"], "High jump technique revolution", "medium"),
    ("spt_409", "What year did women's boxing become an Olympic sport?", ["2012", "2008", "2016", "2004"], "2012", "medium"),
    ("spt_410", "Who was the first billion-dollar athlete?", ["Michael Jordan", "Tiger Woods", "LeBron James", "Cristiano Ronaldo"], "Michael Jordan", "medium"),
]

for q in medium_history:
    history_records.append({
        "id": q[0],
        "category": "Sports",
        "subcategory": "Sports History & Records",
        "question": q[1],
        "options": q[2],
        "correct_answer": q[3],
        "difficulty": q[4],
        "topic": None,
        "subtopic": None
    })

# Hard questions (16)
hard_history = [
    ("spt_411", "What is the Dempsey Roll?", ["Boxing weaving technique", "Football play", "Baseball pitch", "Basketball move"], "Boxing weaving technique", "hard"),
    ("spt_412", "Who won the first Heisman Trophy?", ["Jay Berwanger", "Larry Kelley", "Nile Kinnick", "Tom Harmon"], "Jay Berwanger", "hard"),
    ("spt_413", "What year did the designated hitter rule start in MLB?", ["1973", "1970", "1975", "1968"], "1973", "hard"),
    ("spt_414", "Who was the first athlete on a Wheaties box?", ["Lou Gehrig", "Babe Ruth", "Jack Armstrong (fictional)", "Bob Richards"], "Lou Gehrig", "hard"),
    ("spt_415", "What is the Sullivan Award?", ["Top amateur athlete award", "Coaching achievement", "Sportsmanship award", "Olympic medal"], "Top amateur athlete award", "hard"),
    ("spt_416", "What team completed the first perfect season in NFL?", ["1972 Miami Dolphins", "1985 Chicago Bears", "2007 New England Patriots", "1978 Pittsburgh Steelers"], "1972 Miami Dolphins", "hard"),
    ("spt_417", "What year did basketball introduce the 24-second shot clock?", ["1954", "1950", "1960", "1947"], "1954", "hard"),
    ("spt_418", "Who was the first Olympic athlete to win gold in same event in four consecutive Olympics?", ["Al Oerter (discus)", "Carl Lewis", "Michael Phelps", "Paul Elvstrøm"], "Al Oerter (discus)", "hard"),
    ("spt_419", "What is the Dick Fosbury technique revolution year?", ["1968", "1964", "1972", "1960"], "1968", "hard"),
    ("spt_420", "What boxing match was the 'Rumble in the Jungle'?", ["Ali vs. Foreman 1974", "Ali vs. Frazier", "Ali vs. Liston", "Tyson vs. Holyfield"], "Ali vs. Foreman 1974", "hard"),
    ("spt_421", "What is the Bradman Average in cricket?", ["99.94 batting average", "100 runs per match", "50 wickets per season", "10 centuries"], "99.94 batting average", "hard"),
    ("spt_422", "Who was the first openly gay athlete in major US sports?", ["Jason Collins (NBA)", "Michael Sam (NFL)", "Robbie Rogers (MLS)", "Glenn Burke (MLB)"], "Jason Collins (NBA)", "hard"),
    ("spt_423", "What year did the forward pass become legal in football?", ["1906", "1900", "1910", "1920"], "1906", "hard"),
    ("spt_424", "What is the Paavo Nurmi Award?", ["Outstanding distance runner", "Sprint achievement", "Field event excellence", "Olympic medal count"], "Outstanding distance runner", "hard"),
    ("spt_425", "Who was the first Black woman to win Wimbledon?", ["Althea Gibson", "Serena Williams", "Venus Williams", "Zina Garrison"], "Althea Gibson", "hard"),
    ("spt_426", "What year did hockey adopt the center red line?", ["1943", "1940", "1950", "1935"], "1943", "hard"),
]

for q in hard_history:
    history_records.append({
        "id": q[0],
        "category": "Sports",
        "subcategory": "Sports History & Records",
        "question": q[1],
        "options": q[2],
        "correct_answer": q[3],
        "difficulty": q[4],
        "topic": None,
        "subtopic": None
    })

# Athletes & Biography (50 questions) - 17 easy, 17 medium, 16 hard
athletes_bio = []

# Easy questions (17)
easy_athletes = [
    ("spt_427", "What sport did Michael Jordan play professionally?", ["Basketball", "Baseball", "Golf", "Tennis"], "Basketball", "easy"),
    ("spt_428", "What number did Michael Jordan wear for most of his career?", ["23", "32", "45", "12"], "23", "easy"),
    ("spt_429", "Which Williams sister has won more Grand Slam singles titles?", ["Serena Williams", "Venus Williams", "Equal", "Neither won any"], "Serena Williams", "easy"),
    ("spt_430", "What country is Usain Bolt from?", ["Jamaica", "Kenya", "Ethiopia", "United States"], "Jamaica", "easy"),
    ("spt_431", "What sport did Babe Ruth play?", ["Baseball", "Basketball", "Football", "Boxing"], "Baseball", "easy"),
    ("spt_432", "Who is known as 'King James' in basketball?", ["LeBron James", "James Harden", "Michael Jordan", "Magic Johnson"], "LeBron James", "easy"),
    ("spt_433", "What country is Cristiano Ronaldo from?", ["Portugal", "Spain", "Brazil", "Argentina"], "Portugal", "easy"),
    ("spt_434", "Who is known as 'The Great One' in hockey?", ["Wayne Gretzky", "Bobby Orr", "Mario Lemieux", "Gordie Howe"], "Wayne Gretzky", "easy"),
    ("spt_435", "What position did Tom Brady play?", ["Quarterback", "Running back", "Wide receiver", "Linebacker"], "Quarterback", "easy"),
    ("spt_436", "Who is considered the greatest boxer of all time?", ["Muhammad Ali", "Mike Tyson", "Floyd Mayweather", "Sugar Ray Leonard"], "Muhammad Ali", "easy"),
    ("spt_437", "What sport did Tiger Woods revolutionize?", ["Golf", "Tennis", "Boxing", "Swimming"], "Golf", "easy"),
    ("spt_438", "Who won the most Super Bowl rings as a player?", ["Tom Brady", "Joe Montana", "Terry Bradshaw", "Charles Haley"], "Tom Brady", "easy"),
    ("spt_439", "What country is Pelé from?", ["Brazil", "Argentina", "Portugal", "Spain"], "Brazil", "easy"),
    ("spt_440", "Who is known as 'His Airness'?", ["Michael Jordan", "LeBron James", "Kobe Bryant", "Julius Erving"], "Michael Jordan", "easy"),
    ("spt_441", "What sport did Simone Biles dominate?", ["Gymnastics", "Swimming", "Track and field", "Figure skating"], "Gymnastics", "easy"),
    ("spt_442", "Who holds the record for most career points in NBA?", ["LeBron James", "Kareem Abdul-Jabbar", "Karl Malone", "Kobe Bryant"], "LeBron James", "easy"),
    ("spt_443", "What position did Mia Hamm play in soccer?", ["Forward", "Midfielder", "Defender", "Goalkeeper"], "Forward", "easy"),
]

for q in easy_athletes:
    athletes_bio.append({
        "id": q[0],
        "category": "Sports",
        "subcategory": "Athletes & Biography",
        "question": q[1],
        "options": q[2],
        "correct_answer": q[3],
        "difficulty": q[4],
        "topic": None,
        "subtopic": None
    })

# Medium questions (17)
medium_athletes = [
    ("spt_444", "Who was known as 'Dr. J' in basketball?", ["Julius Erving", "Magic Johnson", "Larry Bird", "Kareem Abdul-Jabbar"], "Julius Erving", "medium"),
    ("spt_445", "What illness did Lou Gehrig have?", ["ALS (Amyotrophic Lateral Sclerosis)", "Cancer", "Alzheimer's", "Parkinson's"], "ALS (Amyotrophic Lateral Sclerosis)", "medium"),
    ("spt_446", "Who was the first female gymnast to score a perfect 10?", ["Nadia Comăneci", "Olga Korbut", "Mary Lou Retton", "Simone Biles"], "Nadia Comăneci", "medium"),
    ("spt_447", "What college did Michael Jordan attend?", ["University of North Carolina", "Duke University", "UCLA", "Georgetown"], "University of North Carolina", "medium"),
    ("spt_448", "Who was known as 'The Iron Horse'?", ["Lou Gehrig", "Cal Ripken Jr.", "Babe Ruth", "Joe DiMaggio"], "Lou Gehrig", "medium"),
    ("spt_449", "What sport did Bo Jackson play professionally (two sports)?", ["Football and Baseball", "Basketball and Baseball", "Football and Basketball", "Baseball and Hockey"], "Football and Baseball", "medium"),
    ("spt_450", "Who was the first woman to dunk in a WNBA game?", ["Lisa Leslie", "Candace Parker", "Brittney Griner", "Sheryl Swoopes"], "Lisa Leslie", "medium"),
    ("spt_451", "What year did Kobe Bryant retire?", ["2016", "2015", "2017", "2014"], "2016", "medium"),
    ("spt_452", "Who was known as 'Rocket' Richard in hockey?", ["Maurice Richard", "Henri Richard", "Bobby Hull", "Gordie Howe"], "Maurice Richard", "medium"),
    ("spt_453", "What position did Derek Jeter play?", ["Shortstop", "Second base", "Third base", "Outfield"], "Shortstop", "medium"),
    ("spt_454", "Who was the first Black Formula 1 driver?", ["Lewis Hamilton", "Willy T. Ribbs", "Marc Gené", "Karun Chandhok"], "Lewis Hamilton", "medium"),
    ("spt_455", "What tragic event ended Ayrton Senna's life?", ["Racing crash at San Marino GP", "Plane crash", "Heart attack", "Training accident"], "Racing crash at San Marino GP", "medium"),
    ("spt_456", "Who was known as 'The Golden Bear' in golf?", ["Jack Nicklaus", "Arnold Palmer", "Gary Player", "Tiger Woods"], "Jack Nicklaus", "medium"),
    ("spt_457", "What disease did Muhammad Ali battle later in life?", ["Parkinson's disease", "Alzheimer's", "ALS", "Dementia"], "Parkinson's disease", "medium"),
    ("spt_458", "Who was the first woman to play in a men's professional sports league?", ["Billie Jean King (exhibition)", "Jackie Mitchell (baseball)", "Manon Rhéaume (hockey)", "Danica Patrick (racing)"], "Billie Jean King (exhibition)", "medium"),
    ("spt_459", "What number did Kobe Bryant wear after switching from 8?", ["24", "23", "32", "33"], "24", "medium"),
    ("spt_460", "Who was known as 'The Big Unit'?", ["Randy Johnson", "Shaquille O'Neal", "Wilt Chamberlain", "David Robinson"], "Randy Johnson", "medium"),
]

for q in medium_athletes:
    athletes_bio.append({
        "id": q[0],
        "category": "Sports",
        "subcategory": "Athletes & Biography",
        "question": q[1],
        "options": q[2],
        "correct_answer": q[3],
        "difficulty": q[4],
        "topic": None,
        "subtopic": None
    })

# Hard questions (16)
hard_athletes = [
    ("spt_461", "Who was the first athlete to appear on a Wheaties box?", ["Lou Gehrig", "Babe Ruth", "Bob Richards", "Jack Armstrong"], "Lou Gehrig", "hard"),
    ("spt_462", "What was Jim Thorpe's Native American name?", ["Wa-Tho-Huk", "Sitting Bull", "Crazy Horse", "Red Cloud"], "Wa-Tho-Huk", "hard"),
    ("spt_463", "Who was the first player to break the MLB color barrier?", ["Jackie Robinson", "Larry Doby", "Satchel Paige", "Willie Mays"], "Jackie Robinson", "hard"),
    ("spt_464", "What year did Jesse Owens win four gold medals at Berlin Olympics?", ["1936", "1932", "1940", "1928"], "1936", "hard"),
    ("spt_465", "Who was known as 'The Manassa Mauler'?", ["Jack Dempsey", "Joe Louis", "Rocky Marciano", "Gene Tunney"], "Jack Dempsey", "hard"),
    ("spt_466", "What was Secretariat's margin of victory in 1973 Belmont Stakes?", ["31 lengths", "20 lengths", "15 lengths", "10 lengths"], "31 lengths", "hard"),
    ("spt_467", "Who was the first Black player in NHL?", ["Willie O'Ree", "Grant Fuhr", "Jarome Iginla", "P.K. Subban"], "Willie O'Ree", "hard"),
    ("spt_468", "What was Knute Rockne's famous 'Win one for the Gipper' speech about?", ["George Gipp", "Elmer Layden", "Harry Stuhldreher", "Jim Crowley"], "George Gipp", "hard"),
    ("spt_469", "Who was the first woman to compete in Indianapolis 500?", ["Janet Guthrie", "Danica Patrick", "Sarah Fisher", "Lyn St. James"], "Janet Guthrie", "hard"),
    ("spt_470", "What disease did Roberto Clemente die delivering aid for?", ["Earthquake relief (plane crash)", "Hurricane relief", "Famine relief", "Flood relief"], "Earthquake relief (plane crash)", "hard"),
    ("spt_471", "Who was known as 'Shoeless Joe'?", ["Joe Jackson", "Joe DiMaggio", "Joe Morgan", "Joe Torre"], "Joe Jackson", "hard"),
    ("spt_472", "What year did Arthur Ashe win Wimbledon?", ["1975", "1973", "1970", "1977"], "1975", "hard"),
    ("spt_473", "Who was the first athlete to win Olympic gold medals in both Summer and Winter Games?", ["Eddie Eagan", "Clara Hughes", "Christa Luding-Rothenburger", "Lauryn Williams"], "Eddie Eagan", "hard"),
    ("spt_474", "What was Wilma Rudolph's childhood illness she overcame?", ["Polio", "Scarlet fever", "Tuberculosis", "Rheumatic fever"], "Polio", "hard"),
    ("spt_475", "Who was known as 'The Galloping Ghost'?", ["Red Grange", "Jim Thorpe", "Bronko Nagurski", "Sammy Baugh"], "Red Grange", "hard"),
    ("spt_476", "What year did Roger Bannister break the 4-minute mile?", ["1954", "1952", "1956", "1950"], "1954", "hard"),
]

for q in hard_athletes:
    athletes_bio.append({
        "id": q[0],
        "category": "Sports",
        "subcategory": "Athletes & Biography",
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

# Add both subcategories
data['categories']['Sports'].extend(history_records)
data['categories']['Sports'].extend(athletes_bio)

# Sort
data['categories']['Sports'].sort(key=lambda q: int(q['id'].split('_')[1]))

# Save
with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Added 50 Sports History & Records questions")
print(f"   - {len([q for q in history_records if q['difficulty'] == 'easy'])} easy")
print(f"   - {len([q for q in history_records if q['difficulty'] == 'medium'])} medium")
print(f"   - {len([q for q in history_records if q['difficulty'] == 'hard'])} hard")
print()
print("✅ Added 50 Athletes & Biography questions")
print(f"   - {len([q for q in athletes_bio if q['difficulty'] == 'easy'])} easy")
print(f"   - {len([q for q in athletes_bio if q['difficulty'] == 'medium'])} medium")
print(f"   - {len([q for q in athletes_bio if q['difficulty'] == 'hard'])} hard")
print(f"\n✅ Sports category now has {len(data['categories']['Sports'])} total questions")
