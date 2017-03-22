# encoding: utf-8

import sys
import os
import json
from datetime import datetime
from twython import TwythonStreamer
import time
from redis import StrictRedis
import signal
import timeit

QUERY = os.getenv("TWITTER_TRACKING_QUERY")

# FIXME improve naming according to
# https://prometheus.io/docs/practices/naming/

metrics_template = """tracker_processed_urls_in_last_tweet_count {0}
tracker_processed_tweets_total {1}
tracker_processed_last_tweet_duration_seconds {2}
"""

def sigterm_handler(_signo, _stack_frame):
    print("Terminating due to SIGTERM")
    sys.exit(0)

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'id' not in data:
            if "limit" in data:
                q = float(self.tweet_count) / float(self.tweet_count + data["limit"]["track"])
                print("Processed %d tweets, missed %d so far (%.2f%%)" % (
                    self.tweet_count, data["limit"]["track"], q * 100.0))
                return
            sys.stderr.write("Discarded empty tweet:\n")
            sys.stderr.write(json.dumps(data) + "\n")
            return
        else:
            self.tweet_count += 1
        if 'text' not in data:
            return
        if "entities" not in data:
            return
        if "urls" not in data["entities"]:
            return
        if len(data["entities"]["urls"]) == 0:
            return

        start_time = timeit.default_timer()
        process_tweet_metrics = process_tweet(data)
        tracker_processed_last_tweet_duration_seconds = timeit.default_timer() - start_time

        with open('/tmp/metrics', 'w') as f:
            f.write(metrics_template.format(
                process_tweet_metrics['tracker_processed_urls_in_last_tweet_count'],
                self.tweet_count,
                tracker_processed_last_tweet_duration_seconds))

    def on_error(self, status_code, data):
        sys.stderr.write("ERROR %s - %s\n" % (status_code, data))


def twitter_date_to_datetime(s):
    """
    Converts twitter date string like 'Wed Jul 10 14:47:19 +0000 2013'
    to datetime
    """
    months = {
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
        'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
    (weekday, month, day, time, offset, year) = s.split()
    (hour, minute, second) = time.split(':')
    return datetime(int(year), int(months[month]), int(day),
        int(hour), int(minute), int(second))


def process_tweet(data):
    del data["user"]
    if "extended_entities" in data:
        del data["extended_entities"]
    data['created_at'] = twitter_date_to_datetime(data['created_at'])
    urls = []
    for url in data["entities"]["urls"]:
        urls.append(url["expanded_url"])

    # if len(urls) == 0:
    #     return

    # store URLs to redis
    for url in urls:
        key = "incoming_urls"
        value = url.encode("utf8")
        redis.lpush(key, value)

    print('Processed tweet %s with %d URLs' % (data['id'], len(urls)))
    return {'tracker_processed_urls_in_last_tweet_count': len(urls)}



if __name__ == '__main__':
    signal.signal(signal.SIGTERM, sigterm_handler)

    TWITTER_CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
    TWITTER_CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")
    TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
    TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    for variable in (TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET):
        if variable is None:
            sys.stderr.write("ERROR: environment variable '%s' is not set.\n")
            sys.exit(1)

    # Redis connection
    print("Connecting to Redis host 'redis' on port 6379")
    redis = StrictRedis(host='inbox-redis', port=6379, db=0)

    print "Starting tweet tracking"

    stream = MyStreamer(TWITTER_CONSUMER_KEY,
        TWITTER_CONSUMER_SECRET,
        TWITTER_ACCESS_TOKEN,
        TWITTER_ACCESS_TOKEN_SECRET)
    MyStreamer.tweet_count = 0

    try:
        while True:
            try:
                stream.statuses.filter(track=QUERY)
            except Exception, e:
                sys.stderr.write("Some error has occurred. Waiting a jiffy before resuming tracking.\n")
                sys.stderr.write(str(e) + "\n")
                time.sleep(3)
    finally:
        print("Exiting")
