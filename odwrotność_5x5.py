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


def odwrotnosc_gauss(macierz):
    rows = len(macierz)
    cols = len(macierz[0])
    if rows != cols:
        return 'macierz nie jest kwadratowa'
    elif wyznacznik(macierz) == 0:
        return 'wyznacznik = 0, macierz odwrotna nie istnieje'
    else:
        n = len(macierz)
        jednostkowa = [[0 for x in range(n)] for y in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    jednostkowa[i][j] = 1

        rozszerzona = [row + jednostkowa[i] for i, row in enumerate(macierz)]

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


A = [[2,-1,1,1,1,2], [1,-1,2,2,1,1],[5,-2,2,1,1,-4], [2,3,4,-2,1,-2], [2,3,4,7,-2,3], [3,2,-1,4,-4,2]]
A1 = [[3,2,-3,2,1], [4,6,3,-1,5], [2,5,-1,4,3], [1,2,3,4,5], [4,2,6,7,1]]
A2 = [[2,-1,1,1,1,2,1], [1,-1,2,2,1,1,3],[5,-2,2,1,1,-4,4], [2,3,4,-2,1,-2,2], [2,3,4,7,-2,3,1], [3,2,-1,4,-4,2,2]]


print(odwrotnosc_gauss(A))
print(odwrotnosc_gauss(A1))
print(odwrotnosc_gauss(A2))

