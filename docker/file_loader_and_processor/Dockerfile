FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache --virtual .build-deps build-base libressl-dev libffi-dev gcc musl-dev python3-dev

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install gunicorn
ADD ./requirements.txt /app/
RUN pip install -r requirements.txt

ADD ./file_loader_and_processor /app/file_loader_and_processor
ADD ./docker /app/docker

RUN chmod +x /app/docker/file_loader_and_processor/server-entrypoint.sh
RUN chmod +x /app/docker/file_loader_and_processor/worker-entrypoint.sh