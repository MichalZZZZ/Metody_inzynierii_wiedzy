import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


def average(numbers_set):
    if len(numbers_set) == 0:
        return None
    else:
        sum = 0
        for num in numbers_set:
            sum += num
        return sum / len(numbers_set)


def standard_deviation(numbers_set):
    if len(numbers_set) == 0:
        return None
    else:
        result = 0
        for num in numbers_set:
            result += (num - average(numbers_set)) ** 2
        n = len(numbers_set) - 1
        result = math.sqrt(result / n)
    return result


def pearson_correlation(df):
    n = len(df)
    result = (n * sum(df['X'] * df['Y']) - sum(df['X'] * sum(df['Y']))) / (
        math.sqrt((n * sum(df['X'] ** 2) - sum(df['X']) ** 2) * (n * sum(df['Y'] ** 2) - sum(df['Y']) ** 2)))
    return result


def line_regression(x):
    return (b * x) + a


def predict_y(x, b, a):
    return (b * x) + a


df = pd.DataFrame()
df['X'] = [1, 2, 3, 4, 5]
df['Y'] = [4, 6, 9, 11, 18]

n = len(df['X'])
pearson = pd.DataFrame(df[:])
pearson['y2'] = df['Y'] ** 2
pearson['xy'] = df['X'] * df['Y']
pearson['x2'] = df['X'] ** 2
pearson['y2'] = df['Y'] ** 2
pearson.loc['sum'] = pearson.sum()

b = pearson_correlation(df) * (standard_deviation(df['Y']) / standard_deviation(df['X']))
a = average(df['Y']) - (b * average(df['X']))

print('n = ', n)
print(pearson)
print()
print(f'srednia dla x: {average(df["X"])}')
print(f'srednia dla y: {average(df["Y"])}')
print(f'odchylenie standardowe dla x: {standard_deviation(df["X"])}')
print(f'odchylenie standardowe dla y: {standard_deviation(df["Y"])}')
print(f'wspolczynnik kolelacji: {pearson_correlation(df)}')
print()

df.loc[5] = ({'X': 6, 'Y': np.nan})
df.loc[6] = ({'X': 7, 'Y': np.nan})
df.loc[7] = ({'X': 8, 'Y': np.nan})

print(df)
print()

df.at[5, 'Y'] = predict_y(df['X'][5], b, a)
df.at[6, 'Y'] = predict_y(df['X'][6], b, a)
df.at[7, 'Y'] = predict_y(df['X'][7], b, a)
print(df)

x = np.linspace(0, 9, 1000)
plt.scatter(df['X'], df['Y'], label='Wartosci niezalezne')
plt.plot(x, line_regression(x), 'r', label='Regresja liniowa')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
