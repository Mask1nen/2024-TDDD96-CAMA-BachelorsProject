FROM python:3.9-slim

ENV PYTHONBUFFERED=1

WORKDIR /cama_backend

COPY /requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
