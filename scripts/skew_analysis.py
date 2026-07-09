import os

os.environ["PYSPARK_PYTHON"] = "python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python"


from pyspark.sql import SparkSession
from pyspark.sql.functions import count


# Création Spark
spark = SparkSession.builder \
    .appName("Analyse Data Skew") \
    .master("local[*]") \
    .getOrCreate()


# Chemin Parquet Snappy
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

path = os.path.join(
    BASE_DIR,
    "data",
    "somelec",
    "parquet_snappy"
)
# Lecture des données
df = spark.read.parquet(path)


print("\n==============================")
print("DISTRIBUTION PAR VILLE")
print("==============================")


# Nombre de lignes par ville
df.groupBy("ville") \
    .agg(count("*").alias("nombre_releves")) \
    .orderBy("nombre_releves", ascending=False) \
    .show(20)



print("\n==============================")
print("NOMBRE DE PARTITIONS")
print("==============================")


print(
    "Partitions actuelles :",
    df.rdd.getNumPartitions()
)



print("\n==============================")
print("TAILLE DES PARTITIONS")
print("==============================")


tailles_partitions = (
    df.rdd
    .mapPartitions(lambda x: [sum(1 for _ in x)])
    .collect()
)


for i, taille in enumerate(tailles_partitions):

    print(
        "Partition",
        i,
        ":",
        taille,
        "lignes"
    )



# ==============================
# Test après repartitionnement
# ==============================

print("\n==============================")
print("APRES REPARTITION PAR VILLE")
print("==============================")


df_repart = df.repartition("ville")


print(
    "Partitions après repartition :",
    df_repart.rdd.getNumPartitions()
)


tailles_repart = (
    df_repart.rdd
    .mapPartitions(lambda x: [sum(1 for _ in x)])
    .collect()
)


for i, taille in enumerate(tailles_repart):

    print(
        "Partition",
        i,
        ":",
        taille,
        "lignes"
    )



spark.stop()