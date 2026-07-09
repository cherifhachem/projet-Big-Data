import os
import sys
from pyspark.sql import SparkSession
from config.config import HDFS_CSV

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

def lire_csv():
    spark = (
        SparkSession.builder
        .appName("NYC Taxi")
        .master("local[*]")
        .getOrCreate()
    )

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(HDFS_CSV)
    )

    return spark, df