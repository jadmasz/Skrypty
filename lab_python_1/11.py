a = [1, 2, 12, 4]
b = [2, 4, 5, 8]
macierz=[[0 for x in range(len(a))] for y in range(len(b))]
for i in range(len(a)):
	for j in range(len(b)):
		macierz[i][j] = a[i]*b[j]

for line in macierz:
	print(line)
