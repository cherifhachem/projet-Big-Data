import os

BASE = "results/parquet"

def folder_size(path):
    total = 0
    for root, _, files in os.walk(path):
        for f in files:
            total += os.path.getsize(os.path.join(root, f))
    return round(total / 1024 / 1024, 2)

if __name__ == "__main__":
    print("📦 Taille des fichiers Parquet (MB)")
    print("Snappy        :", folder_size(BASE + "/snappy"))
    print("Gzip          :", folder_size(BASE + "/gzip"))
    print("Uncompressed  :", folder_size(BASE + "/uncompressed"))