from pyspark.sql import SparkSession
import time
import os


def convert_csv_to_parquet(
        spark,
        input_file,
        output_folder
):

    print("\n================================")
    print("Conversion :", input_file)
    print("================================")


    # -----------------------------
    # Lecture CSV
    # -----------------------------

    debut = time.time()


    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(input_file)
    )


    temps_lecture = time.time() - debut


    print(
        "Temps lecture CSV :",
        round(temps_lecture,2),
        "secondes"
    )


    df.printSchema()


    # -----------------------------
    # Conversion Parquet
    # -----------------------------


    compressions = {

        "uncompressed": "uncompressed",

        "snappy": "snappy",

        "gzip": "gzip"

    }


    resultats = []


    for nom, compression in compressions.items():


        chemin = (
            output_folder
            + "/parquet_"
            + nom
        )


        debut = time.time()


        (
            df.write
            .mode("overwrite")
            .option(
                "compression",
                compression
            )
            .parquet(chemin)
        )


        temps_ecriture = (
            time.time() - debut
        )


        print(
            "Création",
            nom,
            ":",
            round(
                temps_ecriture,
                2
            ),
            "secondes"
        )


        resultats.append(
            {
                "format": "Parquet",
                "compression": compression,
                "temps_ecriture": temps_ecriture
            }
        )


    return resultats