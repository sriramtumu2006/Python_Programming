#print the grades for marks use conditional statements
def grade(x):
    if x>80 and x<=100:
        return "Distension"
    elif x>70 and x<=80:
        return "A"
    elif x>50 and x<=70:
        return "B"
    elif x>40 and x<=50:
        return "C"
    elif x==40:
        return "P"
    elif x<40:
        return "Fail"
    else:
        return "Enter valid input"
m=int(input("Enter Marks : "))
print(grade(m))    
