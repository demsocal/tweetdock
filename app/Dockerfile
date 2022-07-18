FROM python:3.8
WORKDIR /code
ENV POSTGRES_PASSWORD admin
ENV POSTGRES_USER admin
ENV POSTGRES_DB postgrez
ENV API_Key pVKx2qkOL7NMpHKlqu1dBQCyO
ENV API_Key_Secret HgNZoBsRAZg2fGtiMoOGAoHOzMU7IeqfYXUom7txqmWBQtjztp
ENV Access_Token 1382296867317325825-yfFRAcuM1mYeQlaHIs7QLnosuzPhNC
ENV Access_Token_Secret LmHbboVZD6obTwBiNdOPnl3cbav5KM4IIao2fc7WYows3
ENV Bearer_Token AAAAAAAAAAAAAAAAAAAAAOXQegEAAAAAN3ttS28U9UzWbksPrqhLXwvWspQ%3DxHxAnm9PKieOK5MxDoI2yGoWnUB6T8B9BzhVi4EiokXqmx7SbW
ENV dbserver db
ENV user admin
ENV password admin
ENV database postgrez
ENV port 5432
ENV table_emp employees
ENV table_tweet tweets
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY tweet-app.py tweet-app.py
COPY .env .env
CMD ["python3", "tweet-app.py"]


