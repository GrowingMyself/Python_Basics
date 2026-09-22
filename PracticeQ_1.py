##Write a Python program to accept the marks of a student in 5 subjects and calculate the student's total marks, percentage, grade, and result.
##The program should follow these conditions:
##Accept marks for 5 subjects from the user.
##Calculate the total marks.
##Calculate the percentage.
##If the student's score is less than 35 in any subject, the student has failed.
##If the student passes in all subjects, assign a grade based on the percentage:
##75% and above → Distinction
##60% to 74% → First Class
##50% to 59% → Second Class
##35% to 49% → Pass.
#->That question is asked in infosys coding round.

Subject1=int(input("Enter the marks of 1st sub :"))
Subject2=int(input("Enter the marks of 1st sub :"))
Subject3=int(input("Enter the marks of 1st sub :"))
Subject4=int(input("Enter the marks of 1st sub :"))
Subject5=int(input("Enter the marks of 1st sub :"))

totalmarks=Subject1+Subject2+Subject3+Subject4+Subject5

percentage=totalmarks/5

if Subject1<35 or Subject2<35 or Subject3<35 or Subject4<35 or Subject5<35:
    grade="fail"
    result="fail"
else:
    result="Pass"
    
if percentage>=75:
    grade="Distintion"
elif percentage>=60:
    grade="First class"
elif percentage>=50:
    grade="Second class"
else:
    grade="Pass"

print("Total Marks :",totalmarks)
print("percentage :",percentage)
print("grade :",grade)
print("result :",result)





    
       

