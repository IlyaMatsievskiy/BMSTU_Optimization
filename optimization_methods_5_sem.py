# -*- coding: utf-8 -*-
"""optimization methods_5_sem.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1v1eLEaklAx9z6uR_nZRte77a_pEcNctB
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x ** 2 + 3 * x * (math.log(x) - 1)

x = []
y = []
for i in np.arange(0.5, 1, 0.01, dtype = float):
    x.append(i)
    y.append(f(i))
plt.plot(x, y, color='blue')
plt.show()

"""**Lab 1. Метод деления отрезка пополам**"""

def bisection(a, b, e):
    if b - a < 2 * e:
        return (a + b) / 2
    d = e
    x1 = (a + b - d) / 2
    x2 = (a + b + d) / 2
    f1 = f(x1)
    f2 = f(x2)
    if f1 <= f2:
        return bisection(a, x2, e)
    else:
        return bisection(x1, b, e)

print(bisection(0.5, 1, 0.05))

"""**Lab 2. Метод золотого сечения**"""

def golden_ratio(a, b, e, x1, x2, T = (math.sqrt(5) - 1) / 2):
    if b - a < 2 * e:
        return (a + b) / 2
    f1 = f(x1)
    f2 = f(x2)
    if f1 <= f2:
        b = x2
        x2 = x1
        x1 = a + (1 - T) * (b - a)
        return golden_ratio(a, b, e, x1, x2)
    else:
        a = x1
        x1 = x2
        x2 = a + T * (b - a)
        return golden_ratio(a, b, e, x1, x2)

a = 0.5
b = 1
e = 0.05
T = (math.sqrt(5) - 1) / 2
x1 = a + (1 - T) * (b - a)
x2 = a + T * (b - a)
print(golden_ratio(a, b, e, x1, x2))

"""**Lab 3. Метод Ньютона**"""