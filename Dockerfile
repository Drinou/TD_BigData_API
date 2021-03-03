FROM ubuntu:18.04
COPY . /tp
RUN apt update && apt install -y python3-pip
RUN pip3 install flask flask_pymongo
WORKDIR /tp
CMD python3 td_api.py