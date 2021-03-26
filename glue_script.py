from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession(SparkContext.getOrCreate())
spark.sql("show databases").show()
