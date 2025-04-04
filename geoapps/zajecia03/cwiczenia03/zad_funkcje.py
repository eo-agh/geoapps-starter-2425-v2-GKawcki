
def zmien_wartosc(arg):
    if isinstance(arg, int):
        arg = 65482652
    if isinstance(arg, list):
        arg[0] = 'kalafior' 
    return arg



def zamowienie_produktu(nazwa_produktu, *, cena, ilosc = 1):
    wartosc = cena*ilosc
    return [wartosc, f"Zamówiłes {nazwa_produktu} za {wartosc}, w ilosci: {ilosc}"]


 


def stworz_raport(*args, **kwargs):
    dane = []      
    for id in args:
        cena = kwargs[f"cena_{id}"]
        nazwa = kwargs[f"nazwa_{id}"]
        print(f"Element {id}: {nazwa} za {cena}")
        




if __name__ == "__main__":
    a = 7
    b = [1, 2, 3]
    print(f"{zmien_wartosc(a)} {zmien_wartosc(b)}")
    wynik = []
    produkty = [
        ("Czekolada", {"cena": 4.5, "ilosc": 15}),
        ("Cukierki", {"cena": 1.5, "ilosc": 30}),
        ("Bezy", {"cena": 8, "ilosc": 5})
        ]
    for nazwa, parametry in produkty:
        wynik += zamowienie_produktu(nazwa, **parametry)
    print(wynik)
    stworz_raport(101, 102, nazwa_101="Kubek termiczny", cena_101="45.99 zł", nazwa_102="Długopis", cena_102="4.99 zł")





    