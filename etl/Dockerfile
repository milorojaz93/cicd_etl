FROM bitnami/spark:latest

USER root

# Crear carpeta para jars y copiar el conector
RUN mkdir -p /opt/spark/jars
COPY mysql-connector-j-9.3.0.jar /opt/spark/jars/mysql-connector-j-9.3.0.jar

# Establecer classpath para Spark (aunque Spark ya escanea esta ruta automáticamente)
ENV SPARK_CLASSPATH="/opt/spark/jars/mysql-connector-j-9.3.0.jar"
RUN mkdir -p /output
WORKDIR /app
COPY process_prov.py .
