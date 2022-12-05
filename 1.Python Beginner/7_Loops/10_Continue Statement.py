'''Continue command is used to stop the current iteration of the loop and continue with the next.
If a value satisfies continue python will not run the loop for that value and will move to the next one.'''

for i in range (10):
    print(i)
    if i == 5:
        continue
    print("Printed")
 # Here printed is not shown for 5 as the continue statement 
 # in between made python abort this loop and move to next one.