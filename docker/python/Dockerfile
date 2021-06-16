FROM python:3.8-buster

RUN apt-get update && apt-get install -y locales && echo 'ja_JP UTF-8' > /etc/locale.gen
RUN useradd -u 1000 python -m
RUN pip install flake8 && pip install autopep8
USER python
RUN pip install fastapi sqlalchemy uvicorn jinja2 python-multipart mysqlclient databases[mysql]
USER root