class BrakMiejsc(Exception):
    pass

class ZleMiejsce(Exception):
    pass

miejsca = [['O', 'O', 'O'],
           ['O', 'O', 'O'],
           ['O', 'O', 'O']]

zarezerwowane = 0

print('Wybierz akcje:\n1. Zarezerwuj miejsce\n2. Zobacz dostępne miejsca\n3. anuluj rezerwacje\n4. Wyjście')
akcja = input('Wybierz akcje: ')

while akcja != '4':
    if akcja == '1':
        if zarezerwowane == 9:
            raise BrakMiejsc('Brak miejsc na sali')
        
        rzad = input('Wybierz rzad: ')
        kolumna = input('Wybierz kolumne: ')
        if miejsca[int(rzad)-1][int(kolumna)-1] == 'X':
            raise ZleMiejsce('Miejsce jest już zajęte')
        
        miejsca[int(rzad)-1][int(kolumna)-1] = 'X'
        print('\nZarezerwowano miejsce\n')
        zarezerwowane += 1
        
        print('Wybierz akcje:\n1. Zarezerwuj miejsce\n2. Zobacz dostępne miejsca\n3. anuluj rezerwacje\n4. Wyjście')
        akcja = input('Wybierz akcje: ')
    if akcja == '2':
        print('\nDostępne miejsca:')
        print(miejsca)
        
        
        print('\nWybierz akcje:\n1. Zarezerwuj miejsce\n2. Zobacz dostępne miejsca\n3. anuluj rezerwacje\n4. Wyjście')
        akcja = input('Wybierz akcje: ')

    if akcja == '3':
        rzad = input('Wybierz rzad: ')
        kolumna = input('Wybierz kolumne: ')
        if miejsca[int(rzad)-1][int(kolumna)-1] == 'O':
            raise ZleMiejsce('Miejsce nie jest zarezerwowane')
        miejsca[int(rzad)-1][int(kolumna)-1] = 'O'
        zarezerwowane -= 1
        print('\nAnulowano rezerwacje\n')
        print('Wybierz akcje:\n1. Zarezerwuj miejsce\n2. Zobacz dostępne miejsca\n3. anuluj rezerwacje\n4. Wyjście')
        akcja = input('Wybierz akcje: ')





