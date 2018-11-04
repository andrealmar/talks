FROM python:3.6-alpine
WORKDIR /src
ADD requirements.txt /src
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /src
CMD gunicorn --bind 0.0.0.0:5000 --workers 10 app:app
EXPOSE 5000
