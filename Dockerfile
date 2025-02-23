# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:3.7
ENV PYTHONUNBUFFERED 1

# If you prefer miniconda:
#FROM continuumio/miniconda3

LABEL Name=perdana_member Version=1.0.0
EXPOSE 8087

WORKDIR /app
ADD . /app

# Using pip:
RUN apt-get update && apt-get install -y default-libmysqlclient-dev \
    && pip install --upgrade pip && pip install -r requirements.txt

# RUN python manage.py makemigrations && python manage.py migrate
# RUN python manage.py collectstatic --noinput
