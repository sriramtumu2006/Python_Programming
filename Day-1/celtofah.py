#function with arguments and return type.
def fahr(x):
    f=(x*(9/5))+32
    return f
c=eval(input("Enter temperature in celsius :"))
fa=fahr(c)
print("Fahrenheit = ",fa)