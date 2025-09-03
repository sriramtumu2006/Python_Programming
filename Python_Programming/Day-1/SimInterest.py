#Calculate simple interest and total amount.
p=int(input("Enter the principal amount : "))
t=int(input("Enter the no of months : "))
r=int(input("Enter the rate of interest : "))
si=(p*t*r)/100
ta=p+si
print("Simple Interest = ",si)
print("Total Amount = ",ta)