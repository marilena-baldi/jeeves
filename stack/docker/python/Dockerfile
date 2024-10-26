FROM python:3.10 AS base

ARG PROJECT_PATH=/app
ENV PYTHONPATH=${PROJECT_PATH}

WORKDIR ${PROJECT_PATH}

RUN apt-get update -y && apt-get install -y sshpass

COPY ./src/requirements.txt ./requirements.txt
RUN pip3 install -r ./requirements.txt

CMD ["python3", "main.py"]