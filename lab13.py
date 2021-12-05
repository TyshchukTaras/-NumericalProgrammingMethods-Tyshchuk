from scipy import integrate
from numpy import *

def f(x):
    return 1 / sqrt(0.5*x + 1.5)

v, err = integrate.quad(f, 1.2, 2)

def left(f, a, b, n):
    h = (b - a) / n
    sum = 0
    for i in range(0, n):
        sum += f(a + i * h)
    return sum * h

print("Left rectangle =", left(f, 1.2, 2, 10))

def right(f, a, b, n):
    h = (b - a) / n
    sum = 0
    for i in range(1, 1 + n):
        sum += f(a + i * h)
    return sum * h

print("Right rectangle =", right(f, 1.2, 2, 10))

def middle(f, a, b, n):
    h = (b - a) / n
    sum = 0
    for i in range(0, n):
        sum += f(a + i * h / 2)
    return sum * h

print("Middle rectangle =", middle(f, 1.2, 2, 10))
v, err = integrate.quad(f, 1.2, 2)
print('Check  =', v)

def f1(x):
    return log10(x**2 + 3) / (2*x)

def simpson(f1, a, b, n):
    h = (b - a) / n
    simp = f1(a) + f1(b)
    for i in range(1, n):
        f = a + i * h
        if i % 2 == 0:
            simp = simp + 2 * f1(f)
        else:
            simp = simp + 4 * f1(f)
    simp = simp * h / 3
    return simp

print("\nSimpsons method =", simpson(f1, 1.2, 2, 8))
v, err = integrate.quad(f1, 1.2, 2)
print('Check =', v)

def f2(x):
    return 1 / sqrt(x**2 + 0.6)

def tr_int(f2, a, b, n):
    h = (b - a) / n
    sum = 0.5 * (f2(a) + f2(b))
    for i in range(1, n):
        sum += f2(a + i * h)
    return sum * h

print('\nTrapezoidal method =', tr_int(f2, 1.2, 2.6, 20))
v, err = integrate.quad(f2, 1.2, 2.6)
print('Check =', v)