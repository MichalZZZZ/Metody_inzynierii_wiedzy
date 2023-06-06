import numpy as np

def transpozycja(macierz):
    wynik = [[0 for j in range(len(macierz))] for i in range(len(macierz[0]))]
    for i in range(len(macierz)):
        for j in range(len(macierz[0])):
            wynik[j][i] = macierz[i][j]
    return wynik

def mnozenie(macierz1, macierz2):
    x = transpozycja(macierz2)
    x2 = transpozycja(macierz1)
    if len(x) == len(macierz2) or len(macierz1) == len(macierz2) or len(x2) == len(macierz2):
        wynik = [[0 for j in range(len(macierz2[0]))] for i in range(len(macierz1))]
        for i in range(len(macierz1)):
            for j in range(len(macierz2[0])):
                for k in range(len(macierz1[0])):
                    wynik[i][j] += macierz1[i][k] * macierz2[k][j]
        return wynik
    else:
        return 'liczba kolumn w pierwszej macierzy musi równać się liczbie wierszy w drugiej'


macierz1 = [
    [1,2,3],
    [4,5,6],
    [4,5,6]
]

macierz2 = [
    [3,1,2],
    [2,4,2],
    [3,1,2]
]


macierz3 = [
    [3,1,2],
    [2,4,2],
    [3,1,2]
]

macierz4 = [
    [3,1],
    [2,4],
    [3,1]
]


macierz5 = [
    [3,1,2],
    [2,4,2],
    [3,1,2]
]

macierz6 = [
    [3,1,2],
    [2,4,2],
]


macierz7 = [
    [3,1],
    [2,4]
]

macierz8 = [
    [1,1],
    [6,7]
]

macierz9 = [
    [3,1,2],
    [2,4,2]
]

macierz10 = [
    [3,1],
    [2,4],
    [3,1]
]

print(mnozenie(macierz1, macierz2))
print(mnozenie(macierz3, macierz4))
print(mnozenie(macierz5, macierz6))
print(mnozenie(macierz7, macierz8))
print(mnozenie(macierz9, macierz10))