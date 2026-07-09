import time
import pandas as pd
import os



def measure_time(function):
    """
    Mesure le temps d'exécution d'une fonction.
    """

    debut = time.time()

    result = function()

    fin = time.time()

    return result, round(fin - debut, 3)



def benchmark_read(spark, dataset, base_path):


    print("\n================================")
    print("Benchmark lecture :", dataset)
    print("================================")


    fichiers = {


        "CSV":
            f"{base_path}/{dataset}.csv",


        "Parquet":
            f"{base_path}/{dataset.split('_')[0]}/parquet_uncompressed",


        "Snappy":
            f"{base_path}/{dataset.split('_')[0]}/parquet_snappy",


        "Gzip":
            f"{base_path}/{dataset.split('_')[0]}/parquet_gzip"

    }


    resultats = []


    for format, chemin in fichiers.items():


        print("\nLecture :", format)


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



        # Force Spark à exécuter réellement la lecture
        nombre_lignes = df.count()


        temps = round(
            time.time() - debut,
            3
        )


        print(
            "Nombre lignes :",
            nombre_lignes
        )

        print(
            "Temps lecture :",
            temps,
            "secondes"
        )


        resultats.append({

            "dataset": dataset,

            "format": format,

            "temps_lecture_s": temps

        })
    os.makedirs(
        "results",
        exist_ok=True
    )

    df_resultats = pd.DataFrame(resultats)

    df_resultats.to_csv(
        "results/read_benchmark.csv",
        index=False
    )

    print(
        "\nRésultats sauvegardés dans results/read_benchmark.csv"
    )

    return resultats