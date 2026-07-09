import os
import pandas as pd


def get_folder_size(path):

    total = 0

    if os.path.isfile(path):
        return os.path.getsize(path)

    if os.path.exists(path):

        for root, dirs, files in os.walk(path):

            for file in files:

                filepath = os.path.join(root, file)

                total += os.path.getsize(filepath)

    return total



def bytes_to_mb(size):

    return round(size / (1024 * 1024), 2)



def compression_rate(original, compressed):

    return round(
        ((original - compressed) / original) * 100,
        2
    )



def analyse_sizes(dataset_name):


    print("\n==============================")
    print("Analyse :", dataset_name)
    print("==============================")


    fichiers = {

        "CSV":
            f"data/{dataset_name}.csv",

        "Parquet":
            f"data/{dataset_name.split('_')[0]}/parquet_uncompressed",

        "Snappy":
            f"data/{dataset_name.split('_')[0]}/parquet_snappy",

        "Gzip":
            f"data/{dataset_name.split('_')[0]}/parquet_gzip"

    }


    resultats = []


    taille_csv = get_folder_size(
        fichiers["CSV"]
    )


    for format, chemin in fichiers.items():


        taille = get_folder_size(
            chemin
        )


        reduction = 0


        if format != "CSV":

            reduction = compression_rate(
                taille_csv,
                taille
            )


        resultat = {

            "dataset": dataset_name,

            "format": format,

            "taille_Mo":
                bytes_to_mb(taille),

            "reduction_%":
                reduction

        }


        print(resultat)


        resultats.append(resultat)



    # ==========================
    # Sauvegarde CSV
    # ==========================

    os.makedirs(
        "results",
        exist_ok=True
    )


    df = pd.DataFrame(
        resultats
    )


    df.to_csv(
        "results/compression_results.csv",
        mode="a",
        header=not os.path.exists(
            "results/compression_results.csv"
        ),
        index=False
    )


    print(
        "Résultats sauvegardés"
    )


    return resultats