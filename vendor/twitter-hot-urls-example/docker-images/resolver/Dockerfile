FROM python:2.7-slim

RUN pip install requests redis

COPY resolve.py /

WORKDIR /

ENTRYPOINT ["python", "-u", "resolve.py"]
