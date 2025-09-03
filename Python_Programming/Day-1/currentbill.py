#Calculate current bill and print the details of the consumer
cNo=eval(input("Enter Consumer Number : "))
cName=input("Enter Consumer Name : ")
pmr=eval(input("Enter present month reading : "))
lmr=eval(input("Enter last month reading : "))
tu=pmr-lmr
cb=tu*3.80
print("Consumer No : ",cNo)
print("Consumer Name : ",cName)
print("Present Month Reading : ",pmr)
print("Last Month Reading : ",lmr)
print("Total Units : ",tu)
print("Current Bill : ",round(cb,2))