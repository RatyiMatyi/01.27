"""Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás
segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!"""

szavak = []

for i in range(3):
    szo = input("Adj meg egy szót: ")
    szavak.append(szo)
print(szavak)

def legrovideb(szavak):
    legrovidebb = szavak[0]
    for szo in szavak:
        if len(szo) < len(legrovidebb):
            legrovidebb = szo
    print(f"Legrövidebb szó: {legrovidebb} ")
legrovideb(szavak)


