import docx2txt
import re


my_text = docx2txt.process("resume.docx")

pattern = re.compile(r'[a-zA-Z0-9-\.]+@[a-zA-Z-\.]*\.(com|edu|net)')

matches = pattern.finditer(my_text)

for match in matches:
    print(match.group(0))

