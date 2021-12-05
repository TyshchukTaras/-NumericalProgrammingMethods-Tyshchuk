import math

x = [2.4, 2.6, 2.8, 3.0, 3.2, 3.4]
y = [3.526, 3.782, 3.945, 4.043, 4.104, 4.155]

def diff(y, j):
    mas = []
    for i in range(len(y)):
        mas.append(y[i] - y[i-1])

    mas.pop(0)

    if j == 1:
        return mas
    else:
        j -= 1
        return diff(mas, j)

h = x[1] - x[0]

y1 = 1/h * (diff(y, 1)[1] - diff(y, 2)[1] / 2 + diff(y, 3)[1] / 3 - diff(y, 4)[1] / 4)
print("y'(x) =", round(y1, 4))

y2 = 1/h**2 * (diff(y, 2)[1] - diff(y, 3)[1] + 11/12 * diff(y, 4)[1])
print("y''(x) =", round(y2, 4))
