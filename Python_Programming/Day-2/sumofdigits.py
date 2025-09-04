#calculate the sum of digits using for loop.
def sumd(x):
    sum=0
    for i in range(1,len(str(x))+1):
        r=x%10
        sum=sum+r
        x=x//10
    return sum
n=int(input("Enter a number : "))
print(f"Sum of digits of {n} = {sumd(n)}")