import datetime
import os
import re

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

path = 'src/content'
changes_path = 'src/content/changes/'
crds_path = 'src/content/ui-api/management-api/crd/'

INVALID_LAST_REVIEW_DATE = 'INVALID_LAST_REVIEW_DATE'
INVALID_OWNER            = 'INVALID_OWNER'
LONG_DESCRIPTION         = 'LONG_DESCRIPTION'
LONG_LINK_TITLE          = 'LONG_LINK_TITLE'
LONG_TITLE               = 'LONG_TITLE'
LONG_USER_QUESTIONS      = 'LONG_USER_QUESTIONS'
NO_DESCRIPTION           = 'NO_DESCRIPTION'
NO_FRONT_MATTER_FOUND    = 'NO_FRONT_MATTER_FOUND'
NO_LAST_REVIEW_DATE      = 'NO_LAST_REVIEW_DATE'
NO_LINK_TITLE            = 'NO_LINK_TITLE'
NO_OWNER                 = 'NO_OWNER'
NO_TITLE                 = 'NO_TITLE'
NO_TRAILING_NEWLINE      = 'NO_TRAILING_NEWLINE'
NO_USER_QUESTIONS        = 'NO_USER_QUESTIONS'
NO_WEIGHT                = 'NO_WEIGHT'
REVIEW_TOO_LONG_AGO      = 'REVIEW_TOO_LONG_AGO'
SHORT_DESCRIPTION        = 'SHORT_DESCRIPTION'
SHORT_TITLE              = 'SHORT_TITLE'
UNKNOWN_ATTRIBUTE        = 'UNKNOWN_ATTRIBUTE'

# valid top level keys in front matter
valid_keys = set((
    'aliases',
    'changes_categories',
    'changes_entry',
    'date',
    'description',
    'last_review_date',
    'layout',
    'linkTitle',
    'menu',
    'owner',
    'source_repository',
    'source_repository_ref',
    'technical_name',
    'title',
    'user_questions',
    'weight',
))

def dump_result(rdict):
    for key in rdict:
        if len(rdict[key]) > 0:
            print(f'\n{key}')
            for item in sorted(rdict[key]):
                print(f'  - {item}')


def get_front_matter(source_text):
    """
    Tries to find front matter in the beginning of the document and
    then returns a dict or raises an exception.
    """
    matches = list(re.finditer(r"(---)\n", source_text))
    if len(matches) >= 2:
        front_matter_start = matches[0].start(1)
        front_matter_end = matches[1].start(1)
        data = load(source_text[(front_matter_start + 3):front_matter_end], Loader=Loader)
        return data
    return None


def main():
    # Result dict has a key for each rule to check, where the value is a list of pages
    result = {
        INVALID_LAST_REVIEW_DATE: set(),
        INVALID_OWNER: set(),
        LONG_DESCRIPTION: set(),
        LONG_LINK_TITLE: set(),
        LONG_TITLE: set(),
        LONG_USER_QUESTIONS: set(),
        NO_DESCRIPTION: set(),
        NO_FRONT_MATTER_FOUND: set(),
        NO_LAST_REVIEW_DATE: set(),
        NO_LINK_TITLE: set(),
        NO_OWNER: set(),
        NO_TITLE: set(),
        NO_TRAILING_NEWLINE: set(),
        NO_USER_QUESTIONS: set(),
        NO_WEIGHT: set(),
        REVIEW_TOO_LONG_AGO: set(),
        SHORT_DESCRIPTION: set(),
        SHORT_TITLE: set(),
        UNKNOWN_ATTRIBUTE: set(),
    }

    # Iterate through pages
    fpaths = []
    for root, _, files in os.walk(path):
        for file in files:
            if not file.endswith('.md'):
                continue
            
            fpaths.append(os.path.join(root, file))

    for fpath in fpaths:
        fm = {}

        with open(fpath, 'r') as input:
            content = input.read()

            if not content.endswith('\n'):
                result[NO_TRAILING_NEWLINE].add(fpath)
                # Can't parse reliably, so skipping further checks
                continue

            try:
                fm = get_front_matter(content)
            except Exception as e:
                print(f'ERROR: page {fpath} has no front matter')
        
        if fm is None:
            result[NO_FRONT_MATTER_FOUND].add(fpath)
            continue

        # Evaluate linkTitle
        if 'linkTitle' in fm:
            if len(fm['linkTitle']) > 40:
                result[LONG_LINK_TITLE].add(fpath)
        
        # Evaluate title
        if 'title' in fm:
            if len(fm['title']) < 5:
                result[SHORT_TITLE].add(fpath)
            elif len(fm['title']) > 40 and not 'linkTitle' in fm and not fpath.startswith(changes_path):
                result[NO_LINK_TITLE].add(fpath)
            if len(fm['title']) > 100:
                result[LONG_TITLE].add(fpath)
        else:
            result[NO_TITLE].add(fpath)
        
        if 'description' in fm:
            if fm['description'] is None:
                result[NO_DESCRIPTION].add(fpath)
            elif len(fm['description']) < 70:
                if not fpath.startswith(changes_path):
                    result[SHORT_DESCRIPTION].add(fpath)
            elif len(fm['description']) > 300:
                result[LONG_DESCRIPTION].add(fpath)
        else:
            result[NO_DESCRIPTION].add(fpath)

        # Evaluate menu
        if 'menu' in fm:
            if 'linkTitle' not in fm:
                result[NO_LINK_TITLE].add(fpath)
            if 'weight' not in fm:
                result[NO_WEIGHT].add(fpath)
        
        # Evaluate owner
        if 'owner' in fm:
            # TODO: check owner validity
            if type(fm['owner']) != list:
                result[INVALID_OWNER].add(fpath)
            elif len(fm['owner']) == 0:
                result[NO_OWNER].add(fpath)
            else:
                for o in fm['owner']:
                    if not o.startswith('https://github.com/orgs/giantswarm/teams/'):
                        result[INVALID_OWNER].add(fpath)
        else:
            if (not fpath.startswith(changes_path) and
                not fpath.startswith(crds_path)):
                result[NO_OWNER].add(fpath)
        
        if 'user_questions' in fm:
            for q in fm['user_questions']:
                if len(q) > 80:
                    result[LONG_USER_QUESTIONS].add(fpath)
        else:
            if (not fpath.startswith(changes_path) and
                not fpath.startswith(crds_path)):
                result[NO_USER_QUESTIONS].add(fpath)
        
        if 'last_review_date' in fm:
            if type(fm['last_review_date']) is datetime.date:
                diff = datetime.date.today() - fm['last_review_date']
                if diff > datetime.timedelta(days=365):
                    result[REVIEW_TOO_LONG_AGO].add(fpath)
            else:
                result[INVALID_LAST_REVIEW_DATE].add(fpath)
        else:
            if (not fpath.startswith(changes_path) and
                not fpath.startswith(crds_path)):
                result[NO_LAST_REVIEW_DATE].add(fpath)
        
        # Evaluate all attributes
        for key in fm.keys():
            if key not in valid_keys:
                result[UNKNOWN_ATTRIBUTE].add(f'{key} in {fpath}')

    dump_result(result)


if __name__ == '__main__':
    main()
