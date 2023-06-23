import datetime
import json
import os
import re

import click
from colored import fg, bg, attr

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

# Some path config
path         = 'src/content'
changes_path = 'src/content/changes/'
crds_path    = 'src/content/use-the-api/management-api/crd/'
docs_host    = 'https://github.com/giantswarm/docs/blob/main/'

todays_date = datetime.date.today()

## Validation modes

# Validate everything
VALIDATE_ALL = "all"
# Only the last_review_date
VALIDATE_LAST_REVIEW_DATE = "last-reviewed"

# Unique identifiers for our checks
INVALID_DESCRIPTION      = 'INVALID_DESCRIPTION'
INVALID_LAST_REVIEW_DATE = 'INVALID_LAST_REVIEW_DATE'
INVALID_OWNER            = 'INVALID_OWNER'
LONG_DESCRIPTION         = 'LONG_DESCRIPTION'
NO_FULL_STOP_DESCRIPTION = 'NO_FULL_STOP_DESCRIPTION'
LONG_LINK_TITLE          = 'LONG_LINK_TITLE'
LONG_TITLE               = 'LONG_TITLE'
LONG_USER_QUESTION       = 'LONG_USER_QUESTION'
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

GITHUB_ACTIONS = os.getenv('GITHUB_ACTIONS')

SEVERITY_FAIL = 'FAIL'
SEVERITY_WARN = 'WARN'

# All checks with metadata, in a logical order
checks = (
    # 1. prerequisites
    {
        'id': NO_FRONT_MATTER,
        'description': 'No front matter found in the beginning of the page',
        'severity': SEVERITY_FAIL,
    },
    {
        'id': NO_TRAILING_NEWLINE,
        'description': 'There must be a newline character at the end of the page to ensure proper parsing',
        'severity': SEVERITY_FAIL,
    },
    {
        'id': UNKNOWN_ATTRIBUTE,
        'description': 'There is an unknown front matter attribute in this page',
        'severity': SEVERITY_FAIL,
        'has_value': True,
    },
    # 2. standard attributes
    {
        'id': NO_TITLE,
        'description': 'The page should have a title',
        'severity': SEVERITY_FAIL,
    },
    {
        'id': LONG_TITLE,
        'description': 'The title should be less than 40 characters',
        'severity': SEVERITY_FAIL,
        'has_value': True,
    },
    {
        'id': SHORT_TITLE,
        'description': 'The title should be longer than 5 characters',
        'severity': SEVERITY_FAIL,
        'has_value': True,
    },
    {
        'id': NO_DESCRIPTION,
        'description': 'Each page should have a description',
        'ignore_paths': [crds_path, changes_path],
        'severity': SEVERITY_FAIL,
    },
    {
        'id': LONG_DESCRIPTION,
        'description': 'The description should be less than 300 characters',
        'ignore_paths': [crds_path],
        'severity': SEVERITY_FAIL,
        'has_value': True,
    },
    {
        'id': NO_FULL_STOP_DESCRIPTION,
        'description': 'The description should end with a full stop',
        'ignore_paths': [crds_path, changes_path],
        'severity': SEVERITY_FAIL,
        'has_value': True,
    },
    {
        'id': SHORT_DESCRIPTION,
        'description': 'The description should be longer than 70 characters',
        'ignore_paths': [crds_path, changes_path],
        'severity': SEVERITY_FAIL,
        'has_value': True,
    },
    {
        'id': INVALID_DESCRIPTION,
        'description': 'Description must be a simple string without any markup or line breaks',
        'ignore_paths': [crds_path],
        'severity': SEVERITY_FAIL,
    },
    {
        'id': NO_LINK_TITLE,
        'description': 'The page should have a linkTitle, which appears in menus and list pages. If not given, title will be used and should be no longer than 40 characters.',
        'ignore_paths': [crds_path, changes_path],
        'severity': SEVERITY_WARN,
    },
    {
        'id': LONG_LINK_TITLE,
        'description': 'The linkTitle (used in menu and list pages; title is used if linkTitle is not given) should be less than 40 characters',
        'severity': SEVERITY_FAIL,
        'ignore_paths': [changes_path],
    },
    {
        'id': NO_WEIGHT,
        'description': 'The page should have a weight attribute, to control the sort order',
        'severity': SEVERITY_WARN,
    },
    # 3. custom attributes
    {
        'id': NO_OWNER,
        'description': 'The page should have an owner assigned',
        'ignore_paths': [crds_path, changes_path],
        'severity': SEVERITY_FAIL,
    },
    {
        'id': INVALID_OWNER,
        'description': 'The owner field values must start with a Github teams URL',
        'severity': SEVERITY_FAIL,
        'has_value': True,
    },
    {
        'id': NO_LAST_REVIEW_DATE,
        'description': 'The page should have a last_review_date',
        'ignore_paths': [crds_path, changes_path],
        'severity': SEVERITY_WARN,
    },
    {
        'id': REVIEW_TOO_LONG_AGO,
        'description': 'The last review date is too long ago',
        'severity': SEVERITY_WARN,
        'has_value': True,
    },
    {
        'id': INVALID_LAST_REVIEW_DATE,
        'description': 'The last_review_date should be of format YYYY-MM-DD',
        'severity': SEVERITY_FAIL,
        'has_value': True,
    },
    {
        'id': NO_USER_QUESTIONS,
        'description': 'The page should have user_questions assigned',
        'ignore_paths': [crds_path, changes_path],
        'severity': SEVERITY_FAIL,
    },
    {
        'id': LONG_USER_QUESTION,
        'description': 'Each user question should be no longer than 100 characters',
        'severity': SEVERITY_FAIL,
        'has_value': True,
    },
    {
        'id': NO_QUESTION_MARK,
        'description': 'Questions should end with a question mark',
        'severity': SEVERITY_FAIL,
        'has_value': True,
    }
)

