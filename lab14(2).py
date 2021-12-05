import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

xi = np.linspace(0.8, 1.8)
yi = np.linspace(1.3, 4.6782)

ax.plot(xi, yi)
ax.grid()

plt.title("Метод Ейлера")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
