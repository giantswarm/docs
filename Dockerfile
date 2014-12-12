# Inspired by https://github.com/dotcloud/docker/blob/master/docs/Dockerfile

FROM 		ubuntu:14.04
MAINTAINER	Matthias Luebken <matthias@giantswarm.io>



RUN apt-get update -qq && apt-get install -y -qq python-pip gettext
RUN pip install mkdocs==0.9 BeautifulSoup==3.2.1 elasticsearch==1.2.0


WORKDIR	/docs
EXPOSE	8000
ADD 	. /docs

CMD ["./run.sh"]
