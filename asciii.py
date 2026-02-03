r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

matrix = []
for i in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)

for j in range(c):
    max_col = matrix[0][j]
    for i in range(1, r):
        if matrix[i][j] > max_col:
            max_col = matrix[i][j]
    print(max_col)
