from pyspark.sql import SparkSession
import time
import os

spark = SparkSession.builder.appName("benchmark-full").getOrCreate()

input_path = "data/nyc_taxi.csv"

compressions = ["snappy", "gzip", "uncompressed"]

results = []

print("\n🚀 BENCHMARK COMPLET\n")

for comp in compressions:
    output_path = f"results/parquet/{comp}"

    # WRITE
    start_write = time.time()

    df = spark.read.option("header", True).option("inferSchema", True).csv(input_path)
    df.write.mode("overwrite").option("compression", comp).parquet(output_path)

    write_time = time.time() - start_write

    # READ
    start_read = time.time()
    df2 = spark.read.parquet(output_path)
    df2.count()
    read_time = time.time() - start_read

    # SIZE
    size = sum(
        os.path.getsize(os.path.join(root, f))
        for root, _, files in os.walk(output_path)
        for f in files
    ) / 1024 / 1024

    results.append((comp, write_time, read_time, size))

    print(f"{comp}")
    print(f"   write : {round(write_time, 3)} sec")
    print(f"   read  : {round(read_time, 3)} sec")
    print(f"   size  : {round(size, 2)} MB\n")

spark.stop()