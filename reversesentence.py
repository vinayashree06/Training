s = input("Enter the string: ")
i = 0
while i < len(s) and s[i]!=' ':
    i+=1
j=len(s)-1
while j>=0 and s[j]!=' ':
    j-=1
first= s[:i]
middle = s[i:j+1]
last = s[j+1:]
result = last + middle + first
print(result)
