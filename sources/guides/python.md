# Swarmify Python

__Last edited on October 8, 2014 by Matthias Lübken__

## Dockerfile
```
FROM python:2.7

RUN pip install Flask
ADD . /code
WORKDIR /code

EXPOSE  5000
CMD python app.py
```

## app.py
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
```

## fig.yml
```
web:
  build: .
  command: python app.py
  ports:
   - "5000:5000"
```

## commands
```
$ docker build -t giantswarm/flaskexample .
$ docker run -p 5000:5000 giantswarm/flaskexample
$ docker push giantswarm/flaskexample
```

## swarm.json
```
{
    "app_name": "helloflask",
    "services": [
        {
            "service_name": "helloflask-service",
            "components": [
                {
                    "component_name": "flaskexample",
                    "image": "giantswarm/flaskexample",
                    "args": ["python", "app.py"],
                    "ports": [ "5000/tcp" ],
                    "domains": { "helloflask.alpha.giantswarm.io": "5000" }
                }
            ]
        }
    ]
}
```