import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange

x = np.array([-4, -1, 1, 2])
y = np.array([-6, 3, -11, -6])

def lagranz(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1
                p2 = p2 * 1
            else:
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])

        z = z + y[i] * p1/p2

    return z

xnew = np.linspace(np.min(x), np.max(x))
ynew = [lagranz(x, y, i) for i in xnew]
plt.plot(x, y, "o", xnew, ynew)
plt.grid()
plt.title("Інтерполяційний багаточлен Лагранжа")
plt.show()

f = lagrange(x, y)
fig = plt.figure(figsize=(10, 8))
plt.plot(xnew, f(xnew), "b", x, y, 'ro')
plt.title('Перевірка')
plt.grid()
plt.show()
