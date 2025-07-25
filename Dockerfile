FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY docker_req.txt /app/

RUN pip install --upgrade pip && pip install -r docker_req.txt

COPY . /app/

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]

