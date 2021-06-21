FROM python:3.8-buster

RUN apt-get update && apt-get install -y locales && echo 'ja_JP UTF-8' > /etc/locale.gen
RUN useradd -u 1000 python -m
RUN pip install flake8 && pip install autopep8

USER python
RUN pip install fastapi sqlalchemy==1.4.3 uvicorn jinja2 python-multipart mysqlclient pytest databases aiomysql
ENV PATH $PATH:/home/python/.local/bin
USER root

WORKDIR /home/python
RUN curl -sL https://deb.nodesource.com/setup_14.x -o nodesource_setup.sh && bash nodesource_setup.sh && apt-get install nodejs
RUN chown -R python:python /home/python