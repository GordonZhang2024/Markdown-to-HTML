from markdown_parser import *

with open('sample.md') as samplemd:
    sample = samplemd.read().splitlines()
    
html = parser(sample)
print(html)

#with open('sample.html', 'w+') as samplehtml:
#    samplehtml.writelines(html)