# valid top level keys in front matter
valid_keys = set((
    'aliases',
    'changes_categories',
    'changes_entry',
    'crd',
    'date',
    'description',
    'expiration_in_days',
    'last_review_date',
    'layout',
    'linkTitle',
    'menu',
    'owner',
    'search',
    'source_repository',
    'source_repository_ref',
    'technical_name',
    'title',
    'user_questions',
    'weight',
))

# Convenience dict for checks by ID
checks_dict = {}
for c in checks:
    checks_dict[c['id']] = c



def print_json(rdict):
    """
    Print a formatted result report to JSON.

    rdict is a dict with file paths as keys and a list of check results as a value.
    """
    out = []
    for fpath in rdict.keys():
        for check in rdict[fpath]['checks']:
            try:
                title = check.get('title') or ""
                description = checks_dict[check['check']]['description']
                owners = []
                doc_owner = check.get('owner')
                if hasattr(doc_owner, "__len__"):
                  for i in doc_owner:
                    team_name = re.search('\/.*\/([^\/]+)\/?$', i).group(1)
                    team_label = team_name.replace("-", "/")
                    owners.append(team_label)
            except AttributeError:
                pass
            out.append({
                'title': 'Doc entry \"'+title+'\" needs to be reviewed',
                'message': description+" for [this document]("+docs_host+fpath+").",
                'owner': owners
            })

    json_object = json.dumps(out)
    print(json_object)


def print_result(rdict):
    """
    Print a formatted result report to STDOUT.

    rdict is a dict with file paths as keys and a list of check results as a value.
    """
    global checks_dict

    nfails = 0
    nwarnings = 0

    for fpath in rdict.keys():
        print(f'\n{fpath}')

        fails = []
        warnings = []

        for check in rdict[fpath]['checks']:
            if checks_dict[check['check']]['severity'] == SEVERITY_FAIL:
                fails.append(check)
                nfails += 1
            else:
                warnings.append(check)
                nwarnings += 1

        def format_line(check_id, severity_str, description, value):
            out = f' - {severity(severity_str)} - {headline(check_id)} - {description}'
            if checks_dict[check_id].get('has_value') and value != "":
                if type(value) == str:
                    out += f': {literal(value.strip())}'
                elif type(value) == datetime.date:
                    out += f': {literal(value.isoformat())}'
                else:
                    out += f': {literal(json.dumps(value))}'
            return out

        for check in fails:
            print(format_line(check['check'], SEVERITY_FAIL, checks_dict[check['check']]['description'], check.get('value')))
        for check in warnings:
            print(format_line(check['check'], SEVERITY_WARN, checks_dict[check['check']]['description'], check.get('value')))

    print('')
    if nfails > 0:
        print(f'Found {nfails} critical problems, marked with {severity(SEVERITY_FAIL)}.')
    if  nwarnings > 0:
        print(f'Found {nwarnings} less severe problems, marked with {severity(SEVERITY_WARN)}.')


