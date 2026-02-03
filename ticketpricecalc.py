n=int(input("Enter the age"))
time=float(input("Enter show timing"))
ticketprice=0
if(n>13):
    if(time ==10.15 or time==18.80 or time==22.00):
        ticketprice=2
        print("Ticketprice:",ticketprice)
    else:
        ticketprice=1
        print("Ticketprice:",ticketprice)
else:
    ticketprice=1
    print("Ticket price:$",ticketprice)
    