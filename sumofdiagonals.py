
n=int(input())
matrix=[list(map(int,input().split())) for _ in range(n)]
p=0
s=0
for i in range(n):
    p+=matrix[i][i]
    s+=matrix[i][n-1-i]
print(p,s)