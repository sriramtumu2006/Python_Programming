#check whether a number is prime or not using while loop.
def chprime(x):
    if(x<1):
        return "NOT Prime"
    else:
        co=0
        i=2
        while(x>=i):
            if(x%i==0):
                co+=1;
            else:
                i+=1
        if(co>1):
            return "Not Prime"
        else:
            return "Prime"
        
n=int(input("enter a number : "))
print(chprime(n))