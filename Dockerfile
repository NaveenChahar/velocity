FROM python:3.9-slim-buster

WORKDIR /home/velocity

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

