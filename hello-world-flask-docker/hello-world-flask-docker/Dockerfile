# syntax=docker/dockerfile:1

FROM python:3.9.6-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "gunicorn", "--bind" , "0.0.0.0:7000", "main:app", "--log-level", "debug"]