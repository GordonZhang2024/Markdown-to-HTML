
import re
with open('sample.md') as sample:
    lines = sample.readlines()

for index, line in enumerate(lines):
    
    head = re.match(r'[^\\]#', line)
    if head != None:
        head = str(head.group(0))
        len = len(head)
        if len <= 6:
            line = line.replace(head, f'<h{len}>')
            line = line + f'</h{len}>'
            lines[index] = line



print(lines)