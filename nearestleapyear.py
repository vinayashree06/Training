n=int(input("Enter year: "))
if(n%4==0):
    print("Upcoming nearest leap year",n)
elif(n%4==1):
    print("Upcoming nearest leap year",n+3)
elif(n%4==2):
    print("Upcoming nearest leap year",n+2)
else:
    print("Upcoming nearest leap year",n+1)