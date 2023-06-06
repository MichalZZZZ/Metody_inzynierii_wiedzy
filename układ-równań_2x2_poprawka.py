def uklad_rownan(macierz, wektor):
    rows = len(macierz)
    cols = len(macierz[0])
    if rows != cols:
        return 'macierz nie jest kwadratowa'
    a = float(macierz[0][0])
    b = float(macierz[0][1])
    c = float(macierz[1][0])
    d = float(macierz[1][1])
    e = float(wektor[0][0])
    f = float(wektor[1][0])
    det = a * d - b * c
    if det == 0:
        if e / a != f / c:
            return 'Brak rozwiązań'
        else:
            return 'Nieskończenie wiele rozwiązań'
    else:
        wynik = [[0], [0]]
        x = (d * e - b * f) / det
        y = (-c * e + a * f) / det
        wynik[0][0] = x
        wynik[1][0] = y
        return wynik



A = [[2,-1], [1,-0.5]]
W = [[2], [1]]
A1 = [[2,-1], [1,-1]]
W1 = [[1], [2]]
A2 = [[2,-1], [2,-1]]
W2 = [[1], [2]]
print(uklad_rownan(A, W))
print(uklad_rownan(A1, W1))
print(uklad_rownan(A2, W2))
