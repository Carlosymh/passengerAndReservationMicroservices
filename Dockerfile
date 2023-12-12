FROM python:3.9

WORKDIR /app

COPY requirements.txt .


RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

COPY . /app


EXPOSE 8000

ENTRYPOINT ["/app/django.sh"]