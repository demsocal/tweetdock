FROM python:3.8
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY tweet-app.py tweet-app.py
COPY .env .env
CMD ["python", "tweet-app.py"]