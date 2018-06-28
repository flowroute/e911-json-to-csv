FROM ubuntu:16.04

WORKDIR /app
RUN apt-get update
RUN apt-get install -y python-tk python-pip
ADD . /app
RUN pip install --no-cache-dir requests

ENTRYPOINT python json2csv.py
