def kwadrat(x):
    return x ** 2



if __name__ == "__main__":
    imiona = ['Anna', 'Jan', 'Ewa']
    oceny = [5, 4, 3]
    for imie, ocena in zip(imiona, oceny):
        print(f"{imie} {ocena} ")
    liczby = [1, 2, 3, 4, 5]
    kwadraty = list(map(kwadrat, liczby))
    print(kwadraty)