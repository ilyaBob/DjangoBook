FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /home/project

RUN python -m pip install Django psycopg2-binary python-slugify djangorestframework beautifulsoup4 requests django-silk

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000

