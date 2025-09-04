#convert numbers to words.
def conv(x):
    if x=="1":
        return " one"
    elif x=="2":
        return " two"
    elif x=="3":
        return " three"
    elif x=="4":
        return " four"
    elif x=="5":
        return " five"
    elif x=="6":
        return " six"
    elif x=="7":
        return " seven"
    elif x=="8":
        return " eight"
    elif x=="9":
        return " nine"
    elif x=="0":
        return " zero"
    else:
        return " Invalid!"
n=int(input("Enter a number : "))
for i in str(n):
    print(conv(i),end=" ")