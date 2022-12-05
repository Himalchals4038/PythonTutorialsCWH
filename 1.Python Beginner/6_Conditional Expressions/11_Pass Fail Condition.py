'''A test requires minimum 33% marks in individual subject and 40% in total to pass the exam
Accept input of 3 subjects from student and display whether he/she has passed or failed in exam.'''

m1 = int(input("Enter marks of student in Maths :"))
m2 = int(input("Enter marks of student in Chemistry :"))
m3 = int(input("Enter marks of student in Physics :"))

a1 = (m1/80)*100
a2 = (m2/80)*100
a3 = (m3/80)*100

b = (a1+a2+a3)/3

if (a1>=33 and a2>=33 and a3>=33):
    if (b>=40):
        print("The student has passed.")
    else:
        print("The student has failed.")
else:
    print("The student has failed.")
