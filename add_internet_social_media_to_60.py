#!/usr/bin/env python3
"""Add 60 Internet & Social Media questions from scratch"""
import json

new_questions = []

# Easy questions (20)
easy = [
    ("tec_144", "What does 'WWW' stand for?", ["World Wide Web", "Wide World Web", "World Web Wide", "Web World Wide"], "World Wide Web"),
    ("tec_145", "Which social media platform is known for 280-character posts?", ["Twitter/X", "Facebook", "Instagram", "LinkedIn"], "Twitter/X"),
    ("tec_146", "What color is the Facebook logo?", ["Blue", "Red", "Green", "Purple"], "Blue"),
    ("tec_147", "Which video platform was acquired by Google in 2006?", ["YouTube", "Vimeo", "Dailymotion", "Twitch"], "YouTube"),
    ("tec_148", "What does 'URL' stand for?", ["Uniform Resource Locator", "Universal Resource Link", "Unified Resource Location", "Universal Reference Locator"], "Uniform Resource Locator"),
    ("tec_149", "Which social media platform uses hashtags most prominently?", ["Twitter/X", "Facebook", "LinkedIn", "Snapchat"], "Twitter/X"),
    ("tec_150", "What is the maximum length of a YouTube video username?", ["Not applicable - usernames vary", "15 characters", "20 characters", "30 characters"], "Not applicable - usernames vary"),
    ("tec_151", "Which streaming service is known for its red logo?", ["Netflix", "Hulu", "Disney+", "Amazon Prime"], "Netflix"),
    ("tec_152", "What does 'DM' stand for on social media?", ["Direct Message", "Digital Mail", "Direct Mail", "Data Message"], "Direct Message"),
    ("tec_153", "Which social media platform is owned by Meta?", ["Instagram", "Twitter", "TikTok", "Snapchat"], "Instagram"),
    ("tec_154", "What search engine has a colorful logo?", ["Google", "Bing", "Yahoo", "DuckDuckGo"], "Google"),
    ("tec_155", "Which platform is known for short-form videos and dances?", ["TikTok", "YouTube", "Instagram", "Vine"], "TikTok"),
    ("tec_156", "What does 'ISP' stand for?", ["Internet Service Provider", "Internet Search Protocol", "Internal System Provider", "Integrated Service Platform"], "Internet Service Provider"),
    ("tec_157", "Which emoji shows a face crying with laughter?", ["😂", "😭", "😅", "🤣"], "😂"),
    ("tec_158", "What is Google's email service called?", ["Gmail", "Outlook", "Yahoo Mail", "ProtonMail"], "Gmail"),
    ("tec_159", "Which social media platform is primarily for professional networking?", ["LinkedIn", "Facebook", "Instagram", "Twitter"], "LinkedIn"),
    ("tec_160", "What does '@' symbol represent on social media?", ["Mention/Tag a user", "Email address", "Location", "Hashtag"], "Mention/Tag a user"),
    ("tec_161", "Which streaming platform is owned by Amazon?", ["Prime Video", "Netflix", "Hulu", "HBO Max"], "Prime Video"),
    ("tec_162", "What does 'WiFi' stand for?", ["Wireless Fidelity", "Wide Fidelity", "Wireless File", "Wire-Free Internet"], "Wireless Fidelity"),
    ("tec_163", "Which social media platform has a ghost as its logo?", ["Snapchat", "WhatsApp", "Telegram", "Discord"], "Snapchat"),
]

for q in easy:
    new_questions.append({"id": q[0], "category": "Technology", "subcategory": "Internet & Social Media", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "easy", "topic": None, "subtopic": None})

# Medium questions (20)
medium = [
    ("tec_164", "What year was Facebook founded?", ["2004", "2003", "2005", "2006"], "2004"),
    ("tec_165", "Which company owns WhatsApp?", ["Meta (Facebook)", "Google", "Microsoft", "Apple"], "Meta (Facebook)"),
    ("tec_166", "What was Twitter's original character limit before it was increased to 280?", ["140", "100", "120", "160"], "140"),
    ("tec_167", "Which protocol is used for secure web browsing?", ["HTTPS", "HTTP", "FTP", "SMTP"], "HTTPS"),
    ("tec_168", "What does 'VPN' stand for?", ["Virtual Private Network", "Virtual Public Network", "Variable Private Network", "Verified Private Network"], "Virtual Private Network"),
    ("tec_169", "Which video game streaming platform was acquired by Amazon?", ["Twitch", "YouTube Gaming", "Mixer", "Facebook Gaming"], "Twitch"),
    ("tec_170", "What year was YouTube founded?", ["2005", "2004", "2006", "2007"], "2005"),
    ("tec_171", "Which social media platform was known for 6-second videos?", ["Vine", "TikTok", "Instagram", "Snapchat"], "Vine"),
    ("tec_172", "What does 'SEO' stand for?", ["Search Engine Optimization", "Social Engine Optimization", "Search Engine Operation", "Site Engine Optimization"], "Search Engine Optimization"),
    ("tec_173", "Which company created the Chrome browser?", ["Google", "Microsoft", "Apple", "Mozilla"], "Google"),
    ("tec_174", "What is Reddit's mascot called?", ["Snoo", "Doo", "Roo", "Blue"], "Snoo"),
    ("tec_175", "Which email protocol is used for receiving emails?", ["IMAP or POP3", "SMTP", "FTP", "HTTP"], "IMAP or POP3"),
    ("tec_176", "What was the original name of Twitter before rebranding to X?", ["Twitter (it's now called X)", "Twttr", "Chirp", "Tweet"], "Twitter (it's now called X)"),
    ("tec_177", "Which search engine focuses on user privacy?", ["DuckDuckGo", "Google", "Bing", "Yahoo"], "DuckDuckGo"),
    ("tec_178", "What does 'AMA' stand for on Reddit?", ["Ask Me Anything", "Against Medical Advice", "American Medical Association", "Automated Message Alert"], "Ask Me Anything"),
    ("tec_179", "Which social media platform was acquired by Elon Musk in 2022?", ["Twitter (now X)", "Facebook", "Instagram", "TikTok"], "Twitter (now X)"),
    ("tec_180", "What is the name of Discord's currency?", ["Nitro", "Discord Coins", "Server Tokens", "Chat Credits"], "Nitro"),
    ("tec_181", "Which country banned TikTok nationwide in 2020?", ["India", "United States", "China", "Australia"], "India"),
    ("tec_182", "What does 'FOMO' stand for in internet slang?", ["Fear Of Missing Out", "Find Out More Online", "Follow On My Own", "First Online Meeting Only"], "Fear Of Missing Out"),
    ("tec_183", "Which messaging app uses end-to-end encryption by default?", ["Signal", "Facebook Messenger", "Telegram", "Discord"], "Signal"),
]

for q in medium:
    new_questions.append({"id": q[0], "category": "Technology", "subcategory": "Internet & Social Media", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "medium", "topic": None, "subtopic": None})

# Hard questions (20)
hard = [
    ("tec_184", "What year was the first email sent?", ["1971", "1969", "1975", "1980"], "1971"),
    ("tec_185", "Which protocol do most instant messaging services use?", ["XMPP or proprietary protocols", "HTTP", "FTP", "SMTP"], "XMPP or proprietary protocols"),
    ("tec_186", "What was the first social media site to reach 1 million users?", ["Friendster", "MySpace", "Facebook", "SixDegrees"], "Friendster"),
    ("tec_187", "Which internet protocol assigns IP addresses automatically?", ["DHCP", "DNS", "HTTP", "FTP"], "DHCP"),
    ("tec_188", "What does 'ICANN' stand for?", ["Internet Corporation for Assigned Names and Numbers", "International Computer and Network Names", "Internet Control and Access Network Node", "Integrated Communication Access Network Node"], "Internet Corporation for Assigned Names and Numbers"),
    ("tec_189", "Which social media platform was originally called 'The Facebook'?", ["Facebook", "Friendster", "MySpace", "LinkedIn"], "Facebook"),
    ("tec_190", "What is the maximum file size for a standard email attachment (most providers)?", ["25 MB", "10 MB", "50 MB", "100 MB"], "25 MB"),
    ("tec_191", "Which company developed the Tor browser for anonymous browsing?", ["The Tor Project (nonprofit)", "Mozilla", "Google", "Opera"], "The Tor Project (nonprofit)"),
    ("tec_192", "What year was the first tweet sent?", ["2006", "2004", "2005", "2007"], "2006"),
    ("tec_193", "Which top-level domain (TLD) was the first ever created?", [".com", ".net", ".org", ".edu"], ".com"),
    ("tec_194", "What does 'RSS' stand for in web feeds?", ["Really Simple Syndication", "Rich Site Summary", "Remote System Service", "Real-time Streaming Service"], "Really Simple Syndication"),
    ("tec_195", "Which platform pioneered the concept of 'Stories' that disappear after 24 hours?", ["Snapchat", "Instagram", "Facebook", "WhatsApp"], "Snapchat"),
    ("tec_196", "What was the first registered domain name?", ["symbolics.com", "google.com", "yahoo.com", "mit.edu"], "symbolics.com"),
    ("tec_197", "Which internet meme featuring a frog was designated a hate symbol?", ["Pepe the Frog", "Doge", "Grumpy Cat", "Nyan Cat"], "Pepe the Frog"),
    ("tec_198", "What does 'WebRTC' stand for?", ["Web Real-Time Communication", "Web Remote Transfer Control", "Website Real-Time Content", "Web Resource Transfer Connection"], "Web Real-Time Communication"),
    ("tec_199", "Which company created the first web browser with a GUI?", ["NCSA (Mosaic)", "Netscape", "Microsoft", "Apple"], "NCSA (Mosaic)"),
    ("tec_200", "What year was Instagram launched?", ["2010", "2009", "2011", "2012"], "2010"),
    ("tec_201", "Which internet protocol is used for transferring files?", ["FTP", "HTTP", "SMTP", "POP3"], "FTP"),
    ("tec_202", "What was the original purpose of LinkedIn when launched in 2003?", ["Professional networking", "Job searching only", "Resume hosting", "Company reviews"], "Professional networking"),
    ("tec_203", "Which social media platform has the most active users as of 2024?", ["Facebook", "YouTube", "Instagram", "TikTok"], "Facebook"),
]

for q in hard:
    new_questions.append({"id": q[0], "category": "Technology", "subcategory": "Internet & Social Media", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "hard", "topic": None, "subtopic": None})

# Load, add, sort, save
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

data['categories']['Technology'].extend(new_questions)
data['categories']['Technology'].sort(key=lambda q: int(q['id'].split('_')[1]))

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added 60 Internet & Social Media questions")
print(f"Technology now has {len(data['categories']['Technology'])} total questions")
print(f"Added: 20 easy, 20 medium, 20 hard")
