FROM python:3

ENV PYTHONBUFFERED 1
RUN mkdir /django
WORKDIR /django
COPY . /django/
RUN pip install -r requirements.txt