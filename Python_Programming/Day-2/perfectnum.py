#print perfect numbers upto n digits.
def perfect(x):
    for i in range(1,x):
        n=i
        c=0
        for j in range(1,i):
            if(i%j==0):
                c+=j
        if(n==c):
            print(n,end=" ")
y=int(input("Enter a value : "))
perfect(y)
            