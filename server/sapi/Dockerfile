FROM python:2.7
MAINTAINER Wil Black wil.black@solalla.com
RUN mkdir /code
ADD sapi/ /code/
ADD requirements.txt /code/
RUN pip install -r /code/requirements.txt
WORKDIR /code/web/sapi