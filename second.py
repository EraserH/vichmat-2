# Создать две матрицы из случайных целых чисел из интервала [2,7) подходящего размера.
# Найти их произведение тремя способами:
# 1) записав скалярный алгоритм умножения матриц
# 2) записав векторный алгоритм, записав матрицу С
# 3) проверив с помощью функции np.dot.
import numpy as np

n: int
n, k, m = 4, 5, 6
A = np.random.randint(2, 7, (n, k))
print(f"\nmatrix A  \n{A}")
B = np.random.randint(2, 7, (k, m))
print(f"\nmatrix B  \n{B}")

# 1)
scalar_result = np.zeros((n, m), dtype=int)
for i in range(n):
    for j in range(m):
        for p in range(k):
            scalar_result[i, j] = scalar_result[i, j] + A[i, p] * B[p, j]
print(f"\nmatrix C (A*B скалярный алгоритм умножения матриц)  \n{scalar_result}")

# 2
vector_result = np.zeros((n, m), dtype=int)
for i in range(n):
    for j in range(m):
        vector_result[i, j] = np.dot(A[i, :], B[:, j])
print(f"\nmatrix C (A*B векторный алгоритм)  \n{vector_result}")
# 3
result = np.dot(A, B)
print(f"\nматрица C (A*B проверка с помощью функции np.dot)  \n{result}")

if np.array_equal(scalar_result, result) & np.array_equal(vector_result, result):
    print("Результаты сходятся")
else:
    print("Результаты расходятся")
