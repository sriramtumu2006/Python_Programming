#check whether the input is alphabet,digit or special character.use condition statements.
def check(x):
    if x.isalpha():
        return "Alphabet"
    elif x.isdigit():
        return "Digit"
    else:
        return "Special Character"
y=input("Enter input : ")
print(check(y))        