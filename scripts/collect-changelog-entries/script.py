import os
import yaml
import html2text
import requests
import re
from datetime import datetime, timedelta
from markdown import markdown

# GitHub API URL to list files in the folder
API_URL = f'https://api.github.com/repos/giantswarm/github/contents/repositories'

# Read GITHUB_TOKEN from environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

# Headers for authentication
headers = {
    'Authorization': f'token {GITHUB_TOKEN}'
}

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
                entry= entry.replace("### Added", "")
                entry= entry.replace("### Removed", "")
                entry= entry.replace("### Changed", "")
                entry= entry.replace("### Fixed", "")
                entry= '\n'.join(line for line in entry.split("\n") if line.strip())
                entry= '\n'.join('    ' + line if line.lstrip().startswith('*') else line for line in entry.splitlines())
                last_week_entries.append({
                    'repo': repo,
                    'date': date_str,
                    'entry': '\n'+entry
                })

    return last_week_entries

# Function to fetch file content from GitHub
def fetch_file_content(file_url):
    return requests.get(file_url,headers=headers).text

def fetch_app_repositories():
    # Fetch the list of team yaml files in the folder
    response = requests.get(API_URL,headers=headers)
    response.raise_for_status()
    files = response.json()


    all_apps = []
    for file in files:
        if file['name'].endswith('.yaml'):
            print(f'Processing file: {file["name"]} with URL: {file["download_url"]}')
            file_content = fetch_file_content(file["download_url"])
            apps = yaml.safe_load(file_content)
            all_apps.extend(apps)

    # Filter entries that have the flavour "app"
    apps = [
        app for app in all_apps
        if 'gen' in app and 'flavours' in app['gen'] and 'app' in app['gen']['flavours']
    ]

    return apps

def main():
    # Get current date in right format
    d = datetime.now()
    d = d.strftime('%Y-%m-%d')

    app_repos = fetch_app_repositories()

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

<!-- This where BREAKING CHANGES ARE HIGHLIGHTED -->

## Apps"""

    metadata_end = f"""

## Docs

<!-- FER is filling this one -->"""

    with open(f'./src/content/changes/highlights/{d}.md', 'w') as f:
      f.write(metadata)
      f.write("\n")

    all_apps = []
    # Get list of repositories to fetch changelogs from
    for app_repo in app_repos:
      repo = app_repo['name']

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
          hf.write("\n")
        last_app = app['repo']
      hf.write(metadata_end)
      hf.write("\n")

if __name__ == '__main__':
    main()
