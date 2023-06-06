import numpy as np

def mnozeniewektora(v1: list, skalar: int):
    lista = []
    for i in range(len(v1)):
        lista.append(v1[i] * skalar)
    return lista

a: list = [3, 0, 5]
skalar = 3

print(mnozeniewektora(a, skalar))