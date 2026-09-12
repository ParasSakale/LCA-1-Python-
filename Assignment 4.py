# Write a Python program to create an array and perform addition of two matrices.
# (Using list and NumPy array).

#Using list
matrix_1 = [[1,2,3],
            [4,5,6],
            [7,8,9]]
matrix_2 = [[10, 11, 12],
           [13, 14, 15],
           [16, 17, 18]]
result = []

for i in range(len(matrix_1)):
    row = []
    for j in range(len(matrix_1[0])):
        sum_value = matrix_1[i][j] + matrix_2[i][j]
        row.append(sum_value)
    result.append(row)
print(result)

#Using NumPy
import numpy as np
np_matrix_1 = np.array(matrix_1)
np_matrix_2 = np.array(matrix_2)
np_result = np_matrix_1 + np_matrix_2
print(np_result)

