FROM python:3.9.6-alpine

WORKDIR /usr/src/game_nerd

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
COPY . .