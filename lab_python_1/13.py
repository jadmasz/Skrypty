import copy
import random
matrix_size = 8
matrix1 = [[0 for x in range(matrix_size)] for y in range(matrix_size)]
matrix2 = matrix1
matrix3 = matrix1
for x in range(matrix_size):
	for y in range(matrix_size):
		matrix1[x][y] = random.randint(0,1000)
		matrix2[x][y] = random.randint(0,1000)

for x in range(matrix_size):
	for y in range(matrix_size):
		for z in range(matrix_size):
			matrix3[x][y] = matrix3[x][y] + matrix1[x][z] * matrix2[z][y]