def dump_annotations(rdict):
    """
    Create an annotations JSON file for use with
    https://github.com/yuzutech/annotations-action
    in ./annotations.json

    with one annotation per file

    [
        {
            file: "path/to/file.js",
            line: 5,
            title: "title for my annotation",
            message: "my message",
            annotation_level: "failure"
        }
    ]
    """

    global checks_dict

    annotations = []

    def format_message_part(check_id, severity_str, description, value):
        out = f'{severity_str} - {description}\n'
        if checks_dict[check_id].get('has_value') and value is not None and value != "":
            if type(value) == str:
                out += f': {value.strip()}\n'
            elif type(value) == datetime.date:
                out += f': {value.isoformat()}\n'
            else:
                out += f': {json.dumps(value)}\n'
        return out + "\n"

    for fpath in rdict.keys():
        level = 'warning'

        # line range to attach the annotation to
        end_line = 1

        nwarnings = 0
        nfails = 0

        message = ""

        for check in rdict[fpath]['checks']:
            end_line = max(end_line,
                           check.get('line', 1),
                           check.get('end_line', rdict[fpath]['num_front_matter_lines'] + 1))

            if checks_dict[check['check']]['severity'] == SEVERITY_FAIL:
                level = 'failure'
                nfails += 1
            else:
                nwarnings += 1

            message += format_message_part(check['check'],
                                           checks_dict[check['check']]['severity'],
                                           checks_dict[check['check']]['description'],
                                           check.get('value'))

        headline = f'Found {nwarnings} less severe problems'
        if nwarnings > 0 and nfails > 0:
            headline = f'Found {nfails} severe and {nwarnings} less severe problems'
        elif nfails > 0 and nwarnings == 0:
            headline = f'Found {nfails} severe problems'

        annotations.append({
            'file': fpath,
            'line': 1,
            'end_line': end_line,
            'title': headline,
            'message': message,
            'annotation_level': level,
        })

    with open('annotations.json', 'w') as fp:
        json.dump(annotations, indent=2, fp=fp)


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


def ignored_path(path, check_id):
    "Returns true if the given path should be ignored for the given check"
    check = None

    for c in checks:
        if c['id'] == check_id:
            check = c
            break

    if 'ignore_paths' not in check:
        return False

    for ignore_path in check['ignore_paths']:
        if path.startswith(ignore_path):
            return True

    return False

