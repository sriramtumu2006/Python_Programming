#Print the current bill for given units use conditional statements
def cubill(tu):
    if tu>0 and tu<=50:
        return tu*3.80
    elif tu>51 and tu<=100:
        return (50*3.80)+(tu-50)*4.20
    elif tu>100 and tu<=200:
        return (50*3.80)+(50*4.20)+(tu-100)*5.10
    elif tu>200 and tu<=300:
        return (50*3.80)+(50*4.20)+(100*5.10)+(tu-200)*6.30
    elif tu>300: 
        return (50*3.80)+(50*4.20)+(100*5.10)+(200*6.30)+(tu-300)*7.50
    else:
        return "Invalid Input!"
y=int(input("Enter total units : "))
print("Current Bill : ",cubill(y))
    