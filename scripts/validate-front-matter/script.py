import datetime
import os
import re
import sys

from colored import fg, bg, attr

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
NO_FRONT_MATTER          = 'NO_FRONT_MATTER'
NO_LAST_REVIEW_DATE      = 'NO_LAST_REVIEW_DATE'
NO_LINK_TITLE            = 'NO_LINK_TITLE'
NO_OWNER                 = 'NO_OWNER'
NO_QUESTION_MARK         = 'NO_QUESTION_MARK'
NO_TITLE                 = 'NO_TITLE'
NO_TRAILING_NEWLINE      = 'NO_TRAILING_NEWLINE'
NO_USER_QUESTIONS        = 'NO_USER_QUESTIONS'
NO_WEIGHT                = 'NO_WEIGHT'
REVIEW_TOO_LONG_AGO      = 'REVIEW_TOO_LONG_AGO'
SHORT_DESCRIPTION        = 'SHORT_DESCRIPTION'
SHORT_TITLE              = 'SHORT_TITLE'
UNKNOWN_ATTRIBUTE        = 'UNKNOWN_ATTRIBUTE'

# All checks with metadata, in a logical order
checks = (
    # 1. prerequisites
    {
        'id': NO_FRONT_MATTER,
        'description': 'The page does not have any front matter',
    },
    {
        'id': NO_TRAILING_NEWLINE,
        'description': 'There should be a newline character at the end of the page',
    },
    {
        'id': UNKNOWN_ATTRIBUTE,
        'description': 'There is an unknown front matter attribute in this page',
    },
    # 2. standard attributes
    {
        'id': NO_TITLE,
        'description': 'The page should have a title',
    },
    {
        'id': LONG_TITLE,
        'description': 'The title should be less than 40 characters',
    },
    {
        'id': SHORT_TITLE,
        'description': 'The title should be longer than 5 characters',
    },
    {
        'id': NO_DESCRIPTION,
        'description': 'Each page should have a description',
    },
    {
        'id': LONG_DESCRIPTION,
        'description': 'The description should be less than 300 characters',
    },
    {
        'id': SHORT_DESCRIPTION,
        'description': 'The description should be longer than 70 characters',
    },
    {
        'id': NO_LINK_TITLE,
        'description': 'The page should have a linkTitle, which appears in menus and list pages',
    },
    {
        'id': LONG_LINK_TITLE,
        'description': 'The linkTitle (used in menu and list pages) should be less than 40 characters',
    },
    {
        'id': NO_WEIGHT,
        'description': 'The page should have a weight attribute',
    },
    # 3. custom attributes
    {
        'id': NO_OWNER,
        'description': 'The page should have an owner assigned',
    },
    {
        'id': INVALID_OWNER,
        'description': 'The owner field values must start with a Github teams URL',
    },
    {
        'id': NO_LAST_REVIEW_DATE,
        'description': 'The page should have a last_review_date',
    },
    {
        'id': REVIEW_TOO_LONG_AGO,
        'description': 'The last review date is too long ago',
    },
    {
        'id': INVALID_LAST_REVIEW_DATE,
        'description': 'The last_review_date should be of format YYYY-MM-DD',
    },
    {
        'id': NO_USER_QUESTIONS,
        'description': 'The page should have user_questions assigned',
    },
    {
        'id': LONG_USER_QUESTIONS,
        'description': 'Each user question should be no longer than 80 characters',
    },
    {
        'id': NO_QUESTION_MARK,
        'description': 'Questions should end with a question mark'
    }
)

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
    global checks
    for check in checks:
        if len(rdict[check['id']]) == 0:
            continue
        
        hl = headline(check['description'])
        print(f"\n{hl} ({check['id']})")
        for item in sorted(rdict[check['id']]):
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


def literal(text):
    "Returns a text wrapped in ANSI markup to stand out as a literal"
    return f"{fg('yellow')}{bg('black')}{text}{attr('reset')}"


def headline(text):
    "Return a text styled as headline"
    return f"{fg('white')}{attr('bold')}{text}{attr('reset')}"


def main():
    # Result dict has a key for each rule to check, where the value is a list of pages
    result = {}
    for check in checks:
        result[check['id']] = set()

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
                # TODO: once we fail on collected errors,
                # collect this one here instead of failing immediately.
                print(f'ERROR: page {fpath} has no front matter')
                sys.exit(1)
        
        if fm is None:
            result[NO_FRONT_MATTER].add(fpath)
            continue

        # Evaluate linkTitle
        if 'linkTitle' in fm:
            if len(fm['linkTitle']) > 40:
                result[LONG_LINK_TITLE].add(f"{fpath} linkTitle: {literal(fm['linkTitle'])}")
        
        # Evaluate title
        if 'title' in fm:
            if len(fm['title']) < 5:
                result[SHORT_TITLE].add(f"{fpath} title: {literal(fm['title'])}")
            elif len(fm['title']) > 40 and not 'linkTitle' in fm and not fpath.startswith(changes_path):
                result[NO_LINK_TITLE].add(f"{fpath} title: {literal(fm['title'])}")
            if len(fm['title']) > 100:
                result[LONG_TITLE].add(f"{fpath} title: {literal(fm['title'])}")
        else:
            result[NO_TITLE].add(fpath)
        
        if 'description' in fm:
            if fm['description'] is None:
                result[NO_DESCRIPTION].add(fpath)
            elif len(fm['description']) < 70:
                if not fpath.startswith(changes_path):
                    result[SHORT_DESCRIPTION].add(f"{fpath} description: {literal(fm['description'])}")
            elif len(fm['description']) > 300:
                result[LONG_DESCRIPTION].add(f"{fpath} description: {literal(fm['description'])}")
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
                        result[INVALID_OWNER].add(f"{fpath} owner: {literal(o)}")
        else:
            if (not fpath.startswith(changes_path) and
                not fpath.startswith(crds_path)):
                result[NO_OWNER].add(fpath)
        
        if 'user_questions' in fm:
            for q in fm['user_questions']:
                if len(q) > 80:
                    result[LONG_USER_QUESTIONS].add(f"{fpath} question: {literal(q)}")
                if not q.endswith('?'):
                    result[NO_QUESTION_MARK].add(f"{fpath} question: {literal(q)}")
        else:
            if (not fpath.startswith(changes_path) and
                not fpath.startswith(crds_path) and
                not fpath.endswith('_index.md')):
                result[NO_USER_QUESTIONS].add(fpath)
        
        if 'last_review_date' in fm:
            if type(fm['last_review_date']) is datetime.date:
                diff = datetime.date.today() - fm['last_review_date']
                if diff > datetime.timedelta(days=365):
                    result[REVIEW_TOO_LONG_AGO].add(f"{fpath} last_review_date: {literal(fm['last_review_date'])}")
            else:
                result[INVALID_LAST_REVIEW_DATE].add(f"{fpath} last_review_date: {literal(fm['last_review_date'])}")
        else:
            if (not fpath.startswith(changes_path) and
                not fpath.startswith(crds_path)):
                result[NO_LAST_REVIEW_DATE].add(fpath)
        
        # Evaluate all attributes
        for key in fm.keys():
            if key not in valid_keys:
                result[UNKNOWN_ATTRIBUTE].add(f'{fpath} attribute {literal(key)}')

    dump_result(result)


if __name__ == '__main__':
    main()
