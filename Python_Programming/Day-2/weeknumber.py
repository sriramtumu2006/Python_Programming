#print the day for the week number
def week(x):
    if x==1 :
        return "Sunday"
    elif x==2:
        return "Monday"
    elif x==3:
        return "Tuesday"
    elif x==4:
        return "Wednesday"
    elif x==5:
        return "Thursday"
    elif x==6:
        return "Friday"
    elif x==7:
        return "Saturday"
    else:
        return "Invalid Input!Please enter between 1 to 7"
wn=int(input("Enter week number : "))
print(week(wn))