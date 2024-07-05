docker build -t hello-world-flask-docker:1.0 .
docker run -d -p 7000:7000 hello-world-flask-docker:1.0