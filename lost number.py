l1=[1,2,3,4,5]
l2=[1,2,4,5]
sum1=0
sum2=0
for i in l1:
    sum1=sum1+i
for i in l2:
    sum2=sum2+i
print("Lost number",(sum1-sum2))