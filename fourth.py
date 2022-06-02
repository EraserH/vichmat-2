# Решить систему, используя LU разложение

import numpy as np

A = np.array([[8.2, -3.2, 14.2, 14.8],
             [5.6, -12, 15, -6.4],
             [5.7, 3.6, -12.4, -2.3],
             [6.8, 13.2, -6.3, -8.7]], float)
B = np.array([-8.4, 4.5, 3.3, 14.3])
n = 4
A1 = A.copy()
U = np.zeros((n, n), float)
L = np.identity(n, float)
for i in range(n):
    for j in range(n):
        if i <= j:
            U[i, j] = A1[i, j] - np.dot(L[i, :i], U[:i, j])
        if i > j:
            L[i, j] = (A1[i, j] - np.dot(L[i, :j], U[:j, j])) / U[j, j]

print(f"\nmatrix A1  \n{A1}")

invL = np.linalg.inv(L)
y = invL.dot(B)
invU = np.linalg.inv(U)
x = invU.dot(y)
print(x)