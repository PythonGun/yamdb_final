FROM python:3.7-slim
RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip3 install -r api_yamdb/requirements.txt --no-cache-dir
RUN pip install psycopg2-binary==2.9
RUN python3 manage.py migrate
RUN python3 manage.py makemigrations reviews
RUN python3 manage.py migrate
RUN python3 manage.py collectstatic --no-input
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]