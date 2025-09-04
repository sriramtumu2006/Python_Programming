def palin(x):
    for i in range(1,x+1):
        n=i
        c=0
        while(i>0):
            r=i%10
            c=(c*10)+r
            i=i//10
        if(n==c):
            print(n,end=" ")
y=int(input("Enter a value"))
palin(y)
            