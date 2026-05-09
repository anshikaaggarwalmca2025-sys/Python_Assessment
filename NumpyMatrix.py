# Program for NumPy matrix operations

import numpy as np

# Create 5x5 matrix with random integers
matrix = np.random.randint(1, 100, (5, 5))

# Display matrix
print("Matrix:\n", matrix)

# Row-wise sum
row_sum = np.sum(matrix, axis=1)

# Column-wise sum
column_sum = np.sum(matrix, axis=0)

# Transpose of matrix
transpose_matrix = matrix.T

# Determinant of matrix
determinant = np.linalg.det(matrix)

# Display results
print("\nRow-wise Sum:\n", row_sum)

print("\nColumn-wise Sum:\n", column_sum)

print("\nTranspose of Matrix:\n", transpose_matrix)

print("\nDeterminant of Matrix:\n", determinant)



#output:
Matrix:
 [[12 45 78 23 56]
 [34 67 89 12 45]
 [23 56 90 11 44]
 [65 32 10 87 54]
 [22 44 66 88 99]]

Row-wise Sum:
 [214 247 224 248 319]

Column-wise Sum:
 [156 244 333 221 298]
