FROM python:3.9.7
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN apt-get update \
    && apt-get -y install lsb-release \
    && apt-get -y install libmariadb-dev-compat libmariadb-dev \
    && pip install mysqlclient==2.0.3

RUN pip install -r requirements.txt

COPY . /code/



