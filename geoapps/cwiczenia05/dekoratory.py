import time
def czas_wykonania(unit):
    def zmierz_czas(funkcja):
        def wrapper(*args, **kwargs):
            start = time.time()
            wynik = funkcja(*args, **kwargs)
            end = time.time()
            if unit == 'microseconds':
                start *= 1000000
                end *= 1000000
                print(f"Czas wykonania: {end - start} mikrosekund")
            elif unit == 'seconds':
                print(f"Czas wykonania: {end - start} sekund")
            
            return wynik
        return wrapper
    return zmierz_czas

@czas_wykonania(unit='microseconds')
def dodaj(a, b):
    for i in range(b):
        a += i
    return a

print(dodaj(14, 10000))