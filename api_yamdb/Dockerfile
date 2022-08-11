FROM python:3.7-slim
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt --no-cache-dir
RUN pip3 install psycopg2-binary==2.9
ENTRYPOINT ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000"]