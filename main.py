#!/usr/bin/python
from markdown_parser import parser
from bs4 import BeautifulSoup
import click

@click.group()
def cli():
    """\
    Convert Markdown to HTML
    """

@cli.command()
@click.argument('file')
@click.argument('output_file')
def convert(file, output_file):
    with open(file) as f:
        markdown = f.read().splitlines()

    html = parser(markdown)
    with open(output_file, 'w+') as o:
        o.write(html)
        
if __name__ == '__main__':
    cli()
