FROM python:3.8-slim
RUN apt-get update && apt-get install build-essential python-dev -y
COPY requirements.txt /var/www/html/requirements.txt
RUN pip install -r /var/www/html/requirements.txt && pip install uwsgi

COPY . /var/www/html
EXPOSE 9090
WORKDIR /var/www/html
CMD ["uwsgi", "--http", ":9090", "--wsgi-file", "khabarkoi/wsgi.py", "--master", "--processes", "4", "--threads", "2"]
