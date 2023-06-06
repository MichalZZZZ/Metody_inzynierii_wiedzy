

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


def odwrotnosc_gauss(matrix):
    if len(matrix) != 3:
        return 'macierz nie jest 3x3'
    elif wyznacznik(matrix) == 0:
        return 'macierz odwrotna nie istnieje'
    else:
        jednostkowa = [[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]]

        rozszerzona = [row + jednostkowa[i] for i, row in enumerate(matrix)]

        p1 = len(rozszerzona)
        p2 = len(rozszerzona[0])

        for j in range(p1):
            max_wierz = j
            for i in range(j + 1, p1):
                if abs(rozszerzona[i][j]) > abs(rozszerzona[max_wierz][j]):
                    max_wierz = i

            rozszerzona[j], rozszerzona[max_wierz] = rozszerzona[max_wierz], rozszerzona[j]

            for i in range(j + 1, p1):
                czynnik = rozszerzona[i][j] / rozszerzona[j][j]
                for k in range(j, p2):
                    rozszerzona[i][k] -= czynnik * rozszerzona[j][k]

        for j in range(p1 - 1, -1, -1):
            for i in range(j - 1, -1, -1):
                czynnik = rozszerzona[i][j] / rozszerzona[j][j]
                for k in range(p2 - 1, j - 1, -1):
                    rozszerzona[i][k] -= czynnik * rozszerzona[j][k]

            dzielnik = rozszerzona[j][j]
            for k in range(p2 - 1, j - 1, -1):
                rozszerzona[j][k] /= dzielnik

        macierz_odwrotna = [[row[i] for i in range(p1, p2)] for row in rozszerzona]

        return macierz_odwrotna


A = [[1,2,-3], [4,5,6],[7,8,9]]
B = [[-2,2,5], [-4,1,-2],[6,3,1]]
C = [[1,2,3],[4,5,6],[7,8,9]]
D = [[1,2,3],[4,6,5]]


print(odwrotnosc_gauss(A))
print(odwrotnosc_gauss(B))
print(odwrotnosc_gauss(C))
print(odwrotnosc_gauss(D))
