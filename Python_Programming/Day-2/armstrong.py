#print armstrong numbers upto n.
def arms(x):
    t=n=x
    c=0
    k=0
    while(x>0):
        c+=1
        x=x//10
    while(n>0):
        r=n%10
        k+=r**c
        n=n//10
    if(t==k):
        print("Armstrong")
    else:
        print("Not Armstrong")
y=int(input("Enter a value : "))
arms(y)