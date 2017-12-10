FROM python:3.5.3

LABEL maintainer="RafRaf <smartrafraf@gmail.com>"

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip==9.0.1 pip-tools==1.9.0

COPY requirements.txt /app/

RUN pip install -r requirements.txt && rm -rf /root/.cache/*

CMD python boobogram.py