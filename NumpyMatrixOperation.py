# Program for matrix operations using NumPy

import numpy as np

# Create matrices
matrix1 = np.array([
    [1, 2],
    [3, 4]
])

matrix2 = np.array([
    [5, 6],
    [7, 8]
])

# Addition
addition = matrix1 + matrix2

# Subtraction
subtraction = matrix1 - matrix2

# Multiplication
multiplication = np.dot(matrix1, matrix2)

# Inverse of first matrix
inverse_matrix1 = np.linalg.inv(matrix1)

# Display results
print("Matrix 1:\n", matrix1)

print("\nMatrix 2:\n", matrix2)

print("\nAddition:\n", addition)

print("\nSubtraction:\n", subtraction)

print("\nMultiplication:\n", multiplication)

print("\nInverse of Matrix 1:\n", inverse_matrix1)



#output:
Addition:
 [[ 6  8]
 [10 12]]

Subtraction:
 [[-4 -4]
 [-4 -4]]

Multiplication:
 [[19 22]
 [43 50]]