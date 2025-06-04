from pyspark.sql import SparkSession
from pyspark.sql.functions import col, date_format
from pyspark.sql.types import StringType
from pyspark.sql.functions import udf

@udf(returnType=StringType())
def map_proveedor(producto):
    return oProductos.get(producto, "Desconocido")

spark = SparkSession.builder \
    .appName("ETL Ventas por Proveedor") \
    .getOrCreate()

jdbc_url = "jdbc:mysql://mysql:3306/ventas_db?allowPublicKeyRetrieval=true&useSSL=false"
connection_props = {
    "user": "root",
    "password": "root",
    "driver": "com.mysql.cj.jdbc.Driver"
}

dfVentas = spark.read.jdbc(url=jdbc_url, table="ventas", properties=connection_props)
dfProveedores = spark.read.option("header", "true").csv("/output/proveedores.csv")
oProductos = {row["producto"]: row["proveedor"] for row in dfProveedores.collect()}
dfVentas = dfVentas.withColumn("proveedor", map_proveedor(col("producto")))
dfVentas = dfVentas.withColumn("fecha_part", date_format("fecha", "yyyy-MM-dd"))
dfSalida = dfVentas.groupBy("proveedor", "cliente_id", "fecha_part") \
    .agg({"id": "count", "monto": "sum"}) \
    .withColumnRenamed("count(id)", "cantidad_transacciones") \
    .withColumnRenamed("sum(monto)", "monto_total")

dfSalida.write \
    .partitionBy("proveedor", "fecha_part") \
    .mode("overwrite") \
    .parquet("/output/proveedores")

spark.stop()
