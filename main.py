import os

os.environ["PYSPARK_PYTHON"] = "python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python"


from pyspark.sql import SparkSession

from scripts.convert import convert_csv_to_parquet
from scripts.size_analysis import analyse_sizes
from scripts.benchmark import benchmark_read
from scripts.column_benchmark import benchmark_column_access



def main():

    spark = (
        SparkSession.builder
        .appName("Benchmark Stockage Big Data")
        .master("local[*]")
        .getOrCreate()
    )


    spark.sparkContext.setLogLevel("ERROR")


    fichiers = [

        (
            "data/snim_logs.csv",
            "data/snim"
        ),

        (
            "data/somelec_releves.csv",
            "data/somelec"
        )

    ]


    # Conversion CSV -> Parquet
    for fichier, sortie in fichiers:

        convert_csv_to_parquet(
            spark,
            fichier,
            sortie
        )


    # Analyse des tailles
    analyse_sizes(
        "snim_logs"
    )

    analyse_sizes(
        "somelec_releves"
    )


    # Benchmark lecture
    benchmark_read(
        spark,
        "snim_logs",
        "data"
    )


    benchmark_read(
        spark,
        "somelec_releves",
        "data"
    )

    benchmark_column_access(
        spark
    )
    spark.stop()



if __name__ == "__main__":
    main()