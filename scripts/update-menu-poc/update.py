import sys
import opml

from pprint import pprint


# number of space characters used for indentation per level
indentation = 2

def parse_input(path):
    outline = opml.parse(path)
    
    html = '<section class="nav-wrap">\n'
    html += '\t<nav class="acnav" role="navigation">\n'

    def recurse(o, h, depth=0):
        indent = (depth + 2) * "\t"

        h += f'{indent}<ul class="acnav__list acnav__list--level{(depth + 1)}">\n'

        for item in o:
            if len(item) > 0:
                h += f'{indent}\t<li class="has-children">\n'

                try:
                    h += f'{indent}\t\t<div class="acnav__label">{item.text}</div>\n'
                except AttributeError:
                    pass
                
                h = recurse(item, h, depth + 1)

                h += f'{indent}\t</li>\n'
            else:
                h += f'{indent}\t<li><a class="acnav__link" href="">{item.text}</a></li>\n'
        
        h += f'{indent}</ul>\n'

        return h

    html = recurse(outline[0], html)

    html += '\t</nav>\n'
    html += '</section>\n'
    
    print(html)

def main():
    if len(sys.argv) < 2:
        print("ERROR: No hierarchy file path given.")
        sys.exit(1)

    parse_input(sys.argv[1])


if __name__ == '__main__':
    main()
