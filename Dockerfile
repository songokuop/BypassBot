FROM python:3.10-slim-buster

WORKDIR /app

RUN apt-get -qq update --fix-missing && apt-get -qq upgrade -y && apt-get install git -y

COPY requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]
