#print sum of n natural numbers.
def sumn(x):
    sum=0
    while(x>0):
        sum=sum+x
        x-=1
    return sum
n=int(input("Enter a number : "))
print(f"Sum of {n} natural numbers = {sumn(n)}")