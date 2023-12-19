FROM python:3.10 AS base

ARG PROJECT_PATH=/app
ENV PYTHONPATH=${PROJECT_PATH}

WORKDIR ${PROJECT_PATH}

COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r ./requirements.txt