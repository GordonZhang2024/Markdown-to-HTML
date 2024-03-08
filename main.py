#!/usr/bin/python
from markdown_parser import parser
import click


@click.command()
@click.argument('file')
@click.argument('output_file')
def convert(file, output_file):
    '''\
    Convert Markdown to HTML
    '''
    with open(file) as f:
        markdown = f.read().splitlines()

    html = parser(markdown)
    with open(output_file, 'w+') as o:
        o.write(html)
        
if __name__ == '__main__':
    convert()
