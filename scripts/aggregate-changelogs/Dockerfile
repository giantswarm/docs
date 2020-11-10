FROM python:3.9-alpine

RUN apk --no-cache add yaml-dev build-base

RUN pip install pygithub
RUN pip install --global-option='--with-libyaml' pyyaml

ENTRYPOINT ["python3"]
