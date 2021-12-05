import numpy as np

#ex1
m1 = np.matrix([[2, 3, 1], [-1, 1, 0], [1, 2, -1]])
m2 = np.matrix([[1, 2, 1], [0, 1, 2], [3, 1, 1]])
i = m1 * m2
j = m2 * m1
ex1 = i - j
print("ex1(2) = ")
print(ex1)
print("------------------------------------------------------------------")
#ex2
m3 = np.matrix([[-1, 0, 2], [0, 1, 0], [1, 2, -1]])
print("ex2(2) = ")
print(np.linalg.matrix_power(m3, 2))
print("------------------------------------------------------------------")
#ex3
m4 = np.matrix([[5, 8, -4], [6, 9, -5], [4, 7, -3]])
m5 = np.matrix([[3, 2, 5], [4, -1, 3], [9, 6, 5]])
ex3 = m4 * m5
print("ex3(2) = ")
print(ex3)
print("------------------------------------------------------------------")
#ex4
m6 = np.matrix([[0, 2, 0], [3, 4, 5], [6, 7, 8]])
print("ex4(2) = ")
print(np.linalg.det(m6))
print("------------------------------------------------------------------")
#ex5
m7 = np.matrix([[2, 3, 4, 1], [1, 2, 3, 4], [3, 4, 1, 2], [4, 1, 2, 3]])
print("ex5(2) = ")
print(np.linalg.det(m7))
print("------------------------------------------------------------------")
#ex6
m8 = np.matrix([[2, 1, 0, 0], [3, 2, 0, 0], [1, 1, 3, 4], [2, -1, 2, 3]])
print("ex6(4) = ")
print(np.linalg.inv(m8))
print("------------------------------------------------------------------")
#ex7
m9 = np.matrix([[1, -1, 3, 4], [0, -1, 2, 1], [1, 1, -1, 2], [2, 3, -5, 3]])
print("ex7(2) = ")
print(np.linalg.matrix_rank(m9))
print("------------------------------------------------------------------")
#ex8
m10_A = np.matrix([[2, -1, 1], [3, 2, 2], [1, -2, 1]])
m10_B = np.matrix([[2], [-2], [1]])
A_det = np.linalg.det(m10_A)
X_m = np.matrix(m10_A)
X_m[:, 0] = m10_B
Y_m = np.matrix(m10_A)
Y_m[:, 1] = m10_B
Z_m = np.matrix(m10_A)
Z_m[:, 2] = m10_B
x = np.linalg.det(X_m) / A_det
y = np.linalg.det(Y_m) / A_det
z = np.linalg.det(Z_m) / A_det
print("ex8(2) = ")
print("x =", x, "\ny =", y, "\nz =", z)
print("------------------------------------------------------------------")
#ex9
m11_A = np.matrix([[1, -2, 3], [4, 2, -3], [3, -3, 5]])
m11_B = np.matrix([[-5], [0], [-9]])
# i11 = np.linalg.inv(m11_A)
# result = i11 * m11_B
#
# print("ex9(2) = ")
# print(result)
print("ex9(2) = ")
print(np.linalg.solve(m11_A, m11_B))
print("------------------------------------------------------------------")
#ex10(3)

nrows = 7
ncols = 6
a = np.random.randint(100, size=(nrows, ncols))
print("ex10(3) = ")
print("String sum = ", a.sum(axis=1)/2)
print("Column sum = ", a.sum(axis=0)/2)
