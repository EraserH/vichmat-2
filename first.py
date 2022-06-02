# Вариант 22
# Создать квадратную матрицу из случайных вещественных чисел из (2,4) размера 10 .
# Найти скалярное произведение 4 строки на 5 столбец. Использовать срезы матриц.
import numpy as np

matrix = np.random.uniform(2, 4, (10, 10))
print(matrix)
result = matrix[3, :] * matrix[:, 4]
print("Результат: ")
print(result)
