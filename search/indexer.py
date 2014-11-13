# encoding: utf8

"""
Search indexer for mkdocs

Written by Marian

What it does:
- Parses mkdocs.yml
- For each markdown file mentioned in mkdocs.yml
  - pushes content to elasticsearch

Run from the same directory
"""

import config
import yaml
import os
import re
import sys
import logging
from elasticsearch import Elasticsearch
from datetime import datetime
from BeautifulSoup import BeautifulSoup
from markdown import markdown

def hosts_config(path):
    file_handle = open(path, "r")
    hosts = yaml.load(file_handle)
    file_handle.close()
    return hosts

def mkdocs_pages(path):
    """
    Reads the mkdocs YAML file contents
    and returns a list of dicts per markdown page
    """
    file_handle = open(path, "r")
    data = yaml.load(file_handle)
    pages = []
    for item in data["pages"]:
        record = {
            "file": item.pop(0)
        }
        record["breadcrumb"] = item
        pages.append(record)
    return pages


def markdown_to_text(markdown_text):
    """expects markdown unicode"""
    html = markdown(markdown_text)
    text = ''.join(BeautifulSoup(html).findAll(text=True))
    text = text.replace(" | ", " ")
    text = re.sub(r"[\-]{3,}", "-", text)  # markdown tables
    return text


def index_page(path, breadcrumb, index):
    """
    Send one page to elasticsearch
    """
    # get document body
    file_handler = open(os.path.join(config.SOURCE_PATH, path), "r")
    mdtext = file_handler.read()
    file_handler.close()
    mdtext = mdtext.decode("utf8")
    text = markdown_to_text(mdtext)

    title = breadcrumb.pop()

    # remove trailing index.md
    path = re.sub(r"index\.md$", "", path)
    uri = "/%s/" % path.replace(".md", "")
    uri = uri.replace("//", "/")

    # catch-all text field
    alltext = title
    alltext += " " + text
    alltext += " " + uri
    alltext += " " + " ".join(breadcrumb)

    # document data
    docdata = {
        "title": title,
        "uri": uri,
        "body": text,
        "timestamp": datetime.utcnow(),
        "breadcrumb": breadcrumb,
        "text": alltext,
    }

    # set main/sub categories "breadcrumb_<i>"
    for i in range(1, len(breadcrumb) + 1):
        key = "breadcrumb_%d" % i
        docdata[key] = breadcrumb[i - 1]

    # send to ElasticSearch
    es.index(
        index=index,
        doc_type=config.ELASTICSEARCH_DOCTYPE,
        id=uri,
        body=docdata)


def make_indexname(name_prefix):
    """creates a random index name"""
    return name_prefix + "-" + datetime.utcnow().strftime("%Y%m%d-%H%M%S")


if __name__ == "__main__":
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    # logging setup
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)

    # read hosts config
    eshosts = hosts_config(config.ELASTICSEARCH_HOSTS)
    for host in eshosts:
        logging.info("Found elasticsearch host in %s: %s" % (config.ELASTICSEARCH_HOSTS, host))

    es = Elasticsearch(hosts=eshosts)
    pages = mkdocs_pages(config.MKDOCS_FILE)

    # make temporary index name
    tempindex = make_indexname(config.ELASTICSEARCH_INDEX)

    es.indices.create(index=tempindex)
    es.indices.put_mapping(index=tempindex,
        doc_type=config.ELASTICSEARCH_DOCTYPE,
        body=config.ELASTICSEARCH_MAPPING)
    
    # index to new index
    for item in pages:
        index_page(item["file"], item["breadcrumb"], tempindex)


    # remove old if existed, re-create alias
    if es.indices.exists_alias(name=config.ELASTICSEARCH_INDEX):
        old_index = es.indices.get_alias(name=config.ELASTICSEARCH_INDEX)
        # here we assume there is only one index behind this alias
        old_index = old_index.keys()[0]
        logging.info("Old index on alias is: %s" % old_index)
        try:
            es.indices.delete_alias(index=old_index, name=config.ELASTICSEARCH_INDEX)
        except elasticsearch.exceptions.NotFoundError:
            logging.error("Could not delete index alias for %s" % (old_index))
            pass
        try:
            es.indices.delete(index=old_index)
        except:
            logging.error("Could not delete index %s" % old_index)
            pass
    es.indices.put_alias(index=tempindex, name=config.ELASTICSEARCH_INDEX)
