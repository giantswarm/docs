FROM python:2.7-slim

RUN pip install twython redis tldextract

COPY track.py /

WORKDIR /

ENTRYPOINT ["python", "-u", "track.py"]
