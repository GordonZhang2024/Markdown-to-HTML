import re
with open('sample.md') as sample:
    lines = sample.readlines()

for index, line in enumerate(lines):
    head = re.match(r'[^\\]#+ ', line)
    if head != None:
        head = str(head.group(0))
        len = len(head) - 1
        if len <= 6:
            line = line.replace(head, f'<h{len}>')
            line = line + f'</h{len}>'
            lines[index] = line

    bold = re.search(r'[\*_]{2}\w+[\*_]{2}', line)
        if bold != None:
            for i in bold.groups:
                strong = '<strong>' + bold[2:-2] + </strong>
                line.replace(i, strong)
            
print(lines)
