m=int(raw_input("Enter The Marks Obtained in Maths 1 : "))
sc=int(raw_input("Enter The Marks Obtained in Science : "))
sst=int(raw_input("Enter The Marks Obtained in Social Studies : "))
eng=int(raw_input("Enter The Marks Obtained in English : "))
ip=int(raw_input("Enter The Marks Obtained in IP :"))
sum=(m+sc+sst+eng+ip)
print("Total Marks Obtained : ")
print sum
mean=float(sum/5)
print("Mean Of Marks Obtained is : ")
print mean
p=float((sum*100)/500)
print("Percentage Obtained is : ")
print p
if (p>35):
    print("Student Passes in the Exams")
else :
    print("Student Fails In the Exams")
