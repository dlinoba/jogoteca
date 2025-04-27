FROM python:3.11-slim AS jogotecaapp

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

ENTRYPOINT ["python","./jogoteca.py"]


FROM mysql/mysql-server:5.7 as jogotecadb

ARG ROOT_PASSWORD=1234
ENV MYSQL_ROOT_PASSWORD=${ROOT_PASSWORD}

ARG SETUP_DATABASE=JOGOTECA
ENV MYSQL_DATABASE=${SETUP_DATABASE}

ARG SETUP_REMOTE_USERNAME=admin
ARG SETUP_REMOVE_PASSWORD=1234

COPY ./prepara_banco.sql /docker-entrypoint-initdb.d/prepara_banco.sql

RUN echo "CREATE USER '${SETUP_REMOTE_USERNAME}'@'%' IDENTIFIED BY '${SETUP_REMOVE_PASSWORD}';GRANT ALL PRIVILEGES ON *.* TO '${SETUP_REMOTE_USERNAME}'@'%' WITH GRANT OPTION;" > /docker-entrypoint-initdb.d/_grant_remote.sql

EXPOSE 3306

CMD ["mysqld"]