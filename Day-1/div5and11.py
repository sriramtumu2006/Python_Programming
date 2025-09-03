#Check whether a number is divisible by and 11 or not.
def divc(x):
    if x%5==0 and x%11==0:
        return True
    else:
        return False
a=int(input("Enter a number : "))
print("Is",a,"divisible by 5 and 11 ?",divc(a))
    