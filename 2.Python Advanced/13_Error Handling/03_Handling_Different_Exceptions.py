# Program to input an integer and find its reciprocal. If error is found, state type of error and give suggestion for proper input.

try :
    a = int(input("Enter your desired number: "))
    c = 1/a
    print(c)

except ZeroDivisionError as e :
    print("Error Code 1 occured: Make sure you are not dividing by 0.")
except ValueError as e :
    print("Error Code 2 occured: Make sure you have entered an integer type value only.")
except SyntaxError as e :
    print("Error Code 3 occured: Make sure you have entered only integers.")
except NameError as e :
    print("Error Code 4 occured: Make sure you have entered an integer.")
except TypeError as e :
    print("Error Code 5 occured: Make sure you have entered all inputs as integers.")
