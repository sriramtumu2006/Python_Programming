#check whether a character is alphabet or not.
def alph(x):
    if x.isalpha():
        print(x,"is alphabet")
    else:
        print(x,"is not alphabet")
a=input("Enter a character : ")
alph(a)