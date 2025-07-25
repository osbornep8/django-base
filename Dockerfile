FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /medai

COPY requirements.txt /medai/

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt 

COPY . /medai/

