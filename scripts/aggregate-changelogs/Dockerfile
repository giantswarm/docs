FROM python:3.9-alpine

RUN apk --no-cache add yaml-dev build-base git

RUN pip install pygithub GitPython python-dateutil
RUN pip install --global-option='--with-libyaml' pyyaml

ENTRYPOINT ["python3"]
