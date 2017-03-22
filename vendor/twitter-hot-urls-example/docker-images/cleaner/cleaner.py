
from redis import StrictRedis
import time
import hashlib
import signal

INTERVAL_SECONDS = 5

URL_HOTLIST_KEY = "url_hotlist"
KEY = "url_hotlist_reductions"

def sigterm_handler(_signo, _stack_frame):
    print("Terminating due to SIGTERM")
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGTERM, sigterm_handler)
    r = False
    while not r:
        try:
            r = StrictRedis(host="hotlist-redis", port=6379, db=0)
        except:
            print("Waiting for redis...")
            time.sleep(2)

    last_time = None

    try:
        while True:
            timestamp = time.time()
            urls = r.zrangebyscore(KEY, 0, timestamp)
            if type(urls) == list and len(urls) > 0:
                for url_key in urls:
                    r.zincrby(URL_HOTLIST_KEY, url_key, -1.0)
                num = r.zremrangebyscore(URL_HOTLIST_KEY, 0, 0.0)
                print("Removed %d old URL entries from %s" % (num, URL_HOTLIST_KEY))
                num = r.zremrangebyscore(KEY, 0, timestamp)
                print("Removed %d old URL scores from %s" % (num, KEY))
            time.sleep(INTERVAL_SECONDS)
    finally:
        print("Exiting")
