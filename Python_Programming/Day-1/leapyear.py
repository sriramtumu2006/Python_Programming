#check whether a year is leap year or not.
def leap(x):
    if (x%4==0 and x%100!=0) or x%400==0  :
        print("Leap Year.")
    else:
        print("Not leap year.") 
y=int(input("Enter year : "))
leap(y)