import random
import math
def W(matrix):
	if len(matrix) == 1:
		return matrix[0][0]
	else:
		A = 0
		for x in range(len(matrix)):
			try:
				new_matrix = matrix[:x] + matrix[x+1:]
			except IndexError:
				pass
			for i in range (len(new_matrix)):
				new_matrix[i] = new_matrix[i][1:]
			A = A + math.pow(-1, 2+x) * matrix[x][0] * W(new_matrix)
		return A

matrix_size = random.randint(3,10)
print("Matrix size = %d" % matrix_size)
matrix1 = [[0 for x in range(matrix_size)] for y in range(matrix_size)]
for x in range(matrix_size):
	for y in range(matrix_size):
		matrix1[x][y] = random.randint(0,9)

print("Generated matrix: ")
for x in matrix1: print(x)

print("W = %d" % W(matrix1))
