from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt
from numpy import *

x = [0.8, 0.9, 1.2, 1.6, 2.1]
y = [1.42, 2.34, 3.48, 1.77, 2.66]

spl = UnivariateSpline(x, y)
xs = linspace(0, 2.8, 1000)

plt.plot(x, y, "ro", xs, spl(xs), "g")
plt.title("Інтерполяція сплайнами")
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["xs", "spl(xs)"])
plt.show()
