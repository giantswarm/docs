FROM python:2.7-slim

RUN pip install Flask gunicorn redis

ADD gunicorn.conf /gunicorn.conf
ADD server.py /server.py

EXPOSE 8000

WORKDIR /

CMD ["gunicorn", "-c", "gunicorn.conf", "server:app"]
