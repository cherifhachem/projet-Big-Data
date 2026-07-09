# Projet Stockage Big Data - Optimisation du stockage et des performances

## 1. Présentation du projet

Ce projet étudie l'optimisation du stockage de données massives dans un contexte où la bande passante et les ressources de stockage sont limitées.

Deux cas d'étude sont considérés :

- **SNIM** : logs de maintenance industrielle
- **SOMELEC** : relevés de consommation électrique

L'objectif est d'évaluer l'apport du format colonne **Apache Parquet** et des différentes méthodes de compression afin de réduire l'espace de stockage et améliorer les performances analytiques.

---

# 2. Objectifs

Les objectifs principaux sont :

- Comparer le stockage CSV et Parquet.
- Évaluer plusieurs compressions :
  - Parquet non compressé
  - Snappy
  - Gzip
- Mesurer les temps de lecture.
- Étudier l'impact du stockage colonne sur les traitements analytiques.
- Analyser le plan d'exécution Spark.
- Identifier les problèmes éventuels de déséquilibre des partitions (data skew).

---

# 3. Technologies utilisées

| Technologie | Utilisation |
|---|---|
| Python | Langage principal |
| Apache Spark | Traitement Big Data distribué |
| PySpark | API Python de Spark |
| Apache Parquet | Format de stockage colonne |
| Pandas | Analyse des résultats |
| Matplotlib | Visualisation |
| Conda | Gestion environnement |

Version principale :
Python 3.10
PySpark 4.1.2
Spark 4.1.2

---

# 4. Structure du projet

---

# 5. Installation

Activer l'environnement :

```bash
conda activate projet-stockage
pip install -r requirements.txt
python main.py
run_project.bat

CSV
 |
 |
Lecture Spark
 |
 |
Conversion Parquet
 |
 +---- Parquet non compressé
 |
 +---- Parquet Snappy
 |
 +---- Parquet Gzip
 |
 |
Analyse stockage
 |
Benchmark lecture
 |
Benchmark traitement
 |
Génération graphiques

| Format  | Réduction stockage |
| ------- | ------------------ |
| Parquet | 64.24 %            |
| Snappy  | 73.92 %            |
| Gzip    | 78.94 %            |


| Format  | Réduction stockage |
| ------- | ------------------ |
| Parquet | 61.98 %            |
| Snappy  | 65.79 %            |
| Gzip    | 74.10 %            |

3.425 secondes

0.790 seconde

environ 4.3 fois plus rapide

df.filter(...).select(...).explain(True)


Après enregistrement, faites :

```powershell
type README.md