FROM python:3.6-alpine

LABEL maintainer="james.luke@hotmail.com"

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

# TODO: use worker count from env
CMD ["gunicorn", "-b 0.0.0.0:8000", "-w 4", "wsgi:app"]
