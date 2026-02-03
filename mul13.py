n = int(input("Enter n:"))
num = 2
result = [num]
increment = 13
for i in range(1, n):
    num = num + increment
    result.append(num)
    increment += 13
print(result)
