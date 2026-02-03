n = int(input("Enter n:"))
a = 1
b = 3
c=4
print(a, b,c, end=" ")
for i in range(2, n):
    d = a + b+c
    print(d, end=" ")
    a=b
    b=c
    c=d
