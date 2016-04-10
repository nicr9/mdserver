FROM ubuntu:14.04
MAINTAINER Nic Roland <nicroland9@gmail.com>

RUN apt-get update; \
    apt-get install -y python python-pip pandoc wget

WORKDIR /opt/
COPY requirements.txt /opt/
RUN sudo pip install -r requirements.txt

RUN wget https://gist.githubusercontent.com/dashed/6714393/raw/ae966d9d0806eb1e24462d88082a0264438adc50/github-pandoc.css
COPY mdserver.py /opt/

EXPOSE 4000

ENTRYPOINT python /opt/mdserver.py
