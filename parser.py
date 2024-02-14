import re
with open('sample.md') as sample:
    lines = sample.read()
    lines = lines.splitlines()

for index, line in enumerate(lines):
    head = re.match(r'#+ ', line)
    if head != None:
        head = str(head.group(0))
        lenth = len(head) - 1
        if lenth <= 6:
            line = line.replace(head, f'<h{lenth}>')
            line = line + f'</h{lenth}>'

    bold = re.findall(r'[\*_]{2}[\w\s]+?[\*_]{2}', line)
    if bold != None:
        for i in bold:
            strong = '<strong>' + i[2:-2] + '</strong>'
            line = line.replace(i, strong)

    italic = re.findall(r'[\*_][\w\s]+?[\*_]', line)
    if italic != None:
        print(italic)
        for i in italic:
            em = '<em>' + i[1:-1] + '</em>'
            line = line.replace(i, em)


    lines[index] = line
print(lines)
