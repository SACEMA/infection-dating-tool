# pull base image (2.7)
FROM python:2.7-alpine

# set work directory
WORKDIR /usr/src/app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ../requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# copy project
COPY ../cephia/ /app
WORKDIR /app

