
"""
Grabs a URL from Redis, resolves the URL and stores the result
in another Redis.

Will check if the URL has been handled before (is in list)

Assuming these settings:

    Incoming Redis Server:
        Hostname: incomingredis
        Port: 6379
        Database ID: 0
        list key: incoming_urls

    Outgoing Redis Server:
        Hostname: outgoingredis
        Port: 6379
        Database ID: 0
"""


import requests
from redis import StrictRedis
import time
import hashlib
import sys
import socket
import signal
import ssl
import timeit


INCOMING_KEY = "incoming_urls"

# REPORTING_INTERVAL = 10

URL_HANDLED_TTL = 3600
HOTLIST_TTL = 3600

# MAXIMUM_JOBS = 5000

# FIXME improve naming according to
# https://prometheus.io/docs/practices/naming/

metrics_template = """resolver_urls_resolved_total {0}
resolver_url_resolve_last_duration_seconds {1}
"""

incoming = False
outgoing = False

while not incoming:
    try:
        incoming = StrictRedis(host="inbox-redis", port=6379, db=0)
    except:
        print("Waiting for incomingredis...")
        time.sleep(2)

while not outgoing:
    try:
        outgoing = StrictRedis(host="hotlist-redis", port=6379, db=0)
    except:
        print("Waiting for outgoingredis...")
        time.sleep(2)


def sigterm_handler(_signo, _stack_frame):
    print("Terminating due to SIGTERM")
    sys.exit(0)

def fetch_url():
    """
    Get the oldest URL from the incoming list
    """
    return incoming.rpop(INCOMING_KEY)


def get_cached_url_result(url):
    """
    Check if this URL has been handled before
    and if yes, return the value
    """
    key = "url_handled:" + hashlib.md5(url).hexdigest()
    return outgoing.get(key)


def set_cached_url_result(url, resolved_url):
    """
    Mark a URL as handled (with expiration time)
    """
    try:
        key = "url_handled:" + hashlib.md5(url.encode("utf8")).hexdigest()
        outgoing.setex(key, URL_HANDLED_TTL, resolved_url)
    except UnicodeDecodeError:
        pass


def resolve_url(url):
    resolved_url = get_cached_url_result(url)
    if resolved_url is None:
        start = time.time()
        response = None
        try:
            response = requests.get(url=url, timeout=3.0, allow_redirects=True)
            duration = time.time() - start
            resolved_url = response.url
            try:
                set_cached_url_result(url, resolved_url)
                print("Resolved URL in %.3f Sec: %s" % (duration, url.encode("utf8")))
            except UnicodeDecodeError:
                pass
            del response
        except requests.exceptions.ConnectionError:
            sys.stderr.write("ERROR: URL %s can't be resolved, connection error.\n" % url)
            resolved_url = url
        except requests.exceptions.ReadTimeout:
            resolved_url = url
        except requests.exceptions.TooManyRedirects:
            resolved_url = url
        except socket.timeout:
            resolved_url = url
        except:
            pass
    return resolved_url


def store_resolved_url(resolved_url):
    """
    Stores the resolved_url as a hotlistable item
    """
    url_key = hashlib.md5(resolved_url.encode("utf8")).hexdigest()
    outgoing.zincrby("url_hotlist", url_key, 1.0)
    outgoing.set("url:" + url_key, resolved_url.encode("utf8"))
    end_time = time.time() + HOTLIST_TTL
    outgoing.zadd("url_hotlist_reductions", float(end_time), url_key)


if __name__ == "__main__":
    signal.signal(signal.SIGTERM, sigterm_handler)
    urls_resolved_total = 0
    nothing_to_do = False

    try:
        while True:
            url = fetch_url()

            if url is not None:
                start_time = timeit.default_timer()
                resolved_url = resolve_url(url)
                url_resolve_last_duration_seconds = timeit.default_timer() - start_time

                if resolved_url is not None:
                    store_resolved_url(resolved_url)
                urls_resolved_total += 1
            else:
                nothing_to_do = True
                url_resolve_last_duration_seconds = 'NaN'

            # write metrics to file in prometheus format
            with open('/tmp/metrics', 'w') as f:
                f.write(metrics_template.format(urls_resolved_total, url_resolve_last_duration_seconds))

            # don't overheat
            if nothing_to_do:
                time.sleep(3)
                nothing_to_do = False

    finally:
        print("Exiting")
