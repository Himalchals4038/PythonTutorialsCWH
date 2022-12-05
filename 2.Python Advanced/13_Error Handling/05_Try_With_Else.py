from re import I


# Else function runs when python is able to run the program correctly.

try :
    i = int(input("Enter your desired number: "))
    j = 1/i
    print(j)
except Exception as e :
    print(e)
else :
    print("The code was run successfully !!")