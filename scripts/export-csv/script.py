import csv
import os
import re

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

from pprint import pprint

PATH = 'src/content'

def main():
    fpaths = []
    for root, _, files in os.walk(PATH):
            for file in files:
                if not file.endswith('.md'):
                    continue
                fpaths.append(os.path.join(root, file))
    
    export_paths(fpaths)


def export_paths(paths):
    """Export data on the list of paths provided"""
    with open('./export.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['title', 'path_l1', 'path_l2', 'path_l3', 'url'])

        for p in paths:
            frontmatter = frontmatter_for_path(p)

            relpath = os.path.relpath(p, PATH)
            relpath = relpath.rstrip('_index.md')
            relpath = relpath.rstrip('index.md')

            writer.writerow([
                frontmatter['title'],
                path_level(relpath, 0),
                path_level(relpath, 1),
                path_level(relpath, 2),
                f'https://docs.giantswarm.io/{relpath}',
            ])


def path_level(path, level):
    """Return the first _level_ dirs of the given paths as a string"""
    parts = path.split(os.path.sep)
    try:
        p = parts[level]
        if p.endswith(".md"):
            return ""
        return p
    except IndexError:
        return ""


def frontmatter_for_path(path):
    """Extract front matter from one markdown file as dict"""
    content = ""
    with open(path, 'r') as inputfile:
        content = inputfile.read()
    
    if content == "":
        return None

    frontmatter_string = get_raw_front_matter(content)
    if frontmatter_string == "":
        return None

    frontmatter = load(frontmatter_string, Loader=Loader)

    return frontmatter

def get_raw_front_matter(source_text):
    """
    Tries to find front matter in the beginning of the document and
    returns it as a string.
    """
    matches = list(re.finditer(r"(---\n)", source_text))
    if len(matches) >= 2:
        front_matter_start = matches[0].start(1)
        front_matter_end = matches[1].start(1)
        return source_text[(front_matter_start + 4):front_matter_end]
    return ""


if __name__ == '__main__':
    main()
