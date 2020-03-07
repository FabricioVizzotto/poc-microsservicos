FROM python:3.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/src

COPY requirements.txt /app/src

RUN pip install -r requirements.txt
COPY . /app/src
