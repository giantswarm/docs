#!/bin/bash

# The purpose of this script is to test the
# search function with predictable settings and content

# create index
curl -XDELETE 'http://sitesearch:9200/testindex/'
curl -XPUT 'http://sitesearch:9200/testindex/' -d "@settings.json"

# put settings
curl -s -XPUT 'http://sitesearch:9200/testindex/_settings' -d "@settings.json"|python -m json.tool

# put mapping
curl -s -XPUT 'http://sitesearch:9200/testindex/_mapping/page' -d "@mapping.json"|python -m json.tool

# index documents
curl -s -XPUT 'http://sitesearch:9200/testindex/page/1' -d '{
    "title" : "Document 1",
    "uri" : "/test/1",
    "breadcrumb" : "Test/1",
    "text": "This is a text containing the filename swarmvars.json in a sentence."
}'

# perform searches.
# TODO: report if the result matches the expectations
curl -s -XGET 'http://sitesearch:9200/testindex/page/_search?q=swarmvars&fields=_id'|python -m json.tool
curl -s -XGET 'http://sitesearch:9200/testindex/page/_search?q=swarmvars.json&fields=_id'|python -m json.tool

