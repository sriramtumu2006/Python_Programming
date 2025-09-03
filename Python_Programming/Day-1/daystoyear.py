#function with arguments and no return type
def conv(x):
    y=x/365
    m=x//30
    print("Years : ",round(y,2),"Months : ",m)
d=int(input("Enter no of days : "))
conv(d)