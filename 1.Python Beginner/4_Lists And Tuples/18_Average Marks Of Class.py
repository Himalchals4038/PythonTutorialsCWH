m1 = input("Enter Marks of Student 1 : ")
m2 = input("Enter Marks of Student 2 : ")
m3 = input("Enter Marks of Student 3 : ")
m4 = input("Enter Marks of Student 4 : ")
m5 = input("Enter Marks of Student 5 : ")
m6 = input("Enter Marks of Student 6 : ")
m7 = input("Enter Marks of Student 7 : ")

m1 = int(m1)
m2 = int(m2)
m3 = int(m3)
m4 = int(m4)
m5 = int(m5)
m6 = int(m6)
m7 = int(m7)

MarksList = [m1, m2, m3, m4, m5, m6, m7]
print("The Marks List is: ", MarksList)
a1 = (m1 + m2 + m3 + m4 + m5 + m6 + m7)/7
print("Class Average: ", a1)

m4 = m4 + 7
m5 = m5 + 5

UpdatedMarksList = [m1, m2, m3, m4, m5, m6, m7]
print("The Updated Marks List is: ", UpdatedMarksList)
a2 = (m1 + m2 + m3 + m4 + m5 + m6 + m7)/7
print("New Class Average: ", a2)

