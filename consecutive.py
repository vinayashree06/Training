num = list(map(int, input("Enter the list:").split()))
num.sort()
flag = 1
for i in range(1, len(num)):
    if num[i]!=num[i-1] + 1:
        flag = 0
        break
print(flag)


