#perform arithmetic operations using functions
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def mod(x,y):
    return x%y
a=eval(input("Enter a value : "))
b=eval(input("Enter b value : "))
print(f"{a} + {b} = {add(a,b)}")
print(f"{a} - {b} = {sub(a,b)}")
print(f"{a} * {b} = {mul(a,b)}")
print(f"{a} / {b} = {div(a,b)}")
print(f"{a} % {b} = {mod(a,b)}")
