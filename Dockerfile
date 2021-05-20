<<<<<<< HEAD
FROM python:3.7-alpine
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . /app
CMD ["python", "app.py"]
=======
FROM python:3.7-alpine 

WORKDIR /app 

COPY . . 

RUN pip install -r requirements.txt

CMD ["app.py"]
ENTRYPOINT ["python"]

>>>>>>> [main] five minutes later
