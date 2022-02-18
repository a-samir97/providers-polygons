FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/

RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/