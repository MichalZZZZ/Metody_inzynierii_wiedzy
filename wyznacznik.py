import numpy as np

#za pomoca Laplace'a
def wyznacznik(macierz):
    ilosc = len(macierz)
    if ilosc == 1:
        return macierz[0][0]
    elif ilosc == 2:
        return macierz[0][0] * macierz[1][1] - macierz[0][1] * macierz[1][0]
    else:
        det = 0
        for i in range(ilosc):
            m = [[macierz[j][k] for k in range(ilosc) if k != i] for j in range(1, ilosc)]
            det += (-1) ** i * macierz[0][i] * wyznacznik(m)
        return det


macierz1 = [
    [1,2,3],
    [4,5,6],
    [1,5,6]
]

macierz2 = [
    [4,2,3],
    [4,1,6],
    [1,5,9]
]

print(wyznacznik(macierz1))
print(wyznacznik(macierz2))