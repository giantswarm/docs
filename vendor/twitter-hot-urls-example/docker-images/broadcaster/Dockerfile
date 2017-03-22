FROM python:2.7-slim

ENV DEBIAN_FRONTEND noninteractive

RUN set -x \
	&& apt-get -q update \
	&& apt-get install -yq --no-install-recommends git-core build-essential \
	&& pip install cython \
	&& pip install git+https://github.com/gevent/gevent.git#egg=gevent \
	&& pip install Flask \
	&& pip install flask-socketio \
	&& apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false build-essential \
	&& rm -rf /var/lib/apt/lists/*

RUN pip install redis

COPY server.py /
ADD templates /templates

ENTRYPOINT ["python", "-u", "/server.py"]

EXPOSE 5000
