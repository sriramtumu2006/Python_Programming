#Factors of a number.
def chprime(t):
    if(t==1):
        return False
    co=0
    for i in range(2,t+1):
        if(t%i==0):
            co+=1;
    if(co>1):
        return False
    else:
        return True
def factor(x):
    for i in range(1,x+1):
        if(x%i==0 and chprime(i)==True):
            print(i,end=" ")
y=int(input("Enter a value : "))
factor(y)
            
            