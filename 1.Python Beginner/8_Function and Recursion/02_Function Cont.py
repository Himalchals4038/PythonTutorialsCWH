'''Solve previous qustion using user-defined function.'''

def average(marks):
    p=(marks[0]+marks[1]+marks[2]+marks[3]+marks[4]+marks[5])/6
    return p

# average(marks) has been defined as the sum of marks of all 6 students divided by total number of students. 

def percent(marks):
    return ((marks[0]+marks[1]+marks[2]+marks[3]+marks[4]+marks[5])/600)*100

# percent(marks) has been defined as the sum of marks of all 6 students divided by total marks into 100.

marks1 = [84, 72, 69, 90, 98, 58]
average1 = average(marks1)
percentage1 = percent(marks1)
print("Average Marks of Section-A is: ", average1)
print("Percentage Marks of Section-A is: ", percentage1)

marks2 = [94, 98, 89, 82, 83, 99]
average2 = average(marks2)
percentage2 = percent(marks2)
print("Average Marks of Section-B is: ", average2)
print("Percentage Marks of Section-B is: ", percentage2)