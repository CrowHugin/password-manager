# syntax=docker/dockerfile:1

FROM ubuntu:22.04
RUN apt-get update && apt-get upgrade -y
RUN apt install python3 -y && apt install python3-pip -y
RUN apt install vim -y

RUN mkdir usr/local/etc/username
WORKDIR /usr/local/etc/username
COPY . ./


RUN pip3 install argparse

