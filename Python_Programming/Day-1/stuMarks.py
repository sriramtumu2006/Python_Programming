#print student deatils with total and avg marks in 3 subjects
sNo=int(input("Enter the student number : "))
sName=input("Enter the student name : ")
sub1=int(input("Enter the subject 1 marks : "))
sub2=int(input("Enter the subject 2 marks : "))
sub3=int(input("Enter the subject 3 marks : "))
tot=sub1+sub2+sub3
avg=tot/3
print("Student No : ",sNo)
print("Student Name : ",sName)
print("Subject 1 Marks : ",sub1)
print("Subject 2 Marks : ",sub2)
print("Subject 3 Marks : ",sub3)
print("Total Marks : ",tot)
print("Average Marks : ",round(avg,2))