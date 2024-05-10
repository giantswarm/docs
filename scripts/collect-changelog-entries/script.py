import html2text
import requests
import re
from datetime import datetime, timedelta
from markdown import markdown

def get_last_week_entries(text, repo):
    # Convert markdown to html
    html = markdown(text)

    # Split html by <h2> tags
    entries = re.split('<h2>', html)

    last_week_entries = []
    one_week_ago = datetime.now() - timedelta(days=7)

    for entry in entries:
        # Find date in the format 'YYYY-MM-DD'
        date_match = re.search(r'\b\d{4}-\d{2}-\d{2}\b', entry)

        if date_match:
            date_str = date_match.group(0)
            entry_date = datetime.strptime(date_str, '%Y-%m-%d')

            h = html2text.HTML2Text()
            entry = h.handle(entry)

            # If entry date is within last week, add to list
            if entry_date > one_week_ago and entry:
                entry = '\n'.join(line for line in entry.splitlines() if line.strip())
                entry = "\n  - " + entry
                entry = re.sub(r'\\-\s*\d{4}-\d{2}-\d{2}$', '', entry, flags=re.MULTILINE)
                entry= entry.replace("### Added", "  __Added__")
                entry= entry.replace("### Removed", "  __Removed__")
                entry= entry.replace("### Changed", "  __Changed__")
                entry= entry.replace("### Fixed", "  __Fixed__")
                last_week_entries.append({
                    'repo': repo,
                    'date': date_str,
                    'entry': entry
                })

    return last_week_entries

def main():
    # Get current date in right format
    d = datetime.now()
    d = d.strftime('%Y-%m-%d')

    # Define the metadata
    metadata = f"""
---
date: {d}T14:00:00
title: Highlights for the week ending {d}
changes_categories:
  - Highlights
owner:
  - https://github.com/orgs/giantswarm/teams/sig-product
---

## General

## Apps"""

    with open(f'./src/content/changes/highlights/{d}.md', 'w') as f:
      f.write(metadata)
      f.write("\n")

    # List of repositories to fetch changelogs from
    with open('./scripts/collect-changelog-entries/repositories.txt', 'r') as rf:
      for repo in rf:
        repo = repo.strip() # Remove newline character
        all_apps = []

        print(f'Processing app repo: {repo} -')

        url = f'https://raw.githubusercontent.com/giantswarm/{repo}/main/CHANGELOG.md'
        response = requests.get(url, allow_redirects=True)

        if response.status_code == 200:
            apps = get_last_week_entries(response.text, repo)
            all_apps.extend(apps)
        else:
            print(f'Failed to fetch CHANGELOG.md from {url}')

        # Update the markdown file
        with open(f'./src/content/changes/highlights/{d}.md', 'a') as hf:
          last_app = ""
          for app in all_apps:
            if app['repo'] != last_app:
              hf.write(f"\n- [{app['repo']}](https://github.com/giantswarm/{app['repo']}) {app['entry']}")
            else:
              hf.write(f"{app['entry']} \n")
            last_app = app['repo']


if __name__ == '__main__':
    main()