def validate(content, fpath, validation):
    """
    Validate the markdown page given as string and
    return a result array containing info on failed checks
    and the number of lines in front matter. Structure:

    {
        "num_front_matter_lines": 5,
        "checks": [
            {
                "check": "UNKNOWN_ATTRIBUTE",
                "value": "my_attribute",
                "line": 1,     # line number where this problem occurs or starts (optional)
                "end_line": 5, # line number where this problem ends (optional)
            }
        ]
    }
    """

    result = {
        'num_front_matter_lines': 0,
        'checks': [],
    }
    num_lines = len(list(content.split("\n")))

    # Detect whether there is front matter
    if not content.endswith('\n'):
        result['checks'].append({
            'check': NO_TRAILING_NEWLINE,
            'line': num_lines, # last line
        })
        return result
    if not content.startswith("---\n"):
        result['checks'].append({
            'check': NO_FRONT_MATTER,
            'line': 1,
        })
        return result

    # Parse front matter
    fm = {}
    fmstring = ""
    num_fmlines = 0
    try:
        fmstring = get_raw_front_matter(content)
        num_fmlines = len(list(fmstring.split("\n")))
        if fmstring != "":
            fm = load(fmstring, Loader=Loader)
    except Exception as e:
        result['checks'].append({
            'check': NO_FRONT_MATTER,
            'line': 1,
        })
        return result

    if fm is None:
        result['checks'].append({
            'check': NO_FRONT_MATTER,
            'line': 1,
        })
        return result

    # Evaluate linkTitle (hugo falls back to `title` if `linkTitle` not given)
    if validation == VALIDATE_ALL:
        if 'linkTitle' in fm or 'title' in fm:
            if len(fm.get('linkTitle') or fm['title']) > 40 and not ignored_path(fpath, LONG_LINK_TITLE):
                result['checks'].append({
                    'check': LONG_LINK_TITLE,
                    'value': fm.get('linkTitle') or fm['title'],
                })

    # Evaluate title
    if validation == VALIDATE_ALL:
        if 'title' in fm:
            if len(fm['title']) < 5:
                result['checks'].append({
                    'check': SHORT_TITLE,
                    'value': fm['title'],
                })
            if len(fm['title']) > 100:
                result['checks'].append({
                    'check': LONG_TITLE,
                    'value': fm['title'],
                })
        else:
            result['checks'].append({
                'check': NO_TITLE,
            })

    if validation == VALIDATE_ALL:
        if 'description' in fm:
            if fm['description'] is None and not ignored_path(fpath, NO_DESCRIPTION):
                result['checks'].append({
                    'check': NO_DESCRIPTION,
                })
            elif type(fm['description']) != str:
                if not ignored_path(fpath, INVALID_DESCRIPTION):
                    result['checks'].append({
                        'check': INVALID_DESCRIPTION,
                        'value': fm['description'],
                    })
            elif len(fm['description']) < 70:
                if not ignored_path(fpath, SHORT_DESCRIPTION):
                    result['checks'].append({
                        'check': SHORT_DESCRIPTION,
                        'value': fm['description'],
                    })
            elif len(fm['description']) > 300:
                if not ignored_path(fpath, LONG_DESCRIPTION):
                    result['checks'].append({
                        'check': LONG_DESCRIPTION,
                        'value': fm['description'],
                    })
            elif not fm['description'].endswith('.'):
                if not ignored_path(fpath, NO_FULL_STOP_DESCRIPTION):
                    result['checks'].append({
                        'check': NO_FULL_STOP_DESCRIPTION,
                        'value': fm['description'],
                    })
            elif "\n" in fm['description'].strip():
                if not ignored_path(fpath, INVALID_DESCRIPTION):
                    result['checks'].append({
                        'check': INVALID_DESCRIPTION,
                        'value': fm['description'],
                    })
        elif not ignored_path(fpath, NO_DESCRIPTION):
            result['checks'].append({
                'check': NO_DESCRIPTION,
            })

    # Evaluate menu
    if validation == VALIDATE_ALL:
        if 'menu' in fm:
            if not (fm.get('linkTitle') or fm.get('title')):
                result['checks'].append({
                    'check': NO_LINK_TITLE,
                })
            if 'weight' not in fm:
                result['checks'].append({
                    'check': NO_WEIGHT,
                })

    # Evaluate owner
    if validation == VALIDATE_ALL:
        if 'owner' in fm:
            if type(fm['owner']) != list:
                result['checks'].append({
                    'check': INVALID_OWNER,
                    'value': fm['owner'],
                })
            elif len(fm['owner']) == 0:
                result['checks'].append({
                    'check': NO_OWNER,
                })
            else:
                for o in fm['owner']:
                    if not o.startswith('https://github.com/orgs/giantswarm/teams/'):
                        result['checks'].append({
                            'check': INVALID_OWNER,
                            'value': fm['owner'],
                        })
        else:
            if not ignored_path(fpath, NO_OWNER):
                result['checks'].append({
                    'check': NO_OWNER,
                })

    if validation == VALIDATE_ALL:
        if 'user_questions' in fm:
            for q in fm['user_questions']:
                if len(q) > 100:
                    result['checks'].append({
                        'check': LONG_USER_QUESTION,
                        'value': q,
                    })
                if not q.endswith('?'):
                    result['checks'].append({
                        'check': NO_QUESTION_MARK,
                        'value': q,
                    })
        else:
            if (not ignored_path(fpath, NO_USER_QUESTIONS) and
                not fpath.endswith('_index.md')):
                result['checks'].append({
                    'check': NO_USER_QUESTIONS,
                })

    if validation in (VALIDATE_ALL, VALIDATE_LAST_REVIEW_DATE):
        if 'last_review_date' in fm:
            if type(fm['last_review_date']) is datetime.date:
                diff = todays_date - fm['last_review_date']
                expiration = 365
                if 'expiration_in_days' in fm and type(fm['expiration_in_days']) is int:
                    expiration = fm['expiration_in_days']

                if diff > datetime.timedelta(days=expiration):
                    result['checks'].append({
                        'check': REVIEW_TOO_LONG_AGO,
                        'title': fm['title'] or "",
                        'owner': fm['owner'] or [],
                        'value': fm['last_review_date'],
                    })
                elif diff < datetime.timedelta(seconds=0):
                    # in the future
                    result['checks'].append({
                        'check': INVALID_LAST_REVIEW_DATE,
                        'title': fm['title'] or "",
                        'owner': fm['owner'] or [],
                        'value': fm['last_review_date'],
                    })
            else:
                result['checks'].append({
                    'check': INVALID_LAST_REVIEW_DATE,
                    'title': fm['title'] or "",
                    'owner': fm['owner'] or [],
                    'value': fm['last_review_date'],
                })
        else:
            if not ignored_path(fpath, NO_LAST_REVIEW_DATE):
                result['checks'].append({
                    'check': NO_LAST_REVIEW_DATE,
                })

    # Evaluate all attributes
    if validation == VALIDATE_ALL:
        for key in fm.keys():
            if key not in valid_keys:
                result['checks'].append({
                    'check': UNKNOWN_ATTRIBUTE,
                    'value': key,
                })

    result['num_front_matter_lines'] = num_fmlines
    return result


def literal(text):
    "Returns a text wrapped in ANSI markup to stand out as a literal"
    return f"{fg('cyan')}{text}{attr('reset')}"

def headline(text):
    "Return a text styled as headline"
    return f"{fg('white')}{text}{attr('reset')}"

def severity(text):
    "Return the check's severity in the right color."
    if text == SEVERITY_FAIL:
        return f"{attr('bold')}{fg('red')}{text}{attr('reset')}"
    elif text == SEVERITY_WARN:
        return f"{attr('bold')}{fg('yellow')}{text}{attr('reset')}"
    return text

@click.command()
@click.option("--validation", default="all", help="Which validation to run. Use 'last-reviewed' or 'all' (default).")
@click.option("--output", default="stdout", help="Offer different output formats, 'json' or 'stdout' supported by now.")
def main(validation, output):
    # Result dict has a key for each file to check
    result = {}

    # Use list of pages from STDIN, or iterate through all pages.
    fpaths = []
    stdin = []

    if not click.get_text_stream('stdin').isatty():
        stdin = click.get_text_stream('stdin').read().strip().split("\n")

    if len(stdin) > 0 and stdin != [""]:
        for line in stdin:
            line = click.format_filename(line)
            if line.startswith(path) and line.endswith('.md'):
                fpaths.append(os.path.join(line))
                print(f"Adding to files checked: {line}")
    else:
        for root, _, files in os.walk(path):
            for file in files:
                if not file.endswith('.md'):
                    continue
                fpaths.append(os.path.join(root, file))

    for fpath in fpaths:
        if not os.path.exists(fpath):
            continue

        with open(fpath, 'r') as input:
            content = input.read()
            r = validate(content, fpath, validation)
            if len(r['checks']) > 0:
                result[fpath] = r

    if output == "json":
        print_json(result)
    else:
        print_result(result)

    if GITHUB_ACTIONS != None:
        dump_annotations(result)


if __name__ == '__main__':
    main()
