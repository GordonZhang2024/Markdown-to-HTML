import re
with open('sample.md') as sample:
    lines = sample.readlines()

for index, line in enumerate(lines):
    head = re.match(r'[^\\]#+ ', line)
    if head != None:
        head = str(head.group(0))
        lenth = len(head) - 1
        if lenth <= 6:
            line = line.replace(head, f'<h{lenth}>')
            line = line + f'</h{lenth}>'
            lines[index] = line

    bold = re.findall(r'[\*_]{2}\w+[\*_]{2}', line)
        if bold != None:
            for i in bold:
                strong = '<strong>' + bold[2:-2] + '</strong>'
                line.replace(i, strong)
            
print(lines)
