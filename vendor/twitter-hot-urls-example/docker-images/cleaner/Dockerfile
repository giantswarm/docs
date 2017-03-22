FROM python:2.7-slim

RUN pip install redis

COPY cleaner.py /

WORKDIR /

ENTRYPOINT ["python", "-u", "cleaner.py"]
