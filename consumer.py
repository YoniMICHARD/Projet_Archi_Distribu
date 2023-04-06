from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import from_json, col


spark = SparkSession.builder.appName('ML-Projet').master('spark://spark-master:7077').getOrCreate()
spark.sparkContext.setLogLevel('WARN')
KAFKA_BOOTSTRAP_SERVERS = 'kafka:9092'
KAFKA_TOPIC = 'myproject'

SCHEMA = StructType
([
        StructField("Entity",StringType())
])

df = spark.readStream \
.format("kafka") \
.option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS) \
.option("subscribe", KAFKA_TOPIC) \
.load() \
# .select(from_json(col("value").cast("string"), SCHEMA).alias("data")) \
# .selectExpr("data.Entity") \
df.printSchema()

schema = StructType().add("Entity", StringType())
personneString = df.selectExpr("CAST(value AS STRING)")
personnedf = personneString.select(from_json(col("value"),schema).alias("data")).select("data.*")

personnedf.writeStream.format("console").outputMode("append").start().awaitTermination()
# df.writeStream \
# .format("console") \
# .outputMode("update")\
# .option("truncate", "false") \
# .start() \
# .awaitTermination()