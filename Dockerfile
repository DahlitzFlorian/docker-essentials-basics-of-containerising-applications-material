FROM python:3.9

EXPOSE 5000

RUN mkdir /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app/ .

CMD [ "python", "main.py" ]
