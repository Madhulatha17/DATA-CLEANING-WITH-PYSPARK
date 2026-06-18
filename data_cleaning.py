from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("Data Cleaning Project") \
    .getOrCreate()

df = spark.read.csv("data/sample_data.csv", header=True, inferSchema=True)

print("Original Data")
df.show()

df = df.dropDuplicates()

df = df.fillna({
    "name": "Unknown",
    "age": 0,
    "city": "Not Available",
    "salary": 0
})

df = df.withColumn("age", col("age").cast("integer")) \
       .withColumn("salary", col("salary").cast("integer"))

print("Cleaned Data")
df.show()

df.write.mode("overwrite").csv("output/cleaned_data")

print("Data cleaning completed successfully!")

spark.stop()
