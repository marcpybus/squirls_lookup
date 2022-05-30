
FROM ubuntu:22.04

LABEL maintainer="marcpybus"
LABEL version="1"
LABEL description="Flask server to run SQUIRLS"

RUN apt update
RUN apt install -y python3-flask default-jre gunicorn python3-gevent && rm -rf /var/lib/apt/lists/* && apt clean

COPY server.py .

EXPOSE 5000
CMD gunicorn -w 4 -b 0.0.0.0:5000 --worker-class gevent server:app

