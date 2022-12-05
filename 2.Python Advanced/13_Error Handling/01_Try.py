# while (True) :
#     print("Press q to quit.")
#     a = input("Enter a number: ")
    
#     if a == 'q' :
#         break
#     a = int(a)

#     if a > 6 :
#         print("The entered number is greater than 6.")

# print("Thanks for running the code !!")
# If anything other can q or integer is written in input then GUI will crash.

# Try command tries to see if the code is runnable else it runs the except sequence. 

while (True) :
    print("Press q to quit.")
    a = input("Enter a number: ")
    
    if a == 'q' :
        break

    try :
        print("Trying...")
        a = int(a)
        if a > 6 :
            print("The entered number is greater than 6.")

    except Exception as e :
        print(f"Your input resulted in an error: {e}")

print("Thanks for running the code !!")