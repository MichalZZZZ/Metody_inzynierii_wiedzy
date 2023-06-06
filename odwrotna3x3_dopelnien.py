

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


def oblicz_odwrotnosc(macierz):
    det = wyznacznik(macierz)
    if len(macierz) != 3:
        return 'macierz nie jest 3x3'
    elif det != 0:
        dopelnienie = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        dopelnienie[0][0] = (macierz[1][1] * macierz[2][2] - macierz[2][1] * macierz[1][2])
        dopelnienie[0][1] = -(macierz[1][0] * macierz[2][2] - macierz[1][2] * macierz[2][0])
        dopelnienie[0][2] = (macierz[1][0] * macierz[2][1] - macierz[1][1] * macierz[2][0])
        dopelnienie[1][0] = -(macierz[0][1] * macierz[2][2] - macierz[0][2] * macierz[2][1])
        dopelnienie[1][1] = (macierz[0][0] * macierz[2][2] - macierz[0][2] * macierz[2][0])
        dopelnienie[1][2] = -(macierz[0][0] * macierz[2][1] - macierz[0][1] * macierz[2][0])
        dopelnienie[2][0] = (macierz[0][1] * macierz[1][2] - macierz[0][2] * macierz[1][1])
        dopelnienie[2][1] = -(macierz[0][0] * macierz[1][2] - macierz[0][2] * macierz[1][0])
        dopelnienie[2][2] = (macierz[0][0] * macierz[1][1] - macierz[0][1] * macierz[1][0])

        transpozycja = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                transpozycja[i][j] = dopelnienie[j][i]

        odwrotna = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                odwrotna[i][j] = transpozycja[i][j] / det

        return odwrotna
    else:
        return 'macierz odwrotna nie istnieje'


A = [[1,2,-3], [4,5,6],[7,8,9]]
B = [[-2,2,5], [-4,1,-2],[6,3,1]]
C = [[1,2,3],[4,5,6],[7,8,9]]
D = [[1,2,3],[4,6,5]]

print(oblicz_odwrotnosc(A))
print(oblicz_odwrotnosc(B))
print(oblicz_odwrotnosc(C))
print(oblicz_odwrotnosc(D))