from pyspark.sql import SparkSession

spark = SparkSession.builder\
        .appName("With example in pyspark")\
        .master("local[1]")\
        .getOrCreate()


data = [
    ('James','','Smith','1991-04-01','M',3000),
    ('Michael','Rose','','2000-05-19','M',4000),
    ('Robert','','Williams','1978-09-05','M',4000),
    ('Maria','Anne','Jones','1967-12-01','F',4000),
    ('Jen','Mary','Brown','1980-02-17','F',-1)
]

column = ["firstName","middleName","lastName","dob","gender","salary"]

df = spark.createDataFrame(data,schema=column)

df.printSchema()
df.show()

from pyspark.sql.functions import col,lit
df.withColumn("salary",col("salary").cast("Integer")).printSchema()

df.withColumn("salary",col("salary")*100).show()

df.withColumn("salaryNew",col("salary") *-1).show()


df.withColumn("country",lit("USA")).show()

df.withColumn("Country", lit("USA")) \
  .withColumn("anotherColumn",lit("anotherValue")) \
  .show()