# encoding: utf8

from flask import Flask
import logging
import os
from redis import StrictRedis
import json

app = Flask(__name__)
app.config["BASE_URL"] = os.environ.get('BASE_URL')

# set up error logging to STDERR
if not app.debug:
    handler = logging.StreamHandler()
    handler.setLevel(logging.WARNING)
    app.logger.addHandler(handler)

r = False
while not r:
    try:
        r = StrictRedis(host="hotlist-redis", port=6379, db=0)
    except:
        print("Waiting for redis...")
        time.sleep(2)


@app.route("/")
def index():
    toplist = r.zrevrange("url_hotlist", 0, 29, withscores=True)
    out = []
    for n in range(len(toplist)):
        key = toplist[n][0]
        url = r.get("url:%s" % key)
        out.append({
            "score": toplist[n][1],
            "url": url
        })
    return(json.dumps(out, indent=2))
