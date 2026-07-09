from pyspark.sql import SparkSession


# Création SparkSession
spark = SparkSession.builder \
    .appName("Explain Plan Stockage") \
    .master("local[*]") \
    .getOrCreate()


# Chemins des données

csv_path = "../data/somelec_releves.csv"

parquet_path = "../data/somelec/parquet_snappy"


# =====================================
# Analyse CSV
# =====================================

print("\n==============================")
print("PLAN EXECUTION CSV")
print("==============================")


df_csv = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(csv_path)
)


requete_csv = (
    df_csv
    .filter(df_csv.consommation_kwh > 500)
    .select(
        "ville",
        "consommation_kwh"
    )
)


requete_csv.explain(True)



# =====================================
# Analyse Parquet Snappy
# =====================================

print("\n==============================")
print("PLAN EXECUTION PARQUET SNAPPY")
print("==============================")


df_parquet = spark.read.parquet(parquet_path)


requete_parquet = (
    df_parquet
    .filter(df_parquet.consommation_kwh > 500)
    .select(
        "ville",
        "consommation_kwh"
    )
)


requete_parquet.explain(True)



spark.stop()