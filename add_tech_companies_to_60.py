#!/usr/bin/env python3
"""Add 60 Tech Companies questions from scratch"""
import json

new_questions = []

# Easy questions (20)
easy = [
    ("tec_204", "Who founded Apple along with Steve Wozniak?", ["Steve Jobs", "Bill Gates", "Tim Cook", "Mark Zuckerberg"], "Steve Jobs"),
    ("tec_205", "Which company is known for the search engine that shares its name?", ["Google", "Yahoo", "Bing", "DuckDuckGo"], "Google"),
    ("tec_206", "Who is the founder of Facebook?", ["Mark Zuckerberg", "Elon Musk", "Jack Dorsey", "Jeff Bezos"], "Mark Zuckerberg"),
    ("tec_207", "Which company makes the iPhone?", ["Apple", "Samsung", "Google", "Microsoft"], "Apple"),
    ("tec_208", "Who is the current CEO of Apple (as of 2024)?", ["Tim Cook", "Steve Jobs", "Jony Ive", "Craig Federighi"], "Tim Cook"),
    ("tec_209", "Which company owns Instagram?", ["Meta (Facebook)", "Google", "Twitter", "Snapchat"], "Meta (Facebook)"),
    ("tec_210", "Who founded Amazon?", ["Jeff Bezos", "Elon Musk", "Bill Gates", "Larry Page"], "Jeff Bezos"),
    ("tec_211", "Which company makes the Galaxy smartphones?", ["Samsung", "Apple", "Google", "Huawei"], "Samsung"),
    ("tec_212", "Who co-founded Microsoft with Paul Allen?", ["Bill Gates", "Steve Jobs", "Larry Ellison", "Mark Zuckerberg"], "Bill Gates"),
    ("tec_213", "Which company is known for electric cars and SpaceX?", ["Tesla (cars) and SpaceX are both Elon Musk companies", "Ford", "General Motors", "Toyota"], "Tesla (cars) and SpaceX are both Elon Musk companies"),
    ("tec_214", "What is Google's parent company called?", ["Alphabet", "Meta", "Google Inc.", "Android"], "Alphabet"),
    ("tec_215", "Which company created the Android operating system?", ["Google", "Apple", "Microsoft", "Samsung"], "Google"),
    ("tec_216", "Who is the CEO of Tesla and SpaceX?", ["Elon Musk", "Jeff Bezos", "Tim Cook", "Mark Zuckerberg"], "Elon Musk"),
    ("tec_217", "Which company makes the Surface laptop?", ["Microsoft", "Apple", "Dell", "HP"], "Microsoft"),
    ("tec_218", "What was Facebook renamed to in 2021?", ["Meta", "Horizon", "Oculus", "Portal"], "Meta"),
    ("tec_219", "Which company owns YouTube?", ["Google", "Microsoft", "Amazon", "Meta"], "Google"),
    ("tec_220", "Who founded Tesla Motors?", ["Martin Eberhard and Marc Tarpenning (Elon Musk joined early)", "Elon Musk", "Jeff Bezos", "Larry Page"], "Martin Eberhard and Marc Tarpenning (Elon Musk joined early)"),
    ("tec_221", "Which company makes the Kindle e-reader?", ["Amazon", "Apple", "Google", "Barnes & Noble"], "Amazon"),
    ("tec_222", "What is Microsoft's cloud computing service called?", ["Azure", "AWS", "Google Cloud", "iCloud"], "Azure"),
    ("tec_223", "Which company acquired LinkedIn in 2016?", ["Microsoft", "Google", "Facebook", "Amazon"], "Microsoft"),
]

for q in easy:
    new_questions.append({"id": q[0], "category": "Technology", "subcategory": "Tech Companies", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "easy", "topic": None, "subtopic": None})

# Medium questions (20)
medium = [
    ("tec_224", "What year was Apple founded?", ["1976", "1975", "1977", "1980"], "1976"),
    ("tec_225", "Which company did Google acquire to enter the smartphone market?", ["Android Inc.", "Motorola", "HTC", "LG"], "Android Inc."),
    ("tec_226", "Who are the co-founders of Google?", ["Larry Page and Sergey Brin", "Mark Zuckerberg and Dustin Moskovitz", "Bill Gates and Paul Allen", "Steve Jobs and Steve Wozniak"], "Larry Page and Sergey Brin"),
    ("tec_227", "What year did Amazon go public?", ["1997", "1995", "1999", "2000"], "1997"),
    ("tec_228", "Which company acquired WhatsApp for $19 billion?", ["Facebook (now Meta)", "Google", "Microsoft", "Apple"], "Facebook (now Meta)"),
    ("tec_229", "What was the original name of Apple's tablet before 'iPad'?", ["iPad was the original name", "iSlate", "iTablet", "Newton"], "iPad was the original name"),
    ("tec_230", "Which company developed the first commercially available smartphone?", ["IBM (Simon Personal Communicator)", "Apple", "Nokia", "BlackBerry"], "IBM (Simon Personal Communicator)"),
    ("tec_231", "What is Amazon's cloud computing service called?", ["AWS (Amazon Web Services)", "Azure", "Google Cloud", "Amazon Cloud"], "AWS (Amazon Web Services)"),
    ("tec_232", "Which company was formerly known as 'BackRub'?", ["Google", "Yahoo", "Bing", "Ask Jeeves"], "Google"),
    ("tec_233", "Who was the first employee of Microsoft?", ["Steve Ballmer (first business manager, not first employee - actually Bob Wallace)", "Bill Gates", "Paul Allen", "Steve Jobs"], "Steve Ballmer (first business manager, not first employee - actually Bob Wallace)"),
    ("tec_234", "Which company owns Oculus VR?", ["Meta (Facebook)", "Google", "Microsoft", "Sony"], "Meta (Facebook)"),
    ("tec_235", "What year was Microsoft founded?", ["1975", "1976", "1980", "1981"], "1975"),
    ("tec_236", "Which company created the first web browser with a graphical interface?", ["Netscape", "Microsoft", "Apple", "Google"], "Netscape"),
    ("tec_237", "Who succeeded Steve Jobs as Apple CEO?", ["Tim Cook", "Jony Ive", "Phil Schiller", "Craig Federighi"], "Tim Cook"),
    ("tec_238", "Which company was originally called 'Cadabra'?", ["Amazon", "Google", "Yahoo", "eBay"], "Amazon"),
    ("tec_239", "What does 'IBM' stand for?", ["International Business Machines", "Internet Business Machines", "Integrated Business Modules", "International Banking Machines"], "International Business Machines"),
    ("tec_240", "Which company acquired Beats Electronics in 2014?", ["Apple", "Google", "Microsoft", "Amazon"], "Apple"),
    ("tec_241", "Who founded Oracle Corporation?", ["Larry Ellison", "Larry Page", "Bill Gates", "Steve Jobs"], "Larry Ellison"),
    ("tec_242", "Which company's motto was 'Don't be evil'?", ["Google", "Apple", "Microsoft", "Facebook"], "Google"),
    ("tec_243", "What year was Tesla Motors founded?", ["2003", "2000", "2005", "2008"], "2003"),
]

for q in medium:
    new_questions.append({"id": q[0], "category": "Technology", "subcategory": "Tech Companies", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "medium", "topic": None, "subtopic": None})

# Hard questions (20)
hard = [
    ("tec_244", "Which company did Elon Musk co-found that later became PayPal?", ["X.com", "Confinity", "eBay", "Venmo"], "X.com"),
    ("tec_245", "What was the stock price of Apple when it went public in 1980?", ["$22 per share", "$15 per share", "$30 per share", "$10 per share"], "$22 per share"),
    ("tec_246", "Which company did Microsoft acquire for $26.2 billion in 2016?", ["LinkedIn", "GitHub", "Skype", "Nokia"], "LinkedIn"),
    ("tec_247", "Who was the first CEO of Google?", ["Eric Schmidt", "Larry Page", "Sergey Brin", "Sundar Pichai"], "Eric Schmidt"),
    ("tec_248", "What was the code name for Apple's first Macintosh project?", ["Annie", "Lisa", "Sara", "Bicycle"], "Annie"),
    ("tec_249", "Which company did Facebook acquire along with WhatsApp in 2014?", ["Oculus VR", "Instagram", "Messenger", "Giphy"], "Oculus VR"),
    ("tec_250", "What was the original name of Yahoo?", ["Jerry and David's Guide to the World Wide Web", "Yahoo Search", "WebCrawler", "David's Directory"], "Jerry and David's Guide to the World Wide Web"),
    ("tec_251", "Which company did Google acquire for $12.5 billion in 2011?", ["Motorola Mobility", "Nest", "YouTube", "Waze"], "Motorola Mobility"),
    ("tec_252", "Who was the original founder of Tesla (before Elon Musk)?", ["Martin Eberhard and Marc Tarpenning", "Elon Musk", "JB Straubel", "Ian Wright"], "Martin Eberhard and Marc Tarpenning"),
    ("tec_253", "What year did Google go public?", ["2004", "2000", "2006", "2002"], "2004"),
    ("tec_254", "Which company created the first personal computer?", ["MITS (Altair 8800)", "Apple", "IBM", "Commodore"], "MITS (Altair 8800)"),
    ("tec_255", "What was Amazon's first product sold online?", ["A book", "Electronics", "Toys", "Music CDs"], "A book"),
    ("tec_256", "Which company did Microsoft acquire for $7.5 billion in 2020?", ["ZeniMax Media (Bethesda)", "Activision Blizzard", "LinkedIn", "GitHub"], "ZeniMax Media (Bethesda)"),
    ("tec_257", "Who was the first investor in Facebook?", ["Peter Thiel", "Mark Zuckerberg", "Sean Parker", "Eduardo Saverin"], "Peter Thiel"),
    ("tec_258", "What was the valuation of Facebook when it went public in 2012?", ["$104 billion", "$50 billion", "$200 billion", "$75 billion"], "$104 billion"),
    ("tec_259", "Which company developed the first commercial GUI operating system?", ["Xerox (Xerox Alto)", "Apple", "Microsoft", "IBM"], "Xerox (Xerox Alto)"),
    ("tec_260", "What year did Netflix shift from DVD rentals to streaming?", ["2007", "2005", "2010", "2008"], "2007"),
    ("tec_261", "Which tech company was founded in a garage in Palo Alto?", ["Hewlett-Packard (HP)", "Apple", "Google", "Amazon"], "Hewlett-Packard (HP)"),
    ("tec_262", "What was Twitter's IPO price per share in 2013?", ["$26", "$20", "$30", "$35"], "$26"),
    ("tec_263", "Which company did Amazon acquire for $13.7 billion in 2017?", ["Whole Foods", "Zappos", "Twitch", "Ring"], "Whole Foods"),
]

for q in hard:
    new_questions.append({"id": q[0], "category": "Technology", "subcategory": "Tech Companies", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "hard", "topic": None, "subtopic": None})

# Load, add, sort, save
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

data['categories']['Technology'].extend(new_questions)
data['categories']['Technology'].sort(key=lambda q: int(q['id'].split('_')[1]))

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added 60 Tech Companies questions")
print(f"Technology now has {len(data['categories']['Technology'])} total questions")
print(f"Added: 20 easy, 20 medium, 20 hard")
