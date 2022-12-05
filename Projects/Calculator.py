
while True :
    
    print("Press q to quit.")
    
    print("Type 1 for Addition \n\
    Type 2 for Substraction \n\
    Type 3 for Multiplication \n\
    Type 4 for Division")

    c = input("Enter your choice: ")

    if c == 'q' :
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    try:
        c = int(c)

        if c == 1 :
            print(f"Your result is {a+b}")
        elif c == 2 :
            print(f"Your result is {a-b}")
        elif c == 3 :
            print(f"Your result is {a*b}")
        elif c == 4 :
            print(f"Your result is {a/b}")
        else :
            print("Please input correct value !!")

    except Exception as e :
        print(f"Please input choices among 1, 2, 3, 4. Your input resulted in an error {e}")

print("Thanks for using the calculator !!")