#!/usr/bin/env python3
"""Add 60 Computers & Software questions from scratch"""
import json

new_questions = []

# Easy questions (20)
easy = [
    ("tec_084", "What does 'OS' stand for?", ["Operating System", "Online Service", "Open Source", "Output System"], "Operating System"),
    ("tec_085", "Which company makes Windows?", ["Microsoft", "Apple", "Google", "IBM"], "Microsoft"),
    ("tec_086", "What does 'USB' stand for?", ["Universal Serial Bus", "United System Bus", "Universal Storage Base", "Uniform Serial Buffer"], "Universal Serial Bus"),
    ("tec_087", "Which company makes macOS?", ["Apple", "Microsoft", "Google", "Dell"], "Apple"),
    ("tec_088", "What is the most common file format for documents?", ["PDF", "DOCX", "TXT", "RTF"], "PDF"),
    ("tec_089", "What does 'RAM' stand for?", ["Random Access Memory", "Read Access Memory", "Rapid Application Module", "Remote Access Manager"], "Random Access Memory"),
    ("tec_090", "Which key combination is used to copy on most computers?", ["Ctrl+C (Cmd+C on Mac)", "Ctrl+V", "Ctrl+X", "Ctrl+Z"], "Ctrl+C (Cmd+C on Mac)"),
    ("tec_091", "What does 'CPU' stand for?", ["Central Processing Unit", "Computer Processing Unit", "Central Program Unit", "Core Processing Unit"], "Central Processing Unit"),
    ("tec_092", "What is the default file extension for Microsoft Word documents?", [".docx", ".pdf", ".txt", ".doc"], ".docx"),
    ("tec_093", "Which browser is made by Google?", ["Chrome", "Firefox", "Safari", "Edge"], "Chrome"),
    ("tec_094", "What does 'PDF' stand for?", ["Portable Document Format", "Personal Document File", "Public Data Format", "Print Document File"], "Portable Document Format"),
    ("tec_095", "Which operating system uses a penguin as its mascot?", ["Linux", "Windows", "macOS", "Unix"], "Linux"),
    ("tec_096", "What does 'GB' stand for in storage capacity?", ["Gigabyte", "Giant Byte", "Global Bit", "Giga Bit"], "Gigabyte"),
    ("tec_097", "Which key is used to delete text in front of the cursor?", ["Delete", "Backspace", "Enter", "Escape"], "Delete"),
    ("tec_098", "What is Microsoft's spreadsheet software called?", ["Excel", "Word", "PowerPoint", "Access"], "Excel"),
    ("tec_099", "What does 'WiFi' allow devices to do?", ["Connect to internet wirelessly", "Transfer files", "Charge batteries", "Display graphics"], "Connect to internet wirelessly"),
    ("tec_100", "Which company created Photoshop?", ["Adobe", "Microsoft", "Apple", "Corel"], "Adobe"),
    ("tec_101", "What is the brain of the computer called?", ["CPU", "RAM", "Hard Drive", "Motherboard"], "CPU"),
    ("tec_102", "What does pressing Ctrl+Z do?", ["Undo", "Redo", "Cut", "Copy"], "Undo"),
    ("tec_103", "Which file format is used for images with transparency?", ["PNG", "JPEG", "BMP", "GIF"], "PNG"),
]

for q in easy:
    new_questions.append({"id": q[0], "category": "Technology", "subcategory": "Computers & Software", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "easy", "topic": None, "subtopic": None})

# Medium questions (20)
medium = [
    ("tec_104", "What year was the first iPhone released?", ["2007", "2005", "2008", "2006"], "2007"),
    ("tec_105", "Which programming language is known for its use in web development alongside HTML and CSS?", ["JavaScript", "Python", "Java", "C++"], "JavaScript"),
    ("tec_106", "What does 'SSD' stand for?", ["Solid State Drive", "Super Speed Drive", "System Storage Device", "Secondary Storage Disk"], "Solid State Drive"),
    ("tec_107", "Which company developed the Python programming language?", ["Guido van Rossum (individual)", "Google", "Microsoft", "Oracle"], "Guido van Rossum (individual)"),
    ("tec_108", "What is the default port number for HTTP?", ["80", "443", "8080", "21"], "80"),
    ("tec_109", "Which Linux distribution is known for its ease of use for beginners?", ["Ubuntu", "Arch Linux", "Gentoo", "Slackware"], "Ubuntu"),
    ("tec_110", "What does 'BIOS' stand for?", ["Basic Input/Output System", "Binary Input/Output System", "Boot Initialization Operating System", "Base Integrated Operating System"], "Basic Input/Output System"),
    ("tec_111", "Which programming language is primarily used for iOS app development?", ["Swift", "Java", "Kotlin", "C#"], "Swift"),
    ("tec_112", "What is the maximum amount of data a standard dual-layer DVD can hold?", ["8.5 GB", "4.7 GB", "9.4 GB", "7.0 GB"], "8.5 GB"),
    ("tec_113", "Which company acquired GitHub in 2018?", ["Microsoft", "Google", "Amazon", "Facebook"], "Microsoft"),
    ("tec_114", "What does 'GUI' stand for?", ["Graphical User Interface", "General User Interface", "Global User Integration", "Graphic Unified Interface"], "Graphical User Interface"),
    ("tec_115", "Which file system is commonly used by modern Windows installations?", ["NTFS", "FAT32", "exFAT", "ext4"], "NTFS"),
    ("tec_116", "What is the name of Apple's voice assistant?", ["Siri", "Alexa", "Cortana", "Google Assistant"], "Siri"),
    ("tec_117", "Which company created the Java programming language?", ["Sun Microsystems", "Oracle", "Microsoft", "IBM"], "Sun Microsystems"),
    ("tec_118", "What does 'API' stand for?", ["Application Programming Interface", "Advanced Program Integration", "Automated Process Interface", "Application Process Indicator"], "Application Programming Interface"),
    ("tec_119", "Which cloud storage service is owned by Microsoft?", ["OneDrive", "Google Drive", "Dropbox", "iCloud"], "OneDrive"),
    ("tec_120", "What is the binary representation of the decimal number 8?", ["1000", "1001", "0111", "1010"], "1000"),
    ("tec_121", "Which version control system does GitHub use?", ["Git", "SVN", "Mercurial", "CVS"], "Git"),
    ("tec_122", "What does 'DNS' stand for?", ["Domain Name System", "Digital Network Service", "Data Name Server", "Domain Network System"], "Domain Name System"),
    ("tec_123", "Which Adobe software is used for video editing?", ["Premiere Pro", "Photoshop", "Illustrator", "After Effects"], "Premiere Pro"),
]

for q in medium:
    new_questions.append({"id": q[0], "category": "Technology", "subcategory": "Computers & Software", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "medium", "topic": None, "subtopic": None})

# Hard questions (20)
hard = [
    ("tec_124", "What was the first commercially available computer with a GUI?", ["Xerox Alto", "Apple Macintosh", "Commodore Amiga", "IBM PC"], "Xerox Alto"),
    ("tec_125", "Which sorting algorithm has the best average-case time complexity?", ["Merge Sort and Quick Sort (O(n log n))", "Bubble Sort", "Insertion Sort", "Selection Sort"], "Merge Sort and Quick Sort (O(n log n))"),
    ("tec_126", "What does 'POSIX' stand for?", ["Portable Operating System Interface", "Personal Operating System Index", "Public Open Source Interface Exchange", "Protected Operating System Interface X"], "Portable Operating System Interface"),
    ("tec_127", "Which computer scientist created the World Wide Web?", ["Tim Berners-Lee", "Vint Cerf", "Robert Kahn", "Marc Andreessen"], "Tim Berners-Lee"),
    ("tec_128", "What is the maximum theoretical transfer speed of USB 3.0?", ["5 Gbps", "10 Gbps", "480 Mbps", "12 Mbps"], "5 Gbps"),
    ("tec_129", "Which company developed the first commercial microprocessor?", ["Intel", "AMD", "Motorola", "IBM"], "Intel"),
    ("tec_130", "What does 'RISC' stand for in computer architecture?", ["Reduced Instruction Set Computer", "Rapid Integrated System Computer", "Remote Instruction Set Computing", "Refined Internal System Core"], "Reduced Instruction Set Computer"),
    ("tec_131", "Who is credited with creating the C programming language?", ["Dennis Ritchie", "Ken Thompson", "Brian Kernighan", "Bjarne Stroustrup"], "Dennis Ritchie"),
    ("tec_132", "What is the hexadecimal representation of the decimal number 255?", ["FF", "F0", "FE", "100"], "FF"),
    ("tec_133", "Which company created the first commercially successful personal computer?", ["Commodore (PET)", "Apple", "IBM", "Tandy"], "Commodore (PET)"),
    ("tec_134", "What does 'RAID' stand for in data storage?", ["Redundant Array of Independent Disks", "Rapid Access Integrated Drive", "Remote Array of Interconnected Devices", "Reliable Array of Internal Disks"], "Redundant Array of Independent Disks"),
    ("tec_135", "Which programming paradigm does Haskell primarily use?", ["Functional", "Object-oriented", "Procedural", "Logic"], "Functional"),
    ("tec_136", "What was the first computer virus to spread 'in the wild'?", ["Elk Cloner", "Morris Worm", "Brain", "Michelangelo"], "Elk Cloner"),
    ("tec_137", "Which company manufactured the 6502 processor used in early Apple computers?", ["MOS Technology", "Intel", "Motorola", "Zilog"], "MOS Technology"),
    ("tec_138", "What does 'CUDA' stand for in NVIDIA's parallel computing platform?", ["Compute Unified Device Architecture", "Central Unit Data Acceleration", "Core Unified Development Architecture", "Compute Universal Driver API"], "Compute Unified Device Architecture"),
    ("tec_139", "Who invented the computer mouse?", ["Douglas Engelbart", "Steve Jobs", "Bill Gates", "Alan Kay"], "Douglas Engelbart"),
    ("tec_140", "What is the default port for HTTPS?", ["443", "80", "8080", "22"], "443"),
    ("tec_141", "Which operating system was developed at Bell Labs?", ["Unix", "Linux", "MS-DOS", "Windows NT"], "Unix"),
    ("tec_142", "What does 'LLVM' stand for?", ["Low Level Virtual Machine", "Linux Level Virtual Manager", "Linked Library Virtual Module", "Local Language Verification Model"], "Low Level Virtual Machine"),
    ("tec_143", "Who developed the first compiler for a programming language?", ["Grace Hopper", "Ada Lovelace", "Alan Turing", "John von Neumann"], "Grace Hopper"),
]

for q in hard:
    new_questions.append({"id": q[0], "category": "Technology", "subcategory": "Computers & Software", "question": q[1], "options": q[2], "correct_answer": q[3], "difficulty": "hard", "topic": None, "subtopic": None})

# Load, add, sort, save
with open('Fiz/Resources/questions.json', 'r') as f:
    data = json.load(f)

data['categories']['Technology'].extend(new_questions)
data['categories']['Technology'].sort(key=lambda q: int(q['id'].split('_')[1]))

with open('Fiz/Resources/questions.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added 60 Computers & Software questions")
print(f"Technology now has {len(data['categories']['Technology'])} total questions")
print(f"Added: 20 easy, 20 medium, 20 hard")
