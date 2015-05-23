# encoding: utf8

"""
Search indexer for the Giant Swarm Docs

Written by Marian

What it does:
- Reads content directory
- For each markdown file
  - parses front matter and content
  - pushes content to elasticsearch

Run from the same directory that contains this file (python ./indexer.py)

Expected env variables:
- SITESEARCH_PORT_9200_TCP_ADDR
- SITESEARCH_PORT_9200_TCP_PORT

"""

import config
import os
import re
import sys
import logging
from elasticsearch import Elasticsearch
from datetime import datetime
from BeautifulSoup import BeautifulSoup
from markdown import markdown
import toml

def get_pages(root_path):
    """
    Reads the content folder structure and returns a list dicts, one per page.
    Each page dict has these keys.

        path: list of logical uri path elements
        uri: URI of the final rendered page as string
        file_path: physical path of the file, as valid from within this script

    Won't return anything for the home page and other index pages.
    """
    num_root_elements = len(root_path.split(os.sep))
    pages = []
    structured_path = []
    for root, dirs, files in os.walk(root_path):
        for filename in files:
            path = root.split(os.sep)[num_root_elements:]
            file_path = root + os.sep + filename
            if filename != "index.md":
                # append name of file (without suffix) as last uri segment
                segment = filename[:-3]
                path.append(segment)
            uri = "/" + "/".join(path) + "/"
            record = {
                "path": path,
                "uri": uri,
                "file_path": file_path
            }
            pages.append(record)
    return pages


def markdown_to_text(markdown_text):
    """expects markdown unicode"""
    html = markdown(markdown_text)
    text = ''.join(BeautifulSoup(html).findAll(text=True))
    text = text.replace(" | ", " ")
    text = re.sub(r"[\-]{3,}", "-", text)  # markdown tables
    return text


def index_page(path, breadcrumb, uri, index):
    """
    Send one page to elasticsearch. Arguments:

    path: File path
    breadcrumb: structured path (list of segments)
    uri: The URI
    index: Elasticsearch index to write to
    """
    # get document body
    file_handler = open(path, "r")
    source_text = file_handler.read()
    source_text_unicode = source_text.decode("utf8")
    file_handler.close()

    # parse front matter
    data = {
        "title": u""
    }
    title = None
    matches = list(re.finditer(r"(\+\+\+)", source_text_unicode))
    if len(matches) < 2:
        logging.warn("Indexing page %s: No front matter found (looking for +++ blah +++)" % path)
        text = markdown_to_text(source_text_unicode)
    else:
        front_matter_start = matches[0].start(1)
        front_matter_end = matches[1].start(1)
        data = toml.loads(source_text[(front_matter_start + 3):front_matter_end])
        text = markdown_to_text(source_text_unicode[(front_matter_end+3):])
        for key in data.keys():
            if type(data[key]) == str:
                data[key] = data[key].decode("utf8")

    data["uri"] = uri
    data["breadcrumb"] = breadcrumb
    data["body"] = text

    # catch-all text field
    data["text"] = data["title"]
    data["text"] += " " + text
    data["text"] += " " + uri
    data["text"] += " " + " ".join(breadcrumb)

    # set main/sub categories "breadcrumb_<i>"
    for i in range(1, len(breadcrumb) + 1):
        data["breadcrumb_%d" % i] = breadcrumb[i - 1]

    # send to ElasticSearch
    es.index(
        index=index,
        doc_type=config.ELASTICSEARCH_DOCTYPE,
        id=uri,
        body=data)


def make_indexname(name_prefix):
    """creates a random index name"""
    return name_prefix + "-" + datetime.utcnow().strftime("%Y%m%d-%H%M%S")


if __name__ == "__main__":
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    es = None

    # logging setup
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)

    # read hosts config
    es_addr = os.getenv("SITESEARCH_PORT_9200_TCP_ADDR")
    es_port = os.getenv("SITESEARCH_PORT_9200_TCP_PORT")
    if es_addr is not None and es_port is not None:
        es_hosts = ["%s:%s" % (es_addr, es_port)]
        logging.info("Found ElasticSearch host config %s" % es_hosts)
        es = Elasticsearch(hosts=es_hosts)
    else:
        logging.error("Search index won't be updated, since no connection to ElasticSearch possible.")
        sys.exit(1)

    # get page data
    pages = get_pages(config.SOURCE_PATH)

    # generate temporary index name
    tempindex = make_indexname(config.ELASTICSEARCH_INDEX)

    es.indices.create(index=tempindex)
    es.indices.put_mapping(index=tempindex,
        doc_type=config.ELASTICSEARCH_DOCTYPE,
        body=config.ELASTICSEARCH_MAPPING)
    
    # index each page into new index
    for page in pages:
        index_page(page["file_path"], page["path"], page["uri"], tempindex)

    # remove old indexif existed, re-create alias
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
