from datetime import datetime
from os import path, makedirs
import os
import re
import sys
import tempfile

from dateutil.parser import parse
import git
from github import Github
from github.GithubException import UnknownObjectException
from yaml import load, dump, CLoader, CDumper

CONFIG_PATH = sys.argv[1]

# Target path for generated content
CONTENT_PATH = sys.argv[2]

# Target path for generated data
DATA_PATH = sys.argv[3]

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

RELEASES_REPO = 'giantswarm/releases'

WARNING_COMMENT = "# Generated by scripts/aggregate-changelogs. WARNING: Manual edits to this files will be overwritten.\n"

def get_releases(client, repo_shortname):
    """
    Yields all Github releases in the given repository
    """
    repo = client.get_repo(repo_shortname)

    for release in repo.get_releases():
        # skip unpublished releases
        if release.published_at is None:
            continue
        
        body = ""
        if release.body is not None:
            body = link_pull_requests(release.body, repo_shortname)
            body = link_commit_hashes(body, repo_shortname)

        yield {
            'repository': repo_shortname,
            'version_tag': release.tag_name,
            'date': release.published_at,
            'body': body,
            'url': release.html_url,
        }

def get_changelog_file(client, repo_shortname):
    repo = client.get_repo(repo_shortname)
    try:
        remote_file = repo.get_contents('CHANGELOG.md')
        return remote_file.decoded_content.decode('utf-8')
    except UnknownObjectException:
        return None

def parse_changelog(body, repo_shortname):
    # Cut off the link reference at the end
    try:
        (good, bad) = body.split("[Unreleased]: ", maxsplit=1)
    except ValueError as e:
        print(f"INFO: snippet '[Unreleased]: ' not found in CHANGELOG.md of {repo_shortname}")
        good = body
    
    # Create chunks based on level 2 headlines
    chunks = re.split(r'\n##\s+', good, flags=re.M)

    # Get rid of some bad chunks
    for chunk in chunks:
        lines = re.split(r'\n+', chunk, flags=re.M)
        
        if len(lines) < 2:
            continue
        if lines[0].startswith('[Unreleased]'):
            continue
        if not lines[0].startswith('['):
            continue
        
        # First line must start with semantic version number in square brackets
        match = re.match(r'^\[([^\.]+)\.([^\.]+)\.([^\]]+)\]', lines[0])
        if match is None:
            continue
        version = f'{match.group(1)}.{match.group(2)}.{match.group(3)}'

        anchor = lines[0].replace(' ', '-').replace('.', '').replace('[', '').replace(']', '')
        url = f'https://github.com/{repo_shortname}/blob/master/CHANGELOG.md#{anchor}'

        # Omit first line and sanitize
        body = '\n'.join(lines[1:]).strip()

        release = {
            'body': body,
            'url': url,
        }

        yield (version, release)


def parse_release_yaml(data, repo_shortname, provider, relative_path):
    if 'apiVersion' not in data:
        raise Exception('Unexpected release data format. No ".apiVersion" attribute found.')
    if data['apiVersion'] != 'release.giantswarm.io/v1alpha1':
        raise Exception('Unexpected release data apiVersion "%s".' % data['apiVersion'])
    if 'kind' not in data:
        raise Exception('Unexpected release data format. No ".kind" attribute found.')
    if data['kind'] != 'Release':
        raise Exception('Unexpected release data kind "%s".' % data['kind'])
    if 'metadata' not in data:
        raise Exception('Unexpected release data format. No ".metadata" attribute found.')
    if 'name' not in data['metadata']:
        raise Exception('Unexpected release data format. No ".metadata.name" attribute found.')
    if 'spec' not in data:
        raise Exception('Unexpected release data format. No ".spec" attribute found.')
    if 'date' not in data['spec']:
        raise Exception('Unexpected release data format. No ".spec.date" attribute found.')
    
    creation = data['spec']['date']
    if type(creation) == str:
        creation = parse(creation)

    return {
        'date': creation,
        'version_tag': data['metadata']['name'],
        'provider': provider,
        'url': f'https://github.com/{repo_shortname}/tree/master{relative_path}',
        'repository': RELEASES_REPO,
    }

def get_cluster_releases(repo_shortname):
    """
    Clones the releases repo, parses the data from it,
    and emits releases.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        print(f'Cloning to temporary directory {tmpdir}')
        git.Git(tmpdir).clone(f"https://github.com/{repo_shortname}.git", depth=1)

        (org, repo) = repo_shortname.split("/", maxsplit=1)

        provider = None
        for root, _, files in os.walk(tmpdir):
            if os.path.basename(root) in ('aws', 'azure', 'kvm'):
                provider = os.path.basename(root)
            
            relative_dir_path = root[len(tmpdir + "/" + repo):]

            for fname in files:
                if fname != "release.yaml":
                    continue

                fpath = path.join(root, fname)
            
                release = {}
                data = None

                # Get structured data
                with open(fpath, 'r') as releasefile:
                    data = load(releasefile, Loader=CLoader)
                
                    try:
                        release = parse_release_yaml(data, repo_shortname, provider, relative_dir_path)
                    except Exception as e:
                        print(f'WARNING: {e}')
                
                # Add release notes
                release_notes_path = os.path.join(root, "README.md")
                if os.path.exists(release_notes_path):
                    with open(release_notes_path, 'r') as release_notes_file:
                        release_notes = release_notes_file.read().strip()
                        
                        # Strip first headline
                        lines = release_notes.split("\n")
                        if len(lines) > 0:
                            if lines[0].startswith('#'):
                                lines = lines[1:]
                        
                        release['body'] = "\n".join(lines).strip()
                
                yield release
                    

def normalize_version(v):
    """
    Removes a 'v' prefix from the version string
    """
    if v.startswith('v'):
        return v[1:]
    return v

def link_pull_requests(mkdwn, repo_shortname):
    """
    Links pull request mentions like #123 in a markdown string

    repo_shortname is the repository in org/repo format.
    """
    def replace_func(match):
        result = f'{match.group(1)}[{match.group(2)}](https://github.com/{repo_shortname}/pull/{match.group(3)})'
        return result
    
    result = re.sub(r'([^\[a-z0-9])(#([0-9]+))', replace_func, mkdwn)
    return result

def link_commit_hashes(mkdwn, repo_shortname):
    """
    Links commit hashes like 9bbbd0ef498474b922830bd2bfaa6a1caf382660
    """
    def replace_hash(match):
        result = f'[{match.group(1)[0:7]}](https://github.com/{repo_shortname}/commit/{match.group(1)})'
        return result
    
    result = re.sub(r'\b([a-f0-9]{40})\b', replace_hash, mkdwn)
    return result

def generate_release_file(repo_shortname, repo_config, release):
    """
    Write a release file with YAML front matter and Markdown body
    """
    version = normalize_version(release['version_tag'])

    org, repo_id = repo_shortname.split("/", maxsplit=1)
    aliases = None
    
    if repo_shortname == RELEASES_REPO:
        provider_label = release['provider'].upper()
        if provider_label == 'AZURE':
            provider_label = 'Azure'
        categories = [f'Workload cluster releases for {provider_label}']
        title = f'Workload cluster release v{version} for {provider_label}'
        description = f'Release notes for {provider_label} workload cluster release v{version}, published on {release["date"].strftime("%d %B %Y, %H:%M")}'
        filename = f"{release['provider']}-{release['version_tag']}.md"
        category_path = f"workload-cluster-releases-{provider_label.lower()}"
        aliases = [f"/changes/tenant-cluster-releases-{provider_label.lower()}/releases/{provider_label.lower()}-{release['version_tag']}/"]
    else:
        categories = [repo_config['category']]
        title = f'{repo_id} release v{version}'
        description = f'Changelog entry for {release["repository"]} version {version}, published on {release["date"].strftime("%d %B %Y, %H:%M")}'
        filename = f"{release['version_tag']}.md"
        category_path = repo_config['category'].lower().replace(" ", "-")
    
    filepath = path.join(CONTENT_PATH, category_path, repo_id, filename)

    frontmatter = {
        'date': release['date'].isoformat(),
        'title': title,
        'description': description,
        'changes_entry': {
            'repository': release['repository'],
            'version_tag': release['version_tag'],
            'version': version,
            'url': release['url'],
        },
        'changes_categories': categories,
    }

    if aliases is not None:
        frontmatter['aliases'] = aliases

    content = "---\n"
    content += WARNING_COMMENT
    content += dump(frontmatter, Dumper=CDumper)
    content += "---\n\n"
    content += release['body']
    content += "\n"

    makedirs(path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as outfile:
        outfile.write(content)


if __name__ == "__main__":
    with open(CONFIG_PATH, 'rb') as configfile:
        conf = load(configfile, Loader=CLoader)
    
    if GITHUB_TOKEN == "":
        print("ERROR: environment variable GITHUB_TOKEN is empty.")
        sys.exit(1)

    g = Github(GITHUB_TOKEN)

    # Write categories to data
    categories = {}
    for cat in conf['categories']:
        try:
            categories[cat['name']] = cat['color']
        except KeyError:
            print(f"ERROR: No color defined for category '{cat['name']}' in config.yaml")
            sys.exit(1)
    with open(os.path.join(DATA_PATH, 'changes_categories.yaml'), 'w') as catfile:
        catfile.write(WARNING_COMMENT)
        catfile.write(dump(categories, Dumper=CDumper))
    
    # Write changelog items
    for repo_short in conf['repositories']:
        repo_conf = conf['repositories'][repo_short]

        releases = []

        if repo_short == RELEASES_REPO:
            for release in get_cluster_releases(repo_short):
                releases.append(release)

        else:
            # Attempt to get GitHub releases (based on tags in the repo).
            releases = list(get_releases(g, repo_short))

            # Attempt to get releas einfo from CHANGELOG.md.
            changelog = get_changelog_file(g, repo_short)
            
            # Match release tags and changelog versions and
            # enhance release data with descriptions from CHANGELOG.md.
            if changelog is None:
                print(f'INFO: repository {repo_short} has no CHANGELOG.md file.')
            else:
                changelog_entries = {}
                for (version, release) in parse_changelog(changelog, repo_short):
                    v = normalize_version(version)
                    changelog_entries[v] = release
                
                for n in range(len(releases)):
                    v = normalize_version(releases[n]['version_tag'])

                    if v not in changelog_entries:
                        print("WARNING: %s version %s not found in CHANGELOG.md" % (repo_short, v))
                        continue
                    
                    releases[n]['url'] = changelog_entries[v]['url']

                    if changelog_entries[v]['body'].strip() != "":
                        releases[n]['body'] = changelog_entries[v]['body']
                    else:
                        print("WARNING: %s version %s entry in CHANGELOG.md is empty" % (repo_short, v))

        for release in releases:
            generate_release_file(repo_short, repo_conf, release)
