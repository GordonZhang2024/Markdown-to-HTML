#!/usr/bin/python
import re

def parser(markdown: list):
    '''
    function parser(): convert Markdown to HTML
        parameter markdown: Markdown type document split by lines
        return: HTML type document
    '''
    
    html = '''\
<html>
    <style>
    p {
        background: lightgrey;
    }
    q {
        background: lightgrey;
    }
    </style>
'''
    for index, line in enumerate(markdown):
    
        h_ = re.match(r'#+\s', line)
        if h_ != None:
            h_ = str(h_.group(0))
            lenth = len(h_) - 1
            if lenth <= 6:
                line = line.replace(h_, f'<h{lenth}>')
                line = line + f'</h{lenth}><hr/>'

        bold = re.findall(r'[\*_]{2}[\w\s]+?[\*_]{2}', line)
        if bold != None:
            for i in bold:
                strong = '<strong>' + i[2:-2] + '</strong>'
                line = line.replace(i, strong)

        italic = re.findall(r'[\*_][\w\s</>]+?[\*_]', line)
        if italic != None:
            for i in italic:
                em = '<em>' + i[1:-1] + '</em>'
                line = line.replace(i, em)

        quote = re.match(r'[>\s]+\s', line)
        if quote != None:
            quote = str(quote.group(0))
            lenth = len(quote) - 1
            line = line.replace(quote, lenth * '<blockquote>')
            line = line + lenth * '</blockquote>'

        code = re.findall(r'`[\w\s</>]+?`', line)
        if code != None:
            for i in code:
                c = '<q><code>' + i[1:-1] + '</code></q>'
                line = line.replace(i, c)

        strikethrough = re.findall(r'~{2}[\w\s]+?~{2}', line)
        if strikethrough != None:
            for i in strikethrough:
                s = '<s>' + i[2:-2] + '</s>'
                line = line.replace(i, s)

        markdown[index] = line + '<br/>'
        html = html + line
    html = html + '</html>'
    return html

