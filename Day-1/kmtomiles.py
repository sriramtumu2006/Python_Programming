#function to convert km to miles with no arg and no return type.
def miles():
    k=eval(input("Enter distance in km : "))
    m=k*0.621
    print("KM = ",k,"miles = ",round(m,2))
miles()