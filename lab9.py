from math import factorial

x = [0.15, 0.16, 0.17, 0.18, 0.19, 0.2]
y = [4.4817, 4.9530, 5.4739, 6.0496, 6.6859, 7.3891]

x1 = 0.159
x2 = 0.234

h = x[1] - x[0]
q1 = (x1 - x[0]) / h
q2 = (x2 - x[-1]) / h

def n(y, j):
    mas = []
    for i in range(len(y)):
        mas.append(y[i] - y[i-1])

    mas.pop(0)
    if j == 1:
        return mas
    else:
        j -= 1
        return n(mas, j)

g1_1 = y[0] + q1 * n(y, 1)[0] + q1 * (q1 - 1) * n(y, 2)[0] / factorial(2)
g2_1 = q1 * (q1 - 1) * (q1 - 2) * n(y, 3)[0] / factorial(3)
g3_1 = q1 * (q1 - 1) * (q1 - 2) * (q1 - 3) * n(y, 4)[0] / factorial(4)
g4_1 = q1 * (q1 - 1) * (q1 - 2) * (q1 - 3) * (q1 - 4) * n(y, 5)[0] / factorial(5)

r1 = g1_1 + g2_1 + g3_1 + g4_1

print("Newton's first interpolation =", r1)

g1_2 = y[5] + q2 * n(y, 1)[4] + q2 * (q2 + 1) * n(y, 2)[3] / factorial(2)
g2_2 = q2 * (q2 + 1) * (q2 + 2) * n(y,3)[2] / factorial(3)
g3_2 = q2 * (q2 + 1) * (q2 + 2) * (q2 + 3) * n(y, 4)[1] / factorial(4)
g4_2 = q2 * (q2 + 1) * (q2 + 2) * (q2 + 3) * (q2 + 4) * n(y, 5)[0] / factorial(5)

r2 = g1_2 + g2_2 + g3_2 + g4_2

print("Newton's second interpolation =", r2)
