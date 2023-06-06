def rzad_macierzy(macierz):
    wiersze = len(macierz)
    kolumny = len(macierz[0])
    rzad = min(wiersze, kolumny)

    for row in range(rzad):
        if macierz[row][row] != 0:
            for kolumny2 in range(row+1, wiersze):
                mnoznik = macierz[kolumny2][row] / macierz[row][row]
                for i in range(rzad):
                    macierz[kolumny2][i] -= mnoznik * macierz[row][i]
        else:
            redukcja = True
            for row2 in range(row+1, wiersze):
                if macierz[row2][row] != 0:
                    macierz[row], macierz[row2] = macierz[row2], macierz[row]
                    redukcja = False
                    break
            if redukcja:
                rzad -= 1
                for i in range(wiersze):
                    macierz[i][row] = macierz[i][rzad]
            row -= 1

    return rzad


A = [[2,-1,1,1,1,2], [1,-1,2,2,1,1],[5,-2,2,1,1,-4], [2,3,4,-2,1,-2], [2,3,4,7,-2,3], [3,2,-1,4,-4,2]]
A1 = [[3,2,-3,2,1], [4,6,3,-1,5], [2,5,-1,4,3], [1,2,3,4,5], [4,2,6,7,1]]
A2 = [[2,-1,1,1,1,2,1], [1,-1,2,2,1,1,3],[5,-2,2,1,1,-4,4], [2,3,4,-2,1,-2,2], [2,3,4,7,-2,3,1], [3,2,-1,4,-4,2,2]]
A3 = [[1,0,0],[0,1,0],[0,0,1]]

print(rzad_macierzy(A))
print(rzad_macierzy(A1))
print(rzad_macierzy(A2))
print(rzad_macierzy(A3))

