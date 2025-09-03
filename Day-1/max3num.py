#Maximum of 3 numbers using nested-if.
def max3(x,y,z):
    if x>y:
        if x>z:
            print(x,"is big")
        else:
            print(z,"is big")
    else:
        if y>z:
            print(y,"is big")
        else:
            print(z,"is big")
a=int(input("Enter a value : "))
b=int(input("Enter b value : "))
c=int(input("Enter c value : "))
max3(a,b,c)