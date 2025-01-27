def eldont(szam):
    if szam > 0:
        print("A szám pozitív")
    elif szam < 0:
        print("Ez a szam negatív")
    elif szam == 0:
        print("Ez a szam 0")

foj = True

while foj:
    szam = input("Adj meg egy számot")

    if szam == "":
        foj = False
        break

    else:
        foj = True
        eldont(int(szam))#szniki szex
