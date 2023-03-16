FROM arm32v7/python:3-slim

RUN apt-get update && \
apt-get install -y python3-pip

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "server.py"]
