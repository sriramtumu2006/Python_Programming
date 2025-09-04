#print n natural numbers using loops.
def nat(n):
    i=1
    while(i<=n):
        print(i,end=" ")
        i+=1
num=int(input("Enter a number : "))
nat(num)