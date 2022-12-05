'''Accept the marks of a student and accordingly report his/her grading.'''

m = int(input("Enter your marks: "))

if (m>90):
    print("Grade: Excellent !!")
elif (90>=m>80):
    print("Grade: A")
elif (80>=m>70):
    print("Grade: B")
elif (70>=m>60):
    print("Grade: C")
elif (60>=m>50):
    print("Grade: D")
elif (50>=m>40):
    print( "Grade: E")
else:
    print("Grade: F")