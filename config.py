# encoding: utf8

"""
Configuration for searchindexer
"""

# ElasticSearch host names or IP addresses and port
ELASTICSEARCH_HOSTS = ["192.168.59.103:9200"]

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
MKDOCS_FILE = "mkdocs.yml"

# Path to markdown files
SOURCE_PATH = "sources/"