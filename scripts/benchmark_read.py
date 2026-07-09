from pyspark.sql import SparkSession
import time

spark = SparkSession.builder.appName("benchmark-read").getOrCreate()

paths = {
    "snappy": "results/parquet/snappy",
    "gzip": "results/parquet/gzip",
    "uncompressed": "results/parquet/uncompressed"
}

print("\n⚡ Benchmark lecture Spark\n")

for name, path in paths.items():
    start = time.time()

    df = spark.read.parquet(path)
    df.count()  # force execution

    end = time.time()

    print(f"{name:15} -> {round(end - start, 3)} sec")

spark.stop()