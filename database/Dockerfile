FROM postgres:12.11
ENV POSTGRES_PASSWORD admin
ENV POSTGRES_USER admin
ENV POSTGRES_DB postgrez
COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql