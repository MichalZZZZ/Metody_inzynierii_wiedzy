import numpy as np


def dodawaniewektorow(v1: list, v2: list):
    if len(v1) == len(v2):
        lista = []
        for i in range(len(v1)):
            lista.append(v1[i] + v2[i])
        return f'wynik dodawania: {lista}'
    else:
        return 'dlugosci nie sa równe'


def skalar(v1: list, v2: list):
    if len(v1) == len(v2):
        wynik = 0
        for i in range(len(v1)):
            wynik += v1[i] * v2[i]
        return f'wynik iloczynu skalarnego: {wynik}'
    else:
        return 'dlugosci nie sa równe'


a: list = [3, 0, 5]
b: list = [6, 4, -2]
print(dodawaniewektorow(a, b))
print(skalar(a, b))
