def stworz_funkcje_potegujaca(wykladnik):
    def poteguj(podstawa):
        return podstawa ** wykladnik
    return poteguj  

def suma_nonlocal():
    suma_nl = 0


    def licznik_1():
        nonlocal suma_nl
        suma_nl += 1
        return suma_nl
    return licznik_1

suma_global = 0

def licznik_2():
    global suma_global
    suma_global += 1
    return suma_global



if __name__ == "__main__":
    potega_2 = stworz_funkcje_potegujaca(2)
    print(potega_2(4))