FROM python:3.11-slim

# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

WORKDIR /medai

COPY requirements.txt /medai/

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt 

COPY . /medai/

