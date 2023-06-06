import numpy as np

def transpozycja(macierz):
    wynik = [[0 for j in range(len(macierz))] for i in range(len(macierz[0]))]
    for i in range(len(macierz)):
        for j in range(len(macierz[0])):
            wynik[j][i] = macierz[i][j]
    return wynik

macierz1 = [
    [1,2,3],
    [4,5,6],
    [4,5,6]
]

macierz6 = [
    [3,1,2],
    [2,4,2],
]

macierz8 = [
    [1,1],
    [6,7]
]

print(transpozycja(macierz1))
print(transpozycja(macierz6))
print(transpozycja(macierz8))
