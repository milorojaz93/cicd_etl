FROM mysql:8.0

ENV MYSQL_DATABASE=ventas_db
ENV MYSQL_ROOT_PASSWORD=root

COPY init.sql /docker-entrypoint-initdb.d/
