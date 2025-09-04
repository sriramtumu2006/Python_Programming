#print strong numbers from 1 to n.
def fact(x):
    f=1
    while x>1:
        f=f*x
        x-=1
    return f
def strong(x):
    for i in range(1,x):
        n=i
        c=0
        while(i>0):
            r=i%10
            c+=fact(r)
            i=i//10
        if(n==c):
            print(n)
y=int(input("Enter a value : "))
strong(y)
        
            