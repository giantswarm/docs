# encoding: utf8

"""
Configuration for searchindexer
"""

# Path of YAML file containing
# ElasticSearch host names or IP addresses and port
ELASTICSEARCH_HOSTS = "hosts.yml"

ELASTICSEARCH_INDEX = "docs"

ELASTICSEARCH_DOCTYPE = "page"

ELASTICSEARCH_MAPPING = {
	"page": {
		"properties": {
			"title": {
				"type": "string",
				"store": True,
				"index": "analyzed",
				"term_vector": "with_positions_offsets",
				"analyzer": "english",
				"boost": 10.0,
			},
			"uri": {
				"type": "string",
				"boost": 5.0,
			},
			"breadcrumb": {
				"type": "string",
				"boost": 5.0,
			},
			"text": {
				"type": "string",
				"store": True,
				"index": "analyzed",
				"term_vector": "with_positions_offsets",
				"analyzer": "english",
			},
			"uri": {
				"type": "string",
				"index": "not_analyzed",
			}
		}
	}
}


# Path to mkdocs YAML file
MKDOCS_FILE = "../mkdocs.yml"

# Path to markdown files
SOURCE_PATH = "../sources"
