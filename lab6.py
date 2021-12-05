from scipy import optimize
from math import sin
from math import cos
from math import fabs

x0 = -1.09
y0 = -0.9

def f1(y):
    return cos(y + 0.5) - 2

def f2(x):
    return (sin(x) - 1) / 2

def it_method(x, y, e):
    xn = x
    yn = y
    xn1 = f2(x)
    yn1 = f1(y)
    n = 1

    while((fabs(xn1 - xn) >= e) and (fabs(yn1 - yn) >= e)):
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn1 = f1(xn1)
        n += 1

    print("x1 =", xn, "\ny1 =", yn, "\nAmount of iteration =", n)

it_method(x0, y0, 0.001)

def re(x):
    return cos(x[1] + 0.5) - x[0] - 2, sin(x[0]) - 2*x[1] - 1

s = optimize.root(re, [0, 0], method="hybr")
print(s.x)
