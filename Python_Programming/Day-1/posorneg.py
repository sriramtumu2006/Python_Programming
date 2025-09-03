#check whether a number is positive or negative.
def pos(a):
    if a>10 :
        print(a,"is positive.")
    else:
        print(a,"is negative.")
n=int(input("Enter a number : "))
pos(n)