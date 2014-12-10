description: This guide shows you how to create, deploy and run a simple Python/Flask project on Giant Swarm

# Swarmify Python

<p class="lastmod">Last edited on November 27, 2014 by Marian Steinbach</p>

This is a simple helloworld with Python and [Flask](http://flask.pocoo.org/). You find all the source files at [github.com/giantswarm/flaskexample](https://github.com/giantswarm/flaskexample).

## Dockerfile
A simple Dockerfile using the official Python image, installing Flask via pip, adding the app as `app.py` and starting it:

```
FROM python:2.7

RUN pip install Flask
ADD . /code
WORKDIR /code

EXPOSE  5000
CMD python app.py
```

## app.py
A simple Flask file return a string at the root route and starting the Flask app:
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
```

## swarm.json
A simple `swarm.json` using a custom image `registry.giantswarm.io/giantswarm/flaskexample` and publishing it with the port `5000`:
```
{
    "app_name": "helloflask",
    "services": [
        {
            "service_name": "helloflask-service",
            "components": [
                {
                    "component_name": "flaskexample",
                    "image": "registry.giantswarm.io/giantswarm/flaskexample",
                    "args": ["python", "app.py"],
                    "ports": [ "5000/tcp" ],
                    "domains": { "helloflask.gigantic.io": "5000" }
                }
            ]
        }
    ]
}
```

## Commands
```
# Build the image:
$ docker build -t registry.giantswarm.io/giantswarm/flaskexample .
# Test the image locally:
$ docker run -p 5000:5000 registry.giantswarm.io/giantswarm/flaskexample
# Push the image:
$ docker push registry.giantswarm.io/giantswarm/flaskexample
# Create the app:
$ swarm create
# Start the app:
$ swarm start helloflask
```