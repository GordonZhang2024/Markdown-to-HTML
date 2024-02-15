import re
from bs4 import beautifulsoup

def parser(markdown: list):
    '''
    function parser(): convert Markdown to HTML
        parameter markdown: Markdown type document split by lines
        return: HTML type document
    '''
    
    html = '<html>'
    for index, line in enumerate(markdown):
    
        h_ = re.match(r'#+ ', line)
        if h_ != None:
            h_ = str(h_.group(0))
            lenth = len(h_) - 1
            if lenth <= 6:
                line = line.replace(h_, f'<h{lenth}>')
                line = line + f'</h{lenth}>'

        bold = re.findall(r'[\*_]{2}[\w\s]+?[\*_]{2}', line)
        if bold != None:
            for i in bold:
                strong = '<strong>' + i[2:-2] + '</strong>'
                line = line.replace(i, strong)

        italic = re.findall(r'[\*_][\w\s</>]+?[\*_]', line)
        if italic != None:
            print(italic)
            for i in italic:
                em = '<em>' + i[1:-1] + '</em>'
                line = line.replace(i, em)


        markdown[index] = line + '<br/>'
        html = html + line
    html = html + '</html>'
    return html
