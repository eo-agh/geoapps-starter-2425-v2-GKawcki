

if __name__ == "__main__":
    dane = (2024, 'Python', 3.8)
    rok, jezyk, wersja = dane
    print(rok)
    print(jezyk)
    print(wersja)

    oceny = [4, 3, 5, 2, 5, 4]
    pierwsza, *srodek, ostatnia = oceny
    print(pierwsza)
    print(srodek)
    print(ostatnia)

    info = ('Jan', 'Kowalski', 30, 'Polska', 'programista')

    imie, nazwisko, _, _, zawod = info
    print(imie)
    print(nazwisko)
    print(zawod)


    dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')])
    rok, [jezyk, wersja, (opis1, opis2)] = dane
    opis =f"{opis1} {opis2}"
    print(rok)
    print(jezyk)
    print(wersja)
    print(opis)

    a = b = [1, 2, 3]
    b[0] = 'zmieniono'
    print(a[0])
    print(b[0])

    a = b = [1, 2, 3]
    c = a[:]
    c[0] = 'nowa wartosc'
    print(a[0])
    print(b[0])
    print(c[0])

    x = y = 10
    y = y + 1
    print(x)
    print(y)

    K = [1, 2]
    L = K
    # konkatenacja
    K = K + [3, 4]
    M = [1, 2]
    N = M
    # przypisanie rozszerzone
    M += [3, 4]
    print(K)
    print(L)
    print(M)
    print(N)