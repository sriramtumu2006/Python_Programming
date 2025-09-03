#check whether a number is even or odd.
def check(x):
    if x%2==0 :
        print(x,"is Even")
    else:
        print(x,"is Odd")
a=int(input("Enter a number : "))
check(a)