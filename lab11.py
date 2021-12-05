import sympy as sp

x = sp.symbols("x")
f = sp.sin(2 * x) * x

def t(x):
    y = 0
    d1 = sp.diff(f, x)
    d2 = sp.diff(d1, x)
    d3 = sp.diff(d2, x)

    print("d1 =", d1, "\nd2 =", d2, "\nd3 =", d3)

    y += f + d1 * x + d2 * (x - 0) ** 2 / 2 + d3 * (x - 0) ** 3 / 6

    print("y =", y)

    return y

p1 = sp.plot(f, t(x), (x, -5, 5))
p1.show()
