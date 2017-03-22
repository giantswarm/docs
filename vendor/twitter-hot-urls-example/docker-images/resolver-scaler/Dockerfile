FROM python:2.7-slim

RUN pip install redis

COPY watch.py /

WORKDIR /

ENTRYPOINT ["python", "-u", "watch.py"]
