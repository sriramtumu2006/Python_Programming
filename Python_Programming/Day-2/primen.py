def pr(x):
    for i in range(2,x):
        co=0
        for j in range(2,i+1):
            if(i%j==0):
                co+=1
        if co==1:
            print(i,end=" ")
n=int(input("Enter a number : "))
pr(n)