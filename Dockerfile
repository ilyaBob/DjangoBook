FROM python:3.12-slim

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y \
    build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /home

RUN python -m pip install Django psycopg2-binary python-slugify djangorestframework
# Копируем зависимости
#COPY requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt


#EXPOSE 8000

CMD cd project && python manage.py migrate && python manage.py runserver 0.0.0.0:8000

