#factorial of a number using loops.
def fact(x):
    f=1
    while x>1:
        f=f*x
        x-=1
    return f
n=int(input("Enter a number : "))
print(f"Factorial of {n} = {fact(n)}")
        