import matplotlib.pyplot as plt

compressions = ["snappy", "gzip", "uncompressed"]

write = [1.2, 2.1, 0.9]  # remplacé par tes résultats
read = [0.5, 0.7, 0.4]
size = [50, 30, 120]

plt.figure()
plt.bar(compressions, size)
plt.title("Taille des fichiers Parquet")
plt.show()

plt.figure()
plt.bar(compressions, read)
plt.title("Temps de lecture")
plt.show()