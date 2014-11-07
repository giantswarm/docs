#!/bin/bash

# start indexing content for search
#python ./searchindexer.py &
python ./searchindexer.py

# use mkdocs server to publish pages
exec mkdocs serve
