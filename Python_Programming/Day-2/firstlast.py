#print the first and last digit of a number using loops.
def fila(x):
    l=x%10
    while(x>0):
        f=x%10
        x=x//10
    return f,l
n=int(input("Enter a number : "))
fi,la=fila(n)
print(f"First digit = {fi}\nLast Digit = {la}")