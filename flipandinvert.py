r = int(input("Enter number of rows:"))
c = int(input("Enter number of columns:"))
matrix = []
for i in range(r):
    matrix.append(list(map(int, input().split())))
for i in range(r):
    matrix[i] = matrix[i][::-1]
    for j in range(c):
        matrix[i][j] = 1-matrix[i][j]
for row in matrix:
    print(*row)
