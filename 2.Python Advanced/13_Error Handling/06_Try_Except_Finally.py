# Finally function executes at the end of the function regardless of code running successfully or not.
# Even if we use exit code then also finally command will execute but python will terminate the program after that.

try :
    i = int(input("Enter your desired number: "))
    j = 1/i
    print(j)

except Exception as e :
    print(e)
    exit()
    
finally :
    print("Thank you for running the code.")

# As we are using exit command, Thanks will not be printed but finally command will be executed.

print("Thanks")