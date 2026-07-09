import csv
import random
import os
from datetime import datetime, timedelta


# ===============================
# Configuration
# ===============================

NOMBRE_LIGNES = 1_000_000

DOSSIER_SORTIE = "data"

os.makedirs(DOSSIER_SORTIE, exist_ok=True)


# ===============================
# Générateur SNIM
# ===============================

def generate_snim(filename, n):

    machines = [
        "Locomotive_01",
        "Locomotive_02",
        "Convoyeur_01",
        "Concasseur_01",
        "Pelleteuse_01"
    ]

    sites = [
        "Zouerate",
        "Guelb",
        "M'haoudat",
        "Nouadhibou"
    ]

    techniciens = [
        "Ahmed",
        "Mohamed",
        "Oumar",
        "Salem"
    ]


    with open(filename, "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow([
            "id_machine",
            "site",
            "date_intervention",
            "temperature",
            "vibration",
            "pression",
            "temps_arret",
            "cout_maintenance",
            "technicien"
        ])


        date_depart = datetime(2024,1,1)


        for i in range(n):

            date = date_depart + timedelta(
                minutes=random.randint(0,500000)
            )

            writer.writerow([

                random.choice(machines),

                random.choice(sites),

                date.strftime("%Y-%m-%d %H:%M:%S"),

                round(random.uniform(40,120),2),

                round(random.uniform(0.1,10),2),

                round(random.uniform(5,50),2),

                random.randint(5,500),

                round(random.uniform(500,20000),2),

                random.choice(techniciens)
            ])


    print("SNIM terminé :", filename)



# ===============================
# Générateur SOMELEC
# ===============================

def generate_somelec(filename, n):


    villes = [
        "Nouakchott",
        "Zouerate",
        "Rosso",
        "Atar",
        "Kaedi"
    ]


    types = [
        "Domestique",
        "Industriel",
        "Commercial"
    ]


    with open(filename, "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)


        writer.writerow([

            "id_client",
            "ville",
            "quartier",
            "date_releve",
            "consommation_kwh",
            "tension",
            "puissance",
            "type_abonnement",
            "latitude",
            "longitude"

        ])



        date_depart = datetime(2024,1,1)


        for i in range(n):


            date = date_depart + timedelta(
                days=random.randint(0,365)
            )


            writer.writerow([

                i,

                random.choice(villes),

                "Quartier_" + str(random.randint(1,50)),

                date.strftime("%Y-%m-%d"),

                round(random.uniform(20,1000),2),

                random.choice([220,230,240]),

                round(random.uniform(1,20),2),

                random.choice(types),

                round(random.uniform(15,27),6),

                round(random.uniform(-17,-5),6)

            ])


    print("SOMELEC terminé :", filename)



# ===============================
# Programme principal
# ===============================


if __name__ == "__main__":


    generate_snim(
        "data/snim_logs.csv",
        NOMBRE_LIGNES
    )


    generate_somelec(
        "data/somelec_releves.csv",
        NOMBRE_LIGNES
    )