FROM python:3.8
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY tweet-app.py tweet-app.py
COPY tweet-app-dummy.py tweet-app-dummy.py
COPY test.py test.py
COPY .env .env
CMD ["python3", "test.py"]



