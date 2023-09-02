FROM python:3.10.9-slim-buster

LABEL maintainer="RafRaf <smartrafraf@gmail.com>"

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip==23.2.1

COPY requirements.txt /app/

RUN pip install -r requirements.txt && rm -rf /root/.cache/*

CMD python boobogram.py