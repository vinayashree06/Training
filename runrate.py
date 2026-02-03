n=int(input("Enter number of overs:"))
o1=95.0
i1=20.5
l1=[]
l1.append(o1)
for i in range(1,n+1): 
    l1.append(o1+i1)
    o1=l1[i]
print(l1)