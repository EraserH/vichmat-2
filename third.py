# Создать произвольную нижнетреугольную матрицу А 5 порядка (не унитреугольную),
# вектор B произвольный. Решить систему AX = B.
import numpy as np

lowA = np.array(
        [[1, 0, 0, 0, 0], [3, 2, 0, 0, 0], [4, 5, 3, 0, 0], [5, 2, 3, 1, 0],
         [4, 5, 2, 5, 3]], int)
print(f"\nmatrix lowA (нижняя треугольная матрица)  \n{lowA}")
vectorB = np.array([1, 2, 3, 4, 5])
print(f"\nvector B  \n{vectorB}")
result = np.linalg.solve(lowA, vectorB)
print(f"\nAX = B\n  \nX (linalg) = {result}")
invlowA = np.linalg.inv(lowA)
x = invlowA.dot(vectorB)
print(f"\nX (руками) = {x}")