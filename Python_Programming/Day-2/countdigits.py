#count the number of digits using for loop.
def count(x):
    count=0
    while(x>0):
        count+=1
        x=x//10
    return count
n=int(input("Enter a number : "))
print(f"count of digits of {n} = {count(n)}")