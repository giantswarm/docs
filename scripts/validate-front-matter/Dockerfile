FROM quay.io/giantswarm/python:3.9-alpine3.13

RUN apk --no-cache add yaml-dev build-base git

RUN pip install --global-option='--with-libyaml' pyyaml

ENTRYPOINT ["python3"]
