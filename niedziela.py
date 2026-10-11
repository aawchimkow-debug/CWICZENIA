import os
from collections import Counter

realpath = r"D:\projekty\norario"
print(("Files: "), len([
    f for f in os.listdir(realpath)
    if os.path.isfile(os.path.join(realpath, f))
]))


rozmiar = sum(
    os.path.getsize(os.path.join(realpath, f))
    for f in os.listdir(realpath)
    if os.path.isfile(os.path.join(realpath, f))
)

print("Total size:", round(rozmiar / 1024, 1), "kb")

print("Extensions:")
extentions = Counter(
    os.path.splitext(f)[1]
    for f in os.listdir(realpath)
    if os.path.isfile(os.path.join(realpath, f))
)

for extentions, liczba in extentions.items():
    print(extentions or "[no extension]", ":", liczba)

print("Largest files:")

rozmiar2 = list(
    os.path.getsize(os.path.join(realpath, f))
    for f in os.listdir(realpath)
    if os.path.isfile(os.path.join(realpath, f))
)

najwieksze = sorted(rozmiar2, reverse=True)[:2]

for rozmiar in najwieksze:
    for f in os.listdir(realpath):
        sciezka = os.path.join(realpath, f)

        if os.path.isfile(sciezka):
            if os.path.getsize(sciezka) == rozmiar:
                print(rozmiar, "B ", sciezka)
                break


