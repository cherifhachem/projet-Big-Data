import pandas as pd
import matplotlib.pyplot as plt
import os


os.makedirs(
    "results/figures",
    exist_ok=True
)


def plot_storage():

    df = pd.read_csv(
        "results/compression_results.csv"
    )

    for dataset in df["dataset"].unique():

        data = df[df["dataset"] == dataset]

        plt.figure(figsize=(8,5))

        plt.bar(
            data["format"],
            data["taille_Mo"]
        )

        plt.title(
            "Comparaison stockage - " + dataset
        )

        plt.xlabel("Format")
        plt.ylabel("Taille (Mo)")

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.savefig(
            f"results/figures/{dataset}_storage.png"
        )

        plt.close()



def plot_reduction():

    df = pd.read_csv(
        "results/compression_results.csv"
    )


    for dataset in df["dataset"].unique():

        data = df[
            df["dataset"] == dataset
        ]


        plt.figure(figsize=(8,5))


        plt.bar(
            data["format"],
            data["reduction_%"]
        )


        plt.title(
            "Réduction stockage - " + dataset
        )


        plt.xlabel(
            "Format"
        )


        plt.ylabel(
            "Réduction (%)"
        )


        plt.xticks(rotation=45)

        plt.tight_layout()


        plt.savefig(
            f"results/figures/{dataset}_reduction.png"
        )


        plt.close()



def plot_read():

    df = pd.read_csv(
        "results/read_benchmark.csv"
    )


    for dataset in df["dataset"].unique():

        data = df[
            df["dataset"] == dataset
        ]


        plt.figure(figsize=(8,5))


        plt.bar(
            data["format"],
            data["temps_lecture_s"]
        )


        plt.title(
            "Temps de lecture - " + dataset
        )


        plt.xlabel(
            "Format"
        )


        plt.ylabel(
            "Temps (secondes)"
        )


        plt.xticks(rotation=45)


        plt.tight_layout()


        plt.savefig(
            f"results/figures/{dataset}_read.png"
        )


        plt.close()



def plot_column_benchmark():

    df = pd.read_csv(
        "results/column_benchmark.csv"
    )


    plt.figure(figsize=(8,5))


    plt.bar(
        df["format"],
        df["temps_traitement_s"]
    )


    plt.title(
        "Benchmark analytique SOMELEC"
    )


    plt.xlabel(
        "Format"
    )


    plt.ylabel(
        "Temps (secondes)"
    )


    plt.tight_layout()


    plt.savefig(
        "results/figures/column_processing.png"
    )


    plt.close()



if __name__ == "__main__":

    plot_storage()

    plot_reduction()

    plot_read()

    plot_column_benchmark()


    print(
        "Graphiques générés"
    )
