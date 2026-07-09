import pandas as pd
import os
import time


def benchmark_column_access(spark):

    print("\n================================")
    print("Benchmark SOMELEC : colonne consommation")
    print("================================")


    resultats = []


    fichiers = {

        "CSV":
        "data/somelec_releves.csv",


        "Snappy":
        "data/somelec/parquet_snappy"

    }


    for format, chemin in fichiers.items():


        print("\nFormat :", format)


        debut = time.time()


        if format == "CSV":


            df = (
                spark.read
                .option("header", True)
                .option("inferSchema", True)
                .csv(chemin)
            )


        else:


            df = spark.read.parquet(chemin)



        # Requête métier SOMELEC
        resultat = (
            df
            .select("consommation_kwh")
            .groupBy()
            .avg("consommation_kwh")
        )


        # Force l'exécution Spark
        valeur = resultat.collect()[0][0]


        temps = round(
            time.time() - debut,
            3
        )


        print(
            "Consommation moyenne :",
            round(valeur,2)
        )


        print(
            "Temps traitement :",
            temps,
            "secondes"
        )


        resultats.append({

            "format": format,

            "temps": temps

        })
    os.makedirs(
        "results",
        exist_ok=True
    )

    df_resultats = pd.DataFrame(resultats)

    df_resultats.to_csv(
        "results/column_benchmark.csv",
        index=False
    )

    print(
        "\nRésultats sauvegardés dans results/column_benchmark.csv"
    )

    return resultats