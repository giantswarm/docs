import requests
from lxml import etree

sitemap = 'https://docs.giantswarm.io/sitemap.xml'

old_prefix = 'https://docs.giantswarm.io'
new_prefix = 'http://localhost:1313'

def main():
    count = 0

    urls = list(get_uris(sitemap))
    for uri in sorted(urls):
        url = new_prefix + uri

        r = requests.head(url)
        if r.status_code != 200:
            count += 1
            print(f'{r.status_code} {url}')
        
    print(f'{count} errors')

def get_uris(sitemap_url):
    r = requests.get(sitemap)
    root = etree.fromstring(r.content)
    for item in root.iter():        
        if item.tag != '{http://www.sitemaps.org/schemas/sitemap/0.9}loc':
            continue
        
        uri = item.text.replace(old_prefix, '')
        yield uri

if __name__ == '__main__':
    main()
