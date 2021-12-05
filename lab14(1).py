import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

xi = np.linspace(1.2, 2.2)
yi = np.linspace(2.1, 2.9)

ax.plot(xi, yi)
ax.grid()

plt.title('Метод Ейлера-Коші')
plt.xlabel("x")
plt.ylabel("y")
plt.show()
