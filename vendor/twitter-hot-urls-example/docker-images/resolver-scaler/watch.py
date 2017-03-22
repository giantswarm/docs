
from redis import StrictRedis
import time
import signal
import sys


INTERVAL_SECONDS = 30

QUEUE_GROWTH_THRESHOLD = 100

def sigterm_handler(_signo, _stack_frame):
    print("Terminating due to SIGTERM")
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGTERM, sigterm_handler)
    r = False
    while not r:
        try:
            r = StrictRedis(host="inbox-redis", port=6379, db=0)
        except:
            print("Waiting for redis...")
            time.sleep(2)

    last_check = None
    last_count = 0

    try:
        while True:
            count = r.llen("incoming_urls")
            if last_check is not None:
                print("Queue size: %d" % count)
                if count > last_count:
                    diff = count - last_count
                    if diff > QUEUE_GROWTH_THRESHOLD:
                        print("Queue growth of %d exceeds limit. Need to do something." % diff)
            last_count = count
            last_check = time.time()
            time.sleep(INTERVAL_SECONDS)
    finally:
        print("Exiting")
